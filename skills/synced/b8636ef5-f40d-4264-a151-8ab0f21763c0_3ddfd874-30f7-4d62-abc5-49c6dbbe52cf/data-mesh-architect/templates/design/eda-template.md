---
title: "Preliminary EDA Template — <Nama Data Product>"
sidebar_label: "EDA Template"
sidebar_position: 10
description: "Template analisis eksplorasi data awal untuk memahami distribusi, anomali, dan karakteristik sumber data sebelum pipeline production"
tags: [design, eda, exploratory-analysis, data-quality]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: design
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Preliminary EDA Template

> **Tujuan dokumen ini:** Template terstruktur untuk melaksanakan Exploratory Data Analysis (EDA) pada sumber data sebelum pipeline production dibangun. Hasil EDA menjadi input untuk Quality Design, Source-to-Target Mapping, dan Infrastructure sizing.

:::note EDA vs Data Profiling
**Data Profiling** (fase Bootstrap) → penilaian cepat: "Apakah data layak?"
**EDA** (fase Design) → analisis mendalam: "Bagaimana karakteristik data ini?"
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` |

---

## Setup & Konfigurasi

```python
# ==============================================================
# EDA Setup — <Nama Data Product>
# Jalankan di: Jupyter Notebook / Google Colab / VS Code
# Environment: Development (JANGAN gunakan production credentials)
# ==============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Konfigurasi display
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', '{:.2f}'.format)
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# [!]  PERINGATAN PRIVASI: Jangan print atau log data PII dalam notebook ini
# Gunakan sample data yang sudah di-anonymize untuk kolom PII

# Koneksi ke sumber (melalui read-only service account)
# Gunakan connection string dari Vault/SSM — JANGAN hardcode
import os
DB_CONN = os.environ.get('EDA_DB_CONN_STRING')  # Set dari environment

print(f"EDA dimulai: {datetime.now()}")
print(f"Sumber: <nama sumber>")
print(f"Tujuan: Preliminary analysis untuk <nama data product>")
```

---

## 1. Ringkasan Dataset

### 1.1 Overview

```python
# Load sample data (gunakan LIMIT untuk dataset besar)
# CATATAN: Kolom PII harus di-mask sebelum diload ke notebook EDA
query = """
    SELECT 
        -- Kolom non-PII:
        id,
        kode_referensi,
        status,
        tanggal_lahir,
        jumlah,
        -- Kolom PII harus di-mask atau diganti dengan hash:
        MD5(nik::text) as nik_hash,  -- Gunakan hash, bukan nilai asli
        -- created_at untuk analisis temporal
        created_at,
        updated_at
    FROM <schema>.<tabel_sumber>
    WHERE created_at >= CURRENT_DATE - INTERVAL '90 days'
    LIMIT 100000
    -- Untuk dataset kecil, hapus LIMIT
"""

df = pd.read_sql(query, DB_CONN)
print(f"Shape: {df.shape}")
print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
```

**Hasil Overview:**

| Metrik | Nilai |
|---|---|
| **Total Records (sample)** | `<X records>` |
| **Total Kolom** | `<X kolom>` |
| **Rentang Waktu Data** | `<YYYY-MM-DD s.d. YYYY-MM-DD>` |
| **Memory Usage (sample)** | `<X MB>` |
| **Missing Values (total)** | `<X% dari total cells>` |
| **Duplicate Rows** | `<X rows (X%)>` |

### 1.2 Data Types

```python
print(df.dtypes)
print("\nNull counts:")
print(df.isnull().sum())
print(f"\nDuplicate rows: {df.duplicated().sum()}")
```

**Temuan Data Types:**

| Kolom | Tipe Aktual | Tipe Ekspektasi | Perlu Konversi? |
|---|---|---|---|
| `<id>` | `<object>` | `<UUID>` | `<Ya — cast to UUID>` |
| `<tanggal_lahir>` | `<object>` | `<date>` | `<Ya — parse date>` |
| `<jumlah>` | `<float64>` | `<int64>` | `<Ya — int conversion>` |

---

## 2. Analisis Completeness

```python
# Hitung % missing per kolom
missing_pct = (df.isnull().sum() / len(df) * 100).sort_values(ascending=False)
print(missing_pct[missing_pct > 0])

# Visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
missing_pct[missing_pct > 0].plot(kind='bar', ax=ax, color='coral')
ax.set_title('Persentase Missing Values per Kolom')
ax.set_ylabel('% Missing')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('eda_missing_values.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Temuan Completeness:**

| Kolom | % Missing | Acceptable? | Rekomendasi |
|---|---|---|---|
| `<kolom_a>` | `<0.3%>` | `<Ya (SLO: <1%)>` | `<Monitor, tambahkan DQ rule>` |
| `<kolom_b>` | `<15%>` | `<Tidak>` | `<Investigasi sumber; buat rule: impute atau reject>` |
| `<kolom_c>` | `<0%>` | `<Ya>` | `<Pertahankan NOT NULL constraint>` |

---

## 3. Analisis Distribusi Kolom Kunci

### 3.1 Kolom Kategorikal

```python
# Distribusi kolom status / kategorikal
categorical_cols = ['<status>', '<kategori>', '<wilayah>']

for col in categorical_cols:
    if col in df.columns:
        print(f"\n=== {col} ===")
        vc = df[col].value_counts(dropna=False)
        print(vc)
        print(f"Unique values: {df[col].nunique()}")
        
        # Plot
        fig, ax = plt.subplots(figsize=(8, 4))
        vc.head(20).plot(kind='bar', ax=ax)
        ax.set_title(f'Distribusi: {col}')
        plt.tight_layout()
        plt.savefig(f'eda_dist_{col}.png', dpi=150)
        plt.show()
```

**Temuan Distribusi Kategorikal:**

| Kolom | Nilai Unik | Nilai Dominan | Anomali |
|---|---|---|---|
| `<status>` | `<3>` | `<'aktif' (85%)>` | `<Tidak ada>` |
| `<kategori>` | `<15>` | `<'tipe_a' (60%)>` | `<'UNKNOWN' (2%) — perlu cleanup>` |

### 3.2 Kolom Numerik

```python
# Statistik deskriptif kolom numerik
numeric_cols = ['<jumlah>', '<nilai>', '<usia>']
print(df[numeric_cols].describe())

# Deteksi outlier dengan IQR
for col in numeric_cols:
    if col in df.columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
        print(f"{col}: {len(outliers)} outliers ({len(outliers)/len(df)*100:.1f}%)")
```

**Temuan Kolom Numerik:**

| Kolom | Min | Max | Mean | Median | Std Dev | % Outlier | Catatan |
|---|---|---|---|---|---|---|---|
| `<jumlah>` | `<0>` | `<500>` | `<45.2>` | `<40>` | `<22.1>` | `<1.2%>` | `<Distribusi right-skewed>` |
| `<nilai>` | `<-100>` | `<50.000.000>` | `<X>` | `<X>` | `<X>` | `<2.5%>` | `<[!] Nilai negatif mencurigakan>` |

### 3.3 Kolom Temporal

```python
# Analisis distribusi waktu
date_cols = ['<created_at>', '<tanggal_transaksi>']

for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col])
        print(f"\n{col}:")
        print(f"  Min: {df[col].min()}")
        print(f"  Max: {df[col].max()}")
        print(f"  Missing: {df[col].isnull().sum()}")
        
        # Time series volume
        monthly = df.groupby(df[col].dt.to_period('M')).size()
        monthly.plot(kind='line', marker='o', figsize=(12, 4), title=f'Volume per Bulan: {col}')
        plt.tight_layout()
        plt.savefig(f'eda_timeseries_{col}.png', dpi=150)
        plt.show()
```

**Temuan Temporal:**

| Kolom | Rentang | Volume Trend | Anomali |
|---|---|---|---|
| `<created_at>` | `<2023-01 s.d. 2025-04>` | `<+5% per bulan>` | `<Gap di 2024-03 (maintenance?)>` |
| `<tanggal_transaksi>` | `<2023-06 s.d. 2025-04>` | `<Stabil>` | `<Spike Desember setiap tahun>` |

---

## 4. Analisis Uniqueness & Duplikasi

```python
# Cek duplikasi
print(f"Duplikat baris: {df.duplicated().sum()}")
print(f"Duplikat primary key: {df.duplicated(subset=['<id>']).sum()}")
print(f"Duplikat business key: {df.duplicated(subset=['<kode_referensi>']).sum()}")

# Contoh duplikat (tanpa PII)
dupes = df[df.duplicated(subset=['<kode_referensi>'], keep=False)]
print(f"\nContoh duplikat (kolom non-PII):")
print(dupes[['<id>', '<kode_referensi>', '<status>', '<created_at>']].head(10))
```

**Temuan Uniqueness:**

| Key | Duplikat Count | % Duplikat | Penyebab | Strategi Dedup |
|---|---|---|---|---|
| `<id>` | `<0>` | `<0%>` | `<N/A>` | `<N/A>` |
| `<kode_referensi>` | `<1.234>` | `<0.5%>` | `<Multiple insert dari retry>` | `<Keep latest by created_at>` |

---

## 5. Analisis Korelasi & Hubungan Antar Kolom

```python
# Korelasi kolom numerik
numeric_df = df[numeric_cols].dropna()
corr_matrix = numeric_df.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
ax.set_title('Correlation Matrix')
plt.tight_layout()
plt.savefig('eda_correlation.png', dpi=150)
plt.show()
```

---

## 6. Temuan & Rekomendasi EDA

`[Mandatory — rangkum temuan kritis untuk tim]`

### 6.1 Ringkasan Temuan

| Kategori | Temuan | Severity | Dampak pada Pipeline |
|---|---|---|---|
| `<Completeness>` | `<15% null pada kolom_b>` | `Tinggi High` | `<Perlu imputation strategy atau reject rule>` |
| `<Validity>` | `<Nilai negatif pada kolom_nilai>` | `Tinggi High` | `<Tambahkan constraint >= 0 atau investigate sumber>` |
| `<Uniqueness>` | `<0.5% duplikat kode_referensi>` | `Sedang Medium` | `<Tambahkan dedup logic di Silver layer>` |
| `<Temporal>` | `<Gap data Maret 2024>` | `Sedang Medium` | `<Konfirmasi dengan tim sumber; pertimbangkan backfill>` |
| `<Volume>` | `<Growth +5%/bulan — sesuai estimasi>` | `Baik Informasi` | `<Infra sizing masih relevan>` |

### 6.2 Input untuk Quality Design

Berdasarkan EDA, aturan kualitas berikut **wajib** ditambahkan ke `../design/quality-design.md`:
- `<Rule 1: expect_column_values_to_be_between jumlah min=0>` — karena ditemukan nilai negatif
- `<Rule 2: expect_column_values_to_not_be_null untuk kolom_a>` — karena null > SLO target
- `<Rule 3: Dedup check pada kode_referensi>` — karena 0.5% duplikat

### 6.3 Input untuk Source-to-Target Mapping

Transformasi yang perlu ditambahkan ke mapping:
- `<kolom_b: impute NULL dengan 'UNKNOWN' + flag kolom is_kolom_b_imputed>` 
- `<kolom_nilai: filter rows WHERE kolom_nilai >= 0>` — reject atau quarantine nilai negatif
- `<kode_referensi: dedup dengan ROW_NUMBER() PARTITION BY kode_referensi ORDER BY created_at DESC>` 

### 6.4 Catatan untuk Infra Brief

- `<Volume aktual sesuai estimasi — tidak perlu revisi sizing>`
- `<Perlu partisi tabel berdasarkan created_at mengingat growth trend>`

---

## Lampiran: Environment Setup

```bash
# requirements untuk notebook EDA
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
sqlalchemy>=2.0
psycopg2-binary>=2.9
jupyter>=1.0
pandas-profiling>=3.6  # Opsional: automated profiling report
ydata-profiling>=4.0   # Pengganti pandas-profiling
```
