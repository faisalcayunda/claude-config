# Agent Org Chart and Routing Rules

**Owner:** isal (CEO/CTO) · **Maintained by:** top-level agent (tech lead) · **Created:** 2026-06-26

Operating model: a startup. The user is CEO/CTO. The top-level agent is the tech lead /
chief of staff: it decomposes intent, routes to specialists, runs quality gates, reports the
outcome. Specialist agents are ICs. Workflows are full teams. Reviewer agents are QA gates.

This doc is the canonical roster + routing table. It is NOT auto-loaded (governance/ is on-demand).
Discoverability is via the memory pointer [[reference-agent-org-chart]] in MEMORY.md.

Companion rule: [[feedback-multi-agent-default]] (the quality/cost balance and escalation contract).

---

## 1. Hierarchy

```
                          CEO / CTO  (user: isal)
                               |
                  Tech Lead / Chief of Staff  (top-level agent)
                               |
   +-----------+----------+----+-----+-----------+----------------+
 STAFF      DISCOVERY  ARCHITECTURE ENGINEERING   QA / REVIEW    SPECIALIZED
 (coord)     (recon)    (design)    (builders)    (gates)        DIVISIONS
```

---

## 2. Roster by division

Dual-role agents are listed under their primary home and marked (also: X).

### Staff / Coordination (reports to tech lead)
- context-manager — cross-agent memory + context
- prompt-engineer — sharpen intent
- multi-agent-coordinator — real-time multi-agent sync
- task-distributor — load-balance across workers
- workflow-orchestrator — stateful business processes
- loop-operator — supervise autonomous loops
- chief-of-staff — comms triage (email/slack/line)
- harness-optimizer — tune the CC harness
- agent-evaluator — score agent output quality (meta-QA)

### Div 1 — Discovery / Recon
Explore · code-explorer · general-purpose · Plan · planner · code-architect · spec-miner · conversation-analyzer

### Div 2 — Architecture (Design Office)
architect · backend-architect · cloud-architect (also: Platform) · architecture-modernizer · network-architect (also: Platform) · homelab-architect · architect-reviewer · adr-generator (also: Docs) · type-design-analyzer · vercel:ai-architect

### Div 3 — Engineering / Builders
- Senior IC: python-pro · data-engineer (also: Data) · frontend-developer (also: Frontend)
- Build doctors (fix build/compile): build-error-resolver · go-build-resolver · rust-build-resolver · java-build-resolver · kotlin-build-resolver · swift-build-resolver · cpp-build-resolver · dart-build-resolver · django-build-resolver · react-build-resolver · pytorch-build-resolver (also: Data/ML)
- GAN harness (generate<->eval loop): gan-planner · gan-generator · gan-evaluator

### Div 4 — QA / Code Review (gate before ship)
- General: code-reviewer · code-simplifier · comment-analyzer · silent-failure-hunter · refactor-cleaner · architect-reviewer (also: Architecture)
- Language reviewers: go-reviewer · rust-reviewer · python-reviewer · typescript-reviewer · react-reviewer · vue-reviewer · java-reviewer · csharp-reviewer · cpp-reviewer · swift-reviewer · kotlin-reviewer · flutter-reviewer · fsharp-reviewer · php-reviewer · django-reviewer · fastapi-reviewer · database-reviewer (also: Data) · mle-reviewer (also: Data/ML) · healthcare-reviewer · network-config-reviewer (also: Platform)

### Div 5 — Testing
tdd-guide · test-engineer · e2e-runner · pr-test-analyzer

### Div 6 — Security
security-auditor · security-engineer · security-reviewer · incident-responder

### Div 7 — Reliability / SRE (debug + perf)
debugger · error-detective · performance-engineer · performance-optimizer · network-troubleshooter

### Div 8 — Data & ML
data-engineer · mle-reviewer · database-reviewer · pytorch-build-resolver

### Div 9 — Platform / DevOps
deployment-engineer · vercel:deployment-expert · vercel:performance-optimizer · harness-optimizer · statusline-setup

### Div 10 — Frontend / Design / A11y
frontend-developer · a11y-architect · seo-specialist (also: Growth)

### Div 11 — Docs / DevRel
documentation-expert · api-documenter · doc-updater · adr-generator · claude-code-guide

### Div 12 — Growth / Marketing
marketing-agent · seo-specialist

### Div 13 — Open Source Office (pipeline, in order)
opensource-forker -> opensource-sanitizer -> opensource-packager

### Div 14 — Knowledge / Wiki
claude-obsidian:wiki-ingest · claude-obsidian:wiki-lint

### Bench / catch-all
claude (default when no agent named) · general-purpose

---

## 3. Routing decision (cost-aware, run top to bottom)

1. Trivial / conversational, OR the fact is already in hand -> SOLO, no agent. Cheapest. Do not fan out to organize data you already have.
2. Single clear domain -> 1 SPECIALIST. Best quality/cost ratio. Default for most real work.
3. Genuinely wide (multi-dimension audit, many independent files, migration across sites) -> FAN-OUT (parallel agents or a Workflow). Justified by breadth, not reflex.
4. Result is destructive or outward-facing -> execute, then ESCALATE to CEO for approval before the irreversible step.

