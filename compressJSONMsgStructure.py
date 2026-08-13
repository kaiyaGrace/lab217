#!/usr/bin/env python3

"""
Compress Grammarly Part 2 JSON analysis.

Input:
    part2_json_analysis.md

Output:
    part2_compressed.md

The compressed report keeps:
    - endpoint
    - HTTP methods
    - request/response counts
    - content types
    - JSON schema variants
    - schema occurrence counts
    - field frequencies
    - field types

It removes:
    - repeated explanatory text
    - endpoint tree
    - endpoint frequency table
    - schema index
    - interpretation notes
    - duplicate formatting

It does NOT alter the observed schemas.
"""

import argparse
import re
from pathlib import Path


# ============================================================
# HELPERS
# ============================================================

def clean_line(line):
    return line.rstrip()


def extract_number(text, label):
    pattern = rf"\*\*{re.escape(label)}:\*\*\s*([0-9,]+)"
    match = re.search(pattern, text)

    if not match:
        return None

    return int(match.group(1).replace(",", ""))


def extract_inline_value(text, label):
    pattern = rf"\*\*{re.escape(label)}:\*\*\s*(.*)"
    match = re.search(pattern, text)

    if not match:
        return None

    return match.group(1).strip()


# ============================================================
# ENDPOINT PARSER
# ============================================================

def parse_endpoints(lines):

    endpoints = []

    current = None
    section = None
    subsection = None

    i = 0

    while i < len(lines):

        line = clean_line(lines[i])

        # ----------------------------------------------------
        # Endpoint header
        # ----------------------------------------------------

        if line.startswith("### `") and line.endswith("`"):

            if current is not None:
                endpoints.append(current)

            endpoint_text = line[5:-1]

            current = {
                "endpoint": endpoint_text,
                "methods": None,
                "requests": None,
                "statuses": None,

                "request_content_types": [],
                "response_content_types": [],

                "request_json_count": None,
                "response_json_count": None,

                "request_fields": [],
                "response_fields": [],

                "request_schemas": [],
                "response_schemas": [],
            }

            section = None
            subsection = None

            i += 1
            continue

        if current is None:
            i += 1
            continue

        # ----------------------------------------------------
        # Endpoint metadata
        # ----------------------------------------------------

        if line.startswith("**Observed methods:**"):

            current["methods"] = (
                line.split("**Observed methods:**", 1)[1]
                .strip()
            )

        elif line.startswith("**Observed requests:**"):

            current["requests"] = (
                line.split("**Observed requests:**", 1)[1]
                .strip()
            )

        elif line.startswith("**Response statuses:**"):

            current["statuses"] = (
                line.split("**Response statuses:**", 1)[1]
                .strip()
            )

        # ----------------------------------------------------
        # Request / Response sections
        # ----------------------------------------------------

        elif line == "#### Request":

            section = "request"
            subsection = None

        elif line == "#### Response":

            section = "response"
            subsection = None

        # ----------------------------------------------------
        # Content types
        # ----------------------------------------------------

        elif line.startswith("Content types:"):

            value = line.split(
                "Content types:",
                1
            )[1].strip()

            if section == "request":
                current["request_content_types"].append(value)

            elif section == "response":
                current["response_content_types"].append(value)

        # ----------------------------------------------------
        # JSON counts
        # ----------------------------------------------------

        elif line.startswith("JSON requests:"):

            match = re.search(
                r"\*\*(\d+)\*\*",
                line
            )

            if match:
                current["request_json_count"] = int(
                    match.group(1)
                )

        elif line.startswith("JSON responses:"):

            match = re.search(
                r"\*\*(\d+)\*\*",
                line
            )

            if match:
                current["response_json_count"] = int(
                    match.group(1)
                )

        # ----------------------------------------------------
        # Field tables
        # ----------------------------------------------------

        elif line == "**Request field frequency**":

            subsection = "request_fields"

        elif line == "**Response field frequency**":

            subsection = "response_fields"

        elif (
            line.startswith("|")
            and line.count("|") >= 3
            and subsection in (
                "request_fields",
                "response_fields",
            )
        ):

            # Skip table headers
            if (
                "Field" in line
                or line.startswith("|---")
            ):
                i += 1
                continue

            parts = [
                part.strip()
                for part in line.strip("|").split("|")
            ]

            if len(parts) >= 3:

                field = parts[0]
                presence = parts[1]
                field_type = parts[2]

                entry = (
                    f"{field} — "
                    f"{presence} — "
                    f"{field_type}"
                )

                if subsection == "request_fields":
                    current[
                        "request_fields"
                    ].append(entry)

                else:
                    current[
                        "response_fields"
                    ].append(entry)

        # ----------------------------------------------------
        # Schema sections
        # ----------------------------------------------------

        elif line == "**Request schema variants**":

            subsection = "request_schemas"

        elif line == "**Response schema variants**":

            subsection = "response_schemas"

        elif (
            line.startswith("**Schema ")
            and subsection in (
                "request_schemas",
                "response_schemas",
            )
        ):

            current_schema = {
                "header": line,
                "json": [],
            }

            # Find the opening ```json
            j = i + 1

            while j < len(lines):

                candidate = clean_line(
                    lines[j]
                )

                if candidate == "```json":
                    break

                j += 1

            if j >= len(lines):
                i += 1
                continue

            # Collect until closing ```
            j += 1

            while j < len(lines):

                candidate = clean_line(
                    lines[j]
                )

                if candidate == "```":
                    break

                current_schema[
                    "json"
                ].append(
                    candidate
                )

                j += 1

            if subsection == "request_schemas":

                current[
                    "request_schemas"
                ].append(
                    current_schema
                )

            else:

                current[
                    "response_schemas"
                ].append(
                    current_schema
                )

            i = j

        i += 1

    if current is not None:
        endpoints.append(current)

    return endpoints


# ============================================================
# REPORT RENDERING
# ============================================================

def render_endpoint(endpoint):

    lines = []

    lines.append(
        f"## {endpoint['endpoint']}"
    )

    lines.append("")

    if endpoint["methods"]:
        lines.append(
            f"**Methods:** {endpoint['methods']}"
        )

    if endpoint["requests"] is not None:
        lines.append(
            f"**Requests:** {endpoint['requests']}"
        )

    if endpoint["statuses"]:
        lines.append(
            f"**Statuses:** {endpoint['statuses']}"
        )

    lines.append("")

    # --------------------------------------------------------
    # Request
    # --------------------------------------------------------

    lines.append("### REQUEST")
    lines.append("")

    if endpoint["request_content_types"]:

        lines.append(
            "**Content-Type:** "
            + " | ".join(
                endpoint["request_content_types"]
            )
        )

        lines.append("")

    if endpoint["request_json_count"] is None:

        lines.append(
            "No JSON request body observed."
        )

        lines.append("")

    else:

        lines.append(
            f"**JSON messages:** "
            f"{endpoint['request_json_count']}"
        )

        lines.append("")

        if endpoint["request_fields"]:

            lines.append(
                "**Fields:**"
            )

            for field in endpoint[
                "request_fields"
            ]:

                lines.append(
                    f"- {field}"
                )

            lines.append("")

        if endpoint["request_schemas"]:

            lines.append(
                "**Schema variants:**"
            )

            lines.append("")

            for schema in endpoint[
                "request_schemas"
            ]:

                lines.append(
                    schema["header"]
                )

                lines.append("")

                lines.append("```json")

                lines.extend(
                    schema["json"]
                )

                lines.append("```")

                lines.append("")

    # --------------------------------------------------------
    # Response
    # --------------------------------------------------------

    lines.append("### RESPONSE")
    lines.append("")

    if endpoint["response_content_types"]:

        lines.append(
            "**Content-Type:** "
            + " | ".join(
                endpoint["response_content_types"]
            )
        )

        lines.append("")

    if endpoint["response_json_count"] is None:

        lines.append(
            "No JSON response body observed."
        )

        lines.append("")

    else:

        lines.append(
            f"**JSON messages:** "
            f"{endpoint['response_json_count']}"
        )

        lines.append("")

        if endpoint["response_fields"]:

            lines.append(
                "**Fields:**"
            )

            for field in endpoint[
                "response_fields"
            ]:

                lines.append(
                    f"- {field}"
                )

            lines.append("")

        if endpoint["response_schemas"]:

            lines.append(
                "**Schema variants:**"
            )

            lines.append("")

            for schema in endpoint[
                "response_schemas"
            ]:

                lines.append(
                    schema["header"]
                )

                lines.append("")

                lines.append("```json")

                lines.extend(
                    schema["json"]
                )

                lines.append("```")

                lines.append("")

    lines.append("---")
    lines.append("")

    return lines


