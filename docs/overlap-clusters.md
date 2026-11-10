# Overlap clusters and duplicates

Entries that do a similar job, with a recommended pick and the reason. Exact `SKILL.md` copies were found by hashing files across read-only clones.

Ratings and recommended picks are observations from this snapshot, not exclusive endorsements.

## Vendor terminal agents

Recommended pick: **Codex CLI** (`openai/codex`). Reference harness: Apache-2.0 source and the safest defaults (OS sandbox on, network off, OTel off). Claude Code has the richest plugin ecosystem but is proprietary and starts in auto mode

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codex CLI (pick) | openai/codex | 96 | 100 | 78 | 94 | Safe |  |
| Qwen Code | QwenLM/qwen-code | 90 | 100 | 67 | 86 | Safe | Fork of Gemini CLI v0.8.2, since diverged |
| Claude Code | anthropics/claude-code | 85 | 60 | 78 | 91 | Use with care |  |
| Gemini CLI | google-gemini/gemini-cli | 78 | 100 | 77 | 66 | Safe |  |
| Grok Build | xai-org/grok-build | 77 | 100 | 69 | 71 | Safe |  |
| Antigravity CLI | google-antigravity/antigravity-cli | 64 | 60 | 52 | 63 | Use with care | Same vendor as Gemini CLI; closed binary |


## Open, model-agnostic terminal agents (OpenCode lineage)

Recommended pick: **OpenCode** (`anomalyco/opencode`). Upstream, MIT, and --auto is opt-in; Kilo CLI is a fork of it, and Goose defaults to auto with no sandbox

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OpenCode (pick) | anomalyco/opencode | 90 | 100 | 77 | 86 | Safe |  |
| Crush | charmbracelet/crush | 89 | 100 | 66 | 86 | Safe |  |
| Kilo Code | Kilo-Org/kilocode | 87 | 100 | 61 | 85 | Safe | Kilo CLI is a declared fork of OpenCode |
| Pi | earendil-works/pi | 87 | 100 | 71 | 82 | Safe |  |
| Aider | Aider-AI/aider | 85 | 100 | 62 | 78 | Safe |  |
| goose | aaif-goose/goose | 76 | 60 | 62 | 77 | Use with care |  |


## Cline family (IDE agents)

Recommended pick: **Cline** (`cline/cline`). Original upstream and actively maintained; Roo Code is archived (shut down 15 May 2026, excluded), Zoo Code is a community fork, Continue's status is unclear. Turn off CLI auto-approve and telemetry

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Kilo Code | Kilo-Org/kilocode | 87 | 100 | 61 | 85 | Safe | Kilo CLI is a declared fork of OpenCode |
| Cline (pick) | cline/cline | 81 | 60 | 66 | 85 | Use with care |  |
| Continue | continuedev/continue | 56 | 60 | 61 | 49 | Use with care | Status unclear after acquisition |


## Google pair: Gemini CLI vs Antigravity

Recommended pick: **Gemini CLI** (`google-gemini/gemini-cli`). Open source (Apache-2.0) with documented defaults; Antigravity has no license and collects interactions data by default

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gemini CLI (pick) | google-gemini/gemini-cli | 78 | 100 | 77 | 66 | Safe |  |
| Antigravity SDK (Python) | google-antigravity/antigravity-sdk-python | 72 | 100 | 54 | 63 | Safe |  |
| Antigravity CLI | google-antigravity/antigravity-cli | 64 | 60 | 52 | 63 | Use with care | Same vendor as Gemini CLI; closed binary |


## Skill format and official reference skills

Recommended pick: **Anthropic Agent Skills** (`anthropics/skills`). Same SKILL.md format everywhere: anthropics/skills for the spec and examples, openai/plugins for Codex packaging; openai/skills is deprecated

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Vercel agent skills | vercel-labs/agent-skills | 85 | 100 | 74 | 80 | Safe |  |
| Anthropic Agent Skills (pick) | anthropics/skills | 83 | 100 | 91 | 77 | Safe |  |
| Knowledge Work Plugins | anthropics/knowledge-work-plugins | 74 | 100 | 72 | 62 | Safe |  |
| OpenAI Plugins (Codex) | openai/plugins | 73 | 60 | 65 | 74 | Use with care |  |
| Cline Skills | cline/skills | 62 | 100 | 31 | 54 | Safe |  |
| Gemini skills | google-gemini/gemini-skills | 61 | 60 | 61 | 58 | Use with care |  |
| Codex Skills Catalog | openai/skills | 59 | 100 | 71 | 40 | Safe | Deprecated by OpenAI: use openai/plugins |
| Amp Official Plugins | ampcode/official-plugins | 57 | 60 | 24 | 57 | Use with care |  |


