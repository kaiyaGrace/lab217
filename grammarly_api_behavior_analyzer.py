#!/usr/bin/env python3

"""
grammarly_api_behavior_analyzer.py

Analyze a mitmweb/mitmproxy saved flow file for Grammarly API behavior.

Outputs:
    <input>_analysis/
        report.md
        endpoints.csv
        request_fields.csv
        response_fields.csv
        endpoint_examples.csv
        behavior_timeline.csv

The analyzer:
    - Identifies Grammarly traffic using hostname, :authority, SNI,
      URLs, and request/response metadata.
    - Handles HTTP/2 captures where request.host may be an IP address.
    - Detects JSON bodies even when Content-Type is text/plain.
    - Extracts endpoint paths and HTTP methods.
    - Builds endpoint trees.
    - Extracts JSON field paths and value types.
    - Tracks field frequency.
    - Tracks request/response sizes.
    - Records timestamps.
    - Redacts obvious sensitive values.
    - Avoids dumping giant raw JSON bodies into the report.
"""

import sys
import os
import re
import json
import csv
import hashlib
from collections import Counter, defaultdict
from datetime import datetime, timezone

from mitmproxy import io


# ============================================================
# CONFIGURATION
# ============================================================

GRAMMARLY_HOST_PATTERNS = (
    "grammarly.com",
    "grammarly.io",
    "grammarly.localhost",
    "grammarly.ai",
)

OUTPUT_SUFFIX = "_analysis"

MAX_EXAMPLE_LENGTH = 300

# Fields whose VALUES should never be written to output.
SENSITIVE_FIELD_PATTERNS = (
    "token",
    "access_token",
    "refresh_token",
    "authorization",
    "cookie",
    "password",
    "passwd",
    "secret",
    "api_key",
    "apikey",
    "email",
    "user_id",
    "account_id",
    "session_id",
    "device_id",
    "container_id",
    "referral_container_id",
)


# ============================================================
# HELPERS
# ============================================================

def safe_text(value):
    """Convert bytes/objects to safe text."""
    if value is None:
        return ""

    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")

    return str(value)


def normalize_host(value):
    """Normalize a hostname."""
    if not value:
        return ""

    value = safe_text(value).strip().lower()

    # Remove port.
    if value.startswith("["):
        end = value.find("]")
        if end != -1:
            value = value[1:end]
    elif ":" in value:
        # Only strip port if it looks like hostname:port.
        parts = value.rsplit(":", 1)
        if len(parts) == 2 and parts[1].isdigit():
            value = parts[0]

    return value.rstrip(".")


def is_grammarly_host(host):
    """Return True if hostname looks like Grammarly infrastructure."""
    host = normalize_host(host)

    if not host:
        return False

    for pattern in GRAMMARLY_HOST_PATTERNS:
        if host == pattern or host.endswith("." + pattern):
            return True

    return False


def get_header(headers, name):
    """Case-insensitive header lookup."""
    try:
        for key, value in headers.items():
            if str(key).lower() == name.lower():
                return safe_text(value)
    except Exception:
        pass

    return ""


def get_all_header_values(headers, name):
    values = []

    try:
        for key, value in headers.items():
            if str(key).lower() == name.lower():
                values.append(safe_text(value))
    except Exception:
        pass

    return values


def get_authority(flow):
    """
    HTTP/2 :authority is especially important.

    In the user's capture:
        host      = 54.209.50.10
        authority = inkwell.femetrics.grammarly.io
    """

    request = getattr(flow, "request", None)

    if request is None:
        return ""

    # First try normal authority attribute.
    for attr in ("authority", "host_header"):
        try:
            value = getattr(request, attr, "")
            if value:
                return normalize_host(value)
        except Exception:
            pass

    # Then headers.
    try:
        value = get_header(request.headers, ":authority")
        if value:
            return normalize_host(value)
    except Exception:
        pass

    return ""


def get_sni(flow):
    """Extract TLS SNI when available."""
    for connection_name in ("server_conn", "client_conn"):
        conn = getattr(flow, connection_name, None)

        if conn is None:
            continue

        for attr in ("sni", "address"):
            try:
                value = getattr(conn, attr, None)

                if attr == "address":
                    # address may be (host, port)
                    if isinstance(value, tuple) and value:
                        value = value[0]

                if value:
                    value = normalize_host(value)

                    if is_grammarly_host(value):
                        return value
            except Exception:
                pass

    return ""


