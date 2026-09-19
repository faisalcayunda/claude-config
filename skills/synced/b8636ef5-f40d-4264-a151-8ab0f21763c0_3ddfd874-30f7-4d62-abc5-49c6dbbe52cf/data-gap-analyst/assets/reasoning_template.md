# Reasoning Chain Template — 7 Steps

Setiap gap finding WAJIB ditulis mengikuti template ini. Bentuk akhir adalah **narasi paragraf**, BUKAN bullet — supaya pembaca mengikuti alur logika, bukan nge-skim list.

## Template Kerangka

```
**Gap ID: [DIM]-[NNN]** | Severity: [🟢/🟡/🔴] | Confidence: [low/medium/high]

[Paragraf 1 — OBSERVATION]
Pada tabel `<table>` kolom `<column>`, terobservasi <metric> sebesar <value_A>
di Source A versus <value_B> di Source B (source trace: <query atau file +
offset>). Selisih absolut <abs>, relatif <rel%>.

[Paragraf 2 — MAGNITUDE]
Mengacu rubric threshold (lihat `assets/threshold_rubric.md`), selisih ini
masuk kategori <minor/moderate/critical> karena <alasan kuantitatif>. Untuk
konteks: threshold critical adalah <X>, observasi kita <Y> kali lipat di atas
itu / <Y%> di atas batas moderate.

[Paragraf 3 — HYPOTHESIS]
Ada tiga hipotesis penyebab gap, diurutkan dari paling probable berdasarkan
pattern domain <entity>:
- (H1) <hipotesis paling probable> — rasional: <kenapa probable>
- (H2) <hipotesis kedua> — rasional: <kenapa>
- (H3) <hipotesis ketiga, less likely tapi worth checking> — rasional: <kenapa>

[Paragraf 4 — EVIDENCE TEST]
Untuk membedakan ketiga hipotesis, cek data point berikut:
- Untuk H1: <query/check spesifik>. Hasil: <hasil aktual atau "belum dicek">.
- Untuk H2: <query/check spesifik>. Hasil: <hasil>.
- Untuk H3: <query/check spesifik>. Hasil: <hasil>.

[Paragraf 5 — CONCLUSION]
Berdasarkan evidence test, hipotesis yang paling didukung adalah <Hx>, karena
<reasoning dari evidence>. Confidence: <low/medium/high>. <Jika low: butuh
investigasi tambahan untuk <X>.>

[Paragraf 6 — IMPACT]
Konsekuensi gap ini untuk konsumen data downstream:
<narasi konkret konsekuensi — siapa terkena, apa yang break, berapa magnitudo
risiko bisnis>.

[Paragraf 7 — RECOMMENDATION]
Action yang direkomendasikan: <action konkret>. Owner: <role/tim>. Urgency:
<now / sprint ini / backlog>.
```

## Contoh Lengkap (Fictional — DWH vs OLTP)

**Gap ID: D1-003** | Severity: 🔴 Critical | Confidence: high

Pada tabel `orders` di Source A (OLTP `prod_oltp.orders`) tercatat 1.247.892 baris untuk periode 2026-01-01 sampai 2026-05-23, sementara Source B (DWH `dwh.fact_orders`) hanya tercatat 1.103.456 baris untuk periode yang sama (source trace: `SELECT COUNT(*) FROM prod_oltp.orders WHERE created_at BETWEEN '2026-01-01' AND '2026-05-23'` vs `SELECT COUNT(*) FROM dwh.fact_orders WHERE order_date BETWEEN '2026-01-01' AND '2026-05-23'`). Selisih absolut 144.436 baris, selisih relatif 11,6%.

Mengacu rubric threshold di `assets/threshold_rubric.md`, selisih volume 11,6% masuk kategori 🔴 Critical karena melebihi ambang batas 10%. Untuk konteks: threshold moderate adalah 2–10%, observasi kita 1,16 kali batas critical — jadi bukan borderline, tetapi memang signifikan.

Ada tiga hipotesis penyebab gap, diurutkan dari paling probable berdasarkan pattern domain Order management. Pertama, ETL filter di DWH membuang baris dengan `status='CANCELLED'` atau `status='FAILED'` (rasional: praktik umum DWH hanya muat valid completed orders untuk reporting). Kedua, batch lag — ETL terakhir run di T-1 jadi data 1 hari terakhir belum muncul di DWH (rasional: SLA standar DWH adalah T+1). Ketiga, soft-delete di OLTP yang tidak ter-replicate ke DWH (rasional: design DWH biasanya hard-delete via ETL filter `WHERE deleted_at IS NULL`).

Untuk membedakan ketiga hipotesis, perlu cek data point berikut. Untuk H1: `SELECT status, COUNT(*) FROM prod_oltp.orders WHERE created_at BETWEEN '2026-01-01' AND '2026-05-23' GROUP BY status`. Hasil aktual: `CANCELLED: 142.103`, `FAILED: 2.891`, total 144.994 — sangat mendekati gap 144.436. Untuk H2: `SELECT MAX(loaded_at) FROM dwh.etl_audit WHERE table_name='fact_orders'`. Hasil: 2026-05-22 23:15:00, jadi ada lag <24 jam yang menjelaskan sebagian kecil gap tapi bukan mayoritas. Untuk H3: `SELECT COUNT(*) FROM prod_oltp.orders WHERE deleted_at IS NOT NULL AND created_at BETWEEN '2026-01-01' AND '2026-05-23'`. Hasil: 558 baris — tidak signifikan.

Berdasarkan evidence test, hipotesis yang paling didukung adalah H1 (ETL filter status), karena gap 144.436 sangat mendekati total CANCELLED+FAILED sebesar 144.994. Sisa selisih 558 baris bisa dijelaskan dengan H3 (soft-delete) dan sisanya batch lag normal. Confidence: high.

Konsekuensi gap ini untuk konsumen data downstream: laporan revenue harian yang ditarik dari DWH akan secara konsisten underreport ~11% transaksi yang sebenarnya terjadi di OLTP. Untuk dashboard internal ini mungkin acceptable (memang ingin lihat completed only), tapi jika dipakai untuk laporan regulator atau reconciliation finansial, akan menyebabkan mismatch dengan sistem akuntansi yang menghitung semua transaksi termasuk yang failed. Risiko: temuan audit "data warehouse tidak match dengan source system", potensi cost ~Rp 50–200 juta untuk explanation/remediation.

Action yang direkomendasikan: dokumentasikan ETL filter `WHERE status NOT IN ('CANCELLED','FAILED')` secara eksplisit di `data-doc-generator` G-03 untuk tabel `dwh.fact_orders`, dan tambahkan kolom `is_cancelled` / `is_failed` di DWH supaya bisa dipakai untuk reconciliation. Owner: Data Engineer Lead + Data Steward Order Domain. Urgency: sprint ini (sebelum cycle audit regulator berikutnya).

## Catatan Operasional

- **Panjang narasi**: paragraf 1-2 singkat (1-3 kalimat); paragraf 3-5 bisa lebih panjang (3-6 kalimat) sesuai kompleksitas; paragraf 6-7 fokus dan actionable.
- **Tone**: ilmiah-investigatif. Hindari nada defensif ("mungkin saja...", "bisa jadi..."). Pakai bahasa observasional ("terobservasi...", "evidence menunjukkan...", "berdasarkan data...").
- **Confidence rendah jangan ditutup-tutupi**: jika evidence tidak cukup, tulis confidence: low + sebutkan apa yang butuh dicek tambahan. JANGAN paksa konklusi confidence high padahal evidence tipis.
- **Anti-halusinasi**: setiap angka di narasi WAJIB ada di `source_trace` di `gap_findings.json`. Reviewer harus bisa replay query/file dan dapat angka yang sama.
