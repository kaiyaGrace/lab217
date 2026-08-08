"""
GLEAN SQLite writer.

Durability model (design doc §5.3/§5.7): every flow insert and every
anomaly status transition is committed synchronously, one transaction per
event. This -- not the end-of-session summary pass -- is what protects
against data/state loss on crash or SSH-drop-induced kill. The clean
shutdown handler in cli.py only writes `sessions.ended_at`; it has nothing
buffered to flush.
"""

import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from . import inference

ANOMALY_LOG_NAME = "glean_anomalies.log"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------- sessions

def start_session(conn: sqlite3.Connection, label: str, host: str,
                   source_file: Optional[str] = None) -> int:
    cur = conn.execute(
        "INSERT INTO sessions(started_at, source_file, host, label) "
        "VALUES (?, ?, ?, ?)",
        (now_iso(), source_file, host, label),
    )
    conn.commit()
    return cur.lastrowid


def end_session(conn: sqlite3.Connection, session_id: int) -> None:
    """Clean-shutdown summary pass. Not a flush -- see module docstring."""
    conn.execute(
        "UPDATE sessions SET ended_at = ? WHERE id = ?", (now_iso(), session_id)
    )
    conn.commit()


# ---------------------------------------------------------------- endpoints

def get_or_create_endpoint(conn: sqlite3.Connection, session_id: int,
                            path: str, timestamp: str) -> int:
    row = conn.execute(
        "SELECT id FROM endpoints WHERE session_id = ? AND path = ?",
        (session_id, path),
    ).fetchone()
    if row:
        conn.execute(
            "UPDATE endpoints SET last_seen = ?, count = count + 1 WHERE id = ?",
            (timestamp, row["id"]),
        )
        conn.commit()
        return row["id"]
    cur = conn.execute(
        "INSERT INTO endpoints(session_id, path, first_seen, last_seen, count) "
        "VALUES (?, ?, ?, ?, 1)",
        (session_id, path, timestamp, timestamp),
    )
    conn.commit()
    return cur.lastrowid


# -------------------------------------------------------------------- flows

def compute_flow_hash(session_label: str, endpoint_path: str, timestamp: str,
                       request: Any, response: Any) -> str:
    payload = "|".join([
        session_label,
        endpoint_path,
        timestamp,
        inference.canonical_json(request),
        inference.canonical_json(response),
    ])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def insert_flow(conn: sqlite3.Connection, endpoint_id: int, timestamp: str,
                 request: Any, response: Any, status_code: Optional[int],
                 duration_ms: Optional[float], flow_hash: str) -> Optional[int]:
    """INSERT OR IGNORE on flow_hash -- idempotent. Returns the new flow id,
    or None if this exact flow was already present (e.g. re-import)."""
    cur = conn.execute(
        "INSERT OR IGNORE INTO flows"
        "(endpoint_id, timestamp, request_json, response_json, status_code, "
        " duration_ms, flow_hash) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            endpoint_id,
            timestamp,
            inference.canonical_json(request) if request is not None else None,
            inference.canonical_json(response) if response is not None else None,
            status_code,
            duration_ms,
            flow_hash,
        ),
    )
    conn.commit()
    return cur.lastrowid if cur.rowcount else None


# --------------------------------------------------------------- anomalies

def insert_anomaly(conn: sqlite3.Connection, session_id: int,
                    endpoint_id: Optional[int], label: str, endpoint_path: str,
                    atype: str, detail: str,
                    log_path: Optional[Path] = None) -> Optional[int]:
    """INSERT OR IGNORE on (label, endpoint_path, type, detail) -- this is
    a stable logical identity across sessions (unlike endpoint_id, which is
    per-session), so re-imports or re-observing the same anomaly never
    duplicates or un-reviews it. See schema.py docstring on this table."""
    ts = now_iso()
    cur = conn.execute(
        "INSERT OR IGNORE INTO anomalies"
        "(session_id, endpoint_id, label, endpoint_path, type, detail, "
        " timestamp, status) VALUES (?, ?, ?, ?, ?, ?, ?, 'new')",
        (session_id, endpoint_id, label, endpoint_path, atype, detail, ts),
    )
    conn.commit()
    if cur.rowcount and log_path:
        append_anomaly_log(log_path, ts, atype, detail, "new")
    return cur.lastrowid if cur.rowcount else None


