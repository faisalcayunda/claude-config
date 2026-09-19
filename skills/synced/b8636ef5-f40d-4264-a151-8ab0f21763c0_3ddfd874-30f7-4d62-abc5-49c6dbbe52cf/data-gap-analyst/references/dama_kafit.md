# DAMA-DMBOK Mapping — `data-gap-analyst`

Referensi metodologis untuk semua reasoning dan recommendation di skill ini. Berdasarkan DAMA-DMBOK2 (2nd Edition, 2017), khususnya **KA-04 Data Quality** dan **KA-11 Metadata Management**.

Skill `dama-research` punya cakupan lengkap KA-01 s/d KA-14. File ini hanya extract bagian yang relevan untuk gap analysis dua sumber.

## 1. Pemetaan 4 Dimensi Gap Analysis ke DAMA-DMBOK KA-04 Data Quality

KA-04 mendefinisikan 6 dimensi data quality:

| DAMA KA-04 Dimension | Definisi (DMBOK2 §13.1.3) | Relevan ke Dimensi Skill |
|---|---|---|
| Accuracy | Sejauh mana data merepresentasikan entitas dunia nyata secara benar | D3 (semantic delta) |
| Completeness | Sejauh mana semua data yang diharapkan tersedia | D1 (volume + NULL ratio) |
| Consistency | Sejauh mana nilai konsisten antar sistem/copy data | **D1, D2, D3 — core fokus skill ini** |
| Timeliness | Sejauh mana data tersedia tepat waktu untuk dipakai | D4 (freshness) |
| Uniqueness | Sejauh mana tidak ada duplikasi unintended | D1 (distinct count) |
| Validity | Sejauh mana data sesuai aturan format/domain | D2 (constraint), D3 (format) |

Untuk SETIAP gap finding di Layer 1, skill MUST cite dimensi DAMA-DMBOK yang relevan. Contoh: gap volume karena ETL filter → cite **Completeness** + **Consistency**.

## 2. Definisi Operasional Per Dimensi DAMA (Saat Reasoning)

### Completeness (DMBOK2 §13.1.3.2)

> *"Completeness has two aspects: the completeness of the data structure (all required data elements are present), and the completeness of the data content (the data elements have appropriate values)."* — DMBOK2 hal. 459.

Pemakaian di skill ini:

- **Structural completeness**: cek apakah kolom yang ada di Source A juga ada di Source B (D2).
- **Content completeness**: cek NULL ratio per kolom side-by-side (D1).

### Consistency (DMBOK2 §13.1.3.3)

> *"Consistency can mean that data values, formats, and definitions are the same in all source systems where they are stored."* — DMBOK2 hal. 459.

Pemakaian di skill ini — **inti utama skill**:

- **Value consistency** — apakah nilai untuk entity yang sama match antar sumber (D3).
- **Format consistency** — apakah format penulisan match (D3 unit/format delta).
- **Definition consistency** — apakah definisi bisnis match (D3 semantic — perlu cross-check ke G-01 Data Vocabulary via `data-doc-generator`).

### Timeliness (DMBOK2 §13.1.3.5)

> *"Timeliness refers to the expectation that data will be available within an expected time frame."* — DMBOK2 hal. 460.

Pemakaian di skill ini:

- **Currency/Freshness** — selisih `MAX(updated_at)` antar sumber (D4 lag).
- **Latency** — selisih waktu antara event terjadi vs muncul di sistem (jika ada `event_time` dan `loaded_at`).

### Validity (DMBOK2 §13.1.3.6)

> *"Validity refers to whether data values are consistent with a defined domain of values."* — DMBOK2 hal. 460.

Pemakaian di skill ini:

- **Domain validity** — apakah enum values sama (D3 Jaccard, cardinality delta).
- **Format validity** — apakah format date/phone/currency match (D3).
- **Constraint validity** — apakah constraint NOT NULL/UNIQUE/CHECK match (D2).

## 3. KA-11 Metadata Management — Relevansi ke Gap Analysis

Per DMBOK2 §12, metadata management mencakup business glossary, data lineage, dan technical metadata. Untuk gap analysis:

### 3.1 Business Glossary Alignment (DMBOK2 §12.1.3.1)

Jika gap D3 (semantic) muncul karena dua sumber pakai definisi bisnis yang berbeda (mis. `revenue` = gross di OLTP, = net di DWH), itu adalah **business glossary alignment issue**. Skill MUST recommend:

1. Cross-check definisi di G-01 Data Vocabulary (via `data-doc-generator`)
2. Jika definisi belum ada di glossary → eskalasi ke Data Steward untuk finalisasi
3. Sebelum finalisasi → semua dokumentasi dan dashboard yang pakai term ini harus pakai disclaimer "[definisi sedang dalam review]"

### 3.2 Data Lineage (DMBOK2 §12.1.3.3)

Jika gap D1 (volume) ditemukan dan hipotesis paling kuat adalah ETL filter, skill MUST recommend:

1. Update lineage documentation di OpenMetadata (via `openmetadata-catalog-manager`) untuk Source B dengan note "ETL filter: WHERE X = Y"
2. Tambah test case di OpenMetadata: `row_count_ratio(SourceA, SourceB) within (expected_ratio ± tolerance)`
3. Jika lineage belum ada → eskalasi ke Data Engineer Lead untuk add ke catalog

### 3.3 Technical Metadata Sync (DMBOK2 §12.1.3.2)

Jika gap D2 (schema) ditemukan, skill MUST recommend update technical metadata di kedua sumber:

1. Update data dictionary di kedua sumber dengan schema yang baru
2. Tambah versioning di metadata (mis. `schema_version: v2.3.1`)
3. Tambah migration log untuk tracking historical schema changes

## 4. Citation Style untuk Anti-Halusinasi

Setiap kali skill referensi DAMA-DMBOK, pakai format:

```
DMBOK2 §<chapter>.<section>, hal. <page>
```

Contoh:

- `DMBOK2 §13.1.3.2, hal. 459` (Completeness definition)
- `DMBOK2 §13.1.3.3, hal. 459` (Consistency definition)
- `DMBOK2 §12.1.3.1` (Business Glossary)
- `DMBOK2 §12.1.3.3` (Data Lineage)

Jika skill tidak ingat halaman pasti, tulis `DMBOK2 KA-<n>` saja — JANGAN ngarang nomor halaman. Anti-halusinasi guardrail berlaku juga untuk citation.

## 5. Mapping Cepat Severity ↔ DAMA Recommendation

| Severity | DAMA Recommendation Action |
|---|---|
| 🔴 Critical | Treat sebagai DQ Incident (DMBOK2 §13.1.4), eskalasi ke Data Steward + Data Owner, buka tiket di issue tracker, target resolve dalam <SLA> |
| 🟡 Moderate | Catat sebagai DQ Finding, bahas di forum Data Governance reguler (DMBOK2 §3.1.3.2), buat improvement plan untuk sprint berikutnya |
| 🟢 Minor | Catat sebagai DQ Note, monitor di dashboard DQ — tidak butuh action segera |

## 6. Referensi Lanjutan

- DAMA-DMBOK2, Chapter 13 (Data Quality) — landasan KA-04 dimensions
- DAMA-DMBOK2, Chapter 12 (Metadata Management) — landasan KA-11
- ISO 8000-8:2015 Information and data quality — fundamental concepts
- ISO/IEC 25012:2008 Software product Quality Requirements and Evaluation — Data quality model
- Untuk pembahasan modern (data mesh, data contracts, data observability) → panggil skill `dama-research` atau `data-management-researcher`
