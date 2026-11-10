# Evals & testing

Evals, testing and skill measurement

5 entries, sorted by overall score. Snapshot date: 2026-11-10 (America/New_York).

| Name | Repo | Overall | Tier | Safety | Popularity | Usefulness | Rating | Updated | Cost | Description | Safety notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| promptfoo | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | 94 | S | 100 | 58 | 92 | Safe | 2026-11-09 | Free | A CLI and library for evaluating and red-teaming LLM apps and agents: write test cases in YAML, compare prompts and models, run in CI, and generate attack suites. Now part of OpenAI and still MIT. Install with `npm install -g promptfoo` or `npx promptfoo@latest init`. | Widely used; scan hits are documented attack examples |
| MCP Inspector | [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | 93 | S | 100 | 62 | 91 | Safe | 2026-11-04 | Free | The official MCP Inspector for testing MCP servers via a web UI, CLI or TUI: list tools, call them and watch messages. Essential when building your own servers. Run with `npx @modelcontextprotocol/inspector`. | Official MCP project; keep it bound to localhost |
| DeepEval | [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | 85 | A | 100 | 56 | 82 | Safe | 2026-11-10 | Free | DeepEval is a Pytest-style framework for unit-testing LLM apps and agents with metrics like G-Eval, task completion, hallucination and tool correctness, running locally. Good for regression tests on prompts and agents. Install with `pip install -U deepeval`. | Well-known; the only postinstall hook builds its docs site |
| Inspect | [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | 82 | A | 100 | 46 | 75 | Safe | 2026-11-10 | Free | Inspect, the UK AI Security Institute's framework for LLM and agent evaluations, with tool use, sandboxes, model-graded scoring and 200+ prebuilt evals. Strong for serious agent benchmarking. Install with pip and write evals in Python. | Government AI safety lab; clean scan |
| upskill | [huggingface/upskill](https://github.com/huggingface/upskill) | 76 | B | 100 | 55 | 71 | Safe | 2026-10-14 | Freemium | upskill generates Agent Skills and evaluates them: create a skill, test it against several models, and measure how much it lifts results for Claude Code, OpenCode, Codex and others. It is for people who write their own skills. Install with pip or uv and run its CLI. | Official Hugging Face; pip/uv install; model keys from env only; scan clean |


[Back to all types](README.md) · [Full catalog](../CATALOG.md)
