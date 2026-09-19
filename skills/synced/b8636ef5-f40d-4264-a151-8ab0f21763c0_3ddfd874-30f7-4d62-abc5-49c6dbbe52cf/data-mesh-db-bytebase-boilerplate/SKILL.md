---
name: data-mesh-db-bytebase-boilerplate
description: >
  Bootstrap a PostgreSQL database repo deployed through Bytebase GitOps, run
  by Jenkins, with one long-lived git branch per environment (main=
  production, development=dev by default, overridable) instead of
  sequential promotion down a single branch. Generates: idempotent
  bootstrap/ SQL (run once per env, by hand), migrations/ for Bytebase-
  managed changes, a Multibranch Jenkinsfile, .env.example, setup docs, a
  script to import an existing remote database's schema for onboarding, and
  a script to run bytebase-action check/rollout manually without Jenkins.
  Provisions 4 LOGIN roles (owner/readonly/readwrite/ops), 7 schemas
  (sandbox/extensions/bronze/silver/gold/audit/remote) with grants +
  DEFAULT PRIVILEGES, free-for-all sandbox (scoped drop_table()),
  pg_stat_statements, search_path. Trigger for: bootstrap db, bytebase
  gitops/jenkins, provision db roles, medallion schema, sandbox schema,
  postgres_fdw, branch-per-env deployment, import/onboard existing db,
  manual bytebase rollout, test bytebase without jenkins.
compatibility: >
  Claude Code (bash_tool, create_file, present_files required).
  Requires: Docker + Jenkins agent for the generated pipeline (not needed to
  generate the repo itself), psql client, Python not required. Consults
  /data-mesh-architect for naming conventions if that skill is present.
---

# Data Mesh DB Bytebase Boilerplate Skill

Bootstrap a **PostgreSQL database repository** deployed through **Bytebase**
GitOps and **Jenkins** CI/CD, with the same role/schema conventions as this
project's Atlas-based sibling skill (`data-mesh-db-boilerplate`) — 4 roles, a
medallion-shaped schema layout — adapted for Bytebase's migration model and a
free-for-all `sandbox` schema plus a `remote` schema for `postgres_fdw`.

---

## Quick Reference

