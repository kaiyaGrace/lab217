#!/usr/bin/env python3

"""
Grammarly Desktop — Part 2 JSON Message Structure Analyzer

Input:
    A mitmproxy .mitm flow export

Output:
    ONE Markdown file containing:
      - endpoint inventory
      - JSON request schemas
      - JSON response schemas
      - schema variants
      - field frequencies
      - required/optional fields
      - nested objects
      - arrays
      - non-JSON endpoints

This analyzes observed traffic only.
It does NOT print captured JSON values.
"""

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

from mitmproxy import http
from mitmproxy.io import FlowReader


# ============================================================
# CONFIGURATION
# ============================================================

GRAMMARLY_SUFFIXES = (
    ".grammarly.com",
    ".grammarly.io",
)

# Dynamic path components are normalized so that:
#
# /users/12345/settings
# /users/67890/settings
#
# become:
#
# /users/{id}/settings

UUID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-"
    r"[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{12}$"
)

NUMBER_RE = re.compile(r"^\d+$")

HEX_RE = re.compile(r"^[0-9a-fA-F]{16,}$")


# ============================================================
# BASIC UTILITIES
# ============================================================

def decode_body(data):
    if not data:
        return ""

    return data.decode(
        "utf-8",
        errors="replace"
    )


def parse_json_body(data):
    """
    Attempt to parse a body as JSON.

    Returns:
        parsed object, or None
    """

    if not data:
        return None

    text = decode_body(data).strip()

    if not text:
        return None

    try:
        return json.loads(text)
    except Exception:
        return None


def is_grammarly_host(host):
    if not host:
        return False

    host = host.lower()

    return (
        host == "grammarly.com"
        or any(
            host.endswith(suffix)
            for suffix in GRAMMARLY_SUFFIXES
        )
    )


# ============================================================
# PATH NORMALIZATION
# ============================================================

def normalize_segment(segment):

    if UUID_RE.match(segment):
        return "{uuid}"

    if NUMBER_RE.match(segment):
        return "{id}"

    if HEX_RE.match(segment):
        return "{token}"

    return segment


def normalize_path(path):

    if not path:
        return "/"

    segments = [
        segment
        for segment in path.split("/")
        if segment
    ]

    normalized = [
        normalize_segment(segment)
        for segment in segments
    ]

    return "/" + "/".join(normalized)


# ============================================================
# JSON SCHEMA REPRESENTATION
# ============================================================

def primitive_type(value):

    if value is None:
        return "null"

    if isinstance(value, bool):
        return "boolean"

    if isinstance(value, int):
        return "integer"

    if isinstance(value, float):
        return "number"

    if isinstance(value, str):
        return "string"

    return type(value).__name__


def schema_from_value(value):

    if isinstance(value, dict):

        return {
            key: schema_from_value(value[key])
            for key in sorted(value)
        }

    if isinstance(value, list):

        if not value:
            return {
                "__array__": "empty"
            }

        element_schemas = []

        for element in value:
            element_schemas.append(
                schema_from_value(element)
            )

        unique = []

        for schema in element_schemas:
            if schema not in unique:
                unique.append(schema)

        if len(unique) == 1:
            return {
                "__array__": unique[0]
            }

        return {
            "__array__": unique
        }

    return primitive_type(value)


# ============================================================
# SCHEMA FINGERPRINTING
# ============================================================

def canonical_json(value):

    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":")
    )


def schema_fingerprint(schema):

    raw = canonical_json(schema)

    return hashlib.sha256(
        raw.encode("utf-8")
    ).hexdigest()[:10]


# ============================================================
# FIELD STATISTICS
# ============================================================

def collect_fields(
    value,
    prefix="",
    counter=None,
    types=None,
):

    if counter is None:
        counter = Counter()

    if types is None:
        types = defaultdict(Counter)

    if isinstance(value, dict):

        for key, child in value.items():

            path = (
                f"{prefix}.{key}"
                if prefix
                else key
            )

            counter[path] += 1

            types[path][
                primitive_type(child)
                if not isinstance(child, (dict, list))
                else (
                    "object"
                    if isinstance(child, dict)
                    else "array"
                )
            ] += 1

            collect_fields(
                child,
                path,
                counter,
                types,
            )

    elif isinstance(value, list):

        for child in value:

            collect_fields(
                child,
                prefix + "[]",
                counter,
                types,
            )

    return counter, types


