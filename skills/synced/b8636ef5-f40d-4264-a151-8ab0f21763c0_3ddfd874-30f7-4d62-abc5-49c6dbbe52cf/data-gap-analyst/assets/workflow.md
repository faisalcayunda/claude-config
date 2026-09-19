# Workflow Detail — `data-gap-analyst`

Step-by-step operasional. Skill MUST mengikuti urutan ini. Jika ada step yang harus di-skip (mis. Mode D tidak bisa lakukan Step 4 untuk D1/D3/D4), catat eksplisit di output.

## Step 1 — Intake & Validation Input

Auto-detect mode berdasarkan input yang diberikan user:

| Sinyal Input | Mode | Catatan |
|---|---|---|
| User kasih connection string (pg/mysql/bq/snowflake) | A | Validasi connectivity lebih dulu sebelum lanjut |
| User upload file `*_per_column.csv` + `*_profile.md` | B | Output `data-profiling-baseline` — parse columns metric |
| User upload `.csv` / `.xlsx` / `.parquet` / `.json` mentah | C | Profile sendiri pakai `scripts/profile_source.py` |
| User kasih schema YAML/JSON/DDL/markdown | D | Structure-level only |
| Kombinasi 2 mode di atas | Hybrid | Catat mode per source di Input Inventory |

Validasi minimum yang HARUS lulus:

- Identifikasi Source A dan Source B sudah jelas (nama/identity)
- Mode untuk masing-masing source sudah ditentukan
- Kalau Mode A → connection tested, return non-error
- Kalau Mode B → file readable, parseable
- Kalau Mode C → file readable, schema inferable
- Kalau Mode D → schema parseable (YAML valid, DDL parseable)

Jika ada yang gagal validasi → STOP, lapor user, JANGAN lanjut step berikutnya.

## Step 2 — Klarifikasi Business Context (MAX 2 Pertanyaan)

Hanya tanya jika informasi belum tersedia dari konteks chat. Maksimum 2 pertanyaan, gabungkan dalam satu `AskUserQuestion`:

1. **Apa business entity yang dibandingkan?** — contoh: "Customer", "Order", "Transaction", "Inventory". Ini membantu reasoning di Step 6 (semantic interpretation).
2. **Apa tujuan analisis?** — pilih satu:
   - Migrasi (cek source vs target sebelum cutover)
   - Rekonsiliasi (cek dua sistem yang sudah co-exist)
   - Audit (regulator/internal audit minta proof of consistency)
   - Parity check (DWH vs OLTP, lake vs warehouse)

Jika user tidak respons dalam batas wajar → default ke "Rekonsiliasi" + entity "Generic" dan catat di output bahwa default dipakai. JANGAN tanya lagi pertanyaan ketiga.

## Step 3 — Inventory & Alignment

Bangun mapping tabel & kolom antar source:

### 3.1 Table-level mapping

- List semua tabel di Source A
- List semua tabel di Source B
- Match by name (exact) → masuk ke matched set
- Sisanya (unmatched) → fuzzy match dengan reasoning:
  - Levenshtein distance ≤2 → kandidat match
  - Semantic match (mis. `cust`/`customer`/`pelanggan`) → kandidat match
- Tampilkan hasil match ke user untuk konfirmasi (MAX 1x interaksi tambahan)
- Tabel unmatched setelah konfirmasi → flag sebagai *missing table* di D1

### 3.2 Column-level mapping (per tabel matched)

- Match by name (exact) → masuk ke matched set
- Fuzzy match:
  - `customer_id` ≈ `cust_id` ≈ `id_pelanggan`
  - `created_at` ≈ `tgl_dibuat` ≈ `dibuat_pada`
  - `amount` ≈ `nominal` ≈ `total`
- Konfirmasi hasil fuzzy match → jika user approve, lanjut. Jika tidak, flag sebagai *unmatched column*.

## Step 4 — Profiling Execution per Mode

### Mode A

Pakai `scripts/profile_source.py --mode=db --conn=...`. Untuk tabel >10M baris pakai `TABLESAMPLE SYSTEM (1)`. Output: dict per kolom dengan metrik standar (lihat Step 5).

### Mode B

Parse `*_per_column.csv` dari `data-profiling-baseline`. Map header sesuai schema (kolom `column_name`, `null_count`, `distinct_count`, `min`, `max`, `mean`, `median`, `stddev`, `top_values`, dll).

