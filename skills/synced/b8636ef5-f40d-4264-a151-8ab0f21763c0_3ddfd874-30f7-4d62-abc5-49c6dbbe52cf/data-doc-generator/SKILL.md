---
name: data-doc-generator
description: Generate Data Vocabulary (G-01) dan Data Dictionary (G-03) untuk satu database (multi-tabel) dari sumber CSV, PostgreSQL via MCP, atau schema manual. Trigger SETIAP KALI user minta bikin data vocabulary, kamus data, data dictionary, dokumentasi schema, G-01, G-03, dokumentasi atribut, daftar enum, panduan standarisasi data baku, profil data, validasi field, atau dokumen governance level field untuk data product apapun (fintech, pemerintahan, BGN, kesehatan, logistik, e-commerce, HR). Juga kalau user kasih CSV/database connection/schema dan minta didokumentasikan markdown Docusaurus. Skill ini auto-profile data aktual (full COUNT DISTINCT untuk DB, pandas chunksize untuk CSV) dan pakai LLM reasoning untuk bedakan field kategorikal (enum) dari numeric/identifier/date yang sekedar distinct rendah — supaya output anti-halusinasi.
---

# Data Documentation Generator

Skill untuk men-generate **dua dokumen governance** dalam format markdown Docusaurus **per tabel**:

1. **Data Vocabulary (G-01)** — `{table_name}_vocabulary.md` — kamus standarisasi data baku per tabel: enum values dan aturan validasi field
2. **Data Dictionary (G-03)** — `{table_name}_dictionary.md` — kamus teknis per tabel: schema, constraint, serta aturan uniqueness dan completeness

**Penting**: 1 tabel = 2 file. Proses dilakukan **satu tabel pada satu waktu** secara sequential. Jangan muat semua tabel ke konteks sekaligus.

## Prinsip Inti

1. **Anti-halusinasi maksimal**: pakai data aktual untuk profiling, bukan tebakan. Untuk field kategorikal, distinct values dari hasil COUNT DISTINCT full table.
2. **LLM reasoning untuk klasifikasi**: tidak semua field dengan distinct rendah adalah enum. Bedakan kategorikal vs identifier/measure/date.
3. **Vocabulary = validasi + enum saja**: Data Vocabulary hanya berisi aturan validasi (Format, Range, Length, Referential Integrity, Cross-field Rule) dan enum values. **Uniqueness dan completeness rules masuk ke Data Dictionary Section 3, bukan Vocabulary.**
4. **Setiap field di Vocabulary WAJIB punya seksi validasi**: Untuk field non-kategorikal, jangan pernah lewatkan Aturan Validasi. Jika memang tidak ada aturan validasi yang berlaku (jarang sekali), nyatakan secara eksplisit: `Tidak ada aturan validasi — field bebas [alasan singkat]`.
5. **Author dan Owner SELALU kosong** di frontmatter.
6. **Seksi optional benar-benar opsional**:
   - Profil Domain (Vocabulary) — skip jika kosong
   - Header Identifikasi (Data Dictionary) — skip jika kosong
   - Referensi Regulasi (Vocabulary) — skip jika kosong
7. **Section 3 Enum Values di Data Dictionary DILEWATKAN** (info enum ada di Vocabulary).
8. **Sequential one-at-a-time** — proses, generate, dan save 2 file untuk SATU tabel, beri progress update, baru lanjut ke tabel berikutnya.
9. **Standalone** — jangan auto-call skill lain kecuali user eksplisit minta.
10. **Interaktif dengan checkpoint wajib** — jangan jalankan pipeline sampai tuntas tanpa interaksi. Di setiap titik keputusan penting, BERHENTI, ajukan semua pertanyaan terkait dalam satu kelompok, dan TUNGGU jawaban user sebelum melanjutkan ke langkah berikutnya. Lihat Langkah B untuk checkpoint wajib.

## Batas Tanggung Jawab: Vocabulary vs Dictionary

| Rule Type | Masuk ke Mana? |
|---|---|
| Enum / Valid Values (kategorikal) | Vocabulary |
| Format (regex/pattern) | Vocabulary |
| Range (numeric/date min-max) | Vocabulary |
| Length (min/max string length) | Vocabulary |
| Referential Integrity (FK) | Vocabulary |
| Cross-field Business Rule | Vocabulary |
| Uniqueness (UNIQUE constraint, partial unique, deduplikasi) | Dictionary Section 3 |
| Completeness (NOT NULL rationale, null rate threshold, mandatory field rule) | Dictionary Section 3 |
| Data Quality rules lainnya (accuracy threshold, timeliness SLA) | Dictionary Section 3 |

