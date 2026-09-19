# Architecture — how the pipeline fits together

## Repo layout
```
gx_data_quality/
├── run_all.py              # entry point: python run_all.py [config/tables/x.yaml]
├── requirements.txt
├── .env                    # secrets (never committed): DB DSNs, OM_HOST, OM_TOKEN
├── config/
│   ├── connections.yaml    # source name -> env var; OM host/token env names
│   └── tables/*.yaml       # ONE file per table = the checks for that table
└── src/
    ├── db.py               # query_df(source, sql) via psycopg2
    ├── om.py               # all OpenMetadata REST logic (the stable engine)
    └── runner.py           # generic engine: read YAML -> GX -> om.py
```

## Data flow (per table)
Postgres → runner pulls `columns_needed` → Great Expectations computes pass/fail → for each
check `om.ensure_test_case()` resolves the test case's FQN (GET-first; creates if missing
and permitted) → `om.push_result()` stamps pass/fail → OpenMetadata's Data Quality tab
shows it.

## The four-part mental model (what changes when)
- **config/** — where growth happens: new tables, new databases.
- **db.py** — how to read source data. Changes only for a new driver or a large-table SQL mode.
- **runner.py** — the recipe interpreter. Changes only for new recipes (e.g. a custom query).
- **om.py** — the OpenMetadata adapter. Changes only for a new check *type* (one dict line) or a different OM server.

## Why om.py is stable
It receives a generic `(check, table_cfg, column)` plus a result; nothing is hardcoded to a
table or database. `BUILTIN_DEFINITIONS` maps each GX expectation to an OM built-in test;
that dict grows by one line when a new expectation type first appears, and never otherwise.
New tables and new databases never require editing it.

## om.py internals (brief)
- `_client()` — one authenticated OM session (OM_HOST/OM_TOKEN).
- `_ensure_test_suite()` — makes the table's test suite exist (only needed when creating).
- `BUILTIN_DEFINITIONS` + `_*_params` helpers — GX expectation → OM built-in + parameters.
  Three multi-column checks map to the generic `tableCustomSQLQuery` with a readable SQL
  string (documentation only; GX computes the real result).
- `_find_existing_fqn(entity_link, name, raise_if_missing)` — look up a test case by exact
  entityLink + name; return its real FQN, or None.
- `ensure_test_case()` — GET-first: return the existing FQN; only POST-create when missing;
  raise a clear, actionable error if creation is refused.
- `push_result()` — POST the pass/fail result (current API, with a legacy fallback).

## Permissions note
The pipeline authenticates as a bot token (`OM_TOKEN`). It needs Read + push-result on test
cases always, and `Create` on `testCase` only to auto-create checks for a brand-new table.
See `run-and-troubleshoot.md` for the 403 case and the fix.
