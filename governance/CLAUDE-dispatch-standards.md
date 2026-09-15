---
title: "CLAUDE-dispatch-standards.md — §4, §7, §11, §12 Agent Dispatch Standards"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §4, §7, §11, §12. §12.1 brief template and §7.1 mass-dispatch rule are inlined into §2.4 Self-Check for session-start self-containment.

---

## 4. Task Classification

Classify after Wave 0 returns.

### 4.1 Classification Matrix

| Class | Criteria | Pipeline | Typical Duration |
|---|---|---|---|
| **Trivial** | Non-code file, mechanical substitution, no logic or judgment | Orchestrator direct Edit | &lt;30s |
| **Standard** | Code change, 1–5 files, single domain, known scope | Standard Pipeline | 2–10 min |
| | *[DATA-WORK] subclass:* new DAG, new transform, incremental pipeline change | Standard + [DATA-WORK] flag | 2–10 min |
| **Complex** | Multi-file, cross-domain, or architectural impact | Complex Pipeline | 10–45 min |
| | *[DATA-WORK] subclass:* new pipeline service, cross-domain schema, orchestrator migration | Complex + [DATA-WORK] flag | 10–45 min |
| **Critical** | Security, production, data migration, or breaking change | Critical Pipeline | 30 min – several hours |

### 4.2 Classification Rules

- **When in doubt, escalate the class.** Underclassifying is strictly more dangerous than overclassifying.
- **A code file is never Trivial.** Even a one-line code change is Standard (minimum).
- **Any change touching auth, secrets, production config, data migration, or public API surface is Critical.** No exceptions.
- **A documentation change that changes behavior semantics (e.g., changes to this CLAUDE.md §1 or §3) is Complex, not Standard.**

### 4.3 Re-classification

If, during pipeline execution, a specialist discovers the task is bigger than initially classified:

1. Pause the current pipeline.
2. Announce reclassification: *"Reclassifying from Standard → Complex. Reason: discovered cross-service impact."*
3. Restart at Wave 0 of the new class (existing Wave 0 output may be reused if still fresh).

---

## 7. Parallel Execution Strategy

### 7.1 Mass Dispatch Rule

**When N independent items exist, dispatch N agents simultaneously in one message.**

If the plan produces 11 tasks with no inter-dependencies — dispatch 11 agents at once. The orchestrator never processes independent items one by one.

```
❌ Wrong:   analyze app-1 → wait → analyze app-2 → wait → ... → analyze app-11
✅ Correct: dispatch all 11 agents at once → wait for all → synthesize results
```

**Sequential execution is permitted only when agent B has a strict data dependency on agent A's output.** If no dependency exists, parallel is mandatory.

Before each dispatch, ask: *"Which of these tasks are independent of each other?"* All independent tasks go out in one message.

### 7.2 Wave Pattern Rules

- **Within a wave:** All agents dispatched in a single message (true parallel).
- **Between waves:** Wait for ALL agents in wave N before dispatching wave N+1.
- **Dependency test:** Can agent B start without agent A's output? Yes → same wave. No → separate waves.

### 7.3 Always-Parallel Pairings

- `context-manager` + `prompt-engineer` → Wave 0 of every pipeline.
- `Plan` + `Explore` + `architect-reviewer` (existing-patterns audit) → Complex/Critical Wave 1.
- `architect-reviewer` + `code-reviewer` → Complex pipeline gates.
- `documentation-expert` + `api-documenter` → always parallel when both apply.
- `runtime verification` + `test-engineer` → Critical K9.
- N implementation agents with non-overlapping file scopes → always parallel.

### 7.4 Never-Parallel Pairings

- Agents writing to the same file.
- Implementation agent + its reviewer (reviewer needs finished output).
- `Plan` + implementation agents (`Plan` output is required input).
- `architect-reviewer` + `code-reviewer` in Critical pipeline (sequential by design — structural issues caught first).
- Any wave N+1 agent before all wave N agents have returned.

### 7.5 Background Dispatches

`context-manager` save-at-end is the canonical background dispatch (`run_in_background: true`) — it must not block the user-facing response.

Other agents may be background-dispatched only when their output is non-blocking and the orchestrator has independent foreground work.

---

## 11. Context Management Protocol

`context-manager` is called at start and end of every pipeline. **11.1 Wave 0 retrieval** (parallel with `prompt-engineer`): receives task description + project path; returns prior decisions, active work streams, blockers, relevant patterns.

### 11.2 Pipeline End — Save

Always dispatched with `run_in_background: true` (does not block final response).

**Standard/Complex save includes:**
- Decisions made + rationale.
- Agents dispatched + what each produced.
- Files created/modified.
- Unresolved items, TODOs, follow-up tasks.
- Integration points or API contracts changed.
- Risks or known limitations discovered.

