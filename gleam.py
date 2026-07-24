"""
gleam.py — mitmproxy/mitmweb addon for tracking Grammarly endpoint behavior.

Usage:
    mitmweb -s gleam.py

Configurable options (set via mitmweb CLI, e.g. --set gleam_batch_size=500):
    gleam_db_path          str   default "gleam.db"
    gleam_grammarly_only   bool  default True
    gleam_batch_size       int   default 200
    gleam_summary_path     str   default "gleam_summary"
    gleam_flush_interval   float default 5.0   (seconds, periodic flush safety net)
    gleam_summary_interval float default 10.0  (seconds between auto live-summary refreshes; 0 disables)
    gleam_snippet_length   int   default 500   (chars kept for non-JSON body snippets)

While mitmweb is running, gleam auto-refreshes a live summary every
gleam_summary_interval seconds, overwriting:
    gleam_summary_live.json   — machine-readable
    gleam_summary_live.txt    — human-readable, ranked by call volume

You can also trigger an on-demand, timestamped snapshot anytime via the
mitmweb command bar: gleam.summary

On shutdown (mitmweb quits / addon unloaded), gleam:
    1. Flushes any buffered rows to SQLite.
    2. Writes a full SQL dump: gleam_dump_<timestamp>.sql
    3. Writes a final timestamped summary: gleam_summary_<timestamp>.json/.txt
    4. Closes the DB connection cleanly.

Tables:
    rpc_calls          — JSON-RPC request/response pairs (the main table)
    http_flows_other    — non-JSON / non-JSON-RPC HTTP traffic (lightweight)
    ws_flows            — WebSocket connection summaries
"""

import json
import sqlite3
import time
from collections import Counter
from datetime import datetime, timedelta

from mitmproxy import ctx, http

DDL = """
CREATE TABLE IF NOT EXISTS rpc_calls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp_request REAL,
    timestamp_response REAL,
    http_method TEXT,
    scheme TEXT,
    host TEXT,
    path TEXT,
    status_code INTEGER,
    jsonrpc_version TEXT,
    rpc_method TEXT,
    rpc_id TEXT,
    params_json TEXT,
    result_json TEXT,
    error_json TEXT,
    request_headers_json TEXT,
    response_headers_json TEXT,
    latency_ms REAL,
    token_location TEXT,
);

CREATE TABLE IF NOT EXISTS http_flows_other (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp_request REAL,
    timestamp_response REAL,
    http_method TEXT,
    scheme TEXT,
    host TEXT,
    path TEXT,
    status_code INTEGER,
    content_type TEXT,
    request_body_snippet TEXT,
    response_body_snippet TEXT
);

CREATE TABLE IF NOT EXISTS ws_flows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp_open REAL,
    timestamp_close REAL,
    scheme TEXT,
    host TEXT,
    path TEXT,
    message_count INTEGER,
    direction_counts_json TEXT
);

CREATE INDEX IF NOT EXISTS idx_rpc_host_path_method
    ON rpc_calls(host, path, rpc_method);
CREATE INDEX IF NOT EXISTS idx_rpc_ts_request
    ON rpc_calls(timestamp_request);
CREATE INDEX IF NOT EXISTS idx_other_host_path
    ON http_flows_other(host, path);
"""

GRAMMARLY_DOMAIN_MARKERS = ("grammarly.com", "grammarly.io", "grammarly.net")


def _is_grammarly_host(host: str) -> bool:
    if not host:
        return False
    host = host.lower()
    return any(marker in host for marker in GRAMMARLY_DOMAIN_MARKERS)


def _safe_json_loads(text):
    if not text:
        return None
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        return None


def _headers_subset_json(headers) -> str:
    # Store the full header set as JSON text (no masking in v1, per design doc:
    # sensitive data capture is expected/desired for this research project).
    try:
        return json.dumps(dict(headers))
    except Exception:
        return "{}"


