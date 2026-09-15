---
name: airflow-dag-lint
description: Static lint pass for Airflow 3.1.7 DAG files — runs before code-reviewer as a pre-gate; finds import errors, deprecated APIs, top-level code violations, and secrets hygiene issues. Group A: triggered when user pastes or references a *.py file from dags/ directory.
argument-hint: "[file: <path-or-paste>] [--strict]"
---

EXECUTE IMMEDIATELY — do not deliberate. Read the full workflow below first.

## Argument Parsing

Extract from $ARGUMENTS:

- `file:` — path to DAG file, OR user may paste content directly. If neither provided, ask exactly once: "Provide DAG file path or paste DAG content." Do not proceed until content is available.
- `--strict` — all WARN items become FAIL items

## Lint Workflow

**Step 1:** Read `/Users/isal/.claude/business-brain.md` — confirm active stack is Airflow 3.1.7 on-premise. If not confirmed, note it and continue.

**Step 2:** Read the target DAG file (use Read tool if file path given; if pasted content, proceed with the pasted text).

Steps 3–16 are CHECK operations. For each, record result as CRITICAL / FAIL / WARN / PASS.

---

**CHECK 3 — Import: airflow.decorators**
- Pattern: `from airflow.decorators` anywhere in file
- Severity: FAIL
- Fix: Replace with `from airflow.sdk`

**CHECK 4 — Import: Dataset class**
- Pattern: `from airflow.models import Dataset` OR `from airflow.datasets import Dataset`
- Severity: FAIL
- Fix: Replace with `from airflow.sdk import Asset`

**CHECK 5 — Top-level: Variable.get()**
- Pattern: `Variable.get(` appearing outside any function/class definition (module level)
- Severity: FAIL
- Fix: Move inside task function or use Airflow Variables via `{{ var.value.name }}` template

**CHECK 6 — Top-level: Database calls**
- Pattern: Any of `.execute(`, `session.`, `engine.`, `conn.query(`, `cursor.` at module level
- Severity: FAIL
- Fix: Move all DB calls inside task functions

**CHECK 7 — Top-level: Network calls**
- Pattern: Any of `requests.get(`, `requests.post(`, `http.get(`, `urllib.request.` at module level
- Severity: FAIL
- Fix: Move all network calls inside task functions

**CHECK 8 — Removed operator: SubDagOperator**
- Pattern: `SubDagOperator` anywhere in file
- Severity: FAIL
- Fix: SubDAGs removed in Airflow 3.x. Replace with TaskGroup.

**CHECK 9 — Template string: execution_date**
- Pattern: `{{ execution_date` in any string
- Severity: FAIL
- Fix: Rename to `{{ logical_date`

**CHECK 10 — Template string: next_execution_date**
- Pattern: `{{ next_execution_date` in any string
- Severity: FAIL
- Fix: Rename to `{{ next_logical_date`

**CHECK 11 — DAG param: fail_stop**
- Pattern: `fail_stop=` in DAG() constructor
- Severity: FAIL
- Fix: Rename to `fail_fast=`

**CHECK 12 — REST API version**
- Pattern: `/api/v1/` in any string literal
- Severity: FAIL
- Fix: Update to `/api/v2/`

**CHECK 13 — Secrets hygiene**
- Pattern: Any of `password=`, `token=`, `secret=`, `api_key=`, `access_key=` assigned to a string literal (not env var or secret backend call)
- Severity: CRITICAL
- Fix: Move credentials to Airflow Connections or Secrets Backend. Never hardcode.

**CHECK 14 — XCom DataFrame push**
- Pattern: `xcom_push(` or `return` in a task that returns a DataFrame, list, or dict > reasonable size — look for `pd.DataFrame`, `spark.DataFrame`, or large list assignments returned from @task
- Severity: WARN
- Fix: Serialize to file path (e.g., write to /tmp/<uuid>.parquet) and push the path string instead

**CHECK 15 — max_active_runs not set**
- Pattern: DAG() constructor without `max_active_runs=` parameter
- Severity: WARN
- Fix: Add explicit `max_active_runs=1` (or appropriate value) to prevent concurrent DAG runs

**CHECK 16 — retries not set**
- Pattern: `default_args` dict without `retries` key, AND no `retries=` in individual task decorators
- Severity: WARN
- Fix: Add `retries=3` (or project default) to default_args or per-task

---

**Step 17:** Produce output using the format below.

## Output Format

```
## DAG Lint: <filename>
**Airflow version target:** 3.1.7  |  **Mode:** normal | strict
**Result:** PASS | FAIL | WARN

### CRITICAL — deployment blocked
- [LINE xx] <check name>: <what was found> → <fix>

### FAIL — fix before code-reviewer gate
- [LINE xx] <check name>: <what was found> → <fix>

### WARN — recommended (surfaced to code-reviewer as context)
- [LINE xx] <check name>: <what was found> → <recommendation>

### PASS
- <check name> ✓
```

If no issues in a severity category, omit that section.

## Constraints

- This lint pass is a PRE-GATE step. The code-reviewer gate STILL runs after this. This skill feeds the gate — it does not replace it.
- Scope: Airflow 3.1.7 ONLY. Do not apply 2.x-specific guidance.
- Do NOT suggest alternative DAG implementations or refactors. Report findings only.

Stream all output live — never run in background.
