---
name: dbt-model-gen
description: GENERATOR — scaffolds dbt model SQL (with source/ref macros) and schema.yml stub for staging, intermediate, or marts layers. Never executes dbt. Group A: triggered when user asks to create a new dbt model or generate dbt scaffolding.
argument-hint: "[--source <schema.table>] [--model <name>] [--layer staging|intermediate|marts] [--project <path>]"
---

EXECUTE IMMEDIATELY — do not deliberate.

## GENERATOR ONLY — this skill writes text. It never runs dbt run, dbt test, dbt compile, or any dbt command.

---

## Argument Parsing

Extract from $ARGUMENTS:

- `--source` — source table (format: `<schema>.<table>`, e.g., `raw.penerima_manfaat`) OR upstream dbt model name for intermediate/marts layers.
- `--model` — target model name (e.g., `stg_penerima_manfaat`). If omitted, derive from source name with layer prefix.
- `--layer` — REQUIRED. `staging`, `intermediate`, or `marts`. If omitted, ask: "Which layer? (staging / intermediate / marts)" Do not proceed until layer is specified.
- `--project` — path to dbt project root. Default: current working directory. Used to check for sources.yml.

If `--source` is absent: ask "What source table or upstream model should this be built from?" Do not proceed until source is available.

---

## Generate Workflow

### Step 1: Read business context

Read `/Users/isal/.claude/business-brain.md` — confirm dbt context before generating.

### Step 2: Apply layer rules

**staging**
- Naming: prefix `stg_` (e.g., `stg_penerima_manfaat`)
- Output path: `models/staging/<model_name>.sql`
- Reference type: `{{ source('<source_schema>', '<source_table>') }}`
- Rule: SELECT all columns from a SINGLE source table. Rename and cast only. NO business logic, NO joins.
- If user asks to add a JOIN to a staging model: refuse with explanation. Offer to create an intermediate model instead.

**intermediate**
- Naming: prefix `int_` (e.g., `int_pm_sync_joined`)
- Output path: `models/intermediate/<model_name>.sql`
- Reference type: `{{ ref('<upstream_staging_model>') }}`
- Rule: Joins, unions, business transformations go here. References only staging models.

**marts**
- Naming: user-provided (no enforced prefix)
- Output path: `models/marts/<model_name>.sql`
- Reference type: `{{ ref('<upstream_intermediate_model>') }}`
- Rule: Final denormalized/aggregated output. References only intermediate models.

### Step 3: Check sources.yml (staging layer only)

If `--layer staging` and `--project` is given:
- Check if `<project>/models/staging/sources.yml` exists.
- If found: note "sources.yml found — verify source registration."
- If not found: note "sources.yml not found — register source manually before running dbt."

### Step 4: Generate model SQL

Use the current date (YYYY-MM-DD format) in the generated comment.

```sql
-- [dbt-model-gen generated: YYYY-MM-DD]
-- Layer: <staging|intermediate|marts>
with source as (

    -- staging: select * from {{ source('<schema>', '<table>') }}
    -- intermediate/marts: select * from {{ ref('<upstream_model>') }}
    select * from {{ source('<schema>', '<table>') }}

),

renamed as (

    select
        -- TODO: list actual columns here
        *
    from source

)

select * from renamed
```

Substitute the correct macro (`source()` or `ref()`) per layer rules. Do not output both variants in the final file — output only the one appropriate for the layer.

### Step 5: Generate schema.yml stub

```yaml
# [dbt-model-gen generated: YYYY-MM-DD]
version: 2

models:
  - name: <model_name>
    description: "" # TODO: add description
    columns:
      - name: id  # TODO: replace with actual columns
        description: "" # TODO
        tests:
          - not_null
          - unique

# TODO: run /data-quality-check --model <model_name> to generate full test stubs
```

### Step 6: Output next-steps checklist

---

## Output Format

```
## dbt Model Generator: <model_name>

**Layer:** <staging | intermediate | marts>
**Source:** <source>
**Output paths:**
  - models/<layer>/<model_name>.sql
  - models/<layer>/schema.yml (append this block)

### models/<layer>/<model_name>.sql
```sql
[generated SQL]
```

### schema.yml addition
```yaml
[generated YAML]
```

### Next steps
- [ ] Add actual column names to SELECT clause
- [ ] Add column descriptions to schema.yml
- [ ] Register source in sources.yml (if staging layer)
- [ ] Run `/data-quality-check --model <model_name>` to generate full test stubs
- [ ] Run `dbt compile` to validate Jinja syntax
```

---

## Hard Constraints

- GENERATOR ONLY — this skill writes text. It never runs `dbt run`, `dbt test`, `dbt compile`, or any dbt command.
- Do NOT fabricate column names. Use placeholder `-- TODO: list actual columns` if schema is unknown.
- Staging models must not contain JOINs or business logic. If user requests this, refuse and explain layer separation.
- Use `{{ source() }}` for staging only. Use `{{ ref() }}` for intermediate and marts.

---

Stream all output live — never run in background.