# ============================================================
# SCHEMA VARIANT
# ============================================================

class SchemaVariant:

    def __init__(self, schema, count=0):

        self.schema = schema
        self.fingerprint = schema_fingerprint(
            schema
        )
        self.count = count


# ============================================================
# ENDPOINT
# ============================================================

class Endpoint:

    def __init__(
        self,
        host,
        path,
    ):

        self.host = host
        self.path = path

        self.requests = 0

        self.methods = Counter()
        self.statuses = Counter()

        self.request_content_types = Counter()
        self.response_content_types = Counter()

        self.request_variants = {}
        self.response_variants = {}

        self.request_field_counts = Counter()
        self.request_field_types = defaultdict(
            Counter
        )

        self.response_field_counts = Counter()
        self.response_field_types = defaultdict(
            Counter
        )

        self.request_json_count = 0
        self.response_json_count = 0

        self.request_non_json_count = 0
        self.response_non_json_count = 0

    def add_request(
        self,
        method,
        content_type,
        parsed_json,
        raw_body_exists,
    ):

        self.requests += 1
        self.methods[method] += 1

        if content_type:
            self.request_content_types[
                content_type
            ] += 1

        if parsed_json is not None:

            self.request_json_count += 1

            schema = schema_from_value(
                parsed_json
            )

            fingerprint = schema_fingerprint(
                schema
            )

            if fingerprint not in self.request_variants:

                self.request_variants[
                    fingerprint
                ] = SchemaVariant(
                    schema
                )

            self.request_variants[
                fingerprint
            ].count += 1

            fields, types = collect_fields(
                parsed_json
            )

            self.request_field_counts.update(
                fields
            )

            for field, field_types in types.items():

                self.request_field_types[
                    field
                ].update(
                    field_types
                )

        elif raw_body_exists:

            self.request_non_json_count += 1

    def add_response(
        self,
        status,
        content_type,
        parsed_json,
        raw_body_exists,
    ):

        if status is not None:
            self.statuses[str(status)] += 1

        if content_type:
            self.response_content_types[
                content_type
            ] += 1

        if parsed_json is not None:

            self.response_json_count += 1

            schema = schema_from_value(
                parsed_json
            )

            fingerprint = schema_fingerprint(
                schema
            )

            if fingerprint not in self.response_variants:

                self.response_variants[
                    fingerprint
                ] = SchemaVariant(
                    schema
                )

            self.response_variants[
                fingerprint
            ].count += 1

            fields, types = collect_fields(
                parsed_json
            )

            self.response_field_counts.update(
                fields
            )

            for field, field_types in types.items():

                self.response_field_types[
                    field
                ].update(
                    field_types
                )

        elif raw_body_exists:

            self.response_non_json_count += 1


# ============================================================
# SCHEMA RENDERING
# ============================================================

def render_schema(
    schema,
    indent=0,
):

    spaces = " " * indent

    if isinstance(schema, dict):

        # Array representation
        if set(schema.keys()) == {"__array__"}:

            element = schema["__array__"]

            if element == "empty":
                return "[]"

            if isinstance(element, list):

                rendered = []

                for variant in element:

                    rendered.append(
                        render_schema(
                            variant,
                            indent + 4
                        )
                    )

                return (
                    "[\n"
                    + "\n".join(
                        " " * (indent + 4)
                        + item
                        for item in rendered
                    )
                    + "\n"
                    + spaces
                    + "]"
                )

            return (
                "[\n"
                + " " * (indent + 4)
                + render_schema(
                    element,
                    indent + 4
                )
                + "\n"
                + spaces
                + "]"
            )

        lines = ["{"]

        items = list(schema.items())

        for index, (key, value) in enumerate(items):

            child = render_schema(
                value,
                indent + 4
            )

            child_lines = child.splitlines()

            first = child_lines[0]

            lines.append(
                " " * (indent + 4)
                + json.dumps(key)
                + ": "
                + first
            )

            for continuation in child_lines[1:]:
                lines.append(
                    " " * (indent + 4)
                    + continuation
                )

            if index < len(items) - 1:
                lines[-1] += ","

        lines.append(spaces + "}")

        return "\n".join(lines)

    return schema


