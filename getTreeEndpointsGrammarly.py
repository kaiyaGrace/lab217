#!/usr/bin/env python3
"""
Grammarly Desktop mitmproxy Flow Analyzer

Input:
    A saved mitmproxy flow file (.mitm / flow export)

Output:
    One Markdown report:
        grammarly_analysis.md

The report is designed to be:
    1. Opened
    2. Ctrl+A
    3. Ctrl+C
    4. Pasted directly into ChatGPT

What it analyzes:
    - Capture summary
    - Endpoint tree
    - Endpoint frequency
    - HTTP methods
    - Status codes
    - Request schemas
    - Response schemas
    - Query parameter names
    - Content types
    - Request/response sizes
    - First/last observed timestamps
    - Example flow IDs
    - Time-ordered request sequence
    - Basic architecture observations

What it intentionally does NOT output:
    - Raw request bodies
    - Raw response bodies
    - Cookie values
    - Authorization values
    - Query parameter values
    - Arbitrary header secrets

Designed for Grammarly Desktop captures only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlsplit

from mitmproxy import http, io
from mitmproxy.exceptions import FlowReadException


# ============================================================
# Configuration
# ============================================================

OUTPUT_FILENAME = "grammarly_analysis.md"

# Limit very large reports.
MAX_EXAMPLE_FLOW_IDS = 5
MAX_SEQUENCE_ROWS = 500
MAX_SCHEMA_EXAMPLES = 5

# Header names that are safe/useful to expose.
SAFE_HEADERS = {
    "accept",
    "accept-encoding",
    "accept-language",
    "content-type",
    "origin",
    "referer",
    "user-agent",
    "x-client-name",
    "x-client-version",
    "x-grammarly-client",
    "x-grammarly-version",
    "x-request-id",
    "x-requested-with",
}

# Header names that should NEVER appear in the report.
SENSITIVE_HEADER_PATTERNS = (
    "authorization",
    "cookie",
    "set-cookie",
    "token",
    "secret",
    "password",
    "api-key",
    "apikey",
    "session",
    "credential",
)

# Path values that are likely dynamic.
UUID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-"
    r"[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{12}$"
)

INTEGER_RE = re.compile(r"^\d+$")

HEX_RE = re.compile(r"^[0-9a-fA-F]{16,}$")

LONG_BASE64ISH_RE = re.compile(
    r"^[A-Za-z0-9_-]{24,}$"
)

EMAIL_RE = re.compile(
    r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
)


# ============================================================
# General helpers
# ============================================================

def human_timestamp(timestamp: float | None) -> str:
    if not timestamp:
        return "unknown"

    try:
        return datetime.fromtimestamp(
            timestamp,
            tz=timezone.utc,
        ).astimezone().strftime(
            "%Y-%m-%d %H:%M:%S %Z"
        )
    except Exception:
        return "unknown"


def safe_int(value: Any) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def truncate(value: str, limit: int = 120) -> str:
    if len(value) <= limit:
        return value

    return value[: limit - 3] + "..."


# ============================================================
# Endpoint normalization
# ============================================================

def normalize_path_segment(segment: str) -> str:
    """
    Turn dynamic values into placeholders while preserving
    meaningful endpoint names.

    Examples:

        12345
            -> {id}

        UUID
            -> {uuid}

        long hexadecimal token
            -> {hex}

        long base64-ish value
            -> {value}
    """

    if not segment:
        return segment

    decoded = segment.strip()

    if UUID_RE.fullmatch(decoded):
        return "{uuid}"

    if INTEGER_RE.fullmatch(decoded):
        return "{id}"

    if HEX_RE.fullmatch(decoded):
        return "{hex}"

    if (
        len(decoded) >= 24
        and LONG_BASE64ISH_RE.fullmatch(decoded)
        and not decoded.isalpha()
    ):
        return "{value}"

    if EMAIL_RE.fullmatch(decoded):
        return "{email}"

    return decoded


def normalize_path(path: str) -> str:
    if not path:
        return "/"

    segments = [
        segment
        for segment in path.split("/")
        if segment
    ]

    normalized = [
        normalize_path_segment(segment)
        for segment in segments
    ]

    return "/" + "/".join(normalized)


def endpoint_key(
    host: str,
    path: str,
    method: str,
) -> tuple[str, str, str]:
    return (
        host.lower(),
        normalize_path(path),
        method.upper(),
    )


# ============================================================
# Schema generation
# ============================================================

def primitive_schema(value: Any) -> str:
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

    return type(value).__name__


def merge_dict_schemas(values: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Combine multiple observed JSON objects so a field seen in
    different requests does not disappear from the schema.
    """

    all_keys = set()

    for value in values:
        all_keys.update(value.keys())

    merged: dict[str, Any] = {}

    for key in sorted(all_keys):
        present_values = [
            item[key]
            for item in values
            if key in item
        ]

        merged[key] = infer_schema(
            present_values
        )

    return merged


