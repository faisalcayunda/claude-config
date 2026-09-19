# Deriving rules (confirmed-only) and mapping them

## Step 1 — gather evidence
Two sources, used together:
- **Data dictionary docs** if they exist (e.g. `data_dictionary_<table>.md` /
  `data_vocabulary_<table>.md`): these list business rules, often tagged `BVR-xxx`.
- **Live profiling via dbhub** (see `verify-mcp.md` for exact queries): null counts,
  distinct counts, min/max, sample values, FK match rates.

## Step 2 — keep only CONFIRMED, unambiguous rules
Include a rule only if it's clearly asserted and the data supports it. **Exclude** anything
the docs flag as `[TBC]`, "belum terkonfirmasi", "perlu konfirmasi tim product", a
"hipotesis", or conditional/fuzzy wording ("if filled"). Why: a check that fails on
legitimate data trains people to distrust the whole dashboard — a missing check is safer
than a wrong one. When unsure, leave it out and tell the user what you skipped and why.

Worked examples of the discipline:
- A status column's *valid code set* is confirmed by a lookup table → include an in-set check.
- The *meaning/labels* of those codes are an unconfirmed hypothesis → do NOT assert them.
- A nullable FK that's "referential only if filled" with many blanks → skip unless the
  blank handling is unambiguous.
- A "quantity ≥ 1" rule where profiling shows a 0 → that's either a real finding to raise
  with the user, or the rule isn't actually confirmed. Don't ship a check that always fails.

## Step 3 — map each rule to a GX expectation → OM built-in
| Rule intent | GX expectation | OM built-in (level) |
|---|---|---|
| not null | ExpectColumnValuesToNotBeNull | columnValuesToBeNotNull (COLUMN) |
| unique | ExpectColumnValuesToBeUnique | columnValuesToBeUnique (COLUMN) |
| matches pattern | ExpectColumnValuesToMatchRegex | columnValuesToMatchRegex (COLUMN) |
| in a set / FK | ExpectColumnValuesToBeInSet (+ value_set_from) | columnValuesToBeInSet (COLUMN) |
| numeric range / ≥ 0 | ExpectColumnValuesToBeBetween | columnValuesToBeBetween (COLUMN) |
| not in the future | not_in_future (recipe) | columnValuesToBeBetween (COLUMN) |
| compound unique | ExpectCompoundColumnsToBeUnique | tableCustomSQLQuery (TABLE) |
| same-row inequality | ExpectSelectColumnValuesToBeUniqueWithinRecord | tableCustomSQLQuery (TABLE) |
| column A ≥ column B | ExpectColumnPairValuesAToBeGreaterThanB | tableCustomSQLQuery (TABLE) |

Everything in this table is already mapped in `src/om.py` `BUILTIN_DEFINITIONS` — reuse it,
don't reinvent it.

## Step 4 — only if a rule needs a NEW check type: add one mapping
If a rule genuinely needs a GX expectation not in the table above, add one entry to
`BUILTIN_DEFINITIONS` in `src/om.py`. Find the closest OM built-in with the OpenMetadata MCP
`get_test_definitions`. Shape:
```python
"ExpectColumnValueLengthsToBeBetween": {
    "level": "COLUMN",                             # COLUMN attaches to a column; TABLE to the table
    "definition": "columnValueLengthsToBeBetween", # a real OM built-in name from get_test_definitions
    "params": _between_params,                     # returns [{"name","value"}]; reuse one or add a small helper
},
```
If no OM built-in fits, map to `tableCustomSQLQuery` with a helper that returns a readable
SQL string describing the *violating* rows (as the three multi-column checks do). GX stays
the source of truth; OM just gets something meaningful to display. This is the only kind of
change `om.py` ever needs, and it's purely additive — `ensure_test_case` even raises a clear
"add a mapping" error if it meets an unmapped expectation, so nothing fails silently.
