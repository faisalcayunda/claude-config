# Reference: Data Source Workflow

Skill ini mendukung **3 jenis sumber input** untuk men-generate dokumen. Selalu identifikasi sumber dulu, lalu jalankan workflow yang sesuai.

## Decision Tree: Pilih Sumber

```
User minta generate doc → tanya: "Apa sumber datanya?"
  │
  ├─ "Database PostgreSQL"        → Workflow A: Postgres MCP
  ├─ "File CSV"                   → Workflow B: CSV Profiling
  ├─ "Schema saja (CREATE TABLE)" → Workflow C: Manual Schema
  └─ "Belum tahu"                 → Tawarkan ketiga opsi
```

**Catatan penting**: Workflow A dan B punya keuntungan besar — distinct value bisa dihitung dari data aktual untuk auto-detect kategorikal. Workflow C harus mengandalkan user input untuk daftar enum.

---

## Workflow A: Postgres MCP

### A.1 Discover MCP Connector

Sebelum apapun, panggil `tool_search` untuk cek apakah Postgres MCP tersedia:

```
tool_search(query="postgres database query")
```

Jika tidak ada hasil, panggil `search_mcp_registry`:

```
search_mcp_registry(keywords=["postgres", "database", "sql"])
```

Jika tetap tidak ada, suggest user untuk connect via menu Settings → MCP → Postgres. Jangan generate fake SQL output — minta user setup MCP dulu.

### A.2 Identifikasi Scope Database

Tanyakan ke user:

1. **Database mana yang mau didokumentasikan?** (nama database / connection alias)
2. **Schema mana?** (default `public`, tapi banyak data product punya schema khusus seperti `bgn_gold`)
3. **Semua tabel di schema, atau spesifik tabel saja?** (tampilkan daftar tabel kalau perlu, biar user pilih)

### A.3 Eksplorasi Schema

Untuk setiap tabel terpilih, jalankan query schema:

```sql
-- Informasi kolom
SELECT
    column_name,
    data_type,
    character_maximum_length,
    numeric_precision,
    numeric_scale,
    is_nullable,
    column_default,
    ordinal_position
FROM information_schema.columns
WHERE table_schema = '{schema}' AND table_name = '{table}'
ORDER BY ordinal_position;

-- Primary key
SELECT a.attname
FROM pg_index i
JOIN pg_attribute a ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
WHERE i.indrelid = '{schema}.{table}'::regclass AND i.indisprimary;

-- Foreign keys
SELECT
    tc.constraint_name,
    kcu.column_name,
    ccu.table_schema AS foreign_table_schema,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND tc.table_schema = '{schema}' AND tc.table_name = '{table}';

-- Row count
SELECT COUNT(*) FROM {schema}.{table};
```

### A.4 Profiling per Kolom (FULL TABLE SCAN — bukan sample)

User memilih full table COUNT DISTINCT untuk akurasi. Untuk setiap kolom non-PK, jalankan:

```sql
-- Distinct count + null count + min/max/avg untuk numeric/date
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT {column}) AS distinct_count,
    COUNT(*) - COUNT({column}) AS null_count,
    MIN({column}) AS min_val,
    MAX({column}) AS max_val
FROM {schema}.{table};

-- Untuk string: min/max panjang
SELECT
    MIN(LENGTH({column})) AS min_len,
    MAX(LENGTH({column})) AS max_len,
    AVG(LENGTH({column}))::INT AS avg_len
FROM {schema}.{table}
WHERE {column} IS NOT NULL;
```

**Threshold kategorikal**: kolom dianggap kandidat enum jika `distinct_count ≤ 50` DAN bukan numeric continuous (lihat reference `categorical-detection.md`).

Jika kandidat kategorikal, ambil semua distinct values:

```sql
SELECT {column}, COUNT(*) AS freq
FROM {schema}.{table}
WHERE {column} IS NOT NULL
GROUP BY {column}
ORDER BY freq DESC;
```