def infer_schema(values: list[Any]) -> Any:
    """
    Infer a structural schema from observed values.

    Examples:

        "hello"
            -> "string"

        42
            -> "integer"

        {"text": "hello"}
            -> {"text": "string"}

        [{"id": 1}, {"id": 2}]
            -> [{"id": "integer"}]
    """

    if not values:
        return "unknown"

    non_null = [
        value
        for value in values
        if value is not None
    ]

    if not non_null:
        return "null"

    if all(isinstance(value, dict) for value in non_null):
        return merge_dict_schemas(
            non_null
        )

    if all(isinstance(value, list) for value in non_null):
        flattened: list[Any] = []

        for value in non_null:
            flattened.extend(value)

        if not flattened:
            return ["unknown"]

        return [
            infer_schema(flattened)
        ]

    primitive_types = sorted(
        set(
            primitive_schema(value)
            for value in non_null
        )
    )

    if len(primitive_types) == 1:
        return primitive_types[0]

    return " | ".join(
        primitive_types
    )


def pretty_schema(schema: Any, indent: int = 0) -> str:
    """
    Render schema as readable Markdown-ish text.
    """

    pad = " " * indent

    if isinstance(schema, dict):
        if not schema:
            return "{}"

        lines = ["{"]

        items = list(schema.items())

        for index, (key, value) in enumerate(items):
            rendered = pretty_schema(
                value,
                indent + 2,
            )

            value_lines = rendered.splitlines()

            if len(value_lines) == 1:
                line = (
                    " " * (indent + 2)
                    + f'"{key}": {value_lines[0]}'
                )
                lines.append(line)
            else:
                lines.append(
                    " " * (indent + 2)
                    + f'"{key}": {value_lines[0]}'
                )

                lines.extend(
                    value_lines[1:]
                )

            if index < len(items) - 1:
                lines[-1] += ","

        lines.append(
            pad + "}"
        )

        return "\n".join(lines)

    if isinstance(schema, list):
        if not schema:
            return "[]"

        inner = pretty_schema(
            schema[0],
            indent + 2,
        )

        return (
            "[\n"
            + " " * (indent + 2)
            + inner.replace(
                "\n",
                "\n" + " " * (indent + 2),
            )
            + "\n"
            + pad
            + "]"
        )

    return str(schema)


# ============================================================
# Body analysis
# ============================================================

def decode_body_message(message) -> bytes | None:
    """
    Prefer mitmproxy's decoded content API. If content encoding
    cannot be decoded, fall back to raw content.
    """

    try:
        decoded = message.get_content(
            strict=False
        )
    except Exception:
        decoded = None

    if decoded is not None:
        return decoded

    return message.raw_content


def parse_json_body(message) -> Any | None:
    try:
        return message.json()
    except Exception:
        pass

    content = decode_body_message(message)

    if not content:
        return None

    try:
        text = content.decode(
            "utf-8",
            errors="strict",
        )
    except UnicodeDecodeError:
        return None

    try:
        return json.loads(text)
    except Exception:
        return None


def body_schema(message) -> tuple[Any | None, str]:
    """
    Returns:

        (schema, body_type)

    body_type examples:

        json
        form
        text
        binary
        empty
        unavailable
    """

    content = decode_body_message(
        message
    )

    if content is None:
        return None, "unavailable"

    if len(content) == 0:
        return None, "empty"

    content_type = (
        message.headers.get(
            "content-type",
            ""
        )
        or ""
    ).lower()

    parsed_json = parse_json_body(
        message
    )

    if parsed_json is not None:
        return (
            infer_schema(
                [parsed_json]
            ),
            "json",
        )

    if (
        "application/x-www-form-urlencoded"
        in content_type
    ):
        try:
            text = content.decode(
                "utf-8",
                errors="replace",
            )

            pairs = parse_qsl(
                text,
                keep_blank_values=True,
            )

            keys = sorted(
                set(
                    key
                    for key, _ in pairs
                )
            )

            return (
                {
                    key: "string"
                    for key in keys
                },
                "form",
            )

        except Exception:
            return None, "form"

    if (
        "text/" in content_type
        or
        "application/graphql"
        in content_type
        or
        "application/javascript"
        in content_type
    ):
        return (
            "string",
            "text",
        )

    # If it looks like readable UTF-8 text, describe it as text
    # rather than leaking the content.
    try:
        decoded_text = content.decode(
            "utf-8",
            errors="strict",
        )

        if decoded_text.strip():
            return (
                "string",
                "text",
            )
    except UnicodeDecodeError:
        pass

    return (
        f"binary ({len(content)} bytes)",
        "binary",
    )