**Critical save additionally includes:**
- Risk assessment summary.
- Rollback procedure with exact commands/steps.
- Every gate outcome (pass/fail + evidence).

### 11.3 wiki_worthy Flag

The orchestrator MAY set `wiki_worthy: true` in the `context-manager` pipeline-end dispatch brief. When set, `context-manager` will — after saving the memory snapshot — also file the session as a structured wiki note in `/Users/isal/.claude/wiki/` (see context-manager.md Wiki Integration for the exact write contract).

**When to set `wiki_worthy: true`:**
- The pipeline produced a non-obvious architectural decision that future tasks will need to rediscover.
- A new pattern, constraint, or integration contract was established that spans projects or sessions.
- A significant debugging root cause was found that would prevent repeated investigation.
- The task resolved a long-standing ambiguity in system design.

**When NOT to set `wiki_worthy: true`:**
- Routine code changes with no cross-session carry-over value.
- Trivial pipeline class (mechanical substitutions).
- The session is a continuation with no new decisions — only execution.
- The content duplicates an existing wiki page (check index.md before setting the flag).

**Default is absent (no wiki write).** The orchestrator must make an explicit, reasoned judgment. Setting `wiki_worthy: true` on every pipeline degrades the wiki's signal-to-noise ratio — treat it as a scarce resource.

### 11.4 Memory Hygiene

- **Do not** dump raw file contents into memory — use pointers to repo paths.
- **Do not** record transient debug logs — summarize the outcome instead.
- **Do not** persist PII or secrets (see §10).
- **Update stale entries** rather than accumulating duplicates.

---

## 12. Agent Dispatch Standards

Every dispatch MUST include all 7 fields.

| # | Field | Purpose |
|---|---|---|
| 1 | **Task** | Exact description from `Plan` or `prompt-engineer` output |
| 2 | **Context** | Relevant portion of `context-manager` output |
| 3 | **Inputs** | Files, prior agent outputs, or data the agent needs |
| 4 | **Expected output** | What the orchestrator expects to receive back |
| 5 | **Constraints** | Scope boundaries — what the agent must NOT touch |
| 6 | **Confidence check** | Explicit instruction to research first if uncertain (Law 7) |
| 7 | **Success criteria** | Definition of done for this dispatch *(new in v2.0)* |

### 12.1 Brief Template

```
Task:          <one-sentence imperative>
Context:       <3–5 lines of relevant prior state>
Inputs:        <files / prior outputs / data>
Expected:      <exact shape of expected return>
Constraints:   <what NOT to touch / forbidden deviations>
Confidence:    If any part is uncertain, research before answering.
               Use [Explore / context7 / general-purpose] for evidence.
Success:       <measurable completion criterion>
```

### 12.2 Anti-Patterns in Briefs (see §19 for full list)

- "Fix this" with no context → triggers guesswork.
- "Based on your findings, implement it" → pushes synthesis onto the agent.
- "Be comprehensive" → unbounded → triggers over-engineering.

---

## 16.0 New Task or Continuation? (detailed expansion — stub in CLAUDE.md §16.0)

Before classifying a task per §4 / §16.1, the orchestrator must first determine whether the user message is a **new task** or a **continuation** of an active pipeline.

```
Is there an active pipeline in-flight?
  YES — did the orchestrator issue a PAUSE, AskUserQuestion, or gate-prompt in the immediately prior turn?
    YES + user replies with a short acknowledgment?
      → CONTINUATION. Route to active pipeline at the pending step. Reuse Wave 0 output. Do NOT re-dispatch context-manager or prompt-engineer.
    YES + user replies with a new imperative or question?
      → Ambiguous. Apply §3: "Never proceed on ambiguity." Clarify: "Is this a response to the PAUSE, or a new task?"
    NO (no pending step in prior turn)?
      → Treat as new task. Go to §16.1.
  NO (no active pipeline)?
    → New task. Go to §16.1.
```

### Continuation routing rules

| Signal | Classification |
|---|---|
| ya / ok / yes / lanjut / proceed / go (after PAUSE) | Continuation |
| no / batal / stop / abort (after PAUSE) | Continuation — abort path |
| noted / thx / thanks / makasih | Continuation — acknowledge |
| halo / hi / hello (no imperative) | Conversational — no pipeline needed |
| [imperative verb] + [file/library] (any length) | New task |
| [question] about code / system / library | New task (Law 7 — research first) |
| Length > 4 tokens with no active pipeline | New task |

### Why this matters

Without this check, CLAUDE.md Law 0 ("Wave 0 for every task") would re-run `context-manager ∥ prompt-engineer` on every "ya" — burning tokens and introducing an unnecessary delay between a PAUSE presentation and the pipeline's next step. The carve-out is not an exception to Law 0; it is the recognition that Law 0 applies to *tasks*, not to every keystroke.