### A.5 Tampilkan ke User untuk Konfirmasi

Setelah profiling selesai, **JANGAN langsung generate**. Tampilkan summary:

```
Saya sudah profile database `{db_name}`, schema `{schema}`.

Tabel ditemukan:
- bgn_gold.fct_penyaluran_mbg (5.2M baris)
- bgn_gold.dim_sppg (35.270 baris)
- bgn_gold.dim_wilayah (84.000 baris)

Field kategorikal kandidat (akan masuk Vocabulary sebagai enum):
- fct_penyaluran_mbg.status_penyaluran: 4 distinct → terverifikasi, dalam_perjalanan, terdistribusi, gagal
- dim_sppg.tipe_sppg: 3 distinct → reguler, mitra, mandiri

Field PII terdeteksi (perlu klasifikasi Restricted/Confidential):
- dim_sppg.nama_kepala_sppg → Restricted (pii-umum)
- dim_sppg.alamat → Restricted (pii-umum)
- dim_warga.nik (kalau ada) → Confidential (pii-identitas-khusus)

Apakah inferensi ini benar? Ada yang perlu disesuaikan?
```

Tunggu konfirmasi user sebelum melanjutkan ke generate.

---

## Workflow B: CSV File

### B.1 Identifikasi File

Tanyakan ke user:
1. **Lokasi file CSV** (biasanya di `/mnt/user-data/uploads/`)
2. **Apakah satu file = satu tabel?** (sering ya)
3. **Apakah ada multiple file dengan relasi?** (kalau ya, kumpulkan semua)

Jalankan `view /mnt/user-data/uploads` untuk lihat file yang available.

### B.2 Profile CSV dengan Pandas Chunksize

Untuk hemat memory, **WAJIB pakai pandas chunksize**. Jangan `pd.read_csv(file)` polos untuk file besar.

Buat script Python di `/home/claude/profile_csv.py`:

```python
import pandas as pd
import json
from pathlib import Path

CHUNK_SIZE = 50_000

def profile_csv(csv_path: str, max_distinct: int = 50):
    """
    Profile CSV file with chunked reading.
    Returns: dict per column with distinct count, nulls, samples, type.
    """
    # First pass: get column names and dtypes via small sample
    df_sample = pd.read_csv(csv_path, nrows=1000)
    columns = df_sample.columns.tolist()

    # Initialize accumulators
    stats = {col: {
        'distinct_values': set(),
        'null_count': 0,
        'total_count': 0,
        'min_val': None,
        'max_val': None,
        'min_len': None,
        'max_len': None,
        'dtype': str(df_sample[col].dtype),
        'sample_values': [],
    } for col in columns}

    # Full scan with chunks
    for chunk in pd.read_csv(csv_path, chunksize=CHUNK_SIZE, low_memory=False):
        for col in columns:
            series = chunk[col]
            stats[col]['total_count'] += len(series)
            stats[col]['null_count'] += series.isna().sum()

            non_null = series.dropna()
            if len(non_null) == 0:
                continue

            # Distinct collection (cap at max_distinct + 1 to detect overflow)
            if len(stats[col]['distinct_values']) <= max_distinct:
                stats[col]['distinct_values'].update(non_null.astype(str).unique())

            # Min/max for numeric
            if pd.api.types.is_numeric_dtype(non_null):
                cmin, cmax = non_null.min(), non_null.max()
                stats[col]['min_val'] = cmin if stats[col]['min_val'] is None else min(stats[col]['min_val'], cmin)
                stats[col]['max_val'] = cmax if stats[col]['max_val'] is None else max(stats[col]['max_val'], cmax)
            else:
                # String length stats
                lengths = non_null.astype(str).str.len()
                lmin, lmax = lengths.min(), lengths.max()
                stats[col]['min_len'] = lmin if stats[col]['min_len'] is None else min(stats[col]['min_len'], lmin)
                stats[col]['max_len'] = lmax if stats[col]['max_len'] is None else max(stats[col]['max_len'], lmax)

    # Finalize
    for col in columns:
        s = stats[col]
        s['distinct_count'] = len(s['distinct_values'])
        s['is_categorical_candidate'] = (
            s['distinct_count'] <= max_distinct
            and s['distinct_count'] >= 2
            and not (s['dtype'].startswith('float'))  # float biasanya bukan kategorikal
        )
        # Convert set to sorted list for output
        s['distinct_values'] = sorted(list(s['distinct_values'])) if s['is_categorical_candidate'] else None
        s['sample_values'] = list(s['distinct_values'])[:10] if s['distinct_values'] else []

    return stats

if __name__ == '__main__':
    import sys
    out = profile_csv(sys.argv[1], max_distinct=int(sys.argv[2]) if len(sys.argv) > 2 else 50)
    print(json.dumps(out, indent=2, default=str))
```