# ============================================================
# Header analysis
# ============================================================

def safe_header_map(headers) -> dict[str, str]:
    result: dict[str, str] = {}

    for name, value in headers.items():
        lower = name.lower()

        if any(
            pattern in lower
            for pattern in SENSITIVE_HEADER_PATTERNS
        ):
            continue

        if lower in SAFE_HEADERS:
            result[lower] = truncate(
                value,
                200,
            )

    return dict(sorted(result.items()))


# ============================================================
# Query analysis
# ============================================================

def query_parameter_names(query: str) -> list[str]:
    if not query:
        return []

    try:
        pairs = parse_qsl(
            query,
            keep_blank_values=True,
        )

        return sorted(
            set(
                key
                for key, _ in pairs
            )
        )

    except Exception:
        return []


# ============================================================
# Capture records
# ============================================================

def analyze_flow(
    flow: http.HTTPFlow,
) -> dict[str, Any]:

    request = flow.request
    response = flow.response

    split = urlsplit(
        request.pretty_url
    )

    host = (
        split.hostname
        or request.host
        or "<unknown-host>"
    ).lower()

    path = split.path or "/"

    normalized = normalize_path(
        path
    )

    query_names = (
        query_parameter_names(
            split.query
        )
    )

    request_schema, request_body_type = (
        body_schema(request)
    )

    response_schema = None
    response_body_type = "none"

    if response is not None:
        (
            response_schema,
            response_body_type,
        ) = body_schema(response)

    status = (
        response.status_code
        if response is not None
        else None
    )

    request_content_type = (
        request.headers.get(
            "content-type",
            ""
        )
        or ""
    )

    response_content_type = ""

    if response is not None:
        response_content_type = (
            response.headers.get(
                "content-type",
                ""
            )
            or ""
        )

    request_content = (
        request.raw_content
        or b""
    )

    response_content = (
        response.raw_content
        if response is not None
        else b""
    ) or b""

    return {
        "flow_id": flow.id,
        "timestamp": flow.timestamp_created,
        "timestamp_text": human_timestamp(
            flow.timestamp_created
        ),
        "method": request.method.upper(),
        "host": host,
        "path": path,
        "normalized_path": normalized,
        "endpoint": f"{host}{normalized}",
        "query_names": query_names,
        "status": status,
        "request_content_type": request_content_type,
        "response_content_type": response_content_type,
        "request_body_type": request_body_type,
        "response_body_type": response_body_type,
        "request_size": len(request_content),
        "response_size": len(response_content),
        "request_schema": request_schema,
        "response_schema": response_schema,
        "request_headers": safe_header_map(
            request.headers
        ),
        "response_headers": (
            safe_header_map(
                response.headers
            )
            if response is not None
            else {}
        ),
        "http_version": request.http_version,
    }


# ============================================================
# Endpoint aggregation
# ============================================================

def new_endpoint_record() -> dict[str, Any]:
    return {
        "count": 0,
        "methods": Counter(),
        "statuses": Counter(),
        "request_body_types": Counter(),
        "response_body_types": Counter(),
        "request_content_types": Counter(),
        "response_content_types": Counter(),
        "query_names": Counter(),
        "request_schema_samples": defaultdict(list),
        "response_schema_samples": defaultdict(list),
        "request_schema_counts": Counter(),
        "response_schema_counts": Counter(),
        "request_sizes": [],
        "response_sizes": [],
        "first_timestamp": None,
        "last_timestamp": None,
        "flow_ids": [],
        "http_versions": Counter(),
    }


def schema_key(schema: Any) -> str:
    try:
        return json.dumps(
            schema,
            sort_keys=True,
            separators=(",", ":"),
        )
    except Exception:
        return str(schema)


