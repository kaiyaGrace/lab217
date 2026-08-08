"""
GLEAN CLI (design doc §5.6).

    glean run [--label L] [--baseline all|label:X|session] [--db PATH]
    glean attach [--db PATH] [--label L]
    glean import <session_file> [--db PATH]
    glean export <session_id> <file> [--db PATH]      (helper, not in original spec)
    glean diff --a <label|session> --b <label|session> [--db PATH]
    glean status [--db PATH]
    glean review <anomaly_id> [--db PATH]              (helper, see tui.py docstring)
"""

import argparse
import json
import os
import socket
import sys
from pathlib import Path

from . import db, schema, tui


def cmd_run(args):
    """Manual/dev mode: launch mitmweb with the GLEAN addon in the
    foreground. Requires mitmproxy's certs to already be trusted on this
    machine (see README / run instructions)."""
    addon_path = str(Path(__file__).resolve().parent / "addon.py")
    cmd = [
        "mitmweb",
        "-s", addon_path,
        "--set", f"glean_db={args.db}",
        "--set", f"glean_label={args.label}",
        "--set", f"glean_baseline={args.baseline}",
        "--listen-port", str(args.port),
        "--web-port", str(args.web_port),
    ]
    if args.no_browser:
        cmd.append("--no-web-open-browser")
    if args.mode == "transparent":
        cmd += ["--mode", "transparent"]
    if args.showhost:
        cmd.append("--showhost")
    print("[glean] launching:", " ".join(cmd))
    os.execvp(cmd[0], cmd)


def cmd_attach(args):
    conn = schema.connect(args.db)
    session_id = None
    if args.label:
        row = conn.execute(
            "SELECT id FROM sessions WHERE label = ? ORDER BY id DESC LIMIT 1",
            (args.label,),
        ).fetchone()
        session_id = row["id"] if row else None
    tui.run_tui(args.db, session_id=session_id, refresh_seconds=args.refresh)


def cmd_status(args):
    conn = schema.connect(args.db)
    sessions = conn.execute(
        "SELECT id, label, started_at, ended_at, host FROM sessions ORDER BY id DESC LIMIT 5"
    ).fetchall()
    if not sessions:
        print("No sessions found in", args.db)
        return
    for s in sessions:
        state = "running" if s["ended_at"] is None else "ended"
        n_flows = conn.execute(
            "SELECT COUNT(*) c FROM flows f JOIN endpoints e ON f.endpoint_id=e.id "
            "WHERE e.session_id = ?", (s["id"],)
        ).fetchone()["c"]
        n_new = conn.execute(
            "SELECT COUNT(*) c FROM anomalies WHERE session_id = ? AND status='new'",
            (s["id"],),
        ).fetchone()["c"]
        print(
            f"session {s['id']:<4} [{state:7}] label={s['label']:<12} "
            f"host={s['host']:<15} flows={n_flows:<5} new_anomalies={n_new} "
            f"started={s['started_at']}"
        )


def cmd_review(args):
    conn = schema.connect(args.db)
    log_path = Path(args.db).parent / db.ANOMALY_LOG_NAME
    row = conn.execute("SELECT * FROM anomalies WHERE id = ?", (args.anomaly_id,)).fetchone()
    if not row:
        print(f"No anomaly with id {args.anomaly_id}", file=sys.stderr)
        sys.exit(1)
    if row["status"] == "reviewed":
        print(f"Anomaly {args.anomaly_id} already reviewed.")
        return
    db.mark_anomaly_reviewed(conn, args.anomaly_id, log_path=log_path)
    print(f"Anomaly {args.anomaly_id} marked reviewed.")


