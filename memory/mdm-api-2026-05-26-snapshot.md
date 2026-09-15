---
type: session
project: mdm-api
project_path: /Users/isal/Workspaces/Organizations/BGN/apps/mdm-api
pipeline_class: Complex
session_date: 2026-05-26
status: complete
tags:
  - rust
  - axum
  - sqlx
  - postgis
  - bgn
  - mbg
  - kpm
  - scd-type-4
---

# MDM API — Complex Pipeline Snapshot (2026-05-26)

## Summary

Full Axum 0.8 MDM API (Master Data Kelompok Penerima Manfaat) implemented from scratch for BGN.
29 source files + migrations + infra. code-reviewer passed on second cycle (3 blockers resolved).

## Stack

- **Framework:** Axum 0.8 (specificity-based route matching — not registration-order)
- **Database:** PostgreSQL + PostGIS, via sqlx 0.8 (compile-time checked queries)
- **Runtime:** Tokio 1.x async
- **Auth:** JWT + API key middleware (`verifikasi_auth`)
- **Observability:** tracing + opentelemetry 0.27 (OTLP HTTP)
- **OpenAPI:** utoipa 5 + utoipa-swagger-ui 8 (served at `/docs`)
- **Crate version:** mdm-api 2.0.0

## Key Decisions (carry forward)

### 1. Naming convention split
- Function/variable names: English
- JSON response field names: Indonesian (via Indonesian struct field names — no serde rename needed)
- Domain + DTO struct field names: Indonesian

### 2. PostGIS coordinate parameterization
- NEVER use `format!()` to interpolate f64 into SQL
- Correct pattern:
  ```sql
  CASE WHEN $17::double precision IS NOT NULL
       THEN ST_SetSRID(ST_MakePoint($18, $17), 4326)
       ELSE NULL END
  ```
  with `Option<f64>` bound params for lat ($17) and lon ($18)

### 3. SCD Type 4 snapshot — full-column SELECT
- `kpm_riwayat` INSERT must use full column SELECT from `kpm`
- Partial column list defeats audit purpose
- Pattern: `INSERT INTO kpm_riwayat (...all cols...) SELECT (...all cols...) FROM kpm WHERE kpm_id = $1`

### 4. kpm_riwayat missing columns workaround
- Table schema lacks: `adalah_saat_ini`, `dibuat_pada`, `diperbarui_pada`
- `PROYEKSI_KPM_RIWAYAT` constant substitutes:
  - `false AS adalah_saat_ini`
  - `disimpan_pada AS dibuat_pada`
  - `disimpan_pada AS diperbarui_pada`
- Used only in `ambil_kpm` SCD temporal branch

### 5. identitas_kpm — no soft delete
- Table has NO `dihapus_pada` column
- Do NOT add `AND dihapus_pada IS NULL` predicate to queries on this table

### 6. Axum 0.8 route matching
- Specificity-based: literal segments beat parameterized segments automatically
- Registration order does NOT affect route priority
- `/kpm/search` correctly beats `/kpm/:id` without special ordering

### 7. Generic ToSchema limitation
- `Amplop<T: Serialize>` cannot derive `ToSchema` without `T: ToSchema` bound
- Resolution: removed `ToSchema` from both `Amplop<T>` and `AmplopDaftar<T>`
- These wrappers are excluded from OpenAPI schema components

### 8. Initial KPM status on POST
- KPM created with `status = 'non-aktif'` (requires Data Steward activation per spec)
- Original incorrect value was `'aktif'` — corrected in parameterized INSERT

## Files Created (complete)

### Infrastructure
- `Cargo.toml` — mdm-api 2.0.0, axum 0.8, sqlx 0.8, utoipa 5, opentelemetry 0.27
- `config/default.toml`
- `.env.example`
- `.gitignore`
- `Dockerfile` — cargo-chef multi-stage build
- `docker-compose.yml`
- `.dockerignore`

### Migrations
- `migrations/20260526000001_create_extensions_dan_tipe.sql`
- `migrations/20260526000002_create_kpm.sql`
- `migrations/20260526000003_create_indexes.sql`