def aggregate_endpoints(
    records: list[dict[str, Any]],
) -> dict[
    tuple[str, str, str],
    dict[str, Any],
]:

    endpoints: dict[
        tuple[str, str, str],
        dict[str, Any],
    ] = {}

    for record in records:
        key = endpoint_key(
            record["host"],
            record["path"],
            record["method"],
        )

        if key not in endpoints:
            endpoints[key] = (
                new_endpoint_record()
            )

        endpoint = endpoints[key]

        endpoint["count"] += 1

        endpoint["methods"][
            record["method"]
        ] += 1

        if record["status"] is not None:
            endpoint["statuses"][
                str(record["status"])
            ] += 1

        endpoint[
            "request_body_types"
        ][record["request_body_type"]] += 1

        endpoint[
            "response_body_types"
        ][record["response_body_type"]] += 1

        if record["request_content_type"]:
            endpoint[
                "request_content_types"
            ][
                record["request_content_type"]
            ] += 1

        if record["response_content_type"]:
            endpoint[
                "response_content_types"
            ][
                record["response_content_type"]
            ] += 1

        for name in record["query_names"]:
            endpoint[
                "query_names"
            ][name] += 1

        request_schema = (
            record["request_schema"]
        )

        if request_schema is not None:
            key_id = schema_key(
                request_schema
            )

            endpoint[
                "request_schema_counts"
            ][key_id] += 1

            if len(
                endpoint[
                    "request_schema_samples"
                ][key_id]
            ) < MAX_SCHEMA_EXAMPLES:
                endpoint[
                    "request_schema_samples"
                ][key_id].append(
                    request_schema
                )

        response_schema = (
            record["response_schema"]
        )

        if response_schema is not None:
            key_id = schema_key(
                response_schema
            )

            endpoint[
                "response_schema_counts"
            ][key_id] += 1

            if len(
                endpoint[
                    "response_schema_samples"
                ][key_id]
            ) < MAX_SCHEMA_EXAMPLES:
                endpoint[
                    "response_schema_samples"
                ][key_id].append(
                    response_schema
                )

        endpoint[
            "request_sizes"
        ].append(
            record["request_size"]
        )

        endpoint[
            "response_sizes"
        ].append(
            record["response_size"]
        )

        endpoint[
            "http_versions"
        ][
            record["http_version"]
        ] += 1

        timestamp = record["timestamp"]

        if (
            endpoint["first_timestamp"]
            is None
            or timestamp
            < endpoint["first_timestamp"]
        ):
            endpoint[
                "first_timestamp"
            ] = timestamp

        if (
            endpoint["last_timestamp"]
            is None
            or timestamp
            > endpoint["last_timestamp"]
        ):
            endpoint[
                "last_timestamp"
            ] = timestamp

        if len(
            endpoint["flow_ids"]
        ) < MAX_EXAMPLE_FLOW_IDS:
            endpoint[
                "flow_ids"
            ].append(
                record["flow_id"]
            )

    return endpoints


# ============================================================
# Endpoint tree
# ============================================================

def build_endpoint_tree(
    records: list[dict[str, Any]],
) -> dict[str, Any]:

    tree: dict[str, Any] = {}

    for record in records:
        host = record["host"]

        if host not in tree:
            tree[host] = {
                "__count__": 0,
                "__methods__": Counter(),
            }

        node = tree[host]

        node["__count__"] += 1
        node["__methods__"][
            record["method"]
        ] += 1

        segments = [
            segment
            for segment in record[
                "normalized_path"
            ].split("/")
            if segment
        ]

        for segment in segments:
            if segment not in node:
                node[segment] = {
                    "__count__": 0,
                    "__methods__": Counter(),
                }

            node = node[segment]

            node["__count__"] += 1
            node["__methods__"][
                record["method"]
            ] += 1

    return tree


def render_tree(
    tree: dict[str, Any],
) -> list[str]:

    lines: list[str] = []

    display_items = [
        (key, value)
        for key, value in tree.items()
        if not key.startswith("__")
    ]

    display_items.sort(
        key=lambda item: item[0]
    )

    for index, (name, node) in enumerate(
        display_items
    ):

        is_last = (
            index == len(display_items) - 1
        )

        branch = (
            "└── "
            if is_last
            else "├── "
        )

        count = node.get(
            "__count__",
            0,
        )

        methods = node.get(
            "__methods__",
            {},
        )

        method_text = ", ".join(
            sorted(methods.keys())
        )

        suffix = (
            f"  [{count} requests; "
            f"{method_text}]"
            if count
            else ""
        )

        lines.append(
            branch
            + name
            + suffix
        )

        child_prefix = (
            "    "
            if is_last
            else "│   "
        )

        child_tree = {
            key: value
            for key, value in node.items()
            if not key.startswith("__")
        }

        child_lines = render_tree(
            child_tree
        )

        for child_line in child_lines:
            lines.append(
                child_prefix
                + child_line
            )

    return lines


