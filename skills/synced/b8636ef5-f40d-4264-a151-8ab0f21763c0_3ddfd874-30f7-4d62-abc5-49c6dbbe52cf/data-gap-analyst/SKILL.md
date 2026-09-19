---
name: data-gap-analyst
description: >-
  Analisis gap DUA sumber data dengan business context sama. Trigger
  untuk "gap analysis", "analisis gap", "bandingkan dua database",
  "compare data sources", "data gap", "migrasi data validation",
  "validasi migrasi", "rekonsiliasi data", "data parity", "source vs
  target", "data consistency between", "konsistensi antar sumber",
  "audit perpindahan data", "data lineage gap", "before-after data
  comparison", "DWH vs OLTP gap", "lake vs warehouse comparison",
  "OLTP vs OLAP", "cek konsistensi DB", "selisih data antar sistem",
  "data drift antar sistem". Mengukur 4 dimensi (Volume &
  Completeness, Schema & Structural, Value Distribution & Semantic,
  Temporal & Freshness), 7-step reasoning chain, dual-layer writeup
  (teknis + DAMA-DMBOK; awam + pertanyaan strategis pimpinan). Output 4
  artefak (MD/XLSX/PDF/JSON). 4 input mode (live DB, file profiling,
  raw file, schema-only) plus hybrid. JANGAN trigger untuk profiling 1
  sumber (pakai `data-profiling-baseline`) atau dokumentasi schema 1
  DB (pakai `data-doc-generator`).
---

# Data Gap Analyst

Skill ini melakukan **analisis gap antar dua sumber data** yang membawa konteks bisnis yang sama (mis. OLTP vs DWH, source vs target migrasi, lake vs warehouse, sistem lama vs sistem baru, snapshot before vs after). Tujuannya bukan profiling — tetapi **menemukan, menjelaskan, dan menarasikan perbedaan** antara dua sumber, lengkap dengan reasoning chain dan rekomendasi.

Skill ini bagian dari ekosistem IDEAS dan interoperable dengan: `data-profiling-baseline` (membaca output-nya sebagai input Mode B), `data-doc-generator` (G-01/G-03 dipakai sebagai referensi semantik), `openmetadata-catalog-manager` (findings bisa dipublish sebagai test_case/incident), dan `dama-research` (mengacu KA-04 Data Quality & KA-11 Metadata).

## Filosofi

Gap analysis yang baik bukan sekadar `DIFF` skema atau `COUNT(*) - COUNT(*)`. Skill ini fokus pada **3 prinsip non-negotiable**:

1. **Reasoning over reporting.** Setiap gap yang ditemukan WAJIB melewati 7-step reasoning chain — bukan sekadar "ada selisih, tampilkan angka". Pembaca harus bisa mengikuti alur logika: apa yang teramati, seberapa besar, hipotesis penyebab, evidence test, konklusi dengan confidence, dampak, rekomendasi.
2. **Dual-audience by design.** Output ditulis untuk DUA jenis konsumen — Tim Data (analyst/engineer/DPO) dan Stakeholder Bisnis (Direktur/Manager non-teknis/Regulator). Bukan ringkasan, bukan terjemahan — DUA dokumen yang berdiri sendiri.
3. **Anti-halusinasi guardrail.** Setiap angka traceable ke query SQL atau file source dengan offset/sheet reference. Tidak boleh nulis "kemungkinan", "biasanya", "umumnya" tanpa cite metrik aktual atau DAMA-DMBOK. Jika data tidak cukup → tulis eksplisit `[uncertain — butuh data tambahan: X]`.

**Yang TIDAK dilakukan skill ini:**

- Profiling satu sumber → pakai `data-profiling-baseline`.
- Dokumentasi field-level satu database → pakai `data-doc-generator`.
- Eksekusi rekonsiliasi atau migrasi data → skill ini hanya analisis, bukan mover.
- Penilaian skor kualitas data per dimensi (tidak ada "DQ Score: 78%") — skill ini melaporkan gap + severity berbasis threshold rubric eksplisit.

## Input Modes

Skill MUST auto-detect mode berdasarkan apa yang user sediakan. Jika ambigu, ajukan MAKSIMAL 2 pertanyaan klarifikasi (lihat `assets/workflow.md` Step 2).

