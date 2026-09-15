# Kontrol lanjutan: 7 rule section baru (schemas, functions, procedures, queries, impersonation, authorization, system_information)

## Context

Bug report: `CREATE FUNCTION` kena Access Denied. Ditelusuri sampai ke fakta bahwa Trino's `rules.json` punya 9 top-level section yang diakui (`domain/rules.py::TOP_LEVEL_KEYS`), tapi CMS ini cuma mengelola 2: `catalogs` dan `tables`. Diverifikasi ke dokumentasi resmi Trino: section `functions` (dan `procedures`/`system_information`/`authorization`/`impersonation`) DEFAULT MENOLAK SEMUA kalau section-nya absen sama sekali dari rules.json — kebalikan dari `catalogs`/`tables`/`schemas`/`queries` yang default mengizinkan semua kalau absen. Rules.json lokal kita memang tidak punya section `functions` sama sekali, jadi bug-nya bukan salah konfigurasi, itu perilaku default Trino sendiri.

Diverifikasi empiris ke Trino 481 (container lokal, fork terpisah): rule `functions` beneran ditegakkan Trino (bukan sekadar tercatat di layar tapi tidak berlaku, kesalahan yang jadi asal-usul seluruh proyek ini). `OWNERSHIP` dan `EXECUTE` adalah privilege TERPISAH, bukan hierarki: bikin fungsi tidak otomatis dapat izin menjalankannya.

Digrill habis dengan pemilik (banyak ronde, semua keputusan di bawah sudah dikonfirmasi eksplisit):
- Bangun ketujuh section sekaligus (bukan bertahap), full CRUD, sekarang.
- Numpang di modul Kebijakan lewat SATU sub-tab baru "Kontrol lanjutan" (bukan 7 sub-tab terpisah), dengan sub-navigasi internal ke 7 section.
- Antrean/apply SENDIRI (bukan numpang `rule_op` atau `catalog_op`), tapi WAJIB pakai advisory lock KUNCI YANG SAMA (`RULES_KEY = "rules.json"`) dengan antrean aturan yang sudah ada, karena keduanya menulis file yang sama.
- Health check + auto-rollback sama persis seperti tables/catalogs, tidak dikecualikan.
- Tiap section menampilkan banner default-absen yang BENAR per section (sebagian absen=izinkan semua, sebagian absen=tolak semua — harus jelas, tidak boleh disamakan).
- Deteksi rule yang saling menutup (shadow), gaya badge TERBAYANGI di `/rules`, dibangun sekarang juga untuk ketujuh section, bukan ditunda.

Riset lanjutan (setelah janji awal ke pemilik soal fallback yang lebih longgar untuk functions/procedures): dicek langsung `domain/resolver.py::table_universe()`, ternyata universe konkretnya diturunkan dari NILAI LITERAL yang sudah tertulis di rule-rule yang ADA di section itu sendiri (`literalize()`), bukan dari metadata warehouse eksternal. Mekanisme ini generalisasi bersih ke ketujuh section baru tanpa fallback yang dikorbankan presisinya — kabar lebih baik dari yang disampaikan ke pemilik saat grilling, akan dikoreksi saat serah terima.

## Arsitektur

### Tiga kelompok bentuk rule (diverifikasi field-per-field ke dokumentasi Trino)

- **Kelompok A "resource + privilege"**: `schemas` (user/role/group/catalog/schema + `owner`:bool), `functions` (+`function`, `privileges`:list dari EXECUTE/GRANT_EXECUTE/OWNERSHIP), `procedures` (+`procedure`, `privileges`:list dari EXECUTE/GRANT_EXECUTE). Satu model+spec generik, pola `ConnectorSpec`/`CONNECTOR_SPECS`/`BY_CONNECTOR` (`services/catalogs.py:169-224,296-322`) sebagai contoh: dataclass frozen kecil + tuple/dict literal sumber kebenaran, bukan registry class.
- **Kelompok B "pasangan identitas"**: `impersonation` (original_user/original_role/new_user + `allow`:bool), `authorization` (original_user/original_group/original_role/new_user/new_role + `allow`:bool). Model sendiri, tidak ada dimensi catalog/schema sama sekali.
- **Kelompok C "toggle global"**: `queries` (user/role/group/queryOwner + `allow`:list dari execute/view/kill), `system_information` (user/role + `allow`:list dari read/write). Model sendiri, paling kecil.

### Data & antrean

Satu tabel ORM baru, `advanced_op` (mirror `RuleOp`/`CatalogOp`, lihat `infrastructure/orm.py`): `id`, `section` (str: "schemas"|"functions"|...), `kind` (str: "tambah"|"sunting"|"hapus"), `payload` (Text, JSON, TIDAK terenkripsi — rule-rule ini tidak membawa credential seperti antrean katalog, jadi tidak perlu enkripsi Fernet), `label` (str, ringkasan buat ditampilkan di panel antrean), `author`, `error`, `created_at`. Repository `AdvancedOpRepository` mirror persis `RuleOpRepository`/`CatalogOpRepository` (`infrastructure/repositories.py`): `add`/`pending`/`get`/`delete`, generik, tidak hardcode per section.

### Domain: shadow-detection generalisasi

Modul baru `domain/advanced_resolver.py`. Pola sama seperti `domain/resolver.py::rule_matches`/`table_universe`/`find_shadowing` (baca full di file itu untuk state exact), TIGA varian sesuai kelompok:
- Kelompok A: `resource_universe(rules, resource_fields)` — turunkan tuple konkret dari `literalize()` atas field-field resource (catalog/schema/nama) SEPERTI `table_universe`, generik lewat daftar nama field per section (bukan hardcode `catalog`/`schema`/`table`).
- Kelompok B/C: universe identitas dari GABUNGAN dua sumber: (1) nilai literal yang sudah ada di rule-rule section itu sendiri (pola sama), (2) `TrinoAccountRepository(session).all()` (`infrastructure/repositories.py:224-285`) untuk cakupan lebih lengkap daripada cuma yang kebetulan sudah ditulis.
- SEMUA varian mewarisi aturan yang sudah ada: rule yang pakai `group`/`role` (bukan `user` literal) dianggap TIDAK COCOK untuk tujuan analisis (`resolver.py` baris 60-61, komentarnya: "supaya analisis tidak pernah melaporkan rasa aman palsu") — jangan diubah, generalisasi verbatim.

### Validasi (gates)

`ALL_GATES` (`validation/gates.py`) saat ini cuma tahu section `"catalogs"`/`"tables"` lewat `.sections` masing-masing gate; `PolicyService.validate(..., only_sections=frozenset({"schemas"}))` sekarang akan menjalankan NOL gate untuk section baru (celah nyata, ditemukan saat baca `validate()` full). Dua perbaikan:
1. `StructureGate` (G1) checknya SUDAH generik (cek `TOP_LEVEL_KEYS` + `REQUIRED_SECTIONS` atas SELURUH `raw`, sudah menoleransi 7 key baru sejak awal), tapi `.sections = ("tables", "catalogs")`-nya bikin gate ini TIDAK ikut jalan kalau `only_sections` cuma berisi section baru. Perbaikan: tambahkan ketujuh section baru ke `StructureGate.sections`.
2. Gate baru per kelompok (bukan per section, biar tidak 7x): `ResourceRuleGate` (privilege/enum & shape sah untuk kelompok A), `IdentityRuleGate` (kelompok B), `ToggleRuleGate` (kelompok C). Masing-masing `.sections` diisi persis section-section kelompoknya, `blocking = True`.

### Service

`services/advanced_rules.py`, class `AdvancedRulesService(session: Session, settings: Settings)` — signature identik `PolicyService.__init__` (`services/policy.py:128-135`). Method utama `apply_advanced_ops(author: str) -> dict`, MIRROR PERSIS `PolicyService.apply_rule_ops` (baris 675-754, baca full sebelum menulis): `with advisory_lock(self._session, RULES_KEY):` (import `RULES_KEY`/`advisory_lock` dari `services/policy.py`/`infrastructure/database.py`, JANGAN bikin kunci baru), fold antrean FIFO, validasi per-op lewat `self.validate(disk, candidate, only_sections=frozenset({op.section}))` (reuse `PolicyService.validate`, jadi `AdvancedRulesService` butuh instance `PolicyService` juga atau method `validate`/`disk_document`/`disk_text` dipindah ke fungsi bersama yang keduanya pakai — pilih opsi TERMUDAH: `AdvancedRulesService` menerima `policy: PolicyService` di constructor dan delegasikan `disk_document`/`validate` ke situ, bukan duplikasi logic), SATU penulisan `atomic_write` + SATU health check untuk seluruh batch, versi + audit (`self.audit.record(author, "lanjutan.terapkan", ...)`).

### Routes

File baru `web/routes/advanced.py`, `router = APIRouter()` TANPA prefix (konvensi terverifikasi: SEMUA router di proyek ini `APIRouter()` polos, path absolut per route, lihat `web/app.py`). Path: `/advanced` (landing + sub-nav ke 7 section), `/advanced/{section}` (daftar rule section itu + panel antrean), `/advanced/{section}/new`, `/advanced/{section}/{index}/edit`, `/advanced/{section}/{index}/delete`, `/advanced/ops/apply`, `/advanced/ops/{op_id}/discard`, `/advanced/ops/discard-all`. Daftarkan di `web/app.py`: tambah `advanced` ke import `from .routes import (...)` dan `app.include_router(advanced.router)`.

Deps baru di `web/deps.py` (pola `get_policy_service`/`PolicyDep`, baris 34-38): `get_advanced_service(session: SessionDep, settings: SettingsDep, service: PolicyDep) -> AdvancedRulesService` (inject `PolicyDep` juga karena `AdvancedRulesService` delegasikan ke situ) + `AdvancedDep = Annotated[...]`.

### Templates

Bukan 7 template bespoke — 3 template generik (satu per kelompok), tiap satu dipakai ulang untuk section-section sekelompoknya, di-parameterisasi dari spec (pola `_connector_reqs()`/`_editable_props()` di `web/routes/catalogs.py`). Plus 1 halaman landing `/advanced` (sub-nav ke 7).

Mirror UI dari `rules.html` (baca full, sudah dibaca sekali, state exact struktur di riset): `.rule-row`+`data-search`+`data-filter-input`/`data-filter-status`+`data-reorder`+`data-confirm` semua JS-nya SUDAH ADA di `app.js`, tidak perlu JS baru. Panel antrean `<section class="section-card" id="antrean-lanjutan">` mirror struktur `#antrean` di `rules.html` (baris 86-130), actionbar mirror pola mutually-exclusive di `{% block actionbar %}`.

Wiring sub-tab: tambah `('/advanced', 'Kontrol lanjutan')` ke literal `tabs = [...]` di TUJUH template yang include `_module_tabs.html` (`access.html`, `catalog_rules.html`, `publish.html`, `rule_detail.html`, `rules.html`, `simulate.html`, `tables.html`) — tidak ada satu sumber terpusat, memang copy-paste per template (dikonfirmasi lewat grep), representative: `rules.html:6,8`. Halaman-halaman di bawah `/advanced` set `active_tab = '/advanced'` sebelum include, pola `catalog_rules.html:5,7`.

Banner default-absen per section (pola `catalogs.html`'s banner Vault-belum-dikonfigurasi): teks BEDA per section sesuai fakta terverifikasi --- absen=izinkan (`catalogs`/`schemas`/`tables`/`queries`) vs absen=tolak (`functions`/`procedures`/`system_information`/`authorization`/`impersonation`).

### i18n & audit

Semua string baru masuk `web/i18n.py` (ID key, EN value), ikuti konvensi `test_i18n.py` (literal `t("...")` di template ke-scan otomatis; pesan lewat `_back(...)` literal juga ke-scan; hindari pola dict-literal-ke-`page()` yang jadi celah sebelumnya, lihat perbaikan `Terjadi kesalahan`/dkk sesi ini). Audit action baru: `lanjutan.terapkan`, `lanjutan.antrean-buang`, ditambah action per section kalau perlu detail (`skema.terapkan`, `fungsi.terapkan`, dst) -- putuskan saat implementasi, ikuti pola `katalog.hapus`/`aturan.terapkan` yang sudah ada.

## Testing

- `tests/test_advanced_resolver.py` (tanpa DB, pola `test_resolver.py`/`test_catalog_queue.py`): shadow-detection generik untuk ketiga kelompok, termasuk kasus rule pakai `group`/`role` dianggap tidak cocok.
- `tests/test_advanced_http.py` (butuh Postgres, copy fixture PERSIS dari `test_access_http.py`/`test_users_http.py` termasuk `TRUNCATE` list -- WAJIB tambah `advanced_op` ke situ, pelajaran dari kelalaian yang sama sebelumnya di sesi ini): create/edit/delete per kelompok, antrean-lalu-terapkan, held-back saat gate gagal, shadow badge muncul di halaman.
- `tests/test_gates.py`: tambahan gate baru (`ResourceRuleGate`/`IdentityRuleGate`/`ToggleRuleGate`) plus `StructureGate.sections` yang diperluas.

## Verifikasi

`uv run pytest` dan `uv run ruff check src tests` (butuh `docker run --rm -d --name cms-test -e POSTGRES_PASSWORD=uji -p 55432:5432 postgres:16-alpine` untuk test HTTP). Cek manual lewat `python src/trino_cms serve --reload` (JANGAN Docker, instruksi CLAUDE.md 2026-08-12): buka `/advanced`, tambah satu rule `functions` lewat CMS, verifikasi rules.json lokal berubah, opsional verifikasi ke Trino container lokal (pola yang sama dipakai fork riset sebelumnya) kalau mau bukti end-to-end sampai ke enforcement Trino-nya, bukan cuma sampai rules.json.
