#!/usr/bin/env python3
"""Regenerate CSV and Markdown docs from data/library.json and data/meta.json."""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs"


def md_cell(value) -> str:
    s = "" if value is None else str(value)
    return s.replace("|", "\\|").replace("\n", " ").strip()


def fmt_stars(n: int) -> str:
    if n >= 100000:
        return f"{n / 1000:.0f}k"
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


def table(headers, rows) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(md_cell(c) for c in row) + " |")
    return "\n".join(lines) + "\n"


def load():
    catalog = json.loads((DATA / "library.json").read_text())
    meta = json.loads((DATA / "meta.json").read_text())
    authors = json.loads((DATA / "authors.json").read_text())
    return catalog, meta, authors


def write_csv(entries):
    path = DATA / "library.csv"
    fields = [
        "name", "repo", "url", "author", "owner", "overall", "tier",
        "safety_rating", "safety_score", "popularity_score", "usefulness_score",
        "type", "type_label", "type_secondary", "topic", "last_commit",
        "latest_release", "latest_release_date", "stars", "license", "archived",
        "description", "use_case", "safety_notes", "works_with", "install",
        "curl_pipe_installer", "setup_time", "accounts_needed", "cost",
        "impact", "quality", "adoption", "ease", "ease_note", "confidence",
        "overlap_cluster", "related_note", "x_post", "research_credit",
    ]
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for e in entries:
            row = dict(e)
            ww = row.get("works_with") or []
            row["works_with"] = "; ".join(ww) if isinstance(ww, list) else ww
            w.writerow(row)


def catalog_rows(entries):
    rows = []
    for i, e in enumerate(entries, 1):
        rows.append([
            i, e["name"], e["repo"], e["overall"], e["tier"], e["safety_score"],
            e["popularity_score"], e["usefulness_score"], e["safety_rating"],
            e["type_label"], fmt_stars(e["stars"]), e["last_commit"], e["use_case"],
        ])
    return rows


def write_catalog(catalog, meta):
    entries = catalog["entries"]
    DOCS.mkdir(parents=True, exist_ok=True)
    n = catalog["count"]
    generated = catalog["generated"]
    body = [
        "# Catalog",
        "",
        f"{n} entries, sorted by overall score then name. Snapshot date: {generated} (America/New_York).",
        "Headline scores are out of 100. This is a point-in-time read-only review, not a security audit or guarantee.",
        "",
        table(
            ["#", "Name", "Repo", "Overall", "Tier", "Safety", "Popularity", "Usefulness", "Rating", "Type", "Stars", "Updated", "Use case"],
            catalog_rows(entries),
        ),
        "",
        "See [per-type tables](types/) for descriptions and safety notes, and [overlap-clusters.md](overlap-clusters.md) for recommended picks when several entries do the same job.",
        "",
    ]
    (DOCS / "CATALOG.md").write_text("\n".join(body))


def write_types(catalog, meta):
    tdir = DOCS / "types"
    if tdir.exists():
        for p in tdir.glob("*.md"):
            p.unlink()
    tdir.mkdir(parents=True, exist_ok=True)
    slugs = meta["type_slugs"]
    typenames = meta["types"]
    typedesc = meta["type_descriptions"]
    by = defaultdict(list)
    for e in catalog["entries"]:
        by[e["type"]].append(e)
    index = [
        "# Entries by type",
        "",
        f"Primary type for each of the {catalog['count']} catalog entries.",
        "",
        table(
            ["Type", "What belongs here", "Entries"],
            [
                [typenames[k], typedesc[k], len(by.get(k, []))]
                for k in typenames
            ],
        ),
        "",
    ]
    for typ in typenames:
        xs = by.get(typ, [])
        slug = slugs[typ]
        index.append(f"- [{typenames[typ]}]({slug}.md) ({len(xs)})")
        rows = []
        for e in xs:
            rows.append([
                e["name"], f"[{e['repo']}]({e['url']})", e["overall"], e["tier"],
                e["safety_score"], e["popularity_score"], e["usefulness_score"],
                e["safety_rating"], e["last_commit"], e["cost"], e["description"],
                e["safety_notes"],
            ])
        page = [
            f"# {typenames[typ]}",
            "",
            typedesc[typ],
            "",
            f"{len(xs)} entries, sorted by overall score. Snapshot date: {catalog['generated']} (America/New_York).",
            "",
            table(
                ["Name", "Repo", "Overall", "Tier", "Safety", "Popularity", "Usefulness", "Rating", "Updated", "Cost", "Description", "Safety notes"],
                rows,
            ),
            "",
            "[Back to all types](README.md) · [Full catalog](../CATALOG.md)",
            "",
        ]
        (tdir / f"{slug}.md").write_text("\n".join(page))
    index.extend(["", "[Full catalog](../CATALOG.md)", ""])
    (tdir / "README.md").write_text("\n".join(index) + "\n")


