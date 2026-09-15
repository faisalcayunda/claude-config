---
title: "CLAUDE-incident.md — §17 Incident Response & Rollback"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §17. Covers mid-pipeline abort protocol, rollback semantics, and post-mortem templates.

---

## 17. Incident Response & Rollback

### 17.1 Definitions

- **Incident:** A pipeline failure that cannot be resolved within the normal retry budget (§8).
- **Rollback:** Returning the system to its pre-pipeline state.
- **Post-mortem:** Structured analysis of an incident.

### 17.2 Mid-Pipeline Abort Protocol

If the user interrupts or the orchestrator hits a hard failure:

1. **Stop dispatching.** Do not start new waves.
2. **Let in-flight agents finish** (their output may still be useful).
3. **Snapshot state** via `context-manager` — what was done, what was pending.
4. **Surface to user** with structure:

```
⚠ Pipeline aborted

Class:       <Trivial | Standard | Complex | Critical>
Last stage:  <stage ID>
Completed:   <list of done steps>
In-flight:   <list of running agents>
Pending:     <list of not-yet-started steps>
State:       <clean | partial changes | needs rollback>
Rollback:    <exact commands or manual steps, if needed>

How would you like to proceed?
```

### 17.3 Rollback for Critical Pipelines

Every Critical pipeline MUST produce a rollback plan at K12 containing:

- **Revert commands:** Exact git/infra/db commands to undo the change.
- **Verification steps:** How to confirm rollback succeeded.
- **Communication template:** What to say to stakeholders.
- **Time window:** How long the rollback is safe to execute (before data drift or dependent changes complicate it).

### 17.4 Post-Mortem Template

For any incident, produce:

```
# Post-Mortem: <short title>

**Date:** YYYY-MM-DD
**Classification:** <Standard | Complex | Critical>
**Duration:** Wave 0 → abort = N minutes
**Impact:** <what was affected>

## Timeline
- HH:MM — <event>
- HH:MM — <event>
- HH:MM — <resolution>

## Root Cause
<single sentence, then 2-3 line elaboration>

## What Went Wrong
- <contributing factor 1>
- <contributing factor 2>

## What Went Right
- <containment factor 1>
- <containment factor 2>

## Action Items
- [ ] Owner: isal — Due: YYYY-MM-DD — Item: <specific, measurable>
- [ ] Owner: isal — Due: YYYY-MM-DD — Item: <specific, measurable>

## Prevention Rule
<add to lessons_learned.md>
```

---
