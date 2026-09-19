---
name: data-mesh-db-boilerplate
description: >
  Bootstrap a production-ready PostgreSQL database repo using Atlas (atlasgo.io) for
  Data Mesh data products. Generates: atlas.hcl (local/staging/prod), 6 schemas
  (sandbox/extensions/bronze/silver/gold/audit), 4 roles (owner/readonly/readwrite/ops)
  with per-schema grants + DEFAULT PRIVILEGES, 6 extensions (pgcrypto/pg_trgm/
  pg_stat_statements/dblink/postgres_fdw/uuid-ossp), UUID v7 polyfill for PG<18,
  search_path, user-role mapping YAML, direnv .envrc, Makefile, and
  docs/DEVELOPER_GUIDE.md. DB naming: {DOMAIN}_{PRODUCT} lowercase, hyphens to
  underscores. Trigger for: bootstrap db, scaffold database, set up atlas, create
  atlas project, init db for data product, atlas postgres, atlas migrations, atlas
  schema, direnv atlas, db boilerplate, provision roles, create db roles, medallion
  schema, bronze silver gold, setup extensions, uuid v7 polyfill, or any
  atlas+postgres+data-mesh combination. Also trigger to scaffold a database layer
  for any data mesh domain or data product.
compatibility: >
  Claude Code (bash_tool, create_file, present_files required).
  Consults /data-mesh-architect for naming conventions and domain standards.
  Requires: Atlas CLI (atlasgo.io), direnv, Docker (for dev database), Python 3.8+ with PyYAML.
---

# Data Mesh DB Boilerplate Skill

Bootstrap sebuah **PostgreSQL database repository** yang production-ready menggunakan
**Atlas** (atlasgo.io) sebagai schema migration tool, dengan konvensi naming Data Mesh,
**6 standard schemas** (medallion architecture), **4 provisioned roles** dengan per-schema
grants, **6 default extensions**, dan **direnv** untuk environment management.

---

## Quick Reference

| Kebutuhan | File |
|---|---|
| Atlas HCL patterns & env var handling | `references/atlas-patterns.md` |
| Atlas security: roles & grants | `references/atlas-security.md` |
| Data Mesh naming conventions | `references/data-mesh-naming.md` |
| Bootstrap script (generate semua file) | `scripts/bootstrap.sh` |
| Apply user grants script | `scripts/apply-user-grants.py` |
| Starter table HCL template | `assets/schema.pg.hcl.template` |
| Provision SQL template | `assets/provision_db.sql.template` |
| User-role mapping YAML template | `assets/user-role-mapping.yaml.template` |
| Extensions config YAML template | `assets/extensions.yaml.template` |

---

## Alur Kerja

### LANGKAH 1 — Kumpulkan Context

Tanyakan jika belum ada di context:

| Parameter | Contoh | Keterangan |
|---|---|---|
| `DOMAIN_SHORTCODE` | `APM`, `crm`, `fin` | Singkatan domain bisnis |
| `DATA_PRODUCT_SHORTCODE` | `funnel-aktivitas-user`, `cust360` | Singkatan data product (boleh pakai hyphens) |
| `TARGET_DIR` | `.` atau `./db` | Target directory di repo user |
| `PG_PORT` | `5432` | Port PostgreSQL lokal (default: 5432) |
| `PG_USER` | `postgres` | PostgreSQL superuser |

---

### LANGKAH 2 — Derive DB Name dan Role Names

```bash
# Normalisasi: lowercase + hyphens → underscores
DB_NAME = lower({DOMAIN_SHORTCODE}) + "_" + lower({DATA_PRODUCT_SHORTCODE}).replace("-", "_")

# Contoh:
# APM + funnel-aktivitas-user  →  apm_funnel_aktivitas_user
# CRM + cust-360               →  crm_cust_360
# FIN + txn-ledger             →  fin_txn_ledger

# 4 Roles (derived dari DB_NAME):
ROLE_OWNER     = {DB_NAME}
ROLE_READONLY  = {DB_NAME}_readonly
ROLE_READWRITE = {DB_NAME}_readwrite
ROLE_OPS       = {DB_NAME}_ops
```

Tampilkan ke user untuk konfirmasi sebelum generate.

---

### LANGKAH 3 — Baca References

Baca sebelum generate file apapun:
1. `references/atlas-patterns.md` — atlas.hcl syntax, `getenv()`, fileset, lint config
2. `references/atlas-security.md` — role blocks, grants, DEFAULT PRIVILEGES
3. `references/data-mesh-naming.md` — naming rules lengkap

