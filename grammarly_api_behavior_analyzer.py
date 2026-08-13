#!/usr/bin/env python3

"""
Grammarly MITMWeb / mitmproxy Saved-Flow Analyzer

Usage:
    python analyze_grammarly_flows.py smallPractice_2

Optional:
    python analyze_grammarly_flows.py smallPractice_2 --out smallPractice_2_analysis

Requires:
    pip install mitmproxy
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

try:
    from mitmproxy.io import FlowReader
except ImportError:
    print(
        "\nERROR: mitmproxy is not installed.\n"
        "Install it with:\n\n"
        "    python -m pip install mitmproxy\n"
    )
    sys.exit(1)


# ============================================================
# CONFIGURATION
# ============================================================

GRAMMARLY_DOMAINS = (
    "grammarly.com",
    "grammarly.io",
)

TELEMETRY_HINTS = (
    "femetrics",
    "telemetry",
    "metrics",
)

AUTH_HINTS = (
    "/auth/",
    "/oauth/",
    "/login",
    "/logout",
    "/userinfo",
    "/token",
)

CONFIG_HINTS = (
    "/configuration/",
    "/config/",
    "/settings",
    "/experimentation/",
)

STATIC_EXTENSIONS = {
    ".js",
    ".css",
    ".map",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".otf",
    ".html",
}

SENSITIVE_FIELD_PATTERN = re.compile(
    r"""
    (
        token
        |access[_-]?token
        |refresh[_-]?token
        |authorization
        |cookie
        |password
        |passwd
        |secret
        |api[_-]?key
        |client[_-]?secret
        |session[_-]?id
        |user[_-]?id
        |email
        |credential
        |jwt
        |bearer
    )
    """,
    re.IGNORECASE | re.VERBOSE,
)


# ============================================================
# BASIC HELPERS
# ============================================================

def is_grammarly_host(host: str) -> bool:
    """Return True if the hostname belongs to Grammarly."""
    host = (host or "").lower().rstrip(".")

    return any(
        host == domain or host.endswith("." + domain)
        for domain in GRAMMARLY_DOMAINS
    )


def get_body(message) -> bytes:
    """Safely obtain the raw body from a mitmproxy request/response."""
    if message is None:
        return b""

    try:
        if message.raw_content:
            return bytes(message.raw_content)
    except Exception:
        pass

    try:
        if message.content:
            return bytes(message.content)
    except Exception:
        pass

    return b""


def get_content_type(message) -> str:
    """Safely obtain Content-Type."""
    if message is None:
        return ""

    try:
        return message.headers.get("content-type", "")
    except Exception:
        return ""


def parse_json(body: bytes):
    """Try to parse a body as JSON."""
    if not body:
        return None

    try:
        text = body.decode("utf-8", errors="replace").strip()
    except Exception:
        return None

    if not text:
        return None

    try:
        return json.loads(text)
    except Exception:
        return None


def value_type(value) -> str:
    """Return a useful JSON type name."""
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

    if isinstance(value, list):
        return "array"

    if isinstance(value, dict):
        return "object"

    return type(value).__name__


def is_sensitive_field(field_name: str) -> bool:
    """Detect field names that should never have their values exported."""
    return bool(SENSITIVE_FIELD_PATTERN.search(field_name))


def flatten_json(value, prefix="", depth=0, max_depth=8):
    """
    Convert JSON into a compact schema.

    Example:

        {
            "user": {
                "id": "abc"
            },
            "text": "hello"
        }

    becomes:

        user        object
        user.id     string
        text        string

    IMPORTANT:
    Values are never returned.
    """

    results = []

    if depth > max_depth:
        results.append(
            (
                prefix or "$",
                value_type(value),
            )
        )
        return results

    if isinstance(value, dict):

        if prefix:
            results.append(
                (
                    prefix,
                    "object",
                )
            )

        for key, child in value.items():

            key = str(key)

            path = (
                f"{prefix}.{key}"
                if prefix
                else key
            )

            results.extend(
                flatten_json(
                    child,
                    path,
                    depth + 1,
                    max_depth,
                )
            )

    elif isinstance(value, list):

        if prefix:
            results.append(
                (
                    prefix,
                    "array",
                )
            )

        # Don't analyze hundreds/thousands of identical array items.
        for child in value[:5]:

            results.extend(
                flatten_json(
                    child,
                    f"{prefix}[]",
                    depth + 1,
                    max_depth,
                )
            )

    else:

        results.append(
            (
                prefix or "$",
                value_type(value),
            )
        )

    return results


def timestamp_to_iso(timestamp):
    """Convert mitmproxy epoch timestamps to readable UTC."""
    if timestamp is None:
        return ""

    try:
        return datetime.fromtimestamp(
            float(timestamp),
            tz=timezone.utc,
        ).isoformat()
    except Exception:
        return str(timestamp)


# ============================================================
# ENDPOINT CLASSIFICATION
# ============================================================

def classify_endpoint(
    host: str,
    path: str,
    method: str,
    content_type: str,
) -> str:

    host_lower = host.lower()
    path_lower = path.lower()
    content_lower = content_type.lower()

    # Telemetry / metrics
    if any(
        hint in host_lower
        for hint in TELEMETRY_HINTS
    ):
        return "telemetry"

    # Authentication
    if any(
        hint in path_lower
        for hint in AUTH_HINTS
    ):
        return "authentication"

    # Configuration / settings
    if any(
        hint in path_lower
        for hint in CONFIG_HINTS
    ):
        return "configuration"

    # CORS
    if method.upper() == "OPTIONS":
        return "cors_preflight"

    # Static files
    try:
        extension = Path(
            urlsplit(
                "https://" + host + path
            ).path
        ).suffix.lower()
    except Exception:
        extension = ""

    if extension in STATIC_EXTENSIONS:
        return "static"

    # JSON / REST-like API
    if (
        "json" in content_lower
        or path_lower.startswith("/api/")
        or "/v1/" in path_lower
        or "/v2/" in path_lower
    ):
        return "api_candidate"

    return "other_grammarly"


# ============================================================
# CSV WRITER
# ============================================================

def write_csv(
    filename: Path,
    fieldnames,
    rows,
):

    with filename.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
            extrasaction="ignore",
        )

        writer.writeheader()

        for row in rows:
            writer.writerow(row)


# ============================================================
# MAIN ANALYSIS
# ============================================================

def analyze_flow_file(
    input_file: Path,
    output_directory: Path,
):

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    endpoint_stats = defaultdict(
        lambda: {
            "hosts": Counter(),
            "methods": Counter(),
            "categories": Counter(),
            "statuses": Counter(),

            "requests": 0,
            "responses": 0,

            "json_requests": 0,
            "json_responses": 0,

            "request_fields": Counter(),
            "response_fields": Counter(),

            "first_timestamp": None,
            "last_timestamp": None,
        }
    )

    request_field_types = defaultdict(
        lambda: defaultdict(Counter)
    )

    response_field_types = defaultdict(
        lambda: defaultdict(Counter)
    )

    request_field_rows = []
    response_field_rows = []
    timeline_rows = []

    total_flows = 0
    grammarly_flows = 0
    json_request_count = 0
    json_response_count = 0

    # --------------------------------------------------------
    # Read mitmproxy flow file
    # --------------------------------------------------------

    print()
    print("Reading mitmweb flow file...")
    print()

    with input_file.open("rb") as file:

        reader = FlowReader(file)

        for flow in reader.stream():

            total_flows += 1

            if total_flows % 5000 == 0:

                print(
                    f"  Processed {total_flows:,} flows..."
                )

            request = getattr(
                flow,
                "request",
                None,
            )

            if request is None:
                continue

            host = getattr(
                request,
                "host",
                "",
            ) or ""

            # ------------------------------------------------
            # Grammarly filter
            # ------------------------------------------------

            if not is_grammarly_host(host):
                continue

            grammarly_flows += 1

            method = (
                getattr(
                    request,
                    "method",
                    "",
                )
                or ""
            ).upper()

            path = (
                getattr(
                    request,
                    "path",
                    "",
                )
                or "/"
            )

            endpoint = (
                f"{method} {path}"
            )

            request_content_type = get_content_type(
                request
            )

            response = getattr(
                flow,
                "response",
                None,
            )

            response_content_type = get_content_type(
                response
            )

            category = classify_endpoint(
                host,
                path,
                method,
                request_content_type
                or response_content_type,
            )

            stats = endpoint_stats[
                endpoint
            ]

            # ------------------------------------------------
            # Basic endpoint statistics
            # ------------------------------------------------

            stats["requests"] += 1

            stats["hosts"][host] += 1

            stats["methods"][method] += 1

            stats["categories"][category] += 1

            timestamp = getattr(
                request,
                "timestamp_start",
                None,
            )

            if timestamp is not None:

                timestamp = float(timestamp)

                if (
                    stats["first_timestamp"]
                    is None
                    or timestamp
                    < stats["first_timestamp"]
                ):
                    stats["first_timestamp"] = timestamp

                if (
                    stats["last_timestamp"]
                    is None
                    or timestamp
                    > stats["last_timestamp"]
                ):
                    stats["last_timestamp"] = timestamp

            # ------------------------------------------------
            # Response
            # ------------------------------------------------

            status_code = ""

            if response is not None:

                stats["responses"] += 1

                status_code = str(
                    getattr(
                        response,
                        "status_code",
                        "",
                    )
                )

                if status_code:
                    stats["statuses"][
                        status_code
                    ] += 1

            # ------------------------------------------------
            # Request JSON
            # ------------------------------------------------

            request_json = parse_json(
                get_body(request)
            )

            request_fields = []

            if request_json is not None:

                json_request_count += 1

                stats["json_requests"] += 1

                request_fields = flatten_json(
                    request_json
                )

                for field_path, field_type in request_fields:

                    field_name = (
                        field_path
                        .split(".")[-1]
                        .replace("[]", "")
                    )

                    # Never output the value.
                    if is_sensitive_field(
                        field_name
                    ):
                        field_type += " [REDACTED]"

                    stats["request_fields"][
                        field_path
                    ] += 1

                    request_field_types[
                        endpoint
                    ][
                        field_path
                    ][
                        field_type
                    ] += 1

                    request_field_rows.append(
                        {
                            "endpoint": endpoint,
                            "host": host,
                            "field_path": field_path,
                            "type": field_type,
                            "timestamp_utc":
                                timestamp_to_iso(
                                    timestamp
                                ),
                        }
                    )

            # ------------------------------------------------
            # Response JSON
            # ------------------------------------------------

            response_json = None

            if response is not None:

                response_json = parse_json(
                    get_body(response)
                )

            response_fields = []

            if response_json is not None:

                json_response_count += 1

                stats["json_responses"] += 1

                response_fields = flatten_json(
                    response_json
                )

                for field_path, field_type in response_fields:

                    field_name = (
                        field_path
                        .split(".")[-1]
                        .replace("[]", "")
                    )

                    if is_sensitive_field(
                        field_name
                    ):
                        field_type += " [REDACTED]"

                    stats["response_fields"][
                        field_path
                    ] += 1

                    response_field_types[
                        endpoint
                    ][
                        field_path
                    ][
                        field_type
                    ] += 1

                    response_field_rows.append(
                        {
                            "endpoint": endpoint,
                            "host": host,
                            "field_path": field_path,
                            "type": field_type,
                            "timestamp_utc":
                                timestamp_to_iso(
                                    timestamp
                                ),
                        }
                    )

            # ------------------------------------------------
            # Timeline
            # ------------------------------------------------

            timeline_rows.append(
                {
                    "timestamp_utc":
                        timestamp_to_iso(
                            timestamp
                        ),

                    "method": method,

                    "host": host,

                    "path": path,

                    "endpoint": endpoint,

                    "category": category,

                    "request_json":
                        "yes"
                        if request_json is not None
                        else "no",

                    "request_field_count":
                        len(request_fields),

                    "response_status":
                        status_code,

                    "response_json":
                        "yes"
                        if response_json is not None
                        else "no",

                    "response_field_count":
                        len(response_fields),
                }
            )

    # ========================================================
    # BUILD ENDPOINT SUMMARY
    # ========================================================

    endpoint_rows = []

    for endpoint, stats in sorted(
        endpoint_stats.items()
    ):

        category = ""

        if stats["categories"]:

            category = (
                stats["categories"]
                .most_common(1)[0][0]
            )

        endpoint_rows.append(
            {
                "endpoint": endpoint,

                "hosts":
                    "; ".join(
                        host
                        for host, _ in
                        stats["hosts"]
                        .most_common(5)
                    ),

                "category":
                    category,

                "requests":
                    stats["requests"],

                "json_requests":
                    stats["json_requests"],

                "responses":
                    stats["responses"],

                "json_responses":
                    stats["json_responses"],

                "methods":
                    "; ".join(
                        f"{method}={count}"
                        for method, count
                        in stats["methods"]
                        .most_common()
                    ),

                "status_codes":
                    "; ".join(
                        f"{status}={count}"
                        for status, count
                        in stats["statuses"]
                        .most_common()
                    ),

                "first_seen_utc":
                    timestamp_to_iso(
                        stats["first_timestamp"]
                    ),

                "last_seen_utc":
                    timestamp_to_iso(
                        stats["last_timestamp"]
                    ),

                "unique_request_fields":
                    len(
                        stats["request_fields"]
                    ),

                "unique_response_fields":
                    len(
                        stats["response_fields"]
                    ),
            }
        )

    # ========================================================
    # BUILD FIELD SUMMARY
    # ========================================================

    field_summary_rows = []

    all_endpoints = (
        set(request_field_types)
        |
        set(response_field_types)
    )

    for endpoint in sorted(
        all_endpoints
    ):

        request_fields = (
            request_field_types
            .get(endpoint, {})
        )

        response_fields = (
            response_field_types
            .get(endpoint, {})
        )

        all_fields = (
            set(request_fields)
            |
            set(response_fields)
        )

        for field_path in sorted(
            all_fields
        ):

            request_types = (
                request_fields
                .get(field_path, {})
            )

            response_types = (
                response_fields
                .get(field_path, {})
            )

            request_count = sum(
                request_types.values()
            )

            response_count = sum(
                response_types.values()
            )

            field_summary_rows.append(
                {
                    "endpoint":
                        endpoint,

                    "field_path":
                        field_path,

                    "request_occurrences":
                        request_count,

                    "request_types":
                        "; ".join(
                            f"{field_type}={count}"
                            for field_type, count
                            in request_types
                            .most_common()
                        ),

                    "response_occurrences":
                        response_count,

                    "response_types":
                        "; ".join(
                            f"{field_type}={count}"
                            for field_type, count
                            in response_types
                            .most_common()
                        ),
                }
            )

    # ========================================================
    # SORT TIMELINE
    # ========================================================

    timeline_rows.sort(
        key=lambda row:
            row["timestamp_utc"]
    )

    # ========================================================
    # WRITE CSV FILES
    # ========================================================

    print()
    print("Writing results...")

    write_csv(
        output_directory
        / "endpoint_summary.csv",

        [
            "endpoint",
            "hosts",
            "category",
            "requests",
            "json_requests",
            "responses",
            "json_responses",
            "methods",
            "status_codes",
            "first_seen_utc",
            "last_seen_utc",
            "unique_request_fields",
            "unique_response_fields",
        ],

        endpoint_rows,
    )

    write_csv(
        output_directory
        / "request_fields.csv",

        [
            "endpoint",
            "host",
            "field_path",
            "type",
            "timestamp_utc",
        ],

        request_field_rows,
    )

    write_csv(
        output_directory
        / "response_fields.csv",

        [
            "endpoint",
            "host",
            "field_path",
            "type",
            "timestamp_utc",
        ],

        response_field_rows,
    )

    write_csv(
        output_directory
        / "endpoint_field_summary.csv",

        [
            "endpoint",
            "field_path",
            "request_occurrences",
            "request_types",
            "response_occurrences",
            "response_types",
        ],

        field_summary_rows,
    )

    write_csv(
        output_directory
        / "timeline.csv",

        [
            "timestamp_utc",
            "method",
            "host",
            "path",
            "endpoint",
            "category",
            "request_json",
            "request_field_count",
            "response_status",
            "response_json",
            "response_field_count",
        ],

        timeline_rows,
    )

    # ========================================================
    # BUILD MARKDOWN REPORT
    # ========================================================

    report = []

    report.append(
        "# Grammarly MITMWeb API Analysis"
    )

    report.append("")

    report.append(
        f"**Input:** `{input_file.name}`"
    )

    report.append("")

    report.append(
        f"- Total flows: **{total_flows:,}**"
    )

    report.append(
        f"- Grammarly flows: **{grammarly_flows:,}**"
    )

    report.append(
        f"- JSON request bodies: **{json_request_count:,}**"
    )

    report.append(
        f"- JSON response bodies: **{json_response_count:,}**"
    )

    report.append(
        f"- Unique endpoints: **{len(endpoint_rows):,}**"
    )

    report.append("")

    # --------------------------------------------------------
    # Endpoint table
    # --------------------------------------------------------

    report.append(
        "## Endpoint Summary"
    )

    report.append("")

    report.append(
        "| Method | Path | Category | Requests | JSON Req | JSON Resp | Req Fields | Resp Fields |"
    )

    report.append(
        "|---|---|---|---:|---:|---:|---:|---:|"
    )

    for row in endpoint_rows:

        try:
            method, path = (
                row["endpoint"]
                .split(" ", 1)
            )
        except ValueError:
            method = ""
            path = row["endpoint"]

        report.append(
            f"| `{method}` "
            f"| `{path}` "
            f"| {row['category']} "
            f"| {row['requests']} "
            f"| {row['json_requests']} "
            f"| {row['json_responses']} "
            f"| {row['unique_request_fields']} "
            f"| {row['unique_response_fields']} |"
        )

    report.append("")

    # --------------------------------------------------------
    # Request schemas
    # --------------------------------------------------------

    report.append(
        "## Request JSON Schemas"
    )

    report.append("")

    for endpoint in sorted(
        request_field_types
    ):

        report.append(
            f"### `{endpoint}`"
        )

        report.append("")

        report.append(
            "| Field | Occurrences | Type(s) |"
        )

        report.append(
            "|---|---:|---|"
        )

        for field_path, types in sorted(
            request_field_types[
                endpoint
            ].items()
        ):

            count = sum(
                types.values()
            )

            type_text = ", ".join(
                f"{field_type} ({count})"
                for field_type, count
                in types.most_common()
            )

            report.append(
                f"| `{field_path}` "
                f"| {count} "
                f"| {type_text} |"
            )

        report.append("")

    # --------------------------------------------------------
    # Response schemas
    # --------------------------------------------------------

    report.append(
        "## Response JSON Schemas"
    )

    report.append("")

    for endpoint in sorted(
        response_field_types
    ):

        report.append(
            f"### `{endpoint}`"
        )

        report.append("")

        report.append(
            "| Field | Occurrences | Type(s) |"
        )

        report.append(
            "|---|---:|---|"
        )

        for field_path, types in sorted(
            response_field_types[
                endpoint
            ].items()
        ):

            count = sum(
                types.values()
            )

            type_text = ", ".join(
                f"{field_type} ({count})"
                for field_type, count
                in types.most_common()
            )

            report.append(
                f"| `{field_path}` "
                f"| {count} "
                f"| {type_text} |"
            )

        report.append("")

    # --------------------------------------------------------
    # Interpretation notes
    # --------------------------------------------------------

    report.append(
        "## Interpretation Notes"
    )

    report.append("")

    report.append(
        "- This is an analysis of **observed network behavior**."
    )

    report.append(
        "- Endpoint categories are **heuristics**, not proof of Grammarly's backend architecture."
    )

    report.append(
        "- `api_candidate` means the endpoint looks API-like based on its path/content."
    )

    report.append(
        "- Telemetry endpoints are separated from likely application APIs."
    )

    report.append(
        "- Raw request/response values are intentionally NOT included."
    )

    report.append(
        "- Sensitive-looking field values are never written to the report."
    )

    report.append(
        "- Field names such as `user_id` may still appear because the field name itself is relevant to schema analysis."
    )

    report.append(
        "- WebSocket traffic should be analyzed separately from ordinary REST/HTTP JSON traffic."
    )

    report.append("")

    report.append(
        "## Next Research Question"
    )

    report.append("")

    report.append(
        "For the controlled experiment, compare the timeline against the manually performed actions:"
    )

    report.append("")

    report.append(
        "1. Open Word"
    )

    report.append(
        "2. Type text"
    )

    report.append(
        "3. Correct Grammarly errors"
    )

    report.append(
        "4. Ask Grammarly AI to rewrite"
    )

    report.append(
        "5. Insert the rewrite"
    )

    report.append(
        "6. Delete the old text"
    )

    report.append(
        "7. Close Word"
    )

    report.append("")

    report.append(
        "The goal is to identify endpoints and fields that appear/disappear or change around each behavior."
    )

    (
        output_directory
        / "report.md"
    ).write_text(
        "\n".join(report),
        encoding="utf-8",
    )

    # ========================================================
    # DONE
    # ========================================================

    print()
    print("=" * 60)
    print("DONE")
    print("=" * 60)

    print(
        f"Total flows:       {total_flows:,}"
    )

    print(
        f"Grammarly flows:   {grammarly_flows:,}"
    )

    print(
        f"JSON requests:     {json_request_count:,}"
    )

    print(
        f"JSON responses:    {json_response_count:,}"
    )

    print(
        f"Unique endpoints:  {len(endpoint_rows):,}"
    )

    print()
    print(
        f"Results saved to:\n{output_directory.resolve()}"
    )

    print()
    print(
        "START WITH:"
    )

    print(
        f"    {output_directory / 'report.md'}"
    )


# ============================================================
# COMMAND LINE
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Analyze a mitmweb/mitmproxy saved flow "
            "for Grammarly API endpoints and JSON schemas."
        )
    )

    parser.add_argument(
        "flow_file",
        type=Path,
        help="Path to the mitmweb saved-flow file",
    )

    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help=(
            "Output directory. "
            "Default: <flow_file>_analysis"
        ),
    )

    args = parser.parse_args()

    if not args.flow_file.exists():

        print(
            f"ERROR: File not found:\n{args.flow_file}"
        )

        sys.exit(1)

    if args.out is None:

        output_directory = Path(
            str(args.flow_file)
            + "_analysis"
        )

    else:

        output_directory = args.out

    try:

        analyze_flow_file(
            args.flow_file,
            output_directory,
        )

    except KeyboardInterrupt:

        print(
            "\n\nStopped by user."
        )

        sys.exit(130)

    except Exception as error:

        print()
        print("=" * 60)
        print("ERROR")
        print("=" * 60)

        print(
            f"{type(error).__name__}: {error}"
        )

        print()

        print(
            "If this is a FlowReader/flow-format error, "
            "send me the exact error message."
        )

        sys.exit(1)


if __name__ == "__main__":
    main()
    