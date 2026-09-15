---
name: data-quality-check
description: GENERATOR — produces dbt test definitions and/or Great Expectations suite YAML for a given table schema or dbt model. Never executes tests. Group A: triggered when user asks to add data quality checks, generate test stubs, or scaffold DQ for a model or table.
argument-hint: "[--model <name>] [--schema <yaml-or-path>] [--target dbt|ge|both] [--layer staging|intermediate|marts]"
---

EXECUTE IMMEDIATELY — do not deliberate.

## GENERATOR ONLY — this skill produces test definitions. It never runs dbt test, never executes against live data.

---

## Argument Parsing

Extract from $ARGUMENTS:

| Argument | Values | Default | Notes |
|---|---|---|---|
| `--model` | dbt model name | — | e.g., `stg_penerima_manfaat` |
| `--schema` | inline YAML, path to schema.yml, or CREATE TABLE DDL | — | file path → read it; inline → parse directly |
| `--target` | `dbt`, `ge`, `both` | `dbt` | output format(s) |
| `--layer` | `staging`, `intermediate`, `marts` | `staging` | controls test severity |

If neither `--model` nor `--schema` is provided: ask exactly:

> "Provide model name or paste column definitions."

Do NOT proceed until at least one is available.

---

## Step 1 — Read context

Read the Stack line in `/Users/isal/.claude/CLAUDE.md`.
Confirm stack: dbt + Airflow 3.1.7, on-premise. Apply hard rules (no overengineering; no guessing).

---

## Step 2 — Parse inputs

- If `--schema` is a file path: read the file.
- If `--schema` is inline YAML or DDL: parse column names and types directly from the pasted content.
- If only `--model` is given with no `--schema`: stop and ask the user to paste a column list or schema.yml snippet.

**Do NOT infer or guess column definitions. Ask before generating.**

Extract per column:
- `name`
- `data_type` (if available)
- `nullable` hint (if available)

---

## Step 3 — Classify each column

Apply exactly one type label per column:

| Type class | Detection rule |
|---|---|
| `id_column` | name ends in `_id`, `_key`, or is exactly `id` |
| `timestamp_column` | type is `timestamp`/`date`/`datetime`, or name ends in `_at`, `_date`, `_time` |
| `flag_column` | type is `boolean`, or name starts with `is_`, `has_`, `flag_` |
| `categorical_column` | type is `varchar`/`text` AND name contains `_type`, `_status`, `_category`, `_code` |
| `numeric_column` | type is `integer`, `float`, `decimal`, `numeric`, `bigint` |
| `free_text_column` | `varchar`/`text` that does not match categorical pattern |

Apply the first matching rule in order (top wins).

---

## Step 4 — Apply default test matrix

| Column type | dbt tests | GE expectations |
|---|---|---|
| `id_column` | `not_null`, `unique` | `expect_column_values_to_not_be_null`, `expect_column_values_to_be_unique` |
| `timestamp_column` | `not_null`, `dbt_utils.expression_is_true` (`value > '2000-01-01'`) | `expect_column_values_to_not_be_null`, `expect_column_values_to_be_between` |
| `flag_column` | `not_null`, `accepted_values [true, false]` | `expect_column_values_to_not_be_null`, `expect_column_values_to_be_in_set` |
| `categorical_column` | `not_null`, `accepted_values [# TODO: fill values]` | `expect_column_values_to_not_be_null`, `expect_column_values_to_be_in_set` |
| `numeric_column` | `not_null`, `dbt_utils.expression_is_true` (`value >= 0`) | `expect_column_values_to_not_be_null`, `expect_column_values_to_be_between` |
| `free_text_column` | `not_null` | `expect_column_values_to_not_be_null` |

---

## Step 5 — Apply severity by layer

| Layer | Rule |
|---|---|
| `staging` | All tests: `severity: warn` |
| `intermediate` | `id_column` tests: `severity: error`; all others: `severity: warn` |
| `marts` | All tests: `severity: error` |

---

## Step 6 — Generate output (text only)

**Do NOT execute. Do NOT run dbt. Do NOT connect to any database.**

### For `--target dbt` or `both`

Produce a `schema.yml` block with structure:

```yaml
# [data-quality-check generated: YYYY-MM-DD]
models:
  - name: <model-name>
    columns:
      - name: <col_name>
        tests:
          - not_null:
              severity: warn
          - unique
      - name: <categorical_col>
        tests:
          - not_null:
              severity: warn
          - accepted_values:
              values: [] # TODO: fill accepted values
              severity: warn
```

Use dbt-core native test syntax. Wrap `dbt_utils` tests with correct package prefix.

### For `--target ge` or `both`

Produce a Great Expectations suite YAML:

```yaml
expectation_suite_name: <model_name>_suite
expectations:
  - expectation_type: expect_column_values_to_not_be_null
    kwargs:
      column: <col_name>
  - expectation_type: expect_column_values_to_be_unique
    kwargs:
      column: <col_name>
```

---

## Step 7 — Output coverage summary

After all generated blocks, append a coverage table:

```
### Coverage summary
| Column | Type class | Tests applied |
|--------|------------|---------------|
| <col>  | id_column  | not_null, unique |
| <col>  | categorical_column | not_null, accepted_values (TODO) |
```

---

## Full output format

```
## Data Quality Check Generator: <model-name>

**Target:** dbt | ge | both  |  **Layer:** staging | intermediate | marts
**Generated:** YYYY-MM-DD

### dbt schema.yml block
[generated yaml block]

### Great Expectations suite
[generated yaml block — only if --target ge or both]

### Coverage summary
[table]
```

---

## Hard constraints

- GENERATOR ONLY — this skill produces test definitions. It never runs `dbt test`, never executes against live data.
- Do NOT fabricate column names or types. If schema is unknown, ask before generating.
- For `categorical_column`: always output `# TODO: fill accepted values` placeholder. Never guess accepted values.
- Hard rule: do not overengineer. Apply the matrix above only.
- Never add tests beyond the matrix without explicit user request.
- Never modify existing schema.yml files — output is always a new text block for the user to integrate.

---

Stream all output live — never run in background.