def get_candidate_hosts(flow):
    """Return every hostname-like value available in a flow."""
    candidates = []

    request = getattr(flow, "request", None)

    if request is not None:

        for attr in ("host", "authority", "host_header"):
            try:
                value = getattr(request, attr, "")
                if value:
                    candidates.append(normalize_host(value))
            except Exception:
                pass

        try:
            authority = get_header(request.headers, ":authority")
            if authority:
                candidates.append(normalize_host(authority))
        except Exception:
            pass

        try:
            url = getattr(request, "pretty_url", "")
            if url:
                match = re.match(r"^[a-zA-Z]+://([^/:]+)", url)
                if match:
                    candidates.append(normalize_host(match.group(1)))
        except Exception:
            pass

    sni = get_sni(flow)

    if sni:
        candidates.append(sni)

    return list(dict.fromkeys(x for x in candidates if x))


def is_grammarly_flow(flow):
    """
    Robust Grammarly detection.

    IMPORTANT:
    Do NOT depend only on request.host.
    HTTP/2 captures can have an IP there while :authority/SNI contains
    the actual Grammarly hostname.
    """

    candidates = get_candidate_hosts(flow)

    for host in candidates:
        if is_grammarly_host(host):
            return True

    # Last-resort URL/path inspection.
    request = getattr(flow, "request", None)

    if request is not None:
        try:
            url = safe_text(getattr(request, "pretty_url", ""))
            if "grammarly.com" in url.lower():
                return True
            if "grammarly.io" in url.lower():
                return True
        except Exception:
            pass

    return False


def get_best_host(flow):
    """Choose the most useful Grammarly hostname."""
    candidates = get_candidate_hosts(flow)

    for host in candidates:
        if is_grammarly_host(host):
            return host

    return candidates[0] if candidates else ""


def get_path(flow):
    request = getattr(flow, "request", None)

    if request is None:
        return ""

    try:
        path = getattr(request, "path", "")
        if path:
            return safe_text(path)
    except Exception:
        pass

    try:
        url = getattr(request, "pretty_url", "")
        if url:
            match = re.match(r"^[a-zA-Z]+://[^/]+(.*)$", url)
            if match:
                return match.group(1) or "/"
    except Exception:
        pass

    return ""


def get_method(flow):
    request = getattr(flow, "request", None)

    if request is None:
        return ""

    try:
        return safe_text(getattr(request, "method", "")).upper()
    except Exception:
        return ""


def get_body(flow, direction):
    """Return request or response body as bytes."""
    try:
        if direction == "request":
            obj = getattr(flow, "request", None)
        else:
            obj = getattr(flow, "response", None)

        if obj is None:
            return b""

        content = getattr(obj, "content", None)

        if content is None:
            return b""

        if isinstance(content, bytes):
            return content

        return safe_text(content).encode("utf-8", errors="replace")

    except Exception:
        return b""


def looks_like_json_text(text):
    """Cheap JSON detection without relying on Content-Type."""
    if not text:
        return False

    stripped = text.strip()

    if not stripped:
        return False

    if stripped[0] in "{[" and stripped[-1:] in "}]":
        return True

    # Sometimes JSON has whitespace/BOM.
    stripped = stripped.lstrip("\ufeff").strip()

    return (
        (stripped.startswith("{") and stripped.endswith("}"))
        or
        (stripped.startswith("[") and stripped.endswith("]"))
    )


def parse_json_body(body):
    """
    Attempt JSON parsing regardless of Content-Type.

    This is important because the sample Grammarly telemetry uses:
        content-type: text/plain;charset=UTF-8

    while containing JSON.
    """

    if not body:
        return None

    text = body.decode("utf-8", errors="replace")

    # Try normal JSON.
    try:
        return json.loads(text)
    except Exception:
        pass

    # Try stripping UTF-8 BOM.
    try:
        text2 = text.lstrip("\ufeff").strip()
        return json.loads(text2)
    except Exception:
        pass

    return None


