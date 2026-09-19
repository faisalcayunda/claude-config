---
name: openmetadata-catalog-manager
description: "Membaca, mendokumentasikan, dan memperkaya entitas OpenMetadata (tabel, kolom, glossary term, klasifikasi/tag, lineage, data quality test case, RCA) tanpa halusinasi, mengikuti pola Glosarium Data Vocabulary level Data Product & baseline yang ada. Picu saat pengguna menyebut OpenMetadata/Collate, dokumentasi/deskripsi tabel-kolom, link glossary term ke kolom, tag PII/sensitivity/tier, lineage, root cause analysis DQ, patch metadata, dokumentasi schema massal (batch), atau menyalin pola antar database. Picu JUGA untuk tag & deskripsi data quality test case — menandai test case dengan DataQualityDimension (Completeness/Uniqueness/Validity/Consistency/Timeliness) & DQSeverity (Critical/High/Medium/Low) untuk satu tabel atau semua tabel dalam satu database, plus menstandarkan deskripsi test case agar mudah dipahami, termasuk testSuite atau menyamakan pola test case dengan kpm_production. Picu JUGA saat MCP OpenMetadata mati/error/\"connection closed\" — skill auto-fallback ke REST API + script bila token tersedia."
---

# OpenMetadata Catalog Manager

Skill ini adalah jembatan antara user dengan **MCP Server OpenMetadata embedded** (`openmetadata-mcp-stateless` v0.11.2, OpenMetadata ≥ 1.12). Tugasnya: membantu user membaca, memperkaya, dan menstandarkan metadata di katalog OpenMetadata, sambil **menjaga konsistensi penuh** dengan terminologi yang sudah ada di Glosarium **level Data Product** — bukan menciptakan kosakata baru.

Mengapa konsistensi penting? **Sejak Juli 2026, tiap Glosarium Data Vocabulary berada di level Data Product — bukan lagi level Domain.** Artinya: **satu data product = satu glosarium**, mencakup seluruh tabel milik data product itu — yang bisa **tersebar di lebih dari satu database**. Glosarium data product tersebut adalah **single source of truth** untuk semantik data product-nya. Setiap deskripsi tabel/kolom baru yang menyimpang dari pola itu akan merusak Federated Data Governance dan menyebabkan ambiguitas lintas data product. Skill ini secara aktif mencegah penyimpangan tersebut.

> **Pembagian tugas (PENTING).** Pembuatan *wadah* Glosarium level Data Product (`create_glossary`) adalah **tanggung jawab user** — user yang membuat glosarium beserta struktur & profilnya. **Tugas skill ini: mengisi glossary term ke dalam glosarium data product yang sudah dibuat user**, lalu menautkannya (link) ke kolom. Bila glosarium data product target belum ada, skill **berhenti** dan meminta user membuatnya dulu (lihat §0 dan §12) — skill tidak membuat wadah glosarium data product secara otomatis kecuali user memintanya eksplisit.

---

## 0. Pre-Flight — WAJIB sebelum operasi apa pun

Saat skill diaktifkan, lakukan urutan ini sebelum tool call apa pun ke OpenMetadata:

0. **Cek ketersediaan MCP lebih dulu — sebelum langkah 1–4 di bawah.** Pastikan ke-12 tool MCP OpenMetadata (§1) benar-benar aktif, bukan cuma terdaftar namanya. Cara termurah: bila ada akses ke info status MCP server (mis. `get_device_info` di lingkungan dengan remote-devices), cek entri server bernama OpenMetadata — status `failed`/`disconnected`/tidak muncul sama sekali berarti mati, tanpa perlu mencoba tool dulu. Kalau tidak ada akses ke info status itu, lakukan satu panggilan ringan (`search_metadata` dengan query kecil) sebagai probe. Bila error koneksi muncul (mis. "Connection closed", timeout, ECONNREFUSED, tool tidak dikenali sistem), **jangan retry berkali-kali** — cukup satu percobaan ulang untuk menyingkirkan kemungkinan gangguan sesaat.

   Begitu MCP dipastikan mati: cek apakah ada kredensial REST API OpenMetadata yang bisa dipakai — env var host+token (biasanya di file `.env` folder kerja project aktif), atau tanyakan langsung ke user bila tidak ketemu. **Bila kredensial tersedia → langsung beralih ke Mode Fallback REST API + Script (§1a) tanpa menunggu user memerintahkan secara eksplisit**, cukup beri tahu singkat bahwa kamu beralih mode dan kenapa (MCP mati). **Bila kredensial tidak tersedia → berhenti**, laporkan ke user bahwa MCP mati dan skill butuh salah satu dari: MCP diperbaiki, atau kredensial API (host + token) diberikan.

1. **Tanyakan target ke user dengan presisi.** Minimal yang harus diketahui sebelum bekerja:
   - **Data Product target** — nama & kode data product (mis. `Operasional Distribusi` / `operasional-distribusi`, domain `DIS`) beserta domain induknya. Ini yang menentukan glosarium mana yang diisi.
   - Database FQN target (contoh: `Replica Prod DB - prod_siptrack_primary_siptrackdb_prod_readonly.prod_siptrack_primary_siptrackdb_prod`). **Catat semua database** bila data product mencakup lebih dari satu DB.
   - Schema target (contoh: `backend`)
   - Mode operasi: **READ** (inspeksi), **WRITE-SINGLE** (1 entitas), atau **BATCH-SCHEMA** (semua tabel dalam 1 schema)
   - **Glosarium Data Product** yang menjadi rujukan gaya bahasa sekaligus target pengisian term. Format nama: `<domain_code> - <data_product_name> - Data Vocabulary` (mis. `DIS - Operasional Distribusi - Data Vocabulary`). **Dibuat oleh user, bukan oleh skill.**

   Gunakan tool `AskUserQuestion` bila konteks ambigu. Jangan menebak service name — service OpenMetadata sering punya prefix manusiawi seperti "Replica Prod DB - …" yang **tidak bisa diturunkan** dari nama database saja.

2. **Resolusi FQN.** Selalu konfirmasi FQN target dengan `search_metadata` lebih dulu:
   ```
   search_metadata(query="<schema-or-table-name>", entityType="<table|databaseSchema>", size=10)
   ```
   Ambil persis `fullyQualifiedName` dari hasil. JANGAN merakit FQN manual — segmen dengan `-` atau `.` perlu dikutip dan rakitan manual sering salah.

3. **Verifikasi glosarium Data Product target hidup.** Resolusi dulu via `search_metadata(query="<data_product_name>", entityType="glossary")`, lalu ambil FQN persisnya:
   ```
   get_entity_details(entityType="glossary", fqn="<domain_code> - <data_product_name> - Data Vocabulary")
   # contoh: get_entity_details(entityType="glossary", fqn="DIS - Operasional Distribusi - Data Vocabulary")
   ```
   Bila glosarium data product ini **tidak ditemukan**, **berhenti** — pembuatan wadah glosarium adalah tanggung jawab user. Minta user membuatnya dulu dengan konvensi nama `<domain_code> - <data_product_name> - Data Vocabulary`, baru skill mengisi term-nya. Jangan buat wadah glosarium otomatis kecuali user memintanya eksplisit (lihat §12).

4. **Untuk operasi WRITE: ambil state dulu.** JSON Patch RFC 6902 bekerja relatif terhadap state aktual. Patch entity tanpa membaca state dulu berisiko meng-overwrite isi orang lain. Selalu `get_entity_details` sebelum `patch_entity`.

---

## 1. Inventarisasi MCP Tool yang Tersedia

Skill ini hanya boleh memakai 12 tool resmi berikut. **Jangan mengarang nama tool**, jangan menebak parameter. Bila MCP mati (§0 langkah 0), 12 tool ini tetap jadi rujukan definisi operasi — hanya cara memanggilnya yang berubah, lihat padanan REST-nya di **§1a**.

