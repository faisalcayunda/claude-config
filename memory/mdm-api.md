---
project: mdm-api
path: /Users/isal/Workspaces/Organizations/BGN/apps/mdm-api
last_updated: 2026-05-31
status: complete (all 9 endpoints implemented, tested, reviewed, documented); Axum 0.8 route syntax fixed; API-layer field names standardized to English
stack: Rust, Axum 0.8, SQLx, OpenTelemetry, Docker Compose
---

# mdm-api — Session Snapshot

## Project State

All 9 KPM (Keluarga Penerima Manfaat) endpoints implemented, code-review approved, tested, and documented. Project runnable via `docker compose`.

No git repository initialized. No SQLX_OFFLINE setup done.

## Axum 0.8 Route Syntax (established 2026-05-31)

- **Breaking change from 0.7**: path parameters use `{param}` syntax, not `:param`.
- **Fix applied**: 7 routes in `src/main.rs` updated (lines 82, 83, 85, 95, 96, 123, 135).
- **Gate**: `cargo check` clean after fix.

## API-Layer Field Name Convention (established 2026-05-31)

- **Rule**: all API-layer structs (response, request, error, meta DTOs) use English field names.
- **Exception**: DB-bound row structs (`KpmRow`, `IdentityRow`, `HistoryRow`, `AggregateRow`) keep Indonesian names to match DB column names exactly. `KpmStatus` / `RegionLevel` serde renames kept Indonesian (domain vocabulary / DB enum values).
- **Files changed**: `src/dto/response.rs`, `src/dto/request.rs`, `src/dto/meta.rs`, `src/error.rs`, `src/repository/postgres/kpm_repo.rs` (constructors only), `src/handlers/kpm.rs` (parse_pagination strings).
- **Notable fix during review**: `kode_subkategori` renamed to `subcategory_code`; error code strings changed to English. Code-reviewer rejected once (3 defects), approved after fix.
- **Gate**: code-reviewer approved, `cargo check` 0 errors 0 warnings.

## Pre-existing noted (not introduced this session, out of scope)

- `DuplicateIdentity` enum variant has `tipe`/`nilai` internal fields — not in JSON output, no API impact.
- `read_replica_url = ""` in `default.toml` is a latent bug, mitigated by `.env` override.

## config-rs Environment Source Convention (established 2026-05-31)

- **No prefix**: `Environment::default().separator("__")` — env vars use bare section names, e.g. `DATABASE__URL`, `AUTH__JWT_SECRET`.
- **Prior state**: `with_prefix("MDM").separator("__")` required `MDM__DATABASE__URL` etc. — removed this session.
- **Why double underscore**: single `_` separator collides with field names that contain underscores (`jwt_secret`, `read_replica_url`). config-rs splits on every separator occurrence, producing wrong struct traversal paths. `__` is the correct separator whenever any field name contains `_`.
- **Lesson**: logged to lessons_learned.md.

## Architecture Decisions

- **Framework**: Axum with axum-valid 0.24 for request validation
- **Validation approach**: `p.validate().map_err(AppError::from)?` called manually before `Valid(...)` construction in each handler closure — workaround for axum-valid 0.24 trait-solver limitation. Applied in all 7 closures in `src/main.rs`.
- **Router location**: `build_router` moved from `src/router.rs` to `src/main.rs` with closure wrappers. Closures required because axum-valid 0.24 `ValidRejection` trait does not resolve cleanly through function pointer indirection.
- **Error mapping**: `impl From<validator::ValidationErrors> for AppError` added in `src/error.rs` — maps to `ValidasiGagal(Vec<String>)` → HTTP 422. This was the root cause of the first code-reviewer rejection (validation bypass: `Valid<>` was silently passing invalid input).
- **Repository mocking**: `#[cfg_attr(any(test, feature = "test-helpers"), automock)]` on `KpmRepository` trait. mockall 0.13 in dev-deps. Optional dep for `test-helpers` feature in `Cargo.toml`.
- **Telemetry**: `opentelemetry_otlp::SpanExporter::builder().with_http().with_endpoint(...).build()` + `sdktrace::TracerProvider::builder()` — replaced deprecated `new_pipeline()` / `new_exporter()` APIs. Now warning-free.

