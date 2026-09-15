---
name: score-skill
description: Human scoring tool for past skill invocation runs. Presents an unscored run's trace, collects a score (1-10) + outcome + optional correction, and persists it back to eval.json. Part of the GEPA-style optimization loop for ~/.claude/skills/.
argument-hint: "--skill <name> [--run-id <id>]"
---

EXECUTE IMMEDIATELY — do not deliberate.

## Argument Parsing

Extract from $ARGUMENTS:

| Argument | Required | Notes |
|---|---|---|
| `--skill <name>` | YES | Skill directory name under `~/.claude/skills/` |
| `--run-id <id>` | NO | Specific run ID to score; if omitted, targets most recent unscored run |

If `--skill` is missing: stop and tell the user exactly:

> "Usage: /score-skill --skill <name> [--run-id <id>]"

Do NOT proceed without a skill name.

---

## Step 1 — Read eval.json

Read the file at:

```
/Users/isal/.claude/skills/<name>/eval.json
```

where `<name>` is the value of `--skill`.

**If the file does not exist:**
Tell the user:

> "No eval.json found for skill '<name>'. Has it been invoked yet?"

Stop. Do not proceed.

---

## Step 2 — Locate the target run

### If `--run-id` was given:

Find the entry in `runs[]` where `run_id` matches exactly.

If no match:
> "Run ID '<id>' not found in eval.json for skill '<name>'. Check the ID and try again."

Stop.

### If `--run-id` was NOT given:

Scan `runs[]` from most recent to oldest (by `timestamp` descending). Find the first entry where `score` is `null`.

If no unscored run exists:
- Count total runs with a non-null score.
- Compute or read `average_score`.

Tell the user:
> "No unscored runs for '<name>'. All <N> runs have been scored. Average score: <X.XX>"

Stop.

---

## Step 3 — Present the run to the user

Display a summary block using this exact format:

```
## Run to Score — <skill-name>

Run ID:    <run_id>
Timestamp: <timestamp>
Arguments: <arguments>

### Output Preview
<trace.final_lines — the last ~300 chars of output from this run>
(If final_lines is null or empty, show: "[no output preview recorded]")

### Scoring Rubric
<List each criterion.>
```

**Rubric rendering rules:**

The eval.json `_meta` block may store criteria in two formats. Handle both:

- **Array format** (`_meta.rubric.criteria` is a list of objects with `name`, `description`, optional `weight`):
  For each item: `  - <name> (<weight>x): <description>`
  Omit weight notation if weight field is absent.

- **Object format** (`_meta.criteria` is a flat key → description map):
  For each key: `  - <key>: <description>`

If neither is present: show `  [no rubric defined]`

Also show the score scale as a reference footer:
```
Score scale: 1=unusable  5=marginal  7=good  8=strong  9=excellent  10=perfect
Outcome:     pass (>=8, no rework) | partial (5-7, usable with corrections) | fail (<=4, rejected)
```

---

## Step 4 — Collect scoring input

Use `AskUserQuestion` with exactly these three questions in a single call:

1. "Score this run 1-10 (1=terrible, 5=acceptable, 8=good, 10=perfect):"
2. "Outcome — enter one of: pass / partial / fail"
3. "Correction or note (optional — press Enter to skip):"

Wait for all three answers before proceeding.

**Validate the score:**
- Must be an integer between 1 and 10 inclusive.
- If the user enters a non-integer or out-of-range value: tell them "Score must be an integer from 1 to 10." and ask again (one retry only — do not loop indefinitely).

**Validate the outcome:**
- Must be exactly one of: `pass`, `partial`, `fail` (case-insensitive; normalize to lowercase).
- If invalid: tell them "Outcome must be pass, partial, or fail." and ask again (one retry only).

**Correction note:**
- Accept any text. If blank or whitespace-only, store as `null`.

---

## Step 5 — Write back to eval.json

Using the Edit tool, update the eval.json file in place. Apply ALL of the following changes atomically in a single Edit call:

### 5a — Update the target run entry

Set these fields on the matched run object:

```
score                         → <integer score>
outcome                       → "<pass|partial|fail>"
human_review.scored_at        → "<today's date in YYYY-MM-DD format>"
human_review.correction       → "<correction text, or null if blank>"
human_review.note             → null  (leave null unless correction was provided, in which case use the same text — the schema uses both fields; populate correction with the full text)
```

### 5b — Recompute average_score

After updating the run:

1. Collect all entries in `runs[]` where `score` is not `null`.
2. Sum their scores and divide by count.
3. Round to 2 decimal places.
4. Set `average_score` to this value.
5. If zero scored runs remain (edge case): set `average_score` to `null`.

### 5c — Update last_updated

Set `last_updated` to today's date in `YYYY-MM-DD` format.

**Edit tool usage:** Read the current raw JSON text, apply the three changes above, and write back using Edit. Preserve all other fields exactly — do not reformat, reorder, or add/remove keys beyond what is specified here.

---

## Step 6 — Confirm to user

Output a single confirmation line:

```
Scored run <run_id>: <score>/10, <outcome>. Average score now: <X.XX> (<N> scored runs).
```

Where:
- `<N>` = count of runs with a non-null score after this update.
- `<X.XX>` = the recomputed average_score.

---

## Hard constraints

- Read tool and Edit tool ONLY for file operations. No Bash, no Write (use Edit to update existing file).
- Score exactly ONE run per invocation. Do not batch-score.
- Do not modify any field on the run entry other than the four listed in Step 5a.
- Do not modify `_meta`, `skill`, or `description` fields.
- Do not reformat or pretty-print the entire JSON — apply surgical edits only.
- If eval.json is malformed JSON: tell the user "eval.json for '<name>' is not valid JSON. Inspect and repair it manually." Stop.

Stream all output live — never run in background.
