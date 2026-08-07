BEGIN TRANSACTION;
CREATE TABLE http_flows_other (
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
CREATE TABLE rpc_calls (
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
    latency_ms REAL
);
CREATE TABLE ws_flows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp_open REAL,
    timestamp_close REAL,
    scheme TEXT,
    host TEXT,
    path TEXT,
    message_count INTEGER,
    direction_counts_json TEXT
);
CREATE INDEX idx_rpc_host_path_method
    ON rpc_calls(host, path, rpc_method);
CREATE INDEX idx_rpc_ts_request
    ON rpc_calls(timestamp_request);
CREATE INDEX idx_other_host_path
    ON http_flows_other(host, path);
DELETE FROM "sqlite_sequence";
COMMIT;
