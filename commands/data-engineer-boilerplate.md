---
name: data-engineer-boilerplate
description: GENERATOR — scaffolds mature folder/boilerplate structure for Airflow 3.1.7 + dbt + PySpark data projects. Outputs ASCII tree + key file stubs. Never executes commands. Group A: triggered when user asks to bootstrap a new data project, scaffold a data pipeline project, or generate project structure.
argument-hint: "[--stack airflow|dbt|pyspark|monorepo|lakehouse|streaming] [--project <name>] [--depth minimal|standard|full]"
---

EXECUTE IMMEDIATELY — do not deliberate.

## GENERATOR ONLY — this skill writes text. It never runs airflow, dbt, docker, pip, uv, python, make, or terraform.

---

## Argument Parsing

Extract from $ARGUMENTS:

| Argument | Values | Default | Notes |
|---|---|---|---|
| `--stack` | `airflow`, `dbt`, `pyspark`, `monorepo`, `lakehouse`, `streaming` | `monorepo` | determines folder tree |
| `--project` | string | `my_data_project` | replaces `{project_name}` in all output |
| `--depth` | `minimal`, `standard`, `full` | `standard` | controls how many stubs are generated |

If `--stack` is omitted: ask exactly once:

> "Which stack? (airflow / dbt / pyspark / monorepo / lakehouse / streaming)"

Do NOT proceed until stack is specified. All other arguments have safe defaults.

---

## Step 1 — Read business context

Read the Stack line in `/Users/isal/.claude/CLAUDE.md` to confirm the active stack. Take domain names from the relevant wiki page (for example `wiki/entities/MPM sync pipelines.md`) as substitutes for `{domain}` and `{source}` below. If none applies, use `example`.

---

## Step 2 — Determine Stack & Depth

Set `PROJECT = --project value (or "my_data_project")`.

Substitute `{project_name}` → `PROJECT` in all folder trees and stubs below.
Substitute `{domain}` → first domain from that wiki page (or `example`).
Substitute `{source}` → first source system from that wiki page (or `raw`).

| Depth | Folder tree | File stubs |
|---|---|---|
| `minimal` | Full tree for the selected stack | None |
| `standard` | Full tree | pyproject.toml + dbt_project.yml (if dbt in stack) + example DAG header (if airflow in stack) |
| `full` | Full tree | standard stubs + docker-compose.yaml + .github/workflows/ CI yamls + .pre-commit-config.yaml + generate_schema_name.sql (if dbt in stack) + packages/common/config.py (if monorepo) |

---

## Step 3 — Generate Folder Tree (ASCII)

Output exactly ONE tree matching `--stack`. Monorepo is the default.

### --stack airflow

```
{project_name}/
├── dags/
│   ├── __init__.py
│   ├── .airflowignore
│   ├── {domain}/
│   │   ├── __init__.py
│   │   └── {domain}__example_daily.py
│   └── shared/
│       ├── __init__.py
│       ├── task_groups.py
│       └── callbacks.py
├── plugins/
│   ├── operators/
│   ├── hooks/
│   └── sensors/
├── include/
│   └── sql/
├── transforms/
│   ├── __init__.py
│   └── {domain}/
│       └── __init__.py
├── config/
│   ├── base.yaml
│   ├── dev.yaml
│   └── prod.yaml
├── tests/
│   ├── conftest.py
│   ├── dags/
│   │   └── test_dag_integrity.py
│   └── transforms/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yaml
├── .airflowignore
├── .env.example
├── pyproject.toml
└── README.md
```

### --stack dbt

```
{project_name}/
├── dbt_project.yml
├── packages.yml
├── models/
│   ├── staging/
│   │   └── {source}/
│   │       ├── _{source}__sources.yml
│   │       ├── _{source}__models.yml
│   │       └── stg_{source}__example.sql
│   ├── intermediate/
│   │   └── {domain}/
│   │       ├── _int_{domain}__models.yml
│   │       └── int_{domain}_example_joined.sql
│   └── marts/
│       └── {domain}/
│           ├── _{domain}__models.yml
│           ├── fct_example.sql
│           └── dim_example.sql
├── macros/
│   ├── generate_schema_name.sql
│   └── utils/
├── tests/
├── seeds/
├── snapshots/
├── .sqlfluff
└── README.md
```