def json_type(value):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return "boolean"

    if isinstance(value, int) and not isinstance(value, bool):
        return "integer"

    if isinstance(value, float):
        return "number"

    if isinstance(value, str):
        return "string"

    if isinstance(value, list):
        return "array"

    if isinstance(value, dict):
        return "object"

    return type(value).__name__


def is_sensitive_field(path):
    """Determine whether a JSON field path contains sensitive data."""
    lower = path.lower()

    for pattern in SENSITIVE_FIELD_PATTERNS:
        if pattern in lower:
            return True

    return False


def redact_value(path, value):
    """
    Preserve useful schema information while hiding sensitive values.
    """

    if is_sensitive_field(path):
        if value is None:
            return None

        return "<REDACTED>"

    if isinstance(value, dict):
        return {
            key: redact_value(
                f"{path}.{key}" if path else key,
                val
            )
            for key, val in value.items()
        }

    if isinstance(value, list):
        result = []

        for item in value[:10]:
            result.append(
                redact_value(path + "[]", item)
            )

        if len(value) > 10:
            result.append("<...>")

        return result

    if isinstance(value, str):
        if len(value) > MAX_EXAMPLE_LENGTH:
            return value[:MAX_EXAMPLE_LENGTH] + "...<TRUNCATED>"

    return value


def extract_json_fields(value, prefix=""):
    """
    Return:
        field_path -> set(types)

    Example:

        {
            "client": "windows",
            "device": {
                "system_name": "Windows"
            }
        }

    becomes:

        client -> string
        device -> object
        device.system_name -> string
    """

    fields = defaultdict(set)

    if isinstance(value, dict):

        for key, child in value.items():

            key = str(key)

            path = f"{prefix}.{key}" if prefix else key

            fields[path].add(json_type(child))

            child_fields = extract_json_fields(child, path)

            for child_path, child_types in child_fields.items():
                fields[child_path].update(child_types)

    elif isinstance(value, list):

        array_path = prefix + "[]" if prefix else "[]"

        fields[array_path].add("array")

        for item in value[:20]:

            if isinstance(item, (dict, list)):
                child_fields = extract_json_fields(
                    item,
                    array_path
                )

                for child_path, child_types in child_fields.items():
                    fields[child_path].update(child_types)

            else:
                fields[array_path].add(json_type(item))

    return fields


def timestamp_to_string(timestamp):
    if not timestamp:
        return ""

    try:
        dt = datetime.fromtimestamp(
            float(timestamp),
            tz=timezone.utc
        )

        return dt.isoformat()
    except Exception:
        return safe_text(timestamp)


def get_timestamp(flow):
    request = getattr(flow, "request", None)

    if request is not None:
        for attr in ("timestamp_start", "timestamp_created"):
            try:
                value = getattr(request, attr, None)

                if value:
                    return float(value)
            except Exception:
                pass

    return None


def flow_id(flow):
    """Create a stable short ID for the flow."""
    try:
        value = getattr(flow, "id", None)

        if value:
            return safe_text(value)
    except Exception:
        pass

    raw = (
        get_best_host(flow)
        + "|"
        + get_method(flow)
        + "|"
        + get_path(flow)
        + "|"
        + str(get_timestamp(flow))
    )

    return hashlib.sha1(raw.encode()).hexdigest()[:16]


def short_example(value):
    """Compact redacted JSON example."""
    try:
        value = redact_value("", value)

        text = json.dumps(
            value,
            ensure_ascii=False,
            separators=(",", ":")
        )

        if len(text) > MAX_EXAMPLE_LENGTH:
            text = text[:MAX_EXAMPLE_LENGTH] + "...<TRUNCATED>"

        return text

    except Exception:
        return "<UNSERIALIZABLE>"


# ============================================================
# DATA STRUCTURES
# ============================================================

endpoint_stats = defaultdict(
    lambda: {
        "count": 0,
        "methods": Counter(),
        "hosts": Counter(),
        "request_json": 0,
        "response_json": 0,
        "request_bytes": 0,
        "response_bytes": 0,
        "first_timestamp": None,
        "last_timestamp": None,
    }
)

request_fields = defaultdict(
    lambda: {
        "count": 0,
        "types": Counter(),
        "examples": [],
        "endpoints": Counter(),
    }
)

response_fields = defaultdict(
    lambda: {
        "count": 0,
        "types": Counter(),
        "examples": [],
        "endpoints": Counter(),
    }
)

