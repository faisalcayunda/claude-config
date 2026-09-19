# Layer 1 Template — Untuk Tim Data

Insight teknis untuk Analyst, Data Engineer, Data Steward, DPO. Pakai bahasa teknis tanpa filter — pembaca diasumsikan paham SQL, schema, ETL, dan statistical test.

## Kerangka Wajib

```
### [Gap ID — Judul Singkat Teknis]

**Severity**: [🟢/🟡/🔴] | **Dimension**: [D1/D2/D3/D4] | **Confidence**: [low/medium/high]

**Observation (technical)**
<Deskripsi teknis: metric name, value side-by-side, formula, source query.>

**Schema/Distribution Diff**
```sql
-- Source A
<DDL atau query yang menghasilkan angka A>

-- Source B
<DDL atau query yang menghasilkan angka B>

-- Delta query (reconciliation)
<query yang langsung menampilkan selisih>
```

**Technical Impact**
- Query break risk: <SQL pattern yang akan return wrong result>
- Downstream ETL impact: <pipeline yang terkena, schedule break>
- BI dashboard impact: <dashboard/report yang akan miss-render>
- Referential integrity: <FK yang berisiko orphan>

**Action — DDL / Monitoring**

`ALTER TABLE` atau `UPDATE` statement untuk fix:

```sql
<DDL atau DML konkret>
```

Monitoring rule (Great Expectations):

```yaml
<expectation config>
```

Atau monitoring rule (Soda):

```yaml
<soda check>
```

Atau monitoring rule (dbt test):

```yaml
<dbt test config>
```

**Referensi DAMA-DMBOK**
- KA-04 Data Quality dimension: <Completeness/Validity/Consistency/Timeliness/Uniqueness/Accuracy> — lihat `references/dama_kafit.md`
- KA-11 Metadata Management: <topik relevan, mis. lineage, business glossary alignment>
```

## Contoh — D1 Volume Gap

### D1-003 — `dwh.fact_orders` Underreports OLTP by 11.6%

**Severity**: 🔴 Critical | **Dimension**: D1 | **Confidence**: high

**Observation (technical)**

Row count `dwh.fact_orders` untuk periode `2026-01-01` s/d `2026-05-23` adalah 1.103.456, sementara `prod_oltp.orders` untuk periode yang sama 1.247.892. Delta absolut 144.436 baris, delta relatif 11,6% — melebihi threshold critical 10%.

**Schema/Distribution Diff**

```sql
-- Source A (OLTP)
SELECT COUNT(*)
FROM prod_oltp.orders
WHERE created_at BETWEEN '2026-01-01' AND '2026-05-23';
-- 1,247,892

-- Source B (DWH)
SELECT COUNT(*)
FROM dwh.fact_orders
WHERE order_date BETWEEN '2026-01-01' AND '2026-05-23';
-- 1,103,456

-- Delta breakdown (hypothesis H1: status filter di ETL)
SELECT status, COUNT(*) AS cnt
FROM prod_oltp.orders
WHERE created_at BETWEEN '2026-01-01' AND '2026-05-23'
GROUP BY status
ORDER BY cnt DESC;
-- COMPLETED 1,102,898
-- CANCELLED   142,103
-- FAILED        2,891
```

**Technical Impact**

- Query break risk: tidak — ETL berjalan sesuai design. Tapi konsumen yang asumsi `fact_orders` = `orders` akan dapat angka salah.
- Downstream ETL impact: dashboard `revenue_daily_v2`, `region_performance`, `regulator_monthly_report` semua di-feed dari `fact_orders` — semua underreport 11,6% revenue gross.
- BI dashboard impact: laporan ke regulator (BI/OJK/Kemenkeu) mismatch dengan sistem akuntansi yang count dari OLTP.
- Referential integrity: tidak terdampak (FK utuh di kedua sumber).

**Action — DDL / Monitoring**

Tambah kolom `is_cancelled`, `is_failed` ke `fact_orders` supaya rekonsiliasi mudah:

```sql
ALTER TABLE dwh.fact_orders
  ADD COLUMN is_cancelled BOOLEAN DEFAULT FALSE,
  ADD COLUMN is_failed BOOLEAN DEFAULT FALSE;

-- Backfill (one-time job, owner: Data Engineering)
UPDATE dwh.fact_orders f
SET is_cancelled = (o.status = 'CANCELLED'),
    is_failed = (o.status = 'FAILED')
FROM prod_oltp.orders o
WHERE f.order_id = o.id;
```

Update ETL untuk load semua status (bukan filter):

```sql
-- Replace filter di ETL job
-- BEFORE: WHERE status = 'COMPLETED'
-- AFTER:  (tanpa filter, semua status di-load, flag is_cancelled/is_failed)
```

Monitoring rule (dbt test):

```yaml
# models/marts/fact_orders.yml
tests:
  - dbt_utils.equality:
      compare_model: ref('stg_oltp_orders')
      compare_columns:
        - order_id
      tolerance: 0.001  # 0.1% (post-fix expected gap)
```

**Referensi DAMA-DMBOK**

- KA-04 Data Quality dimension: **Completeness** (ETL filter menyebabkan completeness <100% relatif terhadap source) dan **Consistency** (cross-system reconciliation gap) — `references/dama_kafit.md` Section 2.
- KA-11 Metadata Management: ETL filter logic harus didokumentasikan di business glossary `fact_orders` dengan definisi formal "Orders dengan status COMPLETED only" — `references/dama_kafit.md` Section 3.

## Catatan Operasional

- **SQL snippet** boleh panjang jika kompleks, tapi jangan dipendekkan ke pseudocode — pembaca harus bisa langsung paste-and-run.
- **Threshold numerik** WAJIB eksplisit. Jangan "sedikit di atas threshold" — tulis angka.
- **Referensi DAMA** WAJIB di setiap gap finding, paling tidak satu KA. Ini supaya tim data tahu metodologi backing-nya, bukan opini personal.
- **Tone**: peer-to-peer engineer. Boleh asumsi pembaca sudah bisa baca DDL dan paham concept seperti ETL, FK, index. JANGAN definisi ulang istilah dasar.
