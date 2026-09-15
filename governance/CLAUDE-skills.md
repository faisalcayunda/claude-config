---
title: "CLAUDE-skills.md — §14 Skills & Slash Commands"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §14. §14.1 Group A table also inlined into §2.4 Self-Check for Law 6 enforcement.

---

## 14. Skills & Slash Commands

Skills are **not** agents. They are invocable procedures defined globally (`~/.claude/skills/` or built-in) or locally (`.claude/commands/` in the project). Law 6 requires skill-first resolution before specialist dispatch.

### 14.1 Global Skills — Group A (MUST invoke when trigger matches)

| Skill | Trigger | Role |
|---|---|---|
| `update-config` | Configure hooks, automated behaviors, `settings.json` | Harness configurator. Required for any persistent behavior change. |
| `statusline-setup` | Configure the Claude Code status line | Status line configurator. |
| `keybindings-help` | Customize keyboard shortcuts / `~/.claude/keybindings.json` | Keybinding editor. |
| `simplify` | After any implementation wave produces changed code | Quality/efficiency pass — mandatory in Wave 3. |
| `dispatching-parallel-agents` *(v2.1.0)* | 2+ independent tasks with no shared state or sequential dependency | Codifies Law 5 parallel-dispatch discipline. One agent per independent problem domain. |
| `gh-fix-ci` *(v2.1.0)* | User asks to debug/fix failing GitHub Actions PR checks | Uses `gh` CLI to pull failing logs, summarize context, propose fix plan, implement after approval. Scope: GitHub Actions only. |
| `airflow-dag-lint` *(v2.8.0)* | Any DAG file (`*.py` in `dags/`) is modified or reviewed | Pre-gate static lint for Airflow 3.1.7. Runs before code-reviewer; finds import errors, deprecated APIs, top-level code violations, secrets hygiene issues. Output feeds the gate — does not replace it. |
| `data-quality-check` *(v2.8.0)* | User asks to add DQ checks, generate test stubs, or scaffold quality validation for a model or table | Generator: produces dbt test definitions or Great Expectations suite YAML. Never executes tests at runtime. |
| `data-quality-specialist` *(v3.5.0)* | End-to-end data quality analysis: profiling, field-level rule design, monitoring design, DQ governance docs, DQ SOP/SLA, scorecard, issue log, SQL validation checks across all data layers, or PNG data visualization from quality metrics | Comprehensive DQ specialist — covers DAMA-DMBOK dimensions (Accuracy, Validity, Timeliness, Completeness, Uniqueness, Consistency), all data layers (source through mart), ownership/stewardship/remediation, and chart exports. Distinct from `data-quality-check` (which generates test stubs only). |
| `dbt-model-gen` *(v2.8.0)* | User asks to create a new dbt model or generate dbt scaffolding | Generator: scaffolds dbt model SQL with `{{ source() }}`/`{{ ref() }}` macros and `schema.yml` stub for staging/intermediate/marts layers. Never executes dbt. |
| `data-engineer-boilerplate` *(v2.9.0)* | User asks to bootstrap a new data project, scaffold project structure, or generate folder/boilerplate layout | Generator: scaffolds mature Airflow 3.1.7 + dbt + PySpark project folder trees and key file stubs. Never executes commands. Distinct from `dbt-model-gen` (single model) — this generates the full project skeleton. |
| `badan-gizi-nasional` *(v3.2.0)* | Any question mentioning BGN, MBG, SPPG, KPPG, SIPGN, Peruri, Juknis MBG, Kepka BGN, Perpres 83/2024, Perpres 115/2025, or related topics | Knowledge base: single source of truth for BGN/MBG/SIPGN — routes to 28 reference files, enforces numerical accuracy and regulatory citation discipline. JANGAN untuk PKH/BPNT/KIP/PIP. |
| `engineering-researcher` *(v2.10.0)* | Architecture/system design research, DevOps/SRE research, cloud/security research, ADR generation, Technical RFC, System Design Document, Architecture Review, Threat Model, Tech Radar, Runbook, Postmortem, Test Strategy, API Design, Performance Benchmark | World-class engineering research + deliverable generation across 10 knowledge domains and 12 templates (217+ sources). |
| `autoresearch` *(v3.5.0)* | User invokes `/autoresearch` or any sub-command: `:plan`, `:predict`, `:learn`, `:debug`, `:fix`, `:reason`, `:scenario`, `:security`, `:ship`; or requests autonomous iterative improvement with a measurable goal (coverage %, test pass rate, error count, etc.) | Autonomous goal-directed iteration loop: Modify → Verify → Keep/Discard → Repeat. Routes to sub-skill variants per §15. |
| `data-sla-sop` *(v3.5.0)* | User asks to create SLA documents, SOP for data operations, data pipeline SLA, data governance SOP, service level agreement for data, SOP data ingestion/warehouse/quality, or combined SLA+SOP guide for any data system (government/SPBE, enterprise, fintech) | Generator: produces integrated Panduan Lengkap SLA & SOP Data document combining SLA targets + SOP procedures. Covers government (Perpres 95/2018, UU PDP, SPBE), banking (OJK/SNAP), fintech, and enterprise contexts. |
| `save` *(v3.3.0)* | User says "save this", "save that answer", "/save", "file this", "save to wiki", "save this session", "file this conversation", "keep this", "save this analysis", or "add this to the wiki" | Knowledge persistence: files the current conversation as a structured note in ~/.claude wiki (/Users/isal/.claude/wiki/). |
| `wiki` *(v3.3.0)* | User says "set up wiki", "scaffold vault", "/wiki", "obsidian vault", "knowledge base setup" | Wiki setup, scaffolding, vault routing. Delegates to sub-skills. |
| `wiki-ingest` *(v3.3.0)* | User says "ingest", "process this source", "add this to the wiki", "ingest this url", "batch ingest" | Ingest sources into wiki — files, URLs, batch. Creates/updates pages, cross-references. |
| `wiki-query` *(v3.3.0)* | User asks a question and says "from the wiki", "search wiki", "what does the wiki say about", "query:" | Answer questions from wiki content. |
| `wiki-lint` *(v3.3.0)* | User says "lint the wiki", "health check", "wiki audit", "find orphans", "wiki maintenance" | Health check — orphan pages, dead links, stale claims, frontmatter gaps. |
| `wiki-fold` *(v3.3.0)* | User says "fold the wiki", "rollup log", "compress wiki log", "/wiki-fold" | Log rollup (Mechanism 1). Folds old log entries into summary pages. |
| `canvas` *(v3.3.0)* | User says "/canvas", "add to canvas", "create canvas", "add image to canvas", "canvas zone" | Visual layer — add images, PDFs, notes to Obsidian canvas. |
| `defuddle` *(v3.3.0)* | User says "defuddle", "clean this page", "strip this url", "fetch and clean", "remove clutter" | Strip web clutter before wiki ingest — returns clean markdown. |
| `obsidian-bases` *(v3.3.0)* | User says "obsidian bases", "create base", "database view in obsidian", "bases" | Obsidian Bases (database views) creation and management. |
| `obsidian-markdown` *(v3.3.0)* | User says "obsidian syntax", "wikilink format", "callout syntax", "obsidian markdown", "write obsidian note" | Reference for correct Obsidian Flavored Markdown syntax. |
| `obsidian-rest` *(v3.6.1)* | User says "read note from obsidian", "write to obsidian", "list vault files", "open in obsidian", "obsidian api"; or any task requiring direct vault file read/write/open via REST API | Direct vault I/O via Local REST API (port 27123). Wraps `scripts/obsidian.py`: `open`, `read`, `write`, `append`, `list`, `tags` subcommands. Token stored in `~/.claude/.obsidian-token`. |
| `turboapi` *(v3.6.0)* | Any question about TurboAPI; code containing `from turboapi import` or `from dhi import BaseModel`; requests to migrate from FastAPI; dhi models, turbopg, turbonet, Zig HTTP, high-performance Python API; `/turboapi --route`, `--db`, `--migrate`, `--build`, `--test`, `--perf` | Expert knowledge base + scaffolder for TurboAPI v1.0.27+ (FastAPI-compatible, Zig HTTP core, dhi models, TurboPG). Covers install, migration, dhi models, handler classification, caching, security, TurboPG, observability, architecture. |

