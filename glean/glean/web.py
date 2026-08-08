"""
GLEAN web dashboard (design doc §5.5). Lower priority, v1 = simple
read-only auto-refreshing view: endpoint table + anomaly log. Polling,
not websocket push (open question in design doc, deferred to v1 = polling).
"""

from flask import Flask, jsonify, render_template_string

from . import schema

PAGE = """
<!doctype html>
<html>
<head>
  <title>GLEAN</title>
  <meta http-equiv="refresh" content="3">
  <style>
    body { font-family: monospace; background: #111; color: #ddd; padding: 1rem; }
    table { border-collapse: collapse; width: 100%; margin-bottom: 2rem; }
    th, td { border: 1px solid #444; padding: 4px 8px; text-align: left; font-size: 0.85rem; }
    th { background: #222; }
    tr.new { color: #ff6b6b; }
    tr.reviewed { color: #777; }
    h1 { font-size: 1.1rem; }
  </style>
</head>
<body>
  <h1>GLEAN — Grammarly Live Endpoint Analysis (read-only, v1)</h1>
  <p>flows={{ n_flows }} endpoints={{ n_endpoints }} new_anomalies={{ n_new }}</p>

  <table>
    <tr><th>path</th><th>count</th><th>first_seen</th><th>last_seen</th></tr>
    {% for e in endpoints %}
    <tr><td>{{ e['path'] }}</td><td>{{ e['count'] }}</td>
        <td>{{ e['first_seen'] }}</td><td>{{ e['last_seen'] }}</td></tr>
    {% endfor %}
  </table>

  <table>
    <tr><th>id</th><th>type</th><th>detail</th><th>status</th></tr>
    {% for a in anomalies %}
    <tr class="{{ a['status'] }}"><td>{{ a['id'] }}</td><td>{{ a['type'] }}</td>
        <td>{{ a['detail'] }}</td><td>{{ a['status'] }}</td></tr>
    {% endfor %}
  </table>
</body>
</html>
"""


def create_app(db_path: str) -> Flask:
    app = Flask("glean")

    @app.route("/")
    def index():
        conn = schema.connect(db_path)
        endpoints = conn.execute(
            "SELECT path, count, first_seen, last_seen FROM endpoints "
            "ORDER BY last_seen DESC LIMIT 50"
        ).fetchall()
        anomalies = conn.execute(
            "SELECT id, type, detail, status FROM anomalies ORDER BY id DESC LIMIT 50"
        ).fetchall()
        n_flows = conn.execute("SELECT COUNT(*) c FROM flows").fetchone()["c"]
        n_new = conn.execute(
            "SELECT COUNT(*) c FROM anomalies WHERE status='new'"
        ).fetchone()["c"]
        return render_template_string(
            PAGE, endpoints=endpoints, anomalies=anomalies,
            n_flows=n_flows, n_endpoints=len(endpoints), n_new=n_new,
        )

    @app.route("/api/state")
    def api_state():
        conn = schema.connect(db_path)
        endpoints = [dict(r) for r in conn.execute("SELECT * FROM endpoints")]
        anomalies = [dict(r) for r in conn.execute("SELECT * FROM anomalies")]
        return jsonify({"endpoints": endpoints, "anomalies": anomalies})

    return app


def run_web(db_path: str, host: str = "127.0.0.1", port: int = 8081):
    app = create_app(db_path)
    app.run(host=host, port=port)
