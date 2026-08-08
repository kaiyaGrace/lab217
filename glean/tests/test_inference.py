import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from glean.inference import InferenceEngine, flatten_json, json_type


def test_new_endpoint_flags_once():
    eng = InferenceEngine()
    a = eng.observe("POST /a", "request", {"x": 1}, "t1")
    assert any(x["type"] == "new_endpoint" for x in a)
    b = eng.observe("POST /a", "request", {"x": 2}, "t2")
    assert not any(x["type"] == "new_endpoint" for x in b)
    print("ok: new_endpoint flags exactly once")


def test_new_field_on_known_endpoint_flags():
    eng = InferenceEngine()
    eng.observe("POST /a", "request", {"x": 1}, "t1")
    a2 = eng.observe("POST /a", "request", {"x": 1, "y": 2}, "t2")
    assert any("new field 'y'" in x["detail"] for x in a2), a2
    print("ok: brand-new field on known endpoint flags")


def test_null_first_time_flags_once_then_quiet():
    eng = InferenceEngine()
    eng.observe("POST /a", "request", {"x": 1}, "t1")   # x required
    a2 = eng.observe("POST /a", "request", {"x": None}, "t2")  # first null
    assert any("observed null for the first time" in x["detail"] for x in a2), a2
    a3 = eng.observe("POST /a", "request", {"x": None}, "t3")  # second null: quiet
    assert not any("null" in x["detail"] for x in a3), a3
    a4 = eng.observe("POST /a", "request", {"x": 5}, "t4")     # back to int: quiet
    assert not any("type changed" in x["detail"] for x in a4), a4
    print("ok: null-first-time semantics correct")


def test_missing_key_absent_then_reappear_quiet():
    eng = InferenceEngine()
    eng.observe("POST /a", "request", {"x": 1, "y": 2}, "t1")  # both required
    a2 = eng.observe("POST /a", "request", {"x": 1}, "t2")  # y missing -> flag once
    assert any("disappeared" in x["detail"] for x in a2), a2
    a3 = eng.observe("POST /a", "request", {"x": 1}, "t3")  # still missing -> quiet
    assert not any("disappeared" in x["detail"] for x in a3), a3
    a4 = eng.observe("POST /a", "request", {"x": 1, "y": 2}, "t4")  # reappears -> quiet
    assert not any("disappeared" in x["detail"] or "new field" in x["detail"] for x in a4), a4
    print("ok: absent-field lifecycle correct")


def test_real_type_change_flags():
    eng = InferenceEngine()
    eng.observe("POST /a", "request", {"x": 1}, "t1")
    a2 = eng.observe("POST /a", "request", {"x": "one"}, "t2")
    assert any("type changed" in x["detail"] for x in a2), a2
    print("ok: real int->string type change flags")


def test_type_set_distinguishes_optionality_from_real_change():
    eng = InferenceEngine()
    eng.observe("POST /a", "request", {"x": 1}, "t1")
    eng.observe("POST /a", "request", {"x": None}, "t2")  # optionality discovery
    model = eng.endpoints["POST /a"].fields["request"]["x"]
    assert model.types == {"number", "null"}
    assert model.status == "optional-present"
    print("ok: type set + status reflect optionality, not a breaking change")


def test_flatten_nested_json():
    flat = flatten_json({"a": {"b": 1, "c": {"d": 2}}, "e": [1, 2]})
    assert flat == {"a.b": 1, "a.c.d": 2, "e": [1, 2]}
    print("ok: nested json flattens to dotted paths, arrays kept whole")


def test_json_type():
    assert json_type(None) == "null"
    assert json_type(True) == "boolean"
    assert json_type(1) == "number"
    assert json_type("s") == "string"
    assert json_type([1]) == "array"
    assert json_type({"a": 1}) == "object"
    print("ok: json_type covers all JSON scalar/container kinds")


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("\nALL INFERENCE TESTS PASSED")