### Discovery (READ)
| Tool | Kegunaan |
|---|---|
| `search_metadata` | Pencarian keyword + faceted (entityType, owners, tags, tier). Default size 10, max 50. Pakai untuk semua resolusi FQN. |
| `semantic_search` | Pencarian berdasarkan makna (vector embedding). Pakai bila user mendeskripsikan konsep, bukan menyebut nama. Butuh OpenSearch + embedding provider aktif (≥ 1.12). |
| `get_entity_details` | Detail penuh entity berdasarkan `entityType` + `fqn`. Wajib dipanggil sebelum patch apa pun. |
| `get_entity_lineage` | Upstream/downstream dependencies. Default depth 3, max 10. Untuk asset dengan graf > 500 node, set depth ≤ 2 agar tidak meluap. |

### Governance (WRITE)
| Tool | Kegunaan |
|---|---|
| `patch_entity` | Update entity via JSON Patch (string array RFC 6902). Path umum: `/description`, `/tags/-`, `/owners/-`, `/columns/<idx>/description`, `/columns/<idx>/tags/-`. |
| `create_glossary` | Buat glossary baru. **Default: pembuatan wadah glosarium level Data Product adalah tugas user, bukan skill** — pakai tool ini hanya bila user eksplisit minta skill membuatkan wadah. Field wajib: `name`, `description`, `mutuallyExclusive`. |
| `create_glossary_term` | **Operasi glossary utama skill ini.** Tambah term ke glosarium Data Product yang **sudah dibuat user**. Wajib: `glossary` (FQN), `name`, `description`. `parentTerm` opsional untuk hierarchical (mis. `.Entri Kosakata` / `.Validation Rules`). |
| `create_metric` | Buat metric entity (formula SQL/Python/Java/LaTeX). |

### Lineage (READ + WRITE)
| Tool | Kegunaan |
|---|---|
| `create_lineage` | Buat relasi lineage manual. **Butuh UUID + type** kedua sisi (ambil dari `get_entity_details`, bukan FQN). |

### Data Quality (READ + WRITE)
| Tool | Kegunaan |
|---|---|
| `get_test_definitions` | List test definitions tersedia. **Wajib panggil sebelum `create_test_case`** untuk verifikasi `parameterValues` schema. `entityType` = `TABLE` atau `COLUMN`. |
| `create_test_case` | Buat DQ test. `fqn` selalu FQN tabel; untuk column-test isi `columnName`. |
| `root_cause_analysis` | Analisis RCA lewat lineage traversal. Pakai saat user melaporkan kegagalan DQ atau anomali. |

> **Menandai & mendeskripsikan test case yang SUDAH ada** (dimensi + severity + deskripsi mudah dipahami) memakai `get_entity_details` (entityType `table` → `testSuite` → `testCase`) lalu `patch_entity(entityType="testCase", ...)`. Lihat **§8**. Catatan: `search_metadata(entityType="testCase")` **tidak reliabel** untuk menemukan test case — pakai jalur testSuite.

---

## 1a. Mode Fallback — REST API + Script (bila MCP OpenMetadata mati)

Dipicu otomatis oleh §0 langkah 0 ketika MCP mati **dan** kredensial API tersedia. Semua logika skill di luar mekanisme pemanggilan tool **tidak berubah** — pre-flight (§0), Aturan Anti-Halusinasi (§2), template deskripsi (§3–§4), kewajiban konfirmasi sebelum WRITE (Aturan 3), dan seluruh alur operasi (§5–§9) tetap berlaku persis sama. Yang berbeda **hanya** cara memanggil OpenMetadata: lewat REST API (`curl` atau `requests`/`urllib` Python) memakai `OM_HOST` (base URL API, mis. `https://<domain>/api`) + `OM_TOKEN` (Bearer token bot/personal access token) — bukan lewat 12 MCP tool di §1.

**Prinsip kunci — resolve dulu via search, jangan rakit path manual.** Sama seperti §0 langkah 2 melarang merakit FQN manual, di mode fallback selalu `GET /v1/search/query` dulu untuk dapat `id` (UUID) entity, baru pakai `id` itu untuk semua operasi berikutnya. Jangan coba tebak `/name/{fqn}` manual — FQN yang mengandung spasi, tanda kutip, atau tanda hubung (mis. `Replica Prod DB - prod_siptrack_...`) gampang salah encode dan gagal diam-diam.

### Mapping 12 Tool MCP → Endpoint REST

Tabel berikut **sudah diverifikasi langsung** terhadap instance OpenMetadata 1.12.x target (bukan tebakan dari dokumentasi umum):

| Tool MCP | Endpoint REST | Catatan |
|---|---|---|
| `search_metadata` / `semantic_search` | `GET /v1/search/query?q=<query>&index=<entityType>_search_index&size=<n>` | Nama index ikut pola `<entityType>_search_index` — contoh terverifikasi: `table_search_index`, `glossary_term_search_index`, `test_case_search_index`. Hasil ada di `hits.hits[]._source.id` (juga `._id`). Kualitas semantic ranking tergantung embedding provider di server — bila tidak aktif, hasilnya setara text search biasa; jangan janjikan hasil semantik ke user tanpa verifikasi. |
| `get_entity_details` | `GET /v1/<entityTypePlural>/{id}` | Ambil `id` dari search dulu (lihat prinsip kunci di atas). Plural umum: `tables`, `glossaries`, `glossaryTerms`, `databaseSchemas`, `databases`, `teams`. |
| `get_entity_lineage` | `GET /v1/lineage/{entityType}/{id}?upstreamDepth=<0-3>&downstreamDepth=<0-3>&includeDeleted=<bool>` | `entityType` singular lowercase (`table`, `dashboard`, dst). Default depth 1 bila parameter dikosongkan — selalu set eksplisit. |
| `patch_entity` | `PATCH /v1/<entityTypePlural>/{id}` | **Wajib** header `Content-Type: application/json-patch+json` (bukan `application/json` biasa — tanpa ini request ditolak atau diam-diam tidak berefek). Body = JSON Patch array RFC 6902, format identik dengan payload `patch_entity` MCP di §6–§8, tidak perlu diubah. |
| `create_glossary` | `POST /v1/glossaries` | Body: `{name, description, mutuallyExclusive, owners?, reviewers?}` — sama seperti argumen MCP. |
| `create_glossary_term` | `POST /v1/glossaryTerms` | Body: `{glossary, name, description, parentTerm?}` — sama seperti argumen MCP. |
| `create_metric` | `POST /v1/metrics` | **Belum diverifikasi live.** Coba `GET /v1/metrics?limit=1` dulu sebagai probe sebelum WRITE pertama; bila 404, berhenti dan laporkan ke user daripada menebak path lain. |
| `create_lineage` | `PUT /v1/lineage` | Body: `{"edge":{"fromEntity":{"id":"<uuid>","type":"table"},"toEntity":{"id":"<uuid>","type":"table"}}}` — pakai `id` (UUID dari `get_entity_details`), bukan FQN, sama seperti versi MCP (§6.6). |
| `get_test_definitions` | `GET /v1/dataQuality/testDefinitions?entityType=TABLE\|COLUMN&limit=<n>` | **Prefix `dataQuality/` wajib** — `GET /v1/testDefinitions` polos (tanpa prefix) mengembalikan 404 di instance ini. |
| `create_test_case` | `POST /v1/dataQuality/testCases` | **Wajib field `entityLink`**, bukan `fqn`+`columnName` polos seperti di MCP. Format DSL: `<#E::table::<table_fqn>>` untuk table-level, `<#E::table::<table_fqn>::columns::<col_name>>` untuk column-level — contoh nyata terverifikasi: `<#E::table::Replica Prod DB - prod_mysql_sipscm_primary_sipscmdb_prod.prod_mysql_sipscm_primary_sipscmdb_prod.sipscmdb_prod.order_transaction::columns::admin_fee>`. **Selalu ambil pola ini dari satu test case existing dulu** (`GET /v1/dataQuality/testCases/{id}`) sebelum menyusun `entityLink` baru — jangan menebak sintaksnya (Aturan Anti-Halusinasi §2 berlaku sama). Endpoint enumerasi: `GET /v1/dataQuality/testCases/search/list`. |
| `root_cause_analysis` | **Tidak ada endpoint REST publik yang terverifikasi tersedia.** | Fitur ini tampaknya eksklusif MCP/UI (AI-assist). Di mode fallback, dekati manual: `get_entity_lineage` upstream + cek `testCaseStatus` tiap test case di tabel-tabel upstream (lewat `testSuite` → `dataQuality/testCases`) untuk menyusun narasi RCA sendiri sesuai pola §9.2. **Wajib informasikan ke user** bahwa RCA otomatis tidak tersedia di mode fallback dan hasilnya adalah analisis manual, bukan output tool RCA. |

### Aturan Tambahan Khusus Mode Fallback

- **Aturan Anti-Halusinasi (§2) berlaku identik.** Mode fallback bukan alasan untuk menebak nama field/endpoint/parameter. Endpoint yang belum diverifikasi di tabel atas (mis. `create_metric`) wajib dicoba dengan satu `GET` ringan dulu; kalau dapat 404/405, berhenti dan laporkan ke user daripada mencoba variasi path lain berulang-ulang.
- **Urutan pencarian kredensial**: (1) env var `OM_HOST`/`OM_TOKEN` (atau nama serupa) di shell/`.env` folder kerja project aktif, (2) nama umum lain (`OPENMETADATA_HOST_PORT`, `OPENMETADATA_JWT_TOKEN`, dst.) di file konfigurasi project lain, (3) tanyakan langsung ke user via `AskUserQuestion` bila tidak ketemu di manapun. Jangan pernah menampilkan token secara penuh di output — cukup konfirmasi beberapa karakter awal saat melapor token ditemukan.
- **403 saat WRITE biasanya soal scope token, bukan endpoint salah.** Token bot OpenMetadata sering di-scope read-only atau read+limited-write. Bila POST/PATCH/PUT ditolak `403`, laporkan ke user sebagai kemungkinan masalah izin token — jangan asumsikan path-nya salah dan mencoba path lain.
- **MCP mati sering berarti ada masalah konfigurasi di server**, bukan cuma soal jaringan — pola umum yang terlihat: field `href` pada response API menunjuk ke `http://localhost:8585/...` alih-alih domain publik, tandanya setting `openMetadataUrl` server masih default. Setelah tugas di mode fallback selesai, **ingatkan user** bahwa ini akar masalah yang idealnya dibenerin oleh admin OpenMetadata (Settings → Preferences → OpenMetadata URL, atau config server) — mode fallback adalah workaround sementara, bukan pengganti permanen.

---

## 2. Aturan Anti-Halusinasi (Wajib Patuh)

Tiga aturan berikut adalah landasan keandalan skill ini:

**Aturan 1 — Terminologi hanya dari glosarium.** Sebelum menulis deskripsi kolom, atau memasang glossary term ke kolom, **wajib** cek glosarium dulu:

```
search_metadata(query="<nama-field-atau-konsep>", entityType="glossaryTerm", size=5)
```

Bila ada term yang cocok (mis. kolom `current_status` → `DIS - Operasional Distribusi - Data Vocabulary.Entri Kosakata.current_status`), pakai term tersebut sebagai sumber definisi. Jangan menulis ulang definisi dari pengetahuan umum. Bila tidak ada term yang cocok, **jangan menciptakan istilah baru** — tulis `[PERLU VERIFIKASI: tidak ada term cocok untuk <field>, tolong tinjau/buat term di glosarium dulu]` dan tandai untuk review user.

**Aturan 2 — Style mengikuti baseline.** Pola deskripsi tabel dan kolom mengikuti baseline `backend.task` (lihat §3). Pola deskripsi glossary term mengikuti baseline term di `Entri Kosakata` / `Validation Rules` (lihat §4).

**Aturan 3 — Tidak ada operasi WRITE tanpa konfirmasi user.** Sebelum panggil `patch_entity`, `create_glossary_term`, `create_lineage`, atau `create_test_case`, tampilkan rencana perubahan (entity, field, before → after) dan minta persetujuan eksplisit. Untuk mode BATCH, tunjukkan ringkasan rencana lintas tabel sebelum dieksekusi.

---

## 3. Pola Deskripsi Tabel & Kolom — Template Kanonik

Template berikut diekstrak dari baseline `Replica Prod DB - prod_siptrack_primary_siptrackdb_prod_readonly.prod_siptrack_primary_siptrackdb_prod.backend.task`. Semua deskripsi tabel baru di domain Distribusi (dan secara default, domain lain bila user tidak meminta gaya berbeda) **harus** mengikuti template ini.

### 3.1 Template Deskripsi Tabel

```
<paragraf bisnis 1–2 kalimat: apa yang disimpan tabel ini, satu baris merepresentasikan apa>

**Grain:** 1 baris per <key> (<format key, mis. UUID v4>)

**Layer:** Bronze — Transactional Source   ← pilih: Bronze | Master | Archive | Event Log | Silver | Gold
                                            sesuai posisi tabel di medallion

**Volume:** ~<N> baris (per <tanggal snapshot>). Pertumbuhan ~<rate>

**Diperbarui:** Real-time | Daily batch | Sync dari <sistem> | Append-only event log

⚠️ <Data Quality Issues / anomali yang dipertahankan / pitfalls> ← optional, tapi wajib bila profiling menemukan masalah
```

**Contoh real dari baseline `task`:**
> Tabel fakta task pengiriman aktif (transactional fact). Satu baris = satu trip pengiriman dari kitchen SPPG ke titik food_receiver. Snapshot tabel ini mewakili task yang **belum di-archive** (yang sudah dihapus berpindah ke `task_deleted`).
>
> **Grain:** 1 baris per `task_id` (UUID v4)
>
> **Layer:** Bronze — Transactional Source
>
> **Volume:** ~1.171 baris aktif (per 13 Mei 2026). Pertumbuhan ~250 task/hari di fase pilot Jabodetabek + Bali
>
> **Diperbarui:** Real-time saat task lifecycle berjalan (`Dispatched` → `Pickup` → `Delivered` → `Reviewed`)

### 3.2 Template Deskripsi Kolom

Deskripsi kolom adalah 1–2 kalimat singkat (80–160 karakter), bukan paragraf. Detail panjang (enum lengkap, regex, SQL constraint) dibiarkan di glossary term — kolom hanya **menunjuk** ke glossary term yang sudah ada.

Struktur kalimat:
```
<Definisi singkat>. <Range/enum/aturan kondisional/PII flag>. Sumber: <App | Keycloak | Dapodik | EMIS | Master KPPG | …>.
```

**Contoh real dari baseline:**
- `task_id`: "UUID v4 — business key task pengiriman. Dipakai untuk join ke `task_history`, `task_food_safety`, dan integrasi DWH. Sumber: App-generated."
- `current_status`: "Status terkini task dalam siklus hidup pengiriman. Default `Dispatched`. Urutan wajib: Dispatched → Pickup → Delivered → Reviewed. Sumber: App."
- `receiver_name`: "Nama penerima makanan yang menandatangani e-BAST (PII). NULL saat status < Delivered. Wajib di-mask di laporan eksternal. Sumber: App (input mobile)."

Catatan gaya: nama teknis (kolom, tabel, kode enum) selalu dalam `backtick`. Kalimat formal-teknis Bahasa Indonesia. Hindari kalimat panjang berklausa banyak.

### 3.3 Wajib pasangkan Tag + Glossary Link

Untuk setiap kolom yang di-patch, default sertakan **3 hal**:

1. **Sensitivity classification** — pilih satu dari `DataSensitivity.Public`, `DataSensitivity.Internal`, `DataSensitivity.Restricted` (custom org), atau `DataSensitivity.Confidential` bila tersedia. Default `DataSensitivity.Internal` untuk operasional internal.
2. **PII tag** — bila kolom mengandung data pribadi: `PII.NonSensitive`, `PII.Sensitive`. Bila bukan: skip.
3. **Glossary term link** — FQN glossary term (di glosarium **level Data Product**) yang menjelaskan field tersebut (mis. `DIS - Operasional Distribusi - Data Vocabulary.Entri Kosakata.current_status`). Source: `Glossary`.

Bila glossary term belum ada untuk field tersebut, **tandai `[PERLU VERIFIKASI: glossary term hilang untuk <field>]`** — jangan tulis description column dengan tebakan, dan jangan paksa link ke term yang tidak relevan.

---

## 4. Pola Glossary Term — Template Kanonik

Bila user ingin menambah glossary term baru ke glosarium **level Data Product**, ikuti pola dari baseline data vocabulary yang sudah ada (mis. glosarium lama `Domain Distribusi - Data Vocabulary`, atau glosarium data product baru). Ada dua varian: **Entri Kosakata** (untuk atribut bertipe enum) dan **Validation Rules** (untuk atribut non-enum).

Ingat lingkupnya: **satu glosarium = satu data product**, dan satu data product berisi banyak tabel yang **bisa tersebar di lebih dari satu database**. Karena itu, baris **Tabel:** pada sebuah term boleh mencantumkan beberapa tabel lintas schema/DB (mis. `db_a.backend.task`, `db_b.public.task_archive`) selama semuanya milik data product yang sama.

### 4.1 Template Term — Entri Kosakata (atribut enum)

```markdown
**Document ID:** `VOC-<DOMAIN>-<DP>-<FIELD-UPPER-DASH>` | Tabel: `<db>.<schema>.<table>[, <db2>.<schema>.<table2>, …]`

| Metadata | Nilai |
|---|---|
| Nama Field | `<col_name>` |
| Tipe Data | `<postgres_type>` |
| Nullable | Ya / Tidak |
| Klasifikasi | Public / Internal / 🟡 Restricted / 🔴 Confidential |
| PII | NULL / <kategori PII> |
| Regulasi | <Juknis MBG 2026 Bab X / UU PDP 27/2022 / RFC NNNN / …> |
| Sumber | <SIPGN Distribusi (siptrackdb_prod) / Keycloak / Dapodik / …> |
| SCD Type | 0 / 1 / 2 |

<paragraf narasi bisnis 1–3 kalimat menjelaskan makna field>

**Nilai Valid (Enum)** — profiling <N> baris:

| Kode | Display Name | % | Definisi |
|---|---|---|---|
| `<Code>` | <Indonesian display> | XX,X% | <Definisi singkat> |
| … | … | … | … |

<aturan urutan / catatan anomali bila ada>

```sql
ALTER TABLE <schema>.<table>
    ADD CONSTRAINT chk_<col>
    CHECK (<col> IN ('<A>','<B>',...));
```
```

### 4.2 Template Term — Validation Rules (atribut non-enum)

```markdown
**Document ID:** `VOC-<DOMAIN>-<DP>-<FIELD-UPPER-DASH>` | Tabel: `<db>.<schema>.<table>[, <db2>.<schema>.<table2>, …]`

| Metadata | Nilai |
|---|---|
| Nama Field | `<col_name>` |
| Tipe Data | `<postgres_type>` |
| Nullable | Ya / Tidak |
| Klasifikasi | Public / Internal / 🟡 Restricted / 🔴 Confidential |
| PII | NULL / <kategori> |
| Regulasi | <referensi> |
| Sumber | <sumber otoritatif> |

<paragraf narasi singkat>

**1. Format (Regex)**

| Atribut | Nilai |
|---|---|
| Pattern | `<regex>` |
| Contoh Valid | `<example>` |
| Contoh Invalid | `<example>` |

**2. Length / Range / FK / Cross-field rules** ← pilih yang relevan

```sql
ALTER TABLE <schema>.<table>
    ADD CONSTRAINT chk_<col>_format
    CHECK (<col> ~ '<regex>');
```
```

### 4.3 Konvensi Penamaan Term

- **Nama Glosarium (level Data Product)**: `<domain_code> - <data_product_name> - Data Vocabulary` (mis. `DIS - Operasional Distribusi - Data Vocabulary`). `domain_code` & `data_product_name` diambil dari Master Sheet Data Product. **Wadah glosarium ini dibuat user; skill hanya mengisi term.**
- **Document ID prefix (komposit domain + data product)**: `VOC-<DOMAIN>-<DP>-<FIELD-UPPER-DASH>`, di mana `<DOMAIN>` = `domain_code` (mis. `DIS`) dan `<DP>` = `data_product_code` di-UPPER-DASH (mis. `operasional-distribusi` → `OPERASIONAL-DISTRIBUSI`). Contoh lengkap: `VOC-DIS-OPERASIONAL-DISTRIBUSI-CURRENT-STATUS`. **Selalu cek pola `VOC-` yang sudah ada** di glosarium target lewat `search_metadata(query="VOC-", entityType="glossaryTerm")` dulu — bila tim sudah memakai mnemonic tertentu (mis. `FLEET` untuk Distribusi), ikuti yang sudah ada demi konsistensi.
- **Name term**: snake_case mengikuti nama kolom (mis. `current_status`, `task_id`), kecuali term konseptual yang bukan kolom (mis. `pii_password`, `geo_coordinates` — kelompok field).
- **Bahasa**: Bahasa Indonesia formal-teknis. Nama teknis di `backtick`. Display name Indonesia (mis. `Dispatched` → "Dikirim").
- **Klasifikasi 4 level**: `Public`, `Internal`, `🟡 Restricted`, `🔴 Confidential`. Emoji disertakan persis seperti baseline.

### 4.4 Sebelum Create — Cek Duplikasi

Selalu cek dulu apakah term sudah ada:
```
search_metadata(query="<field_name>", entityType="glossaryTerm")
```
Bila ada hit di glosarium yang sama, **jangan create duplikat** — pakai yang ada atau usulkan update via `patch_entity`.

---

## 5. Operasi: READ — Inspeksi

Pakai pola ini untuk semua skenario "kasih tahu saya …" / "apa isi …" / "siapa pemilik …".

### 5.1 Inspeksi 1 Tabel

```
1. search_metadata(query="<table_name>", entityType="table", size=5)
2. Ambil fullyQualifiedName dari hasil yang user maksud
3. get_entity_details(entityType="table", fqn="<fqn>")
4. Sajikan ringkasan: deskripsi, owner, tier, jumlah kolom, kolom-kolom yang belum terdokumentasi, glossary term yang sudah/belum terhubung
```

### 5.2 Inspeksi Schema (semua tabel)

```
1. search_metadata(query="<schema_name>", entityType="databaseSchema", size=3)
2. get_entity_details(entityType="databaseSchema", fqn="<schema_fqn>")
3. Untuk setiap tabel di response → catat FQN, displayName, status deskripsi
4. Sajikan tabel ringkasan: nama tabel | desc tabel ada/tidak | jumlah kolom | kolom tanpa desc
```

Untuk skema dengan banyak tabel, **jangan langsung get_entity_details semua** — output bisa meluap. Tampilkan dulu ringkasan, lalu user pilih tabel mana yang ingin di-drill-down.

### 5.3 Inspeksi Lineage / RCA

```
get_entity_lineage(entityType="table", fqn="<fqn>", upstreamDepth=2, downstreamDepth=2)
```
Untuk root cause:
```
root_cause_analysis(entityType="table", fqn="<fqn>", upstreamDepth=3)
```
Sajikan sebagai ringkasan node yang relevan, bukan dump full graph.

