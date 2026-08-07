#!/usr/bin/env python3
"""
test_gleam.py — regression test for gleam.py (GLEAN)

Drives the Gleam addon through mitmproxy's own addon-testing harness
(mitmproxy.test.taddons + tflow) so the request/response/websocket/error
hooks run exactly as they would under real mitmweb -s gleam.py, then
checks the resulting SQLite DB + summary output against known ground
truth built from synthetic flows.

Usage:
    python3 tests/test_gleam.py

Exit code 0 = all checks passed, 1 = at least one failure.
Requires: pip install mitmproxy --break-system-packages
Requires gleam.py importable (run from the same directory, or put it
on PYTHONPATH).
"""
import json
import os
import sqlite3
import sys
import tempfile
import time
from pathlib import Path

from mitmproxy.test import taddons, tflow

import gleam

FAILURES = []


def check(label, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}" + (f"  ({detail})" if detail and not condition else ""))
    if not condition:
        FAILURES.append(label)


with tempfile.TemporaryDirectory() as tmp:
    db_path = str(Path(tmp) / "gleam_test.db")
    summary_prefix = str(Path(tmp) / "gleam_test_summary")

    addon = gleam.Gleam()

    with taddons.context(addon) as tctx:
        tctx.options.gleam_db_path = db_path
        tctx.options.gleam_summary_path = summary_prefix
        tctx.options.gleam_grammarly_only = True
        tctx.options.gleam_batch_size = 200
        tctx.options.gleam_flush_interval = 5.0
        tctx.options.gleam_summary_interval = 0

        addon.running()

        def make_http_flow(host, path, req_body=b"", resp_body=b"",
                            req_headers=None, status=200):
            f = tflow.tflow(resp=True)
            f.request.host = host
            f.request.headers["Host"] = host
            f.request.path = path
            f.request.method = "POST"
            f.request.headers["Content-Type"] = "application/json"
            if req_headers:
                for k, v in req_headers.items():
                    f.request.headers[k] = v
            f.request.content = req_body
            f.request.timestamp_start = time.time()
            f.response.status_code = status
            f.response.headers["Content-Type"] = "application/json"
            f.response.content = resp_body
            f.response.timestamp_end = f.request.timestamp_start + 0.123
            return f

        print("Case A-D: HTTP flows (RPC w/ header token, RPC w/ body token, RPC error, plain JSON)")
        addon.response(make_http_flow(
            "capi.grammarly.com", "/rpc",
            req_body=json.dumps({"jsonrpc": "2.0", "id": "1", "method": "doc.analyze",
                                  "params": {"text": "hello"}}).encode(),
            resp_body=json.dumps({"jsonrpc": "2.0", "id": "1", "result": {"ok": True}}).encode(),
            req_headers={"Authorization": "Bearer sometoken"},
        ))
        addon.response(make_http_flow(
            "capi.grammarly.com", "/rpc",
            req_body=json.dumps({"jsonrpc": "2.0", "id": "2", "method": "session.refresh",
                                  "params": {"refresh_token": "xyz"}}).encode(),
            resp_body=json.dumps({"jsonrpc": "2.0", "id": "2", "result": {"ok": True}}).encode(),
        ))
        addon.response(make_http_flow(
            "capi.grammarly.com", "/rpc",
            req_body=json.dumps({"jsonrpc": "2.0", "id": "3", "method": "doc.analyze", "params": {}}).encode(),
            resp_body=json.dumps({"jsonrpc": "2.0", "id": "3",
                                   "error": {"code": -1, "message": "bad"}}).encode(),
            status=400,
        ))
        addon.response(make_http_flow(
            "capi.grammarly.com", "/ingest-api/v1/events/ingestion_front_end",
            req_body=json.dumps({"agent_id": "abc", "object_id": "def", "event": "keystroke"}).encode(),
            resp_body=b'{"status":"ok"}',
        ))

        print("Case E: non-Grammarly host should be filtered out entirely")
        addon.response(make_http_flow(
            "example.com", "/rpc",
            req_body=json.dumps({"jsonrpc": "2.0", "id": "9", "method": "x", "params": {}}).encode(),
            resp_body=b'{"jsonrpc":"2.0","id":"9","result":{}}',
        ))

        print("Case F: connection error on Grammarly host")
        from mitmproxy.flow import Error as FlowError
        f_err = tflow.tflow()
        f_err.request.host = "capi.grammarly.com"
        f_err.request.headers["Host"] = "capi.grammarly.com"
        f_err.request.path = "/rpc"
        f_err.request.method = "POST"
        f_err.error = FlowError("connection reset")
        addon.error(f_err)

        print("Case G: WebSocket lifecycle (one RPC-shaped frame, one plain text frame)")
        from mitmproxy.websocket import WebSocketData, WebSocketMessage
        f_ws = tflow.tflow()
        f_ws.request.host = "capi.grammarly.com"
        f_ws.request.headers["Host"] = "capi.grammarly.com"
        f_ws.request.path = "/ws/ot"
        f_ws.request.scheme = "https"
        addon.websocket_start(f_ws)
        f_ws.websocket = WebSocketData()
        f_ws.websocket.messages.append(WebSocketMessage(1, True, json.dumps({
            "jsonrpc": "2.0", "id": "10", "method": "doc.edit", "params": {"delta": "x"}
        }).encode()))
        addon.websocket_message(f_ws)
        f_ws.websocket.messages.append(WebSocketMessage(1, False, b"not json, just a plain text frame"))
        addon.websocket_message(f_ws)
        addon.websocket_end(f_ws)

        print("Case H: batch auto-flush at a small batch size")
        tctx.options.gleam_batch_size = 2
        for i in range(3):
            addon.response(make_http_flow(
                "capi.grammarly.com", "/rpc",
                req_body=json.dumps({"jsonrpc": "2.0", "id": str(100 + i),
                                      "method": "ping", "params": {}}).encode(),
                resp_body=json.dumps({"jsonrpc": "2.0", "id": str(100 + i), "result": {}}).encode(),
            ))
        auto_flush_triggered = len(addon.rpc_buffer) < 3
        tctx.options.gleam_batch_size = 200

        print("Edge case: malformed JSON body should not crash")
        try:
            f_bad = tflow.tflow(resp=True)
            f_bad.request.host = "capi.grammarly.com"
            f_bad.request.headers["Content-Type"] = "application/json"
            f_bad.request.content = b'{"broken": "json", missing_quotes: True,'
            f_bad.response.content = b"not even json at all"
            addon.response(f_bad)
            malformed_ok = True
        except Exception:
            malformed_ok = False

        print("Edge case: stale websocket state should get swept by tick()")
        f_stale = tflow.tflow()
        f_stale.request.host = "capi.grammarly.com"
        f_stale.request.path = "/ws/stale"
        addon.websocket_start(f_stale)
        addon._ws_state[f_stale.id]["timestamp_open"] = time.time() - 7200
        before_sweep = len(addon._ws_state)
        addon.tick()
        after_sweep = len(addon._ws_state)

        addon._flush(force=True)

        conn = sqlite3.connect(db_path)
        rpc_calls = conn.execute(
            "SELECT rpc_method, status_code, token_location, error_json FROM rpc_calls ORDER BY id"
        ).fetchall()
        http_other = conn.execute(
            "SELECT host, path FROM http_flows_other ORDER BY id"
        ).fetchall()
        ws_flows = conn.execute(
            "SELECT host, path, message_count, direction_counts_json FROM ws_flows"
        ).fetchall()
        ws_rpc = conn.execute(
            "SELECT host, path, rpc_method, direction FROM ws_rpc_messages"
        ).fetchall()
        hosts_rpc = {r[0] for r in conn.execute("SELECT DISTINCT host FROM rpc_calls")}
        hosts_other = {r[0] for r in conn.execute("SELECT DISTINCT host FROM http_flows_other")}
        conn.close()

        addon.summary()
        addon.done()

        print()
        print("=== Checks ===")
        check("6 rpc_calls rows persisted (3 initial + 3 batch)", len(rpc_calls) == 6, str(rpc_calls))
        check("token_location=header detected", rpc_calls[0][2] == "header")
        check("token_location=body detected from params", rpc_calls[1][2] == "body")
        check("error response captured error_json", rpc_calls[2][3] is not None)
        check("3 http_flows_other rows (ingestion event + connection error + malformed-JSON case)",
              len(http_other) == 3, str(http_other))
        check("example.com never appears in rpc_calls", "example.com" not in hosts_rpc)
        check("example.com never appears in http_flows_other", "example.com" not in hosts_other)
        check("ws_flows recorded with 2 total messages", ws_flows and ws_flows[0][2] == 2, str(ws_flows))
        check("ws direction counts 1/1 client<->server", ws_flows and ws_flows[0][3] == '{"client_to_server": 1, "server_to_client": 1}')
        check("only the RPC-shaped ws frame landed in ws_rpc_messages", len(ws_rpc) == 1, str(ws_rpc))
        check("ws_rpc rpc_method correctly parsed", ws_rpc and ws_rpc[0][2] == "doc.edit")
        check("batch_size=2 triggered an automatic mid-loop flush", auto_flush_triggered)
        check("malformed JSON body did not crash response()", malformed_ok)
        check("stale websocket state swept by tick()", before_sweep == 1 and after_sweep == 0,
              f"before={before_sweep} after={after_sweep}")

        print()
        if FAILURES:
            print(f"SOME CHECKS FAILED: {FAILURES}")
            sys.exit(1)
        else:
            print("ALL CHECKS PASSED")
            sys.exit(0)
