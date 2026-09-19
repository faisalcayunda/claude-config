# DQ Test Case — Tagging Dimensi & Severity + Standarisasi Deskripsi

Referensi lengkap untuk operasi §8 (SKILL.md). Baseline gaya & isi: **database `kpm_production`** (service `Prod DB - kpm_production`, mis. tabel `public.beneficiary`) — semua test case di sana sudah diberi tag `DataQualityDimension` + `DQSeverity` dan deskripsi format 3-bagian. Tugas skill: mereplikasi pola itu ke tabel/DB lain **tanpa halusinasi**.

## Daftar Isi
- A. Ruang lingkup & prasyarat
- B. Cara menemukan test case (enumerasi) — jangan pakai search
- C. Klasifikasi 1: `DataQualityDimension` (pilih tepat SATU)
- D. Klasifikasi 2: `DQSeverity` (pilih tepat SATU)
- E. Format deskripsi 3-bagian (baku kpm_production)
- F. Mekanik patch tag + deskripsi (mutually exclusive!)
- G. Alur end-to-end: 1 tabel & 1 DB penuh
- H. Contoh nyata dari `beneficiary` (verbatim)

---

## A. Ruang lingkup & prasyarat

Operasi ini memperkaya **test case data quality** yang sudah ada di OpenMetadata dengan tiga hal sekaligus per test case:
1. **Deskripsi** yang mudah dipahami (format 3-bagian, §E).
2. Tag **`DataQualityDimension.<X>`** — dimensi kualitas yang diukur test (§C).
3. Tag **`DQSeverity.<Y>`** — konsekuensi bisnis bila test gagal (§D).

Cakupan (tanyakan ke user bila belum jelas): **1 tabel** atau **semua tabel dalam 1 database**.

Prasyarat penting: test case-nya **sudah ada** di OpenMetadata (dibuat pipeline Great Expectations / testsuite-bot). Skill ini **tidak membuat** test case baru di sini — untuk itu lihat §6.7 SKILL.md. Fokus operasi ini: menandai & mendeskripsikan test case yang sudah ada.

Kedua classification (`DataQualityDimension`, `DQSeverity`) sudah ada di instance dan bersifat **`mutuallyExclusive: true`** → tiap test case wajib **tepat satu** tag dimensi dan **tepat satu** tag severity. Bila belum yakin classification-nya ada, konfirmasi: `get_entity_details(entityType="classification", fqn="DataQualityDimension")` dan `"DQSeverity"`.

---

## B. Cara menemukan test case (enumerasi)

⚠️ **`search_metadata(entityType="testCase")` TIDAK bisa diandalkan** — filter entity-nya diabaikan dan yang balik malah table/glossary. Jangan pakai itu untuk mencari test case.

Jalur yang benar: **table → testSuite → tests[]**.

```
# 1. Ambil detail tabel → baca referensi testSuite-nya
get_entity_details(entityType="table", fqn="<table_fqn>")
#    → field "testSuite": { "fullyQualifiedName": "<table_fqn>.testSuite", ... }

# 2. Buka testSuite → dapat SEMUA test case tabel itu di array "tests[]"
get_entity_details(entityType="testSuite", fqn="<table_fqn>.testSuite")
#    → tests[]: tiap elemen berisi { id, name, fullyQualifiedName, description }
#    → summary: ringkasan success/failed per kolom (berguna untuk konteks)
```

Dari `tests[]` ambil **`fullyQualifiedName` persis** tiap test case — itulah `fqn` untuk `get_entity_details(entityType="testCase", ...)` dan `patch_entity(entityType="testCase", ...)`. **Jangan rakit FQN manual.**

Pola FQN test case (buat referensi saja, tetap ambil dari `tests[]`):
- Test kolom: `<service>.<db>.<schema>.<table>.<column>.<testName>`
- Test tabel: `<service>.<db>.<schema>.<table>.<testName>`

**Untuk 1 DB penuh:** enumerasi dulu semua tabel di schema (`get_entity_details(entityType="databaseSchema", fqn="<schema_fqn>")` → daftar tabel), lalu untuk tiap tabel jalankan table → testSuite → tests[]. Tabel tanpa testSuite = tidak ada test case, lewati.

Untuk memutuskan dimensi/severity/`Cara perhitungan` dengan benar, baca juga **test definition** tiap test case (`get_entity_details(entityType="testCase", fqn=...)` mengembalikan `testDefinition.name` + `parameterValues`). Nama test definition (mis. `columnValuesToBeNotNull`, `columnValuesToBeInSet`, `tableCustomSQLQuery`) adalah petunjuk utama dimensi.

---

## C. Klasifikasi 1 — `DataQualityDimension` (pilih tepat SATU)

Klasifikasi BGN sesuai *Panduan Verifikasi Data Quality & DQ Reporting BGN v2.0*. Menjawab **"kualitas apa yang diukur"**. 5 dimensi + bobot resmi; **Accuracy sengaja tidak ada** di sini (di-handle evidence-based A0–A3 di luar skor otomatis).

| Dimensi | Tag FQN | Bobot | Tandai bila test memeriksa… | Test definition tipikal |
|---|---|---|---|---|
| Completeness | `DataQualityDimension.Completeness` | 0,25 | keberadaan nilai pada kolom **wajib** (NOT NULL / mandatory presence) | `columnValuesToBeNotNull`; custom SQL "NULL count" |
| Uniqueness | `DataQualityDimension.Uniqueness` | 0,25 | **ketunggalan** identifier / business key / PK; tidak ada duplikat/konflik identity | `columnValuesToBeUnique`, `columnValuesToBePrimaryKey`; custom SQL dedup |
| Validity | `DataQualityDimension.Validity` | 0,20 | kesesuaian nilai ke **standar**: tipe, format, panjang, domain/**enum**, **range**, **regex/pola**, **referential integrity (FK)**, cross-field-standard, privacy | `columnValuesToMatchRegex`, `columnValuesToBeInSet`, `columnValueLengthsToBeBetween`, `columnValuesToBeBetween`; custom SQL FK |
| Consistency | `DataQualityDimension.Consistency` | 0,10 | **keselarasan** antar-field / antar-tabel / antar-sistem / antar-waktu (mis. `updated_at >= created_at`, agregat master vs turunan, rekonsiliasi lintas sistem) | custom SQL cross-field/cross-table; `tableRowCountToEqual` vs sumber lain |
| Timeliness | `DataQualityDimension.Timeliness` | 0,05 | **kemutakhiran/ketibaan** data terhadap SLA (freshness lag, arrival batch, callback SLA) | `tableDataToBeFresh`, `tableFreshness`; custom SQL lag |

**Aturan pembeda yang sering bikin ragu** (dikonfirmasi dari data kpm_production nyata):
- **NOT NULL → Completeness** (bukan Validity). Contoh: `date_of_birth_not_null`, `gender_not_null`, `is_active_not_null`.
- **Enum/inSet & regex/format & range → Validity.** Contoh: `gender_known_values` (inSet L/P), `code_matches_format` (`^P[0-9]{10}$`), `fullname_min_length`.
- **"Tidak boleh di masa depan" pada SATU kolom vs `now()` → Validity** (aturan range dengan batas atas dinamis). Contoh nyata: `created_at_not_in_future`, `date_of_birth_not_in_future` → **Validity**.
- **Perbandingan antar-kolom dalam satu baris (a ≥ b) → Consistency** (cross-field), *walau* diimplementasikan sebagai custom SQL. Contoh nyata: `updated_at_after_created_at`, `deleted_at_after_created_at` → **Consistency**.
- **Referential integrity / FK (custom SQL "orphan") → Validity.** Contoh nyata: `institution_code_references_institution` → **Validity**. (Jangan tertukar ke Consistency — definisi Validity BGN memasukkan "referential integrity".)
- **Business rule layanan (mis. BVR-xxx) via custom SQL** → pilih dimensi menurut *apa yang dijaga*: FK/eksistensi rujukan → Validity; keselarasan antar entitas/agregasi → Consistency.

Jenis test bukan penentu tunggal — **custom SQL bisa jatuh ke Validity, Consistency, Completeness, dst.** tergantung isi aturannya. Baca `sqlExpression`-nya.

---

## D. Klasifikasi 2 — `DQSeverity` (pilih tepat SATU)

Menjawab **"apa akibatnya bila gagal"**. Severity adalah **gate, bukan bobot** — tidak masuk formula skor komposit; fungsinya memicu keputusan rilis (PASS / PASS WITH EXCEPTION / HOLD-QUARANTINE / REJECT).

> **Kewenangan:** penetapan severity adalah hak **Data Owner/Produsen Data per CDE** (Section 19), bukan keputusan teknis. Karena itu skill **mengusulkan** severity + alasan, lalu memasukkannya ke ringkasan konfirmasi batch untuk disetujui user (§G). Jangan perlakukan severity sebagai fakta objektif seperti dimensi.

| Severity | Tag FQN | Kriteria (kapan dipilih) | Efek keputusan & eskalasi |
|---|---|---|---|
| Critical | `DQSeverity.Critical` | kegagalan menghentikan layanan; risiko PDP tinggi; **salah sasaran penerima manfaat**; risiko **keamanan pangan**; **fraud/keuangan**; laporan pimpinan/regulator jadi salah | 1 test Critical **Failed → dataset Red → HOLD/QUARANTINE atau REJECT**, terlepas skor. Triase <4 jam. Waiver hanya via Governance Forum (L3) |
| High | `DQSeverity.High` | mengganggu operasi utama, dashboard strategis, integrasi penting, atau **CDE non-safety** | dataset **Amber → PASS WITH EXCEPTION / HOLD terbatas** + rencana remediasi. Triase <1 hari kerja; plan <2 hari. Eskalasi L2 Data Owner |
| Medium | `DQSeverity.Medium` | menurunkan usability/kerapian (format/enum pendukung, keselarasan timestamp, jejak pembuat) tanpa dampak langsung ke layanan | tidak menghentikan proses; backlog terjadwal. Triase <3 hari kerja. Eskalasi L1 Data Steward |
| Low | `DQSeverity.Low` | kosmetik, minor metadata, isolated issue risiko rendah (typo label, deskripsi kurang lengkap) | tidak memengaruhi status/keputusan rilis; dipantau sebagai tren |

**Heuristik usulan severity** (dari label nyata kpm_production — tetap butuh konfirmasi user):
- Kunci utama identitas, FK ke master yang menentukan **eligibility/kepesertaan**, NIK/UIN/NISN/NPSN, keuangan, keamanan pangan, aturan layanan SPPG-KPM (BVR) → **Critical**. Contoh: `institution_code_references_institution` = Critical.
- Kolom operasional inti **wajib** (NOT NULL `date_of_birth`) atau format kunci bisnis (`code`, `institution_code`) → **High**.
- Enum/format pendukung, urutan timestamp, pola kode sekunder → **Medium**. Contoh: `gender_known_values`, `created_at_not_in_future`, `updated_at_after_created_at` = Medium.
- Kosmetik/metadata → **Low**.

Catatan: **besarnya failedRows tidak menaikkan severity.** `updated_at_after_created_at` gagal ±45% tetap Medium karena akar masalahnya semantik ETL, bukan dampak layanan. Severity soal *konsekuensi*, bukan *jumlah*.

---

## E. Format deskripsi 3-bagian (baku kpm_production)

Setiap deskripsi test case ditulis dalam Bahasa Indonesia, ringkas, untuk pembaca non-teknis. Nama teknis (kolom, kode, pola) selalu di-`backtick`. Struktur:

```
**Apa yang dicek & kenapa penting:** <1 kalimat: apa yang divalidasi + alasan bisnisnya>

**Cara perhitungan:** <bahasa awam: apa yang dipindai, definisi failedRows, kondisi PASS>

⚠️ **Catatan:** <OPSIONAL — hanya bila ada anomali / EXPECTED FAIL / temuan yang perlu konteks>

_Dihitung oleh pipeline Great Expectations (SQL langsung di database produksi) dan hasilnya dikirim ke sini; OpenMetadata tidak mengeksekusi test ini sendiri._
```

- Dua bagian pertama **wajib**. Footer italic **wajib & verbatim** (persis kalimat di atas).
- `⚠️ **Catatan:**` dipakai bila ada anomali/EXPECTED FAIL (mis. muatan bulk, isu migrasi ETL, jumlah pelanggaran hasil profiling). Tulis singkat + status ("EXPECTED FAIL", "temuan riil", "sedang dieskalasi").

**Pustaka frasa "Cara perhitungan" per tipe test** (samakan dengan ini):
- **NOT NULL** (`columnValuesToBeNotNull`): "Seluruh baris dipindai di database; baris dengan `<col>` kosong (NULL) dihitung gagal. failedRows = jumlah baris kosong, passedRows = sisanya. PASS bila failedRows = 0."
- **Regex/format** (`columnValuesToMatchRegex`): "Setiap nilai `<col>` (baris NULL dilewati) dicocokkan dengan pola `<regex>`. failedRows = jumlah nilai yang tidak cocok pola. PASS bila 0."
- **Enum/inSet statis** (`columnValuesToBeInSet`): "Setiap nilai `<col>` (NULL dilewati) dicek keanggotaannya dalam daftar nilai sah: `<A>`, `<B>`. failedRows = nilai di luar daftar. PASS bila 0."
- **Enum dari master (dinamis)**: "Daftar nilai sah diambil LANGSUNG dari tabel master saat test berjalan (query: `<SELECT ...>`), lalu setiap nilai `<col>` (NULL dilewati) dicek keanggotaannya. failedRows = nilai yang tidak ada di master. PASS bila 0."
- **Panjang** (`columnValueLengthsToBeBetween`): "Panjang karakter setiap nilai `<col>` (NULL dilewati) dihitung; minimal `<n>` karakter. failedRows = nilai yang terlalu pendek. PASS bila 0."
- **Range/not-in-future** (`columnValuesToBeBetween`): "Setiap nilai `<col>` dibandingkan dengan `<batas>` (mis. waktu saat test dijalankan, now UTC — dihitung ulang tiap run). failedRows = nilai di luar rentang. PASS bila 0."
- **Cross-field ordering** (custom SQL `a < b`): "Per baris, `<a>` dibandingkan dengan `<b>`; baris dengan `<a>` lebih kecil dari `<b>` dihitung gagal. Baris yang salah satu nilainya kosong dilewati. failedRows = jumlah baris terbalik urutan. PASS bila 0."
- **FK / business rule** (`tableCustomSQLQuery`): "Aturan ini terlalu spesifik untuk test bawaan, jadi dihitung satu query SQL langsung di database (lihat sqlExpression pada test ini): query menghitung baris pelanggar aturan. failedRows = angka pelanggaran hasil query. PASS bila query tidak menemukan pelanggaran (0)."

Bila `computePassedFailedRowCount=false` / test agregat (custom SQL COUNT), tetap jelaskan "failedRows = angka pelanggaran hasil query" — jangan mengarang passedRows bila memang tidak dihitung.

---

## F. Mekanik patch — tag + deskripsi (perhatikan mutual-exclusivity)

Semua operasi lewat `patch_entity(entityType="testCase", fqn="<test_fqn>", patch="<JSON Patch string>")`.

**Wajib baca state dulu:** `get_entity_details(entityType="testCase", fqn=...)` → lihat `tags[]` saat ini. Karena `DataQualityDimension` & `DQSeverity` **mutuallyExclusive**, menambahkan tag dimensi/severity kedua akan konflik. Karena itu **rakit ulang seluruh array `/tags`** = (semua tag lama yang BUKAN dimensi/severity) + (dimensi baru) + (severity baru), lalu `replace`. Ini otomatis:
- menegakkan tepat-satu dimensi & tepat-satu severity,
- **mempertahankan** tag lain apa adanya: `Tier.*`, `DataSensitivity.*`, `PII.*`, dan link glossary term (`... - Data Vocabulary. ...`). Jangan hapus tag-tag ini.

Objek tag minimal untuk dimensi & severity (`source` HARUS `Classification`):
```json
{"tagFQN":"DataQualityDimension.<X>","source":"Classification","labelType":"Manual","state":"Confirmed"}
{"tagFQN":"DQSeverity.<Y>","source":"Classification","labelType":"Manual","state":"Confirmed"}
```

**Satu patch per test case** (deskripsi + tags sekaligus, lebih atomik):
```json
[
  {"op":"replace","path":"/description","value":"<deskripsi 3-bagian §E>"},
  {"op":"replace","path":"/tags","value":[
     {"tagFQN":"Tier.Tier1","source":"Classification","labelType":"Manual","state":"Confirmed"},
     {"tagFQN":"DataSensitivity.Restricted","source":"Classification","labelType":"Manual","state":"Confirmed"},
     {"tagFQN":"<...glossary term lama bila ada...>","source":"Glossary","labelType":"Manual","state":"Confirmed"},
     {"tagFQN":"DataQualityDimension.Validity","source":"Classification","labelType":"Manual","state":"Confirmed"},
     {"tagFQN":"DQSeverity.Medium","source":"Classification","labelType":"Manual","state":"Confirmed"}
  ]}
]
```
Catatan:
- Bila test case belum punya deskripsi sama sekali, `replace` `/description` tetap jalan; bila ditolak, pakai `op:"add"`.
- Bila memilih mode "hanya isi deskripsi kosong/generic", lewati `op` `/description` untuk test yang deskripsinya sudah format 3-bagian & jelas — tetap kerjakan tag-nya.
- Tag glossary term lama disalin **verbatim** (tagFQN & `source:"Glossary"`). Bila ragu isi field tag lama, ambil dari hasil `get_entity_details` dan salin apa adanya.
- `payload` `patch` adalah **string** berisi JSON array.

---

## G. Alur end-to-end

Model konfirmasi mengikut pilihan user. Default yang dipakai di sini: **penetapan dimensi otomatis (objektif), severity diusulkan; eksekusi setelah SATU konfirmasi batch** di akhir (bila user memilih mode lain — mis. konfirmasi dimensi & severity terpisah, atau konfirmasi per-tabel — sesuaikan).

### G.1 — Satu tabel
```
1. get_entity_details(table, <table_fqn>)              → ambil testSuite.fqn
2. get_entity_details(testSuite, <table_fqn>.testSuite) → ambil tests[] (semua FQN + deskripsi lama)
3. Untuk SETIAP test case:
   a. get_entity_details(testCase, <test_fqn>)   → testDefinition, parameterValues, tags lama, deskripsi lama
   b. Tetapkan dimensi (§C) — objektif dari apa yang dicek
   c. Usulkan severity (§D) + alasan singkat
   d. Susun deskripsi 3-bagian (§E), pertahankan catatan anomali bila ada
   e. Rakit 1 patch (deskripsi + /tags reassembled, §F)
4. Tampilkan TABEL RENCANA ke user: | test case | dimensi | severity (usulan) | deskripsi ada→baru | catatan |
5. Setelah user setujui (1x batch): jalankan patch_entity per test case
6. Laporkan: N test ditandai, rincian dimensi & severity, deskripsi yang diperbarui, yang dilewati
```

### G.2 — Satu DB penuh
```
1. Konfirmasi database + schema target
2. Enumerasi tabel (databaseSchema) → daftar tabel
3. Untuk tiap tabel: table → testSuite → tests[] (lewati tabel tanpa testSuite)
4. Untuk tiap test case: tetapkan dimensi + usulkan severity + susun deskripsi (seperti G.1.3)
5. Tampilkan RENCANA agregat (ringkas per tabel: jumlah test, distribusi dimensi & severity, contoh)
   — untuk DB besar, tampilkan ringkasan + tawarkan drill-down per tabel sebelum eksekusi
6. Setelah 1x konfirmasi batch: eksekusi patch per test case, urut per tabel
7. Laporan akhir: total test ditandai, distribusi dimensi (+bobot) & severity, deskripsi diperbarui, anomali yang perlu perhatian
```

Selalu tunduk pada Aturan Anti-Halusinasi (§2 SKILL.md): dimensi hanya dari daftar §C; severity hanya dari §D; jangan mengarang test definition/parameter — baca dari entity. Bila sebuah test tidak jelas dimensinya (mis. custom SQL ambigu), tandai `[PERLU KONFIRMASI dimensi: <alasan>]` di rencana dan minta arahan, jangan menebak.

---

## H. Contoh nyata dari `beneficiary` (verbatim — patokan gaya)

| Test case | testDefinition | Dimensi | Severity | Deskripsi (ringkas) |
|---|---|---|---|---|
| `date_of_birth_not_null` | columnValuesToBeNotNull | Completeness | High | "Tanggal lahir wajib terisi — dasar penghitungan umur…" |
| `gender_known_values` | columnValuesToBeInSet | Validity | Medium | "Nilai sah jenis kelamin hanya L dan P; '-' placeholder bulk…" + ⚠️ EXPECTED FAIL |
| `code_matches_format` | columnValuesToMatchRegex | Validity | (High) | "Kode PM (kunci utama) harus berpola P + 10 digit…" |
| `created_at_not_in_future` | columnValuesToBeBetween | Validity | Medium | "Waktu pembuatan record tidak masuk akal bila di masa depan…" |
| `updated_at_after_created_at` | tableCustomSQLQuery | Consistency | Medium | "Waktu terakhir diubah tidak boleh mendahului waktu dibuat…" + ⚠️ EXPECTED FAIL ±45% ETL |
| `institution_code_references_institution` | tableCustomSQLQuery | Validity | Critical | "PM yang menunjuk KPM harus menunjuk KPM yang benar-benar ada — dasar sahnya kepesertaan…" |

Contoh deskripsi lengkap (`gender_known_values`, verbatim baseline):
```
**Apa yang dicek & kenapa penting:** Nilai sah jenis kelamin hanya L dan P; tanda '-' adalah placeholder data bulk, bukan kategori.

**Cara perhitungan:** Setiap nilai `gender` (NULL dilewati) dicek keanggotaannya dalam daftar nilai sah: `L`, `P`. failedRows = nilai di luar daftar. PASS bila 0.

⚠️ **Catatan:** EXPECTED FAIL saat ini: ±5,7 juta baris (8%) masih '-' dari muatan bulk -- failedRows check ini adalah meteran kemajuan remediasi, bukan alarm baru.

_Dihitung oleh pipeline Great Expectations (SQL langsung di database produksi) dan hasilnya dikirim ke sini; OpenMetadata tidak mengeksekusi test ini sendiri._
```
