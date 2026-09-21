from __future__ import annotations
from typing import Any, Dict, List
from apexreg_sdk.resolver import search

def crewai_tool_discovery(query: str) -> List[Dict[str, Any]]:
    """
    CrewAI-style tool discovery: given a query, return a list of candidate tools/agents.
    Each item is a dict with basic metadata (name, description, endpoint).
    """
    result = search(query)
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
