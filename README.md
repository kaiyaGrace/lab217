# Glimpse 👀

**Glimpse** is a lightweight Python tool that analyzes **mitmproxy flow logs** to identify sensitive information captured from **Grammarly** network traffic.

It scans HTTP requests and responses for common types of sensitive data (PII, PHI, PCI-DSS, and credentials), summarizes the results in the terminal, and stores them in a **SQLite database** for further analysis using SQL.

---

## Features

- Detects common sensitive information including:
  - Passwords
  - API Keys & Tokens
  - Credit Card Numbers
  - Social Security Numbers
  - Medical Record Numbers
  - ICD Codes
  - Phone Numbers
  - Email Addresses
  - Usernames
  - Street Addresses
- Filters non-text and static assets to reduce noise
- Generates a terminal summary report
- Saves structured results to SQLite for additional querying

---

## Prerequisites

Before running Glimpse, make sure you have:

- Python **3.10+**
- **mitmproxy** installed
- A mitmproxy flow log (`.flow` file)
- SQLite (included with most Python installations)

### Install Dependencies

```bash
pip install mitmproxy
```

---

## Usage

### 1. Capture Traffic

Run mitmproxy/mitmweb and save a flow log.

Example:

```bash
mitmweb -w grammarly.flow
```

---

### 2. Run Glimpse

```bash
python3 analyze_flows.py grammarly.flow
```

Or specify an output database:

```bash
python3 analyze_flows.py grammarly.flow --db glimpse.db
```

---

### 3. View Results

Glimpse will:

- Analyze the captured Grammarly traffic
- Display a summary report in the terminal
- Save all findings into the SQLite database

---

## Output

The SQLite database contains two tables:

- **captured_flows** – metadata about each analyzed HTTP flow
- **sensitivity_matches** – all detected sensitive information and classifications

This database can be queried directly using SQLite or any SQL analysis tool.

---

## Notes

- Glimpse analyzes **only Grammarly traffic** contained within the provided mitmproxy flow log.
- Sensitive values are **partially masked** before being stored in the database.
- Static assets (JavaScript, images, CSS, fonts, etc.) are automatically ignored to improve performance and reduce false positives.

---

## License

Created for educational and cybersecurity research purposes.