Jalankan: `python /home/claude/profile_csv.py /mnt/user-data/uploads/file.csv > /home/claude/profile.json`

### B.3 LLM Reasoning Pass

Setelah profiling, hasil di-load ke context. Untuk setiap kolom, terapkan LLM reasoning (lihat `categorical-detection.md`) untuk konfirmasi mana yang kategorikal. **Tidak semua field dengan distinct ≤ 50 adalah enum** — contoh:
- Field `umur` 0-50 → BUKAN enum (continuous), set range validation
- Field `tanggal_lahir` distinct = 5000 → bukan kandidat tapi tetap perlu format DATE validation

### B.4 Konfirmasi ke User

Sama dengan Workflow A.5: tampilkan ringkasan, minta konfirmasi sebelum generate.

---

## Workflow C: Manual Schema

User kasih schema dalam bentuk `CREATE TABLE`, ERD, atau spreadsheet kolom. Tidak ada data aktual untuk profiling.

### C.1 Parse Schema

Identifikasi dari input user:
- Nama tabel + schema
- Daftar kolom: nama, tipe data, nullable, default, PK/FK

### C.2 Interview Daftar Enum

Karena tidak ada distinct value, **wajib tanya user** untuk:
1. Field mana yang enum?
2. Daftar nilai valid untuk masing-masing
3. Field mana yang PII?

### C.3 Infer Validasi dari Pola Nama

Gunakan pola nama field untuk infer validasi (lihat `validation-rules.md`):
- `nik` → format regex `^[0-9]{16}$`
- `kode_wilayah` → format regex `^[0-9]{10}$`
- `email` → format regex email
- `tanggal_*` → range tidak di masa depan
- `jumlah_*` / `nominal_*` → range ≥ 0

---

## Multi-Tabel = Multi-Document? TIDAK

**Aturan penting**: 1 database = 1 dokumen Vocabulary + 1 dokumen Data Dictionary.

- Data Dictionary punya **section 2.x per tabel** (2.1, 2.2, 2.3, dst)
- Vocabulary punya **entri per atribut** (field yang sama di beberapa tabel disebut sekali tapi dengan referensi ke semua tabel)

Contoh struktur Data Dictionary untuk 3 tabel:

```
## 1. Inventori Tabel dan Objek
| Tabel | ... |
| bgn_gold.fct_penyaluran_mbg | ... |
| bgn_gold.dim_sppg | ... |
| bgn_gold.dim_wilayah | ... |

## 2. Data Dictionary per Objek
### 2.1 bgn_gold.fct_penyaluran_mbg
[full field table]
### 2.2 bgn_gold.dim_sppg (SCD Type 2)
[full field table]
### 2.3 bgn_gold.dim_wilayah
[full field table]
```

Vocabulary akan punya entry seperti `status_penyaluran` (digunakan di fct_penyaluran_mbg) DAN field umum seperti `kode_wilayah` (digunakan di fct_penyaluran_mbg DAN dim_wilayah) — di kolom "Digunakan di tabel" cantumkan semua.