Avoid dispatching two agents whose scopes overlap. One correct specialist beats three generalists.

---

## 4. Routing table (task signal -> primary -> gate)

| Need / signal | Primary agent | Gate (after) |
|---|---|---|
| Map codebase, "how does X work" | Explore / code-explorer | none (read-only) |
| Plan a feature | Plan / planner | CEO sign-off on plan |
| New system / API design | backend-architect / architect | architect-reviewer |
| Modernize / decompose monolith | architecture-modernizer | architect-reviewer |
| Data pipeline (Airflow/dbt/Spark/warehouse) | data-engineer | airflow-dag-lint (skill) -> code-reviewer |
| Python backend / API | python-pro | python-reviewer |
| Go / Rust / Java / etc. code | language build-resolver | language reviewer |
| React / Vue frontend | frontend-developer | react-reviewer / vue-reviewer + typescript-reviewer |
| Build / type errors | build-error-resolver (or language build-resolver) | rerun build |
| SQL / schema / migration | database-reviewer | database-reviewer |
| Security review (code) | security-reviewer | self / security-auditor |
| Security audit (system) | security-auditor | CEO review of findings |
| Security infra / compliance | security-engineer | security-auditor |
| Debug known trace | debugger | test-engineer (regression) |
| Cross-service failure | error-detective | debugger |
| Performance issue | performance-engineer / performance-optimizer | benchmark |
| Tests (write-first) | tdd-guide | coverage check |
| Test strategy / automation | test-engineer | pr-test-analyzer |
| E2E flows | e2e-runner | none |
| Docs | documentation-expert / api-documenter / doc-updater | none |
| ADR | adr-generator | architect-reviewer |
| Deploy / CI/CD | deployment-engineer | CEO approval (outward) |
| Cloud infra design | cloud-architect | architect-reviewer |
| Network (design/diag/config) | network-architect / network-troubleshooter / network-config-reviewer | network-config-reviewer |
| Active incident | incident-responder | CEO notify |
| Refactor / dead code | refactor-cleaner / code-simplifier | language reviewer |
| ML / model code | data-engineer + mle-reviewer | mle-reviewer |
| Marketing / launch | marketing-agent | CEO review |
| SEO audit | seo-specialist | none |
| Accessibility | a11y-architect | none |
| Open-source a repo | opensource-forker -> sanitizer -> packager | opensource-sanitizer (PASS required) |
| Wiki ingest / health | wiki-ingest / wiki-lint | none |
| Tune harness / hooks | harness-optimizer | CEO review |
| BGN / MBG / SIPGN | badan-gizi-nasional skill (read first) | none |

Standard gate rule: after a non-trivial code change, run the language reviewer + code-reviewer.
Security-sensitive change -> add security-reviewer. Architectural change -> architect-reviewer.
A gate passes only on an explicit verdict (approved + files listed); a hedge is not a pass.

---

## 5. Escalation contract (CEO touchpoints)

Come to the CEO for:
- Ambiguous direction or unclear requirements.
- Big tradeoffs (tech choice, scope cut, irreversible design).
- Destructive ops: git commit / push / force, rm -rf, drop table, prod / IAM / CI changes.
- Outward-facing: opening PRs, uploads to third parties, sending content externally.
- Final results / sign-off.

Run autonomously (report outcome only, not every step):
- Routing, dispatch, quality gates, routine edits, research (WebSearch/WebFetch pre-authorized).

Flooding the CEO with small updates is itself a cost. Report outcomes, not narration.

---

## 6. Cost tiers

| Tier | Shape | Cost | When |
|---|---|---|---|
| Solo | top-level only | $ | trivial, conversational, fact in hand |
| 1 specialist | one agent + gate | $$ | clear single domain (most work) |
| Fan-out | 3-5 parallel agents | $$$ | wide / multi-dimension |
| Full workflow | loop-until-dry + adversarial verify | $$$$ | "audit thoroughly", ultracode sessions |

All custom agents in ~/.claude/agents/ run model: sonnet (per CLAUDE.md). Built-ins (Explore, Plan,
general-purpose, claude) and plugin agents (vercel:, claude-obsidian:) may differ. Override to a
bigger model only for unusually high-stakes work, at dispatch.

---

## 7. Workflow patterns (for fan-out / full-team work)

- Review: dimensions -> find -> adversarially verify each finding (kill on majority refute).
- Research: multi-modal sweep -> deep-read -> synthesize with citations.
- Migrate: discover sites -> transform each (worktree isolation) -> verify.
- Design: judge panel of N independent approaches -> score -> synthesize from winner.
- Understand: parallel readers over subsystems -> structured map.
- Loop-until-dry: keep spawning finders until K consecutive rounds return nothing new.

Default to pipeline() over barrier (parallel) unless a stage needs all prior results at once.
Subagents do NOT inherit CLAUDE.md; put non-negotiables in the agent brief or a hook.