### Mode A — Live DB via MCP

PostgreSQL / MySQL / BigQuery / Snowflake / Redshift. Validasi minimum: connection string Source A + Source B + table mapping (atau auto-discover via `information_schema`).

- Profiling otomatis per tabel: `COUNT(*)`, `COUNT(DISTINCT col)`, `MIN`/`MAX`, NULL ratio, top-N values, schema introspection (`information_schema.columns`, `.table_constraints`, `.key_column_usage`), index strategy (`pg_indexes` / equivalent).
- Optimasi performa: gunakan `TABLESAMPLE SYSTEM (1)` untuk tabel >10M baris (catat sampling rate di output, supaya pembaca tahu angka adalah estimasi); `FULL SCAN` untuk tabel <10M.
- Catat connection metadata (host, db, schema, timestamp profiling) sebagai bagian dari Input Inventory di output.

### Mode B — Baca File Profiling Existing

Output dari `data-profiling-baseline` (per-kolom CSV 30+ metrik, markdown report, PNG charts, PDF). Format file yang didukung: `*_per_column.csv`, `*_profile.md`, `*_index.md`.

- Parse CSV per-kolom dari kedua sumber → align by column name → fuzzy match jika nama berbeda. Fuzzy match WAJIB pakai reasoning (semantic match), contoh: `customer_id` ≈ `cust_id` ≈ `id_pelanggan`, `created_at` ≈ `tgl_dibuat` ≈ `dibuat_pada`. Hasil fuzzy match wajib ditampilkan untuk verifikasi user sebelum lanjut.
- Untuk Mode B, dimensi D3 (Distribution & Semantic) bisa dianalisis hanya sebatas metrik yang tersedia di file profiling — jika user butuh KS-test, butuh raw data atau Mode A/C.

### Mode C — Raw File (CSV/XLSX/Parquet/JSON)

- Profile sendiri pakai `pandas` chunked (`chunksize=100_000`) untuk file >500MB; full load untuk file kecil.
- Hitung metrik minimum yang sama dengan Mode A (row count, distinct count, NULL ratio, MIN/MAX, top-N, mean/median/stddev untuk numeric, length stats untuk string).
- Jika XLSX punya >1 sheet, perlakukan setiap sheet sebagai "tabel" terpisah; ajukan mapping ke user.

### Mode D — Schema-only / Data Dictionary

- Input YAML / JSON / markdown schema definition (mis. output `data-doc-generator` G-01/G-03, atau OpenAPI/dbt schema, atau DDL `CREATE TABLE` script).
- Gap analysis terbatas pada **structure-level**: skema diff (D2), tidak bisa D1/D3/D4.
- Skill MUST inform user secara eksplisit di output: *"Mode D aktif — gap analysis terbatas pada structure-level. Untuk volume, distribution, dan temporal gap, butuh data aktual (Mode A/B/C)."*

### Mode Hybrid

Skill MENDUKUNG mix mode (mis. Source A = live DB Mode A, Source B = file profiling Mode B). Ini critical untuk skenario migrasi (sumber masih live, target sudah dimigrasi tapi data hanya tersedia sebagai snapshot file). Catat mode per source di Input Inventory.

## Empat Dimensi Gap (WAJIB Semua Dihitung)

Untuk setiap dimensi, lihat formula eksplisit, threshold default, dan reasoning prompt di `assets/threshold_rubric.md` dan `assets/reasoning_template.md`.

### D1 — Volume & Completeness Gap (Gap Utama)

Apa yang dihitung:

- **Row count delta** per tabel: absolut, persentase, relative diff (`|A-B| / max(A,B)`).
- **Per-table coverage**: tabel ada di A tidak di B (dan sebaliknya) — flag sebagai *missing table A→B* atau *extra table A→B*.
- **NULL ratio per kolom** side-by-side (Source A vs Source B), highlight kolom dengan delta NULL ratio >5pp (percentage point).
- **Distinct value count delta** per kolom kunci (FK candidate, business key, enum).

