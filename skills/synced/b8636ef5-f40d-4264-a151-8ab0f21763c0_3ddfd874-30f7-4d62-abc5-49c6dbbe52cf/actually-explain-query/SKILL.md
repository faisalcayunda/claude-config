---
name: actually-explain-query
description: Explain and visualise any SQL query as an interactive logic map artifact — every step as a plain-language node, plus a data funnel showing how many rows survive each stage and why. Works on PostgreSQL, MySQL and Trino, including CTEs, recursive CTEs, subqueries, window functions, set operations and cross-catalog federated queries. Use this whenever someone pastes a query and asks what it does, why it is slow, why the numbers look wrong, whether it is safe to run, to review or document a query, or to walk a non-engineer through one, or to hand the explanation over as a PDF — even if they only say "check this query" or "apa maksud query ini" and never mention diagrams or visualisation.
---

# actually-explain-query

Someone hands you a query. They usually cannot tell, by reading it, what it
actually does to their data — where rows disappear, where they multiply, which
filter does the real work. Your job is to answer that question **visually and
concretely**, as a published artifact they can click through, not as an essay.

The output is a single interactive page: a top-to-bottom logic map where every
step is a card in plain language, a code pane that highlights the matching SQL
when a step is clicked, and a **data funnel** that tracks how many rows enter
and leave each stage and explains the mechanism behind every change.

You do not need a SQL parser. You read SQL better than one — and unlike a
parser you can reason about what a join key means, whether a filter will
actually match anything, and why a number moves. A bundled script owns the
layout and rendering so every explanation comes out looking the same; you own
the analysis that fills it.

## The loop

1. **Decompose** the query into steps.
2. **Ground** it against the real database if you can reach one.
3. **Count** the funnel — measured if possible, reasoned if not.
4. **Build the spec, render, publish**, then say the two or three things that matter.

Start immediately; do not ask permission or propose a plan first. The only
question worth asking up front is which database to connect to, and only when
several are plausible and the answer changes the numbers.

---

### Language

