# pem-sync-deploy — LOCAL SKILL TEMPLATE

## Installation

This file is a **template**. It is not the command itself.

Copy the command body (between the BEGIN and END markers below) into:

    <pem-repo>/.claude/commands/pem-sync-deploy.md

Steps:
1. Navigate to the root of the `pem-master-individu-pm-sync-mpm` repository.
2. Create the directory if it does not exist: `mkdir -p .claude/commands`
3. Copy everything between the BEGIN and END markers into `.claude/commands/pem-sync-deploy.md`.
4. Remove these installation instructions — only the command body goes into the project repo.
5. Commit the file: `git add .claude/commands/pem-sync-deploy.md && git commit -m "chore: add pem-sync-deploy local skill"`

After installation the skill is invocable as `/pem-sync-deploy` from within the project.

---

<!-- ===== BEGIN COMMAND BODY — copy from here ===== -->

---
name: pem-sync-deploy
description: Deploy pem-master-individu-pm-sync-mpm pipeline — runs pre-flight checks, dbt models, triggers Airflow DAG, confirms Asset registration. LOCAL skill for pem project only. Deploy step is Group B (user-confirmed).
argument-hint: "[--env dev|staging|prod] [--dry-run] [--skip-dbt] [--dag-only]"
---

EXECUTE IMMEDIATELY — do not deliberate.

## Hard Constraints

- Deploy step (Step 7) requires explicit 'y' confirmation. This is Group B — never auto-trigger.
- Hard rule: Never commit secrets. If Step 4 finds credentials: stop immediately.
- Hard rule: No data deletion without rollback path. Step 5 always captures rollback reference.
- Airflow REST API: always use /api/v2/ (v1 removed in Airflow 3.x).
- On-premise deployment only — no cloud storage, no AWS/GCP/Azure commands.

---

## Argument Parsing

Extract from `$ARGUMENTS`:

| Flag | Default | Effect |
|------|---------|--------|
| `--env dev\|staging\|prod` | `dev` | Target environment. If `prod`, see Step 3a — explicit confirmation required. |
| `--dry-run` | off | Print all commands that WOULD run; execute nothing. Safe for inspection. |
| `--skip-dbt` | off | Skip dbt run/test; go straight to Airflow trigger. |
| `--dag-only` | off | Skip ALL pre-flight checks and dbt; trigger Airflow DAG directly. Use with caution. |

Set `ENV`, `DRY_RUN`, `SKIP_DBT`, `DAG_ONLY` variables from the parsed flags before proceeding.

---

## Step 1 — Context Confirmation

Read wiki `/Users/isal/.claude/wiki/entities/MPM sync pipelines.md` and `concepts/MPM sync reconciliation policy.md` and confirm:
- Project `pem-master-individu-pm-sync-mpm` is listed as an active project.
- Owner is `isal`.

If the pages are missing or the project is not listed: print a warning and continue.

---

## Step 2 — Project Overrides

Read `.claude/CLAUDE.md` in the current working directory (if it exists). Apply any deployment-specific overrides found there (e.g., custom dbt target names, alternate Airflow base URL, model selector tags).

---

## Step 3 — Pre-flight Checks

Skip this entire step if `--dag-only` is set.

### Step 3a — Production Gate

If `ENV` is `prod`:

```
STOP — You are deploying to PRODUCTION.
Type 'yes' to continue or anything else to abort.
```

Wait for user input. Continue **only** if the response is exactly `yes` (lowercase, no trailing space). Any other input: print "Deploy aborted." and exit.

### Step 3b — dbt Project Root Check

Check that `dbt_project.yml` exists in the current working directory.

If not found: **FAIL** with:
```
Not in dbt project root. Navigate to project root first.
```
Do not proceed.

### Step 3c — Git Status Warning

Run `git status --short`. If there are any uncommitted or untracked files, print:
```
[WARN] Uncommitted changes detected:
<git status output>
Proceeding, but consider committing first.
```
This is a warning, not a hard stop.

### Step 3d — dbt Compile

Run: `dbt compile --target <ENV>`

If `--dry-run`: print the command only; do not execute.

If compilation fails: **STOP**, print the full error, do not proceed to Step 4.

---

## Step 4 — Secrets Check

Skip this step if `--dag-only` is set.

Scan the output of `git diff --staged` and `git diff HEAD~1..HEAD` for the following patterns assigned to string literals:

- `password=`
- `token=`
- `secret=`
- `api_key=`

