# Context Detection & Method Selection Guide

Panduan ini mendefinisikan sinyal deteksi otomatis untuk memilih Advanced Methods (Tier 2) yang tepat berdasarkan karakteristik dataset yang dibaca dari `_profile_raw.json` dan `_dataset_meta.json`.

---

## Deteksi Berurutan (jalankan top-to-bottom)

### 1. Time-Series Context
**Sinyal AKTIF jika:**
- Ada ≥1 kolom dengan `data_type = str` yang sample-nya berbentuk ISO 8601, epoch, atau format tanggal umum APAPUN
- ATAU `data_type = datetime64`
- ATAU nama kolom mengandung: `date`, `time`, `tanggal`, `waktu`, `timestamp`, `created`, `updated`, `period`, `bulan`, `tahun`, `dt`

**Metode yang dijalankan:**
- Deteksi frekuensi temporal (harian/mingguan/bulanan/tahunan) via delta antara sorted timestamps
- Gap analysis: bandingkan expected sequence vs actual
- Trend detection: Mann-Kendall test (jika ada numeric target column)
- ACF/PACF: hitung autocorrelation hingga lag 40 untuk kolom numerik utama
- Stationarity: ADF test (H0 = non-stationary; p<0.05 → stationary), KPSS test
- Seasonality hint: ACF peak pada lag periodik

**Output tambahan di CSV:**
- `temporal_frequency`: inferred (daily/weekly/monthly/etc.)
- `gap_count`: jumlah timestamp yang hilang
- `is_stationary`: True/False/null berdasarkan ADF p-value
- `trend_direction`: up/down/flat/null

---

### 2. Text/NLP Context
**Sinyal AKTIF jika:**
- Ada ≥1 kolom string dengan `avg_length > 50` dan `cardinality_level = High`
- ATAU nama kolom mengandung: `description`, `comment`, `notes`, `keterangan`, `catatan`, `text`, `content`, `narasi`, `alasan`, `reason`, `remarks`

**Metode yang dijalankan:**
- Token count distribution (word count per cell)
- Type-Token Ratio (TTR) = unique words / total words
- Top-20 unigram/bigram (setelah stopword removal)
- Language detection via heuristic (Latin vs CJK vs Arabic script)
- PII scan dengan regex: email, phone (Indonesian +62/08xx), NIK (16 digit), NPWP (15/16 digit), credit card (Luhn), IP address

**Output tambahan di CSV:**
- `avg_word_count`: rata-rata jumlah kata
- `pii_detected`: list tipe PII yang ditemukan (email/phone/nik/etc.)
- `language_detected`: ind/eng/mix/other
- `top_terms`: 5 term paling sering (pipe-separated)

---

### 3. Geospatial Context
**Sinyal AKTIF jika:**
- Ada kolom dengan nama: `lat`, `latitude`, `lon`, `longitude`, `lng`, `x`, `y`, `koordinat`, `geom`, `geometry`
- ATAU ada kolom dengan sample values dalam range [-90,90] dan [-180,180] secara bersamaan

**Metode yang dijalankan:**
- Boundary validity: lat ∈ [-90,90], lon ∈ [-180,180]
- Null island detection: (lat=0, lon=0) count
- Precision consistency: std of decimal places
- Geographic clustering hint: bbox (min_lat, max_lat, min_lon, max_lon)

**Output tambahan di CSV:**
- `coord_null_island_count`: count of (0,0) records
- `coord_invalid_count`: count of out-of-range
- `coord_precision_std`: std of decimal place count

---

### 4. Financial/Transactional Context
**Sinyal AKTIF jika:**
- Ada kolom numeric dengan nama mengandung: `price`, `amount`, `harga`, `nilai`, `total`, `payment`, `revenue`, `sales`, `cost`, `biaya`, `nominal`, `saldo`, `transaksi`, `invoice`
- ATAU ada kolom yang range-nya multi-orde magnitudo (max/min > 1000)

**Metode yang dijalankan:**
- **Benford's Law analysis**: hitung frekuensi digit pertama, bandingkan dengan expected P(d) = log10(1+1/d). Hitung MAD (Mean Absolute Deviation). Threshold: <0.006 OK, 0.006-0.012 acceptable, >0.015 suspect.
- **Round number detection**: % nilai yang habis dibagi 100, 1000, 10000
- **Negative value check**: count negatif — valid untuk debit/credit, flag untuk harga
- **Zero value check**: % nilai nol — bisa placeholder

**Output tambahan di CSV:**
- `benford_mad`: MAD dari Benford analysis (null jika tidak relevan)
- `benford_status`: OK/acceptable/suspect/null
- `round_number_pct`: % round numbers
- `zero_count`: count nilai nol

**Kapan SKIP Benford:** kolom dengan range <2 orde magnitudo, kolom kode/ID, kolom dengan nilai terbatas.

---

### 5. Hierarchical/Parent-Child Context
**Sinyal AKTIF jika:**
- Ada kolom `parent_id`, `parent_code`, `id_parent`, `id_induk`, atau pasangan `id` + `parent_id`
- ATAU ada kolom yang mengandung hierarki eksplisit (level, depth, tier, kelas, kategori + sub_kategori)

**Metode yang dijalankan:**
- Orphan detection: parent_id values yang tidak ada di id column
- Cycle detection: DFS untuk mendeteksi circular reference (A→B→A)
- Depth distribution: hitung kedalaman setiap node
- Coverage: % leaf nodes vs internal nodes

**Output tambahan di CSV:**
- `orphan_count`: jumlah orphan records
- `has_cycle`: True/False
- `max_depth`: kedalaman hierarki maksimum

---

