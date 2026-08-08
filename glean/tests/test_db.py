import sys, os, tempfile, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from glean import schema, db, inference


def fresh_db():
    tmp = tempfile.mktemp(suffix=".db")
    conn = schema.init_db(tmp)
    return tmp, conn


def test_flow_hash_idempotent_insert():
    path, conn = fresh_db()
    sid = db.start_session(conn, "control", "frodo")
    eid = db.get_or_create_endpoint(conn, sid, "POST /a", "t1")

    fh = db.compute_flow_hash("control", "POST /a", "t1", {"x": 1}, {"y": 2})
    first = db.insert_flow(conn, eid, "t1", {"x": 1}, {"y": 2}, 200, 12.3, fh)
    second = db.insert_flow(conn, eid, "t1", {"x": 1}, {"y": 2}, 200, 12.3, fh)  # re-import
    assert first is not None
    assert second is None  # ignored as duplicate
    count = conn.execute("SELECT COUNT(*) c FROM flows").fetchone()["c"]
    assert count == 1, count
    print("ok: duplicate flow_hash insert is a no-op (idempotent import)")
    os.remove(path)


def test_anomaly_dedup_and_review_persistence():
    path, conn = fresh_db()
    sid = db.start_session(conn, "control", "frodo")
    eid = db.get_or_create_endpoint(conn, sid, "POST /a", "t1")

    log = tempfile.mktemp(suffix=".log")
    a1 = db.insert_anomaly(conn, sid, eid, "control", "POST /a", "new_endpoint", "new endpoint: POST /a", log)
    a2 = db.insert_anomaly(conn, sid, eid, "control", "POST /a", "new_endpoint", "new endpoint: POST /a", log)  # dupe
    assert a1 is not None
    assert a2 is None
    count = conn.execute("SELECT COUNT(*) c FROM anomalies").fetchone()["c"]
    assert count == 1, count

    db.mark_anomaly_reviewed(conn, a1, log)
    row = conn.execute("SELECT status, reviewed_at FROM anomalies WHERE id=?", (a1,)).fetchone()
    assert row["status"] == "reviewed" and row["reviewed_at"] is not None

    # simulate "re-import after crash": inserting the same anomaly again must
    # NOT reset it back to 'new'
    a3 = db.insert_anomaly(conn, sid, eid, "control", "POST /a", "new_endpoint", "new endpoint: POST /a", log)
    assert a3 is None
    row2 = conn.execute("SELECT status FROM anomalies WHERE id=?", (a1,)).fetchone()
    assert row2["status"] == "reviewed"
    print("ok: anomaly dedup + review status survives re-insert (crash-safe)")

    with open(log) as f:
        lines = f.read().strip().split("\n")
    assert len(lines) == 2  # one 'new' line, one 'reviewed' line
    assert lines[0].split("\t")[2] == "new"
    assert lines[1].split("\t")[2] == "reviewed"
    print("ok: anomaly log derived correctly (new, then reviewed)")
    os.remove(path)
    os.remove(log)


def test_anomaly_dedup_survives_across_sessions():
    """Regression test for the bug caught during manual CLI testing:
    endpoint_id is scoped per-session (endpoints is UNIQUE(session_id,
    path)), so re-importing the same file creates a NEW session and NEW
    endpoint_id. Dedup must key off (label, endpoint_path), not
    endpoint_id, or every re-import re-raises every anomaly."""
    path, conn = fresh_db()
    log = tempfile.mktemp(suffix=".log")

    sid1 = db.start_session(conn, "control", "frodo")
    eid1 = db.get_or_create_endpoint(conn, sid1, "POST /a", "t1")
    a1 = db.insert_anomaly(conn, sid1, eid1, "control", "POST /a", "new_endpoint", "new endpoint: POST /a", log)
    assert a1 is not None

    # Simulate a second import of the same session file: new session,
    # new (session-scoped) endpoint_id, SAME label + path.
    sid2 = db.start_session(conn, "control", "frodo")
    eid2 = db.get_or_create_endpoint(conn, sid2, "POST /a", "t1")
    assert eid2 != eid1  # confirms endpoint_id really did change
    a2 = db.insert_anomaly(conn, sid2, eid2, "control", "POST /a", "new_endpoint", "new endpoint: POST /a", log)
    assert a2 is None, "anomaly re-appeared on re-import despite same label+path"

    count = conn.execute("SELECT COUNT(*) c FROM anomalies").fetchone()["c"]
    assert count == 1
    print("ok: anomaly dedup survives re-import across sessions (label+path key)")
    os.remove(path)
    os.remove(log)


def test_rebuild_schema_fields_matches_inference_engine():
    path, conn = fresh_db()
    sid = db.start_session(conn, "control", "frodo")
    eid = db.get_or_create_endpoint(conn, sid, "POST /a", "t1")
    fh1 = db.compute_flow_hash("control", "POST /a", "t1", {"x": 1}, None)
    fh2 = db.compute_flow_hash("control", "POST /a", "t2", {"x": None}, None)
    db.insert_flow(conn, eid, "t1", {"x": 1}, None, 200, 1.0, fh1)
    db.insert_flow(conn, eid, "t2", {"x": None}, None, 200, 1.0, fh2)

    n = db.rebuild_schema_fields(conn, sid)
    assert n >= 1
    row = conn.execute(
        "SELECT field_type_set, status FROM schema_fields WHERE field_path='x'"
    ).fetchone()
    types = json.loads(row["field_type_set"])
    assert set(types) == {"number", "null"}
    assert row["status"] == "optional-present"
    print("ok: schema_fields rebuild reproduces inference engine's field model")
    os.remove(path)


def test_wal_mode_and_foreign_keys_enabled():
    path, conn = fresh_db()
    mode = conn.execute("PRAGMA journal_mode").fetchone()[0]
    fk = conn.execute("PRAGMA foreign_keys").fetchone()[0]
    assert mode.lower() == "wal", mode
    assert fk == 1
    print("ok: WAL mode + foreign_keys on (readers don't block writer)")
    os.remove(path)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("\nALL DB TESTS PASSED")