def write_clusters(catalog, meta):
    by = {e["repo"]: e for e in catalog["entries"]}
    parts = [
        "# Overlap clusters and duplicates",
        "",
        "Entries that do a similar job, with a recommended pick and the reason. "
        "Exact `SKILL.md` copies were found by hashing files across read-only clones.",
        "",
        "Ratings and recommended picks are observations from this snapshot, not exclusive endorsements.",
        "",
    ]
    for cl in meta["clusters"]:
        members = [by[r] for r in cl["members"] if r in by]
        members.sort(key=lambda e: (-e["overall"], e["name"].lower()))
        pick = cl["recommended"]
        pick_name = by[pick]["name"] if pick in by else pick
        parts.append(f"## {cl['name']}")
        parts.append("")
        parts.append(f"Recommended pick: **{pick_name}** (`{pick}`). {cl['reason']}")
        parts.append("")
        rows = []
        for e in members:
            note = e.get("related_note") or ""
            label = f"{e['name']} (pick)" if e["repo"] == pick else e["name"]
            rows.append([label, e["repo"], e["overall"], e["safety_score"], e["popularity_score"], e["usefulness_score"], e["safety_rating"], note])
        parts.append(table(["Entry", "Repo", "Overall", "Safety", "Popularity", "Usefulness", "Rating", "Note"], rows))
        parts.append("")
    parts.extend([
        "## Exact duplicates, mirrors and forks",
        "",
        "Identical `SKILL.md` counts come from hashing files over 300 bytes. A zero means a documented fork or successor, not identical files.",
        "",
        table(
            ["Repo", "Overlaps with", "Identical SKILL.md files", "What it means"],
            [
                [d["repo"], d["overlaps_with"], d["identical_skill_md"] or "—", d["meaning"]]
                for d in meta["duplicates"]
            ],
        ),
        "",
        "Roo Code (archived 15 May 2026) and its community fork Zoo Code are not listed; Cline is the pick for that family.",
        "",
    ])
    (DOCS / "overlap-clusters.md").write_text("\n".join(parts))


