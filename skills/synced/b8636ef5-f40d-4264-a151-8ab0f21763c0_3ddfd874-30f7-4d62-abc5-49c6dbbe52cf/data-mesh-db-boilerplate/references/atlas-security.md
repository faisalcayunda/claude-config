# Atlas Security: Roles, Grants & DEFAULT PRIVILEGES

## Table of Contents
1. [Role Patterns in PostgreSQL/Atlas](#1-role-patterns)
2. [Grant Patterns](#2-grant-patterns)
3. [DEFAULT PRIVILEGES — Critical for Data Mesh](#3-default-privileges)
4. [4-Role Design for Data Products](#4-4-role-design)
5. [6-Schema Grant Matrix (SQL)](#5-6-schema-grant-matrix-sql)
6. [Extensions as Code](#6-extensions-as-code)
7. [search_path Configuration](#7-search_path-configuration)
8. [Atlas mode: roles = true](#8-atlas-mode-roles)

---

## 1. Role Patterns

### PostgreSQL role types in data mesh

```sql
-- Group role (no login) — used as permission bucket
CREATE ROLE myapp NOLOGIN NOINHERIT CREATEROLE;

-- Readonly group role
CREATE ROLE myapp_readonly NOLOGIN NOINHERIT;

-- Readwrite group role  
CREATE ROLE myapp_readwrite NOLOGIN NOINHERIT;

-- Ops group role
CREATE ROLE myapp_ops NOLOGIN NOINHERIT;

-- Login user assigned to a role
CREATE ROLE analyst_jane LOGIN PASSWORD 'changeme';
GRANT myapp_readonly TO analyst_jane;
```

**Why NOLOGIN for group roles?** Group roles are permission buckets, not individual users.
Individual login users are GRANTED to group roles. This allows:
- Adding/removing users without changing any GRANTs on schemas/tables
- Auditing who has what permission by checking role membership
- Rotating credentials without touching database permissions

**Why NOINHERIT?** Forces explicit `SET ROLE` to use elevated privileges.
Use `INHERIT` if you want automatic privilege inheritance (simpler but less secure).

### Checking role membership

```sql
-- Who is member of which role?
SELECT r.rolname AS role, m.rolname AS member
FROM pg_auth_members am
JOIN pg_roles r ON r.oid = am.roleid
JOIN pg_roles m ON m.oid = am.member
ORDER BY r.rolname, m.rolname;

-- What can a role do in a schema?
SELECT grantee, privilege_type, is_grantable
FROM information_schema.role_usage_grants
WHERE object_schema = 'bronze'
ORDER BY grantee, privilege_type;

-- Table-level grants
SELECT grantee, table_schema, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE table_schema IN ('bronze', 'silver', 'gold')
ORDER BY grantee, table_schema, table_name;
```

---

## 2. Grant Patterns

### Database-level grants (CONNECT)

```sql
-- Must grant CONNECT before any schema access
GRANT CONNECT ON DATABASE mydb TO myapp_readonly;
GRANT CONNECT ON DATABASE mydb TO myapp_readwrite;
GRANT CONNECT ON DATABASE mydb TO myapp_ops;

-- Revoke default public CONNECT (security hardening)
REVOKE CONNECT ON DATABASE mydb FROM PUBLIC;
```

### Schema-level grants

```sql
-- USAGE: allows accessing objects inside the schema (required for all roles)
GRANT USAGE ON SCHEMA bronze TO myapp_readonly;

-- CREATE: allows creating new objects (tables, sequences) in schema
GRANT USAGE, CREATE ON SCHEMA bronze TO myapp_ops;

-- ALL: full schema control (owner only)
GRANT ALL PRIVILEGES ON SCHEMA bronze TO myapp;
```

### Table-level grants

```sql
-- Readonly
GRANT SELECT ON ALL TABLES IN SCHEMA bronze TO myapp_readonly;

-- Readwrite DML (no DROP/TRUNCATE — those require ownership)
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA silver TO myapp_readwrite;

-- Ops — append to audit, read gold
GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA audit TO myapp_ops;
GRANT SELECT ON ALL TABLES IN SCHEMA gold TO myapp_ops;
```

---

## 3. DEFAULT PRIVILEGES — Critical for Data Mesh

**Why this matters:** `GRANT ON ALL TABLES` only covers *existing* tables at the time of execution.
When new tables are created later (by Atlas migrations), they won't have the grants.
`ALTER DEFAULT PRIVILEGES` fixes this by automatically granting to new objects.

```sql
-- For any table created by role 'myapp' in schema 'bronze',
-- automatically grant SELECT to readonly role:
ALTER DEFAULT PRIVILEGES
  FOR ROLE myapp
  IN SCHEMA bronze
  GRANT SELECT ON TABLES TO myapp_readonly;

-- Readwrite gets DML on new tables in silver:
ALTER DEFAULT PRIVILEGES
  FOR ROLE myapp
  IN SCHEMA silver
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myapp_readwrite;

-- Ops gets INSERT on new tables in audit:
ALTER DEFAULT PRIVILEGES
  FOR ROLE myapp
  IN SCHEMA audit
  GRANT SELECT, INSERT ON TABLES TO myapp_ops;
```

### Verify default privileges

```sql
SELECT pg_catalog.pg_get_userbyid(d.defaclrole) AS role,
       n.nspname AS schema,
       CASE d.defaclobjtype
         WHEN 'r' THEN 'TABLE'
         WHEN 'S' THEN 'SEQUENCE'
         WHEN 'f' THEN 'FUNCTION'
       END AS object_type,
       d.defaclacl AS privileges
FROM pg_catalog.pg_default_acl d
LEFT JOIN pg_catalog.pg_namespace n ON n.oid = d.defaclnamespace
ORDER BY role, schema;
```

---

## 4. Four-Role Design for Data Products

Standard 4-role pattern for data mesh data products:

```
{db_name}              ← OWNER: full control, CI/CD, Atlas migrations
{db_name}_readonly     ← Analysts, BI tools, dashboards
{db_name}_readwrite    ← Developers, dbt models (with write access)
{db_name}_ops          ← Ingestion pipelines (Airbyte, Fivetran), external apps
```

### Why separate `_readwrite` from `_ops`?

| Concern | `_readwrite` | `_ops` |
|---|---|---|
| Who uses it | Human developers | Service accounts, pipelines |
| Creates tables in | `sandbox` only | `sandbox` + `bronze` |
| Access to `gold` | Full DML | SELECT only |
| Access to `audit` | SELECT only | SELECT + INSERT |
| Rotation frequency | Low (dev turnover) | High (key rotation, pipeline changes) |

Separating allows different rotation policies and audit trails.

---

## 5. Six-Schema Grant Matrix (SQL)

Complete grant statements for the 6-schema data mesh layout:

```sql
-- ============================================================
-- DB-LEVEL: CONNECT
-- ============================================================
REVOKE CONNECT ON DATABASE {DB_NAME} FROM PUBLIC;
GRANT CONNECT ON DATABASE {DB_NAME} TO {DB_NAME}_readonly;
GRANT CONNECT ON DATABASE {DB_NAME} TO {DB_NAME}_readwrite;
GRANT CONNECT ON DATABASE {DB_NAME} TO {DB_NAME}_ops;

-- ============================================================
-- SCHEMA: sandbox (exploration + dev)
-- ============================================================
GRANT USAGE ON SCHEMA sandbox TO {DB_NAME}_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA sandbox TO {DB_NAME}_readonly;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA sandbox
  GRANT SELECT ON TABLES TO {DB_NAME}_readonly;

GRANT USAGE, CREATE ON SCHEMA sandbox TO {DB_NAME}_readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA sandbox TO {DB_NAME}_readwrite;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA sandbox
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {DB_NAME}_readwrite;

GRANT USAGE, CREATE ON SCHEMA sandbox TO {DB_NAME}_ops;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA sandbox TO {DB_NAME}_ops;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA sandbox
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {DB_NAME}_ops;

-- ============================================================
-- SCHEMA: extensions (no table grants needed)
-- ============================================================
GRANT USAGE ON SCHEMA extensions TO {DB_NAME}_readonly;
GRANT USAGE ON SCHEMA extensions TO {DB_NAME}_readwrite;
GRANT USAGE ON SCHEMA extensions TO {DB_NAME}_ops;

-- ============================================================
-- SCHEMA: bronze (raw ingestion — ops can create tables)
-- ============================================================
GRANT USAGE ON SCHEMA bronze TO {DB_NAME}_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA bronze TO {DB_NAME}_readonly;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA bronze
  GRANT SELECT ON TABLES TO {DB_NAME}_readonly;

GRANT USAGE ON SCHEMA bronze TO {DB_NAME}_readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA bronze TO {DB_NAME}_readwrite;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA bronze
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {DB_NAME}_readwrite;

GRANT USAGE, CREATE ON SCHEMA bronze TO {DB_NAME}_ops;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA bronze TO {DB_NAME}_ops;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA bronze
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {DB_NAME}_ops;

-- ============================================================
-- SCHEMA: silver (cleaned — full DML for readwrite + ops)
-- ============================================================
GRANT USAGE ON SCHEMA silver TO {DB_NAME}_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA silver TO {DB_NAME}_readonly;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA silver
  GRANT SELECT ON TABLES TO {DB_NAME}_readonly;

GRANT USAGE ON SCHEMA silver TO {DB_NAME}_readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA silver TO {DB_NAME}_readwrite;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA silver
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {DB_NAME}_readwrite;

GRANT USAGE ON SCHEMA silver TO {DB_NAME}_ops;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA silver TO {DB_NAME}_ops;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA silver
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {DB_NAME}_ops;

-- ============================================================
-- SCHEMA: gold (curated serving — ops read-only)
-- ============================================================
GRANT USAGE ON SCHEMA gold TO {DB_NAME}_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA gold TO {DB_NAME}_readonly;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA gold
  GRANT SELECT ON TABLES TO {DB_NAME}_readonly;

GRANT USAGE ON SCHEMA gold TO {DB_NAME}_readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA gold TO {DB_NAME}_readwrite;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA gold
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO {DB_NAME}_readwrite;

GRANT USAGE ON SCHEMA gold TO {DB_NAME}_ops;
GRANT SELECT ON ALL TABLES IN SCHEMA gold TO {DB_NAME}_ops;  -- READ-ONLY for ops
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA gold
  GRANT SELECT ON TABLES TO {DB_NAME}_ops;

-- ============================================================
-- SCHEMA: audit (append-only — readwrite read-only, ops insert)
-- ============================================================
GRANT USAGE ON SCHEMA audit TO {DB_NAME}_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA audit TO {DB_NAME}_readonly;
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA audit
  GRANT SELECT ON TABLES TO {DB_NAME}_readonly;

GRANT USAGE ON SCHEMA audit TO {DB_NAME}_readwrite;
GRANT SELECT ON ALL TABLES IN SCHEMA audit TO {DB_NAME}_readwrite;  -- READ-ONLY
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA audit
  GRANT SELECT ON TABLES TO {DB_NAME}_readwrite;

GRANT USAGE ON SCHEMA audit TO {DB_NAME}_ops;
GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA audit TO {DB_NAME}_ops;  -- INSERT only
ALTER DEFAULT PRIVILEGES FOR ROLE {DB_NAME} IN SCHEMA audit
  GRANT SELECT, INSERT ON TABLES TO {DB_NAME}_ops;
```

---

## 6. Extensions as Code

### In migrations SQL (recommended — explicit and reviewable)

```sql
-- Must be run as superuser or with CREATEEXTENSION privilege
-- Install in extensions schema (not public)
CREATE EXTENSION IF NOT EXISTS pgcrypto       WITH SCHEMA extensions;
CREATE EXTENSION IF NOT EXISTS pg_trgm        WITH SCHEMA extensions;
CREATE EXTENSION IF NOT EXISTS dblink         WITH SCHEMA extensions;
CREATE EXTENSION IF NOT EXISTS postgres_fdw   WITH SCHEMA extensions;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"    WITH SCHEMA extensions;

-- pg_stat_statements MUST be in pg_catalog (not extensions schema)
-- Also requires: shared_preload_libraries = 'pg_stat_statements' in postgresql.conf
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

### In Atlas HCL (declarative alternative)

```hcl
extension "pgcrypto" {
  schema  = schema.extensions
  version = "1.3"
  comment = "Cryptographic functions"
}

extension "pg_trgm" {
  schema  = schema.extensions
  version = "1.6"
  comment = "Trigram similarity for fuzzy search"
}

extension "uuid-ossp" {
  schema  = schema.extensions
  version = "1.1"
  comment = "UUID generation"
}
```

**Note:** Atlas HCL extension support requires Atlas Pro for some databases.
Use SQL migrations for open-source Atlas.

---

## 7. search_path Configuration

### Database-level (persists across all connections)

```sql
-- Set for entire database — all users connecting to {DB_NAME}
-- will have these schemas in their search path automatically
ALTER DATABASE {DB_NAME}
  SET search_path = public, extensions, audit, gold, silver, bronze, sandbox;
```

### Verify search_path

```sql
-- Check current setting
SHOW search_path;

-- Check DB-level setting
SELECT datname, datconfig
FROM pg_database
WHERE datname = '{DB_NAME}';
```

### In DATABASE_URL (for application connections)

```
postgres://user:pass@host:5432/{DB_NAME}?search_path=public,extensions,audit,gold,silver,bronze,sandbox&sslmode=disable
```

---

## 8. Atlas `mode: roles = true`

To include roles in Atlas schema inspection and diff:

```hcl
env "local" {
  url = getenv("DATABASE_URL")
  dev = "docker://postgres/16/dev?search_path=public"

  mode {
    roles       = true  # Include roles in inspection
    permissions = true  # Include grants in inspection
    sensitive   = ALLOW # Allow passwords in planning (use with care)
  }
}
```

**When to use:** If you want Atlas to manage roles declaratively in HCL and detect drift.
For this skill, we manage roles via SQL migrations (clearer, version-controlled).
Enable `mode { roles = true }` only if you need Atlas to audit role drift in CI.
