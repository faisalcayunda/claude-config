#!/usr/bin/env bash
# bootstrap.sh — Generate data-mesh-db-boilerplate repo structure v2.0
# Usage: bash bootstrap.sh --domain APM --product funnel-aktivitas-user [--dir ./db] [--port 5432] [--user postgres]
set -euo pipefail

BOLD='\033[1m'; CYAN='\033[36m'; GREEN='\033[32m'; YELLOW='\033[33m'; RESET='\033[0m'
info()    { echo -e "${CYAN}  →${RESET} $1"; }
success() { echo -e "${GREEN}  ✓${RESET} $1"; }
warn()    { echo -e "${YELLOW}  ⚠${RESET} $1"; }
header()  { echo -e "\n${BOLD}$1${RESET}"; }

DOMAIN=""; PRODUCT=""; TARGET_DIR="."; PG_PORT="5432"; PG_USER="postgres"
while [[ $# -gt 0 ]]; do
  case $1 in
    --domain)   DOMAIN="$2";     shift 2 ;;
    --product)  PRODUCT="$2";    shift 2 ;;
    --dir)      TARGET_DIR="$2"; shift 2 ;;
    --port)     PG_PORT="$2";    shift 2 ;;
    --user)     PG_USER="$2";    shift 2 ;;
    *) echo "Unknown: $1"; exit 1 ;;
  esac
done

[[ -z "$DOMAIN" || -z "$PRODUCT" ]] && { echo "Usage: bash bootstrap.sh --domain APM --product funnel-aktivitas-user"; exit 1; }

DB_NAME=$(echo "${DOMAIN}_${PRODUCT}" | tr '[:upper:]' '[:lower:]' | tr '-' '_')
ROLE_OWNER="${DB_NAME}"
ROLE_READONLY="${DB_NAME}_readonly"
ROLE_READWRITE="${DB_NAME}_readwrite"
ROLE_OPS="${DB_NAME}_ops"

header "⚡ Data Mesh DB Boilerplate v2.0"
echo "  DB Name : ${DB_NAME}"
echo "  Roles   : ${ROLE_OWNER} | ${ROLE_READONLY} | ${ROLE_READWRITE} | ${ROLE_OPS}"
echo "  Schemas : sandbox, extensions, bronze, silver, gold, audit"
echo "  Target  : ${TARGET_DIR}"

mkdir -p "${TARGET_DIR}/config" "${TARGET_DIR}/schema" "${TARGET_DIR}/migrations" "${TARGET_DIR}/scripts"

header "📁 Generating files..."

# .gitignore
cat > "${TARGET_DIR}/.gitignore" << 'EOF'
.env
*.env.local
.direnv/
__pycache__/
*.pyc
.DS_Store
EOF
success ".gitignore"

# .env.example
cat > "${TARGET_DIR}/.env.example" << EOF
# ${DB_NAME} — Atlas Database Configuration
# cp .env.example .env && set PG_PASSWORD. JANGAN commit .env!

DB_NAME=${DB_NAME}
PG_HOST=localhost
PG_PORT=${PG_PORT}
PG_USER=${PG_USER}
PG_PASSWORD=changeme

# Constructed URLs (search_path disertakan)
DATABASE_URL=postgres://\${PG_USER}:\${PG_PASSWORD}@\${PG_HOST}:\${PG_PORT}/\${DB_NAME}?search_path=public,extensions,audit,gold,silver,bronze,sandbox&sslmode=disable
DEV_DATABASE_URL=docker://postgres/16/dev?search_path=public

# Staging & Production (isi via CI/CD secrets)
# STAGING_DATABASE_URL=postgres://...
# PROD_DATABASE_URL=postgres://...
# ATLAS_TOKEN=your_atlas_token
EOF
success ".env.example"

[[ ! -f "${TARGET_DIR}/.env" ]] && cp "${TARGET_DIR}/.env.example" "${TARGET_DIR}/.env" && success ".env (isi PG_PASSWORD!)" || warn ".env already exists"

# .envrc
cat > "${TARGET_DIR}/.envrc" << 'EOF'
# .envrc — direnv | run: direnv allow
if [ -f .env ]; then dotenv .env; fi
export ATLAS_ENV=local
echo "✓ direnv: ${DB_NAME} loaded — HOST=${PG_HOST}:${PG_PORT} DB=${DB_NAME}"
EOF
success ".envrc"

# atlas.hcl
cat > "${TARGET_DIR}/atlas.hcl" << EOF
# atlas.hcl — ${DB_NAME} | Docs: https://atlasgo.io/atlas-schema/projects

data "hcl_schema" "app" {
  paths = fileset("schema/**/*.pg.hcl")
}

env "local" {
  url = getenv("DATABASE_URL")
  dev = "docker://postgres/16/dev?search_path=public"
  src = data.hcl_schema.app.url
  migration { dir = "file://migrations" }
  lint { destructive { error = false } }
}

env "staging" {
  url = getenv("STAGING_DATABASE_URL")
  dev = "docker://postgres/16/dev?search_path=public"
  src = data.hcl_schema.app.url
  migration { dir = "file://migrations" }
  lint { destructive { error = true } }
}

env "prod" {
  url = getenv("PROD_DATABASE_URL")
  dev = "docker://postgres/16/dev?search_path=public"
  migration { dir = "file://migrations" }
  lint {
    destructive { error = true }
    concurrent_index { error = true }
  }
}
EOF
success "atlas.hcl"

# config/user-role-mapping.yaml
cat > "${TARGET_DIR}/config/user-role-mapping.yaml" << EOF
# user-role-mapping.yaml — Map login users → provisioned roles
# Run: make apply-grants | make apply-grants-dry (preview)
# Login users harus sudah dibuat di PostgreSQL: CREATE USER ... LOGIN PASSWORD '...'
# File ini AMAN untuk di-commit (tidak ada credential).

db_name: ${DB_NAME}

roles:
  owner:
    role: ${ROLE_OWNER}
    comment: "DB owner — full privileges"
    members: []
    # - username: svc_owner
    #   comment: "Owner service account"

  readonly:
    role: ${ROLE_READONLY}
    comment: "Read-only: CONNECT + USAGE + SELECT"
    members: []
    # - username: analyst_jane
    #   comment: "Data analyst"
    # - username: svc_metabase
    #   comment: "Metabase BI tool"

  readwrite:
    role: ${ROLE_READWRITE}
    comment: "Read-write DML (no DROP/TRUNCATE). CREATE TABLE in sandbox only."
    members: []
    # - username: dev_john
    #   comment: "Developer"

  ops:
    role: ${ROLE_OPS}
    comment: "Ops: pipelines, ETL. CREATE TABLE in bronze + sandbox."
    members: []
    # - username: svc_airbyte
    #   comment: "Airbyte ingestion"
    # - username: svc_dbt
    #   comment: "dbt transformation"
EOF
success "config/user-role-mapping.yaml"

# config/extensions.yaml
cat > "${TARGET_DIR}/config/extensions.yaml" << EOF
# extensions.yaml — PostgreSQL extensions untuk ${DB_NAME}
# Semua diinstall di schema 'extensions' kecuali pg_stat_statements
# ⚠ pg_stat_statements: butuh shared_preload_libraries di postgresql.conf

schema: extensions

extensions:
  - name: pgcrypto
    comment: "Cryptographic functions"
    enabled: true
  - name: pg_trgm
    comment: "Trigram similarity — fuzzy search"
    enabled: true
  - name: pg_stat_statements
    comment: "Query tracking — REQUIRES shared_preload_libraries config"
    enabled: true
    schema_override: pg_catalog
  - name: dblink
    comment: "Cross-database queries"
    enabled: true
  - name: postgres_fdw
    comment: "Foreign Data Wrapper"
    enabled: true
  - name: uuid-ossp
    comment: "UUID generation functions"
    enabled: true
EOF
success "config/extensions.yaml"

# schema/schemas.pg.hcl
cat > "${TARGET_DIR}/schema/schemas.pg.hcl" << EOF
# schemas.pg.hcl — 6 standard schemas untuk ${DB_NAME}
# Roles dan grants: migrations/00000001_provision_db.sql

schema "sandbox"    { comment = "Exploration area — readwrite + ops dapat CREATE TABLE" }
schema "extensions" { comment = "PostgreSQL extensions — diinstall di sini, bukan di public" }
schema "bronze"     { comment = "Raw ingestion layer — source-aligned, append-only" }
schema "silver"     { comment = "Cleaned + validated data — conformance layer" }
schema "gold"       { comment = "Curated aggregations + serving layer — read-heavy" }
schema "audit"      { comment = "Immutable audit + lineage logs — append-only" }
EOF
success "schema/schemas.pg.hcl"