## Tiga Workflow Berdasarkan Sumber Data

### Workflow A: PostgreSQL via MCP

```
User pilih "Database PostgreSQL"
  -> tool_search untuk cari postgres MCP
  -> kalau ada: gunakan; kalau tidak: search_mcp_registry + suggest_connectors
  -> eksplorasi schema (list tables, columns, PK, FK) — catat daftar tabel
  -> untuk SETIAP tabel (satu per satu):
      -> FULL TABLE COUNT DISTINCT per kolom tabel ini saja
      -> LLM reasoning kategorikal vs non-kategorikal
      -> generate 2 file untuk tabel ini
      -> progress update
```

### Workflow B: CSV File

```
User pilih "File CSV"
  -> identifikasi semua file di /mnt/user-data/uploads/
  -> untuk SETIAP file CSV (satu per satu):
      -> run scripts/profile_csv.py untuk file ini saja
      -> LLM reasoning kategorikal vs non-kategorikal
      -> generate 2 file untuk tabel/file ini
      -> progress update
```

### Workflow C: Manual Schema

```
User pilih "Schema manual"
  -> parse CREATE TABLE / spreadsheet, identifikasi semua tabel
  -> untuk SETIAP tabel (satu per satu):
      -> TIDAK ada profiling otomatis, tanya user untuk enum values tabel ini
      -> infer validasi dari pola nama field
      -> generate 2 file untuk tabel ini
      -> progress update
```

Detail lengkap setiap workflow ada di `references/data-source-workflow.md`.

## Workflow Eksekusi

### Tahap 0: Identifikasi Sumber

Pertama sekali, tanya pakai `ask_user_input_v0`:

> Apa sumber data untuk dokumentasi ini?
> - Database PostgreSQL (via MCP)
> - File CSV
> - Schema manual (CREATE TABLE / spreadsheet)
> - Kombinasi (akan saya jelaskan)

### Tahap 1: Scope

Tanyakan secara prose:
1. Nama database / data product
2. Domain bisnis
3. Generate G-01, G-03, atau keduanya?
4. Schema mana (jika DB) atau file mana (jika CSV)
5. Tabel mana yang in-scope -> **simpan sebagai ordered list**, tapi JANGAN profiling semua sekaligus

### Tahap 2 dst: Loop Per Tabel (SATU TABEL PADA SATU WAKTU)

Setelah scope dikonfirmasi, proses tabel **secara sequential**. Untuk **setiap tabel** dalam daftar:

#### Langkah A — Profiling Tabel Ini

**Untuk Postgres**: jalankan SQL queries dari `references/postgres-queries.md` **hanya untuk tabel ini**. Save hasilnya ke `/home/claude/profile_{table_name}.json`.

**Untuk CSV**: jalankan `scripts/profile_csv.py` **hanya untuk file ini**:
```bash
python /path/to/scripts/profile_csv.py /mnt/user-data/uploads/file.csv \
    --max-distinct 50 \
    --chunksize 50000 \
    --output /home/claude/profile_{table_name}.json
```

**Untuk Schema Manual**: skip profiling, tanya user untuk daftar enum tabel ini saja.

#### Langkah B — LLM Reasoning + Konfirmasi (KRUSIAL)

Untuk **setiap kolom tabel ini**, lakukan reasoning berdasarkan `references/categorical-detection.md`:

1. Cek nama field (status_*, tipe_*, kode_provinsi -> kategorikal; nik, nama, tanggal, jumlah -> non-kategorikal)
2. Cek apakah distinct count akan bertambah signifikan jika data 10x lipat
3. Cek apakah values terlihat seperti label diskret atau measurement continuous
4. Cek apakah field akan dipakai sebagai axis pivot/group by atau dijumlahkan

Untuk field yang **uncertain**, JANGAN langsung putuskan — kumpulkan di daftar UNCERTAIN.

**Untuk setiap kolom yang terdeteksi kategorikal, evaluasi kelengkapan enum:**

