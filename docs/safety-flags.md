# Safety flags

Defaults observed in public vendor documentation, READMEs, or a read-only pattern scan of cloned repositories on 2026-11-10 (America/New_York). Each flag is an observed fact from those sources, with the documented opt-out where one was found. This list is not a complete security audit and is not a guarantee that an unlisted tool is safe.

| Flag | Entry | Observed default | Documented way to turn it off | Source |
| --- | --- | --- | --- | --- |
| Telemetry on by default | Claude Code | Metrics telemetry on with the Claude API | DISABLE_TELEMETRY=1 | Contributor review of vendor docs |
| Telemetry on by default | Cline | Telemetry on | telemetryOptOut: true | Contributor review of vendor docs |
| Telemetry on by default | Gemini CLI | Anonymized usage statistics on | privacy.usageStatisticsEnabled: false | Contributor review of vendor docs |
| Telemetry on by default | Antigravity CLI | Interactions data collected | Opt out in settings (per README) | Contributor review of vendor docs |
| Telemetry on by default | Aider | Analytics opt-in is asked of a random subset; --yes-always accepts it | --analytics-disable | Contributor review of vendor docs |
| Telemetry on by default | Amp (not a catalog entry; closed source) | Threads sync to ampcode.com; auto-updates on | amp.updates.mode; telemetry opt-out unknown | Contributor review of vendor docs |
| Telemetry on by default | Mem0 | PostHog telemetry in SDK and CLI | MEM0_TELEMETRY=False | Contributor review of vendor docs |
| Telemetry on by default | Agents CLI (ADK) | One usage signal per command | AGENTS_CLI_TELEMETRY=0 | Contributor review of vendor docs |
| Telemetry on by default | Docker Agent | Usage telemetry | Documented opt-out in Docker Agent docs | Contributor review of vendor docs |
| Telemetry on by default | Graphiti | Anonymous telemetry with a UUID in ~/.cache/graphiti | GRAPHITI_TELEMETRY_ENABLED=false | Contributor review of vendor docs |
| Telemetry on by default | Opik | Anonymous usage reports | OPIK_USAGE_REPORT_ENABLED=false | Contributor review of vendor docs |
| Telemetry on by default | Microsoft Agent Framework | Feature-usage bitmask in the User-Agent | AGENT_FRAMEWORK_USER_AGENT_DISABLED or AGENT_FRAMEWORK_FEATURE_MASK_DISABLED | Contributor review of vendor docs |
| Cloud upload | Claude Subconscious | Every Claude Code transcript goes to Letta cloud; a background agent reads files and searches the web | Self-host Letta and set LETTA_BASE_URL | Contributor review of vendor docs |
| Cloud upload | Letta Code | Agents run against api.letta.com | Run `letta server` and self-host | Contributor review of vendor docs |
| Cloud upload | Logfire SDK | Default destination is Logfire cloud | Export to your own OTel backend | Contributor review of vendor docs |
| Cloud upload | OpenLLMetry | Traceloop SDK sends to Traceloop cloud when a key is set | Point the exporter at your own OTel endpoint | Contributor review of vendor docs |
| Cloud upload | Codex plugin for Claude Code | Code is sent to OpenAI for review | Inherent; use only on code you can share with OpenAI | Contributor review of vendor docs |
| Cloud upload | Claude Plugins Official | Marketplace is auto-added to Claude Code | CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL | Contributor review of vendor docs |
| curl\|bash installer | Agent Plugins for AWS | aws-transform skill runs an awsstatic.com install.sh \| bash; HyperPod scripts pipe base64 to bash on nodes | Install the CLI yourself after reading the script | Contributor review and pattern scan |
| curl\|bash installer | Agent Toolkit for AWS | A skill suggests the astral.sh uv curl\|sh installer; signing-in skill offers to run aws login | Install uv yourself; scope IAM read-only | Contributor review of vendor docs |
| curl\|bash installer | Gemini skills | gemini-api-cli skill pipes a raw.githubusercontent.com install.sh to bash | Install the CLI yourself | Contributor review of vendor docs |
| curl\|bash installer | OpenAI Plugins (Codex) | Some partner plugins run third-party curl\|sh or irm\|iex installers (e.g. boltz-api-cli) | Vet each plugin before enabling | Contributor review of vendor docs |
| curl\|bash installer | Trail of Bits Claude Code config | rustup and LM Studio curl\|sh installers | Install those tools yourself | Contributor review of vendor docs |
| curl\|bash installer | Amplifier | uv curl\|sh and irm\|iex in the install path | Install uv yourself | Contributor review of vendor docs |
| curl\|bash installer | Antigravity CLI | Binary installed via a curl script; no source or license | Read the script first | Contributor review of vendor docs |
| Auto-approve / yolo | Goose | GOOSE_MODE defaults to auto (fully autonomous) | GOOSE_MODE=approve or smart_approve | Contributor review of vendor docs |
| Auto-approve / yolo | Cline | CLI --auto-approve defaults to true; no shell allow/deny list | --auto-approve=false or ACP mode; block commands with a PreToolUse hook; keep extension YOLO off | Contributor review of vendor docs |
| Auto-approve / yolo | Claude Code | Interactive sessions start in auto mode (classifier) on v2.1.283+ | Set permissions.defaultMode to default | Contributor review of vendor docs |
| Auto-approve / yolo | Amp (not a catalog entry; closed source) | Allow-all when no permissions are set; unmatched MCP servers allowed | Configure permission rules (cited from search, not fetched directly) | Contributor review of vendor docs |
| Auto-approve / yolo | Cursor CLI (not a catalog entry; closed source) | -p has write and shell access; --yolo/--force plus --trust runs unattended | Avoid --force and --trust; use --sandbox enabled | Contributor review of vendor docs |
| Auto-approve / yolo | Aider | --yes-always confirms every prompt | Don't pass --yes-always | Contributor review of vendor docs |
| Auto-approve / yolo | OpenCode | run --auto approves anything not denied; serve can bind 0.0.0.0 | Don't pass --auto; bind to localhost | Contributor review of vendor docs |
| Auto-approve / yolo | Codex CLI | --yolo removes sandbox and approvals (opt-in) | Default is safe; don't pass --yolo | Contributor review of vendor docs |
| Auto-approve / yolo | Trail of Bits Claude Code config | Recommends a claude-yolo alias (--dangerously-skip-permissions) inside its sandbox | Use only inside that sandbox | Contributor review of vendor docs |
| Auto-approve / yolo | Docker Agent | --yolo / autoApprove mode available | Leave it off | Contributor review of vendor docs |
| Sandbox off by default | Grok Build | No sandbox; --yolo always approves | Enable the sandbox (docs.x.ai/build/features/sandbox) | Contributor review of vendor docs |
| Sandbox off by default | Gemini CLI | Sandbox off unless --yolo | Run with --sandbox; set security.disableYoloMode | Contributor review of vendor docs |
| Sandbox off by default | Claude Code | Bash sandbox is opt-in | Turn on the sandbox in settings | Contributor review of vendor docs |
| Sandbox off by default | Goose | Approval policy only, no OS sandbox | Run in a container or VM | Contributor review of vendor docs |
| Sandbox off by default | Pi | Core defaults unknown | Run in a container (pi.dev docs) | Contributor review of vendor docs |
| Model-code execution | smolagents | CodeAgent runs model-written Python | Use a remote or sandboxed executor (E2B, Docker) | Contributor review of vendor docs |
| Model-code execution | Symphony | Autonomous agents act on repos; preview for trusted environments | Run in an isolated environment | Contributor review of vendor docs |
| Model-code execution | Episodic Memory | npm postinstall runs a local script | Review the script; install from the plugin | Contributor review of vendor docs |


Defaults that showed up most often in this review: Goose runs in auto mode with no OS sandbox; Cline's CLI auto-approves and sends telemetry by default; Amp (closed source, not a catalog entry) allows all tools and unmatched MCP servers when no rules are set; Claude Code starts interactive sessions in classifier auto mode; Grok Build and Gemini CLI run without a sandbox by default. Codex CLI was the closest to a conservative default among the harnesses reviewed (sandbox on, network off, according to OpenAI's docs).

ClawHub, OpenClaw's public skill registry, is rated **Avoid** in this catalog. Public reports by [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), [Acronis TRU](https://www.acronis.com/en/tru/posts/poisoning-the-well-ai-supply-chain-attacks-on-hugging-face-and-openclaw/), and [Dark Reading](https://www.darkreading.com/cyber-risk/malicious-openclaw-skills-clawhub-threaten-ai-supply-chain) describe large numbers of malicious skills uploaded there. Do not install third-party skills from it unreviewed.