# schema/tables.pg.hcl (starter)
cat > "${TARGET_DIR}/schema/tables.pg.hcl" << EOF
# tables.pg.hcl — Starter schema untuk ${DB_NAME}
# Edit sesuai kebutuhan data product. Hapus contoh table ini jika tidak diperlukan.
#
# UUID v7 (RECOMMENDED) vs v4:
#   extensions.uuid_generate_v7()  ← time-ordered, reduces index fragmentation
#   gen_random_uuid()              ← fully random PG13+ built-in (fallback only)
#
# Polyfill uuid_generate_v7() diinstall di 00000001_provision_db.sql.
# Dengan search_path = public, extensions, ..., dapat dipanggil tanpa prefix.

table "user_events_raw" {
  schema  = schema.bronze
  comment = "Raw user events — DO NOT MODIFY after ingestion"

  column "id" {
    type    = uuid
    null    = false
    default = sql("extensions.uuid_generate_v7()")
    comment = "UUID v7 PK — time-ordered for B-tree index performance"
  }
  column "event_id"   { type = character_varying(255); null = false; comment = "Source event ID" }
  column "event_type" { type = character_varying(100); null = false }
  column "user_id"    { type = character_varying(255); null = true }
  column "session_id" { type = character_varying(255); null = true }
  column "properties" { type = jsonb; null = true; comment = "Event properties as JSON" }
  column "occurred_at"{ type = timestamptz; null = false }
  column "ingested_at"{ type = timestamptz; null = false; default = sql("now()") }
  column "created_at" { type = timestamptz; null = false; default = sql("now()") }
  column "updated_at" { type = timestamptz; null = false; default = sql("now()") }
  column "created_by" { type = character_varying(255); null = false; default = "system" }
  column "is_deleted" { type = boolean; null = false; default = false }

  primary_key { columns = [column.id] }
  index "idx_user_events_raw_event_id" { columns = [column.event_id]; unique = true }
  index "idx_user_events_raw_user_id"  { columns = [column.user_id];  where  = "user_id IS NOT NULL" }
  index "idx_user_events_raw_occurred" { columns = [column.occurred_at] }
  index "idx_user_events_raw_type"     { columns = [column.event_type] }
}
EOF
success "schema/tables.pg.hcl"

# migrations/00000001_provision_db.sql
MIGRATION_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
cat > "${TARGET_DIR}/migrations/00000001_provision_db.sql" << EOF
-- provision_db.sql — Database Provisioning
-- Data Product : ${DOMAIN}/${PRODUCT} | DB: ${DB_NAME} | Generated: ${MIGRATION_DATE}
-- Run as: psql -U postgres -d ${DB_NAME} -f this_file.sql
-- Or via: atlas migrate hash --env local && atlas migrate apply --env local

BEGIN;

-- ============================================================
-- 1. ROLES (idempotent via DO blocks)
-- ============================================================
DO \$\$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '${ROLE_OWNER}') THEN
    CREATE ROLE ${ROLE_OWNER} NOLOGIN NOINHERIT;
    RAISE NOTICE 'Created: ${ROLE_OWNER}';
  END IF;
END \$\$;
DO \$\$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '${ROLE_READONLY}') THEN
    CREATE ROLE ${ROLE_READONLY} NOLOGIN NOINHERIT;
    RAISE NOTICE 'Created: ${ROLE_READONLY}';
  END IF;
END \$\$;
DO \$\$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '${ROLE_READWRITE}') THEN
    CREATE ROLE ${ROLE_READWRITE} NOLOGIN NOINHERIT;
    RAISE NOTICE 'Created: ${ROLE_READWRITE}';
  END IF;
END \$\$;
DO \$\$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '${ROLE_OPS}') THEN
    CREATE ROLE ${ROLE_OPS} NOLOGIN NOINHERIT;
    RAISE NOTICE 'Created: ${ROLE_OPS}';
  END IF;
END \$\$;

-- ============================================================
-- 2. SCHEMAS
-- ============================================================
CREATE SCHEMA IF NOT EXISTS sandbox;
CREATE SCHEMA IF NOT EXISTS extensions;
CREATE SCHEMA IF NOT EXISTS bronze;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;
CREATE SCHEMA IF NOT EXISTS audit;

ALTER SCHEMA sandbox    OWNER TO ${ROLE_OWNER};
ALTER SCHEMA extensions OWNER TO ${ROLE_OWNER};
ALTER SCHEMA bronze     OWNER TO ${ROLE_OWNER};
ALTER SCHEMA silver     OWNER TO ${ROLE_OWNER};
ALTER SCHEMA gold       OWNER TO ${ROLE_OWNER};
ALTER SCHEMA audit      OWNER TO ${ROLE_OWNER};

COMMENT ON SCHEMA sandbox    IS 'Exploration area — readwrite + ops CREATE TABLE';
COMMENT ON SCHEMA extensions IS 'PostgreSQL extensions';
COMMENT ON SCHEMA bronze     IS 'Raw ingestion — source-aligned, append-only';
COMMENT ON SCHEMA silver     IS 'Cleaned + validated — conformance layer';
COMMENT ON SCHEMA gold       IS 'Curated aggregations + serving layer';
COMMENT ON SCHEMA audit      IS 'Immutable audit + lineage logs';

-- ============================================================
-- 3. SECURITY HARDENING
-- ============================================================
REVOKE CREATE    ON SCHEMA public FROM PUBLIC;
REVOKE CONNECT   ON DATABASE ${DB_NAME} FROM PUBLIC;

-- ============================================================
-- 4. GRANT CONNECT
-- ============================================================
GRANT CONNECT ON DATABASE ${DB_NAME} TO ${ROLE_READONLY};
GRANT CONNECT ON DATABASE ${DB_NAME} TO ${ROLE_READWRITE};
GRANT CONNECT ON DATABASE ${DB_NAME} TO ${ROLE_OPS};

-- ============================================================
-- 5. SCHEMA GRANTS + DEFAULT PRIVILEGES
-- Matrix: see references/atlas-security.md
-- ============================================================

-- sandbox (exploration: readwrite+ops can CREATE TABLE)
GRANT USAGE           ON SCHEMA sandbox TO ${ROLE_READONLY};
GRANT SELECT          ON ALL TABLES IN SCHEMA sandbox TO ${ROLE_READONLY};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA sandbox
  GRANT SELECT ON TABLES TO ${ROLE_READONLY};

GRANT USAGE, CREATE   ON SCHEMA sandbox TO ${ROLE_READWRITE};
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA sandbox TO ${ROLE_READWRITE};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA sandbox
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO ${ROLE_READWRITE};

GRANT USAGE, CREATE   ON SCHEMA sandbox TO ${ROLE_OPS};
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA sandbox TO ${ROLE_OPS};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA sandbox
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO ${ROLE_OPS};

-- extensions (USAGE only — no table grants)
GRANT USAGE ON SCHEMA extensions TO ${ROLE_READONLY};
GRANT USAGE ON SCHEMA extensions TO ${ROLE_READWRITE};
GRANT USAGE ON SCHEMA extensions TO ${ROLE_OPS};

-- bronze (raw ingestion: ops can CREATE TABLE)
GRANT USAGE ON SCHEMA bronze TO ${ROLE_READONLY};
GRANT SELECT ON ALL TABLES IN SCHEMA bronze TO ${ROLE_READONLY};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA bronze
  GRANT SELECT ON TABLES TO ${ROLE_READONLY};

GRANT USAGE ON SCHEMA bronze TO ${ROLE_READWRITE};
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA bronze TO ${ROLE_READWRITE};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA bronze
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO ${ROLE_READWRITE};

GRANT USAGE, CREATE   ON SCHEMA bronze TO ${ROLE_OPS};
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA bronze TO ${ROLE_OPS};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA bronze
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO ${ROLE_OPS};

-- silver (cleaned: full DML for readwrite + ops)
GRANT USAGE ON SCHEMA silver TO ${ROLE_READONLY};
GRANT SELECT ON ALL TABLES IN SCHEMA silver TO ${ROLE_READONLY};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA silver
  GRANT SELECT ON TABLES TO ${ROLE_READONLY};

GRANT USAGE ON SCHEMA silver TO ${ROLE_READWRITE};
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA silver TO ${ROLE_READWRITE};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA silver
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO ${ROLE_READWRITE};

