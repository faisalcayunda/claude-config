# Running manually + troubleshooting

## First-time setup
```bash
pip install -r requirements.txt      # ideally in a fresh venv/conda env
cp .env.example .env                 # then fill real DSNs + OM_HOST + OM_TOKEN
```

## Run
```bash
python run_all.py                                          # every table config
python run_all.py config/tables/scm.<schema>.<table>.yaml  # just one table
```
Expected output: `=== schema.table ===`, `Loaded N rows.`, then one `[PASS]`/`[FAIL]` line
per check. On a table's first run the test cases are created, then results pushed;
re-running is safe (idempotent — existing cases are reused, a fresh result is added). The
`absl` / `grpc` lines at startup are harmless GX/protobuf noise.

`[PASS]`/`[FAIL]` is a data-quality outcome — a `[FAIL]` means the data violated the rule,
which is often a real finding worth surfacing. An exception that stops the run is a
pipeline error — see below.

## Manual by design
This skill does not schedule anything. If the user wants this to run on a schedule
(cron / Airflow), that's the separate scheduling skill — point them there and stop.

## Common errors and fixes
- **`403 ... "User does not have ANY of the required permissions"` on `POST .../testCases`** —
  the bot token can read and push results but cannot *create* test cases, and this table's
  checks don't exist yet. Fix: an OpenMetadata admin grants the bot `Create` on the
  `testCase` resource (add the `Create` operation to the bot's allow policy/role), or
  pre-create the checks once via the OM UI. Note `EditAll` does **not** include `Create` —
  they are separate operations, so a policy with EditAll+ViewAll still can't create.
- **`404` on push, or results landing on the wrong test** — the `table.fqn` in the YAML
  doesn't match OpenMetadata. Re-copy the exact FQN via the OM MCP (see `verify-mcp.md`).
- **`KeyError: No BUILTIN_DEFINITIONS mapping for expectation '...'`** — a check uses an
  expectation type not mapped yet. Add one line to `src/om.py` (see `derive-rules.md`, Step 4).
- **`value_set_from` query error** — the referenced `source` isn't in `connections.yaml`,
  or the SQL is wrong. Test the query with dbhub first.
- **DB connection / SSL error** — the DSN in `.env` is wrong or the database isn't reachable
  from where you're running. Confirm connectivity with dbhub.
- **A Great Expectations kwargs error** — a check's `kwargs` shape is off (e.g. a wrong
  key). Compare against the shapes in `add-table.md`.

## Quick pre-flight
Before handing a run to the user, run the offline validator — it catches structural and
mapping problems without touching the network:
```bash
python scripts/validate_config.py <repo-root> config/tables/<the-new-config>.yaml
```
