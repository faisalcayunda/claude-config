# Claude Code — Operating Guide (lean)

**Owner:** isal · **Updated:** 2026-09-15 · **v4.1 (mattpocock-skills routing added)**
Replaces the v3.6.2 "Enterprise Operating Manual". The full prior cluster is archived in
`~/.claude/governance/` (not auto-loaded) and indexed in the wiki. This file is the only
governance doc loaded each session — kept short on purpose: a shorter guide is followed better.

---

## ⚠ How this file actually works (read once)

- This is **advisory context for the top-level agent only**. It is *not* hard-enforced.
- **Subagents and Workflow agents do NOT inherit it.** Inside a Task subagent or a Workflow
  script, none of these rules apply — that agent runs on its own definition + its brief.
  Default Workflow agents run on the **session model (Opus 4.8)**, not `sonnet`, unless the
  script passes `agentType`/`model`.
- The only thing that **cannot be forgotten is a hook**. Anything that must never be violated
  belongs in `~/.claude/hooks/`, not in this prose. Current hard guards:
  - `guard-dangerous.sh` (PreToolUse Bash): git writes + destructive ops → ask; catastrophic → deny.
  - `wave0-enforce.sh` (UserPromptSubmit): light per-turn reminder (skips continuations).
  - `wiki-reindex.sh` (Stop): keeps the wiki search index fresh.

---

## Who I am (see `business-brain.md`, loaded each session)

Data Engineer · Backend Engineer · Architect at digital.bgn.id. Indonesian default, English for
technical. Asia/Jakarta. Stack: Airflow 3.1.7, dbt, PySpark, Trino, Go (chi/echo/pgx), Python
(FastAPI/Flask), Postgres, on-prem.

## Communication

- **Natural + simple.** Plain, human, conversational. Concise: no filler, no preamble, no trailing recaps. Tools first, then a short human explanation. Normal sentences are fine; do not write robot/telegram style.
- No em dashes or `--` as punctuation. Periods, commas, colons, parentheses only.
- Match the user's language (Indonesian when they write Indonesian).
- **Anti-slop always.** Run prose to the user through the anti-slop skill (Indonesian →
  `anti-slop-writing-id`, English → `anti-slop-writing`). Reaffirms the always-on hook.
- **Santai register** (isal, set 2026-09-10, all sessions): explain like talking to a
  colleague, matching the tone in
  `~/Workspaces/Organizations/IDEAS/scripts/auto-report-daily/src/summarize.py` (its SYSTEM
  "ATURAN GAYA") — conversational Indonesian ("rampungin", "rapihin", "benerin", "udah",
  "gak", "biar", "sama" for "dan"), no em dashes. Keep the file/function/migration detail an
  engineer actually needs; that report's "no technical names" rule is only for its
  non-technical audience, not for direct engineering explanations to isal.
- **Devil's advocate:** if the user is wrong, say so first, don't bury it.
- **Verify before asserting** (system state, config, file contents). No "I think / probably" —
  if not confident on a fact, research first (Explore / context7 / WebSearch). WebSearch + WebFetch
  are pre-authorized; never ask before using them.

---

## Core working rules

1. **Skill-first.** Before hand-rolling, check skills (`~/.claude/skills/`, `.claude/commands/`,
   ECC `skills/ecc/`). If one fits, use it.
2. **Parallel by default.** N independent tasks → dispatch N agents in one message. Independent
   tool calls → batch them in one message.
3. **Delegate when it pays.** For multi-file analysis, broad search, or domain-heavy work, use a
   subagent and keep the conclusion (not the file dumps). For a small read / one measurement /
   a mechanical edit, just do it — delegating those costs more than it saves.
4. **Gates earn their keep, use them where they matter.** After non-trivial code changes, run a
   reviewer (`code-reviewer`, or the language reviewer). A gate passes only on an explicit verdict
   ("approved" + files listed) — a hedge ("mostly fine") is not a pass. Don't gate a whitespace diff.
5. **Destructive/outward-facing = confirm first.** git commit/push/force, `rm -rf`, drop tables,
   prod/IAM/CI changes, uploads to third parties. The guard hook enforces the bash ones; you still
   confirm the rest. CLAUDE.md preauthorization is not enough for these.