### 6. ID/Key Column Context
**Sinyal AKTIF jika:**
- `is_unique = True` pada kolom string
- ATAU nama kolom mengandung: `id`, `kode`, `code`, `nik`, `npsn`, `nomor`, `no`, `uuid`, `guid`, `ean`, `barcode`, `isbn`
- ATAU `max_length == min_length` (fixed-length pattern)

**Metode yang dijalankan:**
- Format consistency: semua nilai harus pola sama
- Fixed-length validation: max_length == min_length
- Numeric-only check untuk kode yang seharusnya numerik
- Checksum hint:
  - 16-digit semua numerik → kandidat NIK (check prefix 1-9)
  - 13-digit → kandidat EAN/barcode
  - 8-digit → kandidat NPSN (semua digit, tidak mulai 0)
- Sequence gap: untuk ID integer auto-increment, cek range vs count

**Output tambahan di CSV:**
- `id_format_pct_conforming`: % yang conform ke pola dominan
- `sequence_gap_count`: jumlah gap dalam sequence (null jika non-sequential)

---

### 7. Multi-Column Relationship Context
**Sinyal AKTIF jika:**
- Dataset memiliki ≥3 kolom numerik
- ATAU ada pasangan kolom yang berhubungan logis (weight_gram + weight_kg; price + discount + final_price)

**Metode yang dijalankan:**
- **Pearson correlation** untuk kolom numerik-numerik
- **Cramér's V** untuk kolom kategori-kategori (hitung via chi-square)
- **Point-biserial** untuk boolean-numeric pairs
- **Inclusion Dependency hint**: cek apakah value set kolom A ⊆ value set kolom B
- Cross-column validation: sum check (e.g., subtotal + tax = total)

**Output tambahan di CSV:**
- `max_correlation_with`: kolom yang paling tinggi korelasinya (Pearson/Cramér's V)
- `max_correlation_value`: nilai korelasinya

---

### 8. Advanced Statistical Context
**Sinyal AKTIF jika:**
- Dataset memiliki ≥500 rows
- Ada ≥3 kolom numerik kontinu

**Metode yang dijalankan:**
- **Shannon Entropy**: H = -Σ p(x_i) * log2(p(x_i)) untuk kategori; normalized [0,1]. Low entropy = dominant/predictable.
- **Bimodality Coefficient (BC)**: BC = (g1²+1)/(g2+3*(n-1)²/((n-2)(n-3))). BC > 0.555 → bimodal.
- **HHI (Herfindahl-Hirschman Index)** untuk kategori: HHI = Σ (share_i)². Range [1/N, 1]. >0.25 concentrated.
- **Coefficient of Variation (CV)**: CV = σ/|μ|. Perbandingan variabilitas relatif.
- **Normality p-value**: Shapiro-Wilk (n≤5000) atau D'Agostino K² (n>5000). p<0.05 → reject normality.

**Output tambahan di CSV:**
- `shannon_entropy`: null jika non-categorical atau <500 rows
- `bimodality_coefficient`: null jika bukan numerik
- `hhi_concentration`: null jika bukan kategori
- `cv_pct`: CV dalam persen
- `normality_pvalue`: p-value normality test (null jika non-numeric)

---

## Decision Tree Summary

```
Dataset loaded
├─ Untuk SETIAP kolom numerik: klasifikasi numeric_subtype  ← Tier 1, WAJIB
│   ├─ continuous       → IQR/3σ/skew/distribution_shape valid
│   ├─ boolean-flag     → laporkan minority share, skip IQR
│   ├─ fk-categorical   → laporkan kandidat orphan FK, skip IQR
│   ├─ enum-numeric     → laporkan distribusi kode + out-of-set, skip IQR
│   └─ id-sequence      → laporkan gap + monotonisitas, skip IQR
├─ Ada kolom datetime? → AKTIFKAN Time-Series methods
├─ Ada kolom text panjang (avg>50)? → AKTIFKAN NLP/Text methods
├─ Ada kolom lat/lon? → AKTIFKAN Geospatial methods
├─ Ada kolom finansial (price/amount)? → AKTIFKAN Financial/Benford methods
├─ Ada parent_id / hierarki? → AKTIFKAN Hierarchy methods
├─ Ada kolom ID fixed-length? → AKTIFKAN ID/Key methods
├─ ≥3 kolom numerik (yang subtype=continuous)? → AKTIFKAN Correlation methods
└─ ≥500 rows dan ≥3 numerik (subtype=continuous)? → AKTIFKAN Advanced Statistical methods
```

Multiple contexts bisa AKTIF bersamaan. Setiap context menambah kolom di CSV output dan chart di visualisasi.

**Catatan tentang numeric_subtype:** Klasifikasi ini wajib dilakukan **sebelum** menerapkan metode statistik dispersi (IQR/3σ/skewness/correlation/Benford). Metode dispersi dirancang untuk variabel kontinu, sehingga menerapkannya ke kolom kategoris yang kebetulan bertipe integer (FK ID, boolean flag, enum kode) menghasilkan **false positive sistematis** yang menyesatkan konsumen laporan. Aturan klasifikasi lengkap ada di `references/metrics_definitions.md` sub-bagian *"Numeric Subtype Classification"*.

### Sinyal cepat per subtype

| Sinyal | Subtype yang disarankan |
|---|---|
| Nama kolom diawali `is_`/`has_`/`can_`/`should_` ATAU distinct=2 dengan nilai {0,1} | `boolean-flag` |
| Kolom adalah PK ATAU nama `id` dengan cardinality_ratio ≥ 0.95 | `id-sequence` |
| Nama berakhiran `_id` (selain `id` saja), tipe integer, cardinality_ratio < 0.5 | `fk-categorical` |
| Distinct ≤ 20, cardinality_ratio < 0.05, nama mengandung `kode_/status_/tipe_/level_/golongan_` | `enum-numeric` |
| Sisanya | `continuous` |