---

### LANGKAH 4 — Generate Repo Structure

```
{TARGET_DIR}/
├── .envrc                              ← direnv: load .env ke shell
├── .env                                ← secrets (gitignored!)
├── .env.example                        ← template .env untuk Git
├── .gitignore
├── Makefile
├── atlas.hcl                           ← Atlas project config
│
├── config/
│   ├── user-role-mapping.yaml          ← ★ ISI INI: map login users → roles
│   └── extensions.yaml                 ← extensions config
│
├── schema/
│   ├── schemas.pg.hcl                  ← 6 schema declarations
│   └── tables.pg.hcl                   ← starter tables (edit per data product)
│
├── migrations/
│   ├── 00000001_provision_db.sql       ← roles, grants, extensions, uuid_generate_v7, search_path
│   └── atlas.sum                       ← generated: atlas migrate hash --env local
│
├── scripts/
│   ├── apply-user-grants.py            ← apply config/user-role-mapping.yaml
│   └── verify-roles.sh                 ← verify role setup
│
├── docs/
│   └── DEVELOPER_GUIDE.md             ← ★ comprehensive dev reference (13 sections)
│
└── README.md
```

**Urutan generate wajib diikuti:**
1. `.gitignore` → `.env.example` → `.env` → `.envrc`
2. `atlas.hcl`
3. `config/user-role-mapping.yaml` + `config/extensions.yaml`
4. `schema/schemas.pg.hcl` + `schema/tables.pg.hcl`
5. `migrations/00000001_provision_db.sql`
6. `scripts/apply-user-grants.py` + `scripts/verify-roles.sh`
7. `Makefile` → `README.md`
8. **Terakhir:** jalankan `atlas migrate hash --env local` → generate `migrations/atlas.sum`

---

### LANGKAH 5 — File Contents Specification

#### `.gitignore`
```
.env
*.env.local
.direnv/
__pycache__/
*.pyc
```

#### `.env.example`
```bash
# {DB_NAME} — Atlas Database Configuration
# cp .env.example .env && nano .env (isi PG_PASSWORD)
# JANGAN commit .env ke Git!

DB_NAME={DB_NAME}

PG_HOST=localhost
PG_PORT={PG_PORT}
PG_USER={PG_USER}
PG_PASSWORD=changeme

# Constructed URLs — dikonstruksi dari variabel di atas
# search_path disertakan di URL agar semua tools otomatis set schema
DATABASE_URL=postgres://${PG_USER}:${PG_PASSWORD}@${PG_HOST}:${PG_PORT}/${DB_NAME}?search_path=public,extensions,audit,gold,silver,bronze,sandbox&sslmode=disable
DEV_DATABASE_URL=docker://postgres/16/dev?search_path=public

# Staging & Production (isi via CI/CD secrets)
# STAGING_DATABASE_URL=postgres://...
# PROD_DATABASE_URL=postgres://...

# Atlas Cloud (optional)
# ATLAS_TOKEN=your_atlas_token
```

#### `.envrc`
```bash
# .envrc — direnv configuration for {DB_NAME}
# Jalankan: direnv allow
# Docs: https://direnv.net

# Load .env file
if [ -f .env ]; then
  dotenv .env
fi

# Atlas default environment
export ATLAS_ENV=local

echo "✓ direnv: ${DB_NAME} loaded"
echo "  HOST=${PG_HOST}:${PG_PORT} | DB=${DB_NAME} | USER=${PG_USER}"
```

#### `atlas.hcl`
```hcl
# atlas.hcl — Atlas Project Configuration
# Data Product : {DOMAIN_SHORTCODE}/{DATA_PRODUCT_SHORTCODE}
# DB           : {DB_NAME}
# Schemas      : sandbox, extensions, bronze, silver, gold, audit
#
# Prereq: direnv allow (loads .env)
# Ref: https://atlasgo.io/atlas-schema/projects

# Load all .pg.hcl files from schema/ directory
data "hcl_schema" "app" {
  paths = fileset("schema/**/*.pg.hcl")
}

# ── Local Development ──────────────────────────────────────────────
env "local" {
  url = getenv("DATABASE_URL")
  dev = "docker://postgres/16/dev?search_path=public"
  src = data.hcl_schema.app.url

  migration {
    dir = "file://migrations"
  }

  lint {
    destructive {
      error = false  # Warn only in local
    }
  }
}

# ── Staging ────────────────────────────────────────────────────────
env "staging" {
  url = getenv("STAGING_DATABASE_URL")
  dev = "docker://postgres/16/dev?search_path=public"
  src = data.hcl_schema.app.url

  migration {
    dir = "file://migrations"
  }

  lint {
    destructive {
      error = true
    }
  }
}

# ── Production ─────────────────────────────────────────────────────
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
      error = true
    }
  }
}
```