## Project instructions and specs

Recommended pick: **AGENTS.md** (`agentsmd/agents.md`). Open spec read by Codex, Goose, Cursor and Grok; point Gemini and Claude Code at it with a one-line shim

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AGENTS.md (pick) | agentsmd/agents.md | 78 | 100 | 60 | 72 | Safe |  |
| Trail of Bits Claude Code config | trailofbits/claude-code-config | 63 | 60 | 55 | 62 | Use with care |  |
| Agent Skills Discovery RFC | cloudflare/agent-skills-discovery-rfc | 59 | 100 | 45 | 46 | Safe |  |


## Vendor plugin marketplaces

Recommended pick: **Claude Plugins (official)** (`anthropics/claude-plugins-official`). Claude plugin format is the import source; Cursor's repo already ships a .claude-plugin manifest. None pin SHAs, so vet each plugin

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pstack | cursor/plugins | 87 | 100 | 76 | 83 | Safe |  |
| Claude Plugins (official) (pick) | anthropics/claude-plugins-official | 83 | 100 | 73 | 75 | Safe |  |
| OpenAI Plugins (Codex) | openai/plugins | 73 | 60 | 65 | 74 | Use with care |  |
| Kilo Marketplace | Kilo-Org/kilo-marketplace | 72 | 100 | 36 | 66 | Safe |  |
| Amp Official Plugins | ampcode/official-plugins | 57 | 60 | 24 | 57 | Use with care |  |


## AWS

Recommended pick: **Agent Toolkit for AWS** (`aws/agent-toolkit-for-aws`). Current official bundle; it supersedes awslabs/mcp. Scope IAM read-only first

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Agent Toolkit for AWS (pick) | aws/agent-toolkit-for-aws | 72 | 60 | 64 | 72 | Use with care |  |
| Agent Plugins for AWS | awslabs/agent-plugins | 67 | 60 | 49 | 66 | Use with care |  |
| AWS MCP Servers | awslabs/mcp | 64 | 100 | 60 | 46 | Safe | Superseded by aws/agent-toolkit-for-aws |


## Anthropic learning resources

Recommended pick: **Claude Cookbooks** (`anthropics/claude-cookbooks`). Broader and current: agent patterns, skills, memory and tracing

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Cookbooks (pick) | anthropics/claude-cookbooks | 83 | 100 | 71 | 75 | Safe |  |
| Claude Quickstarts | anthropics/claude-quickstarts | 80 | 100 | 67 | 72 | Safe |  |


## Cross-model review

Recommended pick: **Codex plugin for Claude Code** (`openai/codex-plugin-cc`). Official, one plugin, adds Codex review inside Claude Code; tstack's council does three-model review

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codex plugin for Claude Code (pick) | openai/codex-plugin-cc | 85 | 100 | 73 | 82 | Safe |  |
| tstack | t3dotgg/tstack | 64 | 60 | 79 | 66 | Use with care |  |


## Engineering skill packs (pstack family and peers)

Recommended pick: **Superpowers** (`obra/superpowers`). Most complete spec-to-TDD-to-review loop, works across harnesses, Safe; use pstack via cursor/plugins if you are in Cursor

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Agent Skills (Addy Osmani) | addyosmani/agent-skills | 90 | 100 | 81 | 88 | Safe |  |
| Superpowers (pick) | obra/superpowers | 90 | 100 | 81 | 88 | Safe |  |
| pstack | cursor/plugins | 87 | 100 | 76 | 83 | Safe |  |
| Matt Pocock skills | mattpocock/skills | 84 | 100 | 95 | 80 | Safe |  |
| Agent Skills for Context Engineering | muratcankoylan/Agent-Skills-for-Context-Engineering | 75 | 100 | 59 | 72 | Safe |  |
| gstack | garrytan/gstack | 75 | 60 | 90 | 78 | Use with care |  |
| pstack-claude | michael-denyer/pstack-claude | 69 | 60 | 49 | 75 | Use with care | Unofficial port of pstack with policy forks |
| pstack port (backnotprop) | backnotprop/pstack | 67 | 60 | 55 | 74 | Use with care | Mirror of pstack in cursor/plugins (same SKILL.md files) |
| tstack | t3dotgg/tstack | 64 | 60 | 79 | 66 | Use with care |  |