Distinct value dari profiling belum tentu mencakup semua kategori yang mungkin. Terapkan aturan keputusan berikut:

- **FK / referensi ke tabel lain**: jika kolom merujuk tabel lain (foreign key, lookup table, master table, reference table), distinct values dari tabel sumber BELUM TENTU lengkap — ada nilai valid yang belum pernah muncul di data. Tandai kolom ini sebagai `PERLU_REF_TABLE`. Jangan ambil kategori dulu — tanyakan tabel referensinya ke user di Checkpoint 1.
- **Kategori terlihat tidak lengkap**: jika tabel referensi tidak tersedia, ATAU berdasarkan reasoning nilai yang ada tampak kurang (mis. kolom status tanpa 'CANCELLED' atau 'REJECTED' padahal logis ada), tandai `PERLU_VALIDASI`. Output Vocabulary untuk kolom ini akan diberi note eksplisit.
- **Kategori sudah pasti lengkap**: jika field boolean atau enum dibatasi CHECK constraint di schema, dokumentasikan langsung tanpa catatan tambahan.

**Aturan keras**: JANGAN pernah mengarang nilai kategori. Pilihannya hanya: (a) ambil dari tabel referensi yang terverifikasi, atau (b) tandai dengan note berikut di entry Vocabulary:
> ⚠️ Perlu validasi ke Tim Product — kategori pada kolom ini kemungkinan belum lengkap; distinct value yang terdeteksi belum tentu mencakup semua kategori yang mungkin.

---

**⛔ CHECKPOINT 1 — BERHENTI setelah reasoning. TUNGGU jawaban user sebelum lanjut ke Langkah C.**

Tampilkan ringkasan dan kumpulkan **semua pertanyaan dalam satu blok**. Jangan lanjut ke generate dokumen sebelum user menjawab. Tanyakan hanya hal yang relevan — lewati baris yang kosong:

- ✅ **KATEGORIKAL**: [daftar field]
- 📋 **NON-KATEGORIKAL**: [daftar field]
- 🔍 **UNCERTAIN** — mohon konfirmasi: mana yang enum vs bukan?
- ⚠️ **PERLU_REF_TABLE** — untuk field ini: tabel referensi mana yang menjadi sumber kategori lengkap?
- ⚠️ **PERLU_VALIDASI** — untuk field ini: ada sumber kategori yang benar, atau setuju ditandai "perlu validasi Tim Product"?
- 🔴 **PII terdeteksi** — mohon konfirmasi klasifikasi
- ❓ **Validation rule tidak jelas** — ada info tambahan untuk field ini?

Jika tidak ada field UNCERTAIN / PERLU_REF_TABLE / PERLU_VALIDASI dan PII sudah jelas, cukup tampilkan ringkasan dan minta satu konfirmasi approve untuk lanjut.

Setelah user menjawab: perbarui klasifikasi dan daftar kategori sesuai jawaban, lalu lanjut ke Langkah C.

Konfirmasi via `ask_user_input_v0`.

#### Langkah C — Optional Metadata (per tabel)

- Doc ID pattern (default G-01, G-03)
- Versi data product (default v1.0.0)
- Referensi regulasi (skip seksi jika kosong)

JANGAN tanya author/owner — selalu kosong.

#### Langkah D — Generate 2 File Tabel Ini

Generate ke `/mnt/user-data/outputs/`:
- `{table_name}_vocabulary.md`
- `{table_name}_dictionary.md`

Konvensi nama file: gunakan nama tabel tanpa schema prefix, titik diganti underscore.
Contoh: tabel `bgn_gold.fct_penyaluran_mbg` -> `fct_penyaluran_mbg_vocabulary.md` dan `fct_penyaluran_mbg_dictionary.md`.

Call `present_files` dengan kedua path untuk tabel ini.

#### Langkah E — Progress Update

Setelah 2 file tersimpan, cetak progress:

```
[OK] Tabel {schema.table_name} selesai ({i} dari {n} tabel)
   -> {table_name}_vocabulary.md
   -> {table_name}_dictionary.md
```

Lanjut ke tabel berikutnya tanpa menunggu konfirmasi, kecuali ada error atau user minta berhenti.

#### Selesai Semua Tabel

Setelah seluruh tabel diproses, tampilkan ringkasan:

```
Dokumentasi selesai — {n} tabel, {2n} file dihasilkan:
[daftar semua file yang dihasilkan]
```

## Struktur Output per Tabel

### {table_name}_vocabulary.md

```
1. Frontmatter YAML (author='', owner='')
2. # Kamus Data — Referensi Kosakata — {schema.table_name}
3. Quote tujuan + :::info cara pakai
4. ## Riwayat Versi
5. ## Referensi Regulasi yang Berlaku  [OPTIONAL — skip jika kosong]
6. ## Profil Domain                     [OPTIONAL — skip jika kosong]
7. ## Entri Kosakata
   ### {field_1}: ...   [KATEGORIKAL atau NON-KATEGORIKAL]
   ### {field_2}: ...
   ... (SEMUA field dari tabel ini — tidak boleh ada yang terlewat)
8. ## Panduan Penambahan Kosakata Baru
9. ## Riwayat Review
10. ## Referensi Silang
```

**Per entry**, pilih pola:
- **KATEGORIKAL**: ada seksi "Nilai yang Valid (Enum)" dengan kolom "Makna untuk Tim Produk" (penjelasan awam per nilai enum) dan frekuensi dari profiling
- **NON-KATEGORIKAL**: ada dua seksi — (1) **"Aturan Bisnis"** (tabel ID BVR + plain language untuk tim produk), (2) **"Implementasi Teknis"** (Format/Range/Length/FK/Cross-field + SQL dengan referensi BVR)

**WAJIB — tidak boleh ada field yang terlewat**:
- Setiap field harus punya salah satu seksi di atas.
- Jika field non-kategorikal dan genuinely tidak punya aturan apapun (free-form murni), tulis eksplisit: `Tidak ada aturan bisnis yang berlaku — field ini adalah teks bebas tanpa constraint format, range, atau referensi.`
- **TIDAK BOLEH masuk ke Vocabulary**: Uniqueness rules, NOT NULL rationale, completeness thresholds, null rate SLA — semua itu masuk Dictionary Section 3.

Detail di `templates/vocabulary-entry-template.md` dan contoh di `references/worked-examples.md`.

### {table_name}_dictionary.md

```
1. Frontmatter YAML (author='', owner='', data_classification=tertinggi, pii_flag=auto)
2. # Data Dictionary — {schema.table_name}
3. Quote tujuan + :::note G-03 vs G-01
4. ## Riwayat Versi
5. ## Header Identifikasi                [OPTIONAL — skip jika kosong]
6. ## 1. Informasi Tabel
7. ## 2. Data Dictionary
   (tabel kolom langsung — tidak ada sub-heading 2.1/2.2 karena ini satu tabel)
8. ## 3. Aturan Kualitas per Field
   (uniqueness + completeness + quality rules — lihat panduan di bawah)
9. ## 4. Panduan Penggunaan untuk Analyst
10. ## Annex A — Field Lineage Diagram
```

**Section 3 — Aturan Kualitas per Field** adalah tempat untuk rules yang mengatur kelengkapan dan keunikan data (BUKAN format/range/enum yang ada di Vocabulary):

| Tipe Rule | Contoh | Implementasi |
|---|---|---|
| Uniqueness | PK natural key, UNIQUE constraint, partial UNIQUE | UNIQUE (field) atau CREATE UNIQUE INDEX WHERE ... |
| Completeness | NOT NULL rationale, null rate threshold | NOT NULL + penjelasan bisnis; atau null_rate < 0.01 |
| Mandatory Conditional | Field wajib diisi jika status = 'aktif' | CHECK (status <> 'aktif' OR field IS NOT NULL) |
| Data Quality SLA | Max 1% null rate, freshness < 24 jam | Monitoring via Great Expectations / dbt test |

Format Section 3:

```markdown
## 3. Aturan Kualitas per Field

| Field | Tipe Rule | Rule | Threshold / Implementasi | Ref. Aturan Bisnis | Keterangan |
|---|---|---|---|---|---|
| `field_name` | Uniqueness | Nilai unik per baris | UNIQUE (field_name) | — | PK surrogate |
| `field_name` | Completeness | NOT NULL | NOT NULL constraint | BVR-003 | Setiap record wajib punya nilai |
| `field_name` | Completeness | Null rate | < 1% dalam monitoring | — | Boleh null untuk kondisi tertentu |
| `field_name` | Mandatory Conditional | Wajib jika status = aktif | CHECK (...) | BVR-007 | — |
```