#### `schema/schemas.pg.hcl`
```hcl
# schemas.pg.hcl — 6 standard schemas untuk {DB_NAME}
# Roles dan grants dikelola di migrations/00000001_provision_db.sql

schema "sandbox" {
  comment = "Exploration area — readwrite + ops dapat CREATE TABLE di sini"
}

schema "extensions" {
  comment = "PostgreSQL extensions — diinstall di sini, bukan di public"
}

schema "bronze" {
  comment = "Raw ingestion layer — source-aligned, append-only. ops dapat CREATE TABLE"
}

schema "silver" {
  comment = "Cleaned + validated data — conformance layer. DML oleh readwrite + ops"
}

schema "gold" {
  comment = "Curated aggregations + serving layer — read-heavy. ops: read-only"
}

schema "audit" {
  comment = "Immutable audit + lineage logs — append-only. Tidak ada UPDATE/DELETE"
}
```

#### `schema/tables.pg.hcl`
Baca `assets/schema.pg.hcl.template` untuk starter table dengan Data Mesh standard columns.
Tempatkan tables di schema yang tepat (bukan `public`):

| Data Type | Schema Target |
|---|---|
| Raw/landing data dari source | `bronze` |
| Cleaned/conformed data | `silver` |
| Aggregated/KPI/serving | `gold` |
| Audit logs, change history | `audit` |
| Exploration/temp tables | `sandbox` |

#### `config/user-role-mapping.yaml`
Baca `assets/user-role-mapping.yaml.template`.

```yaml
# user-role-mapping.yaml
# Map login users/roles → provisioned group roles
# Run: make apply-grants  →  scripts/apply-user-grants.py
# CATATAN: Login users harus sudah dibuat di PostgreSQL terlebih dahulu.
#          Script ini hanya melakukan GRANT, bukan CREATE USER.

db_name: {DB_NAME}

roles:
  owner:
    role: {DB_NAME}
    comment: "DB owner — full privileges on all schemas"
    members: []
    # Uncomment dan isi:
    # - username: svc_owner
    #   comment: "Owner service account"

  readonly:
    role: {DB_NAME}_readonly
    comment: "Read-only: CONNECT + USAGE + SELECT on all schemas"
    members: []
    # - username: analyst_jane
    #   comment: "Data analyst"
    # - username: svc_bi_tool
    #   comment: "Metabase service account"

  readwrite:
    role: {DB_NAME}_readwrite
    comment: "Read-write DML (no DROP/TRUNCATE). CREATE TABLE in sandbox only."
    members: []
    # - username: dev_john
    #   comment: "Backend developer"

  ops:
    role: {DB_NAME}_ops
    comment: "Ops role: pipelines, ETL, external apps. CREATE TABLE in bronze + sandbox."
    members: []
    # - username: svc_airbyte
    #   comment: "Airbyte ingestion pipeline"
    # - username: svc_dbt
    #   comment: "dbt transformation service"
```

#### `config/extensions.yaml`
```yaml
# extensions.yaml — PostgreSQL extensions untuk {DB_NAME}
# Schema target: extensions (semua ext diinstall di sini, bukan public)
# Run: make install-extensions
#
# ⚠  pg_stat_statements membutuhkan:
#    shared_preload_libraries = 'pg_stat_statements' di postgresql.conf
#    Restart PostgreSQL setelah konfigurasi ini.

schema: extensions

extensions:
  - name: pgcrypto
    comment: "Cryptographic functions — gen_random_bytes, crypt, pgp_sym_encrypt"
    enabled: true

  - name: pg_trgm
    comment: "Trigram similarity — fuzzy search, accelerate LIKE/ILIKE queries"
    enabled: true

  - name: pg_stat_statements
    comment: "Query performance tracking. REQUIRES: shared_preload_libraries config"
    enabled: true
    schema_override: pg_catalog  # MUST be in pg_catalog, not extensions schema

  - name: dblink
    comment: "Cross-database queries within same PostgreSQL server"
    enabled: true

  - name: postgres_fdw
    comment: "Foreign Data Wrapper — query external PostgreSQL servers"
    enabled: true

  - name: uuid-ossp
    comment: "UUID generation functions (uuid_generate_v4). PG13+ sudah ada gen_random_uuid() built-in"
    enabled: true
```