def render_field_table(
    endpoint,
    request=True,
):

    if request:
        counts = endpoint.request_field_counts
        types = endpoint.request_field_types
        total = endpoint.request_json_count
    else:
        counts = endpoint.response_field_counts
        types = endpoint.response_field_types
        total = endpoint.response_json_count

    if not counts or total == 0:
        return []

    lines = [
        "| Field | Present | Type |",
        "|---|---:|---|",
    ]

    for field in sorted(counts):

        count = counts[field]

        percentage = (
            count / total * 100
            if total
            else 0
        )

        if percentage >= 99.999:
            presence = "100%"
        else:
            presence = f"{percentage:.1f}%"

        type_string = ", ".join(
            sorted(types[field].keys())
        )

        lines.append(
            f"| `{field}` | {presence} | "
            f"{type_string} |"
        )

    return lines


# ============================================================
# ENDPOINT TREE
# ============================================================

def build_tree(endpoints):

    tree = {}

    for endpoint in endpoints.values():

        host = endpoint.host

        tree.setdefault(
            host,
            {}
        )

        current = tree[host]

        segments = [
            segment
            for segment in endpoint.path.split("/")
            if segment
        ]

        for segment in segments:

            current = current.setdefault(
                segment,
                {}
            )

    return tree


def render_tree(
    tree,
    prefix="",
):

    lines = []

    items = sorted(tree.items())

    for index, (name, subtree) in enumerate(items):

        last = index == len(items) - 1

        branch = (
            "└── "
            if last
            else "├── "
        )

        lines.append(
            prefix + branch + name
        )

        child_prefix = (
            prefix + "    "
            if last
            else prefix + "│   "
        )

        lines.extend(
            render_tree(
                subtree,
                child_prefix
            )
        )

    return lines


# ============================================================
# FLOW ANALYSIS
# ============================================================

def analyze_flow(flow, endpoints):

    if not isinstance(
        flow,
        http.HTTPFlow
    ):
        return

    request = flow.request

    parsed_url = urlparse(
        request.pretty_url
    )

    host = (
        parsed_url.hostname
        or ""
    ).lower()

    if not is_grammarly_host(host):
        return

    path = normalize_path(
        parsed_url.path
    )

    key = (
        host,
        path
    )

    if key not in endpoints:

        endpoints[key] = Endpoint(
            host,
            path
        )

    endpoint = endpoints[key]

    request_content_type = (
        request.headers.get(
            "content-type",
            ""
        ).split(";")[0].strip().lower()
    )

    request_json = parse_json_body(
        request.raw_content
    )

    endpoint.add_request(
        request.method,
        request_content_type,
        request_json,
        bool(request.raw_content),
    )

    response = flow.response

    if response is None:
        return

    response_content_type = (
        response.headers.get(
            "content-type",
            ""
        ).split(";")[0].strip().lower()
    )

    response_json = parse_json_body(
        response.raw_content
    )

    endpoint.add_response(
        response.status_code,
        response_content_type,
        response_json,
        bool(response.raw_content),
    )


# ============================================================
# MARKDOWN REPORT
# ============================================================

