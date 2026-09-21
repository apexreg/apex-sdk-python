# Apex SDK (Python) — Resolve, search, and register AI agents

Minimal Python SDK for ApexRegistry. Use it to resolve agent addresses, search by intent, and register new agents.
Includes LangChain and CrewAI integration examples.

## Install
```bash
pip install apexreg-sdk
```
(For now, install from source by cloning this repo.)

## Usage
```python
from apexreg_sdk import resolve, search

# Resolve by ANS address
agent = resolve("agent://billing.apexreg.org/cardiology")

# Resolve by intent (semantic search)
agent = search("I need an agent that can purchase 500L jet fuel in Cameroon")
```

## Integrations
- LangChain: use the SDK as a tool resolver to discover agents/tools by intent.
- CrewAI: use the SDK to populate tool lists for agents dynamically.

See examples/ for ready-to-run snippets.

## License
Apache‑2.0
