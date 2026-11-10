> Edited for publication: internal researcher names were replaced with a neutral contributor credit. This is a point-in-time, read-only review of public repositories and vendor documentation (10 Nov 2026, America/New_York), not a security audit or a guarantee.

# Official-source additions

Contributor research notes for the AI Skill Library.

Summary: 37 new entries (none in the 129-entry canvas or the existing catalog skip list), split A) official company skill packs/workflows, B) memory & context, C) observability/tracing, D) methodologies, prompt and harness libraries. All repo URLs checked via GitHub API + HTTP 200 on 2026-11-10 ~08:10 ET; stars/license/last-commit straight from the GitHub API. Read-only: README/SKILL/install files fetched as raw text only; nothing installed or run.

Legend: Org 'verified' = GitHub verified-domain badge (`is_verified` from GitHub API). X links: only listed when found via X search; most official launch posts could not be located with the X archive search, so they're marked 'none verified' rather than guessed.


Caveat: org identity/homepage come from the GitHub API. A few extra background details come from prior knowledge and were NOT re-checked this pass, so treat them as UNVERIFIED: Jesse Vincent = Request Tracker creator, Simon Willison = Django co-creator, DSPy = Omar Khattab et al., Agent Framework = successor to SK/AutoGen, AGENTS.md co-announced by OpenAI/Google/Cursor/Factory, Pydantic Logfire backend closed-source, Traceloop SDK cloud default.

## A. Priority: official company skill packs & workflows

### Agent Toolkit for AWS
- Repo: https://github.com/aws/agent-toolkit-for-aws (HTTP 200; ★ 3,450 per API)
- Author: Amazon Web Services (GitHub org `aws`, verified domain; amazon.com/aws).
- What it does: Official AWS-supported MCP servers, skills and plugins (aws-core, data-analytics, devsecops…) for Claude Code, Codex, Cursor and others to build/deploy/operate on AWS.
- Category: A. Official skill pack
- Last commit: 2026-11-09 | License: Apache-2.0
- Safety: Use with care: skills drive real AWS API calls with your credentials; `signing-in-to-aws` skill tells the agent to offer to run `aws login` itself; one skill suggests the astral.sh uv `curl|sh` installer. Scope IAM to read-only first.
- X post: https://x.com/awsdevelopers/status/2110475740097520075 (official @awsdevelopers post about the toolkit; link target not expanded)

### Agent Plugins for AWS
- Repo: https://github.com/awslabs/agent-plugins (HTTP 200; ★ 938 per API)
- Author: AWS Labs (org `awslabs`, verified; amazon.com/aws).
- What it does: Plugins/skills that teach coding agents to architect, deploy and operate on AWS (serverless, Amplify, Location, Transform…).
- Category: A. Official skill pack
- Last commit: 2026-11-10 | License: Apache-2.0
- Safety: Use with care: aws-transform skill instructs `curl -fsSL https://transform-cli.awsstatic.com/install.sh | bash` (AWS-hosted); needs AWS creds.
- X post: none verified

