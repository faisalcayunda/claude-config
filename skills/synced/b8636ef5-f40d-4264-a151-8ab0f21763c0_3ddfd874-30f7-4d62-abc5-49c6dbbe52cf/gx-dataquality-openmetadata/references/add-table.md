# Adding or editing a table's checks

A table's checks live in one file: `config/tables/<source>.<schema>.<table>.yaml`.
Copy a shape from `assets/examples/` and adjust. Validate with
`python scripts/validate_config.py <repo-root> <config.yaml>` before running.

## File schema
```yaml
table:
  source: scm                    # must match a key in config/connections.yaml -> sources
  schema: sipscmdb_prod
  name: order_product
  fqn: "<EXACT fully-qualified name copied from OpenMetadata>"   # never guess this

columns_needed: [id, order_id, price, quantity, created_at, updated_at]  # only what checks use

checks:
  - name: <unique_snake_case_name>   # becomes the test case name in OpenMetadata
    expectation: <GX expectation class or a recipe>
    kwargs: { ... }                  # plain values only (columns, numbers, lists, booleans)
```

`name` must be unique within the table and is what shows in OM (e.g. `id_not_null`,
`price_non_negative`, `updated_at_after_created_at`). `fqn` must be copied verbatim from
OpenMetadata (see `verify-mcp.md`) — a guessed FQN silently mis-targets or 404s.

## Single-column checks (most common)
```yaml
- name: id_not_null
  expectation: ExpectColumnValuesToNotBeNull
  kwargs: {column: id}

- name: id_unique
  expectation: ExpectColumnValuesToBeUnique
  kwargs: {column: id}

- name: id_matches_uuid_format
  expectation: ExpectColumnValuesToMatchRegex
  kwargs: {column: id, regex: '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'}

- name: price_non_negative
  expectation: ExpectColumnValuesToBeBetween
  kwargs: {column: price, min_value: 0}

- name: status_known_values
  expectation: ExpectColumnValuesToBeInSet
  kwargs: {column: status, value_set: [1, 2, 3, 4]}
```

## Recipe: referential integrity (FK) — value_set_from
When a column must reference values that exist in another table, don't hardcode the set —
resolve it at run time:
```yaml
- name: order_id_references_order_transaction
  expectation: ExpectColumnValuesToBeInSet
  kwargs: {column: order_id}
  value_set_from:
    source: scm
    query: "SELECT id FROM sipscmdb_prod.order_transaction"
```
The runner runs that query first and injects the result as `value_set`. GX ignores nulls in
map checks, so a nullable FK column is fine.

## Recipe: not in the future — not_in_future
`not_in_future` is a recipe, not a GX class. The runner turns it into
`ExpectColumnValuesToBeBetween` with `max_value = now()` computed fresh at run time:
```yaml
- name: created_at_not_in_future
  expectation: not_in_future
  kwargs: {column: created_at}
```

## Recipe: multi-column / cross-row checks
These have no direct OM built-in, so om.py maps them to `tableCustomSQLQuery` (a readable
SQL description; GX still computes the real result):
```yaml
- name: seller_buyer_pair_unique          # compound uniqueness
  expectation: ExpectCompoundColumnsToBeUnique
  kwargs: {column_list: [seller_id, buyer_id]}

- name: seller_not_equal_buyer            # same-row inequality
  expectation: ExpectSelectColumnValuesToBeUniqueWithinRecord
  kwargs: {column_list: [seller_id, buyer_id]}

- name: updated_at_after_created_at       # column A >= column B
  expectation: ExpectColumnPairValuesAToBeGreaterThanB
  kwargs: {column_A: updated_at, column_B: created_at, or_equal: true}
```

## Editing an existing config
- **Change a query / value_set**: edit that check's `value_set_from.query` (or `value_set`).
- **Change a connection**: set `table.source` to another source defined in connections.yaml.
- **Add / remove a check**: add or remove a list item; keep `columns_needed` in sync (only
  the columns your checks reference). Re-validate.
- An expectation not yet in `BUILTIN_DEFINITIONS` fails validation with a clear message —
  see `derive-rules.md` to add the one-line mapping.