### --stack pyspark

```
{project_name}/
├── src/
│   └── {project_name}/
│       ├── __init__.py
│       ├── jobs/
│       │   ├── __init__.py
│       │   └── {domain}_job.py
│       ├── transforms/
│       │   ├── __init__.py
│       │   └── {domain}_transforms.py
│       ├── io/
│       │   ├── __init__.py
│       │   ├── readers.py
│       │   └── writers.py
│       └── config.py
├── tests/
│   ├── conftest.py
│   └── jobs/
│       └── test_{domain}_job.py
├── notebooks/
│   └── explore_{domain}.ipynb
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yaml
├── pyproject.toml
├── .env.example
└── README.md
```

### --stack lakehouse — Medallion Architecture + Iceberg/Delta

```
{project_name}/
├── airflow/
│   ├── dags/
│   │   ├── ingestion/
│   │   │   ├── __init__.py
│   │   │   └── {domain}__ingest_cdc_hourly.py
│   │   └── transformation/
│   │       ├── __init__.py
│   │       └── {domain}__transform_daily.py
│   ├── plugins/
│   └── pyproject.toml
├── spark/
│   └── src/
│       └── {project_name}/
│           ├── __init__.py
│           ├── jobs/
│           │   ├── __init__.py
│           │   ├── bronze_ingest.py
│           │   ├── silver_cleanse.py
│           │   └── gold_aggregate.py
│           ├── io/
│           │   ├── __init__.py
│           │   ├── iceberg_reader.py
│           │   └── iceberg_writer.py
│           └── config.py
├── dbt/
│   ├── dbt_project.yml
│   ├── packages.yml
│   └── models/
│       ├── staging/
│       ├── intermediate/
│       └── marts/
├── contracts/
│   └── {domain}/
│       └── {domain}__{source}_v1.yaml
├── catalog/
│   └── iceberg/
│       └── {domain}__{source}.json
├── infra/
│   └── terraform/
├── .github/
│   └── workflows/
│       └── ci-spark.yaml
├── pyproject.toml
├── .pre-commit-config.yaml
└── README.md
```

> **Iceberg vs Delta Lake vs Hudi decision:**
> - Databricks + heavy Spark → Delta Lake
> - Multi-engine (Trino + Spark + Flink on same tables) → Iceberg (default for this stack)
> - High-frequency CDC upserts → Hudi

---

### --stack streaming — Kafka + Spark Structured Streaming

```
{project_name}/
├── src/
│   └── {project_name}/
│       ├── __init__.py
│       ├── consumers/
│       │   ├── __init__.py
│       │   └── {domain}_consumer.py
│       ├── producers/
│       │   ├── __init__.py
│       │   └── {domain}_producer.py
│       ├── transforms/
│       │   ├── __init__.py
│       │   └── {domain}_stream_transforms.py
│       ├── sinks/
│       │   ├── __init__.py
│       │   └── {domain}_sink.py
│       └── config.py
├── schemas/
│   └── {domain}/
│       └── {domain}_event_v1.json
├── contracts/
│   └── {domain}/
│       └── {domain}__stream_v1.yaml
├── tests/
│   ├── conftest.py
│   └── consumers/
│       └── test_{domain}_consumer.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yaml
├── pyproject.toml
├── .env.example
└── README.md
```

---

### --stack monorepo (Airflow + dbt + Python)