### Strands Agent SOPs
- Repo: https://github.com/strands-agents/agent-sop (HTTP 200; ★ 1,217 per API)
- Author: AWS / Strands Agents team (org unverified on GitHub, but repo homepage is the AWS Open Source Blog post by James Hood & Nicholas Clegg, 2025-11-20: https://aws.amazon.com/blogs/opensource/introducing-strands-agent-sops-natural-language-workflows-for-ai-agents/).
- What it does: Markdown 'Standard Operating Procedures' with RFC-2119 MUST/SHOULD steps, parameters and resumable progress; usable as system prompts, via MCP server, or exported as Agent Skills.
- Category: A. Official workflow
- Last commit: 2026-10-25 | License: Apache-2.0
- Safety: Safe: docs + small Python package; scan clean (no curl|bash, no telemetry hits).
- X post: none verified (AWS Open Source LinkedIn post exists)

### Agents CLI (ADK)
- Repo: https://github.com/google/agents-cli (HTTP 200; ★ 6,331 per API)
- Author: Google (org `google`, verified; opensource.google).
- What it does: CLI plus skills that turn Claude Code/Codex/Gemini CLI into an expert at building, evaluating and deploying Agent Development Kit (ADK) agents on Google Cloud.
- Category: A. Official skill pack
- Last commit: 2026-11-04 | License: Apache-2.0
- Safety: Use with care: usage telemetry ON by default (one signal per command); opt out with `AGENTS_CLI_TELEMETRY=0`.
- X post: none verified

### Gemini skills
- Repo: https://github.com/google-gemini/gemini-skills (HTTP 200; ★ 4,445 per API)
- Author: google-gemini org (unverified badge; homepage ai.google.dev, Google's Gemini API docs).
- What it does: Agent Skills for the Gemini API/SDK and model/agent interactions.
- Category: A. Official skill pack
- Last commit: 2026-11-05 | License: Apache-2.0
- Safety: Use with care: gemini-api-cli skill instructs a `curl … raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash` installer; reads GEMINI API key from env.
- X post: none verified

### Firebase agent skills
- Repo: https://github.com/firebase/agent-skills (HTTP 200; ★ 508 per API)
- Author: Firebase (org `firebase`, unverified badge; homepage firebase.google.com).
- What it does: Agent Skills for Firebase (Auth, Firestore, Hosting, Analytics instrumentation, etc.).
- Category: A. Official skill pack
- Last commit: 2026-11-09 | License: Apache-2.0
- Safety: Safe: docs-only skills; 'analytics' hits are Firebase Analytics how-tos, not telemetry.
- X post: none verified

### HashiCorp agent skills
- Repo: https://github.com/hashicorp/agent-skills (HTTP 200; ★ 925 per API)
- Author: HashiCorp (org verified; hashicorp.com).
- What it does: Agent Skills and Claude Code plugins for Terraform, Vault, Packer and other HashiCorp products.
- Category: A. Official skill pack
- Last commit: 2026-11-04 | License: MPL-2.0
- Safety: Safe: docs-only; credential mentions are Terraform/Vault token how-tos. Note MPL-2.0.
- X post: none verified

### OpenAI Plugins (Codex)
- Repo: https://github.com/openai/plugins (HTTP 200; ★ 7,862 per API)
- Author: OpenAI (org verified; openai.com).
- What it does: OpenAI's curated plugin catalog for Codex (skills + MCP), including many partner-built plugins (Cloudflare, Boltz, macOS app building…).
- Category: A. Official skill pack
- Last commit: 2026-11-06 | License: none
- Safety: Use with care: large mixed catalog; some partner plugins tell the agent to run third-party `curl|sh`/`irm|iex` installers (e.g. boltz-api-cli). Vet each plugin. No LICENSE file.
- X post: none verified

### Codex plugin for Claude Code
- Repo: https://github.com/openai/codex-plugin-cc (HTTP 200; ★ 35,026 per API)
- Author: OpenAI (org verified).
- What it does: Claude Code plugin adding /codex:review, /codex:adversarial-review and /codex:rescue to delegate or cross-review work with Codex.
- Category: A. Official workflow
- Last commit: 2026-07-08 | License: Apache-2.0
- Safety: Safe: scan clean; sends code to OpenAI under your ChatGPT/API account.
- X post: none verified

### Symphony
- Repo: https://github.com/openai/symphony (HTTP 200; ★ 27,997 per API)
- Author: OpenAI (org verified).
- What it does: Watches a Linear board and spawns isolated autonomous coding-agent runs that return proof of work (CI, PRs); OpenAI's 'harness engineering' follow-on.
- Category: A. Official workflow
- Last commit: 2026-09-15 | License: Apache-2.0
- Safety: Use with care: README says 'engineering preview for trusted environments'; needs LINEAR_API_KEY; autonomous agents act on repos.
- X post: none verified

### Claude for Financial Services plugins
- Repo: https://github.com/anthropics/financial-services (HTTP 200; ★ 41,196 per API)
- Author: Anthropic (org verified; anthropic.com).
- What it does: Claude Code plugins, skills and managed-agent cookbooks for finance (IC memos, earnings review, GL reconciliation) plus partner MCPs (LSEG, PitchBook, FactSet…).
- Category: A. Official skill pack
- Last commit: 2026-10-28 | License: Apache-2.0
- Safety: Use with care: partner plugins connect to external financial-data MCP endpoints; deploy scripts need ANTHROPIC_API_KEY. Scan otherwise clean.
- X post: none verified

### upskill
- Repo: https://github.com/huggingface/upskill (HTTP 200; ★ 764 per API)
- Author: Hugging Face (org verified; huggingface.co).
- What it does: Generates and evaluates Agent Skills for Claude Code, OpenCode, Codex etc.: create a skill, test it against models, measure lift.
- Category: A. Official skill tooling
- Last commit: 2026-10-14 | License: Apache-2.0
- Safety: Safe: pip/uv install; needs model API keys (env only). Scan clean.
- X post: none verified

### Docker Agent (ex-cagent)
- Repo: https://github.com/docker/docker-agent (HTTP 200; ★ 4,671 per API)
- Author: Docker (org verified; docker.com). Repo renamed from docker/cagent.
- What it does: Declarative YAML agent builder/runtime with multi-agent teams, MCP tools and sandboxing, from Docker Engineering.
- Category: A. Official agent builder
- Last commit: 2026-11-10 | License: Apache-2.0
- Safety: Use with care: collects usage telemetry by default (documented, can be disabled); has a `--yolo`/autoApprove mode.
- X post: none verified

### Trail of Bits Claude Code config
- Repo: https://github.com/trailofbits/claude-code-config (HTTP 200; ★ 2,148 per API)
- Author: Trail of Bits (org verified; trailofbits.com), top security research firm.
- What it does: Opinionated Claude Code defaults: permission deny-rules for ~/.ssh, cloud creds, sandboxing, hooks, local-model setup, workflows.
- Category: A. Official workflow
- Last commit: 2026-08-24 | License: none
- Safety: Use with care: strong credential deny rules, BUT recommends a `claude-yolo` alias (--dangerously-skip-permissions) inside its sandbox and rustup/LM Studio curl|sh installers. No LICENSE.
- X post: none verified

### Snyk Studio Recipes
- Repo: https://github.com/snyk/studio-recipes (HTTP 200; ★ 69 per API)
- Author: Snyk (org verified; snyk.io).
- What it does: Drop-in rules, commands, hooks and skills that embed Snyk scanning/fix loops into AI coding assistants (snyk-fix, drift-detector…).
- Category: A. Official security workflow
- Last commit: 2026-10-20 | License: Apache-2.0
- Safety: Safe: docs/hooks; drift-detector skill prints cloud access tokens (gcloud print-access-token) to run checks; needs Snyk auth. Low stars (official).
- X post: none verified

### Elastic agent skills
- Repo: https://github.com/elastic/agent-skills (HTTP 200; ★ 605 per API)
- Author: Elastic (org `elastic`, unverified badge; elastic.co).
- What it does: Official Elastic skills for Elasticsearch/Kibana/observability/security tasks.
- Category: A. Official skill pack
- Last commit: 2026-10-29 | License: Apache-2.0
- Safety: Safe: docs; API-key usage is Elastic auth how-to.
- X post: none verified


## B. Memory & context

### Mem0
- Repo: https://github.com/mem0ai/mem0 (HTTP 200; ★ 68,747 per API)
- Author: Mem0 (org `mem0ai`, unverified badge; mem0.ai; YC-backed).
- What it does: Drop-in memory layer for agents (extract, store, retrieve user/agent memories) with OpenMemory MCP.
- Category: B. Memory
- Last commit: 2026-11-06 | License: Apache-2.0
- Safety: Use with care: PostHog telemetry ON by default (`MEM0_TELEMETRY`, host us.i.posthog.com) in SDK and CLI; set MEM0_TELEMETRY=False.
- X post: none verified

### Letta Code
- Repo: https://github.com/letta-ai/letta-code (HTTP 200; ★ 3,812 per API)
- Author: Letta (org verified; letta.com), the MemGPT research team. (letta-ai/letta now points here.)
- What it does: Stateful agent harness/TUI whose agents keep long-term memory and self-improve across sessions.
- Category: B. Memory
- Last commit: 2026-11-10 | License: Apache-2.0
- Safety: Use with care: defaults to Letta cloud (api.letta.com) unless self-hosted; needs LETTA_API_KEY.
- X post: none verified

### Claude Subconscious
- Repo: https://github.com/letta-ai/claude-subconscious (HTTP 200; ★ 2,910 per API)
- Author: Letta (org verified).
- What it does: Hooks that send each Claude Code transcript to a Letta agent, which reads your codebase/web and 'whispers back' memory before the next prompt.
- Category: B. Memory
- Last commit: 2026-09-10 | License: MIT
- Safety: Use with care: ships every session transcript to Letta cloud by default (LETTA_BASE_URL to self-host); background agent reads files and searches web.
- X post: none verified

### Graphiti
- Repo: https://github.com/getzep/graphiti (HTTP 200; ★ 32,708 per API)
- Author: Zep (org verified; getzep.com).
- What it does: Temporal knowledge-graph engine for agent memory (episodes→entities/edges with validity times), plus MCP server.
- Category: B. Memory
- Last commit: 2026-11-09 | License: Apache-2.0
- Safety: Use with care: anonymous telemetry on by default (UUID in ~/.cache/graphiti), opt-out via GRAPHITI_TELEMETRY_ENABLED=false.
- X post: none verified

### Episodic Memory
- Repo: https://github.com/obra/episodic-memory (HTTP 200; ★ 499 per API)
- Author: Jesse Vincent (@obra; fsck.com), creator of Request Tracker and of Superpowers (already in library).
- What it does: Indexes past Claude Code conversations locally (SQLite + vectors) so agents can semantically search prior sessions.
- Category: B. Memory
- Last commit: 2026-09-10 | License: MIT
- Safety: Use with care: npm postinstall runs a local node script (rebuilds native sqlite binding); summarization can bill ANTHROPIC_API_KEY if set.
- X post: none verified

### LangMem
- Repo: https://github.com/langchain-ai/langmem (HTTP 200; ★ 1,759 per API)
- Author: LangChain (org `langchain-ai`, unverified badge; langchain.com).
- What it does: Library for agent long-term memory: hot-path memory tools, background extraction and prompt optimization, LangGraph-native.
- Category: B. Memory
- Last commit: 2026-11-03 | License: MIT
- Safety: Safe: scan clean.
- X post: none verified


## C. Observability / tracing / evals-adjacent

### Langfuse skills
- Repo: https://github.com/langfuse/skills (HTTP 200; ★ 338 per API)
- Author: Langfuse (org verified; langfuse.com). Library already has langfuse/langfuse, not this repo.
- What it does: Agent Skills for instrumenting tracing, prompt management and evals with Langfuse.
- Category: C. Observability skills
- Last commit: 2026-11-07 | License: MIT
- Safety: Safe: docs; needs Langfuse keys via env.
- X post: none verified

### W&B skills
- Repo: https://github.com/wandb/skills (HTTP 200; ★ 74 per API)
- Author: Weights & Biases (org verified; wandb.ai).
- What it does: Official Agent Skills for W&B Models and Weave tracing/evals.
- Category: C. Observability skills
- Last commit: 2026-11-06 | License: Apache-2.0
- Safety: Safe: ships an install.sh that only copies skills and echoes WANDB_API_KEY instructions; 'yolo' hits are YOLOv5 model names.
- X post: none verified

### Opik
- Repo: https://github.com/comet-ml/opik (HTTP 200; ★ 23,300 per API)
- Author: Comet (org verified; comet.com).
- What it does: Open-source tracing, evals and monitoring for LLM apps, RAG and agents; self-host or cloud.
- Category: C. Observability / evals
- Last commit: 2026-11-10 | License: Apache-2.0
- Safety: Use with care: has an anonymous usage-report setting (OPIK_USAGE_REPORT_ENABLED) — disable if self-hosting privately.
- X post: none verified

### OpenLLMetry
- Repo: https://github.com/traceloop/openllmetry (HTTP 200; ★ 7,529 per API)
- Author: Traceloop, now 'traceloop from ServiceNow' (org verified; traceloop.com).
- What it does: OpenTelemetry instrumentations for LLM providers, vector DBs and agent frameworks; export to any OTel backend.
- Category: C. Observability
- Last commit: 2026-11-05 | License: Apache-2.0
- Safety: Safe: OTel exporter only sends where you point it; Traceloop SDK defaults to its cloud if key set.
- X post: none verified

### Logfire SDK
- Repo: https://github.com/pydantic/logfire (HTTP 200; ★ 4,544 per API)
- Author: Pydantic (org verified; pydantic.dev), team behind Pydantic.
- What it does: OTel-based observability SDK for LLM/agent systems (Pydantic AI, OpenAI, Anthropic instrumentations); backend is closed-source SaaS.
- Category: C. Observability
- Last commit: 2026-11-10 | License: MIT
- Safety: Safe: SDK open (MIT) but default destination is Logfire cloud; needs write token.
- X post: none verified

### OpenInference
- Repo: https://github.com/Arize-ai/openinference (HTTP 200; ★ 1,314 per API)
- Author: Arize AI (org `Arize-ai`, unverified badge; arize.com). Library has Arize Phoenix, not this.
- What it does: OpenTelemetry semantic conventions + auto-instrumentation for LLM/agent frameworks (Python/JS/Java).
- Category: C. Observability
- Last commit: 2026-11-10 | License: Apache-2.0
- Safety: Safe: its .agents/skills include an issue-triage skill that explicitly says to ignore injected instructions; phoenix-cli skill reads PHOENIX_API_KEY.
- X post: none verified

### claude-code-transcripts
- Repo: https://github.com/simonw/claude-code-transcripts (HTTP 200; ★ 1,730 per API)
- Author: Simon Willison (simonwillison.net), Django co-creator, Datasette author.
- What it does: Converts Claude Code session logs into publishable HTML transcripts for review/sharing.
- Category: C. Observability
- Last commit: 2026-02-12 | License: Apache-2.0
- Safety: Safe: scan clean; transcripts may contain secrets — review before publishing.
- X post: none verified


## D. Methodologies, prompt & agent-harness libraries

### Claude Cookbooks
- Repo: https://github.com/anthropics/claude-cookbooks (HTTP 200; ★ 54,484 per API)
- Author: Anthropic (org verified).
- What it does: Official notebooks/recipes: agent patterns, tool use, Agent SDK, skills, context/memory, OpenTelemetry tracing.
- Category: D. Workflow / prompt library
- Last commit: 2026-11-04 | License: MIT
- Safety: Safe: educational; one README uses astral.sh uv `curl|sh`; repo has its own detect-secrets audit skill.
- X post: none verified

### Claude Agent SDK (Python)
- Repo: https://github.com/anthropics/claude-agent-sdk-python (HTTP 200; ★ 8,516 per API)
- Author: Anthropic (org verified).
- What it does: Python SDK exposing the Claude Code agent loop (tools, hooks, subagents, sessions) for your own agents.
- Category: D. Agent harness
- Last commit: 2026-11-10 | License: MIT
- Safety: Safe: official; README suggests `curl -fsSL https://claude.ai/install.sh | bash` for the CLI (Anthropic-hosted).
- X post: none verified

### Amplifier
- Repo: https://github.com/microsoft/amplifier (HTTP 200; ★ 3,128 per API)
- Author: Microsoft (org verified).
- What it does: Research-demonstrator modular AI development assistant (successor to the Claude-Code-based Amplifier) with composable modules/agents.
- Category: D. Agent harness / methodology
- Last commit: 2026-11-02 | License: MIT
- Safety: Use with care: README caution 'research demonstrator… permissive AI tools'; installer path uses astral uv curl|sh / irm|iex.
- X post: none verified

### Advanced Context Engineering (ACE-FCA)
- Repo: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents (HTTP 200; ★ 2,825 per API)
- Author: HumanLayer (org; humanlayer.dev), Dex Horthy's company (12-Factor Agents, already in library).
- What it does: Essays/method for 'frequent intentional compaction': research→plan→implement with context kept small in large codebases.
- Category: D. Methodology
- Last commit: 2026-10-16 | License: none
- Safety: Safe: markdown only, no code.
- X post: none verified

### AGENTS.md
- Repo: https://github.com/agentsmd/agents.md (HTTP 200; ★ 25,421 per API)
- Author: agentsmd org (unverified badge; agents.md). Format announced by OpenAI with Google, Cursor, Factory etc. — org identity UNVERIFIED beyond site.
- What it does: Spec + site for the AGENTS.md convention: one README-for-agents file read by Codex, Cursor, Jules, Copilot and others.
- Category: D. Methodology / format
- Last commit: 2026-09-10 | License: MIT
- Safety: Safe: Next.js site; only Vercel Analytics on the website itself.
- X post: none verified

### DSPy
- Repo: https://github.com/stanfordnlp/dspy (HTTP 200; ★ 38,994 per API)
- Author: Stanford NLP (org; nlp.stanford.edu), Omar Khattab et al.
- What it does: Framework for programming LMs with signatures/modules and optimizers that compile prompts automatically.
- Category: D. Prompt programming
- Last commit: 2026-11-10 | License: MIT
- Safety: Safe: scan clean.
- X post: none verified

### smolagents
- Repo: https://github.com/huggingface/smolagents (HTTP 200; ★ 30,297 per API)
- Author: Hugging Face (org verified).
- What it does: Barebones agent library where agents write Python code actions; supports sandboxed executors (E2B, Docker, etc.).
- Category: D. Agent harness
- Last commit: 2026-10-06 | License: Apache-2.0
- Safety: Use with care: CodeAgent executes model-written code — use a remote/sandboxed executor; telemetry is opt-in OTel.
- X post: none verified

### Microsoft Agent Framework
- Repo: https://github.com/microsoft/agent-framework (HTTP 200; ★ 14,618 per API)
- Author: Microsoft (org verified). Successor to Semantic Kernel + AutoGen.
- What it does: Python/.NET framework for agents and graph-based multi-agent workflows with OTel tracing.
- Category: D. Agent harness
- Last commit: 2026-11-10 | License: MIT
- Safety: Safe: adds a feature-usage bitmask to its User-Agent (opt out AGENT_FRAMEWORK_FEATURE_MASK_DISABLED / AGENT_FRAMEWORK_USER_AGENT_DISABLED).
- X post: none verified

## Checked but excluded
- Already in library / skip list: pstack, gstack, tstack, superpowers, anthropics/skills, cloudflare skills + security-audit, microsoft/skills, trailofbits/skills, mattpocock/skills, addyosmani/agent-skills, GitHub MCP, Playwright MCP, Context7, promptfoo, stripe/ai, supabase/agent-skills, huggingface/skills, getsentry/skills, langfuse/langfuse, Arize phoenix, humanlayer/12-factor-agents, thedotmack/claude-mem, gastownhall/beads, openai/skills, vercel-labs/skills.
- MemPalace/mempalace (60k★ claimed 'best-benchmarked'): author/org reputation not verifiable → UNVERIFIED, excluded.
- topoteretes/cognee: real and active, but lower author profile than picks; excluded for rep bar.
- 2FastLabs/agent-squad: formerly awslabs/agent-squad, now moved out of AWS org → official status no longer verifiable; excluded.
- letta-ai/letta: now a pointer repo (12 files); replaced by letta-ai/letta-code.
- anthropics/life-sciences (no license, narrow), mongodb/agent-skills, prisma/skills, auth0/agent-skills, PostHog/skills ('under construction'), launchdarkly/ai-tooling: official but very new/low adoption (<200★); good watchlist candidates.
- openai/evals: last commit 2026-04, NOASSERTION license; stale. AgentOps-AI/agentops: last push 2026-06; stale.
- crewAI, langgraph, microsoft/graphrag, vercel/ai, cloudflare/agents, google/adk-python, pydantic-ai, openai-agents-js: frameworks rather than skills/workflows; out of scope for this pass (can add if wanted).
- Not found (404): temporalio/skills, netlify/agent-skills, awslabs/aws-agent-skills.

## Notable safety flags
- Telemetry ON by default: mem0 (PostHog), google/agents-cli, docker/docker-agent, getzep/graphiti, opik usage reports; Agent Framework UA feature mask. All have documented opt-outs.
- Data egress by design: letta-ai/claude-subconscious ships every Claude Code transcript to Letta cloud.
- curl|bash instructed inside skills (agent may run it): awslabs/agent-plugins aws-transform (awsstatic.com), google-gemini/gemini-skills (raw.githubusercontent), openai/plugins partner boltz plugin (third-party domain), trailofbits/claude-code-config (rustup, LM Studio).
- Permission bypass: trailofbits/claude-code-config recommends a --dangerously-skip-permissions alias (inside its sandbox design).
- No prompt-injection-style hidden instructions found; 'ignore previous instructions' hits were defensive text (AWS data-lake skill, Arize triage skill).
