# [BE] Halaman Detail Layanan Internal service

## Context

Portal AdPem (INAGOV) butuh backend untuk **halaman detail layanan Internal service**: ringkasan JP, riwayat perolehan JP, pembelajaran aktif, detail perolehan JP + sertifikat, dan redirect "lanjut ke INTERNAL SERVICE". Spec = 7 grup AC (A Context/Source, B Ringkasan JP, C Riwayat, D Aktif, E Detail, F Redirect, G Error/Integrasi).

**Kenapa sekarang & apa yang sudah ada.** Connector Internal service sudah ada (`internal/modules/integration/connectors/internal_service/`) dan menarik `dashboard` + `courses/me` ke staging (`internal_service.summary`, `internal_service.courses`). Katalog Service sudah punya reachability probe + launch (`POST /v1/integration/services/{id}/access`, `GET /integration/services/{id}/launch`, migration 0050 `service_access`). Scaffolding HTTP/auth/error (huma + `apiresp` + `authz` + `apiquery`) sudah matang. Jadi ini terutama **sisi-baca (BFF)** di atas fondasi yang ada, plus penambahan tarikan diklat.

**Prinsip yang mengikat desain ini (anti-fabrikasi, aturan repo `docs/integration-pull-etl.md` §7 + BE-DETAIL-AC04/BE-HISTORY-AC04):** field yang tak ada sumbernya dikembalikan `null`/ditandai unavailable, tidak pernah dikarang. Kegagalan integrasi tidak pernah jadi `0` (BE-JP-AC08).

**Status verifikasi (live smoke test, 2026-09-15, kredensial dev dari user, tidak dipersist):** login `/auth/login` OK; `angkatan/filter` mengembalikan `[]` untuk user uji → **per-user scoping terkonfirmasi** (bukan katalog global); `dashboard`, `courses/me`, `courses/detail/:slug` (`uuidEnrollment`), `certificate-detail` semua 200 dengan shape sesuai. Dua temuan live tercermin di rencana ini (empty-string cert, float progress). Bentuk diklat terisi + sertifikat terbit masih sandar contoh docs (akun uji nyaris kosong).

## Keputusan terkunci

| # | Keputusan | Nilai |
|---|---|---|
| Q3 | Cakupan pull | Extend connector sesuai kebutuhan AC; field tanpa sumber → null/plan |
| Q4 | Surface API | Modul `internal_service` sendiri, path `/v1/internal_service/...` (pola modul `dashboard`/`profile`) |
| Q5 | Diklat | **Include** (`angkatan/filter`, per-user terkonfirmasi live) |
| Q6 | Model baca | **Hybrid**: list/summary dari staging; detail (E) + sertifikat **live on-demand** |
| Auth | AC01/02/03 | `apiresp.SessionSecurity` + scope kepemilikan via `authz.FromContext(ctx).UserID`/`.NIP`; identitas dari sesi, tak pernah dari client |
| F | Redirect | Reuse `access`/`launch` (whole-app; tak ada deep-link per-course di kontrak) |
| AC04 | Host allowlist | Env-driven allowlist di `core.ValidateServiceURL` (jalur bersama); list kosong = allow-all + warning di env prod-like |

**Tak ada sumber di mana pun (verifikasi grep + live) → null/plan, jangan dikarang:** RPL, target JP tahunan, bucket JP Ekosistem, asal-JP tiga-kategori penuh, masa berlaku + jenis dokumen sertifikat, status kelulusan umum (kecuali Latsar CPNS/PPPK via `swajar`).

## Peta data AC → sumber (terverifikasi)

| AC | Field | Sumber | Catatan |
|---|---|---|---|
| B | JP mandiri | `internal_service.summary.total_lesson_time` | tahunan, reset Jan (API doc 3.2.5); **bukan** "JP Diakui" penuh |
| B | JP diklat + Total | Σ `internal_service.diklat.jp` (baru) | diklat = penyumbang JP terbesar |
| B | kategori | Mandiri=courses, Wajib≈diklat, **Ekosistem=null** | 2/3 bucket derivable |
| B | RPL, target, % | — | `null`; target `20` konstanta **tidak** ditampilkan sebagai data |
| C | riwayat mandiri | `internal_service.courses` (staging, sudah ada) | status=done |
| C | riwayat diklat | `internal_service.diklat` (baru), `tanggalSelesai < now` | nama/lemdik/jp/tanggal/guid |
| C | tanggal pengakuan | mandiri→null (tak ada di `courses/me`); diklat→`tanggal_selesai` | jangan pakai tanggal lain |
| C | asal JP | coarse: Mandiri vs Diklat (derived) | tiga-kategori penuh tak tersedia |
| D | aktif mandiri | `internal_service.courses` (progress<100 / !isDone) | tenggat mandiri = null |
| D | aktif diklat | `internal_service.diklat` (`tanggalSelesai >= now`) | tenggat = `tanggal_selesai` |
| D | status/progres | `is_done` + `progress` bareng | progress bisa 100 tapi isDone false → jangan simpulkan dari satu atribut (BE-ACTIVE-AC03) |
| E | deskripsi/JP/progres | live `courses/detail/:slug` (`courses.description` juga ada di courses/me) | |
| E | sertifikat | live `certificate-detail/:uuidEnrollment` | `""` → null; pakai `statusSertifikat` |
| E | preview dok | live proxy `files/view/certificate?fileName={pathSertifikat}` | biner PDF, via token user |
| E | jenis dok, masa berlaku | — | `null` |
| F | launch + allowlist | reuse `access`/`launch` + allowlist | whole-app |