```
{project_name}/
├── airflow/
│   ├── dags/
│   │   ├── ingestion/
│   │   │   ├── __init__.py
│   │   │   └── {domain}__ingest_daily.py
│   │   ├── transformation/
│   │   │   ├── __init__.py
│   │   │   └── {domain}__transform_daily.py
│   │   └── shared/
│   │       ├── __init__.py
│   │       ├── task_groups.py
│   │       └── callbacks.py
│   ├── plugins/
│   │   ├── operators/
│   │   ├── hooks/
│   │   └── sensors/
│   ├── include/
│   │   └── sql/
│   ├── tests/
│   │   ├── conftest.py
│   │   └── dags/
│   │       └── test_dag_integrity.py
│   ├── Dockerfile
│   ├── docker-compose.yaml
│   └── pyproject.toml
├── dbt/
│   ├── dbt_project.yml
│   ├── packages.yml
│   ├── models/
│   │   ├── staging/
│   │   │   └── {source}/
│   │   │       ├── _{source}__sources.yml
│   │   │       └── stg_{source}__example.sql
│   │   ├── intermediate/
│   │   │   └── {domain}/
│   │   │       └── int_{domain}_example_joined.sql
│   │   └── marts/
│   │       └── {domain}/
│   │           ├── fct_example.sql
│   │           └── dim_example.sql
│   └── macros/
│       └── generate_schema_name.sql
├── contracts/
│   └── {domain}/
│       └── {domain}__{source}_v1.yaml
├── ingestion/
│   └── src/
│       └── ingestion/
│           ├── connectors/
│           ├── loaders/
│           └── models/
├── packages/
│   └── common/
│       └── src/
│           └── common/
│               ├── config.py
│               ├── logging.py
│               └── secrets.py
├── infra/
│   └── terraform/
├── docs/
│   └── adr/
├── .github/
│   └── workflows/
│       ├── ci-airflow.yaml
│       ├── ci-dbt.yaml
│       └── cd-deploy.yaml
├── pyproject.toml
├── .pre-commit-config.yaml
├── Makefile
└── README.md
```

> **Data mesh domain-ownership alternative:**
> Replace phase-based layout (`ingestion/`, `transformation/`) with domain-first:
> ```
> airflow/dags/
> ├── {domain_a}/
> │   ├── {domain_a}__ingest_daily.py
> │   └── {domain_a}__transform_daily.py
> ├── {domain_b}/
> │   └── {domain_b}__ingest_hourly.py
> └── shared/
>     ├── task_groups.py
>     └── callbacks.py
> ```
> Use domain-first when each domain has a dedicated team owning pipelines end-to-end.
> Use phase-first when a single central data team owns all pipelines.

---

## Step 4 — Generate File Stubs

For `--depth minimal`: skip this step entirely.

For `--depth standard` and `--depth full`: generate the stubs below that apply to the selected stack.

---

### Stub 1 — pyproject.toml (all stacks)

```toml
# [data-engineer-boilerplate generated: YYYY-MM-DD]
[project]
name = "{project_name}"
version = "0.1.0"
requires-python = ">=3.9"

dependencies = [
    # Airflow — pin to exact minor; constraint file manages transitive deps
    # "apache-airflow==3.1.7",
    # dbt
    # "dbt-core==1.11.10",
    # "dbt-bigquery==1.11.10",   # or dbt-snowflake / dbt-postgres
    # PySpark
    # "pyspark==3.5.7",
    # Shared
    "pydantic-settings>=2.0",
    "polars>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov",
    "mypy",
    "ruff",
]

[tool.ruff]
line-length = 100
select = ["E", "F", "I", "UP", "B", "SIM"]

[tool.mypy]
python_version = "3.9"
strict = true
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--cov=src --cov-report=term-missing"
```

---

### Stub 2 — dbt_project.yml (stacks: dbt, monorepo)

```yaml
# [data-engineer-boilerplate generated: YYYY-MM-DD]
name: '{project_name}'
version: '1.0.0'
config-version: 2

profile: '{project_name}'

model-paths: ["models"]
macro-paths: ["macros"]
seed-paths: ["seeds"]
test-paths: ["tests"]
snapshot-paths: ["snapshots"]

target-path: "target"
clean-targets: ["target", "dbt_packages"]

models:
  {project_name}:
    staging:
      +materialized: view
      +schema: staging
    intermediate:
      +materialized: ephemeral
    marts:
      +materialized: table
      +schema: marts
```

---

### Stub 3 — Example DAG file header (stacks: airflow, monorepo)

