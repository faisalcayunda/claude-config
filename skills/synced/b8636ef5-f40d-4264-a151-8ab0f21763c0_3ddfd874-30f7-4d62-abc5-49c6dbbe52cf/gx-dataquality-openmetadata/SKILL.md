---
name: gx-dataquality-openmetadata
description: "Build, extend, and manually run the config-driven Great Expectations → OpenMetadata data-quality pipeline (`gx_data_quality`): GX computes real pass/fail on live Postgres and mirrors each result into OpenMetadata's Data Quality tab. Use whenever the user wants to scaffold a new pipeline repo for a new database, add checks for a table via a YAML config, add or change a database source/connection, change a check's query or value_set, add a new expectation→OpenMetadata mapping, validate or troubleshoot a config, or run checks manually and verify created test cases and results. It uses the dbhub MCP to profile source tables and the OpenMetadata MCP to confirm a table's exact fully-qualified name, columns, and existing tests, so configs match reality. Trigger even when unnamed, on gx_data_quality, run_all.py, connections.yaml, a table config, BUILTIN_DEFINITIONS, om.py, ensure_test_case, or 'data quality / GX checks'. MANUAL runs only — cron/Airflow scheduling is a separate skill."
---

# GX → OpenMetadata Data Quality Pipeline (manual)

## What this pipeline is

Great Expectations (GX) does the **real** data-quality checking against live Postgres.
OpenMetadata (OM) is the **noticeboard** where each result is pinned so the team sees
pass/fail where they already look. The code is a small, config-driven courier between
them: **one YAML file per table**, one generic engine, and **adding a table needs no new
Python**. The engine files (`src/db.py`, `src/om.py`, `src/runner.py`, `run_all.py`) are
stable; growth happens in `config/`.

Your job with this skill is to help the user **build or extend** that pipeline and **run
it manually**, using live database and catalog checks so every config matches reality.

## Scope — read this first

In scope: scaffold a new pipeline repo for a new DB; add or edit a table's checks (YAML);
add or change a database source/connection; change a check's query or `value_set`; add an
expectation→OM mapping; validate configs; run manually; verify results via MCP.

**Out of scope: scheduling.** Cron and Airflow are owned by a separate skill. If the user
asks to schedule this, say that's the other skill's job and stop — don't add schedulers here.

## The two MCPs that keep you honest (never guess)

The single biggest way this pipeline breaks is a config that doesn't match reality — a
wrong fully-qualified name, an assumed column, a rule the data doesn't actually satisfy.
Avoid that by **reading the real systems before writing config**:

- **dbhub MCP** — `mcp__dbhub__search_objects_<source>` and `mcp__dbhub__execute_sql_<source>`
  (e.g. `<source>` = `scm`). Confirm a table and its columns exist, and **profile** the
  data (null counts, distinct counts, min/max, sample values) to derive and sanity-check
  rules and to resolve FK value sets. Read-only `SELECT`/`COUNT` only.
- **OpenMetadata MCP** — `mcp__OpenMetadata__search_metadata`, `get_entity_details`,
  `get_test_definitions`. Confirm the table is catalogued, copy its **exact FQN**, list
  columns/types, check whether test cases already exist, and — after a run — verify test
  cases and their latest results.

These are for *checking*. The pipeline itself still does the actual create-and-push when
the user runs it. Prefer reading over assuming, always.

## Figure out what the user needs, then open the right reference

Load only the reference file you need:

| The user wants to… | Go to |
|---|---|
| Set up the pipeline for a brand-new database (from scratch) | `references/add-database.md` (scaffold from `assets/template_repo/`) |
| Add a new database as another source in an existing repo | `references/add-database.md` |
| Add data-quality checks for a table ("add a table") | `references/add-table.md` + `references/derive-rules.md` + `references/verify-mcp.md` |
| Change a check's query, `value_set`, or a table's columns | `references/add-table.md` (§ editing) |
| Use a check type not yet mapped (new expectation) | `references/derive-rules.md` (§ mapping) → add one line to `src/om.py` |
| Run the checks / diagnose a failed run | `references/run-and-troubleshoot.md` |
| Just inspect the DB or the catalog | `references/verify-mcp.md` |
| Understand how the whole thing fits together | `references/architecture.md` |

