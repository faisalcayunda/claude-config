# Spec contract

The renderer takes one JSON file and owns everything visual. You own the
content. Anything you leave out simply does not render — there are no required
fields beyond `nodes` and `edges`, but a spec without `sql`, `summary` and
`funnel` throws away most of the value.

```bash
python3 scripts/render_query_map.py spec.json -o query_map.html
python3 scripts/render_query_map.py spec.json --validate-only   # counts only, no file
python3 scripts/render_query_map.py spec.json -o map.html --standalone  # openable local file
```

The script warns on unknown node kinds and fails loudly on an edge that points
at a node id that does not exist — both are worth fixing rather than ignoring.

## Top level

| key | type | what it does |
| --- | --- | --- |
| `title` | string | Shown in the header and as the artifact title. Name the query's *purpose*, not its syntax: "Top SPPG by daily portions", not "SELECT with CTE". |
| `dialect` | `postgres` · `mysql` · `trino` · `generic` | Picks the documentation links and the engine label. |
| `lang` | `en` · `id` | Language of the page's own labels, the built-in definitions and the docs link. `id`, `ID`, `indonesia` and `bahasa indonesia` all resolve to Indonesian. Your sentences must match it — the renderer warns if the prose and the flag disagree. |
| `grounding` | `live` · `stated` · `schema` · `none` | Where the numbers came from, printed under the funnel. `live` = you ran the counts. `stated` = figures the person gave you. `schema` = catalog statistics, approximate. `none` = nothing measurable, which makes the renderer strip every row count and hide the funnel tab. Set it to the weakest level any number on the page came from. |
| `direction` | `TB` · `LR` | Which way the diagram runs on first load — top-to-bottom (default) or left-to-right. The reader can flip it at any time with the arrow button in the canvas controls; this only picks the starting view. |
| `sql` | string | The original query, verbatim. Drives the code pane and the click-to-highlight. |
| `summary` | string | 2–4 sentences: what the query is *for*, in the Brief tab. Supports `` `code` `` and `**bold**`. |
| `nodes` | array | The steps. |
| `edges` | array | How rows flow between them. |
| `groups` | array | Optional visual clusters, one per CTE or logical block. |
| `funnel` | array | The row-count story, top to bottom. Omit it entirely when you have no real numbers — the funnel tab then disappears rather than rendering empty. |
| `notes` | array of strings | Assumptions, risks, data-quality findings. Shown in the Brief tab. |

## Node

```json
{
  "id": "w_status",
  "kind": "where",
  "label": "WHERE o.status = 'PAID'",
  "plain": "Keeps only orders that were actually paid for.",
  "detail": "Rows where `status` is NULL are dropped as well — a comparison against NULL is never true — so orders that were refunded before settlement disappear here rather than at the refund step.",
  "sql_span": "WHERE o.status = 'PAID'",
  "group": "g_recent",
  "rows_in": 19800000,
  "rows_out": 4120000,
  "delta_note": "79% of rows fail the status test; 210 000 of those are NULL rather than an explicit non-paid state.",
  "columns": ["order_id", "status", "total"],
  "badges": ["hive", "partitioned: dt"],
  "title": "override the panel heading, rarely needed"
}
```

- `id` — any stable string; used by edges and funnel stages.
- `kind` — see the table below. It drives colour, icon and the encyclopedia
  definition shown in the panel, so pick the one that matches what the engine
  is doing, not what the clause is called.
- `sql_span` — a fragment of `sql` to highlight when the node is clicked.
  Whitespace-insensitive, first match wins. Use the shortest fragment that is
  unique; if a fragment repeats (two identical `UNION ALL`s), extend it with the
  following line. `"span": [start, end]` sets character offsets directly when
  that is easier.
- `rows_in` / `rows_out` — numbers (not strings) so the page can compute deltas.
  Omit both when you have no basis for a number; do not invent one.
- `badges` — short chips on the card: the catalog, the partition column, the
  join strategy, `NOT NULL`, whatever a reader would want at a glance.
- `columns` — the columns this step touches, ideally from live introspection.

## Node kinds