```python
# [data-engineer-boilerplate generated: YYYY-MM-DD]
"""
DAG ID:       {domain}__example_daily
Owner:        data-engineering
Schedule:     0 2 * * *   (daily at 02:00 UTC)
SLA:          04:00 UTC
Description:  <one-line purpose of this DAG>
Depends on:   <upstream DAG IDs or external sensors, or "none">
Changelog:
  YYYY-MM-DD  <author>  Initial scaffold
"""

from __future__ import annotations

from datetime import datetime, timedelta

from airflow.sdk import DAG, Asset, task

default_args = {
    "owner": "data-engineering",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": True,
    "email": ["data-engineering@{project_name}.id"],
}

with DAG(
    dag_id="{domain}__example_daily",
    start_date=datetime(2024, 1, 1),
    schedule="0 2 * * *",
    max_active_runs=1,
    catchup=False,
    default_args=default_args,
    tags=["{domain}", "daily"],
) as dag:

    @task()
    def extract() -> str:
        # Return file path or metadata dict — not raw data
        return "/tmp/placeholder.parquet"

    @task()
    def transform(source_path: str) -> str:
        return source_path

    @task()
    def load(transformed_path: str) -> None:
        pass

    load(transform(extract()))
```

---

### Stub 4 — .airflowignore (stacks: airflow, monorepo)

```
# [data-engineer-boilerplate generated: YYYY-MM-DD]
# Patterns listed here are excluded from DAG discovery
tests/
docker/
docs/
*.pyc
__pycache__/
.git/
```

---

### Stub 5 — generate_schema_name.sql (stacks: dbt, monorepo) — depth: full only

```sql
-- [data-engineer-boilerplate generated: YYYY-MM-DD]
-- Env-aware schema routing: prefixes dev/staging schemas; uses raw schema in prod.
-- Reference: https://docs.getdbt.com/docs/build/custom-schemas

{% macro generate_schema_name(custom_schema_name, node) -%}

    {%- set default_schema = target.schema -%}

    {%- if target.name == 'prod' -%}

        {%- if custom_schema_name is none -%}
            {{ default_schema }}
        {%- else -%}
            {{ custom_schema_name | trim }}
        {%- endif -%}

    {%- else -%}

        {%- if custom_schema_name is none -%}
            {{ default_schema }}
        {%- else -%}
            {{ default_schema }}_{{ custom_schema_name | trim }}
        {%- endif -%}

    {%- endif -%}

{%- endmacro %}
```

---

### Stub 6 — packages/common/config.py (stack: monorepo) — depth: full only

```python
# [data-engineer-boilerplate generated: YYYY-MM-DD]
"""
Shared configuration for all monorepo packages.
Reads from environment variables; secrets from env or secrets backend.
"""
from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class CommonSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    env: str = "dev"  # dev | staging | prod
    project_name: str = "{project_name}"

    # Add service-specific fields in subclasses, not here.


class AirflowSettings(CommonSettings):
    airflow_conn_id_dwh: str = "bigquery_prod_dwh"  # TODO: override per env


class DbtSettings(CommonSettings):
    dbt_profiles_dir: str = "~/.dbt"
    dbt_target: str = "dev"  # dev | prod
```

---

### Stub 7 — docker-compose.yaml (stacks: airflow, monorepo) — depth: full only

```yaml
# [data-engineer-boilerplate generated: YYYY-MM-DD]
# Minimal local Airflow 3.1.7 compose — NOT for production use.

x-airflow-common: &airflow-common
  image: apache/airflow:3.1.7
  environment:
    AIRFLOW__CORE__EXECUTOR: LocalExecutor
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    AIRFLOW__CORE__LOAD_EXAMPLES: "false"
    AIRFLOW__CORE__FERNET_KEY: ""  # TODO: set via secrets
  volumes:
    - ./dags:/opt/airflow/dags
    - ./plugins:/opt/airflow/plugins
    - ./include:/opt/airflow/include
  depends_on:
    - postgres

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow  # TODO: replace with secrets management
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data

  airflow-webserver:
    <<: *airflow-common
    command: webserver
    ports:
      - "8080:8080"

  airflow-scheduler:
    <<: *airflow-common
    command: scheduler

  airflow-init:
    <<: *airflow-common
    command: version

volumes:
  postgres-db-volume:
```