# ============================================================
# Report helpers
# ============================================================

def format_counter(
    counter: Counter,
    separator: str = ", ",
) -> str:

    if not counter:
        return "none"

    pieces = []

    for key, value in counter.most_common():
        pieces.append(
            f"{key} ({value})"
        )

    return separator.join(
        pieces
    )


def format_size(value: int) -> str:
    if value < 1024:
        return f"{value} B"

    if value < 1024 * 1024:
        return f"{value / 1024:.1f} KiB"

    return f"{value / (1024 * 1024):.1f} MiB"


def average(values: list[int]) -> float:
    if not values:
        return 0.0

    return sum(values) / len(values)


def percentile(
    values: list[int],
    p: float,
) -> float:

    if not values:
        return 0.0

    ordered = sorted(values)

    index = (
        (len(ordered) - 1)
        * p
    )

    lower = int(index)
    upper = min(
        lower + 1,
        len(ordered) - 1,
    )

    fraction = index - lower

    return (
        ordered[lower]
        * (1 - fraction)
        + ordered[upper]
        * fraction
    )


def schema_counts_markdown(
    counts: Counter,
    samples: defaultdict,
) -> list[str]:

    lines: list[str] = []

    if not counts:
        lines.append(
            "_No structured schema observed._"
        )
        return lines

    sorted_schemas = counts.most_common()

    for index, (
        schema_id,
        count,
    ) in enumerate(
        sorted_schemas,
        start=1,
    ):

        lines.append(
            f"**Schema {index}** — "
            f"{count} request(s)/response(s)"
        )

        examples = samples.get(
            schema_id,
            [],
        )

        if examples:
            schema = examples[0]

            rendered = (
                pretty_schema(schema)
            )

            lines.append("")
            lines.append(
                "```text"
            )
            lines.append(
                rendered
            )
            lines.append(
                "```"
            )

    return lines


# ============================================================
# Architecture observations
# ============================================================

def generate_observations(
    records: list[dict[str, Any]],
    endpoints: dict[
        tuple[str, str, str],
        dict[str, Any],
    ],
) -> list[str]:

    observations: list[str] = []

    if not records:
        return observations

    host_counter = Counter(
        record["host"]
        for record in records
    )

    endpoint_counter = Counter(
        (
            record["host"],
            record["normalized_path"],
        )
        for record in records
    )

    json_count = sum(
        1
        for record in records
        if (
            record[
                "request_body_type"
            ]
            == "json"
            or
            record[
                "response_body_type"
            ]
            == "json"
        )
    )

    binary_count = sum(
        1
        for record in records
        if (
            record[
                "request_body_type"
            ]
            == "binary"
            or
            record[
                "response_body_type"
            ]
            == "binary"
        )
    )

    if len(host_counter) == 1:
        observations.append(
            "The capture communicates with "
            "one observed host."
        )
    else:
        observations.append(
            f"The capture communicates with "
            f"{len(host_counter)} distinct hosts."
        )

    if json_count:
        observations.append(
            f"Structured JSON traffic appears in "
            f"{json_count} of "
            f"{len(records)} HTTP flow(s)."
        )

    if binary_count:
        observations.append(
            f"Binary/non-JSON bodies appear in "
            f"{binary_count} HTTP flow(s); these "
            "may warrant deeper protocol/content "
            "inspection."
        )

    repeated = [
        (
            host,
            path,
            count,
        )
        for (
            host,
            path,
        ), count in endpoint_counter.items()
        if count >= 10
    ]

    repeated.sort(
        key=lambda item: -item[2]
    )

    if repeated:
        top = repeated[:5]

        description = "; ".join(
            f"{host}{path} "
            f"({count} requests)"
            for host, path, count
            in top
        )

        observations.append(
            "High-frequency endpoints observed: "
            + description
            + "."
        )

    error_count = sum(
        1
        for record in records
        if (
            record["status"] is not None
            and record["status"] >= 400
        )
    )

    if error_count:
        observations.append(
            f"{error_count} HTTP flow(s) returned "
            "a 4xx/5xx status."
        )

    methods = Counter(
        record["method"]
        for record in records
    )

    if methods:
        observations.append(
            "Observed HTTP methods: "
            + format_counter(methods)
            + "."
        )

    return observations