GRANT USAGE ON SCHEMA silver TO ${ROLE_OPS};
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA silver TO ${ROLE_OPS};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA silver
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO ${ROLE_OPS};

-- gold (serving: ops is read-only)
GRANT USAGE ON SCHEMA gold TO ${ROLE_READONLY};
GRANT SELECT ON ALL TABLES IN SCHEMA gold TO ${ROLE_READONLY};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA gold
  GRANT SELECT ON TABLES TO ${ROLE_READONLY};

GRANT USAGE ON SCHEMA gold TO ${ROLE_READWRITE};
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA gold TO ${ROLE_READWRITE};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA gold
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO ${ROLE_READWRITE};

GRANT USAGE ON SCHEMA gold TO ${ROLE_OPS};
GRANT SELECT ON ALL TABLES IN SCHEMA gold TO ${ROLE_OPS};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA gold
  GRANT SELECT ON TABLES TO ${ROLE_OPS};

-- audit (append-only: readwrite=read, ops=insert only)
GRANT USAGE ON SCHEMA audit TO ${ROLE_READONLY};
GRANT SELECT ON ALL TABLES IN SCHEMA audit TO ${ROLE_READONLY};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA audit
  GRANT SELECT ON TABLES TO ${ROLE_READONLY};

GRANT USAGE ON SCHEMA audit TO ${ROLE_READWRITE};
GRANT SELECT ON ALL TABLES IN SCHEMA audit TO ${ROLE_READWRITE};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA audit
  GRANT SELECT ON TABLES TO ${ROLE_READWRITE};

GRANT USAGE ON SCHEMA audit TO ${ROLE_OPS};
GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA audit TO ${ROLE_OPS};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA audit
  GRANT SELECT, INSERT ON TABLES TO ${ROLE_OPS};

-- ============================================================
-- 6. EXTENSIONS (di schema extensions)
-- ⚠ pg_stat_statements: uncomment SETELAH shared_preload_libraries config
-- ============================================================
SET search_path = extensions, public;

CREATE EXTENSION IF NOT EXISTS pgcrypto       WITH SCHEMA extensions;
CREATE EXTENSION IF NOT EXISTS pg_trgm        WITH SCHEMA extensions;
CREATE EXTENSION IF NOT EXISTS dblink         WITH SCHEMA extensions;
CREATE EXTENSION IF NOT EXISTS postgres_fdw   WITH SCHEMA extensions;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"    WITH SCHEMA extensions;

-- Uncomment setelah shared_preload_libraries = 'pg_stat_statements' di postgresql.conf:
-- CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA extensions TO ${ROLE_READONLY};
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA extensions TO ${ROLE_READWRITE};
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA extensions TO ${ROLE_OPS};

ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA extensions
  GRANT EXECUTE ON FUNCTIONS TO ${ROLE_READONLY};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA extensions
  GRANT EXECUTE ON FUNCTIONS TO ${ROLE_READWRITE};
ALTER DEFAULT PRIVILEGES FOR ROLE ${ROLE_OWNER} IN SCHEMA extensions
  GRANT EXECUTE ON FUNCTIONS TO ${ROLE_OPS};

-- ============================================================
-- 6b. UUID v7 POLYFILL
-- UUID v7 native hanya di PostgreSQL 18+. Polyfill ini untuk PG <18 (RDS PG 17).
-- Keunggulan: time-ordered, monotonic, reduces B-tree index fragmentation.
-- Requires: pgcrypto (diinstall di atas)
-- Usage: DEFAULT extensions.uuid_generate_v7()
-- Test : SELECT extensions.uuid_generate_v7();
-- ============================================================

CREATE OR REPLACE FUNCTION extensions.uuid_generate_v7()
RETURNS uuid
AS \$\$
DECLARE
  unix_ts_ms bytea;
  uuid_bytes bytea;
BEGIN
  -- 1. Unix timestamp in milliseconds (48 bits / 6 bytes)
  unix_ts_ms := decode(
    lpad(to_hex(floor(extract(epoch from clock_timestamp()) * 1000)::bigint), 12, '0'),
    'hex'
  );
  -- 2. Random 10 bytes via pgcrypto (schema-qualified to avoid search_path issues)
  uuid_bytes := unix_ts_ms || extensions.gen_random_bytes(10);
  -- 3. Set version = 7 (0111) at byte 6
  uuid_bytes := set_byte(uuid_bytes, 6, (get_byte(uuid_bytes, 6) & 15) | 112);
  -- 4. Set variant = 2 (10) at byte 8
  uuid_bytes := set_byte(uuid_bytes, 8, (get_byte(uuid_bytes, 8) & 63) | 128);
  RETURN encode(uuid_bytes, 'hex')::uuid;
END;
\$\$ LANGUAGE plpgsql VOLATILE;

COMMENT ON FUNCTION extensions.uuid_generate_v7() IS
  'UUID v7 polyfill for PostgreSQL <18. Time-ordered UUID. Requires: pgcrypto.';

DO \$\$
DECLARE v_test uuid;
BEGIN
  v_test := extensions.uuid_generate_v7();
  RAISE NOTICE '✓ uuid_generate_v7() polyfill OK → %', v_test;
END \$\$;

-- ============================================================
-- 7. SEARCH PATH
-- Order: public, extensions, audit, gold, silver, bronze, sandbox
-- extensions di depan agar uuid_generate_v7() bisa dipanggil tanpa prefix.
-- ============================================================
ALTER DATABASE ${DB_NAME}
  SET search_path = public, extensions, audit, gold, silver, bronze, sandbox;

DO \$\$
BEGIN
  RAISE NOTICE '✓ Provisioning selesai: ${DB_NAME}';
  RAISE NOTICE '  Roles      : ${ROLE_OWNER} | ${ROLE_READONLY} | ${ROLE_READWRITE} | ${ROLE_OPS}';
  RAISE NOTICE '  Schemas    : sandbox, extensions, bronze, silver, gold, audit';
  RAISE NOTICE '  Extensions : pgcrypto, pg_trgm, dblink, postgres_fdw, uuid-ossp';
  RAISE NOTICE '  UUID v7    : extensions.uuid_generate_v7() — polyfill aktif';
  RAISE NOTICE '  search_path: public, extensions, audit, gold, silver, bronze, sandbox';
  RAISE NOTICE '  ⚠ pg_stat_statements: uncomment setelah shared_preload_libraries config';
  RAISE NOTICE '  ⚠ Next: make apply-grants';
END \$\$;

COMMIT;
EOF
success "migrations/00000001_provision_db.sql"

# scripts/apply-user-grants.py
cat > "${TARGET_DIR}/scripts/apply-user-grants.py" << 'PYEOF'
#!/usr/bin/env python3
"""apply-user-grants.py — Apply user→role mappings from config/user-role-mapping.yaml
Usage:
  python3 scripts/apply-user-grants.py --config config/user-role-mapping.yaml --url $DATABASE_URL
  python3 scripts/apply-user-grants.py --config config/user-role-mapping.yaml --url $DATABASE_URL --dry-run
  python3 scripts/apply-user-grants.py --config config/user-role-mapping.yaml --url $DATABASE_URL --verbose
"""
import argparse, sys, subprocess
try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install pyyaml"); sys.exit(1)

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--config",   required=True)
    p.add_argument("--url",      required=True)
    p.add_argument("--dry-run",  action="store_true")
    p.add_argument("--verbose",  action="store_true")
    return p.parse_args()

