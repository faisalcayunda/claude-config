"""
runner.py -- the ONE generic engine. Reads a table's YAML config, pulls just
the columns it needs straight from Postgres, runs every declared check
through Great Expectations, and pushes each result to OpenMetadata.

Every check is generically dispatched as
    getattr(gx.expectations, check["expectation"])(**kwargs)
so any of GX's ~50 built-in expectation classes works from YAML with zero
new code here, as long as its kwargs are plain values (column names,
numbers, lists, booleans) -- this covers single-column, pair, and
multi-column/compound expectations alike.

Two things get special handling before that generic dispatch:
  - expectation: "not_in_future"   is not a real GX class name -- it's a
    small recipe meaning "ExpectColumnValuesToBeBetween with max_value set
    to right now", because "now" has to be computed at run time, not baked
    into a YAML file.
  - a check with a "value_set_from" block runs that query first (e.g.
    "SELECT id FROM clients") and uses the result as the expectation's
    value_set -- this is how a referential-integrity check ("does this
    column only contain values that really exist in another table?") gets
    expressed without inventing a new GX expectation type.

Deliberately NOT supported: arbitrary computed columns via eval() of a
formula string from YAML. If a check ever needs real derived-column logic
beyond these two recipes, add a small named Python function instead of
teaching this file to interpret more magic YAML -- letting config files
execute arbitrary code is not a trade worth making.
"""
import glob
import os
from datetime import datetime, timezone

import yaml
import great_expectations as gx

from src import db, om

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABLES_DIR = os.path.join(REPO_ROOT, "config", "tables")


def _load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def _column_label(check):
    """Best-effort column/columns name for this check, used both in the
    OpenMetadata FQN and the entityLink -- works for single-column, pair,
    and multi-column checks alike."""
    kwargs = check.get("kwargs", {})
    if "column" in kwargs:
        return kwargs["column"]
    if "column_A" in kwargs:
        return f"{kwargs['column_A']}_{kwargs.get('column_B', '')}"
    if "column_list" in kwargs:
        return "_".join(kwargs["column_list"])
    return None


def _build_expectation(check):
    kwargs = dict(check.get("kwargs", {}))

    if check["expectation"] == "not_in_future":
        kwargs["min_value"] = None
        kwargs["max_value"] = datetime.now(timezone.utc)
        return gx.expectations.ExpectColumnValuesToBeBetween(**kwargs)

    if "value_set_from" in check:
        ref = check["value_set_from"]
        ref_df = db.query_df(ref["source"], ref["query"])
        kwargs["value_set"] = ref_df.iloc[:, 0].tolist()

    expectation_cls = getattr(gx.expectations, check["expectation"])
    return expectation_cls(**kwargs)


def run_table(config_path):
    cfg = _load_yaml(config_path)
    table_cfg = cfg["table"]
    print(f"=== {table_cfg['schema']}.{table_cfg['name']} ===")

    columns = ", ".join(cfg["columns_needed"])
    query = f"SELECT {columns} FROM {table_cfg['schema']}.{table_cfg['name']}"
    df = db.query_df(table_cfg["source"], query)
    print(f"Loaded {len(df)} rows.")

    context = gx.get_context()
    batch = (
        context.data_sources.add_pandas(f"{table_cfg['name']}_pandas")
        .add_dataframe_asset(name="data")
        .add_batch_definition_whole_dataframe("batch")
        .get_batch(batch_parameters={"dataframe": df})
    )

    for check in cfg["checks"]:
        expectation = _build_expectation(check)
        result = batch.validate(expectation)
        column = _column_label(check)
        # om.py owns the fully-qualified name now -- it's whatever OpenMetadata
        # itself assigns when the Test Case is created (read from the create
        # response, or looked up on a 409/already-exists re-run). This file no
        # longer constructs or guesses that string.
        fqn = om.ensure_test_case(check, table_cfg, column)
        om.push_result(fqn, result)
    print()


def run_all():
    paths = sorted(glob.glob(os.path.join(TABLES_DIR, "*.yaml")))
    if not paths:
        print(f"No table configs found in {TABLES_DIR}")
        return
    for path in paths:
        run_table(path)