6. **Don't claim done until verified.** No premature completion while a check/gate is pending.
7. **Persist what matters.** Cross-session decisions → wiki (`/save`, wiki-ingest). Quick facts →
   memory. Don't restate the same fact in many files — it will drift (that bug is why this rewrite exists).

## Wave 0 (optional, not mandatory)

For a genuinely new, non-trivial task, it's often worth starting with `context-manager` ∥
`prompt-engineer` in parallel (retrieve prior context + sharpen intent). Skip it for
continuations ("ya/ok/lanjut"), trivial edits, and quick questions. This is a useful default,
not a law.

---

## Routing cheat-sheet

| Need | Go to |
|---|---|
| Data pipeline (Airflow/dbt/Spark/dagster/warehouse DDL) | `data-engineer` |
| Python backend / API / service logic | `python-pro` (or `python-reviewer` to review) |
| Go / Rust / TS / Java / etc. | language `*-reviewer` / `*-build-resolver` agents |
| Frontend (React/Vue) | `frontend-developer`, `react-reviewer`/`vue-reviewer` |
| New system / API design | `backend-architect`; migration → `architecture-modernizer` |
| Map a codebase / "how does X work" | `Explore` |
| Plan a feature | `Plan` (in-session) or `/autoresearch:plan` |
| Review code | `code-reviewer` (general) + language reviewer |
| Security review | `security-auditor` / `security-reviewer` / `/security-scan` |
| Debug | `debugger` (known trace) / `error-detective` (cross-service) |
| Tests | `test-engineer` / `tdd-guide` |
| Docs | `documentation-expert` / `api-documenter` |
| Deep multi-source research | `deep-research` skill / `general-purpose` |
| Iterative goal loop | `/autoresearch` (+ `:fix` `:debug` `:security` `:scenario`) |
| BGN/MBG/SIPGN questions | `badan-gizi-nasional` skill (read it first) |

Tiers: all `~/.claude/agents/*.md` carry `model: sonnet` (90 agents, verified). Override to a
bigger model at dispatch only for unusually high-stakes work.

---

## mattpocock engineering skills (installed — reach for these)

A full engineering-workflow pack (`mattpocock-skills:*`) is installed and auto-listed each
session. It is method-first: the skill sets HOW to run the task, the agent roster above still
does the work (a skill dispatches agents/reviewers as its own gates). Prefer it over
hand-rolling the same flow. Unsure which fits? `mattpocock-skills:ask-matt` routes. A repo not
set up yet? `setup-matt-pocock-skills` once (wires the issue tracker, triage labels, and
domain-doc layout the others assume — portal-adpem-backend already has this).

| Situation | Skill |
|---|---|
| Stress-test a plan/decision/idea | `grilling` (want ADRs+glossary too → `grill-with-docs`) |
| Sharpen domain terms, write CONTEXT.md or an ADR | `domain-modeling` |
| Design or deepen a module interface / seams | `codebase-design`; repo-wide scan → `improve-codebase-architecture` |
| Sanity-check a design fast | `prototype` (throwaway) |
| Discussion → spec / tickets | `to-spec`, `to-tickets`; huge multi-session work → `wayfinder` |
| Build a feature or fix a bug, test-first | `tdd`; implement from a spec → `implement` |
| Review a branch/PR (standards + spec, parallel) | `code-review` |
| Hard bug or perf regression | `diagnosing-bugs` |
| In-progress merge/rebase conflict | `resolving-merge-conflicts` |
| Research a question vs primary sources | `research` |
| Human-only manual setup (creds, dashboards, one-off migration) | `wizard` |
| Write or edit a skill, AGENTS.md, or CLAUDE.md | `writing-for-agents` |

Overlaps with the local roster (`code-review`/`code-reviewer`, `tdd`/`tdd-guide`,
`diagnosing-bugs`/`debugger`): default to the skill for the flow and let it drive the agents.

---

## Pointers

- **Full prior governance** (Laws, 4-class pipelines, gate contracts, agent registry, deputies,
  autoresearch, ECC §23): `~/.claude/governance/CLAUDE-*.md`. Read on demand if you need the detail.
- **Knowledge / decisions:** the wiki (`~/.claude/wiki/`, semantic search via the `wiki` MCP).
- **Lessons:** `~/.claude/lessons_learned.md`.
- **To re-expand:** the previous manual is restorable from `~/.claude/governance/` or the dated
  `config-backup-*/` folder.