## Spec-driven and planning workflows

Recommended pick: **Spec Kit** (`github/spec-kit`). Official GitHub, agent-agnostic, lightest path from spec to plan to tasks; ACE-FCA is the best short read on the method

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Spec Kit (pick) | github/spec-kit | 88 | 100 | 78 | 82 | Safe |  |
| OpenSpec | Fission-AI/OpenSpec | 84 | 100 | 65 | 80 | Safe |  |
| Strands Agent SOPs | strands-agents/agent-sop | 80 | 100 | 47 | 77 | Safe |  |
| BMAD Method | bmad-code-org/BMAD-METHOD | 78 | 100 | 64 | 71 | Safe |  |
| Advanced Context Engineering (ACE-FCA) | humanlayer/advanced-context-engineering-for-coding-agents | 72 | 100 | 50 | 66 | Safe |  |
| planning-with-files | OthmanAdi/planning-with-files | 70 | 60 | 62 | 75 | Use with care |  |


## Parallel agents and agent control centers

Recommended pick: **OpenHands** (`OpenHands/OpenHands`). Self-hosted, runs any ACP agent including Codex and Claude Code; Symphony is an OpenAI preview for trusted environments

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OpenHands (pick) | OpenHands/OpenHands | 91 | 100 | 66 | 88 | Safe |  |
| HumanLayer | humanlayer/humanlayer | 79 | 100 | 57 | 74 | Safe |  |
| Claude Squad | smtg-ai/claude-squad | 77 | 100 | 49 | 74 | Safe |  |
| Symphony | openai/symphony | 69 | 60 | 71 | 69 | Use with care |  |
| OpenClaw | openclaw/openclaw | 65 | 40 | 92 | 68 | Use with care |  |
| Amplifier | microsoft/amplifier | 61 | 60 | 59 | 58 | Use with care |  |
| Ruflo (Claude Flow) | ruvnet/ruflo | 59 | 40 | 74 | 62 | Use with care |  |
| Vibe Kanban | BloopAI/vibe-kanban | 54 | 60 | 60 | 49 | Use with care | Sunsetting per README |


## Agent memory

Recommended pick: **Mem0** (`mem0ai/mem0`). Simplest SDK for per-user memory in a product (set MEM0_TELEMETRY=False); Basic Memory or Episodic Memory for your own agents' local notes

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Beads | gastownhall/beads | 86 | 100 | 61 | 83 | Safe |  |
| Cognee | topoteretes/cognee | 83 | 100 | 58 | 78 | Safe |  |
| Basic Memory | basicmachines-co/basic-memory | 81 | 100 | 46 | 82 | Safe |  |
| Mem0 (pick) | mem0ai/mem0 | 80 | 60 | 64 | 85 | Use with care |  |
| Letta Code | letta-ai/letta-code | 77 | 60 | 51 | 83 | Use with care |  |
| Graphiti | getzep/graphiti | 73 | 60 | 60 | 77 | Use with care |  |
| LangMem | langchain-ai/langmem | 73 | 100 | 56 | 65 | Safe |  |
| claude-mem | thedotmack/claude-mem | 71 | 60 | 72 | 72 | Use with care |  |
| Episodic Memory | obra/episodic-memory | 68 | 60 | 44 | 74 | Use with care |  |
| Claude Subconscious | letta-ai/claude-subconscious | 65 | 60 | 50 | 66 | Use with care |  |


## LLM tracing and observability