Kolom **Ref. Aturan Bisnis** berisi ID BVR dari Vocabulary yang menjadi landasan bisnis rule ini. Isi `—` jika rule murni teknis tanpa konteks bisnis eksplisit (mis. PK surrogate, index teknis).

**Per object section** (Section 2):
- Tabel fakta: kolom `#, Nama Field, Tipe Data, Nullable, Klasifikasi, Kunci, Default, Deskripsi Teknis, Makna Bisnis, Sumber`
- Tabel dimensi SCD2: kolom `#, Nama Field, Tipe Data, Nullable, Klasifikasi, SCD Role, Deskripsi`
- View: tambahkan blok SQL definisi view di awal section

## Aturan Klasifikasi & Inferensi Otomatis

Lihat `references/metadata-rules.md`. Yang paling penting:

| Indikator | Auto-Inferensi |
|---|---|
| Field nama: nik, nama_*, email, no_hp, alamat, tanggal_lahir | PII detected |
| nik, biometrik, kesehatan, data anak | Confidential |
| Nama, alamat, email, no HP | Restricted |
| Status, tipe, kategori, kode_provinsi | Internal (kategorikal) |
| Field dengan distinct <= 50 + nama label-like | Kategorikal kandidat |
| Field numeric float / counter / measurement | Non-kategorikal (Range) |
| Field FK (nama_id, dim_*_id) | Non-kategorikal (Referential Integrity) |
| Tabel mengandung 1+ field Restricted/Confidential | pii_flag: true |

**Konfirmasi semua inferensi PII ke user** — jangan langsung anggap benar.

## File Reference (Layered)

Saat butuh detail spesifik, baca file ini:

| File | Kapan Dibaca |
|---|---|
| references/data-source-workflow.md | Tahap 0-1: tentukan workflow A/B/C |
| references/postgres-queries.md | Workflow A: SQL queries untuk profiling |
| scripts/profile_csv.py | Workflow B: profiling CSV |
| references/categorical-detection.md | Langkah B: LLM reasoning kategorikal vs non-kategorikal |
| references/validation-rules.md | Generate Vocabulary: format/range/length/FK/cross-field |
| references/metadata-rules.md | Langkah B-D: klasifikasi, tipe data, naming, PII |
| references/interview-checklist.md | Tahap 0-1: alur interview anti-halusinasi |
| references/worked-examples.md | Generate: contoh konkret per skenario |
| templates/data-vocabulary-template.md | Generate: skeleton dokumen vocabulary |
| templates/vocabulary-entry-template.md | Generate: pola entry kategorikal & non-kategorikal |
| templates/data-dictionary-template.md | Generate: skeleton dokumen data dictionary |

**Praktik baca file**: Baca yang relevan untuk tahap saat ini, jangan baca semua di awal.

## Aturan Penulisan Output

- Backtick inline untuk nama field, tipe data, kode enum
- Emoji klasifikasi di tabel: Hijau = Public, Biru = Internal, Kuning = Restricted, Merah = Confidential
- Em-dash untuk pemisah (bukan hyphen)
- Frontmatter date format 'YYYY-MM-DD' (single quote)
- Frontmatter author dan owner SELALU ''
- Untuk frekuensi enum dari profiling, format ribuan dengan titik: 5.234.567
- SQL code blocks dengan ```sql
- Lineage diagrams dengan ``` tanpa language tag

## Hal yang Sering Salah

