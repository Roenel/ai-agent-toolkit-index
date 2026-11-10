# Sandboxes & runtimes

Isolated environments where agent code runs

3 entries, sorted by overall score. Snapshot date: 2026-11-10 (America/New_York).

| Name | Repo | Overall | Tier | Safety | Popularity | Usefulness | Rating | Updated | Cost | Description | Safety notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E2B | [e2b-dev/E2B](https://github.com/e2b-dev/E2B) | 85 | A | 100 | 66 | 83 | Safe | 2026-11-09 | Freemium | E2B gives agents isolated cloud sandboxes (Firecracker microVMs) to run generated code, shell commands and even full desktops, controlled from JS or Python SDKs. It is a common back end for code interpreters and computer-use demos. Install with `npm i e2b` or `pip install e2b` and set E2B_API_KEY. | Well-known; code runs in E2B's cloud VMs, not your machine; needs an API key |
| Cloudflare Sandbox SDK | [cloudflare/sandbox-sdk](https://github.com/cloudflare/sandbox-sdk) | 80 | A | 100 | 49 | 74 | Safe | 2026-11-02 | Cloud account | The Sandbox SDK runs untrusted or generated code in a Linux container owned by one user, task or session, driven from a Cloudflare Worker, with file streaming, S3 mounts and egress control. Good for hosting agent code execution at the edge. Install `@cloudflare/sandbox` in a Workers project. | Official; your Worker controls network egress and credentials |
| Container Use | [dagger/container-use](https://github.com/dagger/container-use) | 79 | B | 100 | 55 | 74 | Safe | 2026-08-12 | Free | Container Use is an MCP server and CLI that gives each coding agent its own container and git branch, so several agents can work in parallel without clobbering your checkout; you review and merge their branches. Works with Claude Code, Cursor and other MCP agents. Install with `brew install dagger/tap/container-use`. | Well-known (Dagger, founded by Docker's creator); agents work in containers |


[Back to all types](README.md) · [Full catalog](../CATALOG.md)
