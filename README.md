# AI Skill Library

A point-in-time catalog of **184** agent skills, harnesses, MCP servers, frameworks, and related tools, each scored for safety, popularity, and usefulness.

Snapshot date: **2026-11-10** (America/New_York). Stars, releases, licenses, and commit dates were read from the GitHub API on that day. Repositories were cloned read-only (git hooks disabled); nothing was installed or run.

This is a **read-only review of public sources**, not a security audit, penetration test, or guarantee of safety, quality, or fitness for a particular purpose. Ratings and flags record what was observed in public repositories and vendor documentation at the time of the snapshot, with the evidence noted on each entry. Projects change quickly; re-check a repo before you install it.

An interactive companion Page (filters, cards, and the same scores) is at [the AI Skill Library canvas](https://cursor.com/canvas/store-a0421101-7af2-4e7f-b327-4f9a0a3c0f49/39b4ad7b-14d8-431c-9667-9042381315c0).

## At a glance

| Rating | Count | Tier | Count | Range |
| --- | --- | --- | --- | --- |
| Safe | 121 | S | 13 | 90–100, adopt now |
| Use with care | 62 | A | 59 | 80–89, strong pick |
| Avoid | 1 | B | 60 | 70–79, good in the right stack or with care |
|  |  | C | 49 | 55–69, situational, stale, or risky; read first |
|  |  | D | 3 | under 55, skip or use only as a reference |

The one Avoid entry is ClawHub (OpenClaw's public skill registry). Public reports by [Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), [Acronis TRU](https://www.acronis.com/en/tru/posts/poisoning-the-well-ai-supply-chain-attacks-on-hugging-face-and-openclaw/), and [Dark Reading](https://www.darkreading.com/cyber-risk/malicious-openclaw-skills-clawhub-threaten-ai-supply-chain) describe large numbers of malicious skills uploaded there.

## Top picks

| # | Name | Overall | Tier | Safety | Popularity | Usefulness | Type | Use case |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [GitHub MCP Server](https://github.com/github/github-mcp-server) | 97 | S | 100 | 70 | 97 | MCP servers | Ask your agent to triage this week's open issues, label them and draft a fix PR for the top bug without leaving the chat. |
| 2 | [Codex CLI](https://github.com/openai/codex) | 96 | S | 100 | 78 | 94 | Agent harnesses & CLIs | Point Codex at a failing test suite in your repo and let it fix the failures inside its sandbox, approving each command before it touches the network. |
| 3 | [agent-browser](https://github.com/vercel-labs/agent-browser) | 94 | S | 100 | 76 | 91 | Browser & computer use | Let a coding agent click through your web app's checkout flow step by step with compact page snapshots, keeping token cost low on long sessions. |
| 4 | [Context7](https://github.com/upstash/context7) | 94 | S | 100 | 70 | 94 | MCP servers | Building against a library that shipped a breaking release last month, add "use context7" so the agent writes code from the current docs instead of a stale API. |
| 5 | [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 94 | S | 100 | 71 | 92 | Browser & computer use | After your agent changes a signup form, have it open the page, fill the form and confirm the success message actually appears. |
| 6 | [promptfoo](https://github.com/promptfoo/promptfoo) | 94 | S | 100 | 58 | 92 | Evals & testing | Before merging a prompt change, run a YAML test suite in CI that compares old and new prompts and fails the PR if accuracy drops or a jailbreak test passes. |
| 7 | [MCP Inspector](https://github.com/modelcontextprotocol/inspector) | 93 | S | 100 | 62 | 91 | Evals & testing | While building your own MCP server, open the Inspector to list its tools, call each one by hand and watch the raw JSON-RPC messages to debug a bad schema. |
| 8 | [Claude Agent SDK (Python)](https://github.com/anthropics/claude-agent-sdk-python) | 91 | S | 100 | 63 | 89 | Agent frameworks & SDKs | Build a custom PR-triage agent on the same loop Claude Code uses, with your own tools and permissions. |
| 9 | [OpenHands](https://github.com/OpenHands/OpenHands) | 91 | S | 100 | 66 | 88 | Dev tools & agent ops | Run Codex, Claude Code and OpenHands agents on different repos from one self-hosted control center and watch them side by side. |
| 10 | [Agent Skills (Addy Osmani)](https://github.com/addyosmani/agent-skills) | 90 | S | 100 | 81 | 88 | Skills & skill packs | Starting a new feature, have the agent walk define → plan → build → verify → review so it can't skip tests or ship without a review step. |

See [docs/starter-stacks.md](docs/starter-stacks.md) for role-based starting sets, and [docs/CATALOG.md](docs/CATALOG.md) for the full list.

## How scores work

Overall score (0–100):

```
Overall = Impact (30) + Quality (20) + Adoption (15) + Ease (15) + Safety (20)
```

An **Avoid** rating sets safety to 0 and caps the overall score at 20.

| Headline score | Range | Formula |
| --- | --- | --- |
| Safety | 0–100 | Safe → 100; Use with care → 60 (40 when the tool has broad system access or ships unvetted bulk content); Avoid → 0. This is the overall score's safety component multiplied by 5. |
| Popularity | 0–100 | Stars 40 × min(1, log10(stars+1) ÷ 5.5) + growth 20 × min(1, log10(stars per month+1) ÷ 4) + X traction 15 × min(1, log10(likes on a linked post+1) ÷ 4.3) + maintainer reach 25 × min(1, log10(max(GitHub, X followers)+1) ÷ 6), minus 10 for a star-velocity anomaly. About 300k stars or 1M followers max out their parts, so no single signal dominates. |
| Usefulness | 0–100 | (Impact + Quality + Ease) ÷ 65 × 100. Popularity and safety are kept out of this headline. |

| Sub-score | Max | How it is derived |
| --- | --- | --- |
| Impact | 30 | Judgment call for a developer building agent products with many PRs and CI. 27–30 daily-driver core; 20–26 strong fit; 12–19 situational; under 12 off-target or stack-specific. |
| Quality | 20 | Measured from the repo: README depth 0–4, test files 0–5 (docs or specs get 2 as n/a), CI workflows 0–3, GitHub releases 0–4, last commit 0–4 (≤14 days 4, ≤45 3, ≤120 2, ≤240 1). Deprecated, sunsetting, superseded, or ownership-unclear repos are capped at 6. |
| Adoption and trust | 15 | Stars on a log scale, at most 6 points (1.2 × log10(stars)). Maintainer reputation 0–6 (official vendor 6, well-known person or company 5, established startup 4, credible small team 3, little-known 2, unverified 1). Contributors 0–3. Minus 2 when stars grow over 10k a month for a little-known maintainer. |
| Ease of adoption | 15 | One npx or plugin command across common coding agents scores 14–15; accounts, keys, Docker, or a new process 9–12; platform deploys or heavy config under 9. |
| Safety | 20 | Safe 20; Use with care 12, or 8 for broad system access or unvetted bulk content; Avoid 0 and the total is capped at 20. Unsafe defaults such as auto-approve without a sandbox, or telemetry on by default, moved an entry to Use with care. |

Other notes on the rubric:

- Stars can add at most 6 of 100 overall points. The gap between 1k and 300k stars is under 3 overall points.
- Quality and the star, release, contributor, and commit figures were read from the GitHub API and the cloned repos on 2026-11-10. Impact and ease are judgment calls, about ±3 points.
- Most entries have no X post linked, so the X part of Popularity is 0 for them; it only adds when a verified post was found.
- Confidence "Low" means a little-known maintainer or unusual star growth; treat that overall score as about ±5.
- Scores are for a general agent-product development use case. A finance or Azure pack can be excellent and still score C here.

## Safety ratings

| Rating | Meaning in this catalog |
| --- | --- |
| Safe | Official or well-known source; the read-only scan and vendor docs did not show a serious default-on risk, or the risk is the ordinary kind (for example, scoping a token). |
| Use with care | Observed issues such as telemetry or cloud upload on by default, a curl-to-shell installer, auto-approve or missing sandbox defaults, or a large unvetted catalog. The entry can still be useful; read the safety notes and opt out of the defaults you do not want. |
| Avoid | Public evidence of a serious, practical risk. In this snapshot, that applies only to ClawHub, as cited above. |

See [docs/safety-flags.md](docs/safety-flags.md) for the 43 observed defaults, each with the documented opt-out where one was found.

## How vetting was done

1. **Verified every link.** Repo metadata, latest commit, releases, and contributors came from the GitHub API on 2026-11-10. Renamed repos were followed (for example sst/opencode → anomalyco/opencode, block/goose → aaif-goose/goose, docker/cagent → docker/docker-agent).
2. **Read-only scan.** Shallow clones with git hooks disabled. Nothing was installed or run. A pattern scan looked for curl-to-shell, base64 exec, credential reads, exfiltration, prompt-injection text, hidden Unicode, and install hooks.
3. **Read every hit.** Most hits were defensive docs, test fixtures, emoji joiners, or official installers. The reason is written on the entry.
4. **Checked defaults.** Contributor review of vendor docs covered approval modes, sandboxes, telemetry, and data upload. Those flags are on the entry and in the safety-flags list.
5. **Found duplicates.** Every `SKILL.md` over 300 bytes was hashed across the clones to find mirrors and re-bundled copies. See [docs/overlap-clusters.md](docs/overlap-clusters.md).
6. **Scored with the rubric above.** Quality, adoption, and popularity were computed from measured signals; impact and ease were judged once per entry.

## Types

| Type | What belongs here | Entries |
| --- | --- | --- |
| Skills & skill packs | SKILL.md packs and plugins that teach an agent a domain or task | 40 |
| Workflows & methodologies | Methods and process packs: spec-driven, planning, TDD, review loops | 15 |
| Agent harnesses & CLIs | Agents you run: terminal and IDE coding agents | 17 |
| Agent frameworks & SDKs | Libraries and SDKs for building your own agents | 9 |
| MCP servers | Servers that give agents tools or data over MCP | 19 |
| MCP & agent infra / gateways | Gateways, registries and frameworks for building and running MCP and tools | 3 |
| Sandboxes & runtimes | Isolated environments where agent code runs | 3 |
| Browser & computer use | Browser and desktop control for agents | 7 |
| Evals & testing | Evals, testing and skill measurement | 5 |
| Agent security & guardrails | Scanners, red-teaming, guardrails and hardening configs | 9 |
| CI & GitHub agents | Agents that run in GitHub Actions and CI | 4 |
| Memory & context | Long-term memory, knowledge graphs and session recall | 10 |
| Observability & cost | Tracing, cost and transcript tooling | 12 |
| Prompt & subagent libraries | Prompt, SOP and subagent collections | 1 |
| Directories & awesome lists | Awesome lists, registries and marketplaces | 12 |
| Guides, specs & starters | Guides, open specs and starter code | 5 |
| Dev tools & agent ops | Runners, installers and agent ops tools | 13 |

Per-type tables: [docs/types/](docs/types/).

## Repository layout

- [`data/library.json`](data/library.json) — canonical catalog (scores, descriptions, use cases, setup, evidence breakdowns)
- [`data/library.csv`](data/library.csv) — the same entries as a spreadsheet (regenerated)
- [`data/meta.json`](data/meta.json) — types, overlap clusters, duplicates, safety flags, starter stacks, scoring notes
- [`data/authors.json`](data/authors.json) — public author directory
- [`docs/CATALOG.md`](docs/CATALOG.md) — full table, sorted by overall score
- [`docs/overlap-clusters.md`](docs/overlap-clusters.md) — recommended pick when several tools overlap
- [`docs/safety-flags.md`](docs/safety-flags.md) — observed unsafe or noteworthy defaults
- [`docs/starter-stacks.md`](docs/starter-stacks.md) — starting sets by job
- [`docs/authors.md`](docs/authors.md) — authors and their entries
- [`sources/official-source-additions.md`](sources/official-source-additions.md) — contributor research notes on official company and verified-creator repos
- [`sources/harness-and-plugin-review.md`](sources/harness-and-plugin-review.md) — contributor research notes on coding-agent harnesses and official plugin catalogs
- [`scripts/generate.py`](scripts/generate.py) — regenerates the CSV and Markdown docs from the JSON files

```bash
python3 scripts/generate.py
```

## License

The catalog data and documentation are licensed under [CC BY 4.0](LICENSE). Each listed project keeps its own license; see the `license` field on the entry.

tstack in this catalog is [Theo Browne's](https://github.com/t3dotgg/tstack) (`t3dotgg/tstack`).
