"""
GLEAN SQLite schema.

`schema_fields` is a derived/materialized index over flows.request_json /
flows.response_json -- it is rebuildable at any time via
`glean.inference.rebuild_schema_fields()`. It is never hand-edited; if it
looks wrong, the fix is a bug in the inference engine, not a patch to this
table.

`flows.flow_hash` is a hash of (session_label, endpoint path, timestamp,
canonicalized request+response bytes) and carries a UNIQUE index so that
`glean import` is a plain INSERT OR IGNORE -- safe to run on the same
session file twice.

`anomalies` is deduplicated on (endpoint_id, type, detail) so re-importing
a session file can never re-create or un-review an anomaly that already
exists.
"""

import sqlite3

SCHEMA_VERSION = 1

DDL = """
CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT
);

CREATE TABLE IF NOT EXISTS sessions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at  TEXT NOT NULL,
    ended_at    TEXT,
    source_file TEXT,
    host        TEXT,
    label       TEXT NOT NULL DEFAULT 'default'
);

CREATE TABLE IF NOT EXISTS endpoints (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id  INTEGER NOT NULL REFERENCES sessions(id),
    path        TEXT NOT NULL,
    first_seen  TEXT NOT NULL,
    last_seen   TEXT NOT NULL,
    count       INTEGER NOT NULL DEFAULT 0,
    UNIQUE(session_id, path)
);

CREATE TABLE IF NOT EXISTS flows (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    endpoint_id    INTEGER NOT NULL REFERENCES endpoints(id),
    timestamp      TEXT NOT NULL,
    request_json   TEXT,
    response_json  TEXT,
    status_code    INTEGER,
    duration_ms    REAL,
    flow_hash      TEXT NOT NULL UNIQUE
);

-- Derived table: rebuildable from flows.*_json. See module docstring.
CREATE TABLE IF NOT EXISTS schema_fields (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    endpoint_id     INTEGER NOT NULL REFERENCES endpoints(id),
    field_path      TEXT NOT NULL,
    direction       TEXT NOT NULL CHECK(direction IN ('request', 'response')),
    field_type_set  TEXT NOT NULL,   -- JSON list, e.g. ["string","null"]
    status          TEXT NOT NULL CHECK(status IN
                        ('required', 'optional-present', 'optional-absent')),
    first_seen      TEXT NOT NULL,
    UNIQUE(endpoint_id, field_path, direction)
);

-- Dedup key is (label, endpoint_path, type, detail) rather than
-- endpoint_id: endpoint_id is scoped per-session (endpoints table is
-- UNIQUE(session_id, path)), so a re-import creates a *new* session and
-- therefore new endpoint rows. Keying dedup off endpoint_id would silently
-- fail to dedupe across re-imports -- label+path is the stable logical
-- identity that survives across sessions with the same label.
-- endpoint_id is kept as a nullable FK purely for convenient joins to the
-- specific session/endpoint that first raised it.
CREATE TABLE IF NOT EXISTS anomalies (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id     INTEGER NOT NULL REFERENCES sessions(id),
    endpoint_id    INTEGER REFERENCES endpoints(id),
    label          TEXT NOT NULL,
    endpoint_path  TEXT NOT NULL,
    type           TEXT NOT NULL CHECK(type IN ('new_endpoint', 'schema_change')),
    detail         TEXT NOT NULL,
    timestamp      TEXT NOT NULL,
    status         TEXT NOT NULL DEFAULT 'new' CHECK(status IN ('new', 'reviewed')),
    reviewed_at    TEXT,
    UNIQUE(label, endpoint_path, type, detail)
);

CREATE INDEX IF NOT EXISTS idx_flows_endpoint ON flows(endpoint_id);
CREATE INDEX IF NOT EXISTS idx_flows_timestamp ON flows(timestamp);
CREATE INDEX IF NOT EXISTS idx_anomalies_status ON anomalies(status);
CREATE INDEX IF NOT EXISTS idx_endpoints_session ON endpoints(session_id);
"""


def connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    # WAL mode: readers (TUI/web dashboard polling) don't block the writer
    # doing incremental per-event commits.
    conn.execute("PRAGMA journal_mode = WAL;")
    return conn


def init_db(db_path: str) -> sqlite3.Connection:
    conn = connect(db_path)
    conn.executescript(DDL)
    conn.execute(
        "INSERT OR IGNORE INTO meta(key, value) VALUES ('schema_version', ?)",
        (str(SCHEMA_VERSION),),
    )
    conn.commit()
    return conn