| Need | File |
|---|---|
| Generate the whole repo | `scripts/bootstrap.sh` |
| Roles/schemas/grants SQL | `assets/bootstrap_provision.sql.template` |
| Jenkins pipeline | `assets/Jenkinsfile.template` |
| One-time Bytebase console setup (copied to output) | `assets/BYTEBASE_SETUP.md.template` |
| Full grant-matrix + rationale (copied to output) | `assets/DEVELOPER_GUIDE.md.template` |
| Onboarding an existing database (copied to output) | `assets/IMPORTING_EXISTING_DATABASE.md.template` |
| Schema-snapshot script for existing databases (copied to output) | `assets/import-existing-schema.sh.template` |
| Manual check/rollout script, no Jenkins needed (copied to output) | `assets/bytebase-manual-rollout.sh.template` |
| Local disposable Bytebase for testing (copied to output) | `assets/docker-compose.bytebase.yml.template` |
| `bytebase-action` CLI flags (Claude's own reference, not copied to output) | `references/bytebase-action-flags.md` |

---

## Workflow

### Step 1 — Get the two required inputs from the user

Every invocation needs, at minimum:

| Parameter | Example | Notes |
|---|---|---|
| Database name | `ops_sample_database` | Must be snake_case. `bootstrap.sh` will lowercase and convert hyphens automatically, but confirm the normalized name with the user if it changed. |
| Target directory | `.` or `./db` | Where the repo gets generated. |

Ask for these if not already given in the conversation — don't guess a
database name, since it becomes 4 role names and a Postgres database that
will exist in real environments.

Optional, with sensible defaults — mention them but don't block on asking:

| Parameter | Default | Notes |
|---|---|---|
| Environments | `dev,production` | Comma-separated, any number, any names — this is the "two environments by default, overridable" requirement. Names must match exactly what gets created in Bytebase's **Settings → Environments** later. |
| Branch map | `dev=development,production=main` | Each environment deploys from exactly one long-lived git branch — **not** sequential promotion down a single branch. `dev`→`development` and `production`→`main` are the defaults for those exact environment names; anything else defaults to a branch named the same as the environment. Override with `--branch-map env=branch,env=branch`. This is the "separate environment by git branches" requirement — confirm the mapping with the user if their environment names don't match the defaults. |
| PostgreSQL host/port | `localhost` / `5432` | Per-environment host/port also live in the generated `.env.example` and can be edited by hand afterward — these flags just seed the template. |
| Bytebase version | `3.14.0` | Self-hosted only. Must match the actual Bytebase server version the team runs, or `bytebase-action`'s version check will fail — ask if unsure rather than assuming this default is right for them. |
| Postgres superuser | `postgres` | Used only in generated comments/scripts for the manual bootstrap step. |
| Git init | on by default | The generator runs `git init`, commits, and creates one branch per distinct value in the branch map, all pointing at the same initial commit. It detects an existing git working tree and skips automatically rather than nesting a repo — pass `--no-git-init` to opt out explicitly instead. |

### Step 2 — Read the SQL template before generating

Before running the generator, skim
`assets/bootstrap_provision.sql.template` and `references/bytebase-action-flags.md`
if you haven't already this session — the grant matrix and the
versioned-mode filename rules are easy to get subtly wrong from memory, and
this skill's whole value is getting them right by default.

### Step 3 — Run the generator

```bash
bash scripts/bootstrap.sh \
  --db-name ops_sample_database \
  --environments dev,production \
  --branch-map dev=development,production=main \
  --dir ./ops-sample-database \
  --bytebase-version 3.14.0
```

This produces the full repo (see layout below) in one shot, including an
initialized git repo with a `development` and a `main` branch (or whatever
`--branch-map` resolves to). It is safe to re-run — every generated SQL
statement is idempotent, and `.env` is never overwritten if it already
exists.

### Step 4 — Explain the two-phase model to the user

This is the part people most often get wrong with Bytebase, so say it
explicitly rather than assuming it's obvious:

1. **Phase 0 (`bootstrap/`)** — runs manually, once per environment, via
   `scripts/run-bootstrap.sh`, as a Postgres superuser, **before** that
   environment's database is registered in Bytebase. It creates the very
   role Bytebase will later connect as, so nothing else can run it first.
2. **Phase 1 (`migrations/`)** — everything after that point is Bytebase's
   job, driven by the Jenkinsfile on every PR/merge.

Point the user at `docs/BYTEBASE_SETUP.md` for the one-time console setup
(environments, instance connections, project, service account, SQL Review
policy) — this part genuinely cannot be scripted from the repo since it's
Bytebase-side state, and the generated docs walk through it in full.

### Step 5 — Fill in the placeholders the generator can't know

The generator cannot know real Bytebase resource names (they don't exist
until the user completes `docs/BYTEBASE_SETUP.md`). After generation, the
Jenkinsfile has clearly marked `TODO` comments for `BYTEBASE_URL`,
`BYTEBASE_PROJECT`, and each environment's `instances/.../databases/...`
target. If the user already knows these values, fill them in during
generation instead of leaving placeholders — ask if it's unclear whether
they've set up Bytebase yet.

### Step 6 — If the environment already has a real database in it

Ask this explicitly rather than assuming a fresh database — it changes the
onboarding path. If the user says an environment already has real tables
(not just an empty database bootstrap created):

1. Still run `scripts/run-bootstrap.sh` for that environment first — it
   only touches roles/schemas/extensions/grants and is idempotent, so it's
   safe even against a database with existing tables.
2. Run `scripts/import-existing-schema.sh --env <name>` to snapshot the
   current schema via `pg_dump` into `bootstrap/imported/`. This is
   informational — it does **not** get fed to `bytebase-action`, and does
   **not** get copied into `migrations/`. Explain why if asked: Bytebase's
   revision history (which versions it's already applied) lives inside
   Bytebase, not git, so a database it's never registered has no applied
   history regardless of what tables physically exist — replaying
   `CREATE TABLE` for things that already exist would fail.
3. Point the user at `docs/IMPORTING_EXISTING_DATABASE.md` for the
   reconciliation step (Bytebase's own Sync Schema / Establish Baseline
   action) — this, like the rest of Bytebase's own state, can't be
   scripted from the repo.
4. Only after the baseline is established should new changes go in
   `migrations/`.

### Step 7 — Local testing without Jenkins

Two generated pieces cover this — mention both when the user wants to test
before wiring up CI, or is debugging why a rollout isn't behaving as
expected:

- `docker-compose.bytebase.yml` — a disposable local Bytebase instance
  (`docker compose -f docker-compose.bytebase.yml up -d`), useful when the
  user doesn't want to experiment against a shared server yet.
- `scripts/bytebase-manual-rollout.sh --env <name> --check` (safe, read-only)
  or `--rollout` (asks for confirmation, actually deploys) — runs the exact
  same `bytebase-action` Docker commands the Jenkinsfile runs, using the
  same env→target mapping generated alongside it. This is a faithful local
  reproduction, not a parallel mechanism that could drift from the
  Jenkinsfile — if the user changes the target mapping, regenerate the repo
  rather than hand-editing one file and not the other.

---

## Repository layout produced

```
{TARGET_DIR}/                          # git repo, one branch per environment
├── .env.example                     # per-environment PG + Bytebase config
├── .env                             # gitignored, seeded from .env.example
├── .gitignore
├── Jenkinsfile                      # Multibranch: check (every branch) → rollout (mapped branches only)
├── docker-compose.bytebase.yml      # disposable local Bytebase for testing
├── bootstrap/
│   ├── 001_provision_{db_name}.sql  # Phase 0 — roles, schemas, grants, extensions (manual, once/env)
│   └── imported/                    # schema snapshots from import-existing-schema.sh (informational)
├── migrations/
│   └── .gitkeep                     # Phase 1 — Bytebase-managed from here on
├── scripts/
│   ├── run-bootstrap.sh             # applies bootstrap/ safely (passwords from .env, not argv)
│   ├── verify-roles.sh              # post-provisioning sanity check
│   ├── import-existing-schema.sh    # snapshot an already-existing database's schema
│   └── bytebase-manual-rollout.sh   # run check/rollout by hand, no Jenkins needed
├── docs/
│   ├── BYTEBASE_SETUP.md            # one-time console + Multibranch Pipeline job setup
│   ├── DEVELOPER_GUIDE.md           # grant matrix, search_path, anti-patterns
│   └── IMPORTING_EXISTING_DATABASE.md  # onboarding a database that already has tables
└── README.md
```

Branches (default `development` and `main`) all point at the same initial
commit right after generation — they diverge as the user works normally
from there. Promotion between environments is a git merge (e.g.
`development` → `main`), not a sequential Jenkins pipeline stage.

---

## Role & schema design (why, not just what)

- **4 roles, all `LOGIN NOINHERIT`**: `{db_name}` (owner — the credential
  Bytebase itself authenticates with to run DDL), `_readonly`, `_readwrite`,
  `_ops`. Unlike a NOLOGIN-group-role + individual-user-mapping design,
  these are meant to back shared service/tool connections directly. This
  was a deliberate choice for this skill (confirmed with the user) because
  Bytebase's instance connection needs one concrete login credential with
  DDL rights — that's the owner role.
- **7 schemas**: `bronze`, `silver`, `gold`, `audit` (read-only except
  `_ops` insert-only), `sandbox` (free-for-all — see below), `extensions`
  (every extension lives here, never in `public`), `remote` (`postgres_fdw`
  foreign tables).
- **`sandbox` is a deliberate, documented exception.** The user asked for
  all three non-owner roles to be able to create *and drop* tables there
  freely. Plain PostgreSQL grants can cover CREATE/SELECT/INSERT/UPDATE/
  DELETE/TRUNCATE, but there is no grantable `DROP TABLE` privilege for
  non-owners — only the owner or a superuser can drop a table. Rather than
  widen `DROP` database-wide (which would defeat the entire point of the
  other 6 schemas being locked down), the template installs one
  `SECURITY DEFINER` function, `sandbox.drop_table(name)`, scoped to that
  schema only, `EXECUTE`-granted to all three roles. Explain this to the
  user rather than silently picking one approach — it's the kind of design
  decision worth them being aware of.
- **`ALTER DEFAULT PRIVILEGES`** is set for every schema, and in `sandbox`
  specifically for *every* role as a possible creator (not just the owner),
  since any of the four roles can create a sandbox table and everyone else
  still needs full grants on it automatically.
- **`pg_stat_statements` installs into `extensions`**, not `pg_catalog` —
  confirmed relocatable on modern PostgreSQL (verified against Supabase's
  and Percona's documented usage), but the template notes the fallback
  (drop `WITH SCHEMA extensions`) in case a locked-down managed Postgres
  build rejects it. It still needs `shared_preload_libraries` + a restart
  regardless of schema — that prerequisite doesn't change.

---

## Anti-patterns to avoid when customizing this further

- ❌ Don't run `bootstrap/*.sql` through Bytebase/Jenkins — it's a manual,
  superuser, pre-flight step by design (see Step 4 above).
- ❌ Don't hardcode passwords into the bootstrap SQL — it takes them as
  `psql -v` variables sourced from `.env` via `run-bootstrap.sh`.
- ❌ Don't grant `TRUNCATE`/`DROP` broadly to satisfy the "sandbox should be
  free-for-all" requirement — use the scoped `drop_table()` helper instead.
- ❌ Don't skip `ALTER DEFAULT PRIVILEGES` — future tables would silently
  lack grants until someone remembers to re-run them.
- ❌ Don't assume Bytebase Cloud conventions (`:cloud` image tag) — this
  skill defaults to self-hosted with a pinned version tag; confirm with the
  user before changing that.
- ❌ Don't invent Bytebase resource names (`instances/...`, `projects/...`)
  — leave the generated `TODO` placeholders until the user has actually
  done the console setup in `docs/BYTEBASE_SETUP.md`.
- ❌ Don't set up a plain Jenkins Pipeline job for this — it needs a
  **Multibranch Pipeline** job so `env.BRANCH_NAME` resolves and each
  environment branch gets its own build.
- ❌ Don't reintroduce sequential all-environments-in-one-run promotion —
  that's the Atlas/GitHub-Actions-tutorial model this skill deliberately
  replaced with branch-per-environment. Promotion is a git merge now.
- ❌ Don't feed `bootstrap/imported/*.sql` (from `import-existing-schema.sh`)
  into `migrations/` or `bytebase-action` directly — those `CREATE TABLE`
  statements will fail against a database where the objects already exist.
  Establishing the baseline is a Bytebase console action; see
  `docs/IMPORTING_EXISTING_DATABASE.md`.
- ❌ Don't use bash `${DB_NAME}` (or any other placeholder name) as a real
  runtime variable inside a script template — `render()` does blind literal
  substitution of `{DB_NAME}`, and `${DB_NAME}` contains that exact
  substring, so it gets corrupted into `$<actual-db-name>` at generation
  time. Found this exact bug in `import-existing-schema.sh.template` during
  testing; every generated-script template must treat placeholder names as
  build-time-only tokens, never as bash variables to source at runtime.
- ❌ Don't put an apostrophe (or any unescaped quote) inside a bash
  `${VAR:?message}` or `${VAR:-message}` word — bash re-parses that word for
  quote characters even though it's nested inside the script's own outer
  double quotes, so `don't` silently breaks the whole script with an
  "unexpected EOF" error. Found this in two scripts during testing; write
  "do not" instead, and never quote an interpolated value with `'...'`
  inside one of these expansions.
- ❌ Don't assume a Postgres `CREATEROLE` admin account (common on RDS/Cloud
  SQL/Azure) can freely `ALTER ... OWNER TO` a role it just created —
  PostgreSQL 16 requires the connecting role to separately be able to
  `SET ROLE` to the target, which creating a role does *not* by itself
  grant. Confirmed by reproducing the exact error (`must be able to SET
  ROLE`) against a real non-superuser account; the fix is the temporary
  `GRANT {role} TO CURRENT_USER` / `REVOKE ... FROM CURRENT_USER` pair
  already in `bootstrap_provision.sql.template` — don't remove it as
  "unnecessary" just because it's a no-op for superusers.
- ❌ Don't assume all 6 extensions install the same way for a non-superuser
  database owner — `dblink`, `postgres_fdw`, and `pg_stat_statements`
  genuinely require actual superuser (verified empirically), while
  `pgcrypto`/`pg_trgm`/`uuid-ossp` don't. This is why each extension is
  wrapped in its own exception-handling `DO` block rather than a single
  flat list of `CREATE EXTENSION` statements — one blocked extension must
  never abort the other five.
- ❌ Don't let a script silently fall back to a hardcoded default account
  (`PG_SUPERUSER` defaulting to `"postgres"`) with no way to configure it
  in `.env` at all — this shipped as a real gap and a real user hit it
  against a managed Postgres (Huawei Cloud RDS) where the actual admin
  account wasn't `"postgres"`, and the script gave no indication anything
  was wrong until the connection failed. Every credential a script needs
  belongs in `.env` (here: `{ENV}_SUPERUSER` / `{ENV}_SUPERUSER_PASSWORD`),
  with the hardcoded default only as a documented last resort, and the
  script should print which value it's using and where it warns when a
  password is empty rather than proceeding silently.
