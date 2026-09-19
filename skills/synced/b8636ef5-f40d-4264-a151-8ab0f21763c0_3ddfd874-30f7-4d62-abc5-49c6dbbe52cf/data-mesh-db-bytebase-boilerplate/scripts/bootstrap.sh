#!/usr/bin/env bash
# bootstrap.sh — Generate a Bytebase + Jenkins database GitOps repo, with one
# long-lived git branch per environment (branch-per-environment model).
#
# Usage:
#   bash bootstrap.sh --db-name ops_sample_database \
#     [--environments dev,production] [--branch-map dev=development,production=main] \
#     [--dir .] [--pg-host localhost] [--pg-port 5432] \
#     [--bytebase-version 3.14.0] [--superuser postgres] [--no-git-init]
#
# --branch-map is optional: any environment named exactly "dev" defaults to
# branch "development", any environment named exactly "production" defaults
# to branch "main", and anything else defaults to a branch with the same
# name as the environment. Override any or all of that with --branch-map.
#
# Run from inside this skill's directory (assets/ must be a sibling of scripts/).
set -euo pipefail

BOLD='\033[1m'; CYAN='\033[36m'; GREEN='\033[32m'; YELLOW='\033[33m'; RED='\033[31m'; RESET='\033[0m'
info()    { echo -e "${CYAN}  →${RESET} $1"; }
success() { echo -e "${GREEN}  ✓${RESET} $1"; }
warn()    { echo -e "${YELLOW}  ⚠${RESET} $1"; }
fail()    { echo -e "${RED}  ✗${RESET} $1"; exit 1; }
header()  { echo -e "\n${BOLD}$1${RESET}"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS_DIR="$(cd "${SCRIPT_DIR}/../assets" && pwd)"

DB_NAME_RAW=""
ENVIRONMENTS_RAW="dev,production"
BRANCH_MAP_RAW=""
TARGET_DIR="."
PG_HOST="localhost"
PG_PORT="5432"
BYTEBASE_VERSION="3.14.0"
PG_SUPERUSER="postgres"
GIT_INIT=1

while [[ $# -gt 0 ]]; do
  case $1 in
    --db-name)          DB_NAME_RAW="$2";       shift 2 ;;
    --environments)      ENVIRONMENTS_RAW="$2";  shift 2 ;;
    --branch-map)        BRANCH_MAP_RAW="$2";    shift 2 ;;
    --dir)               TARGET_DIR="$2";        shift 2 ;;
    --pg-host)           PG_HOST="$2";            shift 2 ;;
    --pg-port)           PG_PORT="$2";            shift 2 ;;
    --bytebase-version)  BYTEBASE_VERSION="$2";  shift 2 ;;
    --superuser)         PG_SUPERUSER="$2";       shift 2 ;;
    --no-git-init)        GIT_INIT=0;              shift 1 ;;
    *) fail "Unknown flag: $1" ;;
  esac
done

[[ -z "$DB_NAME_RAW" ]] && fail "Usage: bash bootstrap.sh --db-name ops_sample_database [--environments dev,production] [--branch-map dev=development,production=main] [--dir .]"

# ── Normalize + validate db name (snake_case) ────────────────────────────────
DB_NAME=$(echo "$DB_NAME_RAW" | tr '[:upper:]' '[:lower:]' | tr '-' '_')
if [[ ! "$DB_NAME" =~ ^[a-z][a-z0-9_]*$ ]]; then
  fail "Database name '${DB_NAME_RAW}' is not valid snake_case even after normalization ('${DB_NAME}'). Use lowercase letters, digits, and underscores, starting with a letter — e.g. ops_sample_database."
fi
if [[ "$DB_NAME" != "$DB_NAME_RAW" ]]; then
  warn "Normalized db name '${DB_NAME_RAW}' → '${DB_NAME}'"
fi