Write the whole explanation in the language the person is using. If they wrote
to you in Indonesian, or asked for Indonesian output in any wording ("pakai
bahasa Indonesia", "jelasin dalam bahasa Indonesia"), set `"lang": "id"` in the
spec and write every `plain`, `detail`, `summary`, `why` and `note` in
Indonesian. That flag is what switches the page's own furniture — the tab
names, the funnel headings, the built-in definition of each SQL construct and
the documentation link — so a spec written in Indonesian with the flag left at
its default renders as a bilingual mess. The renderer warns when it spots that
mismatch; take the warning seriously rather than shipping it.

## 1 · Decompose

Walk the query in **logical execution order**, not the order it is written:

```
FROM / source  →  JOIN  →  WHERE  →  GROUP BY  →  HAVING
   →  window functions  →  QUALIFY  →  DISTINCT  →  SELECT  →  ORDER BY  →  LIMIT
```

One node per operation the engine performs. Each node carries three pieces of
writing, and they do different jobs:

| field    | job | example |
| -------- | --- | ------- |
| `label`  | the literal SQL fragment, so the step is findable in the code | `WHERE o.status = 'PAID'` |
| `plain`  | one short sentence, on the card, about what happens to the **data** | `Keeps only orders that were actually paid for.` |
| `detail` | 2–4 sentences in the side panel: the mechanism, the trap, the consequence | `Rows with status NULL are dropped too — a NULL comparison is never true, so cancelled-then-refunded orders silently vanish here.` |

**Every join node owes the reader a fan-out verdict.** A join is the only
common step that can silently multiply every number downstream, and nobody can
tell which way it goes by reading the SQL — it depends on whether the key is
unique on the right-hand side. So each join's `detail` ends in one of three
statements, and none of them is optional:

- *cannot multiply* — and why: "`users.user_id` is the primary key, so this
  attaches columns without changing the row count";
- *does multiply* — with the factor if you measured it: "`payments` holds one
  row per attempt, averaging 1,3 per order, so `count(*)` and every `sum()`
  below are inflated by that much";
- *not verified* — with the check that settles it: "if `fee_schedules` keeps
  rate history there is more than one row per merchant and every amount below
  is multiplied; confirm with `select count(*), count(distinct merchant_id)
  from fee_schedules`".

The third is a perfectly good answer when you have no database. What is not
acceptable is saying nothing, because silence reads as "this join is fine".
The same duty applies to the aggregates above it: when a join can fan out, say
which measures it corrupts (`count(*)`, `sum(...)`) and which survive
(`count(DISTINCT ...)`, `max(...)`) — that asymmetry is usually why a broken
report looked internally consistent for months.

Write `plain` about rows, not about syntax. "Filters the rows" is a restatement
of the keyword and teaches nothing; "Throws away every order older than 30 days
— that is 94% of the table" is the sentence someone actually needed.

CTEs, subqueries, set operations, window functions, recursion, UNNEST and
cross-catalog reads each have a shape worth getting right, and dialects differ
in ways that change the answer. **Read `references/decomposition.md`** before
you map anything more complicated than a single SELECT with joins — it covers
each shape, the node kinds to use, and the mistakes that make a map misleading.

## 2 · Ground it

A query explained from its text alone is a guess about names. Explained against
the live schema it becomes a statement about data. When the session has a
database MCP that can reach these tables — a Trino MCP (`list_catalogs`,
`get_table_schema`, `execute_query`), a Postgres/MySQL SQL MCP, anything that
can run a read query — use it before you write a single explanation.

What to look up, in priority order, because each one changes what you write:

- **Join key uniqueness, for every join in the query.** This single fact decides
  whether a join keeps the row count flat or multiplies it. It is the most
  common source of "why is my total suddenly 3× too big", and you cannot know it
  from the SQL text. One count settles it:
  `select count(*), count(distinct <key>) from <right table>` — equal means no
  fan-out, and the ratio is the multiplier. Run it for each join before you
  write a word about that step; when you cannot, the node says so rather than
  assuming the safe answer.
- **Column meaning and enum values.** `status = 'AKTIF'` is worth checking:
  if the column only ever holds `aktif` lowercase, the query returns nothing and
  that is the finding.
- **NULL rates** on filtered and joined columns — the quiet row-killer.
- **Partitioning / clustering**, especially on Trino and Hive-backed catalogs:
  whether a date filter prunes partitions or triggers a full scan.
- **Row counts**, which feed the funnel.

Read-only always. Never run the user's INSERT, UPDATE, DELETE or MERGE to find
out what it does — explain it, and say plainly that you did not execute it.
`references/introspection.md` has the concrete call sequences per engine, the
cheap ways to answer each question, and how to stay out of trouble on a big
warehouse.

If nothing is reachable, say so once in the artifact's notes and keep going.
The map is still worth far more than no map — it just carries no row counts,
for the reason spelled out in the next step.

## 3 · Count the funnel — only when there is something to count

When you have real numbers, this is the part people remember: for every stage
the artifact shows rows in, rows out, the delta, and **why it changed**.

The reliable way to get them is to run each prefix of the pipeline as its own
count, which any engine will answer:

```sql
SELECT count(*) FROM (<the query up to and including this step>) t
```

A number on this page is a claim about someone's data, and they will quote it
in a meeting. So put a row count on the page only when it comes from one of
three places:

- a **measurement** you ran (`grounding: "live"`),
- a **catalog statistic** — `SHOW STATS`, `reltuples`, `information_schema`
  (`grounding: "schema"`, and say it is approximate),
- a **figure the person gave you** in their message, or in a file, screenshot
  or previous result they shared (`grounding: "stated"`).

**If none of those are available, leave every number out.** Omit `rows_in`,
`rows_out` and the whole `funnel` array, and set `"grounding": "none"`. The
renderer enforces this — with grounding `none` it strips any stray numbers, and
the funnel tab disappears entirely rather than showing an empty shell. A page
with no funnel is an honest page; a funnel built from plausible-looking guesses
is worse than no funnel at all, because it looks measured and nobody can tell
which figures were real.

That does not make an ungrounded map weak. Row *behaviour* is knowable from the
SQL alone, and it is most of what people need:

- direction — "this step can only shrink the set; it never adds rows"
- mechanism — "an inner join on a non-unique key multiplies: one left row
  becomes one per match"
- risk — "if `kpm_dikecualikan.id_kpm` contains a single NULL, `NOT IN` makes
  this return nothing at all"
- what to check — "run `select count(*), count(distinct id) from …` to find
  out whether this join fans out"

Write that into `plain` and `detail` instead of a number, and point out in
`notes` which counts would settle the open questions. You are handing them the
measurement plan rather than pretending you already ran it.

The mechanism matters more than the number even when you do have numbers.
"742 000 rows" tells them nothing; "18,35M transactions collapse into 742K
SPPG–day pairs, roughly 35 300 sites × 21 operating days" tells them whether
the number is right. Every `why` and `delta_note` should name what moved it:
partition pruning, an inner join dropping orphans, a fan-out from a non-unique
key, a NULL-swallowing comparison, the aggregation grain.

Partial grounding is normal and fine — measure what is cheap, and leave
`rows` as `null` for the stages you could not measure rather than filling the
gap by inference. Set the spec's `grounding` to the weakest level any number on
the page came from, so the label never overstates.

`references/funnel.md` has the probe templates per dialect, the rules for which
operations can grow, shrink or preserve row count, and how to write a stage
that carries its meaning without a figure.

## 4 · Build, render, publish

Write a spec JSON, then render it:

```bash
python3 scripts/render_query_map.py spec.json -o query_map.html
```

The spec is small and self-describing — nodes, edges, funnel stages, notes.
**`references/spec-schema.md` is the contract**: every field, every node kind
with its colour and icon, and a worked example. Read it before writing your
first spec, and match a node's `kind` to what the step actually is, since the
kind drives the colour, the icon and the encyclopedia entry the reader sees.

The page can lay the diagram out top-to-bottom or left-to-right and the reader
flips between them with a button, so this is not a decision you have to get
right — but you can set the starting view with `"direction": "LR"` when the
query is short and wide (a few steps, several parallel branches) rather than a
long pipeline.

### Deliver it

Where the page ends up depends on the session you are running in, not on the
skill — so look at what this session actually has rather than assuming:

- **A tool that publishes artifacts** (Cowork, claude.ai): publish the rendered
  file as-is. The renderer emits exactly the document fragment the artifact
  shell expects, so no flag is needed. The person gets a link they can open on
  any device and share.
- **No artifact tool** (Claude Code, a CI job, any other harness): render with
  `--standalone`, which wraps the same page in a complete HTML document, write
  it somewhere sensible — next to the query file, or the working directory —
  and tell them the path. It is one self-contained file: no server, no build
  step, opens by double-clicking. This is the normal outcome outside Cowork and
  is not a downgrade; the page behaves identically.

Never leave the map only in the transcript. A wall of HTML pasted into chat is
useless to them, and so is a file they were not told the path to.

### PDF

Some of what these maps get used for — attaching to a ticket, sending to a
steering committee, printing for a review — wants a PDF rather than a page:

```bash
python3 scripts/export_pdf.py spec.json -o query_map.pdf     # or an already rendered .html
```

The page carries its own print stylesheet, so the PDF is a proper document
rather than a screenshot: the diagram first, laid out across pages in the light
half of the same palette, then the summary, the row funnel as a table, every
step written out in full, the findings, and the SQL. Produce one when they ask
for a PDF, or when they say the explanation is going somewhere a link cannot
follow. The page also has a print button for whoever opens the HTML themselves;
inside an artifact frame the browser may block it, which is the other reason to
run the script and hand over the file.

If no browser engine is installed, the script says so and stops rather than
producing a broken file — pass that on, and point out that opening the HTML and
printing it to PDF gives exactly the same document.

Check your own work before you hand it over: run the script, confirm it reports
the node and funnel counts you expected, and re-read the `plain` sentences as
if you were the person who asked. If any of them could be swapped for the
keyword itself without losing information, rewrite it.

Your message alongside the artifact is short: what the query does in one or two
sentences, and the one or two findings that would change what they do next —
the step that destroys the most rows, the join that can silently fan out, the
filter that will match nothing. Everything else lives in the page.

## What makes one of these good

- **The funnel explains, not just reports.** Every number change names its
  cause — and the funnel is absent rather than invented when nothing was
  measurable.
- **Every join has a fan-out verdict** — measured, reasoned, or explicitly
  unverified with the check named. A join node that says only what it attaches
  has skipped the question the reader most needs answered.
- **Findings surface.** Orphan keys, NULL traps, missing tie-breakers on
  `LIMIT`, accidental cross joins, `UNION ALL` duplicates, a `WHERE` on a
  LEFT-joined table that quietly turns it into an inner join — put these in
  `notes` and mention the important one in your reply. Reviewing the query is
  part of explaining it.
- **It reads in the user's language,** end to end — cards, panel, funnel and
  notes, with `lang` set to match.
- **Honest grounding.** Every number traces back to a measurement, a catalog
  statistic, or something the person told you. When none of those exist, the
  page carries no numbers at all and says so — and the reader can trust the
  numbers that *are* there precisely because of that.
- **No wasted words on the card.** The card is a glance; the panel is the depth.

## Files

- `references/spec-schema.md` — the spec contract, node kinds, worked example. Read before writing a spec.
- `references/decomposition.md` — how to map CTEs, subqueries, windows, set ops, recursion, cross-catalog reads and DML; dialect differences.
- `references/funnel.md` — row-count arithmetic, probe SQL per dialect, estimating without a database.
- `references/introspection.md` — MCP call sequences for Trino, Postgres and MySQL; what to ask and what it costs.
- `scripts/render_query_map.py` — spec JSON → self-contained HTML page.
- `scripts/export_pdf.py` — spec or page → PDF, via any Chrome/Chromium present.
- `examples/` — two complete specs (a federated Trino pipeline, a recursive Postgres CTE feeding an INSERT) to copy the shape from.