# ============================================================
# Markdown report
# ============================================================

def generate_report(
    input_path: Path,
    records: list[dict[str, Any]],
    endpoints: dict[
        tuple[str, str, str],
        dict[str, Any],
    ],
    tree: dict[str, Any],
) -> str:

    lines: list[str] = []

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    lines.append(
        "# Grammarly Desktop HTTP Flow Analysis"
    )

    lines.append("")
    lines.append(
        "> Automatically generated from a saved "
        "mitmproxy flow capture."
    )

    lines.append(
        "> Raw request/response body values and "
        "sensitive header values are intentionally "
        "not included."
    )

    lines.append("")

    # --------------------------------------------------------
    # Capture summary
    # --------------------------------------------------------

    lines.append(
        "## 1. Capture Summary"
    )

    lines.append("")

    unique_hosts = sorted(
        set(
            record["host"]
            for record in records
        )
    )

    unique_endpoints = len(
        endpoints
    )

    method_counter = Counter(
        record["method"]
        for record in records
    )

    status_counter = Counter(
        str(record["status"])
        for record in records
        if record["status"] is not None
    )

    lines.append(
        f"- **Input file:** `{input_path.name}`"
    )

    lines.append(
        f"- **HTTP flows:** {len(records)}"
    )

    lines.append(
        f"- **Unique endpoints:** "
        f"{unique_endpoints}"
    )

    lines.append(
        f"- **Unique hosts:** "
        f"{len(unique_hosts)}"
    )

    lines.append(
        f"- **HTTP methods:** "
        f"{format_counter(method_counter)}"
    )

    lines.append(
        f"- **HTTP statuses:** "
        f"{format_counter(status_counter)}"
    )

    if records:
        timestamps = [
            record["timestamp"]
            for record in records
        ]

        lines.append(
            f"- **First observed:** "
            f"{human_timestamp(min(timestamps))}"
        )

        lines.append(
            f"- **Last observed:** "
            f"{human_timestamp(max(timestamps))}"
        )

    lines.append("")

    lines.append(
        "### Observed Hosts"
    )

    lines.append("")

    for host in unique_hosts:
        count = sum(
            1
            for record in records
            if record["host"] == host
        )

        lines.append(
            f"- `{host}` — {count} flow(s)"
        )

    lines.append("")

    # --------------------------------------------------------
    # Endpoint tree
    # --------------------------------------------------------

    lines.append(
        "## 2. Endpoint Tree"
    )

    lines.append("")

    lines.append(
        "```text"
    )

    for host in sorted(tree.keys()):
        node = tree[host]

        count = node.get(
            "__count__",
            0,
        )

        methods = node.get(
            "__methods__",
            {},
        )

        method_text = ", ".join(
            sorted(methods.keys())
        )

        lines.append(
            f"{host}  "
            f"[{count} requests; "
            f"{method_text}]"
        )

        child_tree = {
            key: value
            for key, value in node.items()
            if not key.startswith("__")
        }

        child_lines = render_tree(
            child_tree
        )

        for child_line in child_lines:
            lines.append(
                child_line
            )

    lines.append(
        "```"
    )

    lines.append("")

    lines.append(
        "**Normalization note:** dynamic path "
        "segments such as numeric IDs, UUIDs, and "
        "long token-like values are collapsed into "
        "placeholders so repeated operations appear "
        "as one endpoint."
    )

    lines.append("")

    # --------------------------------------------------------
    # Frequency table
    # --------------------------------------------------------

    lines.append(
        "## 3. Endpoint Frequency"
    )

    lines.append("")

    lines.append(
        "| Rank | Method | Host | Normalized Endpoint | Requests |"
    )

    lines.append(
        "|---:|---|---|---|---:|"
    )

    ranked = sorted(
        endpoints.items(),
        key=lambda item: (
            -item[1]["count"],
            item[0][0],
            item[0][1],
            item[0][2],
        ),
    )

    for rank, (
        (host, path, method),
        data,
    ) in enumerate(
        ranked,
        start=1,
    ):

        lines.append(
            f"| {rank} | {method} | "
            f"`{host}` | `{path}` | "
            f"{data['count']} |"
        )

    lines.append("")

    # --------------------------------------------------------
    # Endpoint details
    # --------------------------------------------------------

    lines.append(
        "## 4. Endpoint Details"
    )

    lines.append("")

    for (
        host,
        path,
        method,
    ), data in ranked:

        lines.append(
            f"### `{method} {host}{path}`"
        )

        lines.append("")

        lines.append(
            f"- **Observed requests:** "
            f"{data['count']}"
        )

        lines.append(
            f"- **Methods:** "
            f"{format_counter(data['methods'])}"
        )

        lines.append(
            f"- **Status codes:** "
            f"{format_counter(data['statuses'])}"
        )

        lines.append(
            f"- **Request body types:** "
            f"{format_counter(data['request_body_types'])}"
        )

        lines.append(
            f"- **Response body types:** "
            f"{format_counter(data['response_body_types'])}"
        )

        lines.append(
            f"- **Request content types:** "
            f"{format_counter(data['request_content_types'])}"
        )

        lines.append(
            f"- **Response content types:** "
            f"{format_counter(data['response_content_types'])}"
        )

        lines.append(
            f"- **HTTP versions:** "
            f"{format_counter(data['http_versions'])}"
        )

        if data["query_names"]:
            lines.append(
                "- **Query parameter names:** "
                + ", ".join(
                    f"`{name}`"
                    for name in sorted(
                        data["query_names"]
                    )
                )
            )
        else:
            lines.append(
                "- **Query parameter names:** none observed"
            )

        if data["request_sizes"]:
            lines.append(
                f"- **Average request size:** "
                f"{format_size(int(average(data['request_sizes'])))}"
            )

            lines.append(
                f"- **Largest request:** "
                f"{format_size(max(data['request_sizes']))}"
            )

        if data["response_sizes"]:
            lines.append(
                f"- **Average response size:** "
                f"{format_size(int(average(data['response_sizes'])))}"
            )

            lines.append(
                f"- **Largest response:** "
                f"{format_size(max(data['response_sizes']))}"
            )

        if data["first_timestamp"] is not None:
            lines.append(
                f"- **First observed:** "
                f"{human_timestamp(data['first_timestamp'])}"
            )

        if data["last_timestamp"] is not None:
            lines.append(
                f"- **Last observed:** "
                f"{human_timestamp(data['last_timestamp'])}"
            )

        if data["flow_ids"]:
            lines.append(
                "- **Example flow IDs:** "
                + ", ".join(
                    f"`{flow_id}`"
                    for flow_id
                    in data["flow_ids"]
                )
            )

        lines.append("")

        # Request schemas

        lines.append(
            "#### Request Schema(s)"
        )

        lines.append("")

        lines.extend(
            schema_counts_markdown(
                data[
                    "request_schema_counts"
                ],
                data[
                    "request_schema_samples"
                ],
            )
        )

        lines.append("")

        # Response schemas

        lines.append(
            "#### Response Schema(s)"
        )

        lines.append("")

        lines.extend(
            schema_counts_markdown(
                data[
                    "response_schema_counts"
                ],
                data[
                    "response_schema_samples"
                ],
            )
        )

        lines.append("")

    # --------------------------------------------------------
    # Request sequence
    # --------------------------------------------------------

    lines.append(
        "## 5. Observed Request Sequence"
    )

    lines.append("")

    lines.append(
        "This preserves the chronological order of "
        "captured HTTP flows. It is useful for "
        "spotting request chains and initialization "
        "behavior."
    )

    lines.append("")

    lines.append(
        "| # | Time | Method | Endpoint | Status | Flow ID |"
    )

    lines.append(
        "|---:|---|---|---|---:|---|"
    )

    sequence = sorted(
        records,
        key=lambda record: (
            record["timestamp"],
            record["flow_id"],
        ),
    )

    for index, record in enumerate(
        sequence[:MAX_SEQUENCE_ROWS],
        start=1,
    ):

        status = (
            record["status"]
            if record["status"] is not None
            else "-"
        )

        lines.append(
            f"| {index} | "
            f"{record['timestamp_text']} | "
            f"{record['method']} | "
            f"`{record['host']}"
            f"{record['normalized_path']}` | "
            f"{status} | "
            f"`{record['flow_id']}` |"
        )

    if len(sequence) > MAX_SEQUENCE_ROWS:
        lines.append("")

        lines.append(
            f"_Sequence truncated to "
            f"{MAX_SEQUENCE_ROWS} flows out of "
            f"{len(sequence)} total flows._"
        )

    lines.append("")

    # --------------------------------------------------------
    # Architecture observations
    # --------------------------------------------------------

    lines.append(
        "## 6. Automatically Detected Architecture Signals"
    )

    lines.append("")

    observations = generate_observations(
        records,
        endpoints,
    )

    if observations:
        for observation in observations:
            lines.append(
                f"- {observation}"
            )
    else:
        lines.append(
            "_No automatic observations available._"
        )

    lines.append("")

    # --------------------------------------------------------
    # Analysis notes
    # --------------------------------------------------------

    lines.append(
        "## 7. Analysis Notes"
    )

    lines.append("")

    lines.append(
        "- This report is based only on observed "
        "HTTP traffic in the supplied capture."
    )

    lines.append(
        "- Endpoint names are normalized from the "
        "captured paths; normalization can occasionally "
        "group two distinct operations together if "
        "their path parameters look dynamic."
    )

    lines.append(
        "- Request and response schemas describe "
        "structure rather than actual values."
    )

    lines.append(
        "- Query parameter names are retained, but "
        "query parameter values are not."
    )

    lines.append(
        "- Sensitive header values such as cookies "
        "and authorization material are omitted."
    )

    lines.append(
        "- Binary bodies are reported as binary rather "
        "than decoded into arbitrary data."
    )

    lines.append(
        "- Absence from this report does not prove that "
        "an endpoint or protocol does not exist; it only "
        "means it was not observed in this capture."
    )

    lines.append("")

    lines.append(
        "---"
    )

    lines.append("")

    lines.append(
        "Generated by Grammarly Desktop Flow Analyzer."
    )

    lines.append("")

    return "\n".join(lines)