def mark_anomaly_reviewed(conn: sqlite3.Connection, anomaly_id: int,
                           log_path: Optional[Path] = None) -> None:
    """Synchronous, incremental write -- fires immediately on the TUI
    keybind, same durability guarantee as a flow insert (see module
    docstring). A crash right after this must not un-review the anomaly."""
    ts = now_iso()
    conn.execute(
        "UPDATE anomalies SET status = 'reviewed', reviewed_at = ? WHERE id = ?",
        (ts, anomaly_id),
    )
    conn.commit()
    if log_path:
        row = conn.execute(
            "SELECT type, detail FROM anomalies WHERE id = ?", (anomaly_id,)
        ).fetchone()
        if row:
            append_anomaly_log(log_path, ts, row["type"], row["detail"], "reviewed")


def append_anomaly_log(log_path: Path, ts: str, atype: str, detail: str,
                        status: str) -> None:
    """Purely derivative of the anomalies table -- DB write always happens
    first (see callers above). Reconstructable via
    `SELECT * FROM anomalies ORDER BY timestamp`."""
    with open(log_path, "a") as f:
        f.write(f"{ts}\t{atype}\t{status}\t{detail}\n")


def rebuild_anomaly_log(conn: sqlite3.Connection, log_path: Path) -> int:
    """Regenerate glean_anomalies.log from the anomalies table."""
    rows = conn.execute(
        "SELECT timestamp, type, detail, status FROM anomalies ORDER BY timestamp"
    ).fetchall()
    with open(log_path, "w") as f:
        for r in rows:
            f.write(f"{r['timestamp']}\t{r['type']}\t{r['status']}\t{r['detail']}\n")
    return len(rows)


# ---------------------------------------------------- schema_fields (derived)

def rebuild_schema_fields(conn: sqlite3.Connection, session_id: Optional[int] = None) -> int:
    """Rebuild the derived schema_fields table from raw flows.*_json.
    Safe to call any time the inference logic changes -- see schema.py
    module docstring."""
    conn.execute(
        "DELETE FROM schema_fields WHERE endpoint_id IN "
        "(SELECT id FROM endpoints" + (" WHERE session_id = ?)" if session_id else ")"),
        (session_id,) if session_id else (),
    )
    q = "SELECT id, path FROM endpoints"
    params: tuple = ()
    if session_id:
        q += " WHERE session_id = ?"
        params = (session_id,)
    endpoints = conn.execute(q, params).fetchall()

    written = 0
    for ep in endpoints:
        engine = inference.InferenceEngine()
        flows = conn.execute(
            "SELECT timestamp, request_json, response_json FROM flows "
            "WHERE endpoint_id = ? ORDER BY timestamp",
            (ep["id"],),
        ).fetchall()
        for fl in flows:
            for direction, blob in (
                ("request", fl["request_json"]),
                ("response", fl["response_json"]),
            ):
                if blob is None:
                    continue
                payload = json.loads(blob)
                engine.observe(ep["path"], direction, payload, fl["timestamp"])

        if ep["path"] not in engine.endpoints:
            continue
        model = engine.endpoints[ep["path"]]
        for direction, fields in model.fields.items():
            for fpath, fmodel in fields.items():
                conn.execute(
                    "INSERT OR REPLACE INTO schema_fields"
                    "(endpoint_id, field_path, direction, field_type_set, "
                    " status, first_seen) VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        ep["id"],
                        fpath,
                        direction,
                        json.dumps(sorted(fmodel.types)),
                        fmodel.status,
                        fmodel.first_seen,
                    ),
                )
                written += 1
    conn.commit()
    return written
