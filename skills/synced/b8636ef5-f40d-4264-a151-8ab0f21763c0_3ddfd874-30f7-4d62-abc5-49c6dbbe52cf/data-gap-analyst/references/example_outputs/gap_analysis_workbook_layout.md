# `gap_analysis_workbook.xlsx` — Layout Reference

File ini mendeskripsikan struktur XLSX yang di-generate `scripts/render_bundle.py`. Untuk demo case "DWH vs OLTP Fictional", workbook akan punya 10 sheet seperti di bawah.

XLSX biner sebenarnya dibangun saat skill dijalankan (di runtime, butuh `openpyxl`). File ini adalah blueprint/spec, bukan output binari.

## Sheet 1 — Cover

| Field | Value |
|---|---|
| Report Title | Gap Analysis Report — DWH vs OLTP |
| Source A | `prod_oltp.public` (PostgreSQL 15) |
| Source B | `dwh.mart` (Snowflake) |
| Mode | Hybrid (A: live DB, B: file profiling) |
| Business Entity | Order Management |
| Purpose | Rekonsiliasi pre-audit Q1 2026 |
| Generated At | 2026-05-23 14:00 WIB |
| Skill Version | 1.0.0 |
| Total Gaps | 5 (🔴 2 / 🟡 2 / 🟢 1) |

## Sheet 2 — Executive Summary

Pivot: count per dimension × per severity.

| Dimension | 🟢 Minor | 🟡 Moderate | 🔴 Critical | Total |
|---|---|---|---|---|
| D1 Volume & Completeness | 0 | 0 | 2 | 2 |
| D2 Schema & Structural | 0 | 1 | 0 | 1 |
| D3 Value Distribution | 0 | 1 | 0 | 1 |
| D4 Temporal & Freshness | 1 | 0 | 0 | 1 |
| **Total** | **1** | **2** | **2** | **5** |

Top 5 Finding (sort by severity then dimension):

1. D1-001 🔴 `orders` row count gap 11.6%
2. D1-002 🔴 `customer_email` NULL 100% di DWH
3. D2-001 🟡 `discount_code` missing di DWH
4. D3-001 🟡 KS test p-value 0.003 untuk `amount`
5. D4-001 🟢 Lag DWH 18 jam (75% SLA)

## Sheet 3 — Schema Diff

Side-by-side semua kolom (rows). Highlight cells dengan conditional formatting (red bg for destructive, yellow for moderate).

| Column A | Type A | Constraint A | Column B | Type B | Constraint B | Delta Flag |
|---|---|---|---|---|---|---|
| id | BIGINT | PK NOT NULL | order_id | BIGINT | PK NOT NULL | OK (renamed, semantic match) |
| customer_id | BIGINT | FK NOT NULL | customer_key | BIGINT | FK NOT NULL | OK |
| status | VARCHAR(20) | NOT NULL CHECK IN ('COMPLETED','CANCELLED','FAILED') | order_status | VARCHAR(20) | NOT NULL | 🟡 missing CHECK in B |
| amount | NUMERIC(12,2) | NOT NULL | order_amount_idr | NUMERIC(14,2) | NOT NULL | OK (widening) |
| created_at | TIMESTAMPTZ | NOT NULL | order_date | TIMESTAMP | NOT NULL | 🟡 timezone lost |
| customer_email | VARCHAR(255) | NULL | customer_email | VARCHAR(255) | NULL | 🔴 100% NULL in B (D1-002) |
| discount_code | VARCHAR(50) | NULL | — | — | — | 🟡 missing in B (D2-001) |
| deleted_at | TIMESTAMPTZ | NULL | — | — | — | 🟢 missing in B (intended) |

## Sheet 4 — Volume Diff

| Table A | Row Count A | Table B | Row Count B | Delta Abs | Delta % | Severity | Gap ID |
|---|---|---|---|---|---|---|---|
| orders | 1.247.892 | fact_orders | 1.103.456 | 144.436 | 11.58% | 🔴 | D1-001 |
| order_items | 3.842.105 | fact_order_items | 3.398.210 | 443.895 | 11.55% | 🔴 | (derivative D1-001) |
| customers | 312.450 | dim_customer | 312.448 | 2 | 0.00% | 🟢 | — |
| coupons | 1.247 | — | — | 1.247 | 100% | 🔴 | D2-002 (table missing) |

