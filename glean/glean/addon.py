"""
GLEAN mitmproxy addon (design doc §5.1).

Filters to Grammarly-owned domains, detects JSON-RPC-ish traffic, and
pushes structured events through the inference engine into SQLite --
incrementally, per flow, per design doc §5.3/§5.7 durability model.

Load with mitmproxy/mitmweb:
    mitmweb -s glean/addon.py --set glean_label=control --set glean_baseline=all
"""

import json
import re
import socket
from pathlib import Path
from typing import Any, Optional

from mitmproxy import ctx

from glean import db, inference, schema

DEFAULT_DOMAIN_PATTERNS = [
    r"(^|\.)grammarly\.com$",
    r"(^|\.)grammarly\.io$",
    r"(^|\.)grammarly\.net$",
]


def domain_matches(host: str, patterns=DEFAULT_DOMAIN_PATTERNS) -> bool:
    return any(re.search(p, host) for p in patterns)


def try_parse_json(raw: Optional[bytes]) -> Optional[Any]:
    if not raw:
        return None
    try:
        return json.loads(raw.decode("utf-8", errors="strict"))
    except Exception:
        return None


def is_jsonrpc_ish(payload: Any) -> bool:
    """Heuristic: method/params-style fields, or just any JSON body on a
    filtered-domain flow (REST-like path patterns still count -- see
    design doc 5.1, we don't require strict JSON-RPC envelopes)."""
    if isinstance(payload, dict):
        return True
    return False


class GleanAddon:
    def __init__(self):
        self.conn = None
        self.session_id = None
        self.engine = inference.InferenceEngine()
        self.log_path: Optional[Path] = None
        self.label = "default"
        self.domain_patterns = DEFAULT_DOMAIN_PATTERNS

    def load(self, loader):
        loader.add_option("glean_db", str, "glean.db", "Path to GLEAN SQLite DB")
        loader.add_option("glean_label", str, "default", "Session label")
        loader.add_option(
            "glean_baseline", str, "all",
            "Anomaly comparison scope: all | label:<name> | session",
        )

    def running(self):
        db_path = ctx.options.glean_db
        self.label = ctx.options.glean_label
        self.conn = schema.init_db(db_path)
        self.log_path = Path(db_path).parent / db.ANOMALY_LOG_NAME
        self.session_id = db.start_session(
            self.conn, label=self.label, host=socket.gethostname()
        )
        self._load_baseline(ctx.options.glean_baseline)
        ctx.log.info(f"[glean] session {self.session_id} started, label={self.label}")

    def _load_baseline(self, scope: str):
        """Seed self.engine from prior sessions per the requested scope
        (design doc §5.2 comparison scope)."""
        q = (
            "SELECT e.path, f.timestamp, f.request_json, f.response_json "
            "FROM flows f JOIN endpoints e ON f.endpoint_id = e.id "
            "JOIN sessions s ON e.session_id = s.id"
        )
        params: tuple = ()
        if scope == "session":
            return  # nothing to preload
        elif scope.startswith("label:"):
            q += " WHERE s.label = ?"
            params = (scope.split(":", 1)[1],)
        # else "all" -- no filter
        q += " ORDER BY f.timestamp"
        for row in self.conn.execute(q, params):
            for direction, blob in (
                ("request", row["request_json"]), ("response", row["response_json"])
            ):
                if blob is None:
                    continue
                self.engine.observe(row["path"], direction, json.loads(blob), row["timestamp"])

    def _endpoint_path(self, flow) -> str:
        req = flow.request
        return f"{req.method} {req.path.split('?')[0]}"

    def request(self, flow):
        if not domain_matches(flow.request.pretty_host, self.domain_patterns):
            return
        flow.glean_ts = db.now_iso()  # stash for response()

    def response(self, flow):
        if not domain_matches(flow.request.pretty_host, self.domain_patterns):
            return
        self.handle_flow(
            endpoint_path=self._endpoint_path(flow),
            timestamp=getattr(flow, "glean_ts", db.now_iso()),
            request_raw=flow.request.raw_content,
            response_raw=flow.response.raw_content if flow.response else None,
            status_code=flow.response.status_code if flow.response else None,
            duration_ms=self._duration_ms(flow),
        )

    def _duration_ms(self, flow) -> Optional[float]:
        try:
            return round(
                (flow.response.timestamp_end - flow.request.timestamp_start) * 1000, 2
            )
        except Exception:
            return None

    def handle_flow(self, endpoint_path: str, timestamp: str,
                     request_raw: Optional[bytes], response_raw: Optional[bytes],
                     status_code: Optional[int], duration_ms: Optional[float]):
        """Core capture logic, decoupled from mitmproxy's flow object so it
        can be exercised by tests/synthetic traffic without mitmproxy running."""
        req_json = try_parse_json(request_raw)
        resp_json = try_parse_json(response_raw)
        if req_json is None and resp_json is None:
            return  # not JSON traffic -- out of scope (design doc non-goals)

        endpoint_id = db.get_or_create_endpoint(
            self.conn, self.session_id, endpoint_path, timestamp
        )

        anomalies = []
        if req_json is not None:
            anomalies += self.engine.observe(endpoint_path, "request", req_json, timestamp)
        if resp_json is not None:
            anomalies += self.engine.observe(endpoint_path, "response", resp_json, timestamp)

        flow_hash = db.compute_flow_hash(
            self.label, endpoint_path, timestamp, req_json, resp_json
        )
        db.insert_flow(
            self.conn, endpoint_id, timestamp, req_json, resp_json,
            status_code, duration_ms, flow_hash,
        )
        for a in anomalies:
            db.insert_anomaly(
                self.conn, self.session_id, endpoint_id, self.label, endpoint_path,
                a["type"], a["detail"], log_path=self.log_path,
            )
        return anomalies

    def done(self):
        """Clean shutdown -- summary pass only, see db.end_session docstring."""
        if self.session_id is not None:
            db.end_session(self.conn, self.session_id)
            ctx.log.info(f"[glean] session {self.session_id} closed")


addons = [GleanAddon()]