Recommended pick: **Langfuse** (`langfuse/langfuse`). Most adopted self-hostable tracing and evals, plus official Langfuse skills to wire it in; OpenInference/OpenLLMetry if you stay on plain OTel

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Langfuse (pick) | langfuse/langfuse | 87 | 100 | 64 | 82 | Safe |  |
| Helicone | Helicone/helicone | 84 | 100 | 48 | 80 | Safe |  |
| Logfire SDK | pydantic/logfire | 84 | 100 | 52 | 78 | Safe |  |
| Phoenix | Arize-ai/phoenix | 84 | 100 | 57 | 78 | Safe |  |
| OpenInference | Arize-ai/openinference | 83 | 100 | 46 | 78 | Safe |  |
| OpenLLMetry | traceloop/openllmetry | 83 | 100 | 50 | 78 | Safe |  |
| Laminar | lmnr-ai/lmnr | 82 | 100 | 44 | 83 | Safe |  |
| ccusage | ccusage/ccusage | 81 | 100 | 52 | 77 | Safe |  |
| Opik | comet-ml/opik | 78 | 60 | 58 | 83 | Use with care |  |
| claude-code-transcripts | simonw/claude-code-transcripts | 73 | 100 | 57 | 68 | Safe |  |
| Langfuse skills | langfuse/skills | 71 | 100 | 42 | 65 | Safe |  |
| W&B skills | wandb/skills | 68 | 100 | 32 | 60 | Safe |  |


## Agent frameworks

Recommended pick: **Claude Agent SDK (Python)** (`anthropics/claude-agent-sdk-python`). Builds on the same agent loop you already run in Claude Code; openai-agents-python if you are on OpenAI

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Agent SDK (Python) (pick) | anthropics/claude-agent-sdk-python | 91 | 100 | 63 | 89 | Safe |  |
| FastMCP | PrefectHQ/fastmcp | 88 | 100 | 64 | 85 | Safe |  |
| OpenAI Agents SDK | openai/openai-agents-python | 88 | 100 | 70 | 83 | Safe |  |
| Deep Agents | langchain-ai/deepagents | 83 | 100 | 80 | 77 | Safe |  |
| Microsoft Agent Framework | microsoft/agent-framework | 83 | 100 | 66 | 75 | Safe |  |
| DSPy | stanfordnlp/dspy | 82 | 100 | 62 | 74 | Safe |  |
| Claude Quickstarts | anthropics/claude-quickstarts | 80 | 100 | 67 | 72 | Safe |  |
| GPT Researcher | assafelovic/gpt-researcher | 77 | 100 | 62 | 69 | Safe |  |
| Docker Agent | docker/docker-agent | 76 | 60 | 63 | 78 | Use with care |  |
| smolagents | huggingface/smolagents | 76 | 60 | 73 | 77 | Use with care |  |


## Skill installers and skill tooling

Recommended pick: **Agent Package Manager** (`microsoft/apm`). Lockfile and manifest for skills plus MCP; upskill to measure whether a skill helps

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Agent Package Manager (pick) | microsoft/apm | 84 | 100 | 60 | 78 | Safe |  |
| skills CLI (npx skills) | vercel-labs/skills | 84 | 60 | 75 | 89 | Use with care |  |
| upskill | huggingface/upskill | 76 | 100 | 55 | 71 | Safe |  |


## Security review skills

Recommended pick: **Trail of Bits skills** (`trailofbits/skills`). Deepest audit expertise; Snyk recipes if you already use Snyk

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Trail of Bits skills (pick) | trailofbits/skills | 87 | 100 | 62 | 83 | Safe |  |
| security-audit | cloudflare/security-audit-skill | 77 | 100 | 88 | 69 | Safe |  |
| Snyk Studio Recipes | snyk/studio-recipes | 76 | 100 | 32 | 72 | Safe |  |
| Sentry skills | getsentry/skills | 72 | 100 | 51 | 63 | Safe |  |


## MCP and skill scanners

Recommended pick: **MCP Scanner** (`cisco-ai-defense/mcp-scanner`). Fully local static plus YARA scanning with no account; Snyk's sends data to its API

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP Scanner (pick) | cisco-ai-defense/mcp-scanner | 83 | 100 | 43 | 80 | Safe |  |
| Snyk Agent Scan | snyk/agent-scan | 77 | 60 | 50 | 83 | Use with care |  |
| AI-Infra-Guard | Tencent/AI-Infra-Guard | 66 | 60 | 58 | 65 | Use with care |  |


