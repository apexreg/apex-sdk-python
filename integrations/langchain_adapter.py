from __future__ import annotations
from typing import Any, Dict, List
from apexreg_sdk.resolver import resolve

def langchain_tool_resolver(intent: str) -> List[Dict[str, Any]]:
    """
    LangChain-style tool resolver: given an intent, return a list of candidate tools/agents.
    Each item is a dict with basic metadata (name, description, endpoint).
    """
    result = resolve(intent)
    # Adapt ApexRegistry response to LangChain-style tool list
    # Assuming result has a 'matches' list or a single 'agent' object
    matches = result.get("matches", [])
    if not matches and "agent" in result:
        matches = [result["agent"]]
    tools = []
    for m in matches:
        tools.append({
            "name": m.get("ans_address", "").replace("agent://", ""),
            "description": m.get("capabilities_text", ""),
            "endpoint": m.get("endpoint", ""),
        })
    return tools
