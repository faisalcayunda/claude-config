# Mapping complex SQL onto nodes

The map is only useful if its shape matches what the engine really does. This
file covers the constructs where a naive reading goes wrong.

## Contents

- [The spine](#the-spine)
- [CTEs](#ctes)
- [Recursive CTEs](#recursive-ctes)
- [Subqueries](#subqueries)
- [Joins that fan out](#joins-that-fan-out)
- [Window functions](#window-functions)
- [Set operations](#set-operations)
- [UNNEST, LATERAL and row expansion](#unnest-lateral-and-row-expansion)
- [Cross-catalog queries (Trino)](#cross-catalog-queries-trino)
- [DML](#dml)
- [Dialect differences that change the explanation](#dialect-differences-that-change-the-explanation)
- [Keeping a big query readable](#keeping-a-big-query-readable)

## The spine

Every SELECT becomes a chain in logical order:

```
source(s) → join(s) → where → groupby → having → window → qualify
          → distinct → select → orderby → limit
```

Skip what is not there. Never emit a node for a clause the query does not have,
and never merge two clauses into one node — the funnel needs each one to be its
own measurable stage.

The `select` node earns its place even though it changes no rows: it is where
people look to see what comes out. Give it a `plain` line about the shape of
the output, and say explicitly when it changes columns but not rows.

## CTEs

Each `WITH` block becomes its **own chain of nodes**, ending in a single node of
kind `cte` labelled `CTE: name`. Give every node in that chain the same `group`
so the box reads as one unit — including the tables the block reads, not just
its operations. A table whose only consumer is a join inside the block is part
of the block; leaving it ungrouped parks it outside a box it visibly belongs to.

The `cte` node is the hand-off point. Wherever the main query references the
CTE by name, draw an edge **from the `cte` node** to the consuming step instead
of creating a second source node for it. That is what makes reuse visible: a
CTE referenced three times has three outgoing edges, and the reader immediately
sees that the work is done once and consumed three times — or, if the engine
inlines it, three times, which is worth a note when the CTE is expensive.

A CTE that is never referenced is dead code. Map it, then say so in `notes`.

## Recursive CTEs

`WITH RECURSIVE name AS (anchor UNION ALL recursive_step)` has three parts:

1. the **anchor** (seed) chain — map it normally,
2. a `union` node where both branches meet,
3. the **recursive step** chain, whose self-reference to `name` is *not* a table
   node. Instead draw the feedback edge:

```json
{"from": "cte_chain", "to": "j_step", "kind": "cte", "recursive": true}
```

pointing from the `cte` node back to the first step of the recursive branch.
The renderer loops it around the right-hand side and keeps it out of the layout.

Things worth putting in `detail` here, because they are what actually bites:
the termination condition and what happens without one (Postgres and Trino will
run until they exhaust memory on a cyclic graph), the depth guard, and the fact
that the funnel number for the union node is the *accumulated* total across all
rounds rather than a single pass.

## Subqueries

Three different things wear the same syntax, and they get different kinds:

- **In FROM** — a derived table. Map its internals as a chain, end it in a node
  of kind `subquery` labelled `subquery (alias)`, and feed that into the outer
  query. Row counts flow through it unchanged.
- **In WHERE as EXISTS / IN / NOT IN** — a filter, kind `semijoin`. This never
  duplicates rows, which is exactly why it is often the right fix for a join
  that fans out. `NOT IN` deserves a warning in `detail` whenever the inner
  column is nullable: a single NULL makes `NOT IN` return no rows at all, which
  is the most quietly destructive behaviour in everyday SQL.
- **In the SELECT list** — a scalar subquery, kind `subquery` feeding the
  `select` node. Note in `detail` whether it is correlated: a correlated scalar
  subquery runs per outer row, which is usually the performance answer people
  were looking for.

## Joins that fan out

A join node's `detail` must always answer one question: **can this multiply
rows?** The answer depends on whether the right-hand key is unique, which you
can only know from the schema or from a count — see `introspection.md`. Say
which of the three it is (cannot / does / unverified-with-this-check); leaving
it out reads as reassurance you did not earn.

Watch for the joins that look harmless. A dimension table joined "just to pick
up a rate" or "just for the name" is exactly where history tables bite: one row
per merchant *per contract period*, one row per product *per price change*. If
the join has no predicate narrowing it to the current row — no validity window,
no `is_current` flag — treat fan-out as the likely case, not the edge case.

| situation | effect on row count |
| --- | --- |
| right key unique (PK / unique index) | rows in = rows out for INNER on a matching key; LEFT keeps every left row |
| right key not unique | **multiplies**: each left row × its matches. State the average fan-out if you measured it. |
| INNER JOIN | drops left rows with no match — orphan keys. Quantify them; they are usually a data-quality finding, not intent. |
| LEFT JOIN | never drops left rows — unless a later `WHERE` tests a right-hand column, which silently converts it to an inner join. Flag this every time you see it. |
| CROSS JOIN, or a join whose ON is always true | full cartesian product |
| FULL OUTER | can exceed both inputs |

Multiple joins chain: each join node takes the accumulated result plus one new
source. Do not draw a single node for three joins.

## Window functions

`kind: "window"`, one node per distinct `OVER` clause (several functions sharing
the same window can share a node — say so in the label).

The whole point to communicate: **a window function changes no rows.** It adds a
column. People consistently expect `row_number()` to filter; it does not. The
filtering happens later, in `WHERE rn = 1` or in `QUALIFY`, and that later step
is where the funnel drops. Make the pair visible: the window node with equal
`rows_in`/`rows_out`, then the filter node with the real reduction.

Worth a sentence in `detail` when relevant: the frame. `ORDER BY` inside a
window without an explicit frame defaults to `RANGE UNBOUNDED PRECEDING AND
CURRENT ROW`, which makes a running total behave differently from the
`ROWS`-framed version people assume, especially with ties.

## Set operations

`UNION` / `UNION ALL` / `INTERSECT` / `EXCEPT` become one node with both branches
feeding in. This is the only common family of operations that *adds* rows, so
the funnel usually shows an increase here.

Always distinguish the two in `detail`: `UNION ALL` concatenates and is cheap;
`UNION` de-duplicates, which costs a full sort or hash of the combined set and
can quietly be the most expensive step in the query. If the branches cannot
produce duplicates, `UNION` is paying for nothing — that is a note.

## UNNEST, LATERAL and row expansion

`kind: "unnest"`. These are the steps that legitimately multiply rows: one input
row becomes one row per array element (`CROSS JOIN UNNEST` in Trino, `LATERAL`
in Postgres, `JSON_TABLE` in MySQL 8). Say what the multiplier is if you can
measure the average array length; "each order expands into its line items,
averaging 3,4 rows each" is exactly the sentence the funnel needs.

`LEFT JOIN UNNEST … ON TRUE` (or `WITH ORDINALITY`) preserves rows with empty
arrays; plain `CROSS JOIN UNNEST` drops them. That difference silently changes
totals and belongs in `detail`.

## Cross-catalog queries (Trino)

Use `kind: "catalog"` for any source whose identifier is `catalog.schema.table`
where the catalog differs from other sources in the query, and put the catalog
name in `badges`. The reader's key question is *where does the data physically
come from and what has to move.*

Things worth explaining in `detail` on those nodes:

- A join between two catalogs means rows cross systems. Trino pushes down what
  it can — filters, sometimes aggregations — and pulls the rest across the
  network. Which side gets pushed down determines whether the query is fast.
- Filters on partition columns of a Hive/Iceberg/Delta catalog prune whole
  partitions before any data is read. This is normally the single biggest
  reduction in the funnel and is worth naming explicitly.
- A small table joined to a huge one is usually broadcast to every worker; a
  large-to-large join is partitioned and shuffled. If `explain_query` is
  available, read the plan and say which one happened rather than guessing.
- Connectors differ in what they support. A `LIKE` or a function call that
  cannot be pushed into the source becomes a full read plus a filter in Trino.

## DML

Explain it; do not run it. Map the SELECT side of an `INSERT … SELECT` in full,
then `insert` → `insert_target`. For `UPDATE`: source → `where` → `set` →
`update`. For `DELETE`: source → `where` → `delete`. `MERGE` gets one `merge`
node with the matched / not-matched branches described in `detail`.

The funnel for DML ends with **rows written**, and that is the number the person
cares about. A missing `WHERE` on an UPDATE or DELETE is the single most
important thing you can tell them — put it first in your reply, not only in
`notes`.

## Dialect differences that change the explanation

| | PostgreSQL | MySQL | Trino |
| --- | --- | --- | --- |
| row cap | `LIMIT n OFFSET m`, `FETCH FIRST` | `LIMIT m, n` — the two numbers are reversed | `LIMIT n`, `OFFSET m`, `FETCH FIRST` |
| window filter | no `QUALIFY`; wrap in a subquery | no `QUALIFY`; 8.0+ has window functions | `QUALIFY` |
| de-dup on a key | `DISTINCT ON (col)` | no equivalent — emulated with `row_number()` | no `DISTINCT ON`; use `row_number()` |
| recursive CTE | `WITH RECURSIVE` | `WITH RECURSIVE` (8.0+) | `WITH RECURSIVE`, bounded by `max_recursion_depth` |
| `GROUP BY` leniency | strict | with `ONLY_FULL_GROUP_BY` off, a non-aggregated column returns an arbitrary row — a real correctness trap worth flagging | strict |
| string compare | case-sensitive, collation-dependent | commonly case-**insensitive** (`utf8mb4_0900_ai_ci`), so `= 'AKTIF'` matches `aktif` | case-sensitive |
| `||` | concatenation | logical OR unless `PIPES_AS_CONCAT` | concatenation |
| arrays / structs | arrays, `unnest` | JSON functions, `JSON_TABLE` | arrays, maps, rows, `UNNEST` |
| federation | via FDW | none | native, multi-catalog |

When the dialect is not stated, infer it from the syntax (`QUALIFY` or
`catalog.schema.table` → Trino; backticks or `LIMIT m, n` → MySQL; `::` casts or
`DISTINCT ON` → Postgres) and say which you assumed in `notes`.

## Keeping a big query readable

Above roughly 25 nodes the diagram stops being a glance. Options, in order of
preference: keep every step but lean on `groups` so each CTE reads as one block;
collapse a chain of trivially sequential projections into one node whose label
names both; or, for a genuinely enormous query, map the top-level structure and
say in `notes` which block was summarised and why. Never silently drop a step
that changes the row count — that is the one thing the funnel cannot survive.
