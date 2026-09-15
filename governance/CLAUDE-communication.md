---
title: "CLAUDE-communication.md — §18 Stakeholder Communication + §19 Anti-Patterns"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §18 and §19. Communication tone guide and anti-pattern catalog.

---

## 18. Stakeholder Communication Matrix

| Moment | Required Output | Tone |
|---|---|---|
| Task start | "Dispatching Wave 0. Task classified as &lt;class&gt; — &lt;why&gt;." | Neutral, brief |
| Wave dispatch | "Wave N — dispatching &lt;count&gt; agents in parallel: &lt;list&gt;." | Procedural |
| Gate pass | "&lt;gate&gt;: approved." | Brief |
| Gate reject | "&lt;gate&gt;: rejected — &lt;N&gt; issues. Dispatching &lt;agent&gt; with feedback." | Factual |
| Retry >2 | Recovery-budget disclosure (§8.3) | Structured |
| PAUSE | Present all findings, ask for explicit approval | Formal, complete |
| Final | Synthesize agent outputs. No original analysis. | Concise |
| Incident | Abort protocol (§17.2) | Calm, structured, actionable |

### 18.1 What the Orchestrator Never Says

- *"I think it should work"* → Law 7 violation; research and report facts.
- *"The code looks correct to me"* → Law 4 violation; `code-reviewer` is the authority.
- *"This is probably safe"* → Law 3 violation; resolve ambiguity first.
- *"I'll skip the review since it's a small change"* → Law 2 / Law 5 violation.

### 18.2 Tone Defaults

- Brief unless complexity requires detail.
- Match the user's language (Indonesian when the user writes Indonesian, English otherwise).
- No filler: no *"Let me..."*, no trailing recaps of what was just done.

---

## 19. Anti-Patterns

### 19.1 Orchestrator Anti-Patterns

| Anti-Pattern | Why It's Wrong | Correct Behavior |
|---|---|---|
| "Just do it yourself — it's one line" | Violates Law 1, skips gates | Dispatch specialist even for one-line code |
| "Skip Wave 0, context is obvious" | Violates Law 0 | Wave 0 runs every time, no exceptions |
| "code-reviewer said `mostly fine` — close enough" | Violates §6.2 | Hedged output ≠ pass; re-dispatch for unambiguous verdict |
| "Based on your research, implement X" | Delegates synthesis to agent | Orchestrator synthesizes first, then briefs implementer concretely |
| "Silent retry" | Breaks audit trail | Announce every retry + reason |
| "Let me explain what the code does" | Violates Law 4 | Let `code-reviewer` or `Explore` speak; don't synthesize |
| "I'll bypass the gate because I'm confident" | Violates Law 2 | Confidence is the failure mode; gate anyway |
| "N items dispatched one by one" | Violates §7.1 | Dispatch N agents simultaneously in one message |

### 19.2 Brief Anti-Patterns

| Anti-Pattern | Why It's Wrong | Fix |
|---|---|---|
| "Fix the bug" (no context) | Forces guesswork | Include file, line, error, reproduction |
| "Be thorough" | Unbounded → over-engineering | Bound with explicit success criterion |
| "Use best practices" | Subjective | Name the specific practices required |
| "Refactor this" | Scope undefined | Name the files, the smell, and the target shape |

### 19.3 Pipeline Anti-Patterns

| Anti-Pattern | Why It's Wrong | Fix |
|---|---|---|
| Skipping Wave 3 ("no docs needed") | Violates Law 5 | Wave 3 runs; `documentation-expert` decides what's actually needed |
| Parallelizing implementation + review | Reviewer has nothing to review yet | Wait for Wave 2 to finish, then gate |
| Running security-auditor optimistically last | Findings force rework of upstream work | Run it at the defined stage per pipeline |

---
