#!/usr/bin/env python3
"""
test_glimpse.py — regression test for analyze_flows.py (GLIMPSE)

Builds a synthetic mitmproxy flow log with KNOWN, planted test cases
(positives that should be detected, negatives that should NOT be, and
flows that should be filtered out entirely), runs analyze_flows.py
against it, then checks the resulting SQLite DB against ground truth.

Usage:
    python3 tests/test_glimpse.py [path_to_analyze_flows.py]

Exit code 0 = all checks passed, 1 = at least one failure.
Requires: pip install mitmproxy --break-system-packages
"""
import json
import subprocess
import sys
import sqlite3
import time
import tempfile
from pathlib import Path

from mitmproxy.test import tflow
from mitmproxy.io import FlowWriter, FlowReader

TARGET = sys.argv[1] if len(sys.argv) > 1 else "analyze_flows.py"

flows = []
EXPECTED = []  # (description, expect: True/False/"SKIPPED", specific_type)


def make_flow(host, path, req_body=b"", resp_body=b"", req_ct="application/json"):
    f = tflow.tflow(resp=True)
    f.request.host = host
    f.request.headers["Host"] = host
    f.request.path = path
    f.request.method = "POST"
    f.request.headers["Content-Type"] = req_ct
    f.request.content = req_body
    f.request.timestamp_start = time.time()
    f.response.headers["Content-Type"] = "application/json"
    f.response.content = resp_body
    return f


CASES = [
    ("password_field", "capi.grammarly.com", "/login",
     b'{"username":"kaiya_test","password":"SuperSecret123"}', True, "Password"),
    ("api_key_field", "capi.grammarly.com", "/auth/refresh",
     b'{"api_key":"abc123def456ghi789tokenvalue"}', True, "API Key / Token"),
    ("ssn_with_context", "capi.grammarly.com", "/ingest",
     b'{"note":"user ssn on file is 555-12-6789 for verification"}', True, "SSN"),
    ("credit_card_valid_luhn", "capi.grammarly.com", "/billing",
     b'{"card":"4111111111111111"}', True, "Credit Card"),
    ("credit_card_invalid_luhn", "capi.grammarly.com", "/billing",
     b'{"card":"4111111111111112"}', False, None),
    ("email", "capi.grammarly.com", "/account",
     b'{"email":"kaiya.test@example.com"}', True, "Email Address"),
    ("phone_no_context", "capi.grammarly.com", "/misc",
     b'{"ref_id":"555-123-4567 was the batch code"}', False, None),
    ("phone_with_context", "capi.grammarly.com", "/support",
     b'{"note":"customer phone number is 555-123-4567 please call"}', True, "Phone Number"),
    ("mrn_with_context", "capi.grammarly.com", "/support",
     b'{"note":"patient medical record number AB123456 on file"}', True, "Medical Record Number"),
    ("icd_with_context", "capi.grammarly.com", "/support",
     b'{"note":"diagnosis code J45.9 noted in chart"}', True, "ICD Code"),
    ("street_address", "capi.grammarly.com", "/account",
     b'{"note":"ships to 1234 Sunset Boulevard for the promo"}', True, "Street Address"),
    ("non_grammarly_host_filter", "totally-unrelated-site.com", "/login",
     b'{"username":"x","password":"SuperSecret123"}', "SKIPPED", None),
    ("static_asset_js_skip", "static.grammarly.com", "/assets/bundle.js",
     b'', "SKIPPED", None),
]

flow_objs = []
for desc, host, path, body, expect, stype in CASES:
    ct = "" if path.endswith(".js") else "application/json"
    f = make_flow(host, path, req_body=body, req_ct=ct)
    flow_objs.append(f)
    EXPECTED.append((desc, expect, stype))

with tempfile.TemporaryDirectory() as tmp:
    flow_path = Path(tmp) / "test_flows.mitm"
    db_path = Path(tmp) / "test_run.db"

    with open(flow_path, "wb") as fh:
        writer = FlowWriter(fh)
        for fl in flow_objs:
            writer.add(fl)

    result = subprocess.run(
        [sys.executable, TARGET, str(flow_path), "--db", str(db_path)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print("analyze_flows.py exited non-zero:")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)

    conn = sqlite3.connect(db_path)
    matches_by_flow = {}
    for flow_id, stype in conn.execute("SELECT flow_id, specific_type FROM sensitivity_matches"):
        matches_by_flow.setdefault(flow_id, []).append(stype)
    processed_flows = set(r[0] for r in conn.execute("SELECT flow_id FROM captured_flows"))

    with open(flow_path, "rb") as fh:
        flow_ids_in_order = [fl.id for fl in FlowReader(fh).stream()]

    print(f"{'case':30s} {'expected':10s} {'actual':30s} {'result'}")
    print("-" * 90)
    all_pass = True
    for (desc, expect, stype), fid in zip(EXPECTED, flow_ids_in_order):
        if expect == "SKIPPED":
            ok = fid not in processed_flows
            actual = "skipped" if ok else "PROCESSED (should skip!)"
        elif expect is True:
            found = matches_by_flow.get(fid, [])
            ok = stype in found
            actual = ",".join(found) if found else "NO MATCH"
        else:
            found = matches_by_flow.get(fid, [])
            ok = len(found) == 0
            actual = ",".join(found) if found else "no match (correct)"
        all_pass &= ok
        print(f"{desc:30s} {str(expect):10s} {actual:30s} {'PASS' if ok else 'FAIL'}")

    print()
    print("ALL CHECKS PASSED" if all_pass else "SOME CHECKS FAILED")
    sys.exit(0 if all_pass else 1)