If any match is found: **STOP** immediately with:
```
[FAIL] Possible secret detected in diff. Fix before deploying.
Matched pattern: <pattern>
File: <filename>
```

Do not proceed under any circumstances.

---

## Step 5 — Rollback Reference

Before deploying, capture the current last-successful Airflow run as a rollback anchor.

Query:
```
GET /api/v2/dags/pem_master_individu_pm_sync_mpm/dagRuns?limit=1&order_by=-execution_date
```

Print:
```
Rollback reference: last successful run_id = <run_id> (execution_date: <date>)
```

If the query fails or returns no runs: print `[WARN] No prior successful run found — rollback reference unavailable.` and continue.

---

## Step 6 — dbt Run

Skip this step if `--skip-dbt` or `--dag-only` is set.

### Step 6a — dbt run

Execute:
```
dbt run --target <ENV> --select +tag:pem_sync
```

If the `pem_sync` tag is not defined in `dbt_project.yml`, fall back to:
```
dbt run --target <ENV> --select models/staging/+ models/intermediate/+
```

If `--dry-run`: print the command only; do not execute.

If any model fails:
- **STOP**
- Print the failed model names and their errors
- Do NOT proceed to Step 7

### Step 6b — dbt test

Execute:
```
dbt test --target <ENV> --select +tag:pem_sync
```

If any test with `severity: error` fails:
- **STOP**
- Print the failed test names and models
- Do NOT proceed to Step 7

Tests with `severity: warn` are reported but do not block.

---

## Step 7 — Airflow DAG Trigger (Group B — User Confirmation Required)

### Step 7a — Compose trigger command

Construct the following curl command:
```
curl -X POST \
  http://<AIRFLOW_BASE_URL>/api/v2/dags/pem_master_individu_pm_sync_mpm/dagRuns \
  -H "Content-Type: application/json" \
  -u <username>:<password> \
  -d '{"conf": {"env": "<ENV>", "triggered_by": "pem-sync-deploy-skill"}}'
```

Replace `<AIRFLOW_BASE_URL>` with the value from `.claude/CLAUDE.md` overrides, or default to the on-premise Airflow host for BGN (`sipgn-git.bgn.go.id` domain — confirm the exact host from project config).

### Step 7b — Print command

Print the full curl command to be executed (redact credentials with `****`).

### Step 7c — Dry-run guard

If `--dry-run`: print `[DRY-RUN] Command printed above — not executed.` and skip 7d–7f.

### Step 7d — Explicit confirmation gate

Print exactly:
```
Trigger Airflow DAG pem_master_individu_pm_sync_mpm in <ENV>? [y/N]
```

Wait for user input.

### Step 7e — Execute or abort

- If user responds `y`: execute the curl command.
- Any other input: print `Deploy aborted.` and exit.

### Step 7f — Print run_id

On successful trigger, extract and print the returned `run_id` from the API response.

---

## Step 8 — Asset Confirmation

Skip this step if `--dry-run`.

Poll up to 5 times with 30-second intervals:
```
GET /api/v2/assets?uri_pattern=pem%3A%2F%2Fmaster_individu_pm
```

On success: print `Asset event recorded: <uri> at <timestamp>`

If no confirmation after 5 polls (150 seconds total): print:
```
[WARN] Asset event pending — check Airflow UI for confirmation.
URI: pem://master_individu_pm
```

---

## Step 9 — Deployment Summary

Print the following structured summary upon completion:

```
## pem-sync-deploy: <ENV> [YYYY-MM-DD HH:MM]

### Pre-flight
[OK/WARN/FAIL] dbt compile: <result>
[OK/WARN/FAIL] Git status: <result>
[OK/WARN/FAIL] Secrets scan: <result>
Rollback reference: last successful run_id = <run_id>

### dbt run
[OK] <model>: <rows> rows
[FAIL] <model>: <error>

### dbt test
[OK] <N> tests passed
[FAIL] <test> on <model>: <failure>

### Airflow trigger
DAG: pem_master_individu_pm_sync_mpm
Run ID: <run_id> | DRY-RUN | ABORTED

### Asset confirmation
URI: pem://master_individu_pm
Status: CONFIRMED at <timestamp> | PENDING | SKIPPED

### Summary
Status: SUCCESS | PARTIAL | FAILED | DRY-RUN
Rollback: re-trigger run_id <last_successful_run_id> if needed
```

---

## Stream Footer

Stream all output live — never run in background.

<!-- ===== END COMMAND BODY ===== -->