def cmd_export(args):
    """Not in the original CLI list, but needed to produce the 'saved
    session files' that `glean import` re-imports."""
    conn = schema.connect(args.db)
    sess = conn.execute("SELECT * FROM sessions WHERE id = ?", (args.session_id,)).fetchone()
    if not sess:
        print(f"No session {args.session_id}", file=sys.stderr)
        sys.exit(1)
    flows = conn.execute(
        "SELECT e.path AS endpoint_path, f.timestamp, f.request_json, "
        "f.response_json, f.status_code, f.duration_ms FROM flows f "
        "JOIN endpoints e ON f.endpoint_id = e.id WHERE e.session_id = ? "
        "ORDER BY f.timestamp", (args.session_id,)
    ).fetchall()
    out = {
        "label": sess["label"],
        "host": sess["host"],
        "started_at": sess["started_at"],
        "ended_at": sess["ended_at"],
        "flows": [
            {
                "endpoint_path": f["endpoint_path"],
                "timestamp": f["timestamp"],
                "request": json.loads(f["request_json"]) if f["request_json"] else None,
                "response": json.loads(f["response_json"]) if f["response_json"] else None,
                "status_code": f["status_code"],
                "duration_ms": f["duration_ms"],
            }
            for f in flows
        ],
    }
    with open(args.file, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"Exported session {args.session_id} ({len(flows)} flows) -> {args.file}")


def cmd_import(args):
    """Idempotent: relies on flows.flow_hash UNIQUE + anomalies
    (endpoint_id, type, detail) UNIQUE, both INSERT OR IGNORE. Safe to run
    on the same file twice (design doc §5.6)."""
    from . import inference

    with open(args.session_file) as fh:
        data = json.load(fh)

    conn = schema.init_db(args.db)
    log_path = Path(args.db).parent / db.ANOMALY_LOG_NAME
    label = data.get("label", "imported")
    session_id = db.start_session(
        conn, label=label, host=data.get("host", "unknown"),
        source_file=args.session_file,
    )
    engine = inference.InferenceEngine()

    n_flows_inserted = 0
    n_flows_skipped = 0
    n_anomalies = 0
    for flow in data.get("flows", []):
        path = flow["endpoint_path"]
        ts = flow["timestamp"]
        endpoint_id = db.get_or_create_endpoint(conn, session_id, path, ts)

        anomalies = []
        if flow.get("request") is not None:
            anomalies += engine.observe(path, "request", flow["request"], ts)
        if flow.get("response") is not None:
            anomalies += engine.observe(path, "response", flow["response"], ts)

        flow_hash = db.compute_flow_hash(
            label, path, ts, flow.get("request"), flow.get("response")
        )
        new_id = db.insert_flow(
            conn, endpoint_id, ts, flow.get("request"), flow.get("response"),
            flow.get("status_code"), flow.get("duration_ms"), flow_hash,
        )
        if new_id:
            n_flows_inserted += 1
        else:
            n_flows_skipped += 1

        for a in anomalies:
            if db.insert_anomaly(
                conn, session_id, endpoint_id, label, path, a["type"], a["detail"], log_path
            ):
                n_anomalies += 1

    db.end_session(conn, session_id)
    db.rebuild_schema_fields(conn, session_id)
    print(
        f"[glean import] session={session_id} label={label} "
        f"flows_inserted={n_flows_inserted} flows_skipped(dupe)={n_flows_skipped} "
        f"new_anomalies={n_anomalies}"
    )


def _resolve_scope(conn, scope: str):
    """scope is either a bare session id (int-like string) or a label."""
    if scope.isdigit():
        return "session_id", int(scope)
    return "label", scope


