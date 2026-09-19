# Checking the DB and the catalog with MCP

Use these read-only checks before writing a config (to match reality) and after a run (to
confirm it worked). `<source>` is the dbhub connection name for the database (e.g. `scm`).

## Before writing config

### Confirm the table + copy the exact FQN (OpenMetadata MCP)
- `mcp__OpenMetadata__search_metadata` with the table name → find the table entity.
- `mcp__OpenMetadata__get_entity_details` on it → copy the **fullyQualifiedName** verbatim
  into `table.fqn`, and read the **columns** (names + types). Note whether a testSuite or
  test cases already exist, so you know if the table is fresh.
- `mcp__OpenMetadata__get_test_definitions` → the built-in test definitions this server
  offers (useful when you need to add a new mapping in `om.py`).

### Profile the data (dbhub MCP) — `mcp__dbhub__execute_sql_<source>`
Run small, read-only queries to decide and validate rules:
```sql
-- shape
SELECT COUNT(*) AS rows FROM <schema>.<table>;
-- completeness of a column
SELECT COUNT(*) FILTER (WHERE <col> IS NULL) AS nulls FROM <schema>.<table>;
-- distinct values / candidate value set
SELECT <col>, COUNT(*) FROM <schema>.<table> GROUP BY <col> ORDER BY 2 DESC LIMIT 30;
-- numeric range (for a between / >= 0 rule)
SELECT MIN(<col>), MAX(<col>) FROM <schema>.<table>;
-- does a uniqueness rule actually hold?
SELECT COUNT(*) FROM (SELECT <col> FROM <schema>.<table> GROUP BY <col> HAVING COUNT(*) > 1) d;
-- FK orphans (for a value_set_from referential check)
SELECT COUNT(*) AS orphans
FROM <schema>.<table> c
WHERE c.<fk> IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM <schema>.<parent> p WHERE p.id = c.<fk>);
```
`mcp__dbhub__search_objects_<source>` finds tables/columns when you don't know exact names.

Rule of thumb: encode a rule only when profiling supports it. If a "unique" rule shows
duplicates or a ">= 0" rule shows negatives, that's either a real finding to raise with the
user or a sign the rule isn't confirmed — don't silently ship a check that will always fail.

## After a manual run — verify it landed
- OM MCP `get_entity_details` on the table (or `search_metadata` for its test cases) →
  confirm the expected test cases now exist and each shows a recent result (Success/Failed).
- If a check you expected is missing, or a result didn't update, see
  `run-and-troubleshoot.md`.

## A note on the two identities
The OpenMetadata MCP acts as the **user's** account (typically broad/admin) — great for
inspecting and confirming. The pipeline itself runs as a **bot token** with narrower rights.
So "I can see/create it via the MCP" does not guarantee "the bot can create it on a run" —
if a first run 403s on creation, it's the bot's permission, not the MCP's. See the 403 entry
in `run-and-troubleshoot.md`.