---

## 6. Operasi: WRITE — Single Entity

### 6.1 Update Deskripsi Tabel

```
1. get_entity_details(entityType="table", fqn="<fqn>")  ← baca state dulu
2. Susun deskripsi mengikuti Template §3.1
3. Konfirmasi rencana ke user (tampilkan before → after)
4. patch_entity(entityType="table", fqn="<fqn>",
       patch='[{"op":"replace","path":"/description","value":"<deskripsi-baru>"}]')
```

Bila tabel belum punya deskripsi sama sekali, gunakan `add` bukan `replace`:
```json
[{"op":"add","path":"/description","value":"..."}]
```

### 6.2 Update Deskripsi & Tag Kolom

Index kolom diambil dari urutan `columns[]` di response `get_entity_details`. Hitung 0-based.

```json
[
  {"op":"replace","path":"/columns/5/description","value":"<deskripsi-kolom>"},
  {"op":"add","path":"/columns/5/tags/-","value":{
      "tagFQN":"DataSensitivity.Internal","labelType":"Manual","state":"Confirmed","source":"Classification"
  }},
  {"op":"add","path":"/columns/5/tags/-","value":{
      "tagFQN":"DIS - Operasional Distribusi - Data Vocabulary.Entri Kosakata.task_type",
      "labelType":"Manual","state":"Confirmed","source":"Glossary"
  }}
]
```

Catatan: `source` harus `Classification` untuk tag classification (PII/Tier/DataSensitivity) dan `Glossary` untuk link glossary term — keliru sumber → tag tidak muncul di UI dengan benar.

### 6.3 Add Tier ke Tabel

```json
[{"op":"add","path":"/tags/-","value":{
   "tagFQN":"Tier.Tier1","labelType":"Manual","state":"Confirmed","source":"Classification"}}]
```

### 6.4 Set Owner (sejak 1.5.0 field-nya `owners` array)

```json
[{"op":"add","path":"/owners/-","value":{"id":"<uuid>","type":"team"}}]
```

UUID team/user diambil dari `search_metadata(query="<name>", entityType="team")` → `get_entity_details`.

### 6.5 Buat Glossary Term Baru (ke glosarium Data Product)

> **Prasyarat:** wadah glosarium Data Product sudah dibuat **oleh user** (§0 langkah 3). Bila belum ada, berhenti dan minta user membuatnya — skill tidak membuat wadah otomatis (§12). Bila parent group `Entri Kosakata` / `Validation Rules` belum ada di glosarium itu, konfirmasi ke user lalu buat sebagai term induk dulu.

```
0. Pastikan glosarium Data Product target ada & ambil FQN persisnya (§0).
1. search_metadata(query="<field>", entityType="glossaryTerm")  ← cek duplikasi (§4.4)
2. Bila tidak ada: susun description mengikuti Template §4.1 atau §4.2 (Document ID komposit, §4.3)
3. Konfirmasi ke user
4. create_glossary_term(
       glossary="DIS - Operasional Distribusi - Data Vocabulary",
       parentTerm="DIS - Operasional Distribusi - Data Vocabulary.Entri Kosakata",   ← atau Validation Rules
       name="<field_name>",
       description="<isi-template>"
   )
```

### 6.6 Buat Lineage Manual

```
1. get_entity_details(entityType="table", fqn="<from_fqn>")  → ambil id (UUID)
2. get_entity_details(entityType="table", fqn="<to_fqn>")    → ambil id (UUID)
3. create_lineage(
       fromEntity={"type":"table","id":"<uuid_from>"},
       toEntity  ={"type":"table","id":"<uuid_to>"}
   )
```

### 6.7 Buat Data Quality Test Case

```
1. get_test_definitions(entityType="COLUMN"|"TABLE")  ← baca dataType yang didukung
2. Klasifikasikan test ke kategori ROWS / Custom SQL / Binary-only (lihat Tabel 6.7-A)
3. Untuk Custom SQL: rewrite SQL dari COUNT ke SELECT * (lihat §6.8)
4. Susun parameterValues lengkap + strategy yang tepat
5. Konfirmasi rencana ke user (Aturan 3, §2)
6. create_test_case(
       name="<test_name>",
       fqn="<table_fqn>",
       columnName="<col_name>",          ← optional, untuk column-level
       entityType="table",
       testDefinitionName="<def_name>",
       parameterValues=[{"name":"<p>","value":"<v>"}],
       description="<konteks-singkat>"
   )
```

**Tabel 6.7-A — Klasifikasi Strategy per Test Definition:**

| Kategori | Test Definitions | Behaviour | Tindakan |
|---|---|---|---|
| **Row-level** | `columnValuesToBeNotNull`, `columnValuesToMatchRegex`, `columnValuesToNotMatchRegex`, `columnValuesToBeBetween`, `columnValuesToBeInSet`, `columnValuesToBeNotInSet`, `columnValuesLengthsToBeBetween`, `columnValuesToBeUnique`, `columnValuesToBePrimaryKey`, `columnValuesInTableColumnExist` | Otomatis menghasilkan `passedRows` + `failedRows` — tidak perlu parameter tambahan | Tidak perlu set strategy — OpenMetadata evaluasi per-baris secara native |
| **Custom SQL** | `tableCustomSQLQuery` | Default binary (COUNT); dengan `strategy: ROWS` menghasilkan `passedRows`/`failedRows` | **Wajib set `strategy: ROWS`** + rewrite SQL (§6.8) |
| **Binary-only** (inherent) | `tableRowCountToBeBetween`, `tableRowCountToEqual`, `tableRowInsertedCountToBeBetween`, `tableColumnCountToBeBetween`, `tableColumnCountToEqual`, `tableColumnNameToExist`, `tableColumnToMatchSet`, `columnValuesSumToBeBetween`, `columnValuesMeanToBeBetween`, `columnValuesMedianToBeBetween`, `columnValueStdDevToBeBetween`, `columnValueMaxToBeBetween`, `columnValueMinToBeBetween`, `tableFreshness`, `tableDataToBeFresh`, `tableDataToBeFreshQuery` | Mengukur agregat atau schema — tidak ada "baris yang gagal" yang bisa dikembalikan. Hasilnya selalu binary Success/Failed | Biarkan binary — ini bukan bug, ini by-design |

Bila `parameterValues` schema-nya tidak jelas, **berhenti dan tanya user** — jangan menebak parameter; test case dengan parameter salah akan jalan tapi hasilnya tidak bermakna.

---

### 6.8 Custom SQL — Wajib Strategy ROWS + SQL Rewrite

Untuk `tableCustomSQLQuery`, **selalu gunakan `strategy: ROWS`** agar OpenMetadata bisa menghasilkan `passedRows` dan `failedRows`. Ini membutuhkan SQL yang mengembalikan **baris yang melanggar aturan** — bukan angka COUNT.

**Pattern SQL yang menghasilkan binary-only (❌ hindari):**
```sql
-- SQL ini mengembalikan satu angka → hanya binary Success/Failed
SELECT COUNT(*) FROM backend.location 
WHERE location_id IS NOT NULL AND location_id NOT LIKE '%.%'
```

**Pattern SQL yang menghasilkan passedRows + failedRows (✅ wajib pakai):**
```sql
-- SQL ini mengembalikan baris yang melanggar → OpenMetadata hitung failedRows + passedRows
SELECT * FROM backend.location 
WHERE location_id IS NOT NULL AND location_id NOT LIKE '%.%'
```

Logika internal OpenMetadata dengan strategy ROWS:
- `failedRows` = COUNT baris yang dikembalikan SQL
- `passedRows` = total baris tabel − failedRows
- Test **Fail** bila failedRows > threshold