---

### Stub 8 — .pre-commit-config.yaml (stacks: monorepo, airflow) — depth: full only

```yaml
# [data-engineer-boilerplate generated: YYYY-MM-DD]
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.4
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-merge-conflict
      - id: detect-private-key

  - repo: https://github.com/sqlfluff/sqlfluff
    rev: 3.1.0
    hooks:
      - id: sqlfluff-lint
        args: [--dialect, ansi]
```

---

### Stub 9 — .github/workflows/ci-airflow.yaml (stacks: airflow, monorepo) — depth: full only

```yaml
# [data-engineer-boilerplate generated: YYYY-MM-DD]
name: CI — Airflow

on:
  pull_request:
    paths:
      - "airflow/**"
      - "dags/**"

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -e ".[dev]"

      - name: Ruff lint
        run: ruff check .

      - name: Mypy
        run: mypy src

      - name: Pytest
        run: pytest tests/ --cov=src --cov-fail-under=80
```

---

### Stub 10 — Data Contract YAML — `contracts/{domain}/{domain}__{source}_v1.yaml` (stacks: dbt, monorepo, lakehouse) — depth: full only

```yaml
# [data-engineer-boilerplate generated: YYYY-MM-DD]
# Data Contract — versioned agreement between producer and consumers.
# Commit alongside the pipeline code. Bump major version on breaking schema changes.
# Reference: https://datacontract.com (Open Data Contract Standard)

name: "{domain}__{source}"
version: "1.0.0"
owner: "data-engineering@{project_name}.id"
description: "Raw {source} data produced by the {domain} ingestion pipeline."

schema:
  - name: id
    type: string
    nullable: false
    description: "Primary key."
  - name: created_at
    type: timestamp
    nullable: false
    description: "Row creation timestamp in source system (UTC)."
  - name: _ingested_at
    type: timestamp
    nullable: false
    description: "Pipeline ingestion timestamp (UTC). Set by loader, never by source."

quality:
  - rule: not_null
    column: id
  - rule: not_null
    column: created_at
  - rule: row_count_gte
    value: 1

sla:
  freshness_hours: 25
  uptime_percent: 99.5

consumers:
  - name: "Analytics Team"
    output_port: "warehouse.marts.{domain}"
```

---

### Stub 11 — Iceberg Writer — `spark/src/{project_name}/io/iceberg_writer.py` (stack: lakehouse) — depth: standard and full

```python
# [data-engineer-boilerplate generated: YYYY-MM-DD]
"""
Iceberg writer utilities for the lakehouse stack.
Uses PySpark 3.5.7 with the Iceberg Spark runtime.

SparkConf requirements (add to job entrypoint):
    spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
    spark.sql.catalog.{catalog_name}=org.apache.iceberg.spark.SparkCatalog
    spark.sql.catalog.{catalog_name}.type=rest
    spark.sql.catalog.{catalog_name}.uri=${ICEBERG_REST_CATALOG_URL}
"""
from __future__ import annotations

from pyspark.sql import DataFrame, SparkSession


def write_bronze(
    spark: SparkSession,
    df: DataFrame,
    catalog: str,
    database: str,
    table: str,
    partition_by: list[str] | None = None,
) -> None:
    """Write raw data to the Bronze Iceberg layer (append only)."""
    full_table = f"{catalog}.{database}.{table}"
    writer = df.writeTo(full_table).using("iceberg").option("write.format.default", "parquet")
    if partition_by:
        writer = writer.partitionedBy(*partition_by)
    writer.append()


def upsert_silver(
    spark: SparkSession,
    df: DataFrame,
    catalog: str,
    database: str,
    table: str,
    merge_keys: list[str],
) -> None:
    """Merge (upsert) data into the Silver Iceberg layer."""
    full_table = f"{catalog}.{database}.{table}"
    df.createOrReplaceTempView("_source")
    merge_condition = " AND ".join(
        f"target.{k} = source.{k}" for k in merge_keys
    )
    spark.sql(f"""
        MERGE INTO {full_table} AS target
        USING _source AS source
        ON {merge_condition}
        WHEN MATCHED THEN UPDATE SET *
        WHEN NOT MATCHED THEN INSERT *
    """)
```

