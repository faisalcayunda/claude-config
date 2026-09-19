# `gap_analysis_executive.pdf` — Layout Reference

PDF eksekutif 3-5 halaman, polished design. Untuk demo case "DWH vs OLTP Fictional", layout PDF mengikuti spec berikut. PDF biner sebenarnya dibangun saat skill dijalankan (pakai `reportlab` atau pattern dari skill `canvas-design`).

## Cover Page (Halaman 1)

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│                                                         │
│         GAP ANALYSIS REPORT                             │
│         DWH vs OLTP — Order Management                  │
│                                                         │
│         Rekonsiliasi Pre-Audit Q1 2026                  │
│                                                         │
│                                                         │
│         [Donut chart Severity Distribution]             │
│         🔴 2 Critical                                   │
│         🟡 2 Moderate                                   │
│         🟢 1 Minor                                      │
│                                                         │
│                                                         │
│         Generated: 2026-05-23 14:00 WIB                 │
│         By: data-gap-analyst v1.0.0                     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Halaman 2 — Executive Summary

Narasi Layer 2 dominan (bahasa awam). Embed 2 PNG chart:

- **Chart 1**: Volume bar diff (top 4 tabel dengan delta terbesar) — `chart_volume_diff.png`
- **Chart 2**: NULL ratio heatmap (kolom × source) — `chart_null_heatmap.png`

Teks:

> Dari 5 perbedaan yang ditemukan antara sistem operasional dan sistem laporan, 3 di antaranya butuh keputusan pimpinan dalam waktu dekat:
>
> **🔴 Selisih ~150 ribu pesanan** — sistem laporan tidak mencatat pesanan batal/gagal. Berisiko mismatch ke regulator.
>
> **🔴 Email pelanggan kosong di sistem laporan** — semua kampanye marketing email dari sistem laporan akan return nol. Tim marketing kemungkinan workaround langsung ke operasional.
>
> **🟡 Kode diskon belum masuk sistem laporan** — tim BI tidak bisa analisis efektivitas program promo Q1.

## Halaman 3 — Top 3 Finding Detail

Untuk masing-masing 3 critical finding teratas, satu blok Layer 2 lengkap dengan:

- Judul friendly (mis. "Selisih ~150 ribu pesanan antara dua sistem")
- 1 paragraf narasi (bukan teknis)
- 1 analogi sehari-hari
- 1 paragraf konsekuensi
- 2-3 pertanyaan strategis untuk pimpinan

Embed: distribution overlay chart untuk amount — `chart_distribution_overlay.png`

## Halaman 4 — Visual Summary

Embed 3 chart sekaligus:

- **Chart 4**: Temporal lag timeline (per tabel) — `chart_temporal_lag.png`
- **Chart 5**: Schema diff scorecard (count missing column, type change) — `chart_schema_scorecard.png`
- **Chart 6**: Severity distribution donut — `chart_severity_donut.png`

Narasi singkat: "Distribusi gap per dimensi menunjukkan area utama yang butuh attention: volume & completeness (2 critical) yang berdampak ke akurasi laporan."

## Halaman 5 — Recommendations untuk Pimpinan

3-5 keputusan strategis (BUKAN to-do teknis):

1. **Putuskan source-of-truth untuk laporan regulator** — operasional atau laporan?
2. **Tutup review kebijakan PII email** yang sudah 6 bulan tertahan
3. **Tetapkan policy SLA replicate** — feature baru di operasional WAJIB ada di laporan dalam X hari

Footer: kontak Data Steward + DPO + Data Engineer Lead untuk follow-up.

## Daftar PNG yang Dibutuhkan

| File | Dimensi | Sumber Data |
|---|---|---|
| `chart_volume_diff.png` | 1200×600 | Sheet 4 Volume Diff |
| `chart_null_heatmap.png` | 1200×800 | Per-column NULL ratio A vs B |
| `chart_distribution_overlay.png` | 1200×600 | Histogram amount A vs B |
| `chart_temporal_lag.png` | 1200×400 | Sheet 6 Temporal Diff |
| `chart_schema_scorecard.png` | 800×800 | Sheet 3 Schema Diff aggregate |
| `chart_severity_donut.png` | 600×600 | Summary severity count |

PNG di-generate runtime pakai `matplotlib` atau `plotly` (dengan `kaleido` untuk export PNG). Disimpan di subdirectory `charts/` di output folder.

---

*PDF biner di-generate runtime oleh `scripts/render_bundle.py`. File ini adalah blueprint, bukan output biner.*