### Mode C

Pakai `scripts/profile_source.py --mode=file --path=...`. Untuk file >500MB pakai pandas chunked. Output: dict per kolom dengan metrik standar.

### Mode D

Parse schema (YAML/JSON/DDL). Output: dict per kolom dengan field schema-only (column name, data type, constraint, PK/FK info, default value).

## Step 5 — Gap Calculation per 4 Dimensi

Pakai `scripts/compute_gap.py`. Untuk setiap dimensi, hitung metrik sesuai formula di `assets/threshold_rubric.md`:

- **D1 Volume & Completeness** — row count delta, table coverage, NULL ratio delta, distinct count delta
- **D2 Schema & Structural** — column diff, type diff, constraint diff, PK/FK diff, index diff
- **D3 Value Distribution & Semantic** — stats side-by-side, KS test, Jaccard sim, cardinality delta, unit/format delta
- **D4 Temporal & Freshness** — latest ts, update frequency, coverage period, lag estimation

Untuk setiap metrik yang melebihi threshold → buat gap finding baru (assign `gap_id`).

## Step 6 — Reasoning Chain Generation per Gap Finding

Pakai `scripts/llm_reasoning_helper.py`. Untuk setiap `gap_id`, generate 7-step chain:

1. OBSERVATION
2. MAGNITUDE
3. HYPOTHESIS (2-3 hipotesis)
4. EVIDENCE TEST
5. CONCLUSION (+ confidence)
6. IMPACT
7. RECOMMENDATION (+ owner + urgency)

Template + contoh ada di `assets/reasoning_template.md`. WAJIB ditulis dalam narasi paragraf, bukan bullet.

## Step 7 — Layer 1 (Tim Data) Writeup

Per gap finding, generate Layer 1 text mengikuti template `assets/layer1_template.md`. Pakai bahasa teknis, sertakan SQL snippet/DDL/monitoring rule. Sertakan referensi DAMA-DMBOK KA-04/KA-11 dari `references/dama_kafit.md`.

## Step 8 — Layer 2 (Awam) Writeup

Per gap finding, generate Layer 2 text mengikuti template `assets/layer2_template.md`. JANGAN pakai istilah teknis. Pakai analogi sehari-hari, konsekuensi bisnis konkret, dan pertanyaan strategis untuk pimpinan.

**Test cepat**: kalau Layer 2 dibaca oleh seseorang yang baru bergabung di organisasi 1 minggu dan tidak pernah pegang database, mereka harus bisa paham. Kalau tidak paham → tulis ulang.

## Step 9 — Bundle Generation

Pakai `scripts/render_bundle.py` untuk hasilkan 4 artefak:

- `gap_analysis_report.md` (Docusaurus-ready)
- `gap_analysis_workbook.xlsx` (multi-sheet, conditional formatting di Field-Level Gap Matrix)
- `gap_analysis_executive.pdf` (3-5 halaman, polished, embed 3-6 PNG chart)
- `gap_findings.json` (machine-readable schema sesuai SKILL.md)

Output folder default: `./gap_analysis_output_<timestamp>/`. Boleh di-override via argumen `--output-dir`.

## Step 10 — Self-Verification Checklist

Sebelum present ke user, jalankan checklist berikut. Skill MUST lulus SEMUA:

- [ ] Mode input ter-detect dengan benar dan tercatat di Input Inventory
- [ ] Klarifikasi business context sudah dilakukan (entity + tujuan)
- [ ] Tabel mapping sudah dikonfirmasi user (atau default exact-match dipakai)
- [ ] Semua 4 dimensi tersentuh (kecuali Mode D yang hanya bisa D2)
- [ ] Setiap gap finding punya 7-step reasoning chain LENGKAP (tidak ada step yang skip)
- [ ] Setiap gap finding punya Layer 1 dan Layer 2 (keduanya berdiri sendiri)
- [ ] Setiap angka di report punya `source_trace` (query/file + offset/sheet)
- [ ] Tidak ada kata "kemungkinan/biasanya/umumnya" tanpa cite
- [ ] 4 artefak ter-generate semua (MD + XLSX + PDF + JSON)
- [ ] Threshold rubric yang dipakai tercatat di Scope & Method (default atau override)
- [ ] Jika ada gap yang `[uncertain]` → flag jujur, JANGAN tebak

Jika ada checklist yang gagal → fix sebelum lapor selesai.