---

### Stub 12 — Kafka Consumer — `src/{project_name}/consumers/{domain}_consumer.py` (stack: streaming) — depth: standard and full

```python
# [data-engineer-boilerplate generated: YYYY-MM-DD]
"""
Spark Structured Streaming consumer for {domain} events.
Reads from Kafka topic, applies transforms, writes to Iceberg sink.

Delivery guarantee: at-least-once (idempotent sink required — use upsert_silver).
"""
from __future__ import annotations

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType, StructField, StructType, TimestampType

EVENT_SCHEMA = StructType([
    StructField("id", StringType(), nullable=False),
    StructField("event_type", StringType(), nullable=False),
    StructField("occurred_at", TimestampType(), nullable=False),
    StructField("payload", StringType(), nullable=True),
])


def build_stream(spark: SparkSession, kafka_bootstrap: str, topic: str) -> None:
    """Read from Kafka, parse, transform, write to sink.

    Checkpoint directory must be on durable storage (S3/GCS/HDFS).
    Watermark: 10 minutes — adjust based on source event latency.
    """
    raw = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", kafka_bootstrap)
        .option("subscribe", topic)
        .option("startingOffsets", "latest")
        .option("failOnDataLoss", "false")
        .load()
    )

    parsed = (
        raw
        .select(F.from_json(F.col("value").cast("string"), EVENT_SCHEMA).alias("data"))
        .select("data.*")
        .withWatermark("occurred_at", "10 minutes")
    )

    (
        parsed.writeStream
        .format("iceberg")
        .outputMode("append")
        .option("checkpointLocation", "s3a://{project_name}-checkpoints/{domain}/")
        .option("path", "catalog.silver.{domain}_events")
        .trigger(processingTime="1 minute")
        .start()
        .awaitTermination()
    )
```

---

### Stub 13 — OpenLineage config — `config/openlineage.yml` (stacks: airflow, monorepo, lakehouse) — depth: full only

```yaml
# [data-engineer-boilerplate generated: YYYY-MM-DD]
# OpenLineage client configuration for non-Airflow jobs (PySpark, dlt, custom scripts).
transport:
  type: http
  url: "${OPENLINEAGE_URL}"
  endpoint: "api/v1/lineage"
  auth:
    type: api_key
    api_key: "${OPENLINEAGE_API_KEY}"

namespace: "{project_name}.${ENVIRONMENT}"

# For PySpark jobs, add to SparkConf:
# spark.extraListeners=io.openlineage.spark.agent.OpenLineageSparkListener
# spark.openlineage.transport.type=http
# spark.openlineage.transport.url=<url>
# spark.openlineage.namespace={project_name}.production
```

---

### Stub 14 — packages.yml — `dbt/packages.yml` (stacks: dbt, monorepo, lakehouse) — depth: standard and full

```yaml
# [data-engineer-boilerplate generated: YYYY-MM-DD]
packages:
  - package: dbt-labs/dbt_utils
    version: [">=1.0.0", "<2.0.0"]

  - package: elementary-data/elementary
    version: [">=0.16.0"]

  - package: calogica/dbt_date
    version: [">=0.10.0"]
```

---

### Stub 15 — CI for dbt — `.github/workflows/ci-dbt.yaml` (stacks: dbt, monorepo) — depth: full only

```yaml
# [data-engineer-boilerplate generated: YYYY-MM-DD]
name: CI — dbt

on:
  pull_request:
    paths:
      - "dbt/**"

jobs:
  dbt-lint-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dbt
        run: pip install dbt-core==1.11.10 dbt-duckdb
      - name: dbt deps
        working-directory: dbt
        run: dbt deps
      - name: dbt compile (CI target)
        working-directory: dbt
        env:
          DBT_TARGET: ci
        run: dbt compile --target ci
      - name: dbt test (DuckDB CI target)
        working-directory: dbt
        env:
          DBT_TARGET: ci
        run: dbt test --target ci --store-failures
```