#### `migrations/00000001_provision_db.sql`
Baca `assets/provision_db.sql.template` untuk SQL lengkap.
File ini berisi semua provisioning:
- `CREATE ROLE` (4 roles)
- `CREATE SCHEMA` (6 schemas) + `ALTER SCHEMA OWNER`
- `GRANT CONNECT` pada DB
- Per-schema GRANTs (lihat matriks di bawah)
- `ALTER DEFAULT PRIVILEGES` per schema per role
- `CREATE EXTENSION` (6 extensions)
- `ALTER DATABASE ... SET search_path`

**Setelah create file ini:** `atlas migrate hash --env local`

#### `scripts/apply-user-grants.py`
Baca `scripts/apply-user-grants.py` untuk script Python yang:
- Membaca `config/user-role-mapping.yaml`
- Untuk setiap member di setiap role: `GRANT {role} TO {username};`
- Dry-run mode: `--dry-run`
- Verbose mode: `--verbose`

#### `Makefile`
```makefile
# Makefile — {DB_NAME}
.PHONY: help diff apply status inspect lint validate push hash apply-grants verify-roles install-extensions

ENV     ?= local
DB_NAME ?= {DB_NAME}

help: ## Show commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}'

# ── Atlas commands ─────────────────────────────────────────────────
diff:         ## Generate migration from schema changes
	atlas migrate diff --env $(ENV)
apply:        ## Apply pending migrations
	atlas migrate apply --env $(ENV)
status:       ## Show migration status
	atlas migrate status --env $(ENV)
inspect:      ## Inspect current DB schema (HCL output)
	atlas schema inspect --env $(ENV)
lint:         ## Lint latest migration
	atlas migrate lint --env $(ENV) --latest 1
validate:     ## Validate schema HCL files
	atlas schema validate --env $(ENV)
push:         ## Push to Atlas Cloud
	atlas migrate push $(DB_NAME) --env $(ENV)
hash:         ## Rehash migrations after manual edits
	atlas migrate hash --env $(ENV)
erd:          ## Open ERD in browser (requires atlas login)
	atlas schema inspect --env $(ENV) -w

# ── Provisioning commands ──────────────────────────────────────────
apply-grants:      ## Apply user→role mappings from config/user-role-mapping.yaml
	python3 scripts/apply-user-grants.py --config config/user-role-mapping.yaml --url $$DATABASE_URL
apply-grants-dry:  ## Dry-run: show GRANT statements without executing
	python3 scripts/apply-user-grants.py --config config/user-role-mapping.yaml --url $$DATABASE_URL --dry-run
verify-roles:      ## Verify role setup in database
	bash scripts/verify-roles.sh
```

---

### LANGKAH 6 — Role-Schema Grant Matrix

Matriks privileges per role per schema (dibuat di provision SQL):

| Schema | `_readonly` | `_readwrite` | `_ops` |
|---|---|---|---|
| **sandbox** | USAGE, SELECT | USAGE, **CREATE**, SELECT/INSERT/UPDATE/DELETE | USAGE, **CREATE**, SELECT/INSERT/UPDATE/DELETE |
| **extensions** | USAGE | USAGE | USAGE |
| **bronze** | USAGE, SELECT | USAGE, SELECT/INSERT/UPDATE/DELETE | USAGE, **CREATE**, SELECT/INSERT/UPDATE/DELETE |
| **silver** | USAGE, SELECT | USAGE, SELECT/INSERT/UPDATE/DELETE | USAGE, SELECT/INSERT/UPDATE/DELETE |
| **gold** | USAGE, SELECT | USAGE, SELECT/INSERT/UPDATE/DELETE | USAGE, **SELECT only** |
| **audit** | USAGE, SELECT | USAGE, **SELECT only** | USAGE, SELECT/**INSERT only** |

**DEFAULT PRIVILEGES** (untuk tables dibuat di masa depan) wajib ada di provision SQL
untuk memastikan tables baru otomatis mendapat grants yang benar.

**Tidak ada role** (kecuali owner + superuser) yang mendapat:
`DROP TABLE`, `TRUNCATE`, `ALTER TABLE`, `DROP SCHEMA`, `CREATE SCHEMA`

---

### LANGKAH 7 — Post-Generate Instructions ke User

```
Setup Steps:
1. Edit .env → set PG_PASSWORD
2. direnv allow
3. psql -U {PG_USER} -c "CREATE DATABASE {DB_NAME};"
4. atlas migrate hash --env local      ← generate atlas.sum
5. atlas migrate apply --env local     ← runs 00000001_provision_db.sql
6. nano config/user-role-mapping.yaml  ← add your users
7. make apply-grants                   ← GRANT users to roles
8. make verify-roles                   ← confirm setup
9. Edit schema/tables.pg.hcl           ← design your schema
10. make diff && make apply            ← generate + apply table migrations
```

---

## Output Files yang Dihasilkan

| File | Keterangan |
|---|---|
| `.envrc` | direnv — auto-load `.env` |
| `.env` / `.env.example` | Secrets template |
| `atlas.hcl` | 3 environments (local/staging/prod) |
| `config/user-role-mapping.yaml` | **ISI INI** — user→role GRANT mapping |
| `config/extensions.yaml` | Extensions reference |
| `schema/schemas.pg.hcl` | 6 schema declarations |
| `schema/tables.pg.hcl` | Starter table (uuid_generate_v7 PK) |
| `migrations/00000001_provision_db.sql` | Roles, grants, extensions, UUID v7 polyfill, search_path |
| `scripts/apply-user-grants.py` | Apply user-role-mapping.yaml ke DB |
| `scripts/verify-roles.sh` | Inspect DB: roles, schemas, extensions, grants |
| `docs/DEVELOPER_GUIDE.md` | **★ Comprehensive developer reference** (13 sections) |
| `Makefile` | All commands |
| `README.md` | Quick start |

---

## Anti-Patterns yang Dihindari

- ❌ Hardcode DB URL di `atlas.hcl` → pakai `getenv()`
- ❌ Commit `.env` → ada di `.gitignore`
- ❌ Tables di `public` schema → gunakan `bronze/silver/gold/sandbox`
- ❌ Extensions di `public` schema → gunakan `extensions` schema
- ❌ GRANT langsung ke login user → selalu GRANT ke group role dulu, lalu user ke role
- ❌ Tanpa `ALTER DEFAULT PRIVILEGES` → tables baru tidak dapat grants otomatis
- ❌ Hard DELETE → pakai `is_deleted` soft delete
- ❌ `DROP TABLE` / `TRUNCATE` privileges ke non-owner → dilarang di semua role
- ❌ `pg_stat_statements` tanpa `shared_preload_libraries` config → extension tidak berfungsi
- ❌ `gen_random_uuid()` sebagai PK default → gunakan `extensions.uuid_generate_v7()` untuk time-ordering
- ❌ UUID v7 tanpa polyfill di PG <18 → install `extensions.uuid_generate_v7()` via provision SQL

---

## UUID v7 Polyfill — Catatan Penting

**Kenapa UUID v7?**

| | UUID v4 | UUID v7 |
|---|---|---|
| Ordering | Random | Time-ordered (monotonic) |
| Index fragmentation | Tinggi | Rendah (sequential insert) |
| Write throughput | Normal | Lebih tinggi |
| Index size | Lebih besar | Lebih kecil |
| Native support | PG semua versi | PG 18+ native |

**Polyfill location:** `extensions.uuid_generate_v7()` — diinstall di `00000001_provision_db.sql`

**Dependency:** pgcrypto (`extensions.gen_random_bytes()`) — wajib diinstall lebih dulu

**Usage di Atlas HCL:**
```hcl
column "id" {
  type    = uuid
  null    = false
  default = sql("extensions.uuid_generate_v7()")
}
```

**Usage di raw SQL:**
```sql
-- Column definition
individu_id uuid PRIMARY KEY DEFAULT extensions.uuid_generate_v7()

-- Direct call (search_path sudah include extensions)
SELECT extensions.uuid_generate_v7();
-- → 019dbe15-5e49-7ca4-a1c9-b62ca0395b02
```

**search_path order:** `public, extensions, audit, gold, silver, bronze, sandbox`
Extensions di posisi kedua agar fungsi dapat dipanggil tanpa schema prefix setelah `public`.
