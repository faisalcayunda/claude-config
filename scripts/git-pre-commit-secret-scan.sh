#!/bin/sh
# Git pre-commit hook: block staged credentials and NIK values.
# Install per repo: ln -sf /Users/isal/.claude/scripts/git-pre-commit-secret-scan.sh .git/hooks/pre-commit
# Reviewed example credentials are suppressed through <repo>/.secret-scan-baseline.
root=$(git rev-parse --show-toplevel) || exit 2
set -- --git-staged
[ -f "$root/.secret-scan-baseline" ] && set -- "$@" --baseline "$root/.secret-scan-baseline"
if ! /usr/bin/python3 /Users/isal/.claude/scripts/secret_scan.py "$@"; then
  echo "pre-commit: secret scan failed. Remove the secret, or if the line is a reviewed example," >&2
  echo "regenerate .secret-scan-baseline after review (scripts/secret_scan.py --write-baseline)." >&2
  exit 1
fi