SALAH: Proses semua tabel sekaligus, baru generate di akhir (harus satu per satu)
SALAH: Load profiling semua tabel ke konteks sekaligus (profiling per tabel, hapus dari konteks setelah selesai)
SALAH: Generate tanpa interview / tanpa konfirmasi inferensi
SALAH: Anggap semua distinct <= 50 adalah enum (umur juga distinct rendah tapi numeric)
SALAH: Anggap semua distinct tinggi pasti non-kategorikal (kode_kabupaten punya 514 distinct tapi tetap kategorikal)
SALAH: Isi author/owner dengan nama random
SALAH: Field non-kategorikal tidak punya seksi "Aturan Bisnis" (wajib ada, atau pernyataan eksplisit tidak ada aturan)
SALAH: Seksi "Aturan Bisnis" ditulis dalam bahasa teknis / SQL (harus plain language untuk tim produk)
SALAH: Implementasi Teknis tidak mencantumkan ID BVR di header sub-seksi (BVR-001, BVR-002, dst.)
SALAH: Kolom "Makna untuk Tim Produk" di tabel enum kosong atau berisi kalimat teknis
SALAH: Dictionary Section 3 tidak punya kolom "Ref. Aturan Bisnis"
SALAH: Taruh uniqueness / NOT NULL rationale / completeness rules di Vocabulary (itu masuk Dictionary Section 3)
SALAH: Taruh enum / format / range / FK / cross-field rule di Dictionary Section 3 (itu masuk Vocabulary)
SALAH: Pertahankan Section 3 Enum Values di Data Dictionary (skip!)
SALAH: Halusinasi nilai enum (untuk FK/referensi: ambil dari tabel referensi; untuk kolom standalone: ambil dari distinct values aktual)
SALAH: Dokumentasikan enum dari distinct values saja untuk kolom FK/referensi tanpa menelusuri tabel referensinya
SALAH: Mengarang/menebak nilai enum yang "mungkin ada" — pilihannya hanya (a) sumber terverifikasi atau (b) note "perlu validasi Tim Product"
SALAH: Halusinasi regex pattern (validasi dari sample data atau pola nama field standar)
SALAH: Skip konfirmasi PII
SALAH: Lanjut generate dokumen setelah profiling selesai tanpa BERHENTI di Checkpoint 1
SALAH: Tanyakan satu pertanyaan per giliran — kumpulkan semua pertanyaan dalam satu blok di Checkpoint 1

BENAR: Proses SATU tabel pada satu waktu — save 2 file, lanjut ke tabel berikutnya
BENAR: Profiling hanya untuk tabel yang sedang diproses
BENAR: Sumber: tanya dulu (Workflow A/B/C)
BENAR: LLM reasoning untuk uncertain fields, tanya user
BENAR: Summary inferensi sebelum generate, minta approve
BENAR: Vocabulary non-kategorikal: "Aturan Bisnis" (plain language + BVR ID) → "Implementasi Teknis" (SQL + BVR ref)
BENAR: Vocabulary kategorikal: tabel enum dengan kolom "Makna untuk Tim Produk" yang ditulis awam
BENAR: Dictionary Section 3: uniqueness + completeness + quality SLA + kolom "Ref. Aturan Bisnis" (BVR ID)
BENAR: Setelah save, panggil present_files dengan kedua path untuk tabel tersebut
BENAR: Cetak progress update setelah setiap tabel selesai
BENAR: Kolom FK/referensi → tandai PERLU_REF_TABLE, tanyakan tabel referensi di Checkpoint 1, ambil daftar kategori lengkap dari tabel referensi
BENAR: Enum terlihat tidak lengkap dan tidak ada tabel referensi → tandai PERLU_VALIDASI, tambahkan note "⚠️ Perlu validasi ke Tim Product" di Vocabulary
BENAR: Checkpoint 1 wajib dilakukan setiap tabel — kumpulkan semua pertanyaan dalam satu blok, BERHENTI, TUNGGU jawaban user sebelum generate

## Quick Start

User: "Bantu saya bikin data vocabulary dan dictionary dari database saya"

1. Baca references/interview-checklist.md untuk pola interview
2. Tahap 0: ask_user_input_v0 untuk sumber -> pilih PostgreSQL
3. Baca references/data-source-workflow.md seksi Workflow A
4. Baca references/postgres-queries.md untuk SQL
5. Tahap 1: ask scope, kumpulkan daftar tabel (JANGAN profiling semua)
6. Loop per tabel — untuk tabel pertama:
   a. Jalankan profiling SQL hanya untuk tabel ini
   b. Baca references/categorical-detection.md untuk reasoning
   c. Tampilkan summary tabel ini, ask_user_input_v0 untuk konfirmasi
   d. Baca references/validation-rules.md untuk non-kategorikal rules
   e. Baca references/worked-examples.md untuk contoh format
   f. Generate {table_name}_vocabulary.md + {table_name}_dictionary.md, present_files
   g. Cetak progress update
7. Ulangi langkah 6 untuk tabel berikutnya