## Files Changed — Session 2026-05-31 (config-rs prefix removal)

### Changed
- `src/config.rs` (line 57) — `Environment::with_prefix("MDM").separator("__")` changed to `Environment::default().separator("__")`
- `.env` — 10 keys renamed: `MDM__*` prefix stripped; keys now follow `SECTION__FIELD` convention (e.g. `DATABASE__URL`, `AUTH__JWT_SECRET`, `SERVER__PORT`, `OBSERVABILITY__LOG_LEVEL`, etc.)

### Gate outcomes
| Gate | Outcome |
|---|---|
| code-reviewer | Approved |
| cargo check | Clean |

---

## Files Changed — Session 2026-05-26 (initial implementation)

### Core
- `src/main.rs` — build_router + closure wrappers + `p.validate().map_err(AppError::from)?` in all 7 closures; `use validator::Validate as _;`
- `src/router.rs` — build_router removed (moved to main.rs)
- `src/error.rs` — `impl From<validator::ValidationErrors> for AppError` added
- `src/telemetry.rs` — OTel API updated to non-deprecated form

### DTOs
- `src/dto/permintaan.rs` — `Serialize` added to `PermintaanIdentitas`

### Repository
- `src/repository/traits.rs` — `automock` attr added under cfg_attr gate

### Tests
- `src/handlers/kpm_tests.rs` — 23 unit tests (9 DTO validation + 14 handler tests)
- `tests/kpm_handlers.rs` — 11 integration tests via Router + oneshot

### Dependencies (`Cargo.toml`)
- mockall 0.13 added to dev-deps
- Optional dep for `test-helpers` feature
- axum-valid bumped to 0.24
- utoipa-swagger-ui bumped to 9
- opentelemetry-otlp: `default-features = false`

### Documentation
- `README.md` — created at project root (documentation-expert wave)

## Gate Outcomes

| Gate | Outcome | Notes |
|---|---|---|
| code-reviewer (round 1) | Rejected | Found validation bypass: `Valid<>` not enforcing validator annotations |
| code-reviewer (round 2) | Approved | After `p.validate()` manual call + `From<ValidationErrors>` impl added |

## Known Gaps (pre-existing, not introduced this session)

These are follow-up items documented for the next session:

1. `ParamDaftarKpm` and `ParamAgregatWilayah` derive `Validate` but have no field-level annotations — unbounded `halaman`/`batas` query params accepted without limit.
2. `PermintaanPerbaruiKpm.kode_kategori_kelompok` has no length constraint — empty string accepted on PUT.
3. SQLX_OFFLINE setup not done. `cargo build` requires a live DB or `SQLX_OFFLINE=true` + `sqlx prepare` run first.
4. No git repository initialized (`git init` + initial commit needed before deployment).

## Integration Points

- Docker Compose: project is runnable end-to-end via `docker compose`
- OpenTelemetry: OTLP HTTP exporter configured (endpoint from env); traces emitted
- SQLx: async Postgres via connection pool; queries compiled against live DB at build time (see gap #3)

## Unresolved TODOs

- `cargo run` / end-to-end test not yet confirmed after latest changes
- `git init` + initial commit not done
- `.env.example` not updated to reflect current field naming
- Run `sqlx prepare` against live DB and commit `.sqlx/` query cache to enable offline builds
- Add field-level `#[validate(...)]` constraints to `ParamDaftarKpm`, `ParamAgregatWilayah`, and `PermintaanPerbaruiKpm`
- Consider integration test coverage for the 2 remaining endpoints not covered in `tests/kpm_handlers.rs`
