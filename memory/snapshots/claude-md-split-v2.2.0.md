# Context Snapshot: claude-md-split-v2.2.0

**project:** global-governance
**task:** claude-md-split-v2.2.0
**status:** completed-pending-user-size-decision
**pipeline-class:** Complex
**date:** 2026-04-20
**captured-by:** context-manager

---

## Decision Record

### Problem
CLI performance warning: "Large CLAUDE.md... 84.7k chars > 40.0k".

### Option Selected
Option C — @-include pointer pattern. Load-bearing sections pinned inline in primary; reference sections offloaded to 9 sibling CLAUDE-*.md files.

### Inline Pins (CLAUDE.md primary, non-negotiable)
§0 Preamble, §1 Laws, §2 Mandate, §3 Model Policy, §4 Classification, §5 Pipelines, §6 Gates, §7 Parallel, §11 Context Protocol, §14 Skills, §16 Decision Trees.

### Inlined Fragments (for §2.4 self-containment)
- §12.1 brief template (inserted at §2.4 tail)
- §8.3 escalation template (inserted at §6.3)
- §10.3 destructive-action excerpt (inserted near §2.3)
- §5.7 autoresearch flag cheat-sheet (new section in §5)

### Offloaded Pointer Siblings
| File | Sections |
|------|----------|
| CLAUDE-failure.md | §8 Failure Taxonomy |
| CLAUDE-ops.md | §9 Observability, §10 Security Posture |
| CLAUDE-dispatch-standards.md | §12 Dispatch Standards |
| CLAUDE-agents.md | §13 Agent Registry |
| CLAUDE-autoresearch.md | §15 Autoresearch Toolkit |
| CLAUDE-incident.md | §17 Incident Response |
| CLAUDE-communication.md | §18 Communication Matrix, §19 Anti-Patterns |
| CLAUDE-reference.md | §20 Glossary, §22 Version History |
| CLAUDE-quickref.md | §21 Appendix A Quick Reference |

---

## Agents Dispatched (C1 → C8)

| Stage | Agent | Verdict |
|-------|-------|---------|
| C1 | Plan | Produced split architecture + pipeline |
| C2 | /autoresearch:reason | Adversarial validation passed |
| C4 | 9x extraction passes (Sonnet) | 9 pointer files produced |
| C4 | Primary-rewrite pass | 20 edits applied, CLAUDE.md rewritten |
| C5 round 1 | architect-reviewer | STRUCT-010 High, STRUCT-011 Med, STRUCT-012 Low, STRUCT-013 Low |
| C5 round 1 fix | documentation-expert | All 4 STRUCT findings closed |
| C5 round 2 | architect-reviewer | **compliant** |
| C7 | general-purpose | All mechanical checks pass |
| C8 | documentation-expert (cross-link audit) | Clean — 10 files resolve, 12 stubs consistent, 6 advisory notes (non-blocking) |
| C8 | simplify (prose audit) | ~5.8k low-risk trim identified; ~7.2k medium-risk; hard floor ~43.9k |

### Gate Outcomes
- **architect-reviewer (C5 r1):** rejected — 4 findings (STRUCT-010 to STRUCT-013)
- **architect-reviewer (C5 r2):** compliant
- **general-purpose (C7):** pass — known-fail on >40k threshold is expected/accepted
- **documentation-expert (C8):** clean — 6 advisories logged, none are blockers
- **simplify (C8):** no further improvements within user-defined scope

---

## Files Created / Modified

| File | Action | Size (chars) |
|------|--------|-------------|
| /Users/isal/.claude/CLAUDE.md | Modified (84.7k → 54.6k, 1,634 → 1,068 lines) | 54,637 |
| /Users/isal/.claude/CLAUDE-agents.md | Created | 17,000 |
| /Users/isal/.claude/CLAUDE-autoresearch.md | Created | 4,000 |
| /Users/isal/.claude/CLAUDE-dispatch-standards.md | Created | 1,900 |
| /Users/isal/.claude/CLAUDE-ops.md | Created | 4,000 |
| /Users/isal/.claude/CLAUDE-failure.md | Created | 2,400 |
| /Users/isal/.claude/CLAUDE-incident.md | Created | 2,500 |
| /Users/isal/.claude/CLAUDE-communication.md | Created | 3,700 |
| /Users/isal/.claude/CLAUDE-reference.md | Created | 3,000 (includes v2.2.0 row) |
| /Users/isal/.claude/CLAUDE-quickref.md | Created | 3,300 |

**Version bump:** 2.1.0 → 2.2.0. Effective date: 2026-04-20.

---

## Outcome

- Char reduction: 84.7k → 54.6k = **35.5% reduction**.
- CLI warning will still fire (54.6k > 40.0k threshold) but at reduced impact.
- All 4 STRUCT architectural findings closed.
- No open architectural risks.

---

## Open Items (Pending User Decision)

The user has not yet confirmed which of the following paths to take:

| Option | Action | Projected Size | Risk |
|--------|--------|---------------|------|
| A — Accept current | No further changes | 54.6k | None |
| B — Low-risk prose trim | ~5.8k gain via simplify recommendations | ~48.8k | Low |
| C — Structural moves + trim | §7/§11/§14 → pointers + prose trim (~10.7k gain) | ~43.9k floor | Medium — removes inline pins |
| D — Accept hard floor | §1 Law rationales + user-pinned sections set ~44k floor; 40k is unreachable without touching OFF-LIMITS content | N/A | N/A |

**Constraint:** Trimming §1 Law rationales is OFF-LIMITS per user-defined scope. Removing user-pinned inline sections (§7, §11, §14) is medium-risk and requires explicit user approval.

---

## Known Limitations / Advisories

- Cross-sibling §N bare references (advisories A-E from C8 cross-link audit): a reader opening a sibling file standalone may encounter an unresolved §N reference. Navigation via primary pointer table always resolves. Severity: low, no action required unless user requests explicit file hints.
- Pointer siblings increase file count loaded per session (10 @-includes vs 1 original). Token cost is unchanged — @-include content is fully pulled regardless.
- 40k threshold is a CLI performance guideline, not a hard limit. Functionality is unaffected at 54.6k.

---

## Rollback Plan

If the split causes issues:
1. Restore CLAUDE.md from git or backup (original 84.7k monolith).
2. Delete the 9 CLAUDE-*.md sibling files.
3. Version reverts to 2.1.0.

No infrastructure, IAM, or production config was touched. Rollback is safe at any time.

---

## Lessons Learned Hook

No new lessons_learned.md entry required — this was a documentation pipeline with no functional failures beyond the expected gate rejection cycle (STRUCT findings, closed cleanly in round 2).