endpoint_examples = []

timeline = []

host_counts = Counter()
path_counts = Counter()
method_counts = Counter()

total_flows = 0
grammarly_flows = 0
json_requests = 0
json_responses = 0


# ============================================================
# PROCESS ONE FLOW
# ============================================================

def process_flow(flow):

    global total_flows
    global grammarly_flows
    global json_requests
    global json_responses

    total_flows += 1

    if not is_grammarly_flow(flow):
        return

    grammarly_flows += 1

    host = get_best_host(flow)
    method = get_method(flow)
    path = get_path(flow)
    timestamp = get_timestamp(flow)

    host_counts[host] += 1
    path_counts[path] += 1
    method_counts[method] += 1

    endpoint_key = f"{method} {path}"

    stats = endpoint_stats[endpoint_key]

    stats["count"] += 1
    stats["methods"][method] += 1
    stats["hosts"][host] += 1

    req_body = get_body(flow, "request")
    resp_body = get_body(flow, "response")

    stats["request_bytes"] += len(req_body)
    stats["response_bytes"] += len(resp_body)

    if timestamp:

        if (
            stats["first_timestamp"] is None
            or timestamp < stats["first_timestamp"]
        ):
            stats["first_timestamp"] = timestamp

        if (
            stats["last_timestamp"] is None
            or timestamp > stats["last_timestamp"]
        ):
            stats["last_timestamp"] = timestamp

    # --------------------------------------------------------
    # REQUEST JSON
    # --------------------------------------------------------

    req_json = parse_json_body(req_body)

    if req_json is not None:

        json_requests += 1
        stats["request_json"] += 1

        fields = extract_json_fields(req_json)

        for field_path, types in fields.items():

            key = (endpoint_key, field_path)

            entry = request_fields[key]

            entry["count"] += 1
            entry["endpoints"][endpoint_key] += 1

            for t in types:
                entry["types"][t] += 1

            if len(entry["examples"]) < 3:

                # Try to find actual field value.
                # We use a helper rather than dumping the whole object.
                value = find_json_path(req_json, field_path)

                example = short_example(value)

                if example not in entry["examples"]:
                    entry["examples"].append(example)

    # --------------------------------------------------------
    # RESPONSE JSON
    # --------------------------------------------------------

    resp_json = parse_json_body(resp_body)

    if resp_json is not None:

        json_responses += 1
        stats["response_json"] += 1

        fields = extract_json_fields(resp_json)

        for field_path, types in fields.items():

            key = (endpoint_key, field_path)

            entry = response_fields[key]

            entry["count"] += 1
            entry["endpoints"][endpoint_key] += 1

            for t in types:
                entry["types"][t] += 1

            if len(entry["examples"]) < 3:

                value = find_json_path(resp_json, field_path)

                example = short_example(value)

                if example not in entry["examples"]:
                    entry["examples"].append(example)

    # --------------------------------------------------------
    # ENDPOINT EXAMPLE
    # --------------------------------------------------------

    if len(endpoint_examples) < 10000:

        endpoint_examples.append({
            "flow_id": flow_id(flow),
            "timestamp": timestamp_to_string(timestamp),
            "host": host,
            "method": method,
            "path": path,
            "request_bytes": len(req_body),
            "response_bytes": len(resp_body),
            "request_json": "yes" if req_json is not None else "no",
            "response_json": "yes" if resp_json is not None else "no",
            "request_example": (
                short_example(req_json)
                if req_json is not None
                else ""
            ),
            "response_example": (
                short_example(resp_json)
                if resp_json is not None
                else ""
            ),
        })

    # --------------------------------------------------------
    # TIMELINE
    # --------------------------------------------------------

    timeline.append({
        "timestamp": timestamp_to_string(timestamp),
        "timestamp_epoch": timestamp if timestamp else "",
        "host": host,
        "method": method,
        "path": path,
        "request_bytes": len(req_body),
        "response_bytes": len(resp_body),
        "request_json": "yes" if req_json is not None else "no",
        "response_json": "yes" if resp_json is not None else "no",
    })


# ============================================================
# JSON PATH LOOKUP
# ============================================================

