"""Generates a fake 'saved session file' -- same JSON shape `glean export`
produces -- so `glean import` / `glean diff` can be exercised without live
mitmproxy capture."""
import json

def make_session(label):
    flows = []
    for i in range(5):
        flows.append({
            "endpoint_path": "POST /api/check",
            "timestamp": f"2026-07-20T00:00:0{i}Z",
            "request": {"docId": f"doc{i}", "text": "hello world"},
            "response": {"status": "ok", "score": 0.9 + i * 0.01},
            "status_code": 200,
            "duration_ms": 30.0 + i,
        })
    # a schema change partway through: new field appears
    flows.append({
        "endpoint_path": "POST /api/check",
        "timestamp": "2026-07-20T00:00:10Z",
        "request": {"docId": "doc9", "text": "hi", "locale": "en-US"},
        "response": {"status": "ok", "score": 0.5},
        "status_code": 200,
        "duration_ms": 25.0,
    })
    flows.append({
        "endpoint_path": "GET /api/suggestions",
        "timestamp": "2026-07-20T00:00:11Z",
        "request": None,
        "response": {"suggestions": ["a", "b"]},
        "status_code": 200,
        "duration_ms": 12.0,
    })
    return {
        "label": label,
        "host": "frodo",
        "started_at": "2026-07-20T00:00:00Z",
        "ended_at": "2026-07-20T00:00:12Z",
        "flows": flows,
    }

if __name__ == "__main__":
    import sys
    with open(sys.argv[1], "w") as f:
        json.dump(make_session(sys.argv[2] if len(sys.argv) > 2 else "control"), f)