# ── Parse environments ────────────────────────────────────────────────────────
IFS=',' read -r -a ENVIRONMENTS <<< "$ENVIRONMENTS_RAW"
[[ ${#ENVIRONMENTS[@]} -lt 1 ]] && fail "Need at least one environment"
for e in "${ENVIRONMENTS[@]}"; do
  [[ "$e" =~ ^[a-zA-Z][a-zA-Z0-9_-]*$ ]] || fail "Invalid environment name: '$e'"
done
ENV_LIST=$(printf '%s, ' "${ENVIRONMENTS[@]}")
ENV_LIST="${ENV_LIST%, }"
ENV_LIST_LOWER=$(echo "$ENV_LIST" | tr '[:upper:]' '[:lower:]' | tr ', ' '|' | tr -s '|')

# ── Env → branch mapping ──────────────────────────────────────────────────────
declare -A ENV_TO_BRANCH
if [[ -n "$BRANCH_MAP_RAW" ]]; then
  IFS=',' read -r -a _branch_pairs <<< "$BRANCH_MAP_RAW"
  for pair in "${_branch_pairs[@]}"; do
    env_key="${pair%%=*}"
    branch_val="${pair#*=}"
    [[ "$env_key" == "$pair" ]] && fail "Invalid --branch-map entry '${pair}' — expected env=branch, e.g. dev=development"
    ENV_TO_BRANCH["$env_key"]="$branch_val"
  done
fi
for e in "${ENVIRONMENTS[@]}"; do
  if [[ -z "${ENV_TO_BRANCH[$e]:-}" ]]; then
    case "$e" in
      production) ENV_TO_BRANCH["$e"]="main" ;;
      dev)        ENV_TO_BRANCH["$e"]="development" ;;
      *)          ENV_TO_BRANCH["$e"]="$e" ;;
    esac
  fi
done
BRANCH_MAP_SUMMARY=""
for e in "${ENVIRONMENTS[@]}"; do
  BRANCH_MAP_SUMMARY+="${ENV_TO_BRANCH[$e]}=${e}, "
done
BRANCH_MAP_SUMMARY="${BRANCH_MAP_SUMMARY%, }"

BOOTSTRAP_FILE="001_provision_${DB_NAME}.sql"

# render() always substitutes these, even for templates that don't use them,
# so they must exist (set -u) before the first render() call — they get
# their real values later, right before the templates that need them.
BRANCH_MAP_ENTRIES=""
TARGETS_ENTRIES=""
QUICK_START_STEPS=""

header "⚡ Data Mesh DB Bytebase Boilerplate"
echo "  DB Name      : ${DB_NAME}"
echo "  Roles        : ${DB_NAME} (owner) | ${DB_NAME}_readonly | ${DB_NAME}_readwrite | ${DB_NAME}_ops"
echo "  Schemas      : sandbox, extensions, bronze, silver, gold, audit, remote"
echo "  Environments : ${ENV_LIST}"
echo "  Branch map   : ${BRANCH_MAP_SUMMARY}"
echo "  Bytebase     : self-hosted, image tag ${BYTEBASE_VERSION}"
echo "  Target dir   : ${TARGET_DIR}"

mkdir -p "${TARGET_DIR}/bootstrap" "${TARGET_DIR}/migrations" "${TARGET_DIR}/docs" "${TARGET_DIR}/scripts"

header "📁 Generating files..."

# ── Small helper: slurp a template, run substitutions, write it out ─────────
render() {
  local template_path="$1" output_path="$2"
  local content
  content="$(cat "$template_path")"
  content="${content//\{DB_NAME\}/$DB_NAME}"
  content="${content//\{ENV_LIST\}/$ENV_LIST}"
  content="${content//\{ENV_LIST_LOWER\}/$ENV_LIST_LOWER}"
  content="${content//\{BYTEBASE_VERSION\}/$BYTEBASE_VERSION}"
  content="${content//\{BOOTSTRAP_FILE\}/$BOOTSTRAP_FILE}"
  content="${content//\{SEQ\}/001}"
  content="${content//\{BRANCH_MAP_ENTRIES\}/$BRANCH_MAP_ENTRIES}"
  content="${content//\{BRANCH_MAP_SUMMARY\}/$BRANCH_MAP_SUMMARY}"
  content="${content//\{TARGETS_ENTRIES\}/$TARGETS_ENTRIES}"
  content="${content//\{QUICK_START_STEPS\}/$QUICK_START_STEPS}"
  printf '%s\n' "$content" > "$output_path"
}

