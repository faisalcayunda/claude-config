---
title: "CLAUDE-autoresearch.md — §15 Autoresearch Toolkit"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §15. Flag cheat-sheet for pipeline-critical commands in §5.7.

---

## 15. Autoresearch Toolkit

Autonomous loop commands. **Pattern:** Modify → Verify → Keep/Discard → Repeat until metric achieved or N iterations complete. Amplify pipeline stages — do not replace agents. Never run in background.

### 15.1 Integration Map

| Command | Standard | Complex | Critical | Activation Trigger |
|---|---|---|---|---|
| `/autoresearch:plan` | Optional (after W0) | **Mandatory** (after W0, before C1) | **Mandatory** (after W0, before K1 Wave) | Exit criteria undefined — Standard: optional; Complex/Critical: mandatory |
| `/autoresearch:predict` | Optional (S3) | Optional (C3) | **Mandatory** (K1) | High-risk or unfamiliar change |
| `/autoresearch:learn` | Optional (S2) | Optional (C1) | **Mandatory** (K1) | Deep mapping + doc generation |
| `/autoresearch:reason` | — | Optional (C2) | **Mandatory** (K3) | Architecture decision or agent conflict |
| `/autoresearch:scenario` | Optional (S7) | Optional (C8) | **Mandatory** (K9) | Before `test-engineer` writes tests |
| `/autoresearch:debug` | On failure | On failure | On failure | Unknown bug, 2+ debugger cycles failed |
| `/autoresearch:fix` | Gate reject ×2 | Gate reject ×2 | Gate reject ×2 | Deterministic errors, zero-to-zero loop |
| `/autoresearch:security` | — | Optional (C6) | **Mandatory** (K7) | Auth/data/API surface changed |
| `/autoresearch:ship` | — | — | Optional (K10) | Production deployment |
| `/autoresearch` core | Any | Any | Any | Any measurable iterative goal |

### 15.2 Command Reference

#### `/autoresearch` — Core Loop
**Stage:** Any with a measurable goal. **Pattern:** Modify → Verify → Keep/Discard → Repeat. **Required:** `Goal` · `Scope` · `Metric` · `Verify` · `Guard` (optional) · `Iterations: N`.

```
/autoresearch
Goal: bring test coverage above 80%
Scope: src/**/*.py
Metric: coverage % from pytest-cov
Verify: pytest --cov=src --cov-fail-under=80
Iterations: 10
```

#### `/autoresearch:plan`
Interactive wizard — produces `Goal / Scope / Metric / Direction / Verify` tuple. **Mandatory for Complex and Critical pipelines** (runs after W0, before the first implementation wave) to ensure measurable exit criteria exist before any specialist is dispatched. Optional for Standard class. Use whenever success criteria are undefined.

#### `/autoresearch:predict`
Multi-persona swarm analysis from Security, Performance, Maintainability, Architecture perspectives. Mandatory in Critical K1.

#### `/autoresearch:learn`
Full codebase documentation engine — scout, map, generate/update docs. Modes: `scout` / `generate` / `update`.

#### `/autoresearch:debug`
Autonomous 7-phase loop — Hypothesize → Test → Eliminate → Repeat. Flag: `--fix` (auto-switch to fix after finding bugs).

#### `/autoresearch:fix`
Autonomous repair loop — one atomic fix per iteration, auto-reverted on failure, repeats until zero errors.

```
/autoresearch:fix
Target: failing mypy + pytest errors
Scope: src/**/*.py
Verify: mypy src && pytest
```

#### `/autoresearch:reason`
Adversarial multi-agent refinement — generate → critique → synthesize → blind judge → converge. Mandatory in Critical K3.

#### `/autoresearch:scenario`
Exhaustive use case and edge case generation. Output feeds directly into `test-engineer`.

#### `/autoresearch:security`
Full STRIDE + OWASP Top 10 autonomous audit with code evidence. 4 adversarial red-team personas. Flags: `--fix`, `--fail-on critical`, `--diff`. Mandatory in Critical K7 with `--fix --fail-on critical`.

#### `/autoresearch:ship`
8-phase shipping workflow — Identify → Inventory → Checklist → Prepare → Dry-run → Ship → Verify → Log. Always start with `--dry-run`. Flags: `--dry-run`, `--auto`, `--monitor N`, `--rollback`.

---