**Aturan rewrite:**
1. Ganti `SELECT COUNT(*)` → `SELECT *` (atau `SELECT <kolom_kunci>` untuk tabel besar)
2. Pertahankan kondisi `WHERE` apa adanya — kondisi ini mendefinisikan baris yang melanggar
3. Jangan tambahkan `HAVING`, `GROUP BY`, atau agregat lain
4. Bila SQL asli berisi `WHERE kondisi_valid` (bukan kondisi gagal), **inversi kondisinya**: `WHERE NOT (kondisi_valid)`

**`parameterValues` untuk custom SQL dengan ROWS:**
```json
[
  {"name": "sqlExpression", "value": "SELECT * FROM <schema>.<tabel> WHERE <kondisi_baris_gagal>"},
  {"name": "strategy",      "value": "ROWS"},
  {"name": "threshold",     "value": "0"}
]
```
`threshold: 0` artinya nol baris boleh gagal (zero-tolerance). Sesuaikan bila ada toleransi bisnis (mis. `"5"` = maksimal 5 baris boleh melanggar).

**Kasus edge — SQL tidak bisa dikonversi ke ROWS:**
Bila SQL memang mengukur agregat atau properti tabel (bukan per-baris), gunakan `strategy: COUNT` dan biarkan binary. Contoh yang tetap binary karena tidak ada "baris gagal" yang bisa dikembalikan:
```sql
-- Ini mengukur proporsi NULL pada seluruh tabel — inherently aggregate
SELECT COUNT(*) FROM backend.task WHERE current_status IS NULL
-- → lebih baik diganti dengan test definition columnValuesToBeNotNull (row-level native)
```
Bila memungkinkan, **prefer test definition native** (row-level) daripada custom SQL untuk kasus yang sudah ada definisinya.

---

## 7. Operasi: BATCH-SCHEMA — Dokumentasi Massal Satu Schema

Mode ini dipakai untuk skenario "dokumentasikan semua tabel di schema `backend`" atau "samakan style dengan `prod_siptrack`". Baseline kanonik: schema `prod_siptrack_primary_siptrackdb_prod.backend` (lihat baseline tabel `task` sebagai patokan utama, dan tabel lain di schema yang sama sebagai sumber sekunder).

### 7.1 Alur Batch

```
Step 1 — Resolve target
  1.1 Konfirmasi database + schema target ke user
  1.2 search_metadata + get_entity_details(databaseSchema) → daftar tabel

Step 2 — Audit baseline
  2.1 Daftar tabel sudah ada di schema target (FQN, has_desc, jumlah kolom, kolom tanpa desc)
  2.2 Tampilkan ke user — minta konfirmasi cakupan (semua / subset)

Step 3 — Drill-down per tabel (sequential, agar tidak meluapkan context)
  Untuk SETIAP tabel terpilih:
    a. get_entity_details(entityType="table", fqn=<tbl_fqn>)
    b. Catat: kolom mana yang sudah ada di glosarium (via search_metadata
       per kolom yang menarik, atau lookup batch list term di Entri Kosakata + Validation Rules)
    c. Susun draft patch:
       - Description tabel (mengikuti Template §3.1)
       - Per kolom: description (Template §3.2) + tag sensitivity + glossary link (Template §3.3)
    d. Untuk kolom yang TIDAK ada glossary term-nya:
       tandai [PERLU VERIFIKASI: belum ada glossary term untuk <field>] —
       JANGAN paksakan, jangan buat term baru tanpa persetujuan eksplisit
    e. Tampilkan ringkasan diff per tabel ke user (jumlah field yang akan di-update,
       glossary link yang akan dipasang, gap yang perlu review)

Step 4 — Eksekusi
  4.1 User setujui per-tabel atau bulk
  4.2 patch_entity per tabel (idealnya 1 patch berisi semua op untuk tabel itu —
      lebih atomik daripada banyak patch terpisah)

Step 5 — Laporkan
  5.1 Ringkas: N tabel diperbarui, M kolom didokumentasikan, K kolom butuh review,
      L glossary term yang diusulkan untuk ditambahkan
```

### 7.2 Contoh Panggilan Batch (1 Tabel = 1 Patch)

```json
{
  "name": "patch_entity",
  "arguments": {
    "entityType": "table",
    "fqn": "<service>.<db>.<schema>.<table>",
    "patch": "[
      {\"op\":\"replace\",\"path\":\"/description\",\"value\":\"<isi-template-tabel>\"},
      {\"op\":\"add\",\"path\":\"/tags/-\",\"value\":{\"tagFQN\":\"Tier.Tier2\",\"labelType\":\"Manual\",\"state\":\"Confirmed\",\"source\":\"Classification\"}},
      {\"op\":\"replace\",\"path\":\"/columns/0/description\",\"value\":\"<deskripsi-kolom-0>\"},
      {\"op\":\"add\",\"path\":\"/columns/0/tags/-\",\"value\":{\"tagFQN\":\"DataSensitivity.Internal\",\"labelType\":\"Manual\",\"state\":\"Confirmed\",\"source\":\"Classification\"}},
      {\"op\":\"add\",\"path\":\"/columns/0/tags/-\",\"value\":{\"tagFQN\":\"DIS - Operasional Distribusi - Data Vocabulary.Validation Rules.task_id\",\"labelType\":\"Manual\",\"state\":\"Confirmed\",\"source\":\"Glossary\"}}
    ]"
  }
}
```

Catatan: payload `patch` adalah **string** berisi JSON array — jangan kirim sebagai array literal.

### 7.3 Skenario "Salin Pola dari Database Lain"

Bila user minta menerapkan pola dari `prod_siptrack` ke database lain:
1. Inspeksi schema target (apa kolom yang ada, apa nama field).
2. Untuk setiap kolom, cari padanan di glosarium **data product** yang tepat — **jangan paksakan glossary data product lain** kalau kolom itu milik data product berbeda. Ingat: satu data product bisa mencakup tabel lintas database, jadi cocokkan berdasarkan **kepemilikan data product**, bukan sekadar nama database.
3. Pakai Template §3 sebagai struktur deskripsi, tapi terminologi (kitchen SPPG, food_receiver, e-BAST, dll) **hanya** boleh dipakai bila memang data product/domainnya Distribusi. Untuk data product lain, kosongkan dan biarkan user mengisi terminologi mereka.

---

## 8. Operasi: Tag & Deskripsi DQ Test Case (DataQualityDimension + DQSeverity)

Mode ini untuk permintaan seperti *"tag test case data quality di tabel X"*, *"beri dimensi & severity ke semua test case di DB `kpm_production`"*, *"standarkan deskripsi test case biar mudah dipahami"*, atau *"samakan pola test case dengan `kpm_production`"*. Cakupan: **1 tabel** atau **semua tabel dalam 1 database**.

Tiga hal dikerjakan sekaligus per test case:
1. **Deskripsi** format 3-bagian yang mudah dipahami non-teknis.
2. Tag **`DataQualityDimension.<X>`** — dimensi kualitas yang diukur test (objektif, diturunkan dari apa yang dicek).
3. Tag **`DQSeverity.<Y>`** — konsekuensi bisnis bila test gagal (usulan; penetapan final kewenangan Data Owner).

Baseline gaya & isi: database **`kpm_production`** (service `Prod DB - kpm_production`, mis. `public.beneficiary`) — semua test case di sana sudah mengikuti pola ini. Tugas skill: mereplikasinya ke tabel/DB lain tanpa halusinasi.

📖 **Baca `references/dq-testcase-tagging.md` sebelum mengeksekusi.** File itu memuat vocabulary lengkap 5 dimensi + 4 severity (kriteria & FQN persis), pustaka frasa deskripsi per tipe test, mekanik patch, dan alur end-to-end. Jangan menebak dari ingatan.