def cmd_diff(args):
    conn = schema.connect(args.db)

    def endpoint_set(scope):
        kind, val = _resolve_scope(conn, scope)
        if kind == "session_id":
            rows = conn.execute(
                "SELECT path FROM endpoints WHERE session_id = ?", (val,)
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT DISTINCT e.path FROM endpoints e JOIN sessions s "
                "ON e.session_id = s.id WHERE s.label = ?", (val,)
            ).fetchall()
        return {r["path"] for r in rows}

    def schema_map(scope):
        kind, val = _resolve_scope(conn, scope)
        if kind == "session_id":
            rows = conn.execute(
                "SELECT e.path, sf.field_path, sf.direction, sf.field_type_set, sf.status "
                "FROM schema_fields sf JOIN endpoints e ON sf.endpoint_id = e.id "
                "WHERE e.session_id = ?", (val,)
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT e.path, sf.field_path, sf.direction, sf.field_type_set, sf.status "
                "FROM schema_fields sf JOIN endpoints e ON sf.endpoint_id = e.id "
                "JOIN sessions s ON e.session_id = s.id WHERE s.label = ?", (val,)
            ).fetchall()
        out = {}
        for r in rows:
            key = (r["path"], r["direction"], r["field_path"])
            out[key] = (r["field_type_set"], r["status"])
        return out

    a_eps, b_eps = endpoint_set(args.a), endpoint_set(args.b)
    only_a = sorted(a_eps - b_eps)
    only_b = sorted(b_eps - a_eps)

    print(f"=== Endpoints only in A ({args.a}) ===")
    for p in only_a:
        print(" ", p)
    print(f"=== Endpoints only in B ({args.b}) ===")
    for p in only_b:
        print(" ", p)

    a_schema, b_schema = schema_map(args.a), schema_map(args.b)
    all_keys = set(a_schema) | set(b_schema)
    print(f"=== Schema differences (fields only in one side, or changed) ===")
    diffs = 0
    for key in sorted(all_keys):
        path, direction, field = key
        in_a, in_b = key in a_schema, key in b_schema
        if in_a and in_b and a_schema[key] != b_schema[key]:
            diffs += 1
            print(f"  {path} [{direction}] {field}: A={a_schema[key]} B={b_schema[key]}")
        elif in_a and not in_b:
            diffs += 1
            print(f"  {path} [{direction}] {field}: only in A ({args.a}) -- {a_schema[key]}")
        elif in_b and not in_a:
            diffs += 1
            print(f"  {path} [{direction}] {field}: only in B ({args.b}) -- {b_schema[key]}")
    if not diffs:
        print("  (none)")


def build_parser():
    p = argparse.ArgumentParser(prog="glean")
    sub = p.add_subparsers(dest="command", required=True)

    r = sub.add_parser("run", help="Run mitmweb + GLEAN addon in the foreground")
    r.add_argument("--db", default="glean.db")
    r.add_argument("--label", default="default")
    r.add_argument("--baseline", default="all",
                    help="all | session | label:<name>")
    r.add_argument("--port", type=int, default=8080)
    r.add_argument("--web-port", type=int, default=8081)
    r.add_argument("--no-browser", action="store_true")
    r.add_argument("--mode", default="regular", choices=["regular", "transparent"],
                    help="mitmproxy mode (regular or transparent)")
    r.add_argument("--showhost", action="store_true",
                    help="use the Host header to display/log the intercepted hostname")
    r.set_defaults(func=cmd_run)

    a = sub.add_parser("attach", help="Attach the Rich TUI to a DB/session")
    a.add_argument("--db", default="glean.db")
    a.add_argument("--label", default=None)
    a.add_argument("--refresh", type=float, default=2.0)
    a.set_defaults(func=cmd_attach)

    i = sub.add_parser("import", help="Idempotently import a saved session file")
    i.add_argument("session_file")
    i.add_argument("--db", default="glean.db")
    i.set_defaults(func=cmd_import)

    e = sub.add_parser("export", help="Export a session to a JSON file")
    e.add_argument("session_id", type=int)
    e.add_argument("file")
    e.add_argument("--db", default="glean.db")
    e.set_defaults(func=cmd_export)

    d = sub.add_parser("diff", help="Compare endpoints/schema between two labels or sessions")
    d.add_argument("--a", required=True)
    d.add_argument("--b", required=True)
    d.add_argument("--db", default="glean.db")
    d.set_defaults(func=cmd_diff)

    s = sub.add_parser("status", help="Health check of sessions in the DB")
    s.add_argument("--db", default="glean.db")
    s.set_defaults(func=cmd_status)

    rv = sub.add_parser("review", help="Mark an anomaly reviewed")
    rv.add_argument("anomaly_id", type=int)
    rv.add_argument("--db", default="glean.db")
    rv.set_defaults(func=cmd_review)

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
