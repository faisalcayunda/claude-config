# bytebase-action CLI reference

Source of truth: https://github.com/bytebase/bytebase/blob/main/action/README.md
— re-fetch that page if the user asks for something not covered here, rather
than guessing at flags.

`bytebase-action` is a Docker image (`bytebase/bytebase-action:<tag>`), not a
GitHub-Actions-only tool. It reads flags/env vars and talks to the Bytebase
REST API — this is exactly why it drops into a Jenkins `sh 'docker run ...'`
step with no adaptation needed, unlike the workflow YAML around it.

## Two subcommands

- `check` — lints `--file-pattern` files. Use `--check-release=FAIL_ON_ERROR`
  (or `FAIL_ON_WARNING`) so the Jenkins stage actually fails the build on
  problems; the default `SKIP` never fails regardless of findings.
- `rollout` — creates a release + rollout issue in `--project`, applying
  `--file-pattern` files to `--targets`, up to `--target-stage`. If `--plan`
  is given instead, `--file-pattern`/`--targets` are ignored.

## Global flags that matter for a Jenkinsfile

- `--url` — Bytebase instance URL. Required.
- `--service-account` / `--service-account-secret` — read from
  `BYTEBASE_SERVICE_ACCOUNT` / `BYTEBASE_SERVICE_ACCOUNT_SECRET` env vars if
  not passed as flags. Always prefer the env var for the secret.
- `--project` — `projects/{name}`.
- `--targets` — comma-separated `instances/{instance}/databases/{database}`
  (or a `projects/{project}/databaseGroups/{group}`). Only used when `--plan`
  isn't set.
- `--file-pattern` — glob. In **versioned mode** (what this skill defaults
  to), filenames must start with `v`/`V` + digits, or plain digits/semver:
  `v1.2.3_x.sql`, `1.0_x.sql`, `V2_x.sql`, `202607230001_x.sql` all parse.
  In **declarative mode** (`--declarative`), no version prefix is needed —
  version is auto-generated from a timestamp instead.
- `--target-stage` — `environments/{name}`. If omitted, the rollout is
  created but the command returns without waiting for it to finish.
- `--output` — JSON file with created resource names / check results; worth
  archiving as a Jenkins artifact for traceability.

## Image tags

Self-hosted: pin to the exact Bytebase server version, e.g.
`bytebase/bytebase-action:3.14.0` — mismatched action/server versions are
explicitly checked and can fail before doing anything. Bytebase Cloud users
would instead use the `:cloud` tag (not applicable to this skill's default,
which targets self-hosted).

## Migration type comments (versioned mode only)

A file can declare a special migration type via a leading comment:
```sql
-- migration-type: ghost
ALTER TABLE large_table ADD COLUMN new_col VARCHAR(255);
```
Only `ghost` (gh-ost online schema change) is currently supported; anything
else or absent defaults to a normal migration.
