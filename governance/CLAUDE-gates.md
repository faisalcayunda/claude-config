---
title: "CLAUDE-gates.md — §6 Quality Gates"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §6. §8.3 escalation template inlined into §2.4 Self-Check and §6.3. Extended reference.

---

## 6. Quality Gates

Gates are **non-negotiable checkpoints**. The orchestrator may not proceed past a gate until it is explicitly passed.

### 6.1 Gate Catalog

#### Gate: `code-reviewer`
- **Triggers:** Any code change, regardless of size.
- **Timing:** Standard — alone; Complex — parallel with `architect-reviewer`; Critical — sequential after `architect-reviewer`.
- **Rejection path:** Dispatch implementation agent with feedback → re-review. After 2+ rejections on the same issue: `/autoresearch:fix`.
- **Pass condition:** Explicit **approved** or equivalent assertion in the agent's final output.
- **Pass evidence:** Agent's text includes "approved," "LGTM," or equivalent, **and** lists the files reviewed.

#### Gate: `architect-reviewer`
- **Triggers:** New modules, new layers, cross-service changes, pattern changes.
- **Timing:** Complex — parallel with `code-reviewer`; Critical — sequential before `code-reviewer`.
- **Rejection path:** Back to `backend-architect` or `architecture-modernizer` → both gates re-run.
- **Pass condition:** Explicit **compliant** assertion covering SOLID, layer boundaries, and pattern consistency.

#### Gate: `security-auditor`
- **Triggers:** Auth, authorization, input validation, API surface, secrets, data access, crypto.
- **Timing:** After code gates pass.
- **Rejection path:** Back to implementation agent → re-implement → re-audit.
- **Pass condition:** Explicit **clear** or no unresolved issues at Critical/High severity.

#### Gate: Runtime Verification
- **Triggers:** Always, after all code gates pass.
- **Delegated to:** `general-purpose` or relevant specialist.
- **Must verify:** App starts, changed functionality works end-to-end, no regressions, all existing tests pass.
- **Rejection path:** `/autoresearch:fix` (deterministic errors) or `/autoresearch:debug` (unknown source).
- **Pass condition:** All checks green; verifier names each check and its result.

#### Gate: `test-engineer` Coverage
- **Triggers:** New features, refactors, new endpoints.
- **Must verify:** Coverage thresholds met, critical paths tested, no untested edge cases.
- **Rejection path:** Back to the relevant implementation agent to add missing tests → re-verify.

#### Gate: `simplify`
- **Triggers:** Any implementation wave that produces changed code.
- **Timing:** Standard/Complex — Wave 3 parallel with `test-engineer`, `documentation-expert`; Critical — K9 parallel with runtime verification, `/autoresearch:scenario`, `test-engineer`.
- **Purpose:** Reviews changed code for reuse opportunities, quality improvements, and efficiency gains; fixes issues found in the same pass.
- **Pass condition:** `simplify` returns no further improvements or explicitly confirms the code is clean.
- **Complementary to `code-reviewer`:** simplify = efficiency/reuse; code-reviewer = correctness/maintainability. Run in parallel, not in sequence.

### 6.2 Gate Evidence Requirements

A gate is considered **passed** only when the agent's output contains:

1. An unambiguous pass verdict (`approved`, `clear`, `compliant`, `no issues`).
2. A list of what was checked (files, endpoints, surfaces, paths).
3. A statement of scope coverage (e.g., "reviewed all 4 changed files").

Any output missing #1 or containing hedges (`mostly fine`, `probably OK`) is treated as **not passed** and triggers a re-dispatch with clarifying feedback.

### 6.3 Retry Budget

- **Per gate:** Max 3 rejection cycles. After the 3rd, pause and escalate per §17.
- **Per pipeline:** No hard cap, but >6 total gate rejections triggers orchestrator-initiated PAUSE for user review.

> **§8.3 Escalation template (inlined here — extended failure taxonomy in [CLAUDE-failure.md](./CLAUDE-failure.md)):**
> ```
> ⚠ Pipeline paused — recovery budget exceeded
>
> Gate:         <gate name>
> Cycles used:  <N> / 3
> Attempts:     <list>
> Root cause hypothesis: <best-guess>
> Options: (a) Retry (b) /autoresearch:debug (c) Manual takeover (d) Rollback
>
> How would you like to proceed?
> ```

---
