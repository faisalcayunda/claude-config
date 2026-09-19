# Reference: Postgres SQL Queries untuk Profiling

Kumpulan query siap pakai untuk dijalankan via Postgres MCP server. Gunakan placeholder `{schema}`, `{table}`, `{column}` lalu substitute saat eksekusi.

## 1. List Schemas

```sql
SELECT schema_name
FROM information_schema.schemata
WHERE schema_name NOT IN ('pg_catalog', 'information_schema', 'pg_toast')
  AND schema_name NOT LIKE 'pg_temp_%'
  AND schema_name NOT LIKE 'pg_toast_temp_%'
ORDER BY schema_name;
```

## 2. List Tables in Schema

```sql
SELECT
    table_name,
    table_type,
    pg_size_pretty(pg_total_relation_size(quote_ident(table_schema) || '.' || quote_ident(table_name))) AS size
FROM information_schema.tables
WHERE table_schema = '{schema}'
  AND table_type IN ('BASE TABLE', 'VIEW', 'MATERIALIZED VIEW')
ORDER BY table_name;
```

## 3. Row Count per Table (fast estimate)

```sql
-- Akurat (lambat untuk tabel besar)
SELECT COUNT(*) FROM {schema}.{table};

-- Estimasi cepat dari statistics
SELECT n_live_tup AS estimated_row_count
FROM pg_stat_user_tables
WHERE schemaname = '{schema}' AND relname = '{table}';
```

## 4. Column Schema (per table)

```sql
SELECT
    c.column_name,
    c.ordinal_position,
    c.data_type,
    c.udt_name,
    c.character_maximum_length,
    c.numeric_precision,
    c.numeric_scale,
    c.is_nullable,
    c.column_default,
    pgd.description AS column_comment
FROM information_schema.columns c
LEFT JOIN pg_catalog.pg_statio_all_tables st
    ON c.table_schema = st.schemaname AND c.table_name = st.relname
LEFT JOIN pg_catalog.pg_description pgd
    ON pgd.objoid = st.relid AND pgd.objsubid = c.ordinal_position
WHERE c.table_schema = '{schema}' AND c.table_name = '{table}'
ORDER BY c.ordinal_position;
```

## 5. Primary Key per Table

```sql
SELECT
    kcu.column_name,
    kcu.ordinal_position
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
WHERE tc.table_schema = '{schema}'
  AND tc.table_name = '{table}'
  AND tc.constraint_type = 'PRIMARY KEY'
ORDER BY kcu.ordinal_position;
```

## 6. Foreign Keys per Table

```sql
SELECT
    tc.constraint_name,
    kcu.column_name,
    ccu.table_schema AS foreign_table_schema,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name,
    rc.delete_rule,
    rc.update_rule
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
JOIN information_schema.constraint_column_usage ccu
    ON ccu.constraint_name = tc.constraint_name
JOIN information_schema.referential_constraints rc
    ON rc.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND tc.table_schema = '{schema}'
  AND tc.table_name = '{table}';
```

## 7. Indexes per Table

```sql
SELECT
    i.indexname,
    i.indexdef,
    idx.indisunique AS is_unique,
    idx.indisprimary AS is_primary
FROM pg_indexes i
JOIN pg_class c ON c.relname = i.indexname
JOIN pg_index idx ON idx.indexrelid = c.oid
WHERE i.schemaname = '{schema}' AND i.tablename = '{table}';
```

## 8. Check Constraints per Table

```sql
SELECT
    con.conname AS constraint_name,
    pg_get_constraintdef(con.oid) AS constraint_definition
FROM pg_constraint con
JOIN pg_class rel ON rel.oid = con.conrelid
JOIN pg_namespace ns ON ns.oid = rel.relnamespace
WHERE ns.nspname = '{schema}'
  AND rel.relname = '{table}'
  AND con.contype = 'c';
```

## 9. Profiling per Column (FULL TABLE SCAN)

User memilih full COUNT DISTINCT untuk akurasi. Jangan pakai TABLESAMPLE atau LIMIT.

### 9a. Generic per column

```sql
SELECT
    COUNT(*) AS total_rows,
    COUNT({column}) AS non_null_count,
    COUNT(*) - COUNT({column}) AS null_count,
    COUNT(DISTINCT {column}) AS distinct_count
FROM {schema}.{table};
```

### 9b. Numeric column extras

```sql
SELECT
    MIN({column}) AS min_val,
    MAX({column}) AS max_val,
    AVG({column}) AS avg_val,
    STDDEV({column}) AS stddev_val,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY {column}) AS median_val
FROM {schema}.{table}
WHERE {column} IS NOT NULL;
```

### 9c. String column extras