## LLM red-teaming and guardrails

Recommended pick: **garak** (`NVIDIA/garak`). Broadest out-of-the-box probe set for agent endpoints; NeMo Guardrails for runtime blocking

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| garak (pick) | NVIDIA/garak | 82 | 100 | 60 | 74 | Safe |  |
| NeMo Guardrails | NVIDIA-NeMo/Guardrails | 78 | 100 | 53 | 68 | Safe |  |
| PyRIT | microsoft/PyRIT | 77 | 100 | 59 | 68 | Safe |  |
| Purple Llama | meta-llama/PurpleLlama | 68 | 100 | 54 | 55 | Safe |  |


## Eval frameworks

Recommended pick: **promptfoo** (`promptfoo/promptfoo`). YAML evals plus red-team in CI with no code; DeepEval if you want pytest-style

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| promptfoo (pick) | promptfoo/promptfoo | 94 | 100 | 58 | 92 | Safe |  |
| MCP Inspector | modelcontextprotocol/inspector | 93 | 100 | 62 | 91 | Safe |  |
| DeepEval | confident-ai/deepeval | 85 | 100 | 56 | 82 | Safe |  |
| Inspect | UKGovernmentBEIS/inspect_ai | 82 | 100 | 46 | 75 | Safe |  |


## Browser automation for agents

Recommended pick: **agent-browser** (`vercel-labs/agent-browser`). Cheapest tokens per step and runs as CLI or MCP; Playwright MCP is the safe default for MCP-only clients

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| agent-browser (pick) | vercel-labs/agent-browser | 94 | 100 | 76 | 91 | Safe |  |
| Playwright MCP | microsoft/playwright-mcp | 94 | 100 | 71 | 92 | Safe |  |
| Playwright CLI | microsoft/playwright-cli | 88 | 100 | 63 | 86 | Safe |  |
| Stagehand | browserbase/stagehand | 86 | 100 | 65 | 85 | Safe |  |
| Chrome DevTools MCP | ChromeDevTools/chrome-devtools-mcp | 85 | 60 | 72 | 89 | Use with care |  |
| Browser Use | browser-use/browser-use | 80 | 60 | 75 | 85 | Use with care |  |
| Cua | trycua/cua | 78 | 60 | 67 | 83 | Use with care |  |
| Browserbase skills | browserbase/skills | 64 | 60 | 56 | 66 | Use with care |  |


## GitHub and CI agents

Recommended pick: **GitHub Agentic Workflows** (`github/gh-aw`). Official GitHub, sandboxed safe-outputs model, agent-agnostic

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub Agentic Workflows (pick) | github/gh-aw | 89 | 100 | 69 | 88 | Safe |  |
| Claude Code Action | anthropics/claude-code-action | 84 | 60 | 64 | 89 | Use with care |  |
| Codex Action | openai/codex-action | 74 | 60 | 54 | 78 | Use with care |  |
| Claude Code Security Review | anthropics/claude-code-security-review | 68 | 60 | 62 | 69 | Use with care |  |


## Sandboxes for agent code

Recommended pick: **E2B** (`e2b-dev/E2B`). Mature, SDK-first, fast VMs; container-use if you want local git-branch isolation

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Docker MCP Gateway | docker/mcp-gateway | 85 | 100 | 57 | 83 | Safe |  |
| E2B (pick) | e2b-dev/E2B | 85 | 100 | 66 | 83 | Safe |  |
| Cloudflare Sandbox SDK | cloudflare/sandbox-sdk | 80 | 100 | 49 | 74 | Safe |  |
| Container Use | dagger/container-use | 79 | 100 | 55 | 74 | Safe |  |


## Awesome lists and directories

