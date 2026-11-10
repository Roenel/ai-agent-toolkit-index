# Starter stacks

If you are doing one of these jobs, start with these higher-scoring cluster picks. Scores are from the 2026-11-10 snapshot.

## Solo founder shipping agent products

Write code, ship PRs, test in a real browser and evaluate agents in CI.

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Use case | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codex CLI | openai/codex | 96 | 100 | 78 | 94 | Point Codex at a failing test suite in your repo and let it fix the failures inside its sandbox, approving each command before it touches the network. | Freemium |
| GitHub MCP Server | github/github-mcp-server | 97 | 100 | 70 | 97 | Ask your agent to triage this week's open issues, label them and draft a fix PR for the top bug without leaving the chat. | Free |
| Context7 | upstash/context7 | 94 | 100 | 70 | 94 | Building against a library that shipped a breaking release last month, add "use context7" so the agent writes code from the current docs instead of a stale API. | Freemium |
| agent-browser | vercel-labs/agent-browser | 94 | 100 | 76 | 91 | Let a coding agent click through your web app's checkout flow step by step with compact page snapshots, keeping token cost low on long sessions. | Free |
| promptfoo | promptfoo/promptfoo | 94 | 100 | 58 | 92 | Before merging a prompt change, run a YAML test suite in CI that compares old and new prompts and fails the PR if accuracy drops or a jailbreak test passes. | Free |


## Security reviewer

Audit code, review PRs for vulnerabilities, scan agent tooling and red-team model endpoints.

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Use case | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Trail of Bits skills | trailofbits/skills | 87 | 100 | 62 | 83 | Before a release, have the agent hunt for vulnerabilities in a module using Trail of Bits' audit workflows and static-analysis helpers. | Free |
| MCP Scanner | cisco-ai-defense/mcp-scanner | 83 | 100 | 43 | 80 | Before adding a new MCP server to your config, scan its tool descriptions offline for hidden instructions or malicious patterns. | Free |
| garak | NVIDIA/garak | 82 | 100 | 60 | 74 | Point garak at your agent's model endpoint before launch to probe for prompt injection, jailbreaks and data leakage. | Free |
| Claude Code Security Review | anthropics/claude-code-security-review | 68 | 60 | 62 | 69 | On every trusted PR, have Claude comment on injection, auth and secrets issues in the diff before human review. | Paid |


## Agent builder

Build, debug, trace and add memory to your own agents and MCP servers.

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Use case | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Agent SDK (Python) | anthropics/claude-agent-sdk-python | 91 | 100 | 63 | 89 | Build a custom PR-triage agent on the same loop Claude Code uses, with your own tools and permissions. | Paid |
| MCP Inspector | modelcontextprotocol/inspector | 93 | 100 | 62 | 91 | While building your own MCP server, open the Inspector to list its tools, call each one by hand and watch the raw JSON-RPC messages to debug a bad schema. | Free |
| FastMCP | PrefectHQ/fastmcp | 88 | 100 | 64 | 85 | Wrap your product's internal API as an MCP server by decorating a few Python functions, then expose it to any MCP client with auth. | Free |
| Langfuse | langfuse/langfuse | 87 | 100 | 64 | 82 | Trace every LLM call in your agent product to find which step burns the most tokens, then run evals on a dataset before shipping a prompt change. | Freemium |
| Mem0 | mem0ai/mem0 | 80 | 60 | 64 | 85 | Let your product's assistant remember each user's preferences across chats so it stops asking the same questions. | Freemium |


## Data and analytics

Give agents controlled database and file access, and turn documents into Markdown.

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Use case | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MarkItDown | microsoft/markitdown | 89 | 100 | 79 | 83 | Convert a folder of customer PDFs, slide decks and spreadsheets to Markdown so an agent can summarize them without choking on binary formats. | Free |
| MCP Toolbox for Databases | googleapis/mcp-toolbox | 84 | 100 | 61 | 77 | Give an agent read-only, parameterized queries against your production Postgres so it can answer "how many signups last week" without raw SQL access. | Free |
| DuckDB / MotherDuck MCP | motherduckdb/mcp-server-motherduck | 77 | 100 | 44 | 74 | Ask the agent questions about a 2 GB Parquet export and let it answer with DuckDB SQL locally, no warehouse needed. | Free |
| dbt MCP | dbt-labs/dbt-mcp | 70 | 100 | 42 | 62 | Ask the agent which downstream models break if you change a column, using dbt lineage, then run the affected tests. | Free |


## Frontend and design

Build UI from real components and check it in a real browser.

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Use case | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Playwright MCP | microsoft/playwright-mcp | 94 | 100 | 71 | 92 | After your agent changes a signup form, have it open the page, fill the form and confirm the success message actually appears. | Free |
| Vercel agent skills | vercel-labs/agent-skills | 85 | 100 | 74 | 80 | Have the agent review a Next.js app against React best practices and Vercel performance guidance before deploying. | Free |
| Chrome DevTools MCP | ChromeDevTools/chrome-devtools-mcp | 85 | 60 | 72 | 89 | When a page loads slowly, have the agent record a performance trace and read console and network logs to find the blocking request. | Free |
| shadcn/ui | shadcn-ui/ui | 83 | 100 | 70 | 75 | Ask the agent to add a data table and dialog to your React app; it pulls the real shadcn components from the registry rather than inventing markup. | Free |


## DevOps and CI

Run agents safely in CI and let them read cloud and infrastructure state.

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Use case | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub Agentic Workflows | github/gh-aw | 89 | 100 | 69 | 88 | Write a Markdown workflow that has an agent triage every new issue nightly, with any labels or comments going through validated safe outputs instead of direct write access. | Free |
| Docker MCP Gateway | docker/mcp-gateway | 85 | 100 | 57 | 83 | Run third-party MCP servers each in its own container behind one gateway, so a compromised server can't read your home directory. | Free |
| Claude Code Action | anthropics/claude-code-action | 84 | 60 | 64 | 89 | Comment "@claude fix the flaky test" on a PR and let the action push a fix commit to that branch. | Paid |
| Cloudflare MCP servers | cloudflare/mcp-server-cloudflare | 79 | 100 | 56 | 72 | Ask the agent why a Worker started erroring, and let it read the observability logs and bindings on your account. | Freemium |
| Terraform MCP Server | hashicorp/terraform-mcp-server | 76 | 100 | 50 | 69 | While writing Terraform, let the agent look up the exact current arguments for a provider resource instead of guessing. | Free |

