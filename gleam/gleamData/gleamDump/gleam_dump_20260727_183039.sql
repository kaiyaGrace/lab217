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
INSERT INTO "http_flows_other" VALUES(1,1.78520223951505208e+09,1.78520223963805198e+09,'POST','http','capi.grammarly.com','/ingest-api/v1/events/ingestion_front_end',200,'application/json','{"agent_id": "abc", "object_id": "def", "event": "keystroke"}','{"status":"ok"}');
INSERT INTO "http_flows_other" VALUES(2,946681200.0,NULL,'POST','http','capi.grammarly.com','/rpc',NULL,'','[connection error: connection reset]','');
INSERT INTO "http_flows_other" VALUES(3,946681200.0,946681203.0,'GET','http','capi.grammarly.com','/path',200,'','{"broken": "json", missing_quotes: True,','not even json at all');
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
    latency_ms REAL,
    token_location TEXT
);
INSERT INTO "rpc_calls" VALUES(1,1.78520223951404881e+09,1.78520223963704872e+09,'POST','http','capi.grammarly.com','/rpc',200,'2.0','doc.analyze','"1"','{"text": "hello"}','{"ok": true}',NULL,'{"header": "qvalue", "content-length": "83", "Host": "capi.grammarly.com", "Content-Type": "application/json", "Authorization": "Bearer sometoken"}','{"header-response": "svalue", "content-length": "53", "Content-Type": "application/json"}',1.22999906539916992e+02,'header');
INSERT INTO "rpc_calls" VALUES(2,1.78520223951468539e+09,1.78520223963768529e+09,'POST','http','capi.grammarly.com','/rpc',200,'2.0','session.refresh','"2"','{"refresh_token": "xyz"}','{"ok": true}',NULL,'{"header": "qvalue", "content-length": "94", "Host": "capi.grammarly.com", "Content-Type": "application/json"}','{"header-response": "svalue", "content-length": "53", "Content-Type": "application/json"}',1.22999906539916992e+02,'body');
INSERT INTO "rpc_calls" VALUES(3,1.78520223951487278e+09,1.78520223963787269e+09,'POST','http','capi.grammarly.com','/rpc',400,'2.0','doc.analyze','"3"','{}',NULL,'{"code": -1, "message": "bad"}','{"header": "qvalue", "content-length": "68", "Host": "capi.grammarly.com", "Content-Type": "application/json"}','{"header-response": "svalue", "content-length": "70", "Content-Type": "application/json"}',1.22999906539916992e+02,NULL);
INSERT INTO "rpc_calls" VALUES(4,1.7852022395159161e+09,1.78520223963891601e+09,'POST','http','capi.grammarly.com','/rpc',200,'2.0','ping','"100"','{}','{}',NULL,'{"header": "qvalue", "content-length": "63", "Host": "capi.grammarly.com", "Content-Type": "application/json"}','{"header-response": "svalue", "content-length": "45", "Content-Type": "application/json"}',1.22999906539916992e+02,NULL);
INSERT INTO "rpc_calls" VALUES(5,1.78520223951747679e+09,1.7852022396404767e+09,'POST','http','capi.grammarly.com','/rpc',200,'2.0','ping','"101"','{}','{}',NULL,'{"header": "qvalue", "content-length": "63", "Host": "capi.grammarly.com", "Content-Type": "application/json"}','{"header-response": "svalue", "content-length": "45", "Content-Type": "application/json"}',1.22999906539916992e+02,NULL);
INSERT INTO "rpc_calls" VALUES(6,1.78520223951767277e+09,1.78520223964067268e+09,'POST','http','capi.grammarly.com','/rpc',200,'2.0','ping','"102"','{}','{}',NULL,'{"header": "qvalue", "content-length": "63", "Host": "capi.grammarly.com", "Content-Type": "application/json"}','{"header-response": "svalue", "content-length": "45", "Content-Type": "application/json"}',1.22999906539916992e+02,NULL);
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
INSERT INTO "ws_flows" VALUES(1,1.78520223951537942e+09,1.78520223951541233e+09,'https','capi.grammarly.com','/ws/ot',2,'{"client_to_server": 1, "server_to_client": 1}');
CREATE TABLE ws_rpc_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp REAL,
    host TEXT,
    path TEXT,
    direction TEXT,
    jsonrpc_version TEXT,
    rpc_method TEXT,
    rpc_id TEXT,
    payload_json TEXT
);
INSERT INTO "ws_rpc_messages" VALUES(1,1.78520223951540255e+09,'capi.grammarly.com','/ws/ot','client_to_server','2.0','doc.edit','"10"','{"jsonrpc": "2.0", "id": "10", "method": "doc.edit", "params": {"delta": "x"}}');
CREATE INDEX idx_wsrpc_host_path_method
    ON ws_rpc_messages(host, path, rpc_method);
CREATE INDEX idx_rpc_host_path_method
    ON rpc_calls(host, path, rpc_method);
CREATE INDEX idx_rpc_ts_request
    ON rpc_calls(timestamp_request);
CREATE INDEX idx_other_host_path
    ON http_flows_other(host, path);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('rpc_calls',6);
INSERT INTO "sqlite_sequence" VALUES('http_flows_other',3);
INSERT INTO "sqlite_sequence" VALUES('ws_flows',1);
INSERT INTO "sqlite_sequence" VALUES('ws_rpc_messages',1);
COMMIT;