### Source (29 files)
- `src/lib.rs`, `src/main.rs`, `src/config.rs`, `src/error.rs`, `src/state.rs`
- `src/telemetry.rs`, `src/router.rs`
- `src/domain/mod.rs`, `src/domain/alamat.rs`, `src/domain/enums.rs`
- `src/domain/identitas.rs`, `src/domain/kontak.rs`, `src/domain/koordinat.rs`
- `src/domain/kpm.rs`, `src/domain/metadata_riwayat.rs`, `src/domain/pemetaan_sppg.rs`
- `src/dto/mod.rs`, `src/dto/meta.rs`, `src/dto/permintaan.rs`, `src/dto/respons.rs`
- `src/repository/mod.rs`, `src/repository/traits.rs`
- `src/repository/postgres/mod.rs`, `src/repository/postgres/kpm_repo.rs`
- `src/middleware/mod.rs`, `src/middleware/auth.rs`
- `src/handlers/mod.rs`, `src/handlers/health.rs`, `src/handlers/kpm.rs`

## Gate Outcomes

| Gate | Round | Verdict | Notes |
|------|-------|---------|-------|
| code-reviewer | 1 | REJECTED | 3 blocking issues, 7 warnings |
| code-reviewer | 2 | APPROVED | All blockers resolved |

Blockers resolved in round 2:
1. PostGIS f64 interpolation via `format!()` → replaced with parameterized CASE WHEN
2. `KelompokPenerimaMaanfaat` typo → corrected to `KelompokPenerimaManfaat` in domain/kpm.rs
3. Initial KPM status `'aktif'` → corrected to `'non-aktif'`

## Known Remaining Issues

### WARNING-2 — opentelemetry deprecated API (non-blocking)
- File: `src/telemetry.rs`
- Issue: `new_pipeline()` / `new_exporter()` deprecated in opentelemetry 0.27; removed in 0.28
- Status: compiles with warnings on 0.27; must fix before upgrading to 0.28
- Fix: replace with `OtlpTracingConfig` builder pattern per 0.28 migration guide

### WARNING-5 — identitas_kpm ORDER BY without index (non-blocking)
- `ORDER BY identitas_id` on `identitas_kpm` — no index on `identitas_id`
- Acceptable for current data scale; add index if queries slow down

## Unresolved / Follow-up

- [ ] **test-engineer not run** — no unit or integration tests written yet
- [ ] **documentation-expert not run** — no README or API guide updates
- [ ] **SQLX_OFFLINE setup** — `cargo build` with sqlx macros requires either:
  - Live `DATABASE_URL` pointing to a running PostgreSQL instance, OR
  - `cargo sqlx prepare` to generate `.sqlx/` query cache for offline builds
  - Development setup doc needed for onboarding
- [ ] Changes not committed — no git operations performed this session

## Architecture Notes

### Repository pattern
- `KpmRepository` trait in `src/repository/traits.rs`
- `PostgresKpmRepository` in `src/repository/postgres/kpm_repo.rs`
- State injected via `AppState` (Arc-wrapped PgPool + config)

### Route structure
```
GET  /health                        — public, no auth
GET  /kpm                           — list (paginated)
POST /kpm                           — create (non-aktif initial state)
GET  /kpm/search                    — full-text + filter search
GET  /kpm/geospatial/nearby         — PostGIS nearest-neighbor
GET  /kpm/sppg/:identifier          — by SPPG
GET  /kpm/wilayah/:tingkat/:id      — by region hierarchy
GET  /kpm/aggregate/:tingkat/:id    — regional aggregates
GET  /kpm/:id                       — single KPM detail
PUT  /kpm/:id                       — full update
DELETE /kpm/:id                     — soft delete
GET  /kpm/:id/history               — SCD Type 4 audit trail
GET  /docs                          — Swagger UI (public)
GET  /api-docs/openapi.json         — OpenAPI spec (public)
```

### SCD Type 4 pattern
- Live data: `kpm` table (current state only)
- History: `kpm_riwayat` table (append-only snapshots, `disimpan_pada` timestamp)
- On every PUT: snapshot pre-update row to `kpm_riwayat`, then UPDATE `kpm`
- `PROYEKSI_KPM_RIWAYAT` constant handles schema delta between tables

## Context for Next Session

- Project is code-complete for the defined scope (no tests, no docs)
- Next most urgent: run `cargo sqlx prepare` and document dev setup in README
- After that: test-engineer (integration tests with `axum-test`), then documentation-expert
- opentelemetry 0.28 migration is a known deferred item — do not upgrade without fixing telemetry.rs first