Reasoning checkpoint: jelaskan KENAPA volume berbeda — apakah filter (mis. soft-delete `where deleted_at is null`), partition window (mis. DWH hanya muat 90 hari terakhir), batch lag (ETL run belum selesai), atau memang scope berbeda (mis. DWH = nationwide, OLTP = satu region).

### D2 — Schema & Structural Gap

Apa yang dihitung:

- **Kolom present di A tidak di B** (dan sebaliknya): flag sebagai *missing column A→B* atau *extra column A→B*.
- **Tipe data delta**: `VARCHAR(255)` vs `TEXT`, `INT` vs `BIGINT`, `TIMESTAMP` vs `TIMESTAMPTZ`, `NUMERIC(10,2)` vs `FLOAT8`. Catat lossy candidates (mis. `BIGINT → INT` = data loss risk).
- **Constraint delta**: `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT value`.
- **Primary key / Foreign key delta**: composite PK berbeda urutan? FK menunjuk tabel berbeda?
- **Index strategy delta**: kolom yang ter-index di A tapi tidak di B (impact: query slow-down setelah migrasi).

Reasoning checkpoint: apakah delta ini **destructive** (data loss risk: `VARCHAR(255) → VARCHAR(100)`, `NOT NULL → NULL`, drop column, drop FK) atau **non-destructive** (widening: `INT → BIGINT`, add column nullable, add index)?

### D3 — Value Distribution & Semantic Gap

Apa yang dihitung:

- **Statistik per-kolom side-by-side**: mean, median, stddev, min, max, mode, top-10 frequency.
- **Kolmogorov-Smirnov test** untuk distribusi numeric (`scipy.stats.ks_2samp`) — flag p-value sesuai threshold rubric.
- **Jaccard similarity** untuk distinct value set kolom kategorikal/enum (`|A ∩ B| / |A ∪ B|`).
- **Cardinality delta**: enum di A ada 5 nilai, di B ada 7 nilai → list nilai yang muncul di salah satu sumber tapi tidak di sumber lain.
- **Unit & format delta**: currency `IDR` vs `USD`, date format `ISO-8601` vs `DD/MM/YYYY`, phone `+62...` vs `08...`, decimal separator `.` vs `,`.

Reasoning checkpoint: apakah perbedaan distribusi mencerminkan beda **PERIODE** (snapshot waktu berbeda), beda **SEGMEN** (region/produk berbeda), atau beda **DEFINISI BISNIS** (mis. `revenue` di A = gross, di B = net)? Ini paling sering jadi sumber miscommunication antar tim.

### D4 — Temporal & Freshness Gap

Apa yang dihitung:

- **Latest timestamp** per tabel/kolom date (`MAX(updated_at)`, `MAX(created_at)`).
- **Update frequency**: rata-rata baris baru per hari selama 30 hari terakhir (`COUNT(*) GROUP BY date(created_at)` lalu rata-rata).
- **Coverage period**: `MIN..MAX` date range di kedua sumber.
- **Lag estimation**: `MAX(updated_at) Source A` − `MAX(updated_at) Source B` = lag berapa jam/hari.

Reasoning checkpoint: apakah lag **wajar** (sesuai SLA ETL batch, mis. T+1 daily) atau **mencurigakan** (broken pipeline, mis. SLA T+1 tapi lag 7 hari)?

## Reasoning Engine — Non-Negotiable

Untuk SETIAP gap finding, skill MUST menjalankan 7-step reasoning chain. Template lengkap dengan contoh ada di `assets/reasoning_template.md`. Ringkasan 7 step:

1. **OBSERVATION** — angka apa yang berbeda? (cite metric + value + source query/file)
2. **MAGNITUDE** — seberapa besar gap-nya? (absolut + relatif + threshold classification: 🟢 minor / 🟡 moderate / 🔴 critical sesuai `assets/threshold_rubric.md`)
3. **HYPOTHESIS** — 2-3 hipotesis penyebab gap (urutkan dari paling probable berdasarkan domain pattern)
4. **EVIDENCE TEST** — data point lain mana yang bisa konfirmasi/refute tiap hipotesis? (mis. cek `deleted_at IS NOT NULL`, cek partition window, cek schema migration log)
5. **CONCLUSION** — hipotesis paling didukung evidence + confidence level (low/medium/high). Jika confidence low → tulis eksplisit `[butuh investigasi lanjut: X]`.
6. **IMPACT** — apa konsekuensi gap ini untuk konsumen data downstream? (BI dashboard salah, regulatory report bias, decision risk)
7. **RECOMMENDATION** — action konkret + owner (siapa yang harus eksekusi) + urgency (sekarang/sprint ini/backlog).

