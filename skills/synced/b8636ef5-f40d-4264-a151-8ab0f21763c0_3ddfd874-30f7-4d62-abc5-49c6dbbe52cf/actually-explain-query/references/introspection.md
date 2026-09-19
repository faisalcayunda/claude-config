# Grounding the explanation in the real database

Reading a query's text tells you what it *says*. Reading the schema and a
little data tells you what it *does*. When a database MCP in the session can
reach the tables, spend a few calls before writing any explanation — it is the
difference between "filters by status" and "filters by a status value that
appears in 0,3% of rows, and nowhere in the last 90 days".

Tool names differ between setups. Go by capability, not by name: anything that
can list schemas, describe a table, or run a read-only query will do. Typical
shapes in this environment:

- **Trino** — `list_catalogs`, `list_schemas`, `list_tables`, `get_table_schema`,
  `execute_query`, `explain_query`.
- **Postgres / MySQL** — a SQL MCP with one tool per configured database
  (`execute_sql_<db>`, `search_objects_<db>` and similar). The database name in
  the tool name is usually how you pick the right connection.

If several connections could serve the query, ask which one — that is the one
question worth interrupting for, because the numbers are wrong if you guess.

## What to ask, in order

Each of these changes a sentence you are going to write. Stop when the query
has no more open questions; do not survey the whole warehouse.

**1 · Do the objects exist and what are their columns?**
`get_table_schema` / `DESCRIBE` / `information_schema.columns` for every table in
the query. Catches typos, stale column names, and a query written against a
table that has since changed shape. Put the relevant columns into the node's
`columns` array so the panel shows them.

**2 · Is each join key unique on the right side?**

```sql
SELECT count(*) AS rows, count(DISTINCT id_sppg) AS keys FROM master_sppg;
```

Equal means no fan-out. Otherwise `rows/keys` is the average multiplier — the
most useful single number you can put in a join node.

**3 · What values actually live in the filtered columns?**

```sql
SELECT status, count(*) FROM orders GROUP BY 1 ORDER BY 2 DESC LIMIT 20;
```

This is how you catch `'AKTIF'` vs `'aktif'`, a status that no longer exists,
or a filter that will match nothing. It is also where the selectivity number for
the funnel comes from.

**4 · How null is it?**

```sql
SELECT count(*) AS total,
       count(order_id) AS with_key,
       count(*) - count(ended_at) AS null_ended
FROM contracts;
```

NULLs decide whether a `WHERE`, a `NOT IN` or a join drops rows the author never
intended to drop.

**5 · How is the table physically laid out?** Partition and clustering columns
(Trino: `SHOW CREATE TABLE`, or the `$partitions` / `$properties` system tables;
Postgres: indexes via `pg_indexes`; MySQL: `SHOW INDEX`). This decides whether a
filter prunes or scans, which is usually the top line of the funnel.

**6 · What does the planner intend to do?** `explain_query` on Trino, `EXPLAIN`
on Postgres/MySQL. Read it for join order, broadcast vs partitioned joins, and
predicate pushdown, then describe what you found rather than guessing. Use plain
`EXPLAIN`, not `EXPLAIN ANALYZE`, which executes the query.

## Trino specifics

- Resolve `catalog.schema.table` fully. A bare table name is relative to the
  session catalog and schema, which you may not share.
- `SHOW STATS FOR (SELECT … WHERE …)` gives row-count and NDV estimates without
  running anything — the cheapest way to fill a funnel on a large table.
- Pushdown is the thing to check on a federated query: a filter that the
  connector can evaluate is cheap; one it cannot means every row crosses the
  network first. The EXPLAIN plan shows what was pushed into the source.
- `information_schema` exists per catalog: `hive.information_schema.columns`.

## Postgres specifics

- `pg_class.reltuples` / `pg_stat_user_tables.n_live_tup` for fast table sizes.
- Partial and expression indexes change which filters are cheap; `pg_indexes`
  shows the definitions.
- Beware `EXPLAIN` estimates on a table that has not been analysed recently —
  they can be far off, so label them as planner estimates.

## MySQL specifics

- `information_schema.TABLES.TABLE_ROWS` is an InnoDB approximation, sometimes
  off by tens of percent. Use exact `count(*)` for small tables and say
  "approximate" for large ones.
- Collation matters: on a default `utf8mb4_0900_ai_ci` column, `= 'AKTIF'`
  matches `aktif`. If the user is debugging a filter that "should not match",
  this is often the answer.
- Check `ONLY_FULL_GROUP_BY` in `@@sql_mode` when the query selects a
  non-aggregated column that is not in `GROUP BY` — without it, MySQL returns an
  arbitrary row per group and the result is quietly non-deterministic.

## Rules

- **Read-only, always.** SELECT, SHOW, DESCRIBE, EXPLAIN. Never execute the
  user's INSERT / UPDATE / DELETE / MERGE, never `EXPLAIN ANALYZE` on DML,
  never create a temp table to "test" something.
- **Bound every probe.** `LIMIT` on samples, a date filter on anything large,
  `approx_distinct` instead of `count(DISTINCT …)` on a huge Trino table.
- **Never paste raw rows into the artifact.** You are explaining a query, not
  exporting data. Aggregates, counts and column names are what belong there;
  if you sample rows to understand a column, keep them out of the output.
- **Say what you did.** Set `"grounding"` honestly and put the date of the
  counts in `notes` — row counts age, and someone will read this page in three
  months.
- If a probe fails or the connection is not there, note it once and continue
  with reasoning. Do not retry a dead connection or stall the whole explanation
  on one missing number.