def find_json_path(data, path):
    """
    Find a value using a dotted field path.

    Handles paths such as:
        client
        device.system_name
        labels[]
    """

    if not path:
        return data

    parts = path.split(".")

    current = data

    for part in parts:

        if part.endswith("[]"):
            part = part[:-2]

            if isinstance(current, dict):
                current = current.get(part)

            if isinstance(current, list):
                if current:
                    current = current[0]
                else:
                    return None

            continue

        if isinstance(current, dict):

            if part not in current:
                return None

            current = current[part]

        elif isinstance(current, list):

            if not current:
                return None

            current = current[0]

        else:
            return None

    return current


# ============================================================
# CSV WRITER
# ============================================================

def write_csv(path, fieldnames, rows):

    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
            extrasaction="ignore"
        )

        writer.writeheader()

        for row in rows:
            writer.writerow(row)


# ============================================================
# WRITE RESULTS
# ============================================================

def write_results(output_dir):

    os.makedirs(output_dir, exist_ok=True)

    # --------------------------------------------------------
    # ENDPOINTS CSV
    # --------------------------------------------------------

    endpoint_rows = []

    for endpoint, stats in sorted(
        endpoint_stats.items(),
        key=lambda x: (-x[1]["count"], x[0])
    ):

        endpoint_rows.append({
            "endpoint": endpoint,
            "count": stats["count"],
            "methods": "; ".join(
                f"{k}={v}"
                for k, v in stats["methods"].items()
            ),
            "hosts": "; ".join(
                f"{k}={v}"
                for k, v in stats["hosts"].items()
            ),
            "json_requests": stats["request_json"],
            "json_responses": stats["response_json"],
            "request_bytes": stats["request_bytes"],
            "response_bytes": stats["response_bytes"],
            "first_seen": timestamp_to_string(
                stats["first_timestamp"]
            ),
            "last_seen": timestamp_to_string(
                stats["last_timestamp"]
            ),
        })

    write_csv(
        os.path.join(output_dir, "endpoints.csv"),
        [
            "endpoint",
            "count",
            "methods",
            "hosts",
            "json_requests",
            "json_responses",
            "request_bytes",
            "response_bytes",
            "first_seen",
            "last_seen",
        ],
        endpoint_rows
    )

    # --------------------------------------------------------
    # REQUEST FIELDS CSV
    # --------------------------------------------------------

    request_rows = []

    for (endpoint, field), entry in sorted(
        request_fields.items()
    ):

        request_rows.append({
            "endpoint": endpoint,
            "field": field,
            "count": entry["count"],
            "types": "; ".join(
                f"{k}={v}"
                for k, v in entry["types"].items()
            ),
            "examples": " | ".join(entry["examples"]),
        })

    write_csv(
        os.path.join(output_dir, "request_fields.csv"),
        [
            "endpoint",
            "field",
            "count",
            "types",
            "examples",
        ],
        request_rows
    )

    # --------------------------------------------------------
    # RESPONSE FIELDS CSV
    # --------------------------------------------------------

    response_rows = []

    for (endpoint, field), entry in sorted(
        response_fields.items()
    ):

        response_rows.append({
            "endpoint": endpoint,
            "field": field,
            "count": entry["count"],
            "types": "; ".join(
                f"{k}={v}"
                for k, v in entry["types"].items()
            ),
            "examples": " | ".join(entry["examples"]),
        })

    write_csv(
        os.path.join(output_dir, "response_fields.csv"),
        [
            "endpoint",
            "field",
            "count",
            "types",
            "examples",
        ],
        response_rows
    )

    # --------------------------------------------------------
    # EXAMPLES CSV
    # --------------------------------------------------------

    write_csv(
        os.path.join(output_dir, "endpoint_examples.csv"),
        [
            "flow_id",
            "timestamp",
            "host",
            "method",
            "path",
            "request_bytes",
            "response_bytes",
            "request_json",
            "response_json",
            "request_example",
            "response_example",
        ],
        endpoint_examples
    )

    # --------------------------------------------------------
    # TIMELINE CSV
    # --------------------------------------------------------

    timeline.sort(
        key=lambda x: (
            x["timestamp_epoch"]
            if x["timestamp_epoch"] != ""
            else 0
        )
    )

    write_csv(
        os.path.join(output_dir, "behavior_timeline.csv"),
        [
            "timestamp",
            "timestamp_epoch",
            "host",
            "method",
            "path",
            "request_bytes",
            "response_bytes",
            "request_json",
            "response_json",
        ],
        timeline
    )

    # --------------------------------------------------------
    # REPORT
    # --------------------------------------------------------

    report_path = os.path.join(
        output_dir,
        "report.md"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write("# Grammarly API Behavior Analysis\n\n")

        f.write("## Summary\n\n")

        f.write(f"- Total flows: **{total_flows:,}**\n")
        f.write(f"- Grammarly flows: **{grammarly_flows:,}**\n")
        f.write(f"- JSON requests: **{json_requests:,}**\n")
        f.write(f"- JSON responses: **{json_responses:,}**\n")
        f.write(
            f"- Unique endpoints: **{len(endpoint_stats):,}**\n"
        )
        f.write(
            f"- Unique request fields: "
            f"**{len(request_fields):,}**\n"
        )
        f.write(
            f"- Unique response fields: "
            f"**{len(response_fields):,}**\n\n"
        )

        # ----------------------------------------------------
        # HOSTS
        # ----------------------------------------------------

        f.write("## Grammarly Hosts\n\n")

        f.write("| Host | Flows |\n")
        f.write("|---|---:|\n")

        for host, count in host_counts.most_common():

            f.write(
                f"| `{host}` | {count:,} |\n"
            )

        f.write("\n")

        # ----------------------------------------------------
        # ENDPOINT TREE
        # ----------------------------------------------------

        f.write("## Endpoint Tree\n\n")

        tree = {}

        for endpoint in endpoint_stats:

            try:
                method, path = endpoint.split(" ", 1)
            except ValueError:
                method = ""
                path = endpoint

            if not path:
                path = "/"

            parts = [
                x for x in path.split("/")
                if x
            ]

            current = tree

            for part in parts:
                current = current.setdefault(part, {})

        def write_tree(node, prefix="", indent=0):

            for name in sorted(node):

                child = node[name]

                f.write(
                    "  " * indent
                    + "- "
                    + name
                    + "\n"
                )

                write_tree(
                    child,
                    prefix + "/" + name,
                    indent + 1
                )

        write_tree(tree)

        f.write("\n")

        # ----------------------------------------------------
        # TOP ENDPOINTS
        # ----------------------------------------------------

        f.write("## Endpoints\n\n")

        f.write(
            "| Endpoint | Requests | JSON req | JSON resp | Host(s) |\n"
        )

        f.write(
            "|---|---:|---:|---:|---|\n"
        )

        for endpoint, stats in sorted(
            endpoint_stats.items(),
            key=lambda x: (-x[1]["count"], x[0])
        ):

            hosts = ", ".join(
                stats["hosts"].keys()
            )

            f.write(
                f"| `{endpoint}` | "
                f"{stats['count']:,} | "
                f"{stats['request_json']:,} | "
                f"{stats['response_json']:,} | "
                f"{hosts} |\n"
            )

        f.write("\n")

        # ----------------------------------------------------
        # REQUEST SCHEMAS
        # ----------------------------------------------------

        f.write("## Request JSON Fields by Endpoint\n\n")

        fields_by_endpoint = defaultdict(list)

        for (endpoint, field), entry in request_fields.items():

            fields_by_endpoint[endpoint].append(
                (field, entry)
            )

        for endpoint in sorted(fields_by_endpoint):

            f.write(f"### `{endpoint}`\n\n")

            f.write("| Field | Count | Type(s) | Example |\n")
            f.write("|---|---:|---|---|\n")

            for field, entry in sorted(
                fields_by_endpoint[endpoint],
                key=lambda x: (-x[1]["count"], x[0])
            ):

                types = ", ".join(
                    entry["types"].keys()
                )

                example = (
                    entry["examples"][0]
                    if entry["examples"]
                    else ""
                )

                f.write(
                    f"| `{field}` | "
                    f"{entry['count']:,} | "
                    f"{types} | "
                    f"`{example}` |\n"
                )

            f.write("\n")

        # ----------------------------------------------------
        # RESPONSE SCHEMAS
        # ----------------------------------------------------

        f.write("## Response JSON Fields by Endpoint\n\n")

        fields_by_endpoint = defaultdict(list)

        for (endpoint, field), entry in response_fields.items():

            fields_by_endpoint[endpoint].append(
                (field, entry)
            )

        for endpoint in sorted(fields_by_endpoint):

            f.write(f"### `{endpoint}`\n\n")

            f.write("| Field | Count | Type(s) | Example |\n")
            f.write("|---|---:|---|---|\n")

            for field, entry in sorted(
                fields_by_endpoint[endpoint],
                key=lambda x: (-x[1]["count"], x[0])
            ):

                types = ", ".join(
                    entry["types"].keys()
                )

                example = (
                    entry["examples"][0]
                    if entry["examples"]
                    else ""
                )

                f.write(
                    f"| `{field}` | "
                    f"{entry['count']:,} | "
                    f"{types} | "
                    f"`{example}` |\n"
                )

            f.write("\n")

        # ----------------------------------------------------
        # NOTES
        # ----------------------------------------------------

        f.write("## Analysis Notes\n\n")

        f.write(
            "- Grammarly traffic was identified using hostname, "
            "HTTP/2 `:authority`, TLS SNI, and URL information.\n"
        )

        f.write(
            "- JSON detection does **not** depend solely on "
            "`Content-Type`; this is important because some "
            "Grammarly telemetry uses `text/plain` while carrying "
            "JSON bodies.\n"
        )

        f.write(
            "- Sensitive field values are redacted from examples.\n"
        )

        f.write(
            "- Field paths represent observed wire-level JSON "
            "structure and should not automatically be interpreted "
            "as server-side function arguments.\n"
        )

    return report_path


# ============================================================
# MAIN
# ============================================================

def main():

    if len(sys.argv) != 2:

        print(
            "\nUsage:\n"
            "    python3 grammarly_api_behavior_analyzer.py "
            "<mitmweb_flow_file>\n"
        )

        print(
            "Example:\n"
            "    python3 grammarly_api_behavior_analyzer.py "
            "~/mitmWebLogs/mitmWebPrac_2\n"
        )

        sys.exit(1)

    flow_file = os.path.expanduser(sys.argv[1])

    if not os.path.isfile(flow_file):

        print(
            f"\nERROR: File not found:\n{flow_file}\n"
        )

        sys.exit(1)

    output_dir = (
        flow_file
        + OUTPUT_SUFFIX
    )

    print()
    print("=" * 60)
    print("GRAMMARLY API BEHAVIOR ANALYZER")
    print("=" * 60)
    print()
    print(f"Input:  {flow_file}")
    print(f"Output: {output_dir}")
    print()
    print("Reading mitmweb flow file...")
    print()

    try:

        with open(flow_file, "rb") as f:

            reader = io.FlowReader(f)

            for index, flow in enumerate(
                reader.stream(),
                start=1
            ):

                try:
                    process_flow(flow)

                except Exception as e:

                    # One malformed flow should not kill a 75 MB capture.
                    if index <= 20:
                        print(
                            f"Warning: could not process flow "
                            f"{index}: {e}"
                        )

                if index % 5000 == 0:

                    print(
                        f"  Processed {index:,} flows..."
                    )

    except Exception as e:

        print()
        print("ERROR while reading flow file:")
        print(str(e))
        print()

        sys.exit(1)

    print()
    print("Writing results...")
    print()

    report_path = write_results(output_dir)

    print("=" * 60)
    print("DONE")
    print("=" * 60)
    print()
    print(f"Total flows:       {total_flows:,}")
    print(f"Grammarly flows:   {grammarly_flows:,}")
    print(f"JSON requests:     {json_requests:,}")
    print(f"JSON responses:    {json_responses:,}")
    print(f"Unique endpoints:  {len(endpoint_stats):,}")
    print()
    print("Results saved to:")
    print(output_dir)
    print()
    print("START WITH:")
    print(report_path)
    print()
    print("Other useful files:")
    print(
        f"  {os.path.join(output_dir, 'endpoints.csv')}"
    )
    print(
        f"  {os.path.join(output_dir, 'request_fields.csv')}"
    )
    print(
        f"  {os.path.join(output_dir, 'response_fields.csv')}"
    )
    print(
        f"  {os.path.join(output_dir, 'behavior_timeline.csv')}"
    )
    print()


if __name__ == "__main__":
    main()
    