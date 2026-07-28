#citation: most code from claude, modified by copiolot and chatgpt 
#(cause I ran out of claude tokens D: )


#!/usr/bin/env python3
"""
analyze_flows.py
================
MITMProxy Flow Log PII/PHI/PCI/Credentials Analyzer

Reads a mitmproxy saved flow log, runs a localized detection pipeline
over HTTP request/response payloads, stores structured results in SQLite,
and prints a CLI analytical report.

Usage:
    python3 analyze_flows.py <path_to_flow_log> [--db flow_analysis.db]

Dependencies:
    pip install mitmproxy
"""

import re
import sys
import sqlite3
import argparse
import hashlib
from datetime import datetime
from urllib.parse import urlparse, parse_qs, urlencode

from mitmproxy.io import FlowReader
from mitmproxy.net.http import http1


# ---------------------------------------------------------------------------
# 1.  BINARY CONTENT-TYPE SKIP LIST
#     Payload types we skip to keep memory footprint low.
# ---------------------------------------------------------------------------
BINARY_CONTENT_TYPES = (
    "image/", "video/", "audio/",
    "application/octet-stream",
    "application/zip", "application/x-zip",
    "application/x-rar", "application/gzip",
    "application/pdf", "font/", "application/font",
    "application/wasm",
)

#citation: chat 7/15/26
STATIC_EXTENSIONS = (
    ".js",
    ".mjs",
    ".css",
    ".map",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".otf",
    ".eot",
)

#citation: chat 7/15/26
STATIC_PATHS = (
    "/static/",
    "/assets/",
    "/dist/",
    "/build/",
    "/fonts/",
    "/images/",
    "/img/",
)


def is_binary_content_type(ct: str) -> bool:
    """Return True if the Content-Type looks like binary/non-text data."""
    ct = ct.lower().split(";")[0].strip()
    return any(ct.startswith(b) for b in BINARY_CONTENT_TYPES)


# def is_static_asset(url: str) -> bool:
#     """Return True if the URL path ends with a common static asset extension."""
#     parsed = urlparse(url)
#     path = parsed.path.lower()
#     return any(path.endswith(ext) for ext in STATIC_EXTENSIONS)

#citation: chat 7/15/26
def is_static_asset(url: str) -> bool:
    """
    Return True if the URL points to a static asset that is unlikely to
    contain user-entered sensitive data.
    """
    try:
        path = urlparse(url).path.lower()

        if any(path.endswith(ext) for ext in STATIC_EXTENSIONS):
            return True

        if any(directory in path for directory in STATIC_PATHS):
            return True

        return False

    except Exception:
        return False


# ---------------------------------------------------------------------------
# 2.  REGEX PATTERNS
#     Each entry: (name, compiled_regex, classification, specific_type,
#                  severity, needs_context_check, context_keywords)
# ---------------------------------------------------------------------------

# Context window size (chars) around a high-stakes match
CONTEXT_WINDOW = 50

PATTERNS = [
    # --- CREDENTIALS (CRITICAL) ---
    {
        "name": "password_field",
        # Matches: password=secret, "password":"abc", passwd = "x", etc.
        "regex": re.compile(
            # \b ensures we don't match 'pass' inside 'bypass', 'surpass', 'compass', etc.
            # ["\']? after the key word handles JSON's `"password":"value"` shape,
            # where the key's closing quote sits between the word and the colon.
            r'(?i)\b(password|passwd|pass|pwd)["\']?\s*[=:]\s*["\']?([^\s"\',}]{4,})',
            re.IGNORECASE,
        ),
        "classification": "Credentials",
        "specific_type": "Password",
        "severity": "CRITICAL",
        "needs_context": False,
        "context_keywords": [],
        # Group index for the sensitive value (for masking)
        "value_group": 2,
        "prefix_group": 1,
    },
    {
        "name": "api_key_field",
        # Matches: api_key="abc123", "secret": "xyz", bearer <token>, etc.
        "regex": re.compile(
            r'(?i)(api[_\-]?key|api[_\-]?secret|secret[_\-]?key|access[_\-]?token'
            r'|auth[_\-]?token|bearer)["\']?\s*[=:\s]+["\']?([A-Za-z0-9\-_\.]{8,})["\']?',
            re.IGNORECASE,
        ),
        "classification": "Credentials",
        "specific_type": "API Key / Token",
        "severity": "CRITICAL",
        "needs_context": False,
        "context_keywords": [],
        "value_group": 2,
        "prefix_group": 1,
    },

    # --- PII: SSN (CRITICAL, requires context check) ---
    {
        "name": "ssn",
        # Standard SSN format: 123-45-6789
        "regex": re.compile(r"\b(\d{3}-\d{2}-\d{4})\b"),
        "classification": "PII",
        "specific_type": "SSN",
        "severity": "CRITICAL",
        "needs_context": True,
        # At least one of these must appear in the 50-char window around the match
        "context_keywords": ["ssn", "social", "security", "tax", "taxpayer", "tin"],
        "value_group": 1,
        "prefix_group": None,
    },

    # --- PCI-DSS: Credit Card (CRITICAL, Luhn validated separately) ---
    {
        "name": "credit_card",
        # 13–16 digit sequences, optionally space/dash separated
        # Common card prefixes handled by Luhn validation downstream
        "regex": re.compile(
            r"\b(?:4[0-9]{12}(?:[0-9]{3})?|"          # Visa
            r"5[1-5][0-9]{14}|"                        # MasterCard
            r"3[47][0-9]{13}|"                         # Amex
            r"3(?:0[0-5]|[68][0-9])[0-9]{11}|"        # Diners
            r"6(?:011|5[0-9]{2})[0-9]{12}|"            # Discover
            r"(?:2131|1800|35\d{3})\d{11}|"            # JCB
            r"\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4})\b" # Generic 16-digit
        ),
        "classification": "PCI-DSS",
        "specific_type": "Credit Card",
        "severity": "CRITICAL",
        "needs_context": False,
        "context_keywords": [],
        "value_group": 0,   # full match
        "prefix_group": None,
    },

    # --- PHI: Medical Record Number / ICD Codes (HIGH) ---
    {
        "name": "mrn",
        # MRN: alphanumeric ID near medical keywords.
        # Requires at least 1 uppercase letter prefix ({1,3} not {0,3}) so that
        # bare digit-only sequences (timestamps, IDs, port numbers) don't fire.
        "regex": re.compile(r"\b([A-Z]{1,3}\d{5,10})\b"),
        "classification": "PHI",
        "specific_type": "Medical Record Number",
        "severity": "HIGH",
        "needs_context": True,
        "context_keywords": [
            "mrn", "medical record", "patient", "diagnosis", "rx",
            "icd", "icd-10", "icd10", "prescription", "dob", "date of birth",
        ],
        "value_group": 1,
        "prefix_group": None,
    },
    {
        "name": "icd_code",
        # ICD-10 codes: Letter followed by 2 digits, optional decimal + more digits
        "regex": re.compile(r"\b([A-Z]\d{2}(?:\.\d{1,4})?)\b"),
        "classification": "PHI",
        "specific_type": "ICD Code",
        "severity": "HIGH",
        "needs_context": True,
        "context_keywords": [
            "diagnosis", "icd", "icd-10", "icd10", "code", "condition",
            "procedure", "dx", "billing",
        ],
        "value_group": 1,
        "prefix_group": None,
    },

    # --- PII: Phone Number (MEDIUM) ---
    {
        "name": "phone",
        # US phone formats: (123) 456-7890  /  123-456-7890  /  123.456.7890
        # FIX: area code is now MANDATORY (was optional, causing bare 7-digit
        # sequences like port numbers and IDs to fire constantly).
        # A separator (space / dash / dot) is required between each group so
        # compact numeric strings don't match.
        "regex": re.compile(
            r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b"
        ),
        "classification": "PII",
        "specific_type": "Phone Number",
        "severity": "MEDIUM",
        # FIX: enable context check — phone numbers appear legitimately everywhere
        # in web content; only flag when a phone-related keyword is nearby.
        "needs_context": True,
        "context_keywords": [
            "phone", "tel", "telephone", "mobile", "cell", "call",
            "contact", "fax", "sms", "number", "reach",
        ],
        "value_group": 0,
        "prefix_group": None,
    },
    {
        "name": "street_address",
        # Simple street address heuristic: number + street name + type
        "regex": re.compile(
            # FIX: changed [A-Za-z0-9\s] → [A-Za-z\s] for the street name segment.
            # Allowing digits there caused matches on things like "4 bytes 1234 Rd"
            # or numeric IDs next to a road-type abbreviation in web responses.
            r"\b\d{1,5}\s+[A-Za-z\s]{3,30}"
            r"(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Drive|Dr|"
            r"Lane|Ln|Court|Ct|Place|Pl|Way|Circle|Cir)\b",
            re.IGNORECASE,
        ),
        "classification": "PII",
        "specific_type": "Street Address",
        "severity": "MEDIUM",
        "needs_context": False,
        "context_keywords": [],
        "value_group": 0,
        "prefix_group": None,
    },

    # --- PII: Email Address (LOW) ---
    {
        "name": "email",
        # RFC-5321-ish email pattern
        "regex": re.compile(
            r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b"
        ),
        "classification": "PII",
        "specific_type": "Email Address",
        "severity": "LOW",
        "needs_context": False,
        "context_keywords": [],
        "value_group": 0,
        "prefix_group": None,
    },
    {
        "name": "username_field",
        # Matches: username="kaiya", user: "admin", etc.
        "regex": re.compile(
            # FIX: removed bare 'user' from the alternation.
            # 'user' is ubiquitous in web traffic (/user/profile paths, User-Agent
            # headers, JSON keys like "user_id", "user_data") and generated masses
            # of false positives. 'username' and 'user_name' are specific enough
            # to only appear in actual credential/form contexts.
            r'(?i)\b(username|user_name)["\']?\s*[=:]\s*["\']?([A-Za-z0-9_@.\-]{3,})["\']?'
        ),
        "classification": "PII",
        "specific_type": "Username",
        "severity": "LOW",
        "needs_context": False,
        "context_keywords": [],
        "value_group": 2,
        "prefix_group": 1,
    },
]


# ---------------------------------------------------------------------------
# 3.  ALGORITHMIC HELPERS
# ---------------------------------------------------------------------------

def luhn_check(number_str: str) -> bool:
    """
    Validate a credit card number string using the Luhn (Mod 10) algorithm.
    Strips spaces and dashes before checking.
    Returns True if the number passes Luhn validation.
    """
    digits = re.sub(r"[\s\-]", "", number_str)
    if not digits.isdigit():
        return False

    total = 0
    reverse_digits = digits[::-1]
    for i, d in enumerate(reverse_digits):
        n = int(d)
        if i % 2 == 1:          # Every second digit from the right gets doubled
            n *= 2
            if n > 9:
                n -= 9          # Subtract 9 if result is two digits (same as summing)
        total += n

    return total % 10 == 0


def mask_value(value: str, specific_type: str) -> str:
    """
    Partially mask a sensitive value for safe storage.
    Shows enough for identification without full exposure.
    """
    v = value.strip("\"'")
    if specific_type in ("SSN",):
        # Keep first 3 and last 4: 555-XX-1234
        parts = v.split("-")
        if len(parts) == 3:
            return f"{parts[0]}-XX-{parts[2]}"
        return v[:3] + "-XXX-" + v[-4:]

    elif specific_type == "Credit Card":
        digits_only = re.sub(r"[\s\-]", "", v)
        return "XXXX-XXXX-XXXX-" + digits_only[-4:]

    elif specific_type in ("Password", "API Key / Token"):
        if len(v) <= 4:
            return "****"
        return v[:2] + "*" * (len(v) - 4) + v[-2:]

    elif specific_type == "Phone Number":
        digits = re.sub(r"\D", "", v)
        if len(digits) >= 10:
            return digits[:3] + "-XXX-" + digits[-4:]
        return v[:3] + "****"

    elif specific_type == "Email Address":
        at = v.find("@")
        if at > 1:
            return v[0] + "*" * (at - 1) + v[at:]
        return v

    else:
        # Generic: show first 3 and last 2 chars
        if len(v) <= 5:
            return "***"
        return v[:3] + "***" + v[-2:]


def context_check(text: str, match_start: int, match_end: int, keywords: list) -> bool:
    """
    Inspect a window of CONTEXT_WINDOW characters on each side of a regex match
    and return True if at least one context keyword appears in that window.

    This is the false-positive filter for high-stakes patterns like SSN and MRN,
    where a bare number match is too noisy without surrounding semantic context.
    """
    window_start = max(0, match_start - CONTEXT_WINDOW)
    window_end = min(len(text), match_end + CONTEXT_WINDOW)
    surrounding = text[window_start:window_end].lower()
    return any(kw.lower() in surrounding for kw in keywords)


# ---------------------------------------------------------------------------
# 4.  PAYLOAD EXTRACTION
# ---------------------------------------------------------------------------

def extract_text_from_flow(flow) -> tuple[str, str, str]:
    """
    Extract plain-text content from an HTTP flow's request and response.

    Returns:
        (combined_text, content_type, url)
    """
    parts = []
    content_type = ""

    # --- Request ---
    req = flow.request
    url = req.pretty_url

    # Query string parameters (always text)
    if req.query:
        qs = urlencode(dict(req.query))
        parts.append(f"[QUERY] {qs}")

    # Request body — skip binary types
    req_ct = req.headers.get("content-type", "")
    if req_ct:
        content_type = req_ct
    if req.content and not is_binary_content_type(req_ct):
        try:
            body = req.content.decode("utf-8", errors="replace")
            parts.append(f"[REQ_BODY] {body}")
        except Exception:
            pass

    # --- Response ---
    if flow.response:
        resp = flow.response
        resp_ct = resp.headers.get("content-type", "")
        if resp_ct and not content_type:
            content_type = resp_ct
        try:
            resp_body = resp.get_content(strict=False)
        except ValueError:
            resp_body = None
        if resp_body and not is_binary_content_type(resp_ct):
            try:
                body = resp_body.decode("utf-8", errors="replace")
                parts.append(f"[RESP_BODY] {body}")
            except Exception:
                pass
                pass

    combined = "\n".join(parts)
    return combined, content_type, url


# ---------------------------------------------------------------------------
# 5.  DETECTION PIPELINE
# ---------------------------------------------------------------------------

def detect_sensitive_data(text: str) -> list[dict]:
    """
    Run the full detection pipeline over a text payload.

    Steps:
      1. Regex pattern matching
      2. Context window check (for SSN, MRN, ICD codes)
      3. Luhn algorithm validation (for credit cards)
      4. Build and return list of match dicts
    """
    matches = []
    # Deduplicate: avoid reporting the same value+type twice per flow
    seen = set()

    for pattern in PATTERNS:
        for m in pattern["regex"].finditer(text):
            # Extract the sensitive value from the appropriate capture group
            group_idx = pattern["value_group"]
            try:
                raw_value = m.group(group_idx) if group_idx != 0 else m.group(0)
            except IndexError:
                raw_value = m.group(0)

            if not raw_value:
                continue

            raw_value = raw_value.strip()

            # --- Context window check (for high-stakes patterns) ---
            if pattern["needs_context"]:
                if not context_check(text, m.start(), m.end(), pattern["context_keywords"]):
                    continue  # Skip — no supporting context found nearby

            # --- Luhn validation for credit cards ---
            if pattern["specific_type"] == "Credit Card":
                if not luhn_check(raw_value):
                    continue  # Fails Luhn — likely not a real card number

            # --- Deduplicate within this flow ---
            dedup_key = (pattern["specific_type"], raw_value[:12])
            if dedup_key in seen:
                continue
            seen.add(dedup_key)

            # --- Mask and record ---
            masked = mask_value(raw_value, pattern["specific_type"])
            matches.append({
                "text_captured": masked,
                "sensitivity_level": pattern["severity"],
                "classification": pattern["classification"],
                "specific_type": pattern["specific_type"],
            })

    return matches


# ---------------------------------------------------------------------------
# 6.  DATABASE SETUP
# ---------------------------------------------------------------------------

DB_SCHEMA = """
CREATE TABLE IF NOT EXISTS captured_flows (
    flow_id      TEXT PRIMARY KEY,
    timestamp    DATETIME,
    source       TEXT,
    ip_address   TEXT,
    url          TEXT,
    method       TEXT,
    content_type TEXT,
    word_count   INTEGER,
    source_file  TEXT
);

CREATE INDEX IF NOT EXISTS idx_flows_source_file
    ON captured_flows(source_file);

CREATE TABLE IF NOT EXISTS sensitivity_matches (
    match_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    flow_id          TEXT REFERENCES captured_flows(flow_id),
    text_captured    TEXT,
    sensitivity_level TEXT,
    classification   TEXT,
    specific_type    TEXT
);

-- Indexes for efficient analytical queries
CREATE INDEX IF NOT EXISTS idx_flows_source
    ON captured_flows(source);

CREATE INDEX IF NOT EXISTS idx_matches_flow_id
    ON sensitivity_matches(flow_id);

CREATE INDEX IF NOT EXISTS idx_matches_severity
    ON sensitivity_matches(sensitivity_level);

CREATE INDEX IF NOT EXISTS idx_matches_classification
    ON sensitivity_matches(classification);
"""


def init_db(db_path: str) -> sqlite3.Connection:
    """Initialize the SQLite database, creating tables and indexes."""
    conn = sqlite3.connect(db_path)
    conn.executescript(DB_SCHEMA)
    conn.commit()
    return conn


# def insert_flow(conn: sqlite3.Connection, flow_id: str, timestamp: str,
#                 source: str, url: str, method: str,
#                 content_type: str, word_count: int, source_file: str):
#     """
#     Insert a flow record using INSERT OR IGNORE to enforce idempotency.
#     Reruns won't create duplicates.
#     """
#     conn.execute(
#         """
#         INSERT OR IGNORE INTO captured_flows
#             (flow_id, timestamp, source, url, method, content_type, word_count, source_file)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#         """,
#         (flow_id, timestamp, source, url, method, content_type, word_count, source_file),
#     )

#citation: claude 7/24/26
def insert_flow(conn: sqlite3.Connection, flow_id: str, timestamp: str,
                source: str, ip_address: str, url: str, method: str,
                content_type: str, word_count: int, source_file: str):
    conn.execute(
        """
        INSERT OR IGNORE INTO captured_flows
            (flow_id, timestamp, source, ip_address, url, method, content_type, word_count, source_file)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (flow_id, timestamp, source, ip_address, url, method, content_type, word_count, source_file),
    )

#citation: gemini, approved by chatgpt 7/15/26
def insert_matches(conn: sqlite3.Connection, flow_id: str, matches: list[dict]):
    """Insert all sensitivity matches for a given flow, clearing old ones first to prevent duplicates."""
    # 1. Clear out previous matches for this flow
    conn.execute("DELETE FROM sensitivity_matches WHERE flow_id = ?", (flow_id,))
    
    # 2. Insert the fresh matches
    conn.executemany(
        """
        INSERT INTO sensitivity_matches
            (flow_id, text_captured, sensitivity_level, classification, specific_type)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (flow_id, m["text_captured"], m["sensitivity_level"],
             m["classification"], m["specific_type"])
            for m in matches
        ],
    )

# def insert_matches(conn: sqlite3.Connection, flow_id: str, matches: list[dict]):
#     """Insert all sensitivity matches for a given flow."""
#     conn.executemany(
#         """
#         INSERT INTO sensitivity_matches
#             (flow_id, text_captured, sensitivity_level, classification, specific_type)
#         VALUES (?, ?, ?, ?, ?)
#         """,
#         [
#             (flow_id, m["text_captured"], m["sensitivity_level"],
#              m["classification"], m["specific_type"])
#             for m in matches
#         ],
#     )


# ---------------------------------------------------------------------------
# 7.  ANALYTICAL SQL QUERIES & REPORTING
# ---------------------------------------------------------------------------

SEVERITY_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}

# ANSI color codes for the CLI report
RED     = "\033[91m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

SEVERITY_COLORS = {
    "CRITICAL": RED,
    "HIGH":     YELLOW,
    "MEDIUM":   CYAN,
    "LOW":      GREEN,
}


def severity_color(level: str) -> str:
    return SEVERITY_COLORS.get(level, "")


def print_report(conn: sqlite3.Connection, source_file: str):
    """Run the three required analytical queries, scoped to this run's source_file,
    and print a formatted report."""
    sep = "=" * 65

    print(f"\n{BOLD}{sep}{RESET}")
    print(f"{BOLD}   MITMPROXY FLOW LOG — PII/PHI SENSITIVITY ANALYSIS REPORT{RESET}")
    print(f"{BOLD}{sep}{RESET}\n")

    # -----------------------------------------------------------------------
    # QUERY 1: Which source host has the most sensitive data?
    # Filter: severity HIGH or CRITICAL; group by source
    # -----------------------------------------------------------------------
    #citation: claude 7/24/26
    print(f"{BOLD}[Q1] DESTINATION WEBSITES WITH THE MOST SENSITIVE DATA{RESET}")
    print(f"     (Top 10, ranked by CRITICAL > HIGH > MEDIUM > LOW hit counts)\n")

    q1 = """
        SELECT
            cf.source,
            SUM(CASE WHEN sm.sensitivity_level = 'CRITICAL' THEN 1 ELSE 0 END) AS critical_count,
            SUM(CASE WHEN sm.sensitivity_level = 'HIGH'     THEN 1 ELSE 0 END) AS high_count,
            SUM(CASE WHEN sm.sensitivity_level = 'MEDIUM'   THEN 1 ELSE 0 END) AS medium_count,
            SUM(CASE WHEN sm.sensitivity_level = 'LOW'      THEN 1 ELSE 0 END) AS low_count,
            COUNT(sm.match_id) AS total_hits
        FROM sensitivity_matches sm
        JOIN captured_flows cf ON sm.flow_id = cf.flow_id
        WHERE cf.source_file = ?
        GROUP BY cf.source
        ORDER BY critical_count DESC, high_count DESC, medium_count DESC, low_count DESC, total_hits DESC
        LIMIT 10
    """
    rows = conn.execute(q1, (source_file,)).fetchall()
    if rows:
        print(f"  {'Rank':<5} {'Website Host':<30} {'Crit':>5} {'High':>5} "
              f"{'Med':>5} {'Low':>5} {'Total':>6}")
        print(f"  {'-'*5} {'-'*30} {'-'*5} {'-'*5} {'-'*5} {'-'*5} {'-'*6}")
        for rank, (source, crit, high, med, low, total) in enumerate(rows, 1):
            # Color the row by the highest severity actually present
            if crit:
                color = RED
            elif high:
                color = YELLOW
            elif med:
                color = CYAN
            else:
                color = GREEN
            print(f"  {color}{rank:<5} {source or '(unknown)':<30} "
                  f"{crit:>5} {high:>5} {med:>5} {low:>5} {total:>6}{RESET}")
    else:
        print("  No sensitivity matches found.\n")

    print()

    # -----------------------------------------------------------------------
    # QUERY 2: Total words processed across all flows
    # -----------------------------------------------------------------------
    print(f"{BOLD}[Q2] TOTAL WORDS CAPTURED / PROCESSED{RESET}\n")

    q2 = "SELECT COALESCE(SUM(word_count), 0) FROM captured_flows WHERE source_file = ?"
    total_words = conn.execute(q2, (source_file,)).fetchone()[0]

    q2b = "SELECT COUNT(*) FROM captured_flows WHERE source_file = ?"
    total_flows = conn.execute(q2b, (source_file,)).fetchone()[0]

    print(f"  Total flows processed : {BOLD}{total_flows:,}{RESET}")
    print(f"  Total words processed : {BOLD}{total_words:,}{RESET}")
    print()

    # -----------------------------------------------------------------------
    # QUERY 3: Most common classification of sensitive data
    # Group by classification + specific_type, order by occurrence count
    # -----------------------------------------------------------------------
    print(f"{BOLD}[Q3] MOST COMMON SENSITIVE DATA CLASSIFICATIONS{RESET}")
    print(f"     (all matches, grouped by type)\n")

    q3 = """
        SELECT
            sm.classification,
            sm.specific_type,
            sm.sensitivity_level,
            COUNT(*) AS occurrences
        FROM sensitivity_matches sm
        JOIN captured_flows cf ON sm.flow_id = cf.flow_id
        WHERE cf.source_file = ?
        GROUP BY sm.classification, sm.specific_type
        ORDER BY occurrences DESC
    """
    rows = conn.execute(q3, (source_file,)).fetchall()
    if rows:
        print(f"  {'#':<5} {'Classification':<14} {'Specific Type':<25} "
              f"{'Severity':<10} {'Count':>6}")
        print(f"  {'-'*5} {'-'*14} {'-'*25} {'-'*10} {'-'*6}")
        for rank, (cls, stype, sev, count) in enumerate(rows, 1):
            color = severity_color(sev)
            print(f"  {rank:<5} {cls:<14} {stype:<25} "
                  f"{color}{sev:<10}{RESET} {count:>6}")
    else:
        print("  No sensitivity matches recorded.\n")

    print()

    # -----------------------------------------------------------------------
    # BONUS: Quick summary totals
    # -----------------------------------------------------------------------
    print(f"{BOLD}[SUMMARY] MATCH COUNTS BY SEVERITY LEVEL{RESET}\n")
    q4 = """
        SELECT sm.sensitivity_level, COUNT(*) AS cnt
        FROM sensitivity_matches sm
        JOIN captured_flows cf ON sm.flow_id = cf.flow_id
        WHERE cf.source_file = ?
        GROUP BY sm.sensitivity_level
        ORDER BY cnt DESC
    """
    sev_rows = conn.execute(q4, (source_file,)).fetchall()
    if sev_rows:
        #citation: chatgpt 7/16/26
        max_count = max(cnt for _, cnt in sev_rows)

        for sev, cnt in sev_rows:
            color = severity_color(sev)
            bar_length = max(1, int((cnt / max_count) * 40))
            bar = "█" * bar_length

            print(f"  {color}{sev:<10}{RESET}  {cnt:>5}  {color}{bar}{RESET}")
        # for sev, cnt in sev_rows:
        #     color = severity_color(sev)
        #     bar = "█" * min(cnt, 40)
        #     print(f"  {color}{sev:<10}{RESET}  {cnt:>5}  {color}{bar}{RESET}")
    else:
        print("  No matches recorded.")

    print(f"\n{BOLD}{sep}{RESET}\n")


# ---------------------------------------------------------------------------
# 8.  MAIN FLOW PROCESSING LOOP
# ---------------------------------------------------------------------------

def generate_flow_id(flow) -> str:
    """
    Generate a stable, unique ID for a flow.
    Uses mitmproxy's own flow.id if available, otherwise hashes key fields.
    """
    if hasattr(flow, "id") and flow.id:
        return str(flow.id)
    # Fallback: hash timestamp + URL + method
    raw = f"{flow.request.timestamp_start}|{flow.request.pretty_url}|{flow.request.method}"
    return hashlib.sha1(raw.encode()).hexdigest()

#start claude code edits 7/24/26

# def get_source(flow) -> str:
#     """
#     Return the destination hostname of the flow (i.e., the website being visited).

#     WHY: In a transparent proxy setup all flows share the same client IP, making
#     Q1 ("which source has the most sensitive data?") trivially flat and useless.
#     Using the request host instead answers the meaningful question:
#     "which website's traffic contains the most HIGH/CRITICAL-severity data?"
#     """
#     try:
#         host = flow.request.host
#         if host:
#             return host
#     except Exception:
#         pass
#     # Fallback: parse from pretty_url
#     try:
#         return urlparse(flow.request.pretty_url).netloc or "unknown"
#     except Exception:
#         return "unknown"

def get_source(flow) -> str:
    """
    Return the destination HOSTNAME of the flow (i.e., the website being visited).
    Prefers pretty_host, which resolves the actual domain name when available,
    instead of falling back to the raw connection IP.
    """
    try:
        host = flow.request.pretty_host
        if host:
            return host
    except Exception:
        pass
    try:
        return flow.request.host or "unknown"
    except Exception:
        return "unknown"