```sql
SELECT
    MIN(LENGTH({column})) AS min_len,
    MAX(LENGTH({column})) AS max_len,
    AVG(LENGTH({column}))::INT AS avg_len
FROM {schema}.{table}
WHERE {column} IS NOT NULL;
```

### 9d. Date/Timestamp column extras

```sql
SELECT
    MIN({column}) AS min_date,
    MAX({column}) AS max_date,
    EXTRACT(EPOCH FROM (MAX({column}) - MIN({column}))) / 86400 AS span_days
FROM {schema}.{table}
WHERE {column} IS NOT NULL;
```

## 10. Distinct Values & Frequencies (untuk kategorikal kandidat)

Hanya jalankan ini setelah `distinct_count <= 50`. Jika distinct > 50, kemungkinan bukan kategorikal.

```sql
SELECT
    {column} AS value,
    COUNT(*) AS frequency,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct
FROM {schema}.{table}
WHERE {column} IS NOT NULL
GROUP BY {column}
ORDER BY frequency DESC;
```

## 11. Format Detection (untuk non-kategorikal dengan pattern)

### Detect uniform length (semua baris sama panjang)

```sql
SELECT
    LENGTH({column}) AS len,
    COUNT(*) AS freq
FROM {schema}.{table}
WHERE {column} IS NOT NULL
GROUP BY LENGTH({column})
ORDER BY freq DESC
LIMIT 10;
```

### Detect numeric format (apakah semua digit)

```sql
SELECT
    COUNT(*) FILTER (WHERE {column} ~ '^[0-9]+$') AS all_digits,
    COUNT(*) FILTER (WHERE {column} ~ '^[A-Z0-9]+$') AS alphanumeric_upper,
    COUNT(*) FILTER (WHERE {column} ~ '^[a-zA-Z0-9]+$') AS alphanumeric,
    COUNT(*) AS total
FROM {schema}.{table}
WHERE {column} IS NOT NULL;
```

## 12. Sample Rows (untuk preview)

```sql
SELECT * FROM {schema}.{table} LIMIT 5;
```

## 13. FK Referential Integrity Check (apakah ada orphan)

```sql
-- Cek apakah ada {fk_column} yang tidak ada di parent table
SELECT COUNT(*) AS orphan_count
FROM {schema}.{table} t
LEFT JOIN {parent_schema}.{parent_table} p
    ON t.{fk_column} = p.{parent_column}
WHERE t.{fk_column} IS NOT NULL AND p.{parent_column} IS NULL;
```

---

## Best Practices Eksekusi

1. **Batch the queries**: jangan query satu-satu kalau bisa di-batch. Untuk profiling 10 kolom, buat 10 query lalu kirim sekali.

2. **Skip PK column profiling**: PK pasti unique dan not null, tidak perlu COUNT DISTINCT.

3. **Untuk SCD2 dimensi**: profiling per kolom dilakukan pada semua versi, tapi pertimbangkan juga `WHERE is_current = TRUE` untuk gambaran current state.

4. **Untuk tabel >100M baris**: full COUNT DISTINCT akan lama. Beritahu user dan minta konfirmasi. User sudah pilih full scan, jadi tetap jalankan tapi sertakan estimasi waktu.

5. **Save hasil ke JSON di /home/claude**: profiling result simpan ke file JSON, jangan hanya di context, agar bisa di-reference saat generate.

## Format Output Profiling

Setelah semua query selesai, kompilasi hasilnya ke format JSON seperti CSV profiler:

```json
{
  "source": "postgres",
  "database": "bgn_warehouse",
  "schema": "bgn_gold",
  "tables": {
    "fct_penyaluran_mbg": {
      "row_count": 5234567,
      "primary_key": ["penyaluran_id"],
      "foreign_keys": [
        {"column": "dim_sppg_id", "ref_table": "bgn_gold.dim_sppg", "ref_column": "sk_sppg"}
      ],
      "columns": {
        "status_penyaluran": {
          "data_type": "varchar(20)",
          "is_nullable": false,
          "distinct_count": 4,
          "distinct_values": ["terverifikasi", "dalam_perjalanan", "terdistribusi", "gagal"],
          "frequencies": [{"value": "terdistribusi", "freq": 4500000}, ...],
          "is_categorical_candidate": true,
          "is_pii": false
        },
        "nik": {
          "data_type": "varchar(16)",
          "is_nullable": true,
          "distinct_count": 4800000,
          "min_len": 16, "max_len": 16,
          "format_pattern": "^[0-9]{16}$",
          "is_categorical_candidate": false,
          "is_pii": true,
          "pii_category": "pii-identitas-khusus"
        }
      }
    }
  }
}
```