Recommended pick: **Claude Plugins (official)** (`anthropics/claude-plugins-official`). Vendor-curated; community lists are for discovery only, and ClawHub is rated Avoid

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Plugins (official) (pick) | anthropics/claude-plugins-official | 83 | 100 | 73 | 75 | Safe |  |
| MCP Registry | modelcontextprotocol/registry | 78 | 100 | 61 | 69 | Safe |  |
| Claude Code Templates | davila7/claude-code-templates | 70 | 60 | 68 | 72 | Use with care | Re-bundles skills from Anthropic, OpenAI and Composio lists |
| Awesome Copilot | github/awesome-copilot | 66 | 60 | 71 | 62 | Use with care |  |
| Awesome MCP Servers | punkpeye/awesome-mcp-servers | 62 | 60 | 68 | 57 | Use with care |  |
| Awesome Agent Skills | VoltAgent/awesome-agent-skills | 60 | 60 | 66 | 55 | Use with care |  |
| Awesome Claude Code | hesreallyhim/awesome-claude-code | 59 | 60 | 65 | 58 | Use with care |  |
| Awesome Claude Skills (Composio) | ComposioHQ/awesome-claude-skills | 58 | 60 | 73 | 52 | Use with care | Re-bundles copies of official Anthropic skills |
| Agentic Awesome Skills | sickn33/agentic-awesome-skills | 57 | 40 | 65 | 60 | Use with care |  |
| Awesome Claude Skills (travisvn) | travisvn/awesome-claude-skills | 47 | 60 | 57 | 43 | Use with care |  |
| ClawHub community skills | openclaw/clawhub | 20 | 0 | 68 | 49 | Avoid |  |


## Docs and web to Markdown

Recommended pick: **MarkItDown** (`microsoft/markitdown`). Lightest, broad format support; Docling for hard PDFs

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MarkItDown (pick) | microsoft/markitdown | 89 | 100 | 79 | 83 | Safe |  |
| Docling | docling-project/docling | 83 | 100 | 65 | 75 | Safe |  |
| Defuddle | kepano/defuddle | 79 | 100 | 64 | 72 | Safe |  |
| Firecrawl MCP | firecrawl/firecrawl-mcp-server | 74 | 60 | 62 | 78 | Use with care |  |


## Postgres, Supabase and Neon

Recommended pick: **Supabase agent skills** (`supabase/agent-skills`). Read-only best-practice skills, no DB access needed

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Supabase agent skills (pick) | supabase/agent-skills | 74 | 100 | 68 | 66 | Safe |  |
| Supabase MCP | supabase/mcp | 69 | 60 | 58 | 71 | Use with care |  |
| Neon skills | neondatabase/agent-skills | 66 | 100 | 38 | 58 | Safe |  |


## Microsoft and Azure

Recommended pick: **Microsoft MCP catalog** (`microsoft/mcp`). Official servers; the skill packs only matter if you use Azure

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Microsoft MCP catalog (pick) | microsoft/mcp | 75 | 100 | 59 | 65 | Safe |  |
| Microsoft Skills | microsoft/skills | 74 | 100 | 59 | 65 | Safe |  |
| Azure Skills plugin | microsoft/azure-skills | 62 | 60 | 56 | 58 | Use with care | Shares 54 identical SKILL.md files with microsoft/skills |


## n8n

Recommended pick: **n8n-MCP** (`czlonkowski/n8n-mcp`). Same author; the MCP server carries the node docs, skills complement it

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| n8n-MCP (pick) | czlonkowski/n8n-mcp | 74 | 100 | 60 | 68 | Safe |  |
| n8n Skills | czlonkowski/n8n-skills | 62 | 100 | 54 | 51 | Safe |  |


## Design and UI taste skills

Recommended pick: **shadcn/ui** (`shadcn-ui/ui`). Real components and registry; the two skills have unusual star growth

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| shadcn/ui (pick) | shadcn-ui/ui | 83 | 100 | 70 | 75 | Safe |  |
| UI/UX Pro Max | nextlevelbuilder/ui-ux-pro-max-skill | 70 | 60 | 61 | 75 | Use with care |  |
| Taste Skill | Leonxlnx/taste-skill | 67 | 60 | 75 | 71 | Use with care |  |


## Database and analytics MCP servers

Recommended pick: **MCP Toolbox for Databases** (`googleapis/mcp-toolbox`). Official Google, one server for Postgres, BigQuery, Spanner and more

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP Toolbox for Databases (pick) | googleapis/mcp-toolbox | 84 | 100 | 61 | 77 | Safe |  |
| DuckDB / MotherDuck MCP | motherduckdb/mcp-server-motherduck | 77 | 100 | 44 | 74 | Safe |  |
| ClickHouse MCP | ClickHouse/mcp-clickhouse | 72 | 100 | 48 | 65 | Safe |  |
| dbt MCP | dbt-labs/dbt-mcp | 70 | 100 | 42 | 62 | Safe |  |


