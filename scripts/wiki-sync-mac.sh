#!/usr/bin/env bash
# Sync the wiki repo: pull, scan unpushed commits for secrets, push. Owner decision D10 (b), 2026-11-11.
set -u
export PATH="/opt/homebrew/bin:/usr/bin:/bin:${PATH:-}"

WIKI_DIR="${WIKI_DIR:-$HOME/.claude/wiki}"
LOG="${WIKI_SYNC_LOG:-$HOME/.claude/logs/wiki-sync.log}"
GITLEAKS="${GITLEAKS:-/opt/homebrew/bin/gitleaks}"
mkdir -p "$(dirname "$LOG")"

log() { printf '%s %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" >> "$LOG"; }

cd "$WIKI_DIR" 2>/dev/null || { log "ERROR cannot cd to $WIKI_DIR"; exit 1; }
GIT_DIR_PATH="$(git rev-parse --git-dir 2>/dev/null)" || { log "ERROR $WIKI_DIR is not a git repo"; exit 1; }

if [ -e "$GIT_DIR_PATH/sync-blocked" ]; then
  log "blocked: $GIT_DIR_PATH/sync-blocked exists, skipping (remove it after cleaning the secret)"
  exit 0
fi

# Rebase or merge in progress: someone is working on the tree, skip quietly.
if [ -d "$GIT_DIR_PATH/rebase-merge" ] || [ -d "$GIT_DIR_PATH/rebase-apply" ] || [ -e "$GIT_DIR_PATH/MERGE_HEAD" ]; then
  exit 0
fi

if ! out="$(git pull --rebase --autostash -q origin main 2>&1)"; then
  git rebase --abort >/dev/null 2>&1
  log "ERROR pull --rebase failed, aborted: $(printf '%s' "$out" | tr '\n' ' ')"
  exit 1
fi

ahead="$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)"
if [ "$ahead" = "0" ]; then
  exit 0
fi

if ! scan="$("$GITLEAKS" git --log-opts="origin/main..HEAD" --redact --no-banner --no-color . 2>&1)"; then
  touch "$GIT_DIR_PATH/sync-blocked"
  log "SECRET FOUND in $ahead unpushed commit(s), push stopped. Created $GIT_DIR_PATH/sync-blocked. gitleaks: $(printf '%s' "$scan" | tr '\n' ' ' | /usr/bin/cut -c1-600)"
  exit 1
fi

if out="$(git push -q origin HEAD:main 2>&1)"; then
  log "pushed $ahead commit(s) to origin/main"
else
  log "ERROR push failed: $(printf '%s' "$out" | tr '\n' ' ')"
  exit 1
fi
