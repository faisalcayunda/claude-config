---
title: "CLAUDE-failure.md — §8 Failure Taxonomy & Error Recovery"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §8. §8.3 escalation template also inlined into §6.3 (CLAUDE-gates.md).

---

## 8. Failure Taxonomy & Error Recovery

### 8.1 Failure Classes

| Class | Symptom | First-line Response |
|---|---|---|
| **Transient** | Agent times out, network glitch, rate limit | Re-dispatch the same agent unchanged |
| **Underspec** | Agent returns asking for clarification | Augment brief and re-dispatch |
| **Gate Reject — First** | Reviewer finds specific issues | Dispatch impl agent with rejection feedback |
| **Gate Reject — Repeat (2+)** | Same issue flagged 2+ times | `/autoresearch:fix` — autonomous loop |
| **Runtime Break** | App fails to start / test fails | `/autoresearch:fix` (deterministic) or `/autoresearch:debug` (unknown source) |
| **Context Staleness** | Agent output references non-existent files/symbols | Re-dispatch `context-manager` to rebuild |
| **Agent Conflict** | Two agents produce incompatible outputs | `/autoresearch:reason` — adversarial refinement |
| **Cross-Service Bug** | Error spans services, no clear source | `/autoresearch:debug` before dispatching `debugger` |
| **Plan Drift** | Plan no longer matches discovered reality | Re-dispatch `Plan` with new context |
| **User Intent Drift** | Partway through, user clarifies different intent | Reclassify per §4.3, possibly restart |

### 8.2 Recovery Budget

- **Per gate:** 3 retry cycles max. After 3, escalate to user per §17.
- **Per pipeline:** >6 cumulative gate rejections → proactive user PAUSE.
- **Per session:** Unlimited, but document every retry in `context-manager` snapshot.

### 8.3 Escalation Template

```
⚠ Pipeline paused — recovery budget exceeded

Gate:         <gate name>
Cycles used:  <N> / 3
Attempts:
  1. <agent> returned: <summary>
  2. <agent> returned: <summary>
  3. <agent> returned: <summary>

Root cause hypothesis: <best-guess>
Options:
  (a) Retry with expanded scope
  (b) Switch to /autoresearch:debug for root cause
  (c) Manual intervention — user takes over
  (d) Abandon and roll back (see §17 for rollback)

How would you like to proceed?
```

---