def write_report(
    endpoints,
    flow_count,
    output_file,
):

    lines = []

    lines.append(
        "# Grammarly Desktop — Part 2"
    )

    lines.append(
        "## JSON Message Structure Analysis"
    )

    lines.append("")

    lines.append(
        "> Generated from observed Grammarly Desktop HTTP traffic."
    )

    lines.append(
        "> Captured JSON values are intentionally not included."
    )

    lines.append("")

    lines.append("---")
    lines.append("")

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    total_endpoints = len(endpoints)

    json_request_endpoints = sum(
        1
        for endpoint in endpoints.values()
        if endpoint.request_json_count > 0
    )

    json_response_endpoints = sum(
        1
        for endpoint in endpoints.values()
        if endpoint.response_json_count > 0
    )

    total_request_schemas = sum(
        len(endpoint.request_variants)
        for endpoint in endpoints.values()
    )

    total_response_schemas = sum(
        len(endpoint.response_variants)
        for endpoint in endpoints.values()
    )

    lines.append(
        "## 1. Capture Summary"
    )

    lines.append("")

    lines.append(
        f"- HTTP flows analyzed: **{flow_count}**"
    )

    lines.append(
        f"- Unique Grammarly endpoints: **{total_endpoints}**"
    )

    lines.append(
        f"- Endpoints with JSON requests: **{json_request_endpoints}**"
    )

    lines.append(
        f"- Endpoints with JSON responses: **{json_response_endpoints}**"
    )

    lines.append(
        f"- Unique request schemas: **{total_request_schemas}**"
    )

    lines.append(
        f"- Unique response schemas: **{total_response_schemas}**"
    )

    lines.append("")

    # --------------------------------------------------------
    # Endpoint tree
    # --------------------------------------------------------

    lines.append(
        "## 2. Observed Endpoint Tree"
    )

    lines.append("")

    tree = build_tree(
        endpoints
    )

    lines.append("```text")

    lines.extend(
        render_tree(tree)
    )

    lines.append("```")

    lines.append("")

    # --------------------------------------------------------
    # Endpoint frequency
    # --------------------------------------------------------

    lines.append(
        "## 3. Endpoint Frequency"
    )

    lines.append("")

    lines.append(
        "| Method | Host | Endpoint | Requests | JSON Requests | JSON Responses |"
    )

    lines.append(
        "|---|---|---|---:|---:|---:|"
    )

    endpoint_rows = sorted(
        endpoints.values(),
        key=lambda endpoint: (
            -endpoint.requests,
            endpoint.host,
            endpoint.path,
        )
    )

    for endpoint in endpoint_rows:

        methods = ", ".join(
            endpoint.methods.keys()
        )

        lines.append(
            f"| {methods} | "
            f"`{endpoint.host}` | "
            f"`{endpoint.path}` | "
            f"{endpoint.requests} | "
            f"{endpoint.request_json_count} | "
            f"{endpoint.response_json_count} |"
        )

    lines.append("")

    # --------------------------------------------------------
    # Detailed endpoint schemas
    # --------------------------------------------------------

    lines.append(
        "## 4. JSON Message Structures by Endpoint"
    )

    lines.append("")

    for endpoint in endpoint_rows:

        lines.append("---")
        lines.append("")

        lines.append(
            f"### `{endpoint.host}{endpoint.path}`"
        )

        lines.append("")

        methods = ", ".join(
            endpoint.methods.keys()
        )

        lines.append(
            f"**Observed methods:** `{methods}`"
        )

        lines.append(
            f"**Observed requests:** {endpoint.requests}"
        )

        if endpoint.statuses:

            status_string = ", ".join(
                f"{status}: {count}"
                for status, count
                in sorted(
                    endpoint.statuses.items()
                )
            )

            lines.append(
                f"**Response statuses:** {status_string}"
            )

        lines.append("")

        # ----------------------------------------------------
        # Request
        # ----------------------------------------------------

        lines.append(
            "#### Request"
        )

        lines.append("")

        if endpoint.request_content_types:

            content_types = ", ".join(
                f"`{ctype}` ({count})"
                for ctype, count
                in endpoint.request_content_types.items()
            )

            lines.append(
                f"Content types: {content_types}"
            )

            lines.append("")

        if endpoint.request_json_count == 0:

            if endpoint.request_non_json_count:

                lines.append(
                    "**No JSON request body was observed.**"
                )

            else:

                lines.append(
                    "**No request body was observed.**"
                )

            lines.append("")

        else:

            lines.append(
                f"JSON requests: "
                f"**{endpoint.request_json_count}**"
            )

            lines.append("")

            lines.append(
                "**Request field frequency**"
            )

            lines.append("")

            lines.extend(
                render_field_table(
                    endpoint,
                    request=True
                )
            )

            lines.append("")

            lines.append(
                "**Request schema variants**"
            )

            lines.append("")

            variants = sorted(
                endpoint.request_variants.values(),
                key=lambda variant: -variant.count
            )

            for number, variant in enumerate(
                variants,
                start=1
            ):

                lines.append(
                    f"**Schema {number}** "
                    f"`{variant.fingerprint}` "
                    f"— {variant.count} requests"
                )

                lines.append("")

                lines.append("```json")

                lines.append(
                    render_schema(
                        variant.schema
                    )
                )

                lines.append("```")

                lines.append("")

        # ----------------------------------------------------
        # Response
        # ----------------------------------------------------

        lines.append(
            "#### Response"
        )

        lines.append("")

        if endpoint.response_content_types:

            content_types = ", ".join(
                f"`{ctype}` ({count})"
                for ctype, count
                in endpoint.response_content_types.items()
            )

            lines.append(
                f"Content types: {content_types}"
            )

            lines.append("")

        if endpoint.response_json_count == 0:

            if endpoint.response_non_json_count:

                lines.append(
                    "**No JSON response body was observed.**"
                )

            else:

                lines.append(
                    "**No response body was observed.**"
                )

            lines.append("")

        else:

            lines.append(
                f"JSON responses: "
                f"**{endpoint.response_json_count}**"
            )

            lines.append("")

            lines.append(
                "**Response field frequency**"
            )

            lines.append("")

            lines.extend(
                render_field_table(
                    endpoint,
                    request=False
                )
            )

            lines.append("")

            lines.append(
                "**Response schema variants**"
            )

            lines.append("")

            variants = sorted(
                endpoint.response_variants.values(),
                key=lambda variant: -variant.count
            )

            for number, variant in enumerate(
                variants,
                start=1
            ):

                lines.append(
                    f"**Schema {number}** "
                    f"`{variant.fingerprint}` "
                    f"— {variant.count} responses"
                )

                lines.append("")

                lines.append("```json")

                lines.append(
                    render_schema(
                        variant.schema
                    )
                )

                lines.append("```")

                lines.append("")

    # --------------------------------------------------------
    # Overall schema index
    # --------------------------------------------------------

    lines.append("---")
    lines.append("")

    lines.append(
        "## 5. Schema Index"
    )

    lines.append("")

    lines.append(
        "| Endpoint | Direction | Schema | Occurrences |"
    )

    lines.append(
        "|---|---|---|---:|"
    )

    for endpoint in endpoint_rows:

        for variant in sorted(
            endpoint.request_variants.values(),
            key=lambda variant: -variant.count
        ):

            lines.append(
                f"| `{endpoint.host}{endpoint.path}` | "
                f"Request | "
                f"`{variant.fingerprint}` | "
                f"{variant.count} |"
            )

        for variant in sorted(
            endpoint.response_variants.values(),
            key=lambda variant: -variant.count
        ):

            lines.append(
                f"| `{endpoint.host}{endpoint.path}` | "
                f"Response | "
                f"`{variant.fingerprint}` | "
                f"{variant.count} |"
            )

    lines.append("")

    # --------------------------------------------------------
    # Notes
    # --------------------------------------------------------

    lines.append("---")
    lines.append("")

    lines.append(
        "## 6. Interpretation Notes"
    )

    lines.append("")

    lines.append(
        "- Field percentages represent how often a field was observed "
        "among JSON messages for that endpoint."
    )

    lines.append(
        "- A field observed in approximately 100% of messages is "
        "treated as consistently present in the capture."
    )

    lines.append(
        "- Multiple schema fingerprints indicate structurally "
        "different JSON messages were observed for the same endpoint."
    )

    lines.append(
        "- Dynamic URL path components such as numeric IDs and UUIDs "
        "are normalized when constructing endpoint identities."
    )

    lines.append(
        "- JSON values are not included; only their observed structure "
        "and primitive types are reported."
    )

    lines.append("")

    Path(output_file).write_text(
        "\n".join(lines),
        encoding="utf-8"
    )


# ============================================================
# MAIN
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Analyze JSON message structures "
            "in a Grammarly Desktop mitmproxy capture."
        )
    )

    parser.add_argument(
        "flow_file",
        help="Path to the .mitm flow export"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="part2_json_analysis.md",
        help=(
            "Output Markdown filename "
            "(default: part2_json_analysis.md)"
        )
    )

    args = parser.parse_args()

    flow_path = Path(
        args.flow_file
    )

    if not flow_path.exists():

        print(
            f"[!] File not found: {flow_path}"
        )

        raise SystemExit(1)

    endpoints = {}

    total_flows = 0

    print(
        f"[+] Reading: {flow_path}"
    )

    with open(
        flow_path,
        "rb"
    ) as file:

        reader = FlowReader(file)

        for flow in reader.stream():

            total_flows += 1

            analyze_flow(
                flow,
                endpoints
            )

    print(
        f"[+] Flows read: {total_flows}"
    )

    print(
        f"[+] Grammarly endpoints: "
        f"{len(endpoints)}"
    )

    write_report(
        endpoints,
        total_flows,
        args.output
    )

    print(
        f"[+] Done!"
    )

    print(
        f"[+] Output: {args.output}"
    )


if __name__ == "__main__":
    main()