class Gleam:
    def __init__(self):
        self.conn = None
        self.rpc_buffer = []
        self.other_buffer = []
        self.ws_buffer = []
        self.unique_http_endpoints = set()   # (host, path)
        self.unique_rpc_endpoints = set()    # (host, path, rpc_method)
        self.rpc_hit_counts = Counter()      # (host, path, rpc_method) -> count
        self.http_hit_counts = Counter()     # (host, path) -> count
        self.status_counts = Counter()       # status_code -> count
        self.rpc_call_total = 0
        self.other_flow_total = 0
        self.ws_conn_total = 0
        self.session_start = time.time()
        self._last_flush = time.time()
        self._last_summary = time.time()
        # ws tracking keyed by flow.id -> dict of running state
        self._ws_state = {}

    # ------------------------------------------------------------------
    # Setup / config
    # ------------------------------------------------------------------
    def load(self, loader):
        loader.add_option(
            name="gleam_db_path", typespec=str, default="gleam.db",
            help="Path to the gleam SQLite database file.",
        )
        loader.add_option(
            name="gleam_grammarly_only", typespec=bool, default=True,
            help="Only fully process flows whose host matches Grammarly domains.",
        )
        loader.add_option(
            name="gleam_batch_size", typespec=int, default=200,
            help="Number of buffered rows before an automatic batch insert.",
        )
        loader.add_option(
            name="gleam_summary_path", typespec=str, default="gleam_summary",
            help="Filename prefix for the unique-endpoints summary file.",
        )
        loader.add_option(
            name="gleam_flush_interval", typespec=float, default=5.0,
            help="Seconds between periodic safety-net buffer flushes.",
        )
        loader.add_option(
            name="gleam_summary_interval", typespec=float, default=10.0,
            help="Seconds between automatic live-summary refreshes (0 disables auto-refresh).",
        )
        loader.add_option(
            name="gleam_snippet_length", typespec=int, default=500,
            help="Max characters kept for non-JSON request/response body snippets.",
        )

    def running(self):
        # Called once mitmproxy is fully up; options are guaranteed to be set.
        db_path = ctx.options.gleam_db_path
        self.conn = sqlite3.connect(db_path, isolation_level=None)  # autocommit off manually
        self.conn.execute("PRAGMA journal_mode=WAL;")
        self.conn.executescript(DDL)
        ctx.log.info(f"[gleam] database ready at {db_path}")

    # ------------------------------------------------------------------
    # HTTP hooks
    # ------------------------------------------------------------------
    def request(self, flow: http.HTTPFlow):
        # Nothing persisted yet at request time — we finalize everything in
        # response() where both sides are available. This keeps correlation
        # trivial (flow object is the same instance across hooks) and avoids
        # a separate in-memory join table.
        pass

    def response(self, flow: http.HTTPFlow):
        host = flow.request.pretty_host
        path = flow.request.path.split("?")[0]

        if ctx.options.gleam_grammarly_only and not _is_grammarly_host(host):
            return

        self.unique_http_endpoints.add((host, path))

        content_type = flow.request.headers.get("Content-Type", "") or ""
        req_json = None
        if "json" in content_type.lower() or self._looks_like_json(flow.request.text):
            req_json = _safe_json_loads(flow.request.text)

        is_rpc = isinstance(req_json, dict) and "method" in req_json and (
            "jsonrpc" in req_json or "id" in req_json or "params" in req_json
        )

        ts_req = flow.request.timestamp_start
        ts_resp = flow.response.timestamp_end if flow.response else None
        latency_ms = None
        if ts_req and ts_resp:
            latency_ms = (ts_resp - ts_req) * 1000.0

        if is_rpc:
            resp_json = _safe_json_loads(flow.response.text) if flow.response else None
            result = resp_json.get("result") if isinstance(resp_json, dict) else None
            error = resp_json.get("error") if isinstance(resp_json, dict) else None
            rpc_method = req_json.get("method")

            self.unique_rpc_endpoints.add((host, path, rpc_method))
            self.rpc_hit_counts[(host, path, rpc_method)] += 1
            self.rpc_call_total += 1
            if flow.response:
                self.status_counts[flow.response.status_code] += 1

            row = (
                ts_req,
                ts_resp,
                flow.request.method,
                flow.request.scheme,
                host,
                path,
                flow.response.status_code if flow.response else None,
                req_json.get("jsonrpc"),
                rpc_method,
                json.dumps(req_json.get("id")),
                json.dumps(req_json.get("params")),
                json.dumps(result) if result is not None else None,
                json.dumps(error) if error is not None else None,
                _headers_subset_json(flow.request.headers),
                _headers_subset_json(flow.response.headers) if flow.response else "{}",
                latency_ms,
                token_loc,
            )

            #citation: claude 7/24/26
            token_loc = None
            req_headers = flow.request.headers
            if any(k.lower() == "authorization" for k in req_headers.keys()):
                token_loc = "header"
            elif req_json and "token" in json.dumps(req_json).lower():
                token_loc = "body"
            self.rpc_buffer.append(row)
        else:
            snip_len = ctx.options.gleam_snippet_length
            req_snip = (flow.request.text or "")[:snip_len]
            resp_snip = (flow.response.text or "")[:snip_len] if flow.response else ""
            row = (
                ts_req,
                ts_resp,
                flow.request.method,
                flow.request.scheme,
                host,
                path,
                flow.response.status_code if flow.response else None,
                flow.response.headers.get("Content-Type", "") if flow.response else "",
                req_snip,
                resp_snip,
            )
            self.other_buffer.append(row)
            self.http_hit_counts[(host, path)] += 1
            self.other_flow_total += 1
            if flow.response:
                self.status_counts[flow.response.status_code] += 1

        self._maybe_flush()

    def error(self, flow: http.HTTPFlow):
        # Connection-level errors never reach response() — still record them
        # so we "don't throw the data away."
        host = flow.request.pretty_host
        if ctx.options.gleam_grammarly_only and not _is_grammarly_host(host):
            return
        path = flow.request.path.split("?")[0]
        row = (
            flow.request.timestamp_start,
            None,
            flow.request.method,
            flow.request.scheme,
            host,
            path,
            None,
            "",
            f"[connection error: {flow.error}]",
            "",
        )
        self.other_buffer.append(row)
        self._maybe_flush()

    @staticmethod
    def _looks_like_json(text):
        if not text:
            return False
        stripped = text.strip()
        return stripped.startswith("{") or stripped.startswith("[")

    # ------------------------------------------------------------------
    # WebSocket hooks
    # ------------------------------------------------------------------
    def websocket_start(self, flow: http.HTTPFlow):
        host = flow.request.pretty_host
        if ctx.options.gleam_grammarly_only and not _is_grammarly_host(host):
            return
        self._ws_state[flow.id] = {
            "timestamp_open": time.time(),
            "scheme": flow.request.scheme,
            "host": host,
            "path": flow.request.path.split("?")[0],
            "client_to_server": 0,
            "server_to_client": 0,
        }
        self.unique_http_endpoints.add((host, self._ws_state[flow.id]["path"]))

    def websocket_message(self, flow: http.HTTPFlow):
        state = self._ws_state.get(flow.id)
        if state is None:
            return
        last = flow.websocket.messages[-1]
        if last.from_client:
            state["client_to_server"] += 1
        else:
            state["server_to_client"] += 1

    def websocket_end(self, flow: http.HTTPFlow):
        state = self._ws_state.pop(flow.id, None)
        if state is None:
            return
        msg_count = state["client_to_server"] + state["server_to_client"]
        row = (
            state["timestamp_open"],
            time.time(),
            state["scheme"],
            state["host"],
            state["path"],
            msg_count,
            json.dumps({
                "client_to_server": state["client_to_server"],
                "server_to_client": state["server_to_client"],
            }),
        )
        self.ws_buffer.append(row)
        self.ws_conn_total += 1
        self.http_hit_counts[(state["host"], state["path"])] += 1
        self._maybe_flush()

    # ------------------------------------------------------------------
    # Batching / persistence
    # ------------------------------------------------------------------
    def tick(self):
        # Periodic safety-net flush so data isn't lost if mitmweb is killed
        # ungracefully and a buffer hasn't hit its size threshold yet.
        flush_interval = getattr(ctx.options, "gleam_flush_interval", 5.0)
        if time.time() - self._last_flush >= flush_interval:
            self._flush(force=True)

        # Periodic auto-refresh of the live summary (overwrites a stable
        # filename so you don't accumulate a new file every tick).
        summary_interval = getattr(ctx.options, "gleam_summary_interval", 10.0)
        if summary_interval and time.time() - self._last_summary >= summary_interval:
            self._write_summary("gleam_summary_live")
            self._last_summary = time.time()

    def _maybe_flush(self):
        batch_size = ctx.options.gleam_batch_size
        if (
            len(self.rpc_buffer) >= batch_size
            or len(self.other_buffer) >= batch_size
            or len(self.ws_buffer) >= batch_size
        ):
            self._flush()

    def _flush(self, force=False):
        if not (self.rpc_buffer or self.other_buffer or self.ws_buffer):
            self._last_flush = time.time()
            return
        if self.conn is None:
            return

        if self.rpc_buffer:
            self.conn.executemany(
                """INSERT INTO rpc_calls (
                    timestamp_request, timestamp_response, http_method, scheme,
                    host, path, status_code, jsonrpc_version, rpc_method, rpc_id,
                    params_json, result_json, error_json,
                    request_headers_json, response_headers_json, latency_ms, token_location
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                self.rpc_buffer,
            )

        if self.other_buffer:
            self.conn.executemany(
                """INSERT INTO http_flows_other (
                    timestamp_request, timestamp_response, http_method, scheme,
                    host, path, status_code, content_type,
                    request_body_snippet, response_body_snippet
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                self.other_buffer,
            )
            self.other_buffer.clear()

        if self.ws_buffer:
            self.conn.executemany(
                """INSERT INTO ws_flows (
                    timestamp_open, timestamp_close, scheme, host, path,
                    message_count, direction_counts_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                self.ws_buffer,
            )
            self.ws_buffer.clear()

        self.conn.commit()
        self._last_flush = time.time()

    # ------------------------------------------------------------------
    # Live + final summary of unique Grammarly endpoints
    # ------------------------------------------------------------------
    def _build_summary_dict(self):
        rpc_endpoints = sorted(
            (
                {"host": h, "path": p, "rpc_method": m, "hits": self.rpc_hit_counts[(h, p, m)]}
                for h, p, m in self.unique_rpc_endpoints
            ),
            key=lambda x: -x["hits"],
        )
        http_endpoints = sorted(
            (
                {"host": h, "path": p, "hits": self.http_hit_counts[(h, p)]}
                for h, p in self.unique_http_endpoints
                if (h, p) not in {(r["host"], r["path"]) for r in rpc_endpoints}
            ),
            key=lambda x: -x["hits"],
        )
        elapsed = time.time() - self.session_start
        return {
            "generated_at": datetime.now().isoformat(),
            "session_duration": str(timedelta(seconds=int(elapsed))),
            "totals": {
                "rpc_calls": self.rpc_call_total,
                "other_http_flows": self.other_flow_total,
                "websocket_connections": self.ws_conn_total,
                "unique_rpc_endpoints": len(self.unique_rpc_endpoints),
                "unique_http_endpoints": len(self.unique_http_endpoints),
            },
            "status_code_counts": dict(sorted(self.status_counts.items(), key=lambda kv: str(kv[0]))),
            "rpc_endpoints": rpc_endpoints,
            "other_http_endpoints": http_endpoints,
        }

    def _render_pretty_text(self, summary):
        lines = []
        lines.append("=" * 60)
        lines.append("  GLEAM — Grammarly Endpoint Summary")
        lines.append("=" * 60)
        lines.append(f"  Generated:        {summary['generated_at']}")
        lines.append(f"  Session duration: {summary['session_duration']}")
        lines.append("-" * 60)
        t = summary["totals"]
        lines.append("  Totals")
        lines.append(f"    RPC calls captured:        {t['rpc_calls']}")
        lines.append(f"    Other HTTP flows captured: {t['other_http_flows']}")
        lines.append(f"    WebSocket connections:     {t['websocket_connections']}")
        lines.append(f"    Unique RPC endpoints:      {t['unique_rpc_endpoints']}")
        lines.append(f"    Unique HTTP endpoints:     {t['unique_http_endpoints']}")
        if summary["status_code_counts"]:
            status_str = ", ".join(f"{k}: {v}" for k, v in summary["status_code_counts"].items())
            lines.append(f"    Status codes:              {status_str}")
        lines.append("-" * 60)

        lines.append(f"  RPC endpoints (by call volume)")
        if summary["rpc_endpoints"]:
            for e in summary["rpc_endpoints"]:
                lines.append(f"    [{e['hits']:>4}x]  {e['host']}{e['path']}  ->  {e['rpc_method']}")
        else:
            lines.append("    (none yet)")

        lines.append("-" * 60)
        lines.append(f"  Other Grammarly endpoints (non-JSON-RPC)")
        if summary["other_http_endpoints"]:
            for e in summary["other_http_endpoints"]:
                lines.append(f"    [{e['hits']:>4}x]  {e['host']}{e['path']}")
        else:
            lines.append("    (none yet)")
        lines.append("=" * 60)
        return "\n".join(lines)

    def _write_summary(self, path_prefix):
        summary = self._build_summary_dict()
        json_path = f"{path_prefix}.json"
        txt_path = f"{path_prefix}.txt"
        with open(json_path, "w") as f:
            json.dump(summary, f, indent=2)
        with open(txt_path, "w") as f:
            f.write(self._render_pretty_text(summary))
        return json_path, txt_path

    def summary(self):
        """
        mitmproxy command: gleam.summary
        Writes the current unique-endpoints summary (JSON + readable text)
        without stopping capture. Run from the mitmweb command palette
        anytime you want an on-demand snapshot, separate from the
        auto-refreshing gleam_summary_live files.
        """
        self._flush(force=True)
        prefix = ctx.options.gleam_summary_path
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        json_path, txt_path = self._write_summary(f"{prefix}_{ts}")
        ctx.log.info(f"[gleam] snapshot written to {txt_path} (+ {json_path})")

    # ------------------------------------------------------------------
    # Shutdown
    # ------------------------------------------------------------------
    def done(self):
        self._flush(force=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Final unique-endpoints summary
        prefix = ctx.options.gleam_summary_path if self.conn else "gleam_summary"
        json_path, txt_path = self._write_summary(f"{prefix}_{ts}")

        # Full SQL dump for later ad-hoc querying
        if self.conn is not None:
            dump_path = f"gleam_dump_{ts}.sql"
            with open(dump_path, "w") as f:
                for line in self.conn.iterdump():
                    f.write(f"{line}\n")
            self.conn.close()
            ctx.log.info(f"[gleam] SQL dump written to {dump_path}")

        ctx.log.info(f"[gleam] final summary written to {txt_path} (+ {json_path})")
        ctx.log.info("\n" + self._render_pretty_text(self._build_summary_dict()))


addons = [Gleam()]
