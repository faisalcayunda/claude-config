# Atlas HCL Patterns & Environment Variable Handling

## Table of Contents
1. [Environment Variable Patterns](#1-environment-variable-patterns)
2. [atlas.hcl Structure](#2-atlashcl-structure)
3. [Schema HCL Patterns](#3-schema-hcl-patterns)
4. [Versioned vs Declarative Migrations](#4-versioned-vs-declarative-migrations)
5. [Dev Database Patterns](#5-dev-database-patterns)
6. [Lint Configuration](#6-lint-configuration)
7. [Common Commands Reference](#7-common-commands-reference)

---

## 1. Environment Variable Patterns

### Recommended: `getenv()` built-in function
Atlas has a native `getenv()` function — the cleanest approach, works perfectly with direnv.

```hcl
env "local" {
  url = getenv("DATABASE_URL")
  dev = getenv("DEV_DATABASE_URL")
}
```

When `DATABASE_URL` is not set, Atlas returns a helpful error:
```
Error: missing environment variable "DATABASE_URL"
```

### HCL Variables with ATLAS_VAR_ prefix
For parameterized configs, Atlas reads `ATLAS_VAR_*` environment variables:

```hcl
variable "db_password" {
  type = string
}

env "local" {
  url = "postgres://postgres:${var.db_password}@localhost:5432/mydb?sslmode=disable"
}
```

Run with: `ATLAS_VAR_db_password=secret atlas migrate diff --env local`

### Composite URL construction
Build URL from components using string interpolation:

```hcl
locals {
  pg_host = getenv("PG_HOST")
  pg_port = getenv("PG_PORT")
  pg_user = getenv("PG_USER")
  pg_pass = getenv("PG_PASSWORD")
  db_name = getenv("DB_NAME")
}

env "local" {
  url = "postgres://${local.pg_user}:${local.pg_pass}@${local.pg_host}:${local.pg_port}/${local.db_name}?sslmode=disable"
  dev = "docker://postgres/16/dev?search_path=public"
}
```

**Best practice:** Pre-compose `DATABASE_URL` in `.envrc` / `.env` from parts, then use
`getenv("DATABASE_URL")` in atlas.hcl. Keeps atlas.hcl clean.

---

## 2. atlas.hcl Structure

### Full structure with all features

```hcl
# Locals for shared values
locals {
  db_name = getenv("DB_NAME")
}

# ── Local Development ───────────────────────────────────────────────
env "local" {
  # Target database URL
  url = getenv("DATABASE_URL")

  # Dev database — Atlas uses this to plan migrations
  # Docker driver spins up a temporary container automatically
  dev = "docker://postgres/16/dev?search_path=public"

  # Schema desired state
  src = "file://schema"

  # Versioned migrations
  migration {
    dir    = "file://migrations"
    format = atlas  # atlas (default) or golang-migrate
  }

  # Lint rules
  lint {
    destructive {
      error = false  # Warn only in local
    }
  }
}

# ── Staging ─────────────────────────────────────────────────────────
env "staging" {
  url = getenv("STAGING_DATABASE_URL")
  dev = "docker://postgres/16/dev?search_path=public"
  src = "file://schema"
  migration {
    dir = "file://migrations"
  }
  lint {
    destructive {
      error = true  # Fail on destructive changes in staging
    }
  }
}

# ── Production ──────────────────────────────────────────────────────
env "prod" {
  url = getenv("PROD_DATABASE_URL")
  dev = "docker://postgres/16/dev?search_path=public"
  migration {
    dir = "file://migrations"
  }
  lint {
    destructive {
      error = true
    }
    concurrent_index {
      error = true  # Enforce CONCURRENTLY for production indexes
    }
  }
}
```

### Multiple schema files (split by object type)

```hcl
data "hcl_schema" "app" {
  paths = fileset("schema/**/*.pg.hcl")
}

env "local" {
  src = data.hcl_schema.app.url
  dev = "docker://postgres/16/dev?search_path=public"
  migration {
    dir = "file://migrations"
  }
}
```

---

## 3. Schema HCL Patterns

### Basic table with audit columns (Data Mesh standard)

```hcl
table "customers" {
  schema = schema.public

  column "id" {
    type    = uuid
    null    = false
    default = sql("gen_random_uuid()")
  }
  column "external_id" {
    type = character_varying(255)
    null = true
    comment = "Source system identifier"
  }
  column "name" {
    type = character_varying(500)
    null = false
  }
  column "created_at" {
    type    = timestamptz
    null    = false
    default = sql("now()")
  }
  column "updated_at" {
    type    = timestamptz
    null    = false
    default = sql("now()")
  }
  column "created_by" {
    type    = character_varying(255)
    null    = false
    default = "system"
    comment = "Service or user that created this record"
  }
  column "is_deleted" {
    type    = boolean
    null    = false
    default = false
    comment = "Soft delete flag"
  }

  primary_key {
    columns = [column.id]
  }

  index "idx_customers_external_id" {
    columns = [column.external_id]
    unique  = true
    where   = "external_id IS NOT NULL"
  }

  index "idx_customers_created_at" {
    columns = [column.created_at]
  }
}

schema "public" {
  comment = "Main application schema"
}
```

### Foreign key pattern

```hcl
foreign_key "fk_orders_customer" {
  columns     = [column.customer_id]
  ref_columns = [table.customers.column.id]
  on_update   = NO_ACTION
  on_delete   = RESTRICT
}
```

### Enum type (PostgreSQL)

```hcl
enum "order_status" {
  schema = schema.public
  values = ["draft", "confirmed", "processing", "shipped", "delivered", "cancelled"]
}

table "orders" {
  schema = schema.public
  column "status" {
    type = enum.order_status
    null = false
    default = "draft"
  }
}
```

### Trigger for updated_at auto-update

```hcl
function "set_updated_at" {
  schema = schema.public
  lang   = PLpgSQL
  return = trigger
  as     = <<-SQL
    BEGIN
      NEW.updated_at = now();
      RETURN NEW;
    END;
  SQL
}

trigger "trg_customers_updated_at" {
  on     = table.customers
  before = [UPDATE]
  per    = ROW
  execute = function.set_updated_at
}
```

---

## 4. Versioned vs Declarative Migrations

### Versioned (Recommended for Data Mesh)

**Pros:** Each migration is a committed artifact, auditable, reviewable in PR, traceable.
**Flow:** Edit `schema/*.pg.hcl` → run `atlas migrate diff` → commit migration file → apply.

```bash
# 1. Edit schema/*.pg.hcl (desired state)
# 2. Generate migration
atlas migrate diff add_orders_table --env local

# 3. Inspect generated migration
cat migrations/YYYYMMDDHHMMSS_add_orders_table.sql

# 4. Lint before applying
atlas migrate lint --env local --latest 1

# 5. Apply
atlas migrate apply --env local
```

### Declarative (for prototyping / dev only)

```bash
# Apply schema directly without versioned files
atlas schema apply --env local
```

**Do NOT use declarative in staging/prod.** Always use versioned migrations in CI/CD.

---

## 5. Dev Database Patterns

The dev database is a **temporary database** Atlas uses internally to:
- Normalize the desired schema
- Compute diffs between desired vs current
- Validate SQL before writing migration files

### Docker (recommended — zero config)

```hcl
dev = "docker://postgres/16/dev?search_path=public"
```

Requires Docker running. Atlas pulls the image on first use.

### Existing local database

```hcl
dev = "postgres://postgres:pass@localhost:5432/atlas_dev?sslmode=disable"
```

Create it manually: `createdb atlas_dev`

### Using same DB with different schema

```hcl
dev = "postgres://postgres:pass@localhost:5432/mydb_dev?search_path=public&sslmode=disable"
```

---

## 6. Lint Configuration

```hcl
lint {
  # Fail on destructive changes (DROP TABLE, DROP COLUMN, etc.)
  destructive {
    error = true
  }

  # Enforce CREATE INDEX CONCURRENTLY in production
  concurrent_index {
    error = true
  }

  # Naming conventions
  naming {
    force   = true
    table   {
      match   = "^[a-z][a-z0-9_]*$"
      message = "Table names must be lowercase snake_case"
    }
    column {
      match   = "^[a-z][a-z0-9_]*$"
      message = "Column names must be lowercase snake_case"
    }
  }
}
```

---

## 7. Common Commands Reference

```bash
# Generate migration (versioned)
atlas migrate diff <name> --env local

# Apply pending migrations
atlas migrate apply --env local

# Show pending migrations
atlas migrate status --env local

# Lint latest migration
atlas migrate lint --env local --latest 1

# Inspect current DB schema
atlas schema inspect --env local

# Validate schema files
atlas schema validate --env local

# Rehash after manual migration edits
atlas migrate hash --env local

# Push to Atlas Cloud
atlas migrate push <project-name> --env local

# View ERD in browser (requires atlas login)
atlas schema inspect --env local -w
```