# ============================================================
# Main
# ============================================================

def read_flows(
    input_path: Path,
) -> list[dict[str, Any]]:

    records: list[dict[str, Any]] = []

    try:
        with input_path.open(
            "rb"
        ) as logfile:

            flow_reader = io.FlowReader(
                logfile
            )

            for flow in flow_reader.stream():

                if not isinstance(
                    flow,
                    http.HTTPFlow,
                ):
                    continue

                try:
                    records.append(
                        analyze_flow(flow)
                    )

                except Exception as exc:
                    print(
                        f"[!] Skipping flow "
                        f"{getattr(flow, 'id', '?')}: "
                        f"{exc}",
                        file=sys.stderr,
                    )

    except FlowReadException as exc:
        raise RuntimeError(
            f"Could not read flow file: {exc}"
        ) from exc

    return records


def main() -> int:

    parser = argparse.ArgumentParser(
        description=(
            "Analyze a saved mitmproxy flow file "
            "from Grammarly Desktop and generate "
            "one ChatGPT-ready Markdown report."
        )
    )

    parser.add_argument(
        "flow_file",
        help=(
            "Path to the saved mitmproxy flow file"
        ),
    )

    parser.add_argument(
        "-o",
        "--output",
        default=OUTPUT_FILENAME,
        help=(
            f"Output Markdown file "
            f"(default: {OUTPUT_FILENAME})"
        ),
    )

    args = parser.parse_args()

    input_path = Path(
        args.flow_file
    ).expanduser().resolve()

    output_path = Path(
        args.output
    ).expanduser().resolve()

    if not input_path.exists():
        print(
            f"[ERROR] Input file does not exist:\n"
            f"        {input_path}",
            file=sys.stderr,
        )
        return 1

    if not input_path.is_file():
        print(
            f"[ERROR] Input path is not a file:\n"
            f"        {input_path}",
            file=sys.stderr,
        )
        return 1

    print(
        f"[+] Reading: {input_path}"
    )

    try:
        records = read_flows(
            input_path
        )

    except Exception as exc:
        print(
            f"[ERROR] {exc}",
            file=sys.stderr,
        )
        return 1

    print(
        f"[+] HTTP flows analyzed: "
        f"{len(records)}"
    )

    endpoints = aggregate_endpoints(
        records
    )

    print(
        f"[+] Unique endpoints: "
        f"{len(endpoints)}"
    )

    tree = build_endpoint_tree(
        records
    )

    report = generate_report(
        input_path,
        records,
        endpoints,
        tree,
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path.write_text(
        report,
        encoding="utf-8",
    )

    print(
        f"[+] Report written to:\n"
        f"    {output_path}"
    )

    print("")
    print(
        "[+] Done."
    )

    print(
        "[+] Open the Markdown file, "
        "Ctrl+A, Ctrl+C, and paste it into ChatGPT."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(
        main()
    )