## Cloud and infra MCP servers

Recommended pick: **Cloudflare MCP servers** (`cloudflare/mcp-server-cloudflare`). Official remote servers with OAuth, nothing to host; awslabs/mcp is superseded

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cloudflare MCP servers (pick) | cloudflare/mcp-server-cloudflare | 79 | 100 | 56 | 72 | Safe |  |
| Grafana MCP | grafana/mcp-grafana | 79 | 100 | 57 | 72 | Safe |  |
| Terraform MCP Server | hashicorp/terraform-mcp-server | 76 | 100 | 50 | 69 | Safe |  |
| Kubernetes MCP Server | containers/kubernetes-mcp-server | 69 | 60 | 50 | 71 | Use with care |  |
| AWS MCP Servers | awslabs/mcp | 64 | 100 | 60 | 46 | Safe | Superseded by aws/agent-toolkit-for-aws |


## Work-app MCP servers

Recommended pick: **GitHub MCP Server** (`github/github-mcp-server`). Official and central to a many-PR workflow; Notion's local server is unmaintained (use its hosted MCP)

| Entry | Repo | Overall | Safety | Popularity | Usefulness | Rating | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub MCP Server (pick) | github/github-mcp-server | 97 | 100 | 70 | 97 | Safe |  |
| Composio | ComposioHQ/composio | 75 | 60 | 66 | 78 | Use with care |  |
| Atlassian MCP Server | atlassian/atlassian-mcp-server | 62 | 100 | 45 | 49 | Safe |  |
| Notion MCP Server | makenotion/notion-mcp-server | 58 | 100 | 73 | 42 | Safe | Unmaintained; Notion recommends its hosted MCP |


## Exact duplicates, mirrors and forks

Identical `SKILL.md` counts come from hashing files over 300 bytes. A zero means a documented fork or successor, not identical files.

| Repo | Overlaps with | Identical SKILL.md files | What it means |
| --- | --- | --- | --- |
| cursor/plugins (pstack) | backnotprop/pstack | 43 | Mirror: same pstack skills, kept in sync for non-Cursor users. Install one. |
| microsoft/skills | microsoft/azure-skills | 54 | Near-duplicate: the Azure pack repackages Microsoft's skills. Pick by whether you need Azure deploy skills. |
| cursor/plugins (pstack) | michael-denyer/pstack-claude | 5 | Port: a few pstack skills verbatim, the rest adapted with policy forks. |
| davila7/claude-code-templates | ComposioHQ/awesome-claude-skills | 17 | Directories copying each other's bundled skills. |
| davila7/claude-code-templates | anthropics/skills | 12 | Directory re-bundles official Anthropic skills; get them from the source. |
| ComposioHQ/awesome-claude-skills | anthropics/skills | 5 | Same: copies of official skills inside a list. |
| davila7/claude-code-templates | openai/skills | 3 | Copies of OpenAI's (now deprecated) skills. |
| snyk/agent-scan | anthropics/skills | 5 | Test fixtures only (skills it scans), not a competing pack. |
| czlonkowski/n8n-mcp | czlonkowski/n8n-skills | 2 | Same author ships the skills in both repos; complementary. |
| Kilo-Org/kilocode | anomalyco/opencode | 1 | Fork: Kilo CLI is built from OpenCode. |
| QwenLM/qwen-code | google-gemini/gemini-cli | — | Fork of Gemini CLI v0.8.2; stopped syncing upstream. |
| aws/agent-toolkit-for-aws | awslabs/mcp | — | Successor: the toolkit supersedes awslabs/mcp. |
| openai/plugins | openai/skills | — | Successor: openai/skills is deprecated in favor of openai/plugins. |
| letta-ai/letta-code | letta-ai/letta | — | letta-ai/letta is now a pointer repo; Letta Code replaces it (old entry removed). |
| nizos/probity | nizos/tdd-guard | — | Same author; Probity supersedes TDD Guard. |


Roo Code (archived 15 May 2026) and its community fork Zoo Code are not listed; Cline is the pick for that family.
