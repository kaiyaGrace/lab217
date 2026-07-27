# Grammarly Traffic Analysis Toolkit

Two complementary tools for inspecting Grammarly's network behavior through a transparent mitmproxy setup: **GLIMPSE**, a post-hoc sensitivity analyzer for saved flow logs, and **GLEAN**, a live endpoint/RPC behavior monitor.

---

## Contents

- [Tool Overview](#tool-overview)
- [Transparent Proxy Setup](#transparent-proxy-setup)
- [GLIMPSE](#glimpse)
- [GLEAN](#glean)
- [Screenshots](#screenshots)

---

## Tool Overview

| Tool | Acronym | Purpose |
|------|---------|---------|
| **GLIMPSE** | Grammarly Log Inspection for Metadata, Privacy & Sensitive-data Evaluation | Analyzes **saved** mitmweb flow logs offline to detect PII, PHI, PCI-DSS, and credential data transmitted to Grammarly's endpoints. |
| **GLEAN** | Grammarly Live Endpoint Analysis & Navigation | Runs **live** (or against saved logs) to inventory Grammarly's JSON/RPC endpoints, track schema drift, and flag anomalies in real time. |

Both tools consume traffic captured through a transparent proxy running on **Frodo**, routed from the target client (**Legolas**).

---

## Transparent Proxy Setup

**Prerequisites:** certificates configured and mitmproxy installed on Frodo.

On Frodo:

```bash
./runMitmWebRules
./tspMitmWeb
```

This routes client traffic from Legolas through Frodo's mitmweb instance, which both GLIMPSE and GLEAN read from.

---

## GLIMPSE

`analyze_flows.py` — reads a saved mitmproxy flow log, runs a local detection pipeline over HTTP request/response payloads, and writes structured results to SQLite alongside a CLI sensitivity report.

**Prerequisite:** a downloaded mitmweb flow log.

> **Important:** running GLIMPSE aggregates data into the database across runs. Flush the database before each new run to keep results scoped to a single log:
>
> ```bash
> rm flow_analysis.db
> ```

**Run on Frodo:**

```bash
python3 ~/github/glimpse/analyze_flows_v9.py ~/mitmWebLogs/mitmWeb_p5
```

GLIMPSE outputs a report covering:
- Destination hosts ranked by sensitive-data hit count (Critical/High/Medium/Low)
- Total flows and words processed
- Sensitive data classifications (Credentials, PII, PCI-DSS, PHI) with severity breakdown

---

## GLEAN

A mitmproxy/mitmweb addon and live dashboard that logs Grammarly's JSON-RPC endpoint behavior into SQLite, tracking endpoint inventory and schema-change anomalies as they occur.

**Prerequisite:** mitmweb and certificates configured (see [Transparent Proxy Setup](#transparent-proxy-setup)).

**Run on Frodo:**

```bash
./runMitmWebRules
./tspMitmWeb
```

Then, from the `glean` directory, launch the live dashboard:

```bash
cd ~/glean
python3 -m glean.cli attach --db data/glean.db --label control
```

GLEAN's live dashboard shows:
- A running endpoint inventory (path, hit count, first/last seen)
- Detected anomalies (new endpoints, new/disappeared fields, type changes) with review status

---

## Screenshots

**GLEAN — live endpoint inventory and anomaly detection:**

![GLEAN live dashboard showing endpoint inventory and schema-change anomalies](screenshots/glean_live_dashboard.png)

**GLIMPSE — PII/PHI sensitivity analysis report:**

![GLIMPSE report showing sensitive data by destination host and classification](screenshots/glimpse_sensitivity_report.png)