**Linkage id:** `courses/me` **tak** membawa `uuidEnrollment`; harus `courses/detail/:slug` dulu untuk dapat enrollment id, baru `certificate-detail`. Karena itu **sertifikat = milik endpoint detail (E), live**, bukan list (N+1). Dunia diklat (`angkatan/filter`) terpisah dari dunia mandiri (tak ada id nyambung).

## Modul & endpoint baru

Modul baru `internal/modules/internal_service/` mengikuti struktur `internal/modules/dashboard/` (facade `internal_service.go` → `internal/core/handler.go` + `service.go` + `repository.go`; `RegisterRoutes(_, api)` → `handler.Register(api)`). Semua `Security: apiresp.SessionSecurity`, identitas via `authz.FromContext`, guard `UserID`/`NIP` kosong → 401 (pola `callerUserID`).

1. `GET /v1/internal_service/summary` (B) — DTO: `total_jp *int`, `jp_by_category {mandiri *int, wajib *int, ekosistem *int(null)}`, `rpl *int(null)` + `rpl_included:false`, `target_jp *int(null)` + `percentage *float(null)`, `source {name, synced_at *time.Time}`. Pointer + pola `hasData` untuk bedain 0 valid vs unavailable (BE-JP-AC07).
2. `GET /v1/internal_service/history` (C) — paginated via `apiquery.List[stagingRow, historyDTO]` gabungan mandiri+diklat; search server-side (pg_trgm), filter `jenis` (mandiri/diklat) & `asal_jp`, intersection, kosong → `[]` (BE-HISTORY-AC09). Record: `id`, `jenis`, `nama`, `penyedia`, `tanggal_pengakuan *time.Time`, `jp`, `asal_jp`, `source`.
3. `GET /v1/internal_service/active-learning` (D) — list sortable by `tenggat`; item: `id`, `jenis`, `nama`, `penyedia`, `tenggat *time.Time`, `jp_program`, `jp_recognition_status *string(null)`, `status`, `progress`, `capability {can_open_portal:false, continue_in_internal_service:bool, accessible:bool}`.
4. `GET /v1/internal_service/learning/{id}` (E) — **live**; `id` = course `slug` (mandiri) atau `guid_angkatan` (diklat). Ownership dijamin karena panggilan upstream pakai token user (`isEnroll`). DTO: `status`, `penyedia`, `deskripsi`, `jp_diakui`, `jp_program`, `progres`, `jenis`, `certificate {jenis_dokumen:null, nomor *string(""→null), tanggal_terbit *string(""→null), masa_berlaku:null, status, preview_available:bool}`. Bedakan selesai vs bisa dilanjutkan via `is_done`/`progress`/`modules` (BE-DETAIL-AC05).
5. `GET /v1/internal_service/learning/{id}/certificate` (E, BE-DETAIL-AC06) — **proxy stream PDF** lewat BFF pakai token koneksi user (`files/view/certificate?fileName={pathSertifikat}`); hanya bila `isEnroll` + `pathSertifikat` ada + `statusSertifikat`="Terbit". Tak pernah kasih URL upstream mentah ke client.

**Redirect (F): tidak ada endpoint baru** — reuse `POST /v1/integration/services/{id}/access` (probe + redirect_url) & `GET /integration/services/{id}/launch`.

## Perubahan connector & schema

**`internal/modules/integration/connectors/internal_service/`:**
- Tambah pull `GET /dashboard-profile/api/profile/angkatan/filter` (bare array) → upsert `internal_service.diklat`; land raw ke `raw_pull` (ScopeA). Delete-replace per user (pola `persist()` yang ada).
- **Fix bug laten**: `courseItem.Progress` & `Course.Progress` decode `int` → ganti `float64` (live kirim `0.0`), simpan `int(math.Round(...))` di staging. Verifikasi apakah sync existing sudah error pada float sebelum patch.
- `dashboard`/`courses/me` tetap seperti sekarang. Detail (E) + sertifikat **tidak** ditarik ke staging.

**Client upstream live (detail + sertifikat):** ekstrak client kecil Internal service (login → `courses/detail/:slug`, `certificate-detail/:enr`, `files/view`) yang dipakai modul `internal_service` read-path; kredensial user didekripsi lewat mesin koneksi/`buildTarget` yang ada (`internal/modules/integration/target.go` + vault). Timeout eksplisit (mis. 10-15s), envelope 3-gaya (auth `{code}`, trans `{status}`, learning unwrapped) di-branch per endpoint.

**Migration baru `migrations/00NN_internal_service_diklat.up.sql`** (+ down): tabel `internal_service.diklat` (`user_nip`, `guid_angkatan` PK bersama `user_nip`, `guid_diklat`, `nama_diklat`, `nama_angkatan`, `nama_lemdik`, `alamat`, `daerah`, `jp int`, `tanggal_mulai timestamptz null`, `tanggal_selesai timestamptz null`, `synced_at`). Ikuti pola `internal_service.courses` di `0019_baseline`. GORM AutoMigrate hanya untuk mirror lokal (gated `SCHEMA_AUTOMIGRATE`).

## Keamanan, error, host allowlist

- **Host allowlist (BE-REDIRECT-AC04):** tambah cek allowlist host di `core.ValidateServiceURL` (`internal/modules/integration/internal/core/url.go`), sumber env (mis. `INTEGRATION_ALLOWED_HOSTS`, comma-sep) di `internal/config/config.go`. List kosong = allow-all (staging disposable) + `slog.Warn` di env prod-like. Berlaku untuk semua service launch/probe (jalur bersama).
- **Error contract (G):** semua via `apiresp.OK/Error/Fail/NotFound/DBError`. Bedakan kelas (BE-ERROR-AC05): no-data → `[]`/`null` sukses; upstream unreachable → `Fail(...502/503 BAD_GATEWAY/SERVICE_UNAVAILABLE)`; timeout → kelas tersendiri; internal → 500. `Fail` log cause server-side saja; client dapat pesan aman (BE-ERROR-AC01/02). Reuse higiene yang ada: `httpx` tanpa query string, Sentry scrub nik/nip/sub/cookie/Authorization, kredensial `json:"-"` (BE-ERROR-AC04). Retry = request baru (stateless) → BE-ERROR-AC06 otomatis.
- **Capability (D-AC05):** derived, bukan payload. `accessible=false` bila service tak published/active atau tak ada Connection (status≠connected) atau host tak lolos allowlist; `continue_in_internal_service=true` bila connected + destinasi valid; `can_open_portal=false` (portal tak render course).
- **Source metadata (A-AC05):** `synced_at` staging + `connections.last_synced_at`/`last_error`.

## File utama

- Baru: `internal/modules/internal_service/{internal_service.go, internal/core/{handler.go, service.go, repository.go, dto.go, live_client.go}}`.
- Baru: `migrations/00NN_internal_service_diklat.{up,down}.sql`.
- Ubah: `internal/modules/integration/connectors/internal_service/{connector.go, model.go}` (pull diklat + fix float progress).
- Ubah: `internal/modules/integration/internal/core/url.go` + `internal/config/config.go` (host allowlist).
- Ubah: `cmd/portal-adpem-backend/main.go` (daftar modul `internal_service.New(...)`), `internal/modules/integration/target.go`/connection service bila client live perlu akses kredensial.
- Reuse: `internal/platform/{apiresp, authz, apiquery, httpx, rawpull}`, pola modul `internal/modules/dashboard/`.

## Verifikasi

1. **Unit/integration**: repo test terhadap Postgres CI (`make migrate-up`) — history filter/search/intersection + empty→`[]`; summary 0-vs-null; capability rules; connector decode diklat + float progress; empty-string cert → null.
2. **Live smoke (ulang, di jaringan gov/VPN)**: skrip yang sudah dipakai (login → angkatan/filter → dashboard → courses/me → detail → certificate-detail) untuk konfirmasi shape diklat terisi + cert terbit pada akun yang punya data. Kredensial via `!` prompt, jangan dipersist.
3. **Manual**: `GET /v1/internal_service/{summary,history,active-learning,learning/{id}}` dengan sesi ASN nyata; redirect via `access` + cek host allowlist tolak host non-allowlist.
4. **Lint**: `golangci-lint run ./...` sebelum merge (bukan required check).

## Di luar scope / follow-up

- RPL, target JP tahunan ber-sumber, bucket Ekosistem, status kelulusan diklat umum, masa berlaku/jenis dokumen sertifikat: butuh endpoint upstream yang belum ada.
- Deep-link per-course ke INTERNAL SERVICE (kontrak hanya whole-app SSO).
- Status kelulusan Latsar CPNS/PPPK via `swajar/getcoursebytoken`: bisa jadi enrichment berikutnya (akun uji kosong, shape terisi belum terverifikasi live).
- Update wiki `concepts/Portal AdPem data connectors.md` (inventory 23 endpoint, envelope, linkage, per-user angkatan/filter terkonfirmasi) — dilakukan setelah keluar plan mode.