# .gitignore
cp "${ASSETS_DIR}/gitignore.template" "${TARGET_DIR}/.gitignore"
success ".gitignore"

# bootstrap/<seq>_provision_<db>.sql
render "${ASSETS_DIR}/bootstrap_provision.sql.template" "${TARGET_DIR}/bootstrap/${BOOTSTRAP_FILE}"
success "bootstrap/${BOOTSTRAP_FILE}"

# migrations/ placeholder so git tracks the (initially empty) directory
cat > "${TARGET_DIR}/migrations/.gitkeep" << 'EOF'
Bytebase-managed migrations go here from now on. Filename must start with a
version: e.g. 202607230001_add_column_x_ddl.sql (or semver: 1.1.0_x.sql).
See docs/DEVELOPER_GUIDE.md, section 7.
EOF
success "migrations/.gitkeep"

# .env.example — built per environment
{
  echo "# ${DB_NAME} — Environment Configuration"
  echo "# cp .env.example .env  &&  fill in real passwords. NEVER commit .env."
  echo "# Roles: ${DB_NAME} (owner, used by Bytebase for migrations) | _readonly | _readwrite | _ops"
  echo ""
  echo "DB_NAME=${DB_NAME}"
  for env in "${ENVIRONMENTS[@]}"; do
    ENV_UPPER=$(echo "$env" | tr '[:lower:]' '[:upper:]' | tr '-' '_')
    echo ""
    echo "# ── ${env} ──────────────────────────────────────────────────────────"
    echo "${ENV_UPPER}_PG_HOST=localhost"
    echo "${ENV_UPPER}_PG_PORT=${PG_PORT}"
    echo "# Account used ONLY for the one-time bootstrap (scripts/run-bootstrap.sh,"
    echo "# scripts/import-existing-schema.sh). Needs CREATEDB/CREATEROLE at minimum —"
    echo "# does NOT need to be a true Postgres superuser. On managed providers (RDS,"
    echo "# Cloud SQL, Azure, Huawei Cloud, etc.) this is whatever admin username you"
    echo "# chose when the instance was created — it is usually NOT literally"
    echo "# \"postgres\". Get this wrong and the bootstrap scripts silently fall back to"
    echo "# \"postgres\" with no password, which will fail against any real managed instance."
    echo "${ENV_UPPER}_SUPERUSER=${PG_SUPERUSER}"
    echo "${ENV_UPPER}_SUPERUSER_PASSWORD=changeme"
    echo "${ENV_UPPER}_OWNER_PASSWORD=changeme"
    echo "${ENV_UPPER}_READONLY_PASSWORD=changeme"
    echo "${ENV_UPPER}_READWRITE_PASSWORD=changeme"
    echo "${ENV_UPPER}_OPS_PASSWORD=changeme"
    echo "${ENV_UPPER}_OWNER_DATABASE_URL=postgres://${DB_NAME}:\${${ENV_UPPER}_OWNER_PASSWORD}@\${${ENV_UPPER}_PG_HOST}:\${${ENV_UPPER}_PG_PORT}/${DB_NAME}?sslmode=disable"
    echo "${ENV_UPPER}_OPS_DATABASE_URL=postgres://${DB_NAME}_ops:\${${ENV_UPPER}_OPS_PASSWORD}@\${${ENV_UPPER}_PG_HOST}:\${${ENV_UPPER}_PG_PORT}/${DB_NAME}?sslmode=disable"
  done
  echo ""
  echo "# ── Bytebase (used by Jenkins, not by the app) ─────────────────────"
  echo "BYTEBASE_URL=https://bytebase.your-company.internal"
  echo "BYTEBASE_PROJECT=projects/${DB_NAME}"
  echo "# BYTEBASE_SERVICE_ACCOUNT / BYTEBASE_SERVICE_ACCOUNT_SECRET live in Jenkins credentials — see docs/BYTEBASE_SETUP.md"
} > "${TARGET_DIR}/.env.example"
success ".env.example"

[[ ! -f "${TARGET_DIR}/.env" ]] && cp "${TARGET_DIR}/.env.example" "${TARGET_DIR}/.env" && warn ".env created — fill in real passwords before running scripts/run-bootstrap.sh" || warn ".env already exists, left untouched"

# Jenkinsfile — build the Groovy BRANCH_ENV_MAP entries, keyed by branch name.
# requireApproval is true for every environment except the first one in
# --environments (order defines risk: first = lowest-stakes, e.g. dev).
BRANCH_MAP_ENTRIES=""
for i in "${!ENVIRONMENTS[@]}"; do
  e="${ENVIRONMENTS[$i]}"
  branch="${ENV_TO_BRANCH[$e]}"
  approval="false"
  [[ "$i" -gt 0 ]] && approval="true"
  sep=","
  [[ "$i" -eq $((${#ENVIRONMENTS[@]} - 1)) ]] && sep=""
  BRANCH_MAP_ENTRIES+="  '${branch}': [envName: '${e}', target: 'instances/${e}-instance/databases/${DB_NAME}', requireApproval: ${approval}]${sep}"$'\n'
done
render "${ASSETS_DIR}/Jenkinsfile.template" "${TARGET_DIR}/Jenkinsfile"
success "Jenkinsfile"

# bytebase-manual-rollout.sh's TARGETS assoc array — same instance/database
# targets as BRANCH_ENV_MAP above, but keyed by ENVIRONMENT name (since a
# human picks an environment directly, there's no branch involved).
TARGETS_ENTRIES=""
for e in "${ENVIRONMENTS[@]}"; do
  TARGETS_ENTRIES+="  [${e}]=\"instances/${e}-instance/databases/${DB_NAME}\""$'\n'
done

# docker-compose.bytebase.yml — disposable local Bytebase for testing
render "${ASSETS_DIR}/docker-compose.bytebase.yml.template" "${TARGET_DIR}/docker-compose.bytebase.yml"
success "docker-compose.bytebase.yml"

# docs/
QUICK_START_STEPS="1. cp .env.example .env   # fill in the bootstrap admin account + role passwords per environment
2. For each environment, run once:  scripts/run-bootstrap.sh --env <name>
3. scripts/verify-roles.sh --env <name>   # confirm roles/schemas/extensions
4. Follow docs/BYTEBASE_SETUP.md          # one-time Bytebase console setup
5. Edit the Jenkinsfile's TODOs with your real Bytebase URL/project/targets
6. Set up a Jenkins Multibranch Pipeline job pointed at this repo
7. Push to a mapped branch (${BRANCH_MAP_SUMMARY}) to trigger a rollout"

render "${ASSETS_DIR}/BYTEBASE_SETUP.md.template" "${TARGET_DIR}/docs/BYTEBASE_SETUP.md"
success "docs/BYTEBASE_SETUP.md"

render "${ASSETS_DIR}/DEVELOPER_GUIDE.md.template" "${TARGET_DIR}/docs/DEVELOPER_GUIDE.md"
success "docs/DEVELOPER_GUIDE.md"

render "${ASSETS_DIR}/IMPORTING_EXISTING_DATABASE.md.template" "${TARGET_DIR}/docs/IMPORTING_EXISTING_DATABASE.md"
success "docs/IMPORTING_EXISTING_DATABASE.md"

render "${ASSETS_DIR}/README.md.template" "${TARGET_DIR}/README.md"
success "README.md"

# scripts/
render "${ASSETS_DIR}/run-bootstrap.sh.template" "${TARGET_DIR}/scripts/run-bootstrap.sh"
chmod +x "${TARGET_DIR}/scripts/run-bootstrap.sh"
success "scripts/run-bootstrap.sh"

render "${ASSETS_DIR}/verify-roles.sh.template" "${TARGET_DIR}/scripts/verify-roles.sh"
chmod +x "${TARGET_DIR}/scripts/verify-roles.sh"
success "scripts/verify-roles.sh"

render "${ASSETS_DIR}/import-existing-schema.sh.template" "${TARGET_DIR}/scripts/import-existing-schema.sh"
chmod +x "${TARGET_DIR}/scripts/import-existing-schema.sh"
success "scripts/import-existing-schema.sh"

render "${ASSETS_DIR}/bytebase-manual-rollout.sh.template" "${TARGET_DIR}/scripts/bytebase-manual-rollout.sh"
chmod +x "${TARGET_DIR}/scripts/bytebase-manual-rollout.sh"
success "scripts/bytebase-manual-rollout.sh"

# ── Git: one branch per environment ──────────────────────────────────────────
# Collect distinct branch names in environment order (dedup, in case two
# environments were mapped to the same branch on purpose).
UNIQUE_BRANCHES=()
for e in "${ENVIRONMENTS[@]}"; do
  b="${ENV_TO_BRANCH[$e]}"
  already=0
  for existing in "${UNIQUE_BRANCHES[@]:-}"; do [[ "$existing" == "$b" ]] && already=1; done
  [[ "$already" -eq 0 ]] && UNIQUE_BRANCHES+=("$b")
done

if [[ "$GIT_INIT" -eq 1 ]]; then
  if ( cd "${TARGET_DIR}" && git rev-parse --is-inside-work-tree > /dev/null 2>&1 ); then
    warn "Already inside a git working tree — skipping git init/branch creation. Create these branches yourself: ${UNIQUE_BRANCHES[*]}"
  else
    (
      cd "${TARGET_DIR}"
      git init -q -b "${UNIQUE_BRANCHES[0]}"
      if [[ -z "$(git config user.email 2>/dev/null || true)" ]]; then
        git config user.email "bootstrap@${DB_NAME}.local"
        git config user.name "Data Mesh Bootstrap"
        warn "No git identity configured — set a local placeholder for this repo's initial commit. Update with: git config user.name / user.email"
      fi
      git add -A
      git commit -q -m "Bootstrap ${DB_NAME} data product repo (Bytebase + Jenkins, branch-per-environment)"
      for b in "${UNIQUE_BRANCHES[@]:1}"; do
        git branch -q "$b"
      done
    )
    success "git repo initialized — branches: ${UNIQUE_BRANCHES[*]} (all currently pointing at the same initial commit)"
  fi
else
  warn "Skipped git init (--no-git-init) — create these branches yourself: ${UNIQUE_BRANCHES[*]}"
fi

header "✅ Done"
echo "  Next steps:"
echo "  1. cd ${TARGET_DIR} && cp .env.example .env, fill in passwords"
echo "  2. scripts/run-bootstrap.sh --env ${ENVIRONMENTS[0]}   (repeat per environment)"
echo "  3. scripts/verify-roles.sh --env ${ENVIRONMENTS[0]}"
echo "  4. Onboarding an existing database? scripts/import-existing-schema.sh --env <name>, then docs/IMPORTING_EXISTING_DATABASE.md"
echo "  5. Follow docs/BYTEBASE_SETUP.md"
echo "  6. Fill in the Jenkinsfile TODOs (BYTEBASE_URL, BYTEBASE_PROJECT, instance targets)"
echo "  7. Test without Jenkins: scripts/bytebase-manual-rollout.sh --env ${ENVIRONMENTS[0]} --check"
echo "  8. Push branches (${UNIQUE_BRANCHES[*]}) to your git remote"
echo "  9. Create a Jenkins Multibranch Pipeline job pointed at this repo"
