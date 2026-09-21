"""
Example: Using Apex SDK with CrewAI-style tool discovery.

This snippet shows how to discover tools/agents by query using the CrewAI adapter.
"""

from integrations.crewai_adapter import crewai_tool_discovery

def main() -> None:
    query = "I need an agent that can purchase 500L jet fuel in Cameroon"
    tools = crewai_tool_discovery(query)
    print(f"Found {len(tools)} candidate tools/agents:")
    for t in tools:
        print(f"- {t['name']}: {t['description']}")

if __name__ == "__main__":
    main()
