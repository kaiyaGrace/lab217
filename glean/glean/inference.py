"""
Endpoint & schema inference engine (design doc §5.2).

Field status model (decided, not deferred -- see design doc):
    required          -- seen in every flow so far, never null, never missing
    optional-present  -- seen as null at least once, or key present but not
                         always
    optional-absent   -- the key is sometimes missing entirely

Type tracking stores a *set* of observed types per field (e.g.
{"string", "null"}), not a single type, so a real breaking change
(int -> string) is distinguishable from an optionality discovery
(string -> string|null).
"""

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set


def json_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return "unknown"


def flatten_json(obj: Any, prefix: str = "") -> Dict[str, Any]:
    """Flatten nested JSON into dotted field paths -> leaf/container value.

    Objects recurse into dotted paths (a.b.c). Arrays are represented as a
    single field (a.items) holding the list itself -- we track array
    *presence/type*, not per-index schemas; that's out of scope (see
    design doc non-goals: characterize shape, not fully decode protocol).
    """
    out: Dict[str, Any] = {}
    if isinstance(obj, dict):
        if not obj:
            out[prefix or "$"] = obj
        for k, v in obj.items():
            path = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict):
                out.update(flatten_json(v, path))
            else:
                out[path] = v
    else:
        out[prefix or "$"] = obj
    return out


@dataclass
class FieldModel:
    types: Set[str] = field(default_factory=set)
    status: str = "required"  # required | optional-present | optional-absent
    first_seen: Optional[str] = None
    seen_null_once_flagged: bool = False  # first null->anomaly, then quiet


@dataclass
class EndpointModel:
    path: str
    fields: Dict[str, Dict[str, FieldModel]] = field(
        default_factory=lambda: {"request": {}, "response": {}}
    )
    flow_count: int = 0


class InferenceEngine:
    """In-memory model, one instance per comparison scope (session, or a
    rebuilt all-time/by-label baseline loaded from the DB)."""

    def __init__(self):
        self.endpoints: Dict[str, EndpointModel] = {}

    def observe(
        self, endpoint_path: str, direction: str, payload: Any, timestamp: str
    ) -> List[dict]:
        """Update the model with one flow's payload (request or response
        side) and return a list of anomaly dicts: {type, detail}."""
        anomalies: List[dict] = []
        is_new_endpoint = endpoint_path not in self.endpoints
        if is_new_endpoint:
            self.endpoints[endpoint_path] = EndpointModel(path=endpoint_path)
            anomalies.append(
                {"type": "new_endpoint", "detail": f"new endpoint: {endpoint_path}"}
            )

        ep = self.endpoints[endpoint_path]
        flat = flatten_json(payload) if payload is not None else {}
        seen_paths = set(flat.keys())
        known_fields = ep.fields[direction]

        # Existing known fields not present in this flow -> possibly absent
        for fpath, fmodel in known_fields.items():
            if fpath not in seen_paths:
                if fmodel.status == "required":
                    fmodel.status = "optional-absent"
                    anomalies.append(
                        {
                            "type": "schema_change",
                            "detail": (
                                f"{endpoint_path} [{direction}] field "
                                f"'{fpath}' disappeared (was required)"
                            ),
                        }
                    )
                # already optional -> silently fine, no re-flag

        # Fields present in this flow
        for fpath, value in flat.items():
            vtype = json_type(value)
            if fpath not in known_fields:
                fmodel = FieldModel(
                    types={vtype}, status="required", first_seen=timestamp
                )
                known_fields[fpath] = fmodel
                if not is_new_endpoint:
                    # brand-new field on a known endpoint
                    anomalies.append(
                        {
                            "type": "schema_change",
                            "detail": (
                                f"{endpoint_path} [{direction}] new field "
                                f"'{fpath}' ({vtype})"
                            ),
                        }
                    )
                if vtype == "null":
                    fmodel.status = "optional-present"
                continue

            fmodel = known_fields[fpath]
            is_new_type = vtype not in fmodel.types
            if vtype == "null":
                if fmodel.status == "required" and not fmodel.seen_null_once_flagged:
                    fmodel.seen_null_once_flagged = True
                    anomalies.append(
                        {
                            "type": "schema_change",
                            "detail": (
                                f"{endpoint_path} [{direction}] field "
                                f"'{fpath}' observed null for the first time "
                                f"(was always populated)"
                            ),
                        }
                    )
                fmodel.status = "optional-present"
            elif fmodel.status == "optional-absent":
                # key reappeared -- fine, it's already known-optional
                fmodel.status = "optional-present"

            if is_new_type and vtype != "null":
                # real type change (not just an optionality discovery)
                anomalies.append(
                    {
                        "type": "schema_change",
                        "detail": (
                            f"{endpoint_path} [{direction}] field '{fpath}' "
                            f"type changed: {sorted(fmodel.types)} -> "
                            f"+{vtype}"
                        ),
                    }
                )
            fmodel.types.add(vtype)

        if not is_new_endpoint:
            ep.flow_count += 1
        return anomalies


def canonical_json(obj: Any) -> str:
    """Stable serialization used for hashing (flow_hash) and storage."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)