Reasoning chain WAJIB ditulis dalam **narasi paragraf**, BUKAN bullet — supaya pembaca mengikuti alur logika, bukan sekadar nge-skim list.

## Dual-Audience Insight

Setiap gap finding muncul di DUA section terpisah di output. Layer 1 dan Layer 2 berdiri sendiri — Layer 2 BUKAN ringkasan Layer 1.

### Layer 1 — Untuk Tim Data (Analyst, Engineer, DPO)

Lihat template di `assets/layer1_template.md`. Ciri-ciri:

- **Bahasa teknis** — SQL snippet, statistical test name, threshold numerik eksplisit, schema diff dalam format DDL.
- **Konsekuensi teknis** — risiko query break (mis. "WHERE clause yang filter `status='ACTIVE'` akan return 0 baris di Source B karena enum berubah jadi `'active'`"), downstream ETL impact, BI dashboard impact.
- **Action konkret** — `ALTER TABLE` statement, reconciliation query, monitoring rule (Great Expectations / Soda / dbt test config).
- **Referensi DAMA-DMBOK** — link ke `references/dama_kafit.md` (KA-04 Data Quality dimensions, KA-11 Metadata management).

### Layer 2 — Untuk Stakeholder Awam (Direktur, Manager Non-Teknis, Regulator)

Lihat template di `assets/layer2_template.md`. Ciri-ciri:

- **Bahasa bisnis, TANPA istilah teknis** — JANGAN tulis "cardinality", "skema", "constraint", "NULL ratio", "Kolmogorov-Smirnov", "schema diff". Pakai padanan awam.
- **Analogi sehari-hari** — contoh: *"Bayangkan dua daftar absen siswa, satu mencatat 1.000 nama, satu mencatat 850 nama — artinya ada 150 siswa yang tidak tercatat di sistem kedua."*
- **Konsekuensi bisnis** — revenue impact (Rp...), compliance risk (UU/Peraturan apa terlanggar), decision-making risk (keputusan apa yang berisiko salah).
- **Visualisasi** — emoji indicator 🟢/🟡/🔴, ilustrasi naratif, chart sederhana (bar diff, timeline).
- **Action** — pertanyaan strategis yang harus dijawab pimpinan (BUKAN action teknis). Contoh: *"Pimpinan perlu memutuskan: apakah laporan bulanan ke regulator diambil dari Source A atau Source B? Saat ini keduanya menunjukkan angka berbeda 12%."*

## Output Bundle — 4 Artefak (Wajib Semua Ada)

Setiap kali skill dijalankan, hasilkan SEMUA artefak berikut di folder output:

### O1 — `gap_analysis_report.md` (Docusaurus-ready)

Struktur wajib:

1. TOC (auto-generated dari heading)
2. Executive Summary (1 halaman, dominan Layer 2)
3. Scope & Method (mode input yang dipakai, source A/B identity, timestamp profiling)
4. Input Inventory (mapping tabel & kolom across sources, fuzzy match hasil)
5. Dimensi D1 — Volume & Completeness (reasoning chain per finding)
6. Dimensi D2 — Schema & Structural (reasoning chain per finding)
7. Dimensi D3 — Value Distribution & Semantic (reasoning chain per finding)
8. Dimensi D4 — Temporal & Freshness (reasoning chain per finding)
9. Layer 1 Insight — Tim Data (per dimensi)
10. Layer 2 Insight — Stakeholder Bisnis (per dimensi)
11. Recommendations Matrix (severity × dimension × owner × urgency)
12. Appendix — raw metrics, query/file source untuk setiap angka
13. Mermaid diagram side-by-side schema comparison (D2 visual)

### O2 — `gap_analysis_workbook.xlsx` (Multi-sheet)

Sheets wajib:

1. **Cover** — title, source A/B identity, mode, timestamp, jumlah gap finding per severity
2. **Executive Summary** — gap count per dimensi + per severity, top 5 finding
3. **Schema Diff** — side-by-side semua kolom (kolom A, kolom B, type A, type B, constraint A, constraint B, delta flag)
4. **Volume Diff** — per tabel (row count A, row count B, delta abs, delta %, severity)
5. **Distribution Diff** — per kolom numeric/categorical (stats side-by-side, KS p-value, Jaccard sim, severity)
6. **Temporal Diff** — per tabel/kolom date (latest ts A, latest ts B, lag, severity)
7. **Field-Level Gap Matrix** — heatmap conditional formatting (rows = kolom, columns = dimensi D1-D4, cell = severity color)
8. **Recommendations** — flat list (gap_id, dimension, layer1_text, layer2_text, recommendation, owner, urgency)
9. **Raw Metrics Source A** — semua angka yang dihitung, traceable ke query
10. **Raw Metrics Source B** — semua angka yang dihitung, traceable ke query

### O3 — `gap_analysis_executive.pdf` (Polished)

3-5 halaman, polished design. Boleh pakai pattern dari skill `canvas-design`. Embed 3-6 PNG chart:

- Volume bar diff (top 10 tabel dengan delta terbesar)
- NULL ratio heatmap (kolom × source)
- Distribution overlay (1-2 kolom critical, histogram A vs B)
- Temporal lag timeline (per tabel, bar chart lag dalam jam)
- Schema diff scorecard (count missing column, type change, constraint change)
- Severity distribution donut (🟢/🟡/🔴)

Narasi Layer 2 dominan. 1 halaman terakhir = Recommendations untuk Pimpinan (3-5 keputusan strategis, bukan to-do teknis).

### O4 — `gap_findings.json` (Machine-readable)

Schema (designed untuk CI gate, observability integration, downstream automation):

```json
{
  "metadata": {
    "skill_version": "1.0.0",
    "generated_at": "ISO-8601",
    "mode_source_a": "A|B|C|D",
    "mode_source_b": "A|B|C|D"
  },
  "source_a": { "identity": "...", "tables": [...], "row_count_total": 0 },
  "source_b": { "identity": "...", "tables": [...], "row_count_total": 0 },
  "gaps": [
    {
      "gap_id": "D1-001",
      "dimension": "D1|D2|D3|D4",
      "severity": "🟢|🟡|🔴",
      "observation": "...",
      "magnitude": { "absolute": 0, "relative": 0.0, "unit": "..." },
      "hypothesis": ["...", "...", "..."],
      "evidence_test": "...",
      "conclusion": "...",
      "confidence": "low|medium|high",
      "impact": "...",
      "recommendation": "...",
      "owner": "...",
      "urgency": "now|sprint|backlog",
      "layer1_text": "...",
      "layer2_text": "...",
      "source_trace": { "query_or_file": "...", "offset_or_sheet": "..." }
    }
  ],
  "summary": {
    "total_gaps": 0,
    "by_severity": { "critical": 0, "moderate": 0, "minor": 0 },
    "by_dimension": { "D1": 0, "D2": 0, "D3": 0, "D4": 0 }
  }
}
```

## Threshold & Severity Rubric

Default threshold (user boleh override via config — lihat `assets/threshold_rubric.md`):

| Dimensi | Indikator | 🟢 Minor | 🟡 Moderate | 🔴 Critical |
|---|---|---|---|---|
| D1 Volume | Row count diff % | <2% | 2-10% | >10% |
| D1 Completeness | NULL ratio delta (pp) | <2pp | 2-10pp | >10pp |
| D2 Schema | Tipe data change non-destructive | — | catat | — |
| D2 Schema | Tipe data change destructive | — | — | flag |
| D2 Schema | Drop column / drop FK / NOT-NULL→NULL | — | — | flag |
| D3 Distribution | KS test p-value | >0.05 | 0.01-0.05 | <0.01 |
| D3 Distribution | Jaccard similarity (enum) | >0.95 | 0.80-0.95 | <0.80 |
| D4 Temporal | Lag vs SLA | <50% SLA | 50-100% SLA | >SLA |

