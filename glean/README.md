# GLEAN — Grammarly Live Endpoint Analysis

Implementation of `GLEAN_design_doc.md`. Everything the doc's §5 lists as a
component exists here: the mitmproxy addon, inference engine, SQLite
writer/schema, CLI, Rich TUI, read-only web dashboard, and a systemd unit.

```
glean/
  glean/
    schema.py    -- SQLite DDL (§5.3)
    inference.py -- endpoint/schema inference, 3-state field model (§5.2)
    db.py        -- incremental writer, idempotent import, anomaly dedup (§5.3)
    addon.py      -- mitmproxy addon: domain filter + capture (§5.1)
    cli.py        -- glean run/attach/import/export/diff/status/review (§5.6)
    tui.py        -- Rich dashboard (§5.4)
    web.py        -- Flask read-only dashboard (§5.5)
  glean.service   -- systemd unit (§5.7)
  tests/          -- unit tests + synthetic-session generator
  pyproject.toml
```

## Install

```bash
cd glean
pip install -e .          # installs mitmproxy, rich, flask + the `glean` CLI
```

On the real lab NUC (Frodo), mitmproxy's CA cert needs to be trusted by
whatever's generating traffic, same as your existing transparent-proxy
setup — GLEAN doesn't change that part.

## Run it for real (on Frodo, against live Grammarly traffic)

```bash
# dev/manual mode -- foreground, one command (design doc §5.6)
glean run --label control --baseline all --db data/glean.db

# in another terminal, attach the live TUI
glean attach --db data/glean.db --label control

# and/or the web dashboard (starts inside `glean run`'s mitmweb,
# or standalone:)
python3 -m glean.web   # or: python3 -c "from glean.web import run_web; run_web('data/glean.db')"
```

Always-on mode: copy `glean.service` to `/etc/systemd/system/`, edit the
paths/user, then:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now glean.service
glean status --db data/glean.db
```

## Test it (no live traffic needed)

Everything below runs against synthetic data — no root, no mitmproxy
certs, no real Grammarly traffic required. This is how the whole build was
validated.

```bash
cd glean

# 1. Run the full unit test suite (inference engine, DB writer, addon logic)
python3 tests/run_all.py
```

Covers, and asserts on:
- the null-vs-absent 3-state field model (flags once, then goes quiet)
- real type changes vs. optionality discoveries being told apart
- `flow_hash` making `glean import` idempotent (re-import inserts 0 rows)
- anomaly dedup surviving re-import **across sessions** (this one actually
  caught a real bug during development — endpoint_id is session-scoped,
  so dedup had to key off `label + endpoint_path` instead)
- the domain filter (`*.grammarly.{com,io,net}`) matching/rejecting correctly
- WAL mode + foreign keys being on, so the TUI/web dashboard never blocks the writer

```bash
# 2. End-to-end CLI walkthrough with a synthetic session (mimics real capture)
python3 tests/make_synthetic_session.py /tmp/session_control.json control
glean import /tmp/session_control.json --db /tmp/glean_demo.db
glean import /tmp/session_control.json --db /tmp/glean_demo.db   # re-import: should insert 0 new flows/anomalies
glean status --db /tmp/glean_demo.db

# make a second session with a real schema difference and diff them
python3 - <<'PY'
import json
from tests.make_synthetic_session import make_session
data = make_session("test-x")
data["flows"][0]["request"]["newFlag"] = True
json.dump(data, open("/tmp/session_testx.json", "w"))
PY
glean import /tmp/session_testx.json --db /tmp/glean_demo.db
glean diff --a control --b test-x --db /tmp/glean_demo.db
```

```bash
# 3. Look at the live TUI against that demo DB
glean attach --db /tmp/glean_demo.db --label control
# Ctrl+C to exit. Acknowledge an anomaly from another terminal:
glean review 1 --db /tmp/glean_demo.db
```

```bash
# 4. Web dashboard against the same demo DB
python3 -c "from glean.web import run_web; run_web('/tmp/glean_demo.db', port=8081)"
# then open http://127.0.0.1:8081
```

## What's a simplification vs. the design doc (worth knowing before relying on it)

- **Anomaly acknowledgment** is `glean review <id>` from a second terminal,
  not an in-widget keybind — Rich's polling `Live` redraw loop doesn't do
  raw-terminal keyboard input cleanly. Functionally equivalent (writes
  synchronously, stops re-flagging, appends to the log) — just not a
  single keypress inside the TUI itself.
- **`glean export`** isn't in the doc's original CLI list but had to be
  added — `glean import` needs *something* to import, and the doc's
  "saved session files" weren't given an explicit format. It's a thin
  JSON dump of one session's flows.
- **Web dashboard** is intentionally the v1 scope the doc calls for:
  polling (3s meta-refresh), read-only, no websocket push.
