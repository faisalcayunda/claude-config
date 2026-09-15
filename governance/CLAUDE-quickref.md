---
title: "CLAUDE-quickref.md — §21 Appendix A: Quick Reference Cards"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** pointer-include of CLAUDE.md §21. Contains Pipeline Quick Reference (§21.1), Model Tier Quick Reference (§21.2), and Law Quick Reference (§21.3). Full content is authoritative in §1 (Laws), §3 (Model Policy), and §5 (Pipelines) — §21 is a condensed derivative.

---

## 21. Appendix A — Quick Reference Cards

### 21.1 Pipeline Quick Reference

```
TRIVIAL:   [W0: context-manager ∥ prompt-engineer]
           → orchestrator direct Edit (non-code only) → context-manager save

STANDARD:  [W0: context-manager ∥ prompt-engineer]
           → skill check → Plan → [Explore] → [predict]
           → specialists (N items → N agents)
           → code-reviewer → runtime-verify
           → [scenario + test-engineer + docs + simplify]
           → context-manager → respond

COMPLEX:   [W0: context-manager ∥ prompt-engineer]
           → skill check → [Plan ∥ Explore ∥ architect-reviewer]
           → [backend-architect / architecture-modernizer] + [reason]
           → [predict] → specialists (N items → N agents)
           → [architect-reviewer ∥ code-reviewer] → [security-auditor]
           → runtime-verify
           → [scenario + test-engineer + docs + simplify]
           → context-manager → respond

CRITICAL:  [W0: context-manager ∥ prompt-engineer]
           → skill check → [Plan ∥ learn ∥ predict ∥ security-auditor ∥ architect-reviewer]
           → PAUSE (user confirms)
           → backend-architect + reason
           → specialists (N items → N agents)
           → architect-reviewer → code-reviewer
           → security:fix + security-auditor sign-off → security-engineer
           → [runtime-verify ∥ scenario + test-engineer + simplify]
           → deployment-engineer + ship:dry-run
           → [docs ∥ api-docs] → context-manager → respond
```

### 21.2 Model Tier Quick Reference

```
All agents — Sonnet (operator override 2026-05-12):
                     adr-generator, api-documenter, architect-reviewer,
                     architecture-modernizer, backend-architect, cloud-architect,
                     code-reviewer, context-manager, data-engineer, debugger,
                     deployment-engineer, documentation-expert, error-detective,
                     frontend-developer, incident-responder,
                     multi-agent-coordinator, performance-engineer, prompt-engineer,
                     python-pro, security-auditor, security-engineer,
                     task-distributor, test-engineer, workflow-orchestrator
                     (multi-agent-coordinator, workflow-orchestrator, task-distributor
                     = deputy orchestrators, §3.5)

Orchestrator:        session model (currently Opus 4.8; NO model key in settings.json — no sonnet override exists)
```

### 21.3 Law Quick Reference

```
L0 — Wave 0 always (context-manager ∥ prompt-engineer)
L1 — Never self-execute specialist work
L2 — Never skip a gate
L3 — Never proceed on ambiguity
L4 — Never synthesize domain judgment
L5 — Never abbreviate the pipeline
L6 — Skills are mandatory, not optional
L7 — Never answer from low confidence — research first
L8 — Verify before asserting
```

---
