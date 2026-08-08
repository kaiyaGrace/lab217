import sys, os, tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from glean.addon import domain_matches, try_parse_json, GleanAddon
from glean import schema


def test_domain_matches_seeded_filter():
    assert domain_matches("app.grammarly.com")
    assert domain_matches("api.grammarly.io")
    assert domain_matches("cdn.grammarly.net")
    assert domain_matches("grammarly.com")
    assert not domain_matches("notgrammarly.com")
    assert not domain_matches("grammarly.com.evil.net")
    print("ok: seeded *.grammarly.{com,io,net} filter matches correctly")


def test_try_parse_json():
    assert try_parse_json(b'{"a": 1}') == {"a": 1}
    assert try_parse_json(b'not json') is None
    assert try_parse_json(None) is None
    assert try_parse_json(b'') is None
    print("ok: non-JSON / empty bodies safely ignored (out of scope, not a crash)")


def test_addon_handle_flow_end_to_end():
    """Exercises GleanAddon.handle_flow directly -- the part of the addon
    that's independent of mitmproxy's actual flow objects -- so we can
    verify capture -> inference -> DB without root/live traffic."""
    tmp = tempfile.mktemp(suffix=".db")
    addon = GleanAddon()
    addon.conn = schema.init_db(tmp)
    from glean import db as dbmod
    addon.session_id = dbmod.start_session(addon.conn, "test", "sandbox")
    addon.label = "test"
    addon.log_path = None

    r1 = addon.handle_flow(
        endpoint_path="POST /api/check",
        timestamp="t1",
        request_raw=b'{"docId": "abc", "text": "hello"}',
        response_raw=b'{"status": "ok", "score": 1}',
        status_code=200,
        duration_ms=42.0,
    )
    assert any(a["type"] == "new_endpoint" for a in r1)

    r2 = addon.handle_flow(
        endpoint_path="POST /api/check",
        timestamp="t2",
        request_raw=b'{"docId": "abc", "text": "hello", "lang": "en"}',  # new field
        response_raw=b'{"status": "ok", "score": null}',                 # first null
        status_code=200,
        duration_ms=40.0,
    )
    assert any("new field 'lang'" in a["detail"] for a in r2), r2
    assert any("observed null for the first time" in a["detail"] for a in r2), r2

    # non-JSON traffic on a filtered domain is simply skipped, not an error
    r3 = addon.handle_flow(
        endpoint_path="GET /static/app.js",
        timestamp="t3",
        request_raw=None,
        response_raw=b"function(){}",
        status_code=200,
        duration_ms=5.0,
    )
    assert r3 is None

    n_flows = addon.conn.execute("SELECT COUNT(*) c FROM flows").fetchone()["c"]
    assert n_flows == 2  # static asset never wrote a flow row
    print("ok: addon.handle_flow captures JSON RPC traffic end-to-end, "
          "skips non-JSON, and flags anomalies live")
    os.remove(tmp)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("\nALL ADDON TESTS PASSED")
