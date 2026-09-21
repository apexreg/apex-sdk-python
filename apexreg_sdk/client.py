from __future__ import annotations
import os
import httpx

APEXREG_API_URL = os.environ.get("APEXREG_API_URL", "https://api.apexreg.org")

class ApexClient:
    def __init__(self, base_url: str | None = None) -> None:
        self.base_url = base_url or APEXREG_API_URL

    def resolve_ans(self, ans_uri: str) -> dict:
        """
        Resolve an agent by its ANS address (e.g. agent://billing.apexreg.org/cardiology).
        """
        url = f"{self.base_url}/v1/resolve"
        resp = httpx.get(url, params={"ans": ans_uri})
        resp.raise_for_status()
        return resp.json()

    def resolve_intent(self, intent: str) -> dict:
        """
        Resolve an agent by plain-text intent (semantic search).
        """
        url = f"{self.base_url}/v1/search"
        resp = httpx.post(url, json={"query": intent})
        resp.raise_for_status()
        return resp.json()

    def register_agent(self, card: dict) -> dict:
        """
        Register a new agent card (apex-agent-card.json style).
        """
        url = f"{self.base_url}/v1/register"
        resp = httpx.post(url, json=card)
        resp.raise_for_status()
        return resp.json()
