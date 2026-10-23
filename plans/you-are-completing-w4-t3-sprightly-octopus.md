# W4-T3 second opinion (advisor, read-only)

## Context
Caller asked for full W4-T3 implementation + gates + commit in one pass. Advisor role: verdict on the brief, not execution.

## Verdict
Scope matches development-plan.md W4-T3 (line 482). The process does not: the brief drops G-GOLDEN and the review gate and commits straight after the gates. The damage list is also incomplete.

## Corrections to the brief
1. Add G-GOLDEN (qh-core/src/render.rs is staged-modified; plan requires output unchanged).
2. One opus review round (High tier: spill encryption; plan gates RR, SEC, TD, SF, AR, CR, collapsed by O-20 to one round) BEFORE the commit. Commit, then ledger row.
3. Treat collate.rs / spill.rs / chunk.rs as spliced, not just truncated:
   - collate.rs:9-10 module doc cut mid-sentence and spliced into NumKey doc; collate.rs:58-59 `match rest.find(..)` missing `None =>` arm + close.
   - spill.rs:29-32 duplicated doc comment; missing `ring::aead::{Aad, LessSafeKey, Nonce, UnboundKey, AES_256_GCM}`, `ring::rand::SecureRandom` (trait for `.fill`), `crate::StoreError`.
   - chunk.rs:44 `bytes()` runs straight into `/// Per-column shape summary` with no `}`.
4. NumKey::cmp: zero (empty digits) is compared by `exp` like any other number, so 0 can sort above 0.5 depending on the zero exponent. Handle `is_zero()` before the exponent compare.
5. Split implementation across 2-3 sequential sonnet dispatches (fix 3 files; render/registry/logical/view; store/lib/tests), one commit at the end.

## Verification
G-RUST, G-DENY, G-GOLDEN, spill tests listed in plan line 494, then review, then commit.
