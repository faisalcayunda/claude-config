---
name: optimize-skill
description: GEPA-style automated optimization loop for skill files. Reads failure patterns from eval.json, generates N modified skill variants targeting those failures, scores them against the rubric, and saves the best variant as a unified diff for human review. Never applies changes automatically.
argument-hint: "--skill <name> [--variants N]"
---

EXECUTE IMMEDIATELY — do not deliberate.

---

## Argument Parsing

Extract from $ARGUMENTS:

| Argument | Values | Default | Notes |
|---|---|---|---|
| `--skill` | string | required | skill directory name under `/Users/isal/.claude/skills/` |
| `--variants` | integer 1–10 | 3 | number of candidate variants to generate |

If `--skill` is missing: ABORT with:

> "⛔ --skill <name> is required. Example: /optimize-skill --skill data-engineer-boilerplate"

Resolve paths:
- `SKILL_DIR` = `/Users/isal/.claude/skills/<name>/`
- `EVAL_FILE` = `/Users/isal/.claude/skills/<name>/eval.json`
- `LEARNINGS_FILE` = `/Users/isal/.claude/skills/<name>/learnings.md`
- `VARIANTS_DIR` = `/Users/isal/.claude/skills/<name>/proposed-variants/`
- `COMMANDS_FALLBACK` = `/Users/isal/.claude/commands/<name>.md`

---

## Step 1 — Load and Validate Data

Read `EVAL_FILE`. If the file does not exist: ABORT with:

> "⛔ eval.json not found at EVAL_FILE. Run /score-skill --skill <name> first to initialize it."

Parse the JSON. Extract:
- `runs[]` — all run entries
- `_meta.criteria` — rubric criteria object (check `_meta.rubric.criteria` as fallback if `_meta.criteria` is absent)
- `_meta.skill_source_file` — path override for skill source (may be absent)
- `_meta.scoring_rubric` — score legend (informational)

Count **scored runs**: runs where `score` is not null.

If scored_run_count < 10: ABORT with:

> "⛔ Not enough data. Need 10+ scored runs to optimize (have N). Use /score-skill --skill <name> to score past runs first."

Count from scored runs:
- **low_performers**: runs where `score < 7` OR `outcome` in `["fail", "partial"]`
- **high_performers**: runs where `score >= 8` AND `outcome` == `"pass"` (or outcome is absent but score >= 8)
- **average_score**: sum of all scores / scored_run_count (round to 2 decimal places)

---

## Step 2 — Diagnose Failure Patterns

From low_performers, extract signals for each run:

1. `trace.failure_reason` — if the field exists and is non-empty, record the value
2. `human_review.correction` — if the field exists and is non-empty, record the value
3. `arguments` — the invocation arguments that produced the failure
4. `score` — numeric severity (lower = worse)

Group signals into **named failure patterns**. A pattern is a cluster of related failure reasons. Examples of pattern names:
- "wrong stack mode detection"
- "missing file stubs at standard depth"
- "hardcoded values instead of placeholders"
- "generator constraint violated — ran shell command"
- "argument parsing ambiguity"
- "incomplete output for full depth"

Guidelines for grouping:
- Two failures are the same pattern if they share the same root instruction gap in the skill
- A single run may contribute to multiple patterns if it has multiple failure signals
- Patterns backed by a single run are valid but lower-priority than those backed by multiple

Rank patterns by occurrence count (descending). Identify the **top-3 failure patterns**.

If fewer than 3 distinct patterns exist, use however many exist (minimum 1).

Record for each pattern:
- Pattern name
- Occurrence count
- Representative failure_reason or correction text (1–2 sentences)
- Affected arguments (if a specific argument set triggers it consistently)

---

## Step 3 — Read Skill Source

Determine skill source path:
1. If `_meta.skill_source_file` is set in eval.json, use that path.
2. Otherwise, use `COMMANDS_FALLBACK` = `/Users/isal/.claude/commands/<name>.md`.

Read the skill source file. If it does not exist: ABORT with:

> "⛔ Skill source file not found at <resolved path>. Cannot generate variants without the original."

Hold the full source text in memory as `ORIGINAL_SOURCE`.

---

## Step 4 — Generate N Variants

For each variant index i from 1 to N (where N = --variants, default 3):

**Target pattern assignment:**
- Variant 1 → top failure pattern (rank 1)
- Variant 2 → second failure pattern (rank 2), or rank 1 again with a different fix strategy if only one pattern exists
- Variant 3+ → next ranked pattern, cycling back to rank 1 if patterns are exhausted

**Generation rules per variant:**

1. Start from `ORIGINAL_SOURCE` — do not build variants on top of each other.

2. Identify the specific skill instruction (step, rule, table row, or constraint block) that is responsible for the targeted failure pattern. Name it explicitly in your reasoning.

3. Make **one primary substantive change** per variant addressing that instruction gap:
   - Add a guard condition or explicit disambiguation rule
   - Tighten an ambiguous instruction with a concrete example
   - Add an edge-case handling block
   - Introduce an explicit validation step before a risky action
   - Reorder steps to prevent the failure from being reached without proper setup
   - Strengthen a constraint with a DO / DO NOT pair that covers the failure case

4. Changes must be **substantive** — they alter behavior. Cosmetic edits (whitespace, rephrasing without meaning change) are not valid.

5. **Preserve high-performer elements**: instructions or patterns that appear in invocations where score >= 8 must not be weakened or removed.

6. Each variant is a complete, self-contained skill file text — not a diff. Store as `VARIANT_TEXT[i]`.

7. Note for each variant:
   - `variant_target_pattern`: which failure pattern this addresses
   - `variant_change_summary`: 1–2 sentence description of what was changed and why
   - `variant_changed_section`: the section header or rule name that was modified

---

## Step 5 — Evaluate Variants Against Rubric

Retrieve rubric criteria from `_meta.criteria` (or `_meta.rubric.criteria` as fallback).

If no criteria object is found in eval.json, use this default rubric:

```
correctness:     Does the variant correctly address the targeted failure pattern?  (weight: 0.35)
completeness:    Does the variant preserve all high-performer behaviors?           (weight: 0.30)
clarity:         Are the new/changed instructions unambiguous and precise?         (weight: 0.20)
parsimony:       Is the change minimal — no unnecessary additions?                 (weight: 0.15)
```

**Scoring procedure for each variant:**

For each criterion:
1. Score 1–10: how well does this variant's change address or preserve that criterion?
2. Multiply by the criterion's weight (default: equal weights if not specified in eval.json criteria — divide 1.0 evenly across criteria)
3. Sum weighted scores → `VARIANT_WEIGHTED_SCORE[i]`

**Selection:** Choose the variant with the highest `VARIANT_WEIGHTED_SCORE`. Call this `SELECTED_VARIANT` and `SELECTED_INDEX`.

If two variants tie: prefer the one targeting the higher-ranked failure pattern.

Record per-criterion scores and weighted totals for transparency in the output.

---

## Step 6 — Generate Unified Diff

Compute a unified diff between `ORIGINAL_SOURCE` and `VARIANT_TEXT[SELECTED_INDEX]`.

Unified diff format:
```
--- a/commands/<name>.md
+++ b/commands/<name>.md
@@ -<start>,<count> +<start>,<count> @@
 <context line>
-<removed line>
+<added line>
 <context line>
```

Rules:
- Context lines: 3 lines before and after each change hunk
- If changes are spread across non-adjacent regions, emit multiple `@@` hunks
- Lines that are identical in both versions are context lines (no prefix or space prefix)
- Removed lines are prefixed with `-`
- Added lines are prefixed with `+`

Determine `TODAY` as today's date in `YYYY-MM-DD` format.

Determine `DIFF_FILENAME` = `TODAY-v<SELECTED_INDEX>.diff`

Determine `DIFF_PATH` = `/Users/isal/.claude/skills/<name>/proposed-variants/DIFF_FILENAME`