---

## Step 5 — Output Next-Steps Checklist

After all generated content, always append this section (substitute stack-specific items):

```
### Next steps
- [ ] Replace all {placeholder} values with actual project/domain/source names
- [ ] Review pyproject.toml and uncomment dependencies for your stack
- [ ] Set AIRFLOW__CORE__FERNET_KEY via secrets backend (never hardcode)
- [ ] Register dbt sources in _{source}__sources.yml before running dbt
- [ ] Run `/dbt-model-gen` to scaffold individual staging/intermediate/marts models
- [ ] Run `/data-quality-check` to generate test stubs for each model
- [ ] Run `/airflow-dag-lint` on each DAG file before opening a PR
- [ ] Verify generate_schema_name.sql matches your warehouse's schema strategy
- [ ] Add actual connection IDs to config.py — replace placeholder values
- [ ] Commit .pre-commit-config.yaml and run `pre-commit install`
- [ ] Run `dbt deps` to install packages (dbt_utils, elementary, dbt_date)
- [ ] Run `dbt run --select elementary` after every `dbt run` to populate observability tables
- [ ] Register data contracts in `contracts/` alongside pipeline code — increment major version on breaking schema changes
- [ ] Configure OpenLineage transport in `config/openlineage.yml` (set `OPENLINEAGE_URL` env var)
- [ ] For streaming stack: set `KAFKA_BOOTSTRAP_SERVERS` and `ICEBERG_REST_CATALOG_URL` in `.env`
```

---

## Naming Conventions

> These patterns mirror data-engineer.md § File & Naming Rules — keep in sync when updating either file.

All generated output must follow these patterns:

| Artifact | Pattern | Example |
|---|---|---|
| DAG file | `{domain}__{description}_{cadence}.py` | `finance__revenue_daily.py` |
| DAG ID | match filename without `.py` | `finance__revenue_daily` |
| Task ID | `{verb}_{noun}` snake_case | `extract_salesforce_accounts` |
| Airflow Connection | `{tool}_{env}_{descriptor}` | `bigquery_prod_dwh` |
| dbt staging | `stg_{source}__{entity}` | `stg_salesforce__accounts` |
| dbt intermediate | `int_{entity}_{verb}` | `int_payments_pivoted` |
| dbt fact | `fct_{process}` | `fct_orders` |
| dbt dimension | `dim_{entity}` | `dim_customers` |
| dbt YAML | `_{source_or_domain}__{type}.yml` | `_salesforce__sources.yml` |
| Python test file | `test_{module}.py` | `test_salesforce.py` |

---

## Tool & Version Reference

Recommended pinned versions for generated stubs:

| Tool | Version |
|---|---|
| apache-airflow | 3.1.7 |
| dbt-core | 1.11.10 |
| pyspark | 3.5.7 |
| polars | >=1.0.0 |
| dlt | >=1.0.0 |
| duckdb | 1.4.x (LTS, local dev) |
| pydantic-settings | >=2.0 |
| ruff | latest (linting + formatting) |
| mypy | latest (strict type checking) |
| python | >=3.9 |

---

## Hard Constraints

- GENERATOR ONLY — see banner at top of this skill (never runs airflow, dbt, docker, pip, uv, python, make, or terraform).
- NEVER fabricate org-specific values, actual credentials, or real connection strings. Use named placeholders only.
- NEVER create files directly — all output is text for the user to copy.
- NEVER add dependencies to pyproject.toml stubs beyond those listed in the Tool & Version Reference above.
- NEVER modify existing files in the user's project — output is always a new text block.
- Depth `minimal` produces folder tree only. No stubs. No exceptions.
- If `--stack pyspark` is selected: skip dbt stubs (dbt_project.yml, generate_schema_name.sql) and Airflow stubs (DAG header, .airflowignore, docker-compose).

---

Stream all output live — never run in background.