**Override mechanism:** user boleh kirim `config.yaml` di awal sesi dengan key `thresholds:` — skill akan merge dengan default. Jika tidak ada config, pakai default rubric di atas dan catat di output bahwa default dipakai.

## Anti-Halusinasi Guardrail

Aturan baku — wajib dipatuhi setiap kali skill ini dijalankan:

1. **Setiap angka di report HARUS traceable** ke query SQL atau file source dengan offset/sheet reference. Skill MUST mengisi field `source_trace` di setiap gap di `gap_findings.json`. Di report MD/XLSX, sertakan footnote atau kolom "Source" yang menunjuk ke query/file.
2. **JANGAN PERNAH menulis "kemungkinan", "biasanya", "umumnya", "secara teori"** tanpa cite source DAMA-DMBOK (lihat `references/dama_kafit.md`) atau metrik aktual yang dihitung.
3. **Jika data tidak cukup untuk konklusi → tulis eksplisit** `[uncertain — butuh data tambahan: X]`. JANGAN tebak. Lebih baik confidence rendah + jujur daripada confidence palsu.
4. **Reasoning chain WAJIB tampil di output**, BUKAN hanya konklusi. Setiap gap finding di `gap_analysis_report.md` harus punya 7-step chain visible — pembaca perlu melihat alur, bukan hanya jawaban.
5. **Fuzzy column matching** (Mode B) wajib di-confirm dengan user sebelum dipakai. Tampilkan hasil match → user approve → lanjut. Jika user tidak respons, default ke "exact match only" dan flag mismatch sebagai `[unmatched — butuh konfirmasi user]`.

## Workflow Step-by-Step

Lihat detail di `assets/workflow.md`. Ringkasan 10 langkah:

1. Intake & validation input → deteksi mode A/B/C/D atau hybrid
2. Klarifikasi business context (MAX 2 pertanyaan: nama business entity yang dibandingkan, tujuan: migrasi/rekonsiliasi/audit/parity check)
3. Inventory & alignment → mapping tabel & kolom across sources, fuzzy match dengan reasoning
4. Profiling execution per mode
5. Gap calculation per 4 dimensi (D1-D4)
6. Reasoning chain generation per gap finding (7 step)
7. Layer 1 (Tim Data) writeup
8. Layer 2 (Awam) writeup
9. Bundle generation (MD + XLSX + PDF + JSON)
10. Self-verification checklist sebelum present ke user

## Integration dengan Skill Lain

- **`data-profiling-baseline`** — output `*_per_column.csv` jadi input Mode B. Jika user belum profile salah satu sumber, panggil skill ini lebih dulu untuk generate profiling, baru lanjut gap analysis.
- **`data-doc-generator`** — G-01 (Data Vocabulary) dan G-03 (Data Dictionary) dipakai sebagai referensi semantik. Jika user sudah punya kamus data, gap finding D3 (Semantic) bisa di-cross-check ke definisi resmi.
- **`openmetadata-catalog-manager`** — `gap_findings.json` bisa di-publish ke OpenMetadata sebagai `test_case` (Critical → fail, Moderate → warning, Minor → info) dan ke `incident` jika severity 🔴. Skill `openmetadata-catalog-manager` punya tool yang nerima JSON ini.
- **`dama-research`** — referensi metodologis ada di `references/dama_kafit.md`, terutama KA-04 (Data Quality) dimensions: Completeness, Validity, Consistency, Timeliness, Uniqueness, Accuracy. Mapping ke 4 dimensi gap analysis ini ada di file tersebut.

## Catatan Operasional

- Skill ini fokus **dua sumber**. Jika user butuh bandingkan >2 sumber, ulangi skill secara pairwise (A vs B, A vs C, B vs C) dan agregat manual — JANGAN paksa ke N-way dalam satu run.
- Untuk migrasi project skala besar, jalankan gap analysis sebelum cutover (baseline), saat dual-run (parity check), dan setelah cutover (final reconciliation) — total 3 run, simpan history-nya untuk audit trail.
- Output `gap_findings.json` bisa di-feed ke CI/CD gate — definisikan rule "Critical gap count == 0" sebagai gate sebelum promote ke production.
