---
title: "CLAUDE-ops.md — §9 Observability + §10 Security & Compliance Posture"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §9 and §10. §10.3 destructive-action boundary also inlined into §2.3.

---

## 9. Observability, Telemetry & Audit

### 9.1 What the Orchestrator Records

Pipeline **decision trail** captured by `context-manager` at pipeline end:

**Always recorded:**
- Wave 0 inputs and outputs (`prompt-engineer` refinement, `context-manager` retrieval).
- Classification and reason.
- Skills invoked (global + local).
- Every agent dispatched, in order, with task brief and return summary.
- Every gate: name, verdict, evidence.
- Every retry/rejection with the reason and the fix.
- Files created/modified with their new status.

**Critical-only additions:**
- PAUSE checkpoints and user confirmations (verbatim).
- Risk assessment before K3.
- Rollback plan at K12.
- All gate outcomes individually, pass or fail.

### 9.2 Telemetry Surface

- **Transcript:** Real-time observability surface.
- **`context-manager` snapshots:** Durable, cross-session surface.
- **`lessons_learned.md`:** Appended on correction/mistake (`~/.claude/hooks/lesson-capture-prompt.sh`).

### 9.3 Audit Queries the Orchestrator Must Be Able to Answer

Via `context-manager` retrieve, must answer on request:

- "What did we change in this session?"
- "Why did we choose X over Y?"
- "Which gate rejected what, and how did we fix it?"
- "What's the rollback plan for this Critical change?"

### 9.4 What is NOT Recorded

- Raw file contents (those live in the repo — `context-manager` only records pointers).
- Transient tool outputs (logged only by the CLI transcript).
- Private user data not directly relevant to the task.

---

## 10. Security & Compliance Posture

### 10.1 Secrets Discipline

- **Never** include a secret (API key, password, token, cert) in any user-facing text or agent brief.
- If an agent returns content that appears to include a secret, **redact before surfacing** and flag to the user.
- If the user pastes a secret, acknowledge receipt but **do not echo it back** in any subsequent message; do **not** persist it to `context-manager`.

### 10.2 PII & Sensitive Data

- Treat names, emails, addresses, and health/financial identifiers as sensitive unless explicitly told otherwise.
- Do not persist PII beyond task continuity needs.

### 10.3 Destructive Action Boundary

Destructive actions require **explicit, in-session user approval** — CLAUDE.md preauthorization is not sufficient:

- `rm -rf`, dropping tables, deleting branches/PRs.
- `git push --force` to any shared branch (especially `main`/`master`).
- Any action modifying shared CI/CD pipelines, IAM, or production config.

### 10.4 Third-Party Tool Uploads

Any upload to a third-party tool is a **disclosure event**. Before uploading:

1. Confirm the content contains no secrets or PII.
2. Inform the user what will be uploaded and where.
3. Wait for explicit approval.

### 10.5 Compliance Gates

Any task that triggers security-auditor or `/autoresearch:security` must produce a machine-readable finding list with severity. Critical/High findings **cannot** be deferred past the gate — they either fix or the pipeline stops.

### 10.6 Law Mapping

| Concern | Enforced By |
|---|---|
| No unauthorized code changes | Law 1 |
| No unsupervised destructive ops | §2.3 row 13, §10.3 |
| No claim without evidence | Law 7, Law 8 |
| No silent gate skip | Law 2 |
| No prompt-injection propagation | `prompt-engineer` Wave 0 + §10.1 redaction |

---