### 14.2 Global Skills — Group B (MUST surface to user)

| Skill | Trigger | Role |
|---|---|---|
| `loop` | User wants recurring/interval execution | Recommend in final response. Orchestrator does NOT dispatch mid-pipeline. |
| `schedule` | User wants time-scheduled/cron automation | Recommend in final response. |
| `airflow-log-parse` *(v2.8.0)* | User pastes an Airflow task failure log | Surface as recommendation when Airflow logs appear. Pure deterministic parser — outputs structured JSON `{error_class, task_id, run_id, traceback}`. No routing, no diagnosis. Routing stays with orchestrator (§16.5). |

### 14.3 Local Skill Discovery

Run first during skill check:

```
Does .claude/commands/ exist in current project cwd?
  YES → list all files; each filename (without extension) is an invocable local skill.
        Match task intent against local skill names → invoke immediately (treat as Group A).
  NO  → skip, proceed to Group A.
```

### 14.4 Precedence

**Local skill match > Group A skill > Group B surface > specialist dispatch.**

If any skill matches anywhere, it MUST be used. No fallthrough to specialists.

### 14.5 Skill vs Agent — Why the Distinction Matters

**Skills** are deterministic reviewed procedures; **agents** are probabilistic reasoning processes. Prefer skills where both apply.

---