| kind | use for | colour family |
| --- | --- | --- |
| `table` | a plain table or view read in FROM | green |
| `catalog` | a source in a different catalog (Trino federation) — worth distinguishing so the reader sees data crossing systems | green |
| `subquery` | an inline subquery in FROM acting as a source | green |
| `cte` | the named result of a WITH block (one per CTE, at the end of its subgraph) | teal |
| `join` | INNER / LEFT / RIGHT / FULL / CROSS join | teal |
| `semijoin` | EXISTS, IN, NOT IN used as a filter — never fans out | teal |
| `unnest` | UNNEST, LATERAL, JSON_TABLE, array expansion — can multiply rows | teal |
| `where` | row filter before grouping | yellow |
| `having` | group filter after aggregation | yellow |
| `qualify` | window-result filter (Trino) | yellow |
| `select` | projection / column shaping | blue |
| `window` | any OVER (…) computation | blue |
| `groupby` | GROUP BY with aggregates | pink |
| `aggregate` | aggregate with no GROUP BY (collapses to one row) | pink |
| `distinct` | DISTINCT / DISTINCT ON de-duplication | grey |
| `orderby` | sorting | purple |
| `limit` | LIMIT / FETCH / TOP | grey |
| `union` `intersect` `except` | set operations | purple |
| `values` | literal VALUES rows | purple |
| `insert` `update` `delete` `merge` | DML operations | orange / red |
| `insert_target` | the table receiving an INSERT | green |
| `set` | the SET clause of an UPDATE | yellow |
| `returning` | RETURNING clause | pink |
| `create` `column` | DDL and its column definitions | green / grey |
| `result` | optional final "what the caller gets" node | blue |
| `operation` | anything else | blue |

## Edge

```json
{"from": "w_status", "to": "gb_day", "kind": "groupby", "recursive": false}
```

`kind` only sets the colour; omit it and the edge takes the colour of the node
it points at, which is usually what you want. Set `"recursive": true` on the
feedback edge of a recursive CTE — it is drawn as a loop around the right side
of the diagram and is excluded from the layout so it cannot distort it.

Direction is the direction rows travel. Every node except the sources should
have at least one incoming edge, or it will float at the top of the diagram
disconnected from the story.

## Group

```json
{"id": "g_recent", "label": "CTE: recent_orders"}
```

Nodes carrying `"group": "g_recent"` are drawn inside a labelled box. Use one
group per CTE and per major block.

Membership decides the box, so put **everything that belongs to the block in
it**, including the tables it reads. A lookup table whose only consumer is a
join inside the block belongs in the block; left out, it ends up parked beside
a box it clearly belongs to. The layout keeps non-members outside every box and
pulls overlapping boxes apart, and the renderer warns when a node still lands
inside a box it does not belong to — that warning almost always means a missing
`group` on a source node.

Groups are cosmetic. If a group's members genuinely belong in different parts
of the diagram, the box will be large and awkward; drop the group rather than
fight it.

## Funnel stage

```json
{"node": "gb_day", "stage": "GROUP BY sppg_id, date", "rows": 742000,
 "why": "18,35M transactions collapse into one row per site per day."}
```

Ordered top to bottom, following the main path of the data. Include the stages
where the number *moves*, plus the stages where a reader would expect it to
move and it does not — a window function that keeps every row is worth a stage
precisely because it surprises people.

`rows` may be `null` when a stage was not measured; the bar renders hatched and
the page says so. If *no* stage has a real number, drop the `funnel` array and
set `"grounding": "none"` instead of building a funnel out of guesses — the
renderer enforces that anyway, and warns when it has to strip something. Bar lengths are logarithmic, so a funnel that runs from 400M
to 20 rows stays readable; the printed numbers are exact.

`stage` is a short name for the left pane, not a repeat of the full SQL.
`why` is the sentence that earns the whole feature — name the mechanism.

## Worked examples

Both layouts are computed at render time, so the direction button in the page
switches instantly and the boxes, edges and funnel stay correct either way. A
long linear pipeline reads best top-to-bottom; a query with few steps but many
parallel branches usually reads better left-to-right.

`examples/trino_complex.json` — federated Trino query: two catalogs, three CTEs
(including a semi-join and a window function), measured funnel, Indonesian.

`examples/pg_recursive.json` — recursive Postgres CTE with a feedback edge,
UNION ALL of two branches, INSERT … RETURNING, estimated funnel, English.

Copy their shape. They are both complete and both render.