## Sheet 5 — Distribution Diff

| Column | Mean A | Mean B | Median A | Median B | Stddev A | Stddev B | KS p-value | Jaccard | Severity |
|---|---|---|---|---|---|---|---|---|---|
| amount | 487.234 | 432.108 | 250.000 | 250.000 | 1.245.678 | 1.102.456 | 0.003 | — | 🟡 |
| status | — | — | — | — | — | — | — | 0.93 (3 vs 1 distinct) | 🟡 |
| customer_email | — | — | — | — | — | — | — | 0.00 (B all NULL) | 🔴 |

## Sheet 6 — Temporal Diff

| Table | MAX(updated_at) A | MAX(updated_at) B | Lag (hours) | SLA (hours) | Lag % SLA | Severity | Gap ID |
|---|---|---|---|---|---|---|---|
| orders ↔ fact_orders | 2026-05-23 13:42 | 2026-05-22 20:00 | 17.7 | 24 | 73.8% | 🟢 | D4-001 |
| customers ↔ dim_customer | 2026-05-22 16:30 | 2026-05-22 17:00 | -0.5 | 24 | n/a | 🟢 | — |

## Sheet 7 — Field-Level Gap Matrix (Heatmap)

Conditional formatting: Red bg for 🔴, Yellow for 🟡, Green for 🟢, Gray for OK.

| Field | D1 Volume | D1 Completeness | D2 Schema | D3 Distribution | D4 Temporal |
|---|---|---|---|---|---|
| orders.id ↔ fact_orders.order_id | 🔴 | OK | OK | OK | 🟢 |
| orders.status | 🔴 | OK | 🟡 | 🟡 | — |
| orders.amount | 🔴 | OK | OK | 🟡 | — |
| orders.customer_email | OK | 🔴 | OK | 🔴 | — |
| orders.discount_code | — | — | 🟡 | — | — |

## Sheet 8 — Recommendations

| Gap ID | Dimension | Severity | Layer 1 (excerpt) | Layer 2 (excerpt) | Recommendation | Owner | Urgency |
|---|---|---|---|---|---|---|---|
| D1-001 | D1 | 🔴 | ALTER TABLE fact_orders ADD is_cancelled BOOLEAN | Sistem laporan kurang ~150 ribu pesanan dibanding operasional | DDL change + backfill + glossary | DE Lead + DS Order | Sprint |
| D1-002 | D1 | 🔴 | Tutup PDP-2025-089, apply SHA256 hash | Email pelanggan kosong di sistem laporan | PII decision + ETL re-enable | DPO + DE Lead | Now |
| D2-001 | D2 | 🟡 | Update fact_orders_load.sql + backfill 3 bulan | Fitur diskon belum masuk laporan | ETL update + backfill | DE Lead | Sprint |
| D3-001 | D3 | 🟡 | Auto-resolve after D1-001 | Auto-resolve setelah point pertama dibenahi | Glossary update | DS Order | Backlog |
| D4-001 | D4 | 🟢 | Dashboard freshness badge | Tambah label "data per kemarin malam" | UX update | BI Eng | Backlog |

## Sheet 9 — Raw Metrics Source A

Semua angka yang dihitung dari Source A, lengkap dengan query yang dipakai (kolom `source_query`). Pembaca harus bisa replay query dan dapat angka yang sama.

## Sheet 10 — Raw Metrics Source B

Sama dengan sheet 9, tapi untuk Source B. Untuk Mode B (file profiling), source = file CSV + row reference.

---

*Workbook XLSX di-generate runtime oleh `scripts/render_bundle.py` pakai `openpyxl`. Conditional formatting di-apply via `openpyxl.formatting.rule.PatternFill`. File ini adalah blueprint, bukan biner output.*
