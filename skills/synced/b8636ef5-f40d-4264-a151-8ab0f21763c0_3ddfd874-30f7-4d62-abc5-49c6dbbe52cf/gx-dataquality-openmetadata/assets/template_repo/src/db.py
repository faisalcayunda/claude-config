"""
db.py -- resolves a table config's "source" name (e.g. "scm") into a real
connection, using config/connections.yaml (which source maps to which env
var) plus the actual secret value from the environment (.env, loaded by
run_all.py at startup).

Never hardcodes a password or DSN. If the relevant env var isn't set, this
raises a clear error instead of silently connecting with a blank value.
"""
import os

import pandas as pd
import psycopg2
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONNECTIONS_PATH = os.path.join(REPO_ROOT, "config", "connections.yaml")


def _connections():
    with open(CONNECTIONS_PATH) as f:
        return yaml.safe_load(f)


def get_dsn(source_name):
    sources = _connections()["sources"]
    if source_name not in sources:
        raise KeyError(f"Unknown source '{source_name}' -- add it to config/connections.yaml first.")
    env_var = sources[source_name]["env"]
    dsn = os.environ.get(env_var)
    if not dsn:
        raise RuntimeError(
            f"{env_var} is not set. Copy .env.example to .env and fill in a real "
            f"connection string for source '{source_name}'."
        )
    return dsn


def query_df(source_name, query):
    """Plain psycopg2 connection (not SQLAlchemy) -- see 06_gx_clients_validation.py
    for why: avoids a pandas/SQLAlchemy Engine incompatibility some environments hit."""
    conn = psycopg2.connect(get_dsn(source_name))
    try:
        return pd.read_sql(query, conn)
    finally:
        conn.close()