def write_flags(meta, catalog):
    parts = [
        "# Safety flags",
        "",
        "Defaults observed in public vendor documentation, READMEs, or a read-only pattern scan of cloned repositories "
        f"on {catalog['generated']} (America/New_York). Each flag is an observed fact from those sources, with the documented opt-out where one was found. "
        "This list is not a complete security audit and is not a guarantee that an unlisted tool is safe.",
        "",
        table(
            ["Flag", "Entry", "Observed default", "Documented way to turn it off", "Source"],
            [
                [f["flag"], f["entry"], f["observed_default"], f["opt_out"], f["source"]]
                for f in meta["safety_flags"]
            ],
        ),
        "",
        "Defaults that showed up most often in this review: Goose runs in auto mode with no OS sandbox; "
        "Cline's CLI auto-approves and sends telemetry by default; Amp (closed source, not a catalog entry) "
        "allows all tools and unmatched MCP servers when no rules are set; Claude Code starts interactive "
        "sessions in classifier auto mode; Grok Build and Gemini CLI run without a sandbox by default. "
        "Codex CLI was the closest to a conservative default among the harnesses reviewed (sandbox on, network off, according to OpenAI's docs).",
        "",
        "ClawHub, OpenClaw's public skill registry, is rated **Avoid** in this catalog. Public reports by "
        "[Snyk](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/), "
        "[Acronis TRU](https://www.acronis.com/en/tru/posts/poisoning-the-well-ai-supply-chain-attacks-on-hugging-face-and-openclaw/), "
        "and [Dark Reading](https://www.darkreading.com/cyber-risk/malicious-openclaw-skills-clawhub-threaten-ai-supply-chain) "
        "describe large numbers of malicious skills uploaded there. Do not install third-party skills from it unreviewed.",
        "",
    ]
    (DOCS / "safety-flags.md").write_text("\n".join(parts))


def write_stacks(catalog, meta):
    by = {e["repo"]: e for e in catalog["entries"]}
    parts = [
        "# Starter stacks",
        "",
        "If you are doing one of these jobs, start with these higher-scoring cluster picks. Scores are from the "
        f"{catalog['generated']} snapshot.",
        "",
    ]
    for s in meta["starter_stacks"]:
        parts.append(f"## {s['name']}")
        parts.append("")
        parts.append(s["blurb"])
        parts.append("")
        rows = []
        for repo in s["repos"]:
            e = by[repo]
            rows.append([e["name"], repo, e["overall"], e["safety_score"], e["popularity_score"], e["usefulness_score"], e["use_case"], e["cost"]])
        parts.append(table(["Entry", "Repo", "Overall", "Safety", "Popularity", "Usefulness", "Use case", "Cost"], rows))
        parts.append("")
    (DOCS / "starter-stacks.md").write_text("\n".join(parts))


def write_authors(catalog, authors):
    counts = defaultdict(list)
    for e in catalog["entries"]:
        counts[e["owner"]].append(e)
    kinds = ["Company", "Person", "Project", "Government"]
    parts = [
        "# Author directory",
        "",
        "Profiles are taken from public GitHub profiles, READMEs, and X accounts linked from GitHub. "
        "X handles are listed only when they were linked from the author's GitHub profile or appeared on their own posts.",
        "",
    ]
    for kind in kinds:
        group = [a for a in authors if a["kind"] == kind and a["github_owner"] in counts]
        if not group:
            continue
        parts.append(f"## {kind}")
        parts.append("")
        for a in sorted(group, key=lambda x: (-len(counts[x["github_owner"]]), x["name"].lower())):
            xs = sorted(counts[a["github_owner"]], key=lambda e: (-e["overall"], e["name"].lower()))
            xline = f" · [X]({a['x']})" if a.get("x") else ""
            parts.append(f"### {a['name']}")
            parts.append("")
            parts.append(a["profile"])
            parts.append("")
            parts.append(f"[GitHub]({a['github']}){xline} · {len(xs)} catalog {'entry' if len(xs)==1 else 'entries'}")
            parts.append("")
            parts.append(table(
                ["Entry", "Overall", "Tier", "Rating", "Updated"],
                [[e["name"], e["overall"], e["tier"], e["safety_rating"], e["last_commit"]] for e in xs],
            ))
            parts.append("")
    (DOCS / "authors.md").write_text("\n".join(parts))


def main() -> int:
    catalog, meta, authors = load()
    write_csv(catalog["entries"])
    write_catalog(catalog, meta)
    write_types(catalog, meta)
    write_clusters(catalog, meta)
    write_flags(meta, catalog)
    write_stacks(catalog, meta)
    write_authors(catalog, authors)
    print(f"Regenerated CSV and docs for {catalog['count']} entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
