"""
Example: Using Apex SDK with LangChain-style tool resolution.

This snippet shows how to discover tools/agents by intent using the LangChain adapter.
"""

from integrations.langchain_adapter import langchain_tool_resolver

def main() -> None:
    intent = "I need an agent that can purchase 500L jet fuel in Cameroon"
    tools = langchain_tool_resolver(intent)
    print(f"Found {len(tools)} candidate tools/agents:")
    for t in tools:
        print(f"- {t['name']}: {t['description']}")

if __name__ == "__main__":
    main()
