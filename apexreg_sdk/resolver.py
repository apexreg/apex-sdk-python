from __future__ import annotations
from .client import ApexClient

_default_client: ApexClient | None = None

def get_client() -> ApexClient:
    global _default_client
    if _default_client is None:
        _default_client = ApexClient()
    return _default_client

def resolve(ans_uri_or_intent: str) -> dict:
    """
    Resolve an agent by ANS address or by intent.
    - If it starts with 'agent://', treat as ANS address.
    - Otherwise, treat as plain-text intent (semantic search).
    """
    client = get_client()
    if ans_uri_or_intent.startswith("agent://"):
        return client.resolve_ans(ans_uri_or_intent)
    else:
        return client.resolve_intent(ans_uri_or_intent)

def search(query: str) -> dict:
    """
    Search agents by plain-text query (semantic search).
    Returns top matching agent(s).
    """
    client = get_client()
    return client.resolve_intent(query)