def get_ip(flow) -> str:
    """
    Return the destination IP address of the flow, if available.
    Pulled from the server connection rather than the Host header.
    """
    try:
        if flow.server_conn and flow.server_conn.peername:
            return flow.server_conn.peername[0]
    except Exception:
        pass
    try:
        if flow.server_conn and flow.server_conn.address:
            return flow.server_conn.address[0]
    except Exception:
        pass
    return None
#end claude code 7/24/26


def process_flow_log(flow_log_path: str, db_path: str):
    """
    Main processing loop:
      1. Open the mitmproxy flow log
      2. For each HTTP flow: extract payload, run detection, write to DB
      3. Print the analytical report
    """
    conn = init_db(db_path)

    flows_processed = 0
    flows_skipped   = 0
    total_matches   = 0

    print(f"[*] Opening flow log: {flow_log_path}")
    print(f"[*] Database: {db_path}\n")

    with open(flow_log_path, "rb") as f:
        reader = FlowReader(f)

        for flow in reader.stream():
            # We only process HTTP flows (not WebSocket, DNS, TCP raw, etc.)
            if not hasattr(flow, "request") or flow.request is None:
                flows_skipped += 1
                continue

            
            #citation: gemini 7/15/26
            #ISOLATE GRAMMARLY TRAFFIC ONLY
            host = flow.request.pretty_host.lower() if hasattr(flow.request, "pretty_host") else ""
            if "grammarly" not in host:
                flows_skipped += 1
                continue


            flow_id   = generate_flow_id(flow)
            source    = get_source(flow)
            ip_address = get_ip(flow) #claude 7/24/26
            method    = flow.request.method
            url       = flow.request.pretty_url
            timestamp = datetime.utcfromtimestamp(
                flow.request.timestamp_start
            ).isoformat() if flow.request.timestamp_start else datetime.utcnow().isoformat()

            # # --- Payload Extraction ---
            # combined_text, content_type, _ = extract_text_from_flow(flow)

            # # Skip flows with no text payload
            # if not combined_text.strip():
            #     flows_skipped += 1
            #     continue

            #citation: chat 7/15/26
            combined_text, content_type, url = extract_text_from_flow(flow)

            content_type = (content_type or "").lower()

            # Skip static web assets (JavaScript, CSS, images, fonts, etc.)
            if (
                is_static_asset(url)
                or "javascript" in content_type
                or "ecmascript" in content_type
            ):
                flows_skipped += 1
                continue

            # Skip flows with no text payload
            # if not combined_text.strip():
            #     flows_skipped += 1
            #     continue
            #end chatgpt
        

            word_count = len(combined_text.split())

            # --- Detection Pipeline ---
            matches = detect_sensitive_data(combined_text)

            # --- Persist to DB ---
            with conn:  # Automatic transaction commit/rollback
                insert_flow(
                    conn, flow_id, timestamp, source, ip_address, url,
                    method, content_type, word_count, flow_log_path,
                )
                if matches:
                    insert_matches(conn, flow_id, matches)

            flows_processed += 1
            total_matches   += len(matches)

            # Progress indicator for large logs
            if flows_processed % 100 == 0:
                print(f"  ... processed {flows_processed} flows, "
                      f"{total_matches} matches so far")

    print(f"\n[+] Done.")
    print(f"    Flows processed : {flows_processed:,}")
    print(f"    Flows skipped   : {flows_skipped:,}  (no text payload / non-HTTP)")
    print(f"    Total matches   : {total_matches:,}")

    # --- Analytical Report ---
    print_report(conn, flow_log_path)
    conn.close()


# ---------------------------------------------------------------------------
# 9.  ENTRY POINT
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Analyze mitmproxy flow logs for PII, PHI, PCI, and Credentials."
    )
    parser.add_argument(
        "flow_log",
        help="Path to the mitmproxy saved flow log file (binary format).",
    )
    parser.add_argument(
        "--db",
        default="flow_analysis.db",
        help="Path for the SQLite output database (default: flow_analysis.db).",
    )
    args = parser.parse_args()

    process_flow_log(args.flow_log, args.db)


if __name__ == "__main__":
    main()
    