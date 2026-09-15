# Business Brain — Shared Context for All Skills

**Owner:** isal (Faisal Nugraha)
**Email:** contact@data-ecosystem.id / faisal.nugraha.c@digital.bgn.id
**Org:** digital.bgn.id
**Last updated:** 2026-06-29

> Every skill reads this file before acting. Keep it current.
> Communication preference: natural and simple. Concise but human, not robotic. Tools first, then a short plain explanation.

---

## 1. Who I Am

- **Role:** Data Engineer · Backend Engineer · Software Architect
- **Primary language:** Indonesian (default), English (technical)
- **Timezone:** Asia/Jakarta

## 2. Active Projects

<!-- Format: name — purpose — repo/path — current phase -->
- **pem-master-individu-pm-sync-mpm** — sync master data individu penerima manfaat (PM) — `sipgn-git.bgn.go.id/digital/data-products/domain-penerima-manfaat/master-data-kelompok-penerima-manfaat/pem-master-individu-pm-sync-mpm` — active
- **trino-facs** — Trino column masking + row filtering for FACS security rules — `~/Workspaces/Lab/Experiments/trino/security/rules.json` — active (DATE-type masking constraint resolved 2026-05-20)
- **claude-obsidian** — Obsidian vault + Claude Code integration (Path B, vault at ~/.claude/) — `~/Desktop/claude-obsidian/` / github.com/AgriciDaniel/claude-obsidian — v1.6.0 shipped, push pending

## 3. Tech Stack

**Data:** Airflow 3.1.7 (TaskFlow API), dbt, PySpark, Dagster, Prefect, Trino 4.x (row/column-level security, column masking)
**Backend:** Python 3.x, FastAPI / Flask / Django
**Infra:** GitHub Actions, Terraform / CDK
**Cloud:** On-premise
**Local tooling:** Claude Code (Sonnet 4.6), rtk (Rust Token Killer), Obsidian 1.8.x (vault at ~/.claude/, REST API port 27123)

## 4. Decision Conventions

- Skill-first resolution before specialist dispatch (CLAUDE.md Law 6)
- Wave 0 always runs — context-manager ∥ prompt-engineer (CLAUDE.md Law 0)
- Parallel dispatch for independent tasks (CLAUDE.md §7.1)
- [DATA-WORK] flag for Airflow/dbt/pipeline files → data-engineer only
- **STANDING ORDER (user, 2026-07-25): USE the ~/.claude structure — do NOT default to solo.** The rules above already existed and were still ignored across a long scripts/sppg session (solo Bash/psycopg2/Edit, no data-engineer routing, no reviewer gate). For MPM/scripts/sppg work: route substantial data changes to **data-engineer**; gate non-trivial code/SQL with **code-reviewer + database-reviewer** before "done"; check the **pem-sync-deploy** / **badan-gizi-nasional** skills. Solo only for a small read / one measurement / a mechanical edit.
- Semua konvensi governance dari CLAUDE-*.md berlaku penuh — lihat /Users/isal/.claude/CLAUDE.md
- Communication: natural and simple, human not robotic, tools before a short explanation, no trailing summaries

## 5. Hard Rules — Do NOT

- Do NOT push to main without review
- Do NOT commit secrets, .env, or credentials
- Do NOT bypass CLAUDE.md gates or skip Wave 0
- Do NOT upload to third-party tools without user approval
- Jangan beri estimasi tanpa basis teknis atau data cukup
- Jangan campur tanggung jawab antar layer (frontend vs backend vs infra)
- Jangan overengineer — solusi simpler selalu lebih diutamakan
- Jangan hapus/rusak data tanpa backup atau rollback path yang jelas

## 6. Operational Notes

- **Governance manual:** /Users/isal/.claude/CLAUDE.md (v3.6.2)
- **Memory index:** /Users/isal/.claude/projects/-Users-isal--claude/memory/MEMORY.md
- **Agent definitions:** /Users/isal/.claude/agents/
- **Skills:** /Users/isal/.claude/skills/ (28 registered, see CLAUDE-skills.md §14.1)
- **Wiki:** /Users/isal/.claude/wiki/ (hot cache: wiki/hot.md, index: wiki/index.md)
- **Obsidian REST API:** /Users/isal/.claude/scripts/obsidian.py (port 27123, token: ~/.claude/.obsidian-token)
- **Lessons learned:** /Users/isal/.claude/lessons_learned.md

---

## 7. Project Deep-Context — MPM Sync (loads everywhere; detailed per-file memory only loads inside scripts/sppg)

Two codebases kept in PARITY (same business logic):
- **`~/Workspaces/Organizations/BGN/scripts/sppg/`** — standalone Python CLI: `sync_master_sppg.py`, `sync_sppg_institution.py`, `institution_common.py`, `sync_institution.py`, `sync_beneficiary_created_by.py` (manual tool, leave alone). Has `venv/`, NO ruff. `--dry-run` for verification. NOTE: `py_compile` does NOT catch NameError — use ruff F821 or `import <mod>`.
- **`~/Workspaces/Organizations/BGN/domain/pem-master-individu-pm-sync-mpm/airflow/dags/`** — the Airflow 3.1.7 port. Classic PythonOperator; runtime Connection-ID hydration (NO dotenv under dags); uv; ruff line-length 88; pytest; DagBag import test. Jenkins auto-deploys `airflow/dags/**` on push to **main** ONLY. **Deploy is devops's job now.**
- Accepted parity divergences (NOT drift): wilayah resolver (script HTTP-API 4-level vs airflow DB-cache kel-derive), coordinate coercion (ST_GeomFromText vs safe_float+ST_MakePoint), INSERT/UPDATE template arity (16/16 vs 19/17), institution geography superset in airflow.

Databases (.env / Airflow conn-id). Passwords with a single-S typo are INTENTIONAL, do NOT "fix":
- MPM target — `public` schema, 10.16.3.153 — `pem_mpm_target_db` / `MPM_DB_*` (`MPM_DB_PASSWORD`).
- MDM — `gold` — `pem_mpm_source_db_kpm` / `MDM_DB_*` (`MDM_DB_PASWORD` ← single-S).
- MDM-Individu — `gold`, Huawei RDS host (VPN flaky) — `pem_mpm_source_db_individu` / `MDM_INDIVIDU_DB_*` (`MDM_INDIVIDU_DB_PASWORD` ← single-S).
- Pusdatin `datawarehouse_pusdatin` — 10.16.3.123, schemas data_mart / data_staging_v1 / data_temp — `datawarehouse_pusdatin` / `PUSDATIN_DB_*` (password env `PUSDATIN_PASSWORD`).
- `wil_kode_kewilayahan_zonasi`. Five Airflow connections total; NO Airflow Variables. Diagnostics: use `scripts/sppg/venv` + psycopg2 read-only (dbhub MCP unreliable).

Three DAGs: `pem_master_sppg_to_mpm_v1` (Asset-triggered: etl_sppg → etl_sppg_institution → validate_post_load), `pem_master_kpm_to_mpm_v1` (daily 02:00 WIB), `pem_master_individu_to_mpm_v1` (beneficiary → identity+junction → status; producer/worker + checkpoint + COPY/staging).

