# CI & GitHub agents

Agents that run in GitHub Actions and CI

4 entries, sorted by overall score. Snapshot date: 2026-11-10 (America/New_York).

| Name | Repo | Overall | Tier | Safety | Popularity | Usefulness | Rating | Updated | Cost | Description | Safety notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub Agentic Workflows | [github/gh-aw](https://github.com/github/gh-aw) | 89 | A | 100 | 69 | 88 | Safe | 2026-11-10 | Free | GitHub Agentic Workflows: write repository automation in Markdown, and gh-aw compiles it to Actions that run an agent read-only in a sandbox, with writes going through validated 'safe outputs'. A safer pattern for CI agents. Install the gh extension and follow its create guide. | Official; agent jobs are read-only and sandboxed, writes go through validated safe outputs |
| Claude Code Action | [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) | 84 | A | 60 | 64 | 89 | Use with care | 2026-11-10 | Paid | The official GitHub Action that runs Claude Code on PRs and issues: answer @claude mentions, implement changes, review code or run scripted automation, with API, Bedrock, Vertex or Foundry auth. Core for agent-in-CI workflows. Add the workflow YAML and secrets. | Official, but it runs an agent in CI with repo write tokens |
| Codex Action | [openai/codex-action](https://github.com/openai/codex-action) | 74 | B | 60 | 54 | 78 | Use with care | 2026-10-30 | Paid | The official GitHub Action that installs Codex CLI in a workflow behind a secure proxy, for PR review bots and automated fixes. The Codex counterpart to claude-code-action. Add the workflow with an OpenAI API key secret. | Official, but it runs an agent in CI with repo tokens |
| Claude Code Security Review | [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | 68 | C | 60 | 62 | 69 | Use with care | 2026-02-11 | Paid | A GitHub Action that uses Claude Code to review PR diffs for security vulnerabilities and comment on the PR. Easy security coverage for every PR. Add the action to a workflow with an Anthropic API key; run it only on trusted PRs. | Official, but its README says it isn't hardened against prompt injection; run only on trusted PRs |


[Back to all types](README.md) · [Full catalog](../CATALOG.md)