def write_report(
    endpoints,
    output_file,
):

    lines = []

    lines.append(
        "# Grammarly Desktop — Part 2 "
        "Compressed JSON Analysis"
    )

    lines.append("")

    lines.append(
        f"**Endpoints analyzed:** {len(endpoints)}"
    )

    lines.append("")

    lines.append(
        "This report preserves the observed "
        "JSON schemas and field statistics while "
        "removing redundant report sections."
    )

    lines.append("")

    lines.append("---")
    lines.append("")

    # --------------------------------------------------------
    # Quick index
    # --------------------------------------------------------

    lines.append(
        "## Endpoint Index"
    )

    lines.append("")

    for number, endpoint in enumerate(
        endpoints,
        start=1
    ):

        lines.append(
            f"{number}. `{endpoint['endpoint']}`"
        )

    lines.append("")

    lines.append("---")
    lines.append("")

    # --------------------------------------------------------
    # Endpoint details
    # --------------------------------------------------------

    for endpoint in endpoints:

        lines.extend(
            render_endpoint(endpoint)
        )

    # --------------------------------------------------------
    # Final summary
    # --------------------------------------------------------

    total_request_schemas = sum(
        len(endpoint["request_schemas"])
        for endpoint in endpoints
    )

    total_response_schemas = sum(
        len(endpoint["response_schemas"])
        for endpoint in endpoints
    )

    json_request_endpoints = sum(
        1
        for endpoint in endpoints
        if endpoint["request_json_count"]
        is not None
    )

    json_response_endpoints = sum(
        1
        for endpoint in endpoints
        if endpoint["response_json_count"]
        is not None
    )

    lines.append(
        "# Summary"
    )

    lines.append("")

    lines.append(
        f"- Endpoints: **{len(endpoints)}**"
    )

    lines.append(
        f"- Endpoints with JSON requests: "
        f"**{json_request_endpoints}**"
    )

    lines.append(
        f"- Endpoints with JSON responses: "
        f"**{json_response_endpoints}**"
    )

    lines.append(
        f"- Request schema variants: "
        f"**{total_request_schemas}**"
    )

    lines.append(
        f"- Response schema variants: "
        f"**{total_response_schemas}**"
    )

    lines.append("")

    Path(
        output_file
    ).write_text(
        "\n".join(lines),
        encoding="utf-8"
    )


# ============================================================
# MAIN
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description=(
            "Compress Grammarly Part 2 "
            "JSON analysis."
        )
    )

    parser.add_argument(
        "input_file",
        nargs="?",
        default="part2_json_analysis.md",
        help=(
            "Input Part 2 Markdown file "
            "(default: part2_json_analysis.md)"
        ),
    )

    parser.add_argument(
        "-o",
        "--output",
        default="part2_compressed.md",
        help=(
            "Output Markdown file "
            "(default: part2_compressed.md)"
        ),
    )

    args = parser.parse_args()

    input_path = Path(
        args.input_file
    )

    if not input_path.exists():

        print(
            f"[!] Could not find: "
            f"{input_path}"
        )

        raise SystemExit(1)

    print(
        f"[+] Reading: {input_path}"
    )

    text = input_path.read_text(
        encoding="utf-8",
        errors="replace"
    )

    lines = text.splitlines()

    print(
        f"[+] Input lines: {len(lines):,}"
    )

    endpoints = parse_endpoints(
        lines
    )

    print(
        f"[+] Endpoints found: "
        f"{len(endpoints)}"
    )

    if not endpoints:

        print(
            "[!] No endpoint sections were "
            "found in the input file."
        )

        print(
            "[!] Make sure you are using the "
            "part2_json_analysis.md generated "
            "by part2_json_analyzer.py."
        )

        raise SystemExit(1)

    write_report(
        endpoints,
        args.output
    )

    output_path = Path(
        args.output
    )

    output_lines = (
        output_path
        .read_text(
            encoding="utf-8"
        )
        .splitlines()
    )

    print(
        f"[+] Output lines: "
        f"{len(output_lines):,}"
    )

    print(
        f"[+] Compression: "
        f"{100 * (1 - len(output_lines) / max(len(lines), 1)):.1f}%"
    )

    print(
        f"[+] Created: "
        f"{output_path}"
    )

    print()
    print(
        "[+] Done. Open the compressed file "
        "and paste it here."
    )


if __name__ == "__main__":
    main()
    