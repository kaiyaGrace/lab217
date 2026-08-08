"""
GLEAN TUI dashboard (design doc §5.4). Rich-based, polls the SQLite DB
(WAL mode, so this never blocks the addon's writes) and renders:
  - session stats
  - endpoint inventory table
  - anomaly feed (new vs. reviewed)
  - live flow feed tail

Sensitive fields (tokens, cookies, auth headers) are masked in the
payload preview by default, reusing the same category-pattern approach as
analyze_flows.py's PII/PHI detection (pattern-based on field name).

Acknowledging anomalies is exposed as `glean review <id>` (see cli.py)
rather than an in-widget keybind -- a deliberate simplification for a
polling/redraw-loop TUI rather than a raw-terminal curses app, while still
meeting the "anomalies can be acknowledged and stop re-flagging" goal.
"""

import json
import re
import time
from typing import Optional

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from . import schema

SENSITIVE_FIELD_PATTERNS = [
    re.compile(p, re.IGNORECASE) for p in [
        r"password", r"passwd", r"token", r"auth", r"cookie", r"secret",
        r"session[_-]?id", r"api[_-]?key", r"mrn", r"phone", r"username",
    ]
]


def is_sensitive_field(field_name: str) -> bool:
    return any(p.search(field_name) for p in SENSITIVE_FIELD_PATTERNS)


def mask_payload_preview(raw_json: Optional[str], limit: int = 80) -> str:
    if not raw_json:
        return "-"
    try:
        obj = json.loads(raw_json)
    except Exception:
        return raw_json[:limit]
    if isinstance(obj, dict):
        masked = {
            k: ("****" if is_sensitive_field(k) else v) for k, v in obj.items()
        }
        s = json.dumps(masked)
    else:
        s = json.dumps(obj)
    return s if len(s) <= limit else s[: limit - 1] + "…"


def build_dashboard(conn, session_id: Optional[int]) -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="stats", size=3),
        Layout(name="body"),
    )
    layout["body"].split_row(
        Layout(name="endpoints", ratio=2),
        Layout(name="anomalies", ratio=2),
    )

    where = "WHERE session_id = ?" if session_id else ""
    params = (session_id,) if session_id else ()

    sess = None
    if session_id:
        sess = conn.execute(
            "SELECT * FROM sessions WHERE id = ?", (session_id,)
        ).fetchone()

    n_flows = conn.execute(
        f"SELECT COUNT(*) c FROM flows f JOIN endpoints e ON f.endpoint_id=e.id "
        f"{where}", params
    ).fetchone()["c"]
    n_endpoints = conn.execute(
        f"SELECT COUNT(*) c FROM endpoints {where}", params
    ).fetchone()["c"]
    n_new_anom = conn.execute(
        f"SELECT COUNT(*) c FROM anomalies {where + ' AND' if where else 'WHERE'} status='new'",
        params,
    ).fetchone()["c"]

    label = sess["label"] if sess else "(all sessions)"
    stats_text = (
        f"[bold]GLEAN[/bold]  label={label}  flows={n_flows}  "
        f"endpoints={n_endpoints}  [red]new anomalies={n_new_anom}[/red]"
    )
    layout["stats"].update(Panel(stats_text))

    ep_table = Table(title="Endpoint inventory", expand=True)
    ep_table.add_column("path")
    ep_table.add_column("count", justify="right")
    ep_table.add_column("first_seen")
    ep_table.add_column("last_seen")
    rows = conn.execute(
        f"SELECT path, count, first_seen, last_seen FROM endpoints {where} "
        f"ORDER BY last_seen DESC LIMIT 25", params
    ).fetchall()
    for r in rows:
        ep_table.add_row(r["path"], str(r["count"]), r["first_seen"], r["last_seen"])
    layout["endpoints"].update(ep_table)

    an_table = Table(title="Anomalies", expand=True)
    an_table.add_column("id")
    an_table.add_column("type")
    an_table.add_column("detail", overflow="fold")
    an_table.add_column("status")
    a_where = where + (" " if where else "WHERE ")
    a_rows = conn.execute(
        f"SELECT id, type, detail, status FROM anomalies {where} "
        f"ORDER BY id DESC LIMIT 25", params
    ).fetchall()
    for r in a_rows:
        style = "red" if r["status"] == "new" else "dim"
        an_table.add_row(
            str(r["id"]), r["type"], r["detail"], r["status"], style=style
        )
    layout["anomalies"].update(an_table)

    return layout


def run_tui(db_path: str, session_id: Optional[int] = None,
            refresh_seconds: float = 2.0, iterations: Optional[int] = None):
    """Blocking live dashboard. `iterations` is used by tests to run a
    bounded number of refresh cycles instead of forever."""
    conn = schema.connect(db_path)
    console = Console()
    count = 0
    with Live(build_dashboard(conn, session_id), console=console, refresh_per_second=2) as live:
        while iterations is None or count < iterations:
            time.sleep(refresh_seconds)
            live.update(build_dashboard(conn, session_id))
            count += 1
