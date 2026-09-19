# The data funnel

The funnel answers: **how many rows go in, how many come out of each step, and
what caused the difference.** It is the part of the artifact people screenshot.

## What each operation does to the row count

| step | effect | what to say |
| --- | --- | --- |
| table scan | the starting number | full size, or the pruned size if partitions were eliminated |
| `WHERE` | shrinks, never grows | what fraction failed, and whether NULLs were part of it |
| `INNER JOIN` on a unique key | shrinks or holds | how many rows found no match (orphans) |
| `INNER JOIN` on a non-unique key | **grows** | the average fan-out, e.g. "×3,4 — each order has 3,4 line items on average" |
| `LEFT JOIN` on a unique key | holds exactly | and how many got NULLs on the right |
| `LEFT JOIN` on a non-unique key | grows | same fan-out reasoning |
| `CROSS JOIN` | multiplies | left × right, spelled out |
| `EXISTS` / `IN` (semi-join) | shrinks, never grows | this is the fan-out-free alternative to a join |
| `NOT EXISTS` / `NOT IN` (anti-join) | shrinks | plus the NULL trap: one NULL in the inner set makes `NOT IN` return nothing |
| `GROUP BY` | collapses to one row per key combination | the grain: "one row per site per day" |
| aggregate with no `GROUP BY` | collapses to exactly 1 | |
| `HAVING` | shrinks the number of groups | |
| window function | **holds exactly** | say so explicitly; people expect it to filter |
| `QUALIFY` / `WHERE rn = 1` | shrinks | this is where the window's reduction actually happens |
| `DISTINCT` | shrinks | how many duplicates there were — and whether their existence is itself a bug |
| `UNION ALL` | **grows** — the sum of both branches | |
| `UNION` | grows, then shrinks by de-duplication | report both numbers if you can |
| `INTERSECT` / `EXCEPT` | shrinks | |
| `UNNEST` / `LATERAL` | **grows** | average expansion factor |
| `ORDER BY` | holds | worth a stage only when it precedes a `LIMIT` |
| `LIMIT n` | caps at n | and how many were discarded |
| `INSERT` / `UPDATE` / `DELETE` | rows written / changed | the final, most important number |

## Measuring it

Every engine here answers a counted prefix of the pipeline. Build the prefix up
to and including the step you want, and wrap it:

```sql
SELECT count(*) FROM ( <pipeline up to this step> ) t
```

Practical shape for a query with CTEs — keep the CTEs, replace the final select:

```sql
WITH recent AS (...), daily AS (...)
SELECT count(*) FROM daily;                          -- after the daily CTE
```

```sql
WITH recent AS (...), daily AS (...)
SELECT count(*) FROM daily d
JOIN sites s ON s.id = d.site_id;                    -- after the join
```

Discipline that keeps this cheap and safe:

- **Read-only.** Never execute the user's DML to find its row count. For an
  `INSERT … SELECT`, count the SELECT. For `UPDATE` / `DELETE`, count the same
  `FROM … WHERE` as a SELECT. Say in `notes` that nothing was written.
- **Keep every filter that prunes.** Dropping the date predicate to "get the
  base number" can turn a 31-partition read into a full-table scan. If you want
  the unpruned size, ask the catalog (`pg_class.reltuples`,
  `information_schema.TABLES.TABLE_ROWS`, `SHOW STATS FOR …`) rather than
  counting.
- **Batch the counts.** One statement per stage is fine on a warehouse; on a
  busy OLTP database, prefer a single query that computes several counts at once
  with conditional aggregation:
  `SELECT count(*) AS scanned, count(*) FILTER (WHERE status='PAID') AS kept FROM …`
  (`SUM(CASE WHEN … THEN 1 ELSE 0 END)` in MySQL).
- **Stop if it is slow.** If the first count takes minutes, switch to estimates
  for the rest and mark `"grounding": "schema"`. A half-measured funnel that
  says so beats a stalled session.

### Cheap approximations when exact counts hurt

- Trino: `SHOW STATS FOR (SELECT … )` gives row-count estimates without running
  the query; `approx_distinct()` for cardinality; `TABLESAMPLE BERNOULLI(1)`
  scaled ×100 for a rough shape.
- Postgres: `EXPLAIN` (no `ANALYZE`) gives the planner's row estimate per node —
  useful, but it is an estimate from statistics, so label it as one.
  `pg_class.reltuples` for table size.
- MySQL: `EXPLAIN` `rows` column, `information_schema.TABLES.TABLE_ROWS`
  (InnoDB: approximate, sometimes off by a lot — say so).

### Fan-out, measured directly

The single most valuable number in most funnels. Before reasoning about a join,
ask the key:

```sql
SELECT count(*) AS rows, count(DISTINCT join_key) AS keys FROM right_table;
```

Equal → unique key, no fan-out. `rows / keys` is the average multiplier, and
`max(cnt)` from a grouped count tells you the worst case, which is what
actually blows a query up.

## When there are no numbers to be had

If you cannot measure anything, cannot read a catalog statistic, and the person
gave you no figures, then the honest output has **no numbers in it**: no
`rows_in`, no `rows_out`, no `funnel`, and `"grounding": "none"`. The renderer
drops the funnel tab and strips stray counts, so the page never implies a
measurement that did not happen.

Resist the pull to fill the gap. A guessed selectivity reads exactly like a
measured one once it is set in a card, and the reader has no way to tell them
apart — which quietly poisons the numbers that *were* real. "About 40 000 rows"
in a report someone forwards to their director is a claim you cannot support.

What you write instead carries most of the value, because row *behaviour*
follows from the SQL itself:

| instead of a number | write the behaviour |
| --- | --- |
| "≈ 4 000 rows remain" | "only rows whose status is exactly `'PAID'` survive; NULL statuses are dropped too" |
| "×3,4 fan-out" | "if `order_id` is not unique in `payments`, each order is duplicated once per payment — check before trusting any SUM downstream" |
| "≈ 12 000 groups" | "collapses to one row per site per day, so the grain changes from transaction to site-day" |
| "keeps 5%" | "a top-N cut: everything below rank 20 is discarded, and with no tie-breaker the boundary is not deterministic" |

Then put the measurement plan in `notes`: the two or three counts that would
turn this map into a measured one, written so they can paste and run them.
That is more useful than an invented funnel, and it tells the person exactly
what you could not see.

## Partial grounding

Mixing is fine and common: measure the cheap stages, leave `rows` as `null` for
the ones you skipped — they render hatched and the page says they were not
measured. What is not fine is filling a gap by inference and letting it sit
next to a measured figure. Set `grounding` to the weakest level any number on
the page came from: one catalog estimate among live counts makes the page
`schema`, not `live`.

## Writing the `why`

The number is the claim; the `why` is the evidence. Aim at the mechanism:

- weak: "Filters the data." → says nothing.
- better: "Removes 95% of rows."→ reports, does not explain.
- good: "The date range lands on the partition column, so only 31 of ~640
  partitions are read — the rows are never fetched at all."

- weak: "Joins the tables."
- good: "`site_id` is unique in the master table, so this join adds columns
  without changing the row count; the 2 600 rows it drops are orphan ids present
  in the log but missing from the master — a data-quality issue, not intent."

Where a change is *absent*, say why it is absent. "Row count unchanged: a window
function computes over a frame but keeps every input row" is the stage that
teaches the most, because it is the one people get wrong.
