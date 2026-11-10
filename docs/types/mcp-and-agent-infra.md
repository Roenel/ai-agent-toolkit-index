# MCP & agent infra / gateways

Gateways, registries and frameworks for building and running MCP and tools

3 entries, sorted by overall score. Snapshot date: 2026-11-10 (America/New_York).

| Name | Repo | Overall | Tier | Safety | Popularity | Usefulness | Rating | Updated | Cost | Description | Safety notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FastMCP | [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | 88 | A | 100 | 64 | 85 | Safe | 2026-11-10 | Free | FastMCP is the leading Python framework for building MCP servers, clients and apps: declare tools as functions and it handles schemas, transports, auth and deployment. Core if you build MCP servers in Python. Install with `uv add fastmcp`. | Well-known; clean scan |
| Docker MCP Gateway | [docker/mcp-gateway](https://github.com/docker/mcp-gateway) | 85 | A | 100 | 57 | 83 | Safe | 2026-10-26 | Free | Docker's MCP CLI plugin and Gateway: run catalog MCP servers in isolated containers behind one gateway with secrets management. It reduces the risk of running third-party servers. Use via Docker Desktop's MCP Toolkit or the `docker mcp` CLI. | Official; container isolation reduces MCP risk |
| Composio | [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | 75 | B | 60 | 66 | 78 | Use with care | 2026-11-10 | Freemium | Composio's SDKs and CLI give agents 1000+ toolkits (GitHub, Slack, Gmail, Notion and more) with managed OAuth, per-user sessions, triggers and a sandbox, plus adapters for OpenAI Agents, Claude Agent SDK, Vercel AI SDK and LangChain. Useful when your product needs many integrations fast. Install `@composio/core` or `pip install composio` with an API key. | Legit vendor, but it holds OAuth tokens for your connected apps on its cloud |


[Back to all types](README.md) · [Full catalog](../CATALOG.md)