Write the diff to `DIFF_PATH` using the Write tool. (The Write tool creates parent directories implicitly — no separate mkdir step needed.)

---

## Step 7 — Update learnings.md

Read the current content of `LEARNINGS_FILE`. If the file does not exist, initialize it with:

```markdown
# Learnings — <name>

**Skill:** <name>
**Owner:** isal
**Last updated:** TODAY

> Append-only log. Newest entry on top.

---

## Entries

```

Append the following entry **after** the `## Entries` heading (insert before existing entries so newest is first):

```markdown
## Optimization Run: TODAY
- Total runs analyzed: <scored_run_count> scored, <low_performers count> low-performers, <high_performers count> high-performers
- Current average score: <average_score>/10
- Top failure patterns identified:
  1. <pattern 1 name> (<N> occurrences)
  2. <pattern 2 name> (<N> occurrences)  [omit if fewer than 2 patterns]
  3. <pattern 3 name> (<N> occurrences)  [omit if fewer than 3 patterns]
- Variants generated: <N>
- Selected variant: v<SELECTED_INDEX> (weighted score: <VARIANT_WEIGHTED_SCORE[SELECTED_INDEX] rounded to 2dp> / 10)
- Changes: <variant_change_summary for selected variant>
- Diff saved: proposed-variants/DIFF_FILENAME

```

Write the updated learnings.md back using the Write tool.

---

## Step 8 — Present to User

Output the following summary (substitute all placeholders):

```
✅ Optimization complete for '<name>'

📊 Analysis:
  - <scored_run_count> scored runs | <low_performers count> low-performers | <high_performers count> high-performers
  - Current average: <average_score>/10

🔍 Top failure patterns:
  1. <pattern 1 name> — <representative description> (<N> occurrences)
  2. <pattern 2 name> — <representative description> (<N> occurrences)  [if exists]
  3. <pattern 3 name> — <representative description> (<N> occurrences)  [if exists]

🧬 Variants generated: <N>

  Variant scores (weighted):
  | Variant | Target Pattern          | Score  |
  |---------|------------------------|--------|
  | v1      | <pattern name>         | <X.XX> |
  | v2      | <pattern name>         | <X.XX> |
  | v3      | <pattern name>         | <X.XX> |
  [add rows for each variant]

💡 Recommended variant: v<SELECTED_INDEX> (score: <VARIANT_WEIGHTED_SCORE[SELECTED_INDEX]>/10)
   Changes: <variant_change_summary>
   Section modified: <variant_changed_section>

📁 Diff saved: <DIFF_PATH>

To apply:
  1. Read the diff:   /Users/isal/.claude/commands/<name>.md
  2. Review changes in:  <DIFF_PATH>
  3. Manually apply the diff to /Users/isal/.claude/commands/<name>.md
  ⚠️  Do NOT apply automatically — this is human-in-the-loop by design.
```

---

## Hard Constraints

- NEVER modify `/Users/isal/.claude/commands/<name>.md` directly — the live skill file is read-only during this command.
- NEVER apply the diff automatically — output only, review required.
- NEVER use Bash tool — use only Read and Write tools.
- NEVER use AskUserQuestion — this is a fully autonomous analysis step.
- If eval.json has fewer than 10 scored runs, ABORT at Step 1. Do not proceed.
- All output is streamed live — never run in background.
- Variants are built from `ORIGINAL_SOURCE` only — never layer variants on top of each other.
- The diff in Step 6 must represent only the selected variant's changes — not an aggregate of all variants.

---

## Abort Conditions Summary

| Condition | ABORT message |
|---|---|
| `--skill` argument missing | "⛔ --skill <name> is required. Example: /optimize-skill --skill data-engineer-boilerplate" |
| `eval.json` not found | "⛔ eval.json not found at EVAL_FILE. Run /score-skill --skill <name> first." |
| Scored runs < 10 | "⛔ Not enough data. Need 10+ scored runs to optimize (have N). Use /score-skill --skill <name> to score past runs first." |
| Skill source file not found | "⛔ Skill source file not found at <path>. Cannot generate variants without the original." |