SoT & policy PER TABLE:
- `public.sppg` (master): SoT = **`datawarehouse_pusdatin.data_temp.data_sppg_27469`** (switched 2026-06-22 from gold.xref). Key (id_sppg_smo→sppg_id, kode_sppg); ~27,464 valid pairs (27,469 rows − 5 NULL-kode). **SOFT-delete** (out-of-SoT non-dummy → is_active=FALSE, row kept). **is_active == (pair ∈ SoT)** (status_aktif_sppg no longer read). No delete-fraction breaker/flag; absolute floor _MIN_SOT_PAIRS=10000. Enrichment: name+wilayah-codes SoT-primary, mart→v1 cascade for address/coordinate. created_by = xref `last_change_source_type` + fallback 'sync_master_sppg'. Verhoeff-minted `code` = PK; **id_sppg NOT unique (~2,079 dups)**; name NOT NULL, code_sppg+id_sppg nullable. Wilayah = cached kewilayahan (unchanged).
- `public.institution` ↔ gold.master_kelompok_current — STRICT 1:1 delete-unmastered, dummy-guarded, NO sppg_institution FK guard (Fix B reverted). created_by from original_source_type. Airflow superset adds category_code+status+geography.
- `public.sppg_institution` ↔ gold.xref_kpm_sppg_current (MDM) — **1:1 WITH MDM (user's firm rule; do NOT delete links to satisfy other constraints)**. Verified 348,500=348,500, 0 is_active mismatch. is_active = bool_or(status_keanggotaan='aktif') per (sppg_id,kpm). Option A shell-upsert institutions; Option C skips/deletes links whose institution_code absent from public.institution. Organoleptic delete-protection REMOVED.
- `master_individu` (beneficiary/identity/junction) — intentionally **UPSERT-ONLY** (no delete; user rejected hard AND soft delete — never destroy PM data). created_by inline from `master_individu_current.original_source_type` (COALESCE→MIGRATION_LABEL). **beneficiary.is_active** (2026-06-29, was hardcoded TRUE) = latest `xref_individu_kpm_current.status_keanggotaan` ('aktif'→TRUE else/lulus/none→FALSE), via dedicated unconditional `_reconcile_is_active` (dummy-guarded, no-op-guarded, no updated_at touch). Junction has referential guards EXISTS(beneficiary)+EXISTS(identity). PLACEHOLDER-FILL (2026-06-29, BENEFICIARY-ONLY): build_beneficiary_dto skips ONLY when penerima_manfaat_id missing; null/blank NOT-NULL fields filled by type — text (fullname, gender) → '-', date (date_of_birth) → sentinel 1900-01-01, created_by → fallback, is_active → derived; nullable cols stay NULL. build_identity_dtos relaxed to match (gates only on PM-id + identity_value + identity_type). gender has NO check constraint so '-' is accepted. Freshness guard `>=` (equal-timestamp reruns re-apply) + per-column content change-guard (avoids bloat).

SACRED invariants:
- **DUMMY protection** (created_by='dummy', sppg ids like DMYS####): NEVER insert/update/delete/soft-delete; partitioned out of every set-diff; `created_by IS DISTINCT FROM 'dummy'` on every write; minter seeds dummy_codes. Universal exception across all syncs.
- **NEVER fabricate data to satisfy NOT NULL — for SPPG + institution** (skip + log, fix at source; user strongly rejected name=kode_sppg). EXCEPTION (2026-06-29): the BENEFICIARY sync was explicitly changed to the opposite — it fills NOT-NULL nulls with type placeholders ('-' / sentinel date) rather than skip. So "never fabricate" holds for sppg/institution but NOT beneficiary. Confirm scope before applying either rule.
- **Referential-guard pattern** for the recurring "child refs missing parent" class: add EXISTS(parent) → skip-not-error + log; never fabricate a NOT NULL parent. (Seen: sppg_institution→sppg, beneficiary_identity→beneficiary.)
- **Wilayah codes = Kemendagri DOTTED format on EVERY write to MPM** (public.sppg / public.institution province/city/district/village): provinsi `XX` (no dot), kabko `XX.YY`, kec `XX.YY.ZZ`, kel `XX.YY.ZZ.NNNN` (e.g. `32.01.01.0001`). SoT `data_sppg_27469` stores codes UNDOTTED, so any source-primary passthrough MUST run through `format_kode_wilayah()` before writing — apply it in BOTH the source-primary AND the fallback branch so they never diverge. Verify with a regex PATTERN check, never a `LENGTH()` filter (trivially inverts). Bug fixed 2026-07-25: the SoT-primary branch of `_level` returned codes verbatim → ~27,468 undotted rows in public.sppg.

Recurring gotchas:
- **Deploy gap**: fixes on feat branch don't run until merged to main. Several "prod still errors" were STALE DEPLOYS, not code bugs — verify against deployed bundle, not just working tree.
- **Everything 1:1 with MDM (minus dummy)** is the North Star — EXCEPT public.sppg master which is now 1:1 with Pusdatin data_sppg_27469 (the intentional exception that causes the sppg_institution→sppg orphan tension).

OPEN / pending (as of 2026-06-29):
- SPPG DAG `validate_post_load` RED: **56 `sppg_institution→sppg` orphans** (links reference SPPG absent from data_sppg_27469). DECIDED: keep links 1:1 MDM; master shell-inserts referenced-but-missing SPPG as is_active=FALSE. Blocked by name NOT NULL for nameless ones. **NOT yet implemented.**
- 5 SoT rows (data_sppg_27469) with NULL kode_sppg+name → excluded until source fixed.

Verify commands:
- scripts: `cd scripts/sppg && venv/bin/python -m py_compile <f> && venv/bin/python -c "import <mod>"`
- airflow: `cd pem-master-individu-pm-sync-mpm && uv run ruff check airflow/dags && uv run pytest -q`

Detailed per-file memory (loads only inside scripts/sppg): `~/.claude/projects/-Users-isal-Workspaces-Organizations-BGN-scripts-sppg/memory/` — MEMORY.md index + mpm-sync-1to1-policy, mpm-child-fk-orphan-pattern, verify-live-path-after-port, py-compile-misses-nameerror.