## Principles that keep this trustworthy (and why)

- **Only encode confirmed, unambiguous rules.** If a data dictionary flags something
  `[TBC]`, "belum terkonfirmasi", or "perlu konfirmasi tim product", leave it out. A check
  that fails on legitimate data trains people to ignore the whole dashboard — a missing
  check is safer than a wrong one.
- **Take the FQN from OpenMetadata, never construct it.** Results attach to a test case by
  its fully-qualified name; a guessed FQN silently targets the wrong thing or 404s. Copy
  the real one via the OM MCP.
- **Pull only the columns a check needs** (`columns_needed`). It's faster and keeps PII out
  of memory — several tables are marked `pii_flag: false` precisely because scoping is enforced.
- **`om.py` is the stable engine — you rarely touch it.** New tables and new databases never
  require editing it. It grows by exactly **one line** in `BUILTIN_DEFINITIONS` only when a
  genuinely new *kind* of check appears (see `derive-rules.md`).
- **It's idempotent (GET-first).** Re-running is safe: existing test cases are looked up and
  reused, and each run just adds a fresh result. So you can re-run freely while iterating.

## Most common task: add a table's checks

1. **Confirm the table in OpenMetadata and copy its exact FQN** (OM MCP `search_metadata`
   → `get_entity_details`). Grab the column list/types too. If the table isn't catalogued,
   tell the user — the pipeline can't attach checks to a table OM doesn't know about; stop here.
2. **Profile the data and read any data dictionary.** Use dbhub to count nulls, distinct
   values, and ranges for the columns you're considering; if a `data_dictionary_*`/
   `data_vocabulary_*` doc exists for the table, read it. See `references/derive-rules.md`.
3. **Choose only confirmed rules** and map each to a GX expectation. See `derive-rules.md`
   for the rule-type → expectation table and the recipes (`value_set_from` for FK checks,
   `not_in_future`, multi-column).
4. **Write** `config/tables/<source>.<schema>.<table>.yaml` by copying a shape from
   `assets/examples/`. Field-by-field schema is in `references/add-table.md`.
5. **Validate** it: `python scripts/validate_config.py <repo-root> <path-to-config.yaml>`
   — checks the structure and that every expectation maps in `BUILTIN_DEFINITIONS`, and
   flags anything that would crash the run before it touches the server.
6. **Hand the run to the user** (this skill is manual by design). Give them the command
   from `references/run-and-troubleshoot.md`, e.g.
   `python run_all.py config/tables/<source>.<schema>.<table>.yaml`.
7. **After they run, verify** the test cases were created and carry results (OM MCP) — see
   `references/verify-mcp.md`.

## Scaffolding a brand-new repo (new DB, from scratch)

If there's no pipeline repo yet, copy `assets/template_repo/` to the target folder — it's
the proven engine (`src/`, `run_all.py`, `config/connections.yaml`, `requirements.txt`,
`.env.example`) with an empty `config/tables/`. Then follow `references/add-database.md` to
point it at the new database, and add the first table with the workflow above. The bundled
engine is a working copy of a real deployment, so scaffolding is a copy-and-adjust, not a
rewrite.

## Reference index

- `references/architecture.md` — repo layout, data flow, the four-part mental model, why `om.py` is stable.
- `references/add-table.md` — the table-config YAML schema, editing, and the check recipes.
- `references/add-database.md` — add a source (`connections.yaml` + `.env`) or scaffold a new repo; driver notes.
- `references/derive-rules.md` — deriving rules from dictionaries + dbhub profiling; the confirmed-only discipline; rule→expectation→OM mapping and how to add a new mapping.
- `references/verify-mcp.md` — exact dbhub + OpenMetadata MCP checks, before and after a run.
- `references/run-and-troubleshoot.md` — manual run commands, expected output, and the common errors (403 perms, FQN mismatch, unmapped expectation) with fixes.
