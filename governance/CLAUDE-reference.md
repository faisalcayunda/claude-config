---
title: "CLAUDE-reference.md — §20 Glossary + §22 Version History"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §20 (Glossary) and §22 (Version History). Change control per §0.4.

---

## 20. Glossary

| Term | Definition |
|---|---|
| **Agent** | An LLM-backed specialist dispatched via the `Agent` tool; has its own system prompt and tool access. |
| **Gate** | A mandatory verification checkpoint that must be explicitly passed before the pipeline proceeds. |
| **Orchestrator** | The top-level Claude Code session, running on the user-selected session model (currently Opus 4.8; no `model` key in settings.json). Coordinates; may self-execute small/verification work when delegating costs more than it saves (see Enforcement Reality in CLAUDE.md). |
| **PAUSE** | A pipeline checkpoint requiring explicit user confirmation before proceeding. |
| **Pipeline** | The sequence of waves and gates for a task class (Trivial/Standard/Complex/Critical). |
| **Skill** | A reviewed, invocable procedure — global (`~/.claude/skills/`) or local (`.claude/commands/`). Law 6 gives skills precedence over specialists. |
| **Specialist** | A domain-expert agent (e.g., `python-pro`, `code-reviewer`). |
| **Tier** | Model assignment category. Tier 1 = Opus, Tier 2 = Sonnet, Tier 3 = Situational. |
| **Trivial** | Task class for mechanical non-code substitutions; only class where orchestrator may direct-Edit. |
| **Wave** | A set of agents dispatched simultaneously and waited on as a group. |
| **Wave 0** | `context-manager` ∥ `prompt-engineer` — mandatory first wave of every pipeline. |

---

## 22. Version History

| Version | Date | Changes |
|---|---|---|
| **3.6.2** | 2026-05-20 | Structural noise reduction pass 2: @CLAUDE-agents.md removed from @-includes (−4,100 tokens/session); §13 replaced with compact inline roster (~150 tokens); §2.4 inline skill table removed (−550 tokens/session), replaced with forward ref to CLAUDE-skills.md §14.1; skill-optimization-ready.sh pre-check added (grep fast-exit when 0 scored runs). Total session-start savings this pass: ~4,650 tokens. |
| **3.6.1** | 2026-05-20 | Noise reduction pass 1: removed @CLAUDE-quickref.md + @CLAUDE-preamble.md + @RTK.md; §16.7 GROUP A/B table replaced with forward ref; version history compressed; lesson-capture hook path fixed; context-manager step 0 reverted (business-brain via SessionStart only); business-brain.md refreshed. |
| **3.6.0** | 2026-05-18 | `turboapi` skill created. Full repo ingestion: README, CLAUDE.md, 5 built-in skill files, docs/ARCHITECTURE.md, example_app.py. Knowledge base: 23 sections covering install, migration, dhi models, handler classification, caching, security, TurboPG, middleware, observability, SSE, TestClient, architecture. Scaffold modes: `--route`, `--db`, `--migrate`, `--build`, `--test`, `--perf`. Registered in CLAUDE-skills.md §14.1 + CLAUDE.md §2.4 + §16.7. |
| **3.5.0** | 2026-05-18 | Skill registry audit: data-quality-specialist + data-sla-sop + autoresearch Group A registered; save skill wiki path fixed; 2 ZIP artifacts deleted. |
| **3.4.0** | 2026-05-18 | Wiki-context-manager integration: Wave 0 reads hot.md+index.md+3 matched pages; wiki_worthy flag enables pipeline-end wiki promotion (5-step write sequence). |
| **3.3.0** | 2026-05-18 | claude-obsidian Path B (vault=~/.claude/); save skill + SessionStart/PostCompact hooks; all 24 agents documented as Sonnet per 2026-05-12 operator override. |
| **2.10.0** | 2026-05-18 | engineering-researcher skill: 10 domains, 12 templates, 217+ sources; Group A registered. |
| **2.9.0** | 2026-05-18 | data-engineer-boilerplate skill (4 stacks, generator-only); data-engineer agent Behavioral Constraints + Import Rules; WebSearch+WebFetch added to permissions. |
| **2.8.0** | 2026-05-06 | §16.0 continuation routing decision tree; /autoresearch:plan mandatory for Complex/Critical. Hook pre-classifier rejected (Laws 0/4/8 violations). |
| **2.7.0** | 2026-05-06 | Prose-trim pass: primary 41K→39.6K bytes; cluster −5.8%; v2.4–v2.6 history compressed. |
| **2.6.0** | 2026-05-06 | [DATA-WORK] pre-classification flag (strong/weak/counter-signal tiers); data-engineer hard-first routing for pipeline files. |
| **2.5.0** | 2026-04-20 | Deputy activation policy: user phrases advisory-only; must satisfy bounded-workflow merit criteria independently. |
| **2.4.0** | 2026-04-20 | Prose-trim pass; primary ≤40K chars target. |
| **2.3.0** | 2026-04-20 | Structural split into @-include cluster; §14.1 + §7.1 inlined into §2.4 Self-Check for self-containment. |
| **2.2.0** | 2026-04-20 | Governance cluster: primary + 9 sibling @-includes; primary 84.7K→54.6K chars. §12.1/§8.3/§10.3 inlined. |
| **2.1.0** | 2026-04-20 | +7 agents (cloud-architect, incident-responder, 3 deputies, performance-engineer, adr-generator); deputy orchestrator framework (§3.5, §13.10, §16.5a). |
| **2.0.0** | 2026-04-20 | Major restructure: §0–§22 added; Law 8 (Verify before asserting); Opus/Sonnet tier split; Success Criteria as 7th brief field. |
| **1.x** | pre-2026-04-20 | Original "World-Class Orchestration System" — 8-law framework, 4-class pipeline, agent registry, autoresearch toolkit. |
