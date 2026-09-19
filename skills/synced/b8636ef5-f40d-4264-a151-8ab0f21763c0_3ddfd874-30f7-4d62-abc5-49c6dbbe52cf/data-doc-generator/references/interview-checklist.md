# Reference: Interview Checklist (Anti-Halusinasi)

Skill ini wajib mengumpulkan informasi minimum dari user sebelum generate. Gunakan **`ask_user_input_v0`** untuk pertanyaan single/multi-select, dan **prose biasa** untuk pertanyaan terbuka.

## Aturan Umum

1. **JANGAN halusinasi** — jika user tidak tahu jawabannya, kosongkan field, jangan tebak
2. **Group pertanyaan per batch** — jangan dump semua sekaligus
3. **Boleh skip section opsional** — Profil Domain, Header Identifikasi, Referensi Regulasi semuanya optional
4. **Hormati data yang sudah ada** — jika user kasih CSV/database/schema, parse dulu, baru tanya gap

## Tahap 0: Identifikasi Sumber Data (PERTAMA SEKALI)

Tanya ini paling pertama:

```
ask_user_input_v0:
  question: "Apa sumber data untuk dokumentasi ini?"
  options:
    - "Database PostgreSQL (via MCP)"
    - "File CSV"
    - "Schema manual (CREATE TABLE / spreadsheet)"
    - "Kombinasi (akan saya jelaskan)"
```

Berdasarkan jawaban, ikuti workflow yang sesuai di `data-source-workflow.md`.

## Tahap 1: Scope Database (WAJIB)

Setelah sumber teridentifikasi:

1. **Apa nama database / data product secara keseluruhan?** (contoh: "BGN Penyaluran Harian", "Sistem Kependudukan SIAK")
2. **Apa nama domain bisnis?** (contoh: "Badan Gizi Nasional", "Kependudukan")
3. **Generate dokumen apa saja?**
   - Hanya Data Vocabulary (G-01)
   - Hanya Data Dictionary (G-03)
   - Kedua-duanya (default)
4. **Schema mana saja yang masuk scope?** (kalau database) — kalau lebih dari satu schema, daftar semua
5. **Tabel mana saja yang masuk scope?** — tampilkan daftar dari database, biar user pilih, atau "semua tabel"

## Tahap 2: Eksplorasi Data (Otomatis dari Sumber)

**Untuk Database / CSV**, ini dilakukan **OTOMATIS** tanpa tanya user lagi:

1. Ekstrak schema (nama kolom, tipe data, nullable, PK, FK)
2. Jalankan profiling: distinct count, null count, min/max, length stats
3. Identifikasi kandidat kategorikal vs non-kategorikal pakai LLM reasoning (lihat `categorical-detection.md`)
4. Identifikasi field PII dari pola nama (lihat `metadata-rules.md`)
5. Untuk field kategorikal, kumpulkan semua distinct values

**Untuk Schema Manual**, harus tanya user untuk:
- Daftar field enum + nilai validnya
- Daftar field PII

## Tahap 3: Konfirmasi Inferensi (KRUSIAL untuk Anti-Halusinasi)

Setelah profiling/parsing selesai, **TAMPILKAN RINGKASAN ke user dalam format terstruktur** dan minta approve sebelum generate:

```
Berdasarkan analisis sumber data:

TABEL DITEMUKAN ({N} tabel):
- {schema}.{table_1} ({row_count} baris)
- {schema}.{table_2} ({row_count} baris)

FIELD KATEGORIKAL (akan masuk Vocabulary sebagai enum):
- {table}.{field}: {N} distinct values -> [{val1}, {val2}, ...]

FIELD NON-KATEGORIKAL dengan validasi khusus (akan masuk Vocabulary):
- {table}.{field}: Format regex `{pattern}`
- {table}.{field}: Range [{min}, {max}]
- {table}.{field}: FK ke {ref_table}.{ref_col}

FIELD PII TERDETEKSI:
- {table}.{field}: {classification} ({pii_category})

FIELD UNCERTAIN (perlu konfirmasi):
- {table}.{field}: distinct={N}, sample=[...] - ini kategorikal atau identifier?
```

Lalu pakai `ask_user_input_v0` untuk konfirmasi:

```
question: "Apakah inferensi ini benar?"
options:
  - "Ya, lanjutkan generate"
  - "Ada beberapa yang perlu disesuaikan (akan saya jelaskan)"
  - "Saya mau review per kategori dulu"
```

## Tahap 4: Optional Metadata

Setelah inferensi disetujui, tanyakan optional:

1. **Doc ID pattern** — ada project code khusus? (default `G-01` dan `G-03`)
2. **Versi data product** — vX.Y.Z (default v1.0.0)
3. **Apakah ada regulasi spesifik yang relevan?** (opsional — kalau tidak ada, skip seksi)

**JANGAN tanyakan:**
- Author/Owner → SELALU dikosongkan
- Data Steward → bagian Profil Domain optional, skip kalau user tidak mention
- Header Identifikasi → optional, skip kalau user tidak mention

## Tahap 5: Konfirmasi Final & Generate

Tampilkan ringkasan apa yang akan di-generate, minta GO:

```
Akan generate:
- data-vocabulary.md (N entri: kategorikal=K, non-kategorikal=NK)
- data-dictionary.md (N tabel)

Lokasi: /mnt/user-data/outputs/

Lanjutkan?
```

---

## Edge Cases

### User upload file tapi belum jelas mau dokumentasikan apa

Contoh: user upload `data_sppg.csv` dan langsung `/skill-creator` tanpa context.

**Action**: jalankan `head -5` pada file dulu untuk lihat struktur, lalu tanya:
"Saya lihat ada file CSV dengan {N} kolom: {col1, col2, ...}. Apakah ini satu tabel, atau ada file CSV lain yang berelasi?"

### User punya banyak tabel tapi tidak yakin semua mau didokumentasikan

**Action**: tampilkan daftar tabel, lalu pakai multi-select:

```
ask_user_input_v0:
  question: "Tabel mana yang masuk scope?"
  options:
    - "Semua tabel di schema"
    - "Hanya tabel Gold layer"
    - "Saya pilih manual (akan saya sebutkan)"
  type: single_select
```

### Field punya distinct rendah tapi terlihat seperti identifier

Contoh: `kode_sppg` dengan 50 distinct (sample dataset kecil).

**Action**: JANGAN langsung set kategorikal. Tanya user:

```
"Field `kode_sppg` punya 50 distinct values di sample.
- Apakah ini ID unik per SPPG (jadi non-kategorikal - identifier)?
- Atau memang kategori terbatas (jadi kategorikal - enum)?"
```

### CSV besar (>1 juta baris)

**Action**: tetap pakai pandas chunksize seperti yang sudah didefinisikan di `data-source-workflow.md`. Beritahu user: "File ini punya {N} baris, profiling akan memakan waktu ~{T} detik. Lanjut?"

### Database kosong / tabel kosong

**Action**: profiling tidak bisa identifikasi enum. Beritahu user, tawarkan workflow C (manual schema).

### MCP Postgres tidak tersedia

**Action**: panggil `search_mcp_registry`. Kalau ada hasil, suggest. Kalau tidak, tawarkan alternatif:
- Export schema + sample data ke CSV, lalu pakai Workflow B
- Kasih schema manual, lalu pakai Workflow C

---

## Contoh Flow Lengkap (Database)

**User**: "Bantu saya bikin data vocabulary dan dictionary"

**Claude** (Tahap 0):
```
ask_user_input_v0:
  question: "Apa sumber data untuk dokumentasi?"
  options: [Database PostgreSQL, File CSV, Schema manual, Kombinasi]
```

**User**: pilih Database PostgreSQL

**Claude** (Tahap 1, prose):
- Database mana? (alias di MCP)
- Domain bisnis?
- Schema mana yang in-scope?

**User**: jawab — "db: bgn_warehouse, domain: BGN, schema: bgn_gold"

**Claude** (Tahap 2, otomatis):
- Query daftar tabel di schema
- Query schema setiap tabel
- Profile semua kolom (distinct count, null, range, length)
- LLM reasoning untuk klasifikasi kategorikal vs non-kategorikal
- Identifikasi field PII

**Claude** (Tahap 3, tampilkan summary):
- "Saya temukan 5 tabel, 47 kolom total..."
- "Kategorikal: 8 field (akan masuk Vocabulary)"
- "Non-kategorikal dengan validasi: 15 field"
- "PII: 4 field (3 Restricted, 1 Confidential)"
- "Uncertain: 2 field — minta konfirmasi"
- konfirmasi via `ask_user_input_v0`

**User**: konfirmasi

**Claude** (Tahap 4, optional):
- "Ada project code khusus, atau pakai G-01/G-03 default?"
- "Versi data product?"

**User**: jawab

**Claude** (Tahap 5):
- "Saya akan generate sekarang. OK?"
- generate 2 file -> save -> `present_files`