### 8.1 Ringkas alur
1. **Temukan test case lewat testSuite — bukan search.** `search_metadata(entityType="testCase")` tidak reliabel (filter diabaikan). Jalur benar: `get_entity_details(entityType="table", fqn=...)` → ambil `testSuite.fullyQualifiedName` → `get_entity_details(entityType="testSuite", fqn="<table_fqn>.testSuite")` → array `tests[]` (FQN + deskripsi tiap test). Untuk 1 DB penuh: enumerasi tabel dulu (via `databaseSchema`), lalu ulang per tabel. (Ref §B.)
2. **Baca tiap test case**: `get_entity_details(entityType="testCase", fqn=<test_fqn>)` → `testDefinition.name`, `parameterValues`, tag lama, deskripsi lama.
3. **Tetapkan dimensi (objektif, ref §C)** + **usulkan severity (ref §D)**. Keduanya `mutuallyExclusive` → tepat satu masing-masing.
4. **Susun deskripsi 3-bagian (ref §E)**; pertahankan catatan anomali/EXPECTED FAIL yang sudah ada.
5. **Rakit 1 patch per test case** (ref §F): `replace /description` + `replace /tags`. Array `/tags` dirakit ulang = (semua tag lama **non-DQ**: `Tier`, `DataSensitivity`, `PII`, glossary) + 1 tag dimensi baru + 1 tag severity baru. Jangan hapus tag non-DQ. `source` tag dimensi/severity = `Classification`.
6. **Konfirmasi** sesuai mode user (default: satu konfirmasi batch untuk semua), lalu eksekusi `patch_entity` per test case dan laporkan distribusi dimensi + severity.

### 8.2 Dua classification — mutually exclusive, tepat SATU tiap test
- **`DataQualityDimension`** (bobot resmi): `Completeness` 0,25 · `Uniqueness` 0,25 · `Validity` 0,20 · `Consistency` 0,10 · `Timeliness` 0,05. Accuracy **tidak** termasuk (evidence-based, di luar skor otomatis). Pembeda cepat: NOT NULL → **Completeness**; enum/regex/range/format/FK → **Validity**; ketunggalan/PK/dedup → **Uniqueness**; keselarasan antar-kolom/tabel/sistem (mis. `updated_at ≥ created_at`) → **Consistency**; freshness/arrival SLA → **Timeliness**.
- **`DQSeverity`** (gate, bukan bobot): `Critical` (stop layanan / risiko PDP / salah sasaran PM / keamanan pangan / fraud-keuangan → dataset **Red**, HOLD/REJECT) · `High` (operasi utama / dashboard strategis / CDE non-safety → **Amber**, PASS WITH EXCEPTION) · `Medium` (turun usability, tidak stop proses) · `Low` (kosmetik/metadata). **Besar failedRows TIDAK menaikkan severity** — severity soal konsekuensi, bukan jumlah baris gagal.

Anti-halusinasi (§2): dimensi & severity **hanya** dari daftar di atas (FQN persis di ref). Bila dimensi sebuah test ambigu (mis. custom SQL yang bisa Validity atau Consistency), tandai `[PERLU KONFIRMASI dimensi]` dan minta arahan — jangan menebak.

---

## 9. Lineage & Root Cause Analysis

### 9.1 Skenario Trigger

User berkata "tabel X gagal", "data Y salah", "siapa sumber kolom Z", "siapa yang konsumsi tabel ini", "kalau saya ubah skema ini siapa kena dampak" → trigger pola ini.

### 9.2 Alur RCA Investigatif

```
1. search_metadata → resolve FQN
2. get_entity_lineage(upstreamDepth=3, downstreamDepth=2) untuk peta dependency
3. root_cause_analysis(entityType, fqn, upstreamDepth=3) untuk DQ-aware traversal
4. Sajikan ke user:
   - Upstream chain (sumber potensial)
   - Test case yang failing di upstream (kalau ada)
   - Downstream impact (tabel/dashboard yang akan kena bila masalah tidak diperbaiki)
5. Bila relevan, sarankan create_test_case di titik kritis upstream
```

### 9.3 Create Lineage Manual

Pakai bila lineage parser tidak mendeteksi relasi (mis. SQL dinamis, integrasi non-SQL). Ikuti §6.6.

---

## 10. Klasifikasi & Tag yang Tersedia (Snapshot Baseline)

Daftar berikut adalah tag yang **sudah ada dan dipakai** di instance OpenMetadata target. Sebelum memasang tag baru di luar daftar ini, cek ketersediaannya dulu dengan `search_metadata(query="<tag>", entityType="tag")`.

| Classification | Tag FQN |
|---|---|
| PII | `PII.None`, `PII.NonSensitive`, `PII.Sensitive` |
| Tier (tabel-level) | `Tier.Tier1`, `Tier.Tier2`, `Tier.Tier3`, `Tier.Tier4`, `Tier.Tier5` |
| DataSensitivity (custom org) | `DataSensitivity.Public`, `DataSensitivity.Internal`, `DataSensitivity.Restricted` |
| Certification | `Certification.Bronze` (auto-applied, expiry 30 hari) |
| DataQualityDimension (test case) | `DataQualityDimension.Completeness` (0,25), `.Uniqueness` (0,25), `.Validity` (0,20), `.Consistency` (0,10), `.Timeliness` (0,05) — mutually exclusive, tepat 1/test |
| DQSeverity (test case) | `DQSeverity.Critical`, `.High`, `.Medium`, `.Low` — mutually exclusive, tepat 1/test |

Glossary term yang sering dipakai sebagai column tag (glosarium **level Data Product**, mis. `DIS - Operasional Distribusi - Data Vocabulary`):
- `<domain_code> - <data_product_name> - Data Vocabulary.Entri Kosakata.<field>` — atribut enum (current_status, task_type, priority, role, dst.)
- `<domain_code> - <data_product_name> - Data Vocabulary.Validation Rules.<field>` — atribut non-enum (task_id, do_number, quantity, geo_coordinates, pii_password, dst.)

---

## 11. Common Pitfalls & Mitigasi

| Pitfall | Mitigasi |
|---|---|
| Merakit FQN manual gagal karena segmen `-` atau `.` | Selalu ambil FQN persis dari `search_metadata` |
| `patch_entity` overwrite isi orang lain | Selalu `get_entity_details` lebih dulu; pakai `replace` hanya bila benar-benar mengganti |
| `create_lineage` 400 karena pakai FQN | `create_lineage` butuh UUID, bukan FQN. Ambil dari `get_entity_details.id` |
| Test case tidak jalan / hasil tidak bermakna | Selalu `get_test_definitions` dulu — cocokkan dataType + parameterValues |
| Custom SQL test menghasilkan binary-only (tidak ada passedRows/failedRows) | SQL-nya pakai `SELECT COUNT(*)` → strategy default COUNT. Rewrite ke `SELECT *` + set `strategy: ROWS` (§6.8) |
| Test aggregate/schema tetap binary meski sudah pakai strategy ROWS | Binary adalah perilaku yang benar untuk test seperti `tableRowCountToBeBetween`, `tableFreshness`, dan semua test schema/aggregate — lihat Tabel 6.7-A. Jangan paksa ROWS untuk kategori binary-only |
| Lineage depth meluap context | Set `upstreamDepth ≤ 2` dan `downstreamDepth ≤ 2` untuk asset dengan graph besar |
| Tag classification vs glossary `source` salah | `Classification` untuk PII/Tier/DataSensitivity; `Glossary` untuk link term |
| Field `owner` ditolak | Sejak 1.5.0 field-nya `owners` (array). Pakai `/owners/-` add |
| `patch_entity` error "limits enforcement" (MCP 1.8.x) | Upgrade ke 1.12+, atau pakai Mode Fallback REST PATCH `application/json-patch+json` (§1a) |
| MCP OpenMetadata mati / "Connection closed" / tool tidak muncul | Cek §0 langkah 0 → bila token API tersedia, otomatis pindah ke Mode Fallback REST API + Script (§1a); jangan retry MCP berkali-kali |
| Search index REST salah nama (mis. pakai `table` polos, bukan `table_search_index`) | Ikuti pola `<entityType>_search_index` (§1a); verifikasi dengan query kecil dulu sebelum dipakai luas |
| `create_test_case` via REST ditolak / `entityLink` salah format | Jangan menebak sintaks `entityLink` — ambil polanya dari `GET /v1/dataQuality/testCases/{id}` test case existing dulu (§1a) |
| Output `search_metadata` meluap context | Set `size` kecil (5–10), pakai `entityType` filter spesifik, hindari query terlalu generik |
| `search_metadata(entityType="testCase")` malah balik table/glossary | Filter testCase diabaikan. Temukan test case lewat table → testSuite → `tests[]`, bukan search (§8, ref §B) |
| Tag dimensi/severity kedua ditolak atau dobel | `DataQualityDimension` & `DQSeverity` **mutuallyExclusive**. Rakit ulang seluruh `/tags` (tag non-DQ lama + 1 dimensi + 1 severity) lalu `replace` — jangan `add` tag kedua (§8, ref §F) |
| Patch test case menghapus Tier/PII/glossary | Saat `replace /tags`, sertakan kembali semua tag lama non-DQ; baca dulu via `get_entity_details` (ref §F) |