def psql(url, sql, dry_run, verbose):
    if dry_run:
        print(f"  [DRY-RUN] {sql}"); return True
    if verbose: print(f"  Exec: {sql}")
    r = subprocess.run(["psql", url, "-c", sql, "--no-psqlrc", "-v", "ON_ERROR_STOP=1"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  ✗ {r.stderr.strip()}"); return False
    return True

def user_exists(url, username):
    r = subprocess.run(["psql", url, "-t", "-c",
                        f"SELECT 1 FROM pg_roles WHERE rolname='{username}';",
                        "--no-psqlrc"], capture_output=True, text=True)
    return "1" in r.stdout

def main():
    args = parse_args()
    config = yaml.safe_load(open(args.config))
    db_name = config.get("db_name", "?")
    mode = "[DRY-RUN]" if args.dry_run else "[APPLY]"
    print(f"\n{mode} User grants for: {db_name}  ({args.config})\n")
    total = success = errors = 0
    for rtype, rc in config.get("roles", {}).items():
        role = rc.get("role", ""); members = rc.get("members") or []
        if not members:
            print(f"  • {role}: no members, skipping"); continue
        print(f"  • {role}")
        for m in members:
            username = m.get("username", "").strip()
            if not username: continue
            total += 1
            if not args.dry_run and not user_exists(args.url, username):
                print(f"    ✗ SKIP {username}: does not exist in PostgreSQL"); errors += 1; continue
            sql = f"GRANT {role} TO {username};"
            if psql(args.url, sql, args.dry_run, args.verbose):
                print(f"    ✓ GRANT {role} → {username}  ({m.get('comment','')})"); success += 1
            else:
                print(f"    ✗ FAILED → {username}"); errors += 1
    print(f"\nSummary: {success}/{total} applied, {errors} errors")
    sys.exit(1 if errors > 0 else 0)

if __name__ == "__main__": main()
PYEOF
chmod +x "${TARGET_DIR}/scripts/apply-user-grants.py"
success "scripts/apply-user-grants.py"

# scripts/verify-roles.sh
cat > "${TARGET_DIR}/scripts/verify-roles.sh" << EOF
#!/usr/bin/env bash
# verify-roles.sh — Verify role + schema setup for ${DB_NAME}
DB_URL="\${DATABASE_URL:-}"
[[ -z "\$DB_URL" ]] && { echo "Error: DATABASE_URL not set. Run: direnv allow"; exit 1; }

echo ""
echo "══════════════════════════════════════════════════"
echo "  Verification: ${DB_NAME}"
echo "══════════════════════════════════════════════════"

echo -e "\n── Roles ──────────────────────────────────────"
psql "\$DB_URL" -c "SELECT rolname, rolcanlogin, rolinherit FROM pg_roles WHERE rolname LIKE '${DB_NAME}%' ORDER BY rolname;" 2>/dev/null

echo -e "\n── Schemas ─────────────────────────────────────"
psql "\$DB_URL" -c "SELECT nspname AS schema, pg_get_userbyid(nspowner) AS owner, obj_description(oid,'pg_namespace') AS description FROM pg_namespace WHERE nspname IN ('sandbox','extensions','bronze','silver','gold','audit') ORDER BY nspname;" 2>/dev/null

echo -e "\n── Role Memberships ────────────────────────────"
psql "\$DB_URL" -c "SELECT r.rolname AS role, m.rolname AS member FROM pg_auth_members am JOIN pg_roles r ON r.oid=am.roleid JOIN pg_roles m ON m.oid=am.member WHERE r.rolname LIKE '${DB_NAME}%' ORDER BY r.rolname, m.rolname;" 2>/dev/null

echo -e "\n── Installed Extensions ────────────────────────"
psql "\$DB_URL" -c "SELECT extname, extversion, nspname AS schema FROM pg_extension JOIN pg_namespace ON oid=extnamespace ORDER BY extname;" 2>/dev/null

echo -e "\n── Search Path ─────────────────────────────────"
psql "\$DB_URL" -c "SHOW search_path;" 2>/dev/null

echo -e "\n── Default Privileges ──────────────────────────"
psql "\$DB_URL" -c "SELECT pg_get_userbyid(d.defaclrole) AS grantor, n.nspname AS schema, CASE d.defaclobjtype WHEN 'r' THEN 'TABLE' WHEN 'S' THEN 'SEQ' WHEN 'f' THEN 'FUNC' END AS type, d.defaclacl AS acl FROM pg_default_acl d LEFT JOIN pg_namespace n ON n.oid=d.defaclnamespace WHERE pg_get_userbyid(d.defaclrole)='${ROLE_OWNER}' ORDER BY schema, type;" 2>/dev/null
echo ""
EOF
chmod +x "${TARGET_DIR}/scripts/verify-roles.sh"
success "scripts/verify-roles.sh"

# Makefile
cat > "${TARGET_DIR}/Makefile" << EOF
# Makefile — ${DB_NAME}
.PHONY: help diff apply status inspect lint validate push hash erd apply-grants apply-grants-dry verify-roles

ENV     ?= local
DB_NAME := ${DB_NAME}

help:
	@echo ""
	@echo "  Atlas:"
	@echo "    diff             Generate migration from schema changes"
	@echo "    apply            Apply pending migrations"
	@echo "    status           Show migration status"
	@echo "    inspect          Inspect current DB schema (HCL)"
	@echo "    lint             Lint latest migration"
	@echo "    validate         Validate schema HCL files"
	@echo "    hash             Rehash migrations after manual edits"
	@echo "    erd              Open ERD in browser (requires atlas login)"
	@echo ""
	@echo "  Provisioning:"
	@echo "    apply-grants     Apply config/user-role-mapping.yaml"
	@echo "    apply-grants-dry Preview grants (dry-run)"
	@echo "    verify-roles     Verify roles, schemas, extensions"
	@echo ""
	@echo "  Usage: make <cmd> [ENV=staging|prod]"

diff:             ; atlas migrate diff --env \$(ENV)
apply:            ; atlas migrate apply --env \$(ENV)
status:           ; atlas migrate status --env \$(ENV)
inspect:          ; atlas schema inspect --env \$(ENV)
lint:             ; atlas migrate lint --env \$(ENV) --latest 1
validate:         ; atlas schema validate --env \$(ENV)
push:             ; atlas migrate push \$(DB_NAME) --env \$(ENV)
hash:             ; atlas migrate hash --env \$(ENV)
erd:              ; atlas schema inspect --env \$(ENV) -w
apply-grants:     ; python3 scripts/apply-user-grants.py --config config/user-role-mapping.yaml --url "\$\${DATABASE_URL}" --verbose
apply-grants-dry: ; python3 scripts/apply-user-grants.py --config config/user-role-mapping.yaml --url "\$\${DATABASE_URL}" --dry-run
verify-roles:     ; bash scripts/verify-roles.sh
EOF
success "Makefile"

# README.md
cat > "${TARGET_DIR}/README.md" << EOF
# ${DB_NAME}

Database untuk Data Product **${DOMAIN}/${PRODUCT}** — dikelola dengan [Atlas](https://atlasgo.io).

| | |
|---|---|
| **DB Name** | \`${DB_NAME}\` |
| **Roles** | \`${ROLE_OWNER}\` / \`${ROLE_READONLY}\` / \`${ROLE_READWRITE}\` / \`${ROLE_OPS}\` |
| **Schemas** | \`sandbox\` \`extensions\` \`bronze\` \`silver\` \`gold\` \`audit\` |

## Quick Start

\`\`\`bash
# 1. Setup environment
cp .env.example .env && nano .env    # set PG_PASSWORD
direnv allow

# 2. Buat database
psql -U ${PG_USER} -c "CREATE DATABASE ${DB_NAME};"

# 3. Hash + apply provision migration (roles, schemas, grants, extensions)
atlas migrate hash --env local
atlas migrate apply --env local

# 4. Verify
make verify-roles

# 5. Tambahkan users ke roles
nano config/user-role-mapping.yaml
make apply-grants-dry                # preview
make apply-grants                    # apply

# 6. Design schema
# edit schema/tables.pg.hcl
make diff    # generate migration
make apply   # apply
\`\`\`

## Role Matrix

| Schema | \`_readonly\` | \`_readwrite\` | \`_ops\` |
|---|---|---|---|
| **sandbox** | USAGE, SELECT | USAGE+CREATE, DML | USAGE+CREATE, DML |
| **extensions** | USAGE | USAGE | USAGE |
| **bronze** | USAGE, SELECT | USAGE, DML | USAGE+CREATE, DML |
| **silver** | USAGE, SELECT | USAGE, DML | USAGE, DML |
| **gold** | USAGE, SELECT | USAGE, DML | USAGE, SELECT |
| **audit** | USAGE, SELECT | USAGE, SELECT | USAGE, SELECT+INSERT |

DML = SELECT/INSERT/UPDATE/DELETE. No DROP/TRUNCATE for any non-owner role.

## ⚠ pg_stat_statements
Tambahkan ke \`postgresql.conf\`:
\`\`\`
shared_preload_libraries = 'pg_stat_statements'
\`\`\`
Restart PostgreSQL, lalu uncomment di \`migrations/00000001_provision_db.sql\`.
EOF
success "README.md"

# docs/DEVELOPER_GUIDE.md — comprehensive developer reference
mkdir -p "${TARGET_DIR}/docs"
cat > "${TARGET_DIR}/docs/DEVELOPER_GUIDE.md" << 'GUIDE_HEREDOC'
<!-- AUTO-GENERATED by data-mesh-db-boilerplate bootstrap.sh — DO NOT EDIT HEADER -->
GUIDE_HEREDOC

# Replace placeholder and append the full content
cat >> "${TARGET_DIR}/docs/DEVELOPER_GUIDE.md" << EOF
# Developer Guide — ${DB_NAME}

> **Data Product:** ${DOMAIN} / ${PRODUCT}
> **DB:** \`${DB_NAME}\` | **PG target:** ≥ 13 (polyfill covers < 18 for UUID v7)
> **Migration tool:** [Atlas](https://atlasgo.io) | **Env manager:** [direnv](https://direnv.net)

---

## Table of Contents

1. [Prerequisites & Installation](#1-prerequisites--installation)
2. [Initial Setup (First Time)](#2-initial-setup-first-time)
3. [Directory Structure](#3-directory-structure)
4. [Daily Development Workflow](#4-daily-development-workflow)
5. [Schema Design Guide](#5-schema-design-guide)
6. [UUID v7 Usage Guide](#6-uuid-v7-usage-guide)
7. [Extension Usage Guide](#7-extension-usage-guide)
8. [Role & Access Management](#8-role--access-management)
9. [Environment Management](#9-environment-management)
10. [Makefile Quick Reference](#10-makefile-quick-reference)
11. [Multi-Environment Deployment](#11-multi-environment-deployment)
12. [Troubleshooting](#12-troubleshooting)
13. [CI/CD Integration](#13-cicd-integration)

---

## 1. Prerequisites & Installation

### Required tools

| Tool | Version | Install |
|---|---|---|
| [Atlas CLI](https://atlasgo.io) | latest | \`curl -sSf https://atlasgo.sh | sh\` |
| [direnv](https://direnv.net) | ≥ 2.32 | \`brew install direnv\` / \`apt install direnv\` |
| [Docker](https://docker.com) | ≥ 24 | Required for dev database (Atlas uses it internally) |
| PostgreSQL client (\`psql\`) | ≥ 13 | \`brew install libpq\` / \`apt install postgresql-client\` |
| Python | ≥ 3.8 | For \`scripts/apply-user-grants.py\` |
| PyYAML | any | \`pip install pyyaml\` |

### Shell integration

Add **direnv hook** to your shell rc file — required for automatic \`.env\` loading:

\`\`\`bash
# ~/.zshrc
eval "\$(direnv hook zsh)"

# ~/.bashrc
eval "\$(direnv hook bash)"
\`\`\`

Then restart your shell or run \`source ~/.zshrc\`.

### Verify installations

\`\`\`bash
atlas version          # Atlas v0.x.x
direnv version         # 2.x.x
docker info            # confirms Docker is running
psql --version         # psql (PostgreSQL) 1x.x
python3 --version      # Python 3.x.x
python3 -c "import yaml; print('PyYAML OK')"
\`\`\`

---

## 2. Initial Setup (First Time)

Follow these steps **in order** — each step depends on the previous one.

### Step 1 — Configure environment

\`\`\`bash
cp .env.example .env
\`\`\`

Open \`.env\` and fill in your values:

\`\`\`bash
# Required — change this:
PG_PASSWORD=your_secure_password_here

# Verify the rest (defaults are usually correct for local dev):
PG_HOST=localhost
PG_PORT=${PG_PORT}
PG_USER=${PG_USER}
DB_NAME=${DB_NAME}
\`\`\`

> ⚠ Never commit \`.env\`. It is in \`.gitignore\`.

### Step 2 — Allow direnv

\`\`\`bash
direnv allow
\`\`\`

Expected output:
\`\`\`
✓ direnv: ${DB_NAME} loaded
  HOST=localhost:${PG_PORT} | DB=${DB_NAME} | USER=${PG_USER}
\`\`\`

Every time you \`cd\` into this directory, direnv will automatically load your \`.env\`
into the shell environment. You should see this message each time.

### Step 3 — Create the database

Connect to PostgreSQL as superuser and create the database:

\`\`\`bash
psql -U ${PG_USER} -c "CREATE DATABASE ${DB_NAME};"
\`\`\`

Verify it was created:
\`\`\`bash
psql -U ${PG_USER} -c "\l ${DB_NAME}"
\`\`\`

### Step 4 — Hash the migrations directory

Atlas uses a checksum file (\`atlas.sum\`) to track migration integrity.
Run this once after bootstrap to generate it:

\`\`\`bash
atlas migrate hash --env local
\`\`\`

This creates \`migrations/atlas.sum\`. Commit this file — it is safe and required.

### Step 5 — Apply provision migration

\`\`\`bash
atlas migrate apply --env local
\`\`\`

This runs \`migrations/00000001_provision_db.sql\` which:

- Creates 4 group roles: \`${ROLE_OWNER}\`, \`${ROLE_READONLY}\`, \`${ROLE_READWRITE}\`, \`${ROLE_OPS}\`
- Creates 6 schemas: \`sandbox\`, \`extensions\`, \`bronze\`, \`silver\`, \`gold\`, \`audit\`
- Sets ownership, grants, and DEFAULT PRIVILEGES for each schema per role
- Installs extensions: pgcrypto, pg_trgm, dblink, postgres_fdw, uuid-ossp
- Creates the \`extensions.uuid_generate_v7()\` polyfill function
- Sets \`search_path = public, extensions, audit, gold, silver, bronze, sandbox\`

Expected output:
\`\`\`
Migrating to version 1 (1 pending):
  -- migrating version 1
  -> 00000001_provision_db.sql
NOTICE:  Created: ${ROLE_OWNER}
NOTICE:  Created: ${ROLE_READONLY}
NOTICE:  Created: ${ROLE_READWRITE}
NOTICE:  Created: ${ROLE_OPS}
NOTICE:  ✓ uuid_generate_v7() polyfill OK → 019dbe15-5e49-7ca4-a1c9-...
NOTICE:  ✓ Provisioning selesai: ${DB_NAME}
  -- ok (Xms)
\`\`\`

### Step 6 — Verify setup

\`\`\`bash
make verify-roles
\`\`\`

This shows: roles, schema ownership, installed extensions, search_path, and DEFAULT PRIVILEGES.

### Step 7 — Add users to roles

Edit \`config/user-role-mapping.yaml\` and add login users:

\`\`\`yaml
roles:
  readonly:
    role: ${ROLE_READONLY}
    members:
      - username: analyst_jane
        comment: "Data analyst"
  ops:
    role: ${ROLE_OPS}
    members:
      - username: svc_airbyte
        comment: "Airbyte ingestion"
\`\`\`

> **Note:** Login users must already exist in PostgreSQL:
> \`CREATE USER analyst_jane LOGIN PASSWORD 'secure_pw';\`

Preview and apply:
\`\`\`bash
make apply-grants-dry    # preview without executing
make apply-grants        # apply
\`\`\`

### Step 8 — Design your schema (first table)

Edit \`schema/tables.pg.hcl\`, replace the starter table with your domain objects,
then generate and apply your first table migration:

\`\`\`bash
make diff                # Atlas prompts for migration name — e.g. "initial_schema"
make apply               # applies to database
make status              # confirm: no pending migrations
\`\`\`

---

## 3. Directory Structure

\`\`\`
${DB_NAME}/
│
├── .envrc                        direnv: auto-loads .env on cd
├── .env                          ★ YOUR SECRETS — gitignored, never commit
├── .env.example                  Template — commit this, not .env
├── .gitignore
├── Makefile                      All commands — run: make help
├── atlas.hcl                     Atlas project config (local/staging/prod envs)
│
├── config/
│   ├── user-role-mapping.yaml    ★ EDIT THIS — map login users to roles
│   └── extensions.yaml           Documentation of installed extensions
│
├── schema/
│   ├── schemas.pg.hcl            Declares the 6 schemas (Atlas desired state)
│   └── tables.pg.hcl             ★ EDIT THIS — your table definitions
│
├── migrations/
│   ├── 00000001_provision_db.sql ★ DO NOT EDIT — roles/schemas/grants/extensions
│   ├── <timestamp>_<name>.sql    Generated by: make diff
│   └── atlas.sum                 Atlas integrity checksum — commit this
│
├── scripts/
│   ├── apply-user-grants.py      Reads user-role-mapping.yaml → GRANT users to roles
│   └── verify-roles.sh           Inspect DB: roles, schemas, extensions, grants
│
└── docs/
    └── DEVELOPER_GUIDE.md        This file
\`\`\`

### What to edit vs what not to

| File | Action |
|---|---|
| \`schema/tables.pg.hcl\` | ✅ Edit freely — add/modify your tables |
| \`config/user-role-mapping.yaml\` | ✅ Edit — add login users |
| \`.env\` | ✅ Edit — your local credentials |
| \`migrations/00000001_provision_db.sql\` | ⚠ Edit only to enable pg_stat_statements |
| \`migrations/atlas.sum\` | ❌ Never manually edit — run \`make hash\` instead |
| \`atlas.hcl\` | ⚠ Edit only to add new environments |

---

## 4. Daily Development Workflow

### The core loop

\`\`\`
Edit schema/tables.pg.hcl
        ↓
make diff            ← generates SQL migration file
        ↓
Review migrations/<timestamp>_<name>.sql
        ↓
make lint            ← checks for destructive changes, naming violations
        ↓
git add migrations/ && git commit -m "feat(schema): add <description>"
        ↓
make apply           ← applies to database
        ↓
make status          ← confirm no pending migrations
\`\`\`

### Adding a new table

1. Open \`schema/tables.pg.hcl\`
2. Add your table block (see [Schema Design Guide](#5-schema-design-guide))
3. Run \`make diff\` — enter a descriptive name when prompted (e.g. \`add_sessions_table\`)
4. Review the generated SQL in \`migrations/\`
5. Run \`make lint\` to catch issues
6. Commit both the HCL change and migration file together
7. Run \`make apply\`

### Modifying an existing table

1. Edit the table block in \`schema/tables.pg.hcl\`
   - Add columns: add column block
   - Remove columns: delete block (⚠ destructive — will show lint warning)
   - Rename columns: update name (⚠ Atlas treats as drop + add — see note below)
2. Run \`make diff\` — name it descriptively (e.g. \`add_status_column_to_sessions\`)
3. Review generated SQL carefully
4. Run \`make lint\`
5. Commit and \`make apply\`

> **Renaming columns:** Atlas generates DROP + ADD (data loss risk). Use a two-step migration:
> Step 1: Add new column (migration A). Step 2: Copy data + drop old column (migration B).

### Checking what's pending

\`\`\`bash
make status          # shows applied vs pending migrations
make inspect         # shows current DB schema as HCL (what Atlas sees in DB)
\`\`\`

---

## 5. Schema Design Guide

### Which schema to use?

| Schema | Purpose | Who writes | Who reads |
|---|---|---|---|
| **bronze** | Raw data landed from source systems (Airbyte, Kafka, APIs). Append-only. Never modify after ingestion. | ops | readonly, readwrite, ops |
| **silver** | Cleaned, validated, and conformed data. Transformations of bronze. | readwrite, ops | readonly, readwrite, ops |
| **gold** | Aggregated, curated, KPI outputs. Serving layer for dashboards and APIs. | readwrite | readonly, readwrite, ops (read-only) |
| **audit** | Immutable audit logs and lineage records. Append-only. No UPDATE/DELETE. | ops (insert only) | readonly, readwrite (read-only) |
| **sandbox** | Exploration, prototyping, and temporary tables. Can be recreated anytime. | readwrite, ops | readonly, readwrite, ops |
| **extensions** | PostgreSQL extensions. Do not create application tables here. | owner only | All (USAGE) |

### Standard table pattern

Every table in this repo follows this structure:

\`\`\`hcl
table "sessions" {
  schema  = schema.silver            -- bronze | silver | gold | audit | sandbox
  comment = "User sessions for funnel analysis"

  -- UUID v7 Primary Key (time-ordered — faster inserts, smaller index)
  column "id" {
    type    = uuid
    null    = false
    default = sql("extensions.uuid_generate_v7()")
    comment = "UUID v7 PK — time-ordered for B-tree performance"
  }

  -- Source system reference
  column "external_id" {
    type    = character_varying(255)
    null    = true
    comment = "Identifier from source system (nullable for derived records)"
  }

  -- Your domain columns here
  column "user_id"    { type = uuid; null = false }
  column "started_at" { type = timestamptz; null = false }
  column "ended_at"   { type = timestamptz; null = true }
  column "channel"    { type = character_varying(100); null = true }

  -- Mandatory audit columns (NEVER skip these)
  column "created_at" { type = timestamptz; null = false; default = sql("now()") }
  column "updated_at" { type = timestamptz; null = false; default = sql("now()") }
  column "created_by" {
    type    = character_varying(255)
    null    = false
    default = "system"
    comment = "Service account that created this record"
  }
  column "is_deleted" {
    type    = boolean
    null    = false
    default = false
    comment = "Soft delete — never hard DELETE in data mesh"
  }

  primary_key { columns = [column.id] }

  index "idx_sessions_user_id"    { columns = [column.user_id] }
  index "idx_sessions_started_at" { columns = [column.started_at] }
  index "idx_sessions_external_id" {
    columns = [column.external_id]
    unique  = true
    where   = "external_id IS NOT NULL"
  }
}
\`\`\`

### Bronze table — raw landing pattern

\`\`\`hcl
table "events_raw" {
  schema  = schema.bronze
  comment = "Raw event stream from source — DO NOT MODIFY after ingestion"

  column "id"          { type = uuid; null = false; default = sql("extensions.uuid_generate_v7()") }
  column "source_id"   { type = character_varying(255); null = false; comment = "Source system ID" }
  column "payload"     { type = jsonb; null = false; comment = "Raw payload — schema-less" }
  column "source_name" { type = character_varying(100); null = false }
  column "occurred_at" { type = timestamptz; null = false; comment = "Event time in source" }
  column "ingested_at" { type = timestamptz; null = false; default = sql("now()") }
  column "created_at"  { type = timestamptz; null = false; default = sql("now()") }
  column "updated_at"  { type = timestamptz; null = false; default = sql("now()") }
  column "created_by"  { type = character_varying(255); null = false; default = "system" }
  column "is_deleted"  { type = boolean; null = false; default = false }

  primary_key { columns = [column.id] }
  index "idx_events_raw_source_id"  { columns = [column.source_id] }
  index "idx_events_raw_occurred"   { columns = [column.occurred_at] }
}
\`\`\`

### Audit table — append-only log pattern

\`\`\`hcl
table "change_log" {
  schema  = schema.audit
  comment = "Immutable record of all data changes — append-only"

  column "id"          { type = uuid; null = false; default = sql("extensions.uuid_generate_v7()") }
  column "entity_type" { type = character_varying(100); null = false; comment = "Table name" }
  column "entity_id"   { type = uuid; null = false; comment = "FK to changed record" }
  column "action"      { type = character_varying(20); null = false; comment = "INSERT|UPDATE|DELETE" }
  column "before_data" { type = jsonb; null = true }
  column "after_data"  { type = jsonb; null = true }
  column "changed_by"  { type = character_varying(255); null = false }
  column "changed_at"  { type = timestamptz; null = false; default = sql("now()") }
  column "created_at"  { type = timestamptz; null = false; default = sql("now()") }
  column "updated_at"  { type = timestamptz; null = false; default = sql("now()") }
  column "created_by"  { type = character_varying(255); null = false; default = "system" }
  column "is_deleted"  { type = boolean; null = false; default = false }

  primary_key { columns = [column.id] }
  index "idx_change_log_entity"     { columns = [column.entity_type, column.entity_id] }
  index "idx_change_log_changed_at" { columns = [column.changed_at] }
}
\`\`\`

### Naming conventions

\`\`\`
Tables     : plural snake_case          → user_events, session_steps, funnel_stages
Columns    : snake_case                 → user_id, started_at, is_active
Booleans   : is_* or has_*             → is_deleted, has_consent, is_active
Timestamps : *_at                      → created_at, updated_at, occurred_at
Foreign keys: {table_singular}_id      → user_id, session_id, product_id
Indexes    : idx_{table}_{columns}     → idx_sessions_user_id
Unique     : uq_{table}_{columns}      → uq_users_email
FK constraints: fk_{table}_{ref}       → fk_sessions_users
\`\`\`

---

## 6. UUID v7 Usage Guide

### Why UUID v7 instead of v4?

UUID v4 is fully random. When used as a B-tree primary key, random values cause
**index fragmentation** — new rows are inserted at random positions in the index,
requiring frequent page splits and vacuuming. For write-heavy tables, this significantly
degrades performance.

UUID v7 embeds a **Unix millisecond timestamp** in the first 48 bits, making new UUIDs
**monotonically increasing** in time order. This means new rows are always appended to the
rightmost leaf of the B-tree index, eliminating fragmentation.

| Metric | UUID v4 | UUID v7 |
|---|---|---|
| Index fragmentation | High (random inserts) | Low (sequential) |
| Write throughput | Baseline | Up to 2–3× higher at scale |
| Index size | Larger (fragmented pages) | Smaller (dense pages) |
| Read locality | Poor | Good |
| Native PG support | All versions | PG 18+ native |

### The polyfill

Since our infrastructure runs PostgreSQL ≤ 17, the \`uuid_generate_v7()\` function
is installed as a polyfill in the \`extensions\` schema:

\`\`\`sql
-- Installed automatically by 00000001_provision_db.sql
-- Function: extensions.uuid_generate_v7()
-- Requires: pgcrypto (extensions.gen_random_bytes)
\`\`\`

The function embeds a 48-bit millisecond timestamp + 74 random bits, then sets
version (0111) and variant (10) bits per RFC 9562.

### How to use in Atlas HCL

\`\`\`hcl
-- All PRIMARY KEY columns should use this:
column "id" {
  type    = uuid
  null    = false
  default = sql("extensions.uuid_generate_v7()")
}
\`\`\`

### How to use in raw SQL

\`\`\`sql
-- Column definition (DDL)
user_id uuid NOT NULL DEFAULT extensions.uuid_generate_v7()

-- Or use the short form (search_path includes extensions):
user_id uuid NOT NULL DEFAULT uuid_generate_v7()

-- Generate a UUID directly
SELECT extensions.uuid_generate_v7();
-- → 019dbe15-5e49-7ca4-a1c9-b62ca0395b02
--   ↑↑↑↑↑↑↑↑↑↑↑↑   time component (sortable!)
\`\`\`

### Sorting by creation time

Because UUID v7 encodes time, you can sort by ID to get chronological order:

\`\`\`sql
-- Equivalent to ORDER BY created_at, but uses the index on id:
SELECT * FROM silver.sessions ORDER BY id ASC LIMIT 100;

-- Extract the timestamp from a UUID v7:
SELECT
  id,
  to_timestamp(
    ('x' || lpad(substr(id::text, 1, 8), 16, '0'))::bit(64)::bigint::float / 1000
  ) AS uuid_timestamp
FROM silver.sessions
LIMIT 5;
\`\`\`

---

## 7. Extension Usage Guide

All extensions are installed in the \`extensions\` schema. With \`search_path\` configured,
most functions can be called without schema prefix.

### pgcrypto — Cryptographic functions

\`\`\`sql
-- Hash a password (bcrypt)
SELECT crypt('my_password', gen_salt('bf', 10));

-- Verify a password
SELECT (crypt('my_password', stored_hash) = stored_hash) AS is_valid;

-- Generate random bytes
SELECT encode(gen_random_bytes(16), 'hex');   -- 32-char hex string

-- Symmetric encryption
SELECT pgp_sym_encrypt('sensitive data', 'encryption_key');
SELECT pgp_sym_decrypt(encrypted_col, 'encryption_key');
\`\`\`

Use case: storing hashed passwords, encrypting PII columns at rest.

### pg_trgm — Trigram text search

\`\`\`sql
-- Create a GIN index for fast similarity search
CREATE INDEX idx_products_name_trgm
  ON silver.products USING GIN (name gin_trgm_ops);

-- Find similar names (fuzzy match)
SELECT name, similarity(name, 'produk makan')
FROM silver.products
WHERE similarity(name, 'produk makan') > 0.3
ORDER BY similarity DESC;

-- ILIKE with index acceleration (no % prefix needed)
SELECT * FROM silver.products WHERE name ILIKE '%makan%';
\`\`\`

Use case: search autocomplete, fuzzy product/name matching, typo tolerance.

### dblink — Cross-database queries

\`\`\`sql
-- Query another database on the same server
SELECT * FROM dblink(
  'dbname=other_product user=svc_reader password=xxx host=localhost',
  'SELECT id, name FROM silver.customers'
) AS t(id uuid, name text);
\`\`\`

Use case: joining data across data products without ETL pipeline.

### postgres_fdw — Foreign Data Wrapper

\`\`\`sql
-- Set up connection to external PostgreSQL server
CREATE SERVER external_crm
  FOREIGN DATA WRAPPER postgres_fdw
  OPTIONS (host 'crm-db.internal', dbname 'crm_cust360');

CREATE USER MAPPING FOR ${ROLE_READWRITE}
  SERVER external_crm
  OPTIONS (user 'svc_reader', password 'xxx');

-- Map a foreign table
CREATE FOREIGN TABLE bronze.crm_customers_fdw (
  id uuid,
  name text,
  email text
)
SERVER external_crm
OPTIONS (schema_name 'silver', table_name 'customers');

-- Query it like a local table
SELECT * FROM bronze.crm_customers_fdw LIMIT 10;
\`\`\`

Use case: read from upstream data products without data movement.

### uuid-ossp — UUID generation (legacy)

\`\`\`sql
-- UUID v4 (random) — use uuid_generate_v7() instead for PKs
SELECT uuid_generate_v4();

-- UUID v5 (namespace-based, deterministic)
SELECT uuid_generate_v5(uuid_ns_dns(), 'example.com');
\`\`\`

Use case: deterministic UUIDs for seeding/testing; backward compat only.

### pg_stat_statements — Query performance

> ⚠ Requires \`shared_preload_libraries = 'pg_stat_statements'\` in \`postgresql.conf\`

\`\`\`sql
-- Top 10 slowest queries by total time
SELECT query, calls, total_exec_time::int, mean_exec_time::int,
       rows, stddev_exec_time::int
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;

-- Queries with high row estimates vs actuals (bad plans)
SELECT query, calls, rows, rows/calls AS avg_rows
FROM pg_stat_statements
WHERE calls > 100
ORDER BY avg_rows DESC
LIMIT 10;

-- Reset stats
SELECT pg_stat_statements_reset();
\`\`\`

Use case: identifying slow queries, understanding query patterns, performance tuning.

---

## 8. Role & Access Management

### The 4-role design

| Role | Used by | Can do |
|---|---|---|
| \`${ROLE_OWNER}\` | Atlas CLI, CI/CD, DBA | Everything including DDL |
| \`${ROLE_READONLY}\` | Analysts, BI tools, dashboards, catalog crawlers | CONNECT + USAGE + SELECT |
| \`${ROLE_READWRITE}\` | Developers, dbt (write mode) | SELECT/INSERT/UPDATE/DELETE + CREATE TABLE in sandbox |
| \`${ROLE_OPS}\` | Airbyte, Fivetran, dbt, backend APIs | Write to bronze/silver, read gold, append to audit |

### Creating a login user and assigning to a role

\`\`\`sql
-- Step 1: Create login user (run as superuser)
CREATE USER analyst_jane LOGIN PASSWORD 'secure_password_here';

-- Step 2: Add to user-role-mapping.yaml under 'readonly' role,
--         then run: make apply-grants
\`\`\`

Or directly via SQL (bypasses the config file):

\`\`\`sql
GRANT ${ROLE_READONLY} TO analyst_jane;
\`\`\`

### Checking who has access

\`\`\`sql
-- Who is in each role?
SELECT r.rolname AS role, m.rolname AS member
FROM pg_auth_members am
JOIN pg_roles r ON r.oid = am.roleid
JOIN pg_roles m ON m.oid = am.member
WHERE r.rolname LIKE '${DB_NAME}%'
ORDER BY r.rolname, m.rolname;

-- What can a specific user do?
SELECT table_schema, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE grantee = 'analyst_jane'
ORDER BY table_schema, table_name;
\`\`\`

### Revoking access

\`\`\`sql
-- Remove user from role
REVOKE ${ROLE_READONLY} FROM analyst_jane;

-- Remove all access and drop user
REVOKE ALL PRIVILEGES ON DATABASE ${DB_NAME} FROM analyst_jane;
DROP USER analyst_jane;
\`\`\`

---

## 9. Environment Management

### Three environments

\`\`\`
local   → your machine                (DATABASE_URL)
staging → shared test environment     (STAGING_DATABASE_URL)
prod    → production                  (PROD_DATABASE_URL)
\`\`\`

Switch environment with \`ENV=\`:

\`\`\`bash
make status                  # local (default)
make status ENV=staging      # staging
make apply  ENV=prod         # apply to production
\`\`\`

### Setting up staging/production URLs

Add to CI/CD secrets (GitHub Actions, Jenkins, etc.):

\`\`\`bash
STAGING_DATABASE_URL=postgres://user:pass@staging-host:5432/${DB_NAME}?sslmode=require
PROD_DATABASE_URL=postgres://user:pass@prod-host:5432/${DB_NAME}?sslmode=require
\`\`\`

For local testing of staging:

\`\`\`bash
# Add to .env (gitignored)
STAGING_DATABASE_URL=postgres://user:pass@staging-host:5432/${DB_NAME}
\`\`\`

### direnv tips

\`\`\`bash
direnv allow      # allow .envrc after first clone or after editing .envrc
direnv deny       # unload the environment
direnv status     # show what's loaded
\`\`\`

---

## 10. Makefile Quick Reference

Run \`make help\` to see all commands. Full reference:

### Atlas commands

| Command | Description | When to use |
|---|---|---|
| \`make diff\` | Generate migration from schema changes | After editing \`schema/tables.pg.hcl\` |
| \`make diff ENV=staging\` | Generate diff against staging | Before deploying to staging |
| \`make apply\` | Apply pending migrations to local DB | After reviewing migration files |
| \`make apply ENV=prod\` | Apply to production | After staging is verified |
| \`make status\` | Show applied/pending migration count | Check before committing |
| \`make inspect\` | Show current DB schema as HCL | Debug schema drift |
| \`make lint\` | Lint latest migration file | Before every commit |
| \`make validate\` | Validate HCL schema files | After editing HCL |
| \`make hash\` | Rehash \`atlas.sum\` | After manually editing migration files |
| \`make erd\` | Open ERD visualization in browser | Visual schema review |
| \`make push\` | Push migration dir to Atlas Cloud | For Atlas Cloud CI/CD |

### Provisioning commands

| Command | Description | When to use |
|---|---|---|
| \`make apply-grants\` | Apply \`config/user-role-mapping.yaml\` | After adding users to YAML |
| \`make apply-grants-dry\` | Preview GRANTs without executing | Before \`apply-grants\` |
| \`make verify-roles\` | Show roles, schemas, extensions, grants | After provisioning |

---

## 11. Multi-Environment Deployment

### Recommended deployment flow

\`\`\`
Developer:  make diff → review SQL → make lint → git commit
                ↓
CI (PR):    atlas migrate lint --env staging --latest 1
            atlas migrate status --env staging
                ↓
Merge to develop:
            atlas migrate apply --env staging
                ↓
QA/UAT on staging environment
                ↓
Merge to main:
            atlas migrate apply --env prod
\`\`\`

### GitHub Actions example

\`\`\`yaml
# .github/workflows/migrate.yml
name: Database Migrations

on:
  push:
    branches: [main, develop]
    paths: ['migrations/**', 'schema/**']

jobs:
  migrate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: ariga/setup-atlas@v0
        with:
          cloud-token: \${{ secrets.ATLAS_CLOUD_TOKEN }}

      - name: Apply to staging
        if: github.ref == 'refs/heads/develop'
        run: atlas migrate apply --env staging
        env:
          STAGING_DATABASE_URL: \${{ secrets.STAGING_DATABASE_URL }}
          DEV_DATABASE_URL: docker://postgres/16/dev?search_path=public

      - name: Apply to production
        if: github.ref == 'refs/heads/main'
        run: atlas migrate apply --env prod
        env:
          PROD_DATABASE_URL: \${{ secrets.PROD_DATABASE_URL }}
          DEV_DATABASE_URL: docker://postgres/16/dev?search_path=public
\`\`\`

---

## 12. Troubleshooting

### \`direnv: error .envrc is blocked\`

\`\`\`bash
direnv allow
\`\`\`

### \`Error: missing environment variable "DATABASE_URL"\`

\`\`\`bash
# Check if direnv is loaded
echo \$DATABASE_URL

# If empty:
cat .env          # verify file exists and has values
direnv allow      # re-allow after .env change
\`\`\`

### \`atlas migrate apply\` fails: \`role does not exist\`

The provision migration runs as \`postgres\` superuser. Ensure you're connecting as superuser:
\`\`\`bash
# Check who you're connecting as
psql \$DATABASE_URL -c "SELECT current_user;"

# If not superuser, update .env:
PG_USER=postgres
\`\`\`

### \`ERROR: could not find a "pg_stat_statements" in the extensions schema\`

This extension requires pre-loading. Add to \`postgresql.conf\`:
\`\`\`
shared_preload_libraries = 'pg_stat_statements'
\`\`\`
Restart PostgreSQL, then uncomment in \`migrations/00000001_provision_db.sql\` and re-run.

For managed databases (RDS, Huawei Cloud DCS), enable via parameter group, not postgresql.conf.

### \`ERROR: function uuid_generate_v7() does not exist\`

The polyfill wasn't applied. Run:
\`\`\`bash
atlas migrate status --env local    # check if 00000001 was applied
atlas migrate apply --env local     # apply if pending
\`\`\`

If it shows as applied but function doesn't exist, rerun the provision SQL directly:
\`\`\`bash
psql \$DATABASE_URL -f migrations/00000001_provision_db.sql
\`\`\`

### \`atlas migrate diff\` produces no changes but I edited HCL

\`\`\`bash
make validate    # check HCL is valid
make inspect     # compare what Atlas sees vs your HCL
\`\`\`

If inspect shows the schema matches your HCL, there's nothing to diff — the DB is already in sync.

### \`atlas.sum: checksum mismatch\`

Occurs when migration files are edited manually after being hashed:
\`\`\`bash
make hash        # regenerate atlas.sum
\`\`\`

> Only do this if you intentionally edited a migration. Changing applied migrations is destructive.

### \`GRANT ... TO user\` fails: \`role does not exist\`

The login user must be created first:
\`\`\`sql
CREATE USER username LOGIN PASSWORD 'secure_password';
\`\`\`
Then re-run \`make apply-grants\`.

### \`permission denied for schema silver\`

The connection user is not a member of any provisioned role.
Check role membership:
\`\`\`sql
SELECT r.rolname, m.rolname
FROM pg_auth_members am
JOIN pg_roles r ON r.oid=am.roleid
JOIN pg_roles m ON m.oid=am.member
WHERE m.rolname = 'your_username';
\`\`\`

If empty, run \`make apply-grants\` after adding the user to \`config/user-role-mapping.yaml\`.

---

## 13. CI/CD Integration

### Environment variables required per environment

| Variable | local | staging | prod |
|---|---|---|---|
| \`DATABASE_URL\` | From \`.env\` | CI secret | CI secret |
| \`STAGING_DATABASE_URL\` | Optional in \`.env\` | CI secret | — |
| \`PROD_DATABASE_URL\` | — | — | CI secret |
| \`DEV_DATABASE_URL\` | \`docker://postgres/16/dev\` | same | same |
| \`ATLAS_TOKEN\` | Optional | CI secret (Atlas Cloud) | CI secret |

### Jenkins pipeline snippet

\`\`\`groovy
stage('Database Migration — Staging') {
  when { branch 'develop' }
  environment {
    STAGING_DATABASE_URL = credentials('staging-db-url')
    DEV_DATABASE_URL     = 'docker://postgres/16/dev?search_path=public'
  }
  steps {
    sh 'atlas migrate lint --env staging --latest 1'
    sh 'atlas migrate apply --env staging'
  }
}
\`\`\`

### Pre-commit hook (optional)

Add to \`.git/hooks/pre-commit\`:
\`\`\`bash
#!/bin/bash
# Lint latest migration before commit
if git diff --cached --name-only | grep -q 'migrations/'; then
  atlas migrate lint --env local --latest 1 || exit 1
fi
\`\`\`

---

*Generated by [data-mesh-db-boilerplate](https://github.com/your-org) | Domain: ${DOMAIN} | Product: ${PRODUCT}*
EOF
success "docs/DEVELOPER_GUIDE.md"
echo ""
echo "  DB Name : ${DB_NAME}"
echo "  Target  : ${TARGET_DIR}"
echo ""
warn "pg_stat_statements: uncomment CREATE EXTENSION setelah shared_preload_libraries config"
echo ""
echo -e "${BOLD}Next steps:${RESET}"
echo "  1. nano .env                              ← set PG_PASSWORD"
echo "  2. direnv allow"
echo "  3. psql -U ${PG_USER} -c \"CREATE DATABASE ${DB_NAME};\""
echo "  4. atlas migrate hash --env local"
echo "  5. atlas migrate apply --env local"
echo "  6. make verify-roles"
echo "  7. nano config/user-role-mapping.yaml     ← add users"
echo "  8. make apply-grants"
echo "  9. make diff && make apply                ← schema design"
