# Lab 217

## Contents

- [Background](#background)
- [Prerequisites](#prerequisites)
- [Tool Overview](#tool-overview)
- [Citations](#citations)

## Background

This summer, I have had the privilege of working with Prof. Kroll at the Naval Postgraduate School (NPS) through the Naval Research Labs Internship Program (NREIP). We researched the security risks associated with using Grammarly and how those risks affect the campus community.

My project specifically focused on determining whether certain combinations of Grammarly settings were more prone to leaking sensitive data than others.

Along the way, I realized that the specific tools I wanted to use did not exist.

So, I did my best to create them!

**View the poster:** [Canva](https://canva.link/j3dkh5pfszbgdjo)

## Prerequisites

- [mitmproxy](https://mitmproxy.org/)
- SQL
- Python

## Tool Overview

### Glimpse

Analyzes saved MITMWeb flows and provides a command-line summary of what sensitive data was captured and where it originated.

Glimpse aggregates information into a database, which can be cleared to analyze individual session logs. The database can also be queried directly.

### Glean

Analyzes JSON-RPC endpoints from MITMWeb in real time.

Glean also aggregates information into a database for querying and analysis.

## Citations

- All tools were created with the assistance of Claude and debugged with Claude, ChatGPT, and Gemini.