---

## 12. Stop Conditions — Berhenti & Minta Review Manusia

Skill ini **wajib berhenti** dan menunggu konfirmasi user dalam situasi berikut:

1. **Glosarium Data Product target tidak ditemukan / kosong.** Karena pembuatan wadah glosarium adalah tugas user, skill berhenti dan meminta user membuat glosarium `<domain_code> - <data_product_name> - Data Vocabulary` dulu — skill tidak membuat wadah glosarium data product otomatis kecuali diminta eksplisit.
2. Tidak ada glossary term cocok untuk satu atau lebih kolom dalam batch, dan user belum memberi arahan apakah:
   (a) skip kolom itu, (b) buat term baru, atau (c) tandai `[PERLU VERIFIKASI]`.
3. Operasi WRITE pertama dalam sesi — tampilkan dulu rencana lengkap sebelum eksekusi.
4. `get_test_definitions` mengembalikan kosong atau tidak ada definition yang cocok dengan dataType.
5. Service / database / schema yang diminta user **tidak unik** di hasil search — minta klarifikasi mana yang dimaksud.
6. Hasil `search_metadata` melebihi 50 dan user belum mempersempit query.
7. **Tabel/kolom tidak jelas milik data product yang mana** (mis. satu tabel dipakai lintas data product) — minta user menegaskan glosarium data product mana yang jadi target sebelum mengisi term.
8. **Dimensi test case ambigu** (mis. custom SQL yang bisa masuk Validity atau Consistency) dan user belum memberi arahan — tandai `[PERLU KONFIRMASI dimensi]` di rencana dan minta keputusan; jangan menebak. Severity selalu **diusulkan** untuk dikonfirmasi user karena penetapannya kewenangan Data Owner (bukan keputusan teknis).

---

## 13. Glosarium Data Product Lain

Skill ini bekerja identik untuk data product lain (lintas domain, lintas database). Untuk data product di luar contoh Distribusi:

1. Saat pre-flight, tegaskan **data product** mana yang jadi target dan pastikan wadah glosariumnya (`<domain_code> - <data_product_name> - Data Vocabulary`) sudah dibuat user. Bila belum ada, minta user membuatnya dulu — skill hanya mengisi term.
2. Konvensi Document ID komposit mengikuti domain + data product (`VOC-<DOMAIN>-<DP>-<FIELD>`); tetap cari dengan `search_metadata(query="VOC-", entityType="glossaryTerm")` untuk melihat pola yang sudah dipakai di glosarium target.
3. Terminologi spesifik (mis. kitchen SPPG, e-BAST, ompreng untuk Distribusi) **hanya** dipakai bila memang data product-nya itu. Untuk data product lain, kosongkan dan tunggu user mengisi terminologi mereka.
4. Ingat lintas-DB: satu data product boleh mencakup tabel dari lebih dari satu database — kumpulkan **semua** tabel milik data product itu saat mendokumentasikan, dan baris `Tabel:` pada term boleh lintas DB.
5. Template struktur (Grain/Layer/Volume/Diperbarui untuk tabel; deskripsi singkat + glossary link untuk kolom) berlaku universal.

---

## 14. Quick Reference — Ringkasan Tool Calls

```
# Resolve FQN
search_metadata(query="<name>", entityType="table|databaseSchema|glossaryTerm", size=10)

# Read detail
get_entity_details(entityType="<type>", fqn="<fqn>")

# Lineage
get_entity_lineage(entityType="table", fqn="<fqn>", upstreamDepth=2, downstreamDepth=2)

# RCA
root_cause_analysis(entityType="table", fqn="<fqn>", upstreamDepth=3)

# Patch description + tag + glossary link
patch_entity(entityType="table", fqn="<fqn>", patch="[ ... JSON Patch array ... ]")

# Glossary — wadah level Data Product dibuat USER; skill mengisi term saja
# (create_glossary hanya bila user eksplisit minta skill membuatkan wadah)
create_glossary(name="<domain_code> - <data_product_name> - Data Vocabulary", description=..., mutuallyExclusive=false, owners=[...], reviewers=[...])
create_glossary_term(glossary="<domain_code> - <data_product_name> - Data Vocabulary", name=..., description=..., parentTerm="<glossary_fqn>.Entri Kosakata|Validation Rules")

# Lineage tulis
create_lineage(fromEntity={"type":"table","id":"<uuid>"}, toEntity={"type":"table","id":"<uuid>"})

# Data quality
get_test_definitions(entityType="TABLE|COLUMN", limit=20)
# Row-level test (native): tidak perlu parameter strategy
create_test_case(name=..., fqn=..., testDefinitionName="columnValuesToMatchRegex",
                 columnName=..., parameterValues=[{"name":"regex","value":"<pattern>"}])
# Custom SQL: wajib strategy ROWS + SQL harus return baris yang melanggar (lihat §6.8)
create_test_case(name=..., fqn=..., testDefinitionName="tableCustomSQLQuery",
                 parameterValues=[
                   {"name":"sqlExpression","value":"SELECT * FROM <tbl> WHERE <kondisi_gagal>"},
                   {"name":"strategy","value":"ROWS"},
                   {"name":"threshold","value":"0"}
                 ])
```

```
# DQ test case — enumerasi (JANGAN search_metadata testCase)
get_entity_details(entityType="table", fqn="<table_fqn>")                 # → testSuite.fqn
get_entity_details(entityType="testSuite", fqn="<table_fqn>.testSuite")   # → tests[] (semua test case)
get_entity_details(entityType="testCase", fqn="<test_fqn>")              # → testDefinition, parameterValues, tags lama

# DQ test case — tag dimensi+severity & deskripsi (rakit ulang /tags; mutually exclusive)
patch_entity(entityType="testCase", fqn="<test_fqn>", patch="[
  {\"op\":\"replace\",\"path\":\"/description\",\"value\":\"<deskripsi 3-bagian>\"},
  {\"op\":\"replace\",\"path\":\"/tags\",\"value\":[ <tag non-DQ lama...>,
     {\"tagFQN\":\"DataQualityDimension.Validity\",\"source\":\"Classification\",\"labelType\":\"Manual\",\"state\":\"Confirmed\"},
     {\"tagFQN\":\"DQSeverity.Medium\",\"source\":\"Classification\",\"labelType\":\"Manual\",\"state\":\"Confirmed\"} ]}
]")
```

Patokan: **selalu** lewat alur Pre-flight (§0) → resolve FQN → read state → susun perubahan → konfirmasi user → tulis. Tidak ada shortcut.