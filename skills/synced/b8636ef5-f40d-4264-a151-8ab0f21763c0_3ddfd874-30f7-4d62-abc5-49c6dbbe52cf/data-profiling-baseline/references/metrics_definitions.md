# Metrics Definitions & Reasoning Guide

Dokumen ini adalah rujukan lengkap setiap metrik dalam skill `data-profiling-baseline`.
Sumber: DAMA-DMBOK 2nd Ed. Ch.13 (sebagai taksonomi kondisi), Abedjan et al. (VLDB 2015), ISO 8000, Clauset et al. (SIAM 2009), ydata-profiling docs, Great Expectations catalog.

> **Catatan filosofi:** Skill ini fokus melaporkan **kondisi data apa adanya** (jumlah null, duplikat, anomali, inkonsistensi). DAMA-DMBOK dipakai sebagai *taksonomi referensi* untuk mengelompokkan jenis pengamatan, **bukan** sebagai framework scoring kualitas. Tidak ada perhitungan skor per dimensi (Completeness/Validity/Consistency %) dan tidak ada skor agregat (High/Medium/Low overall) di output.

## Daftar Isi

1. [Core Column Metrics](#1-core-column-metrics)
2. [Advanced Statistical Methods](#2-advanced-statistical-methods)
3. [Context-Specific Metrics](#3-context-specific-metrics)
4. [Inter-Column Metrics](#4-inter-column-metrics)
5. [Dataset-Level Condition Summary](#5-dataset-level-condition-summary)
6. [Conventions Output](#6-conventions-output)

---

## 1. Core Column Metrics

### Informasi Dasar
| Field | Definisi |
|---|---|
| `column_name` | Nama kolom apa adanya (dari header). |
| `description` | Penjelasan ringkas (1 kalimat): arti + unit (jika numerik) + domain bisnis. Hindari tautologi. |
| `data_category` | Klasifikasi peran kolom dalam ekosistem data — salah satu dari: **Master**, **Reference**, **Transaksional**, **Log**, atau **Lainnya**. Lihat panduan di sub-bagian berikut. |
| `data_type` | Dtype pandas yang terdeteksi. |
| `example_value` | Satu nilai non-null sebagai ilustrasi. |

### Kategori Data (LLM Reasoning) — `data_category`

Kolom `data_category` mengklasifikasikan **peran kolom** dalam ekosistem data. Klasifikasi ini membantu konsumen laporan memahami sifat dasar tiap kolom (apakah ia stabil/lambat berubah, apakah ia event, apakah ia metadata audit) tanpa harus terlebih dahulu paham domain. Klasifikasi diisi via LLM reasoning berdasarkan **nama kolom + sample value + konteks tabel**.

> Catatan posisi: skill ini fokus melaporkan **kondisi data**. Kategori ini disertakan sebagai *metadata deskriptif peran*, bukan sebagai skor kualitas. Ia menjawab "kolom ini perannya apa?", bukan "kolom ini bagus/buruk?".

#### Empat kategori + 1 fallback

| Kategori | Definisi singkat | Karakteristik utama |
|---|---|---|
| **Master** | Atribut deskriptif dari entitas bisnis inti yang relatif stabil (Customer, Product, Employee, Sekolah, Yayasan, SPPG, dll.) | Lambat berubah, deskriptif (bukan kuantitatif), sering jadi natural key atau atribut entitas |
| **Reference** | Nilai lookup / code list yang relatif statis dan dipakai berulang sebagai pengkategorian (provinsi, status, satuan, currency, kode pos, jenis kelamin, kelas, golongan) | Kardinalitas rendah, nilai berulang, sering FK ke tabel lookup, sifatnya enum |
| **Transaksional** | Kuantitas/event/measurement bisnis yang merepresentasikan transaksi atau aktivitas (amount, qty, harga, nilai, debit/kredit, jumlah_porsi, tanggal_transaksi, order_id) | Numerik measurement, high-volume saat banyak baris, atau FK ke master dalam konteks event |
| **Log** | Metadata sistem/audit/teknis (created_at, updated_at, modified_by, deleted_at, is_active, version, request_id, session_id, ip_address, log_level) | Tidak punya makna bisnis langsung, dipakai untuk audit/troubleshooting/tracking perubahan |
| **Lainnya** | Tidak jelas masuk salah satu di atas (free-text catatan, file blob, kolom eksperimental, kolom dengan sample value tidak informatif) | Fallback agar tidak memaksakan klasifikasi yang spekulatif |

#### Sinyal heuristik per kategori

**Master** — pakai kombinasi sinyal berikut:
- Nama kolom: `name`, `nama`, `nama_lengkap`, `alamat`, `address`, `email`, `phone`, `no_hp`, `gender`, `tanggal_lahir`, `dob`, `npwp`, `nik` (sebagai atribut, bukan FK), `gtin`, `sku`, atau atribut deskriptif entitas
- Kolom yang `is_unique = True` dan namanya mencerminkan natural key entitas: `customer_id`, `product_code`, `npsn`, `sppg_id`, `employee_id`, `yayasan_id` — itu adalah PK Master
- Sample value: deskriptif (nama orang, alamat, deskripsi produk), bukan kuantitas dan bukan timestamp
- Jika dataset secara keseluruhan adalah Master (mis. tabel `customers`), maka **mayoritas kolom** akan Master kecuali timestamp audit (Log) dan FK ke lookup (Reference)

**Reference** — pakai kombinasi sinyal berikut:
- Nama kolom: `kode_*`, `*_code`, `status`, `tipe`, `type`, `kategori`, `category`, `jenis`, `golongan`, `kelas`, `level`, `tier`, `currency`, `satuan`, `provinsi`, `kabupaten`, `kota`, `kecamatan`, `kelurahan`, `kode_pos`
- `cardinality_level = Low` (≤20 unik) DAN `is_category = True` adalah sinyal kuat
- Sample value berupa kode/label terbatas yang berulang: `"AKTIF"`, `"NON-AKTIF"`, `"JATIM"`, `"IDR"`, `"PENDING"`, `"L"`, `"P"`
- FK ke tabel lookup terpisah (nama kolom mengandung `_code`, `_kode`, `_id` tapi merujuk ke entitas lookup, bukan transaksi)

**Transaksional** — pakai kombinasi sinyal berikut:
- Nama kolom kuantitas: `amount`, `nilai`, `harga`, `price`, `total`, `subtotal`, `qty`, `quantity`, `jumlah`, `volume`, `weight`, `gram`, `kalori`, `protein`, `lemak`, `revenue`, `cost`, `debit`, `kredit`, `payment`, `nominal`
- Nama kolom event: `*_date`, `*_time`, `tanggal_*`, `waktu_*` dengan konteks transaksi (`tanggal_order`, `tanggal_bayar`, `transaction_date`, `delivery_date`, `tanggal_distribusi`)
- Nama kolom event identifier: `transaction_id`, `order_id`, `invoice_no`, `bast_id`, `kupon_id` di dalam tabel transaksi
- FK ke master di konteks event (`customer_id`, `product_id`, `sekolah_id` ketika berada di tabel transaksi/distribusi)
- Karakteristik high-volume + append-mostly secara keseluruhan tabel

**Log** — pakai kombinasi sinyal berikut:
- Nama kolom audit: `created_at`, `updated_at`, `deleted_at`, `modified_at`, `last_login`, `created_by`, `updated_by`, `modified_by`, `dt_created`, `dt_updated`
- Nama kolom teknis: `is_active`, `is_deleted`, `version`, `revision`, `etag`, `request_id`, `session_id`, `trace_id`, `ip_address`, `user_agent`, `log_level`, `event_type`, `event_name`
- Sifatnya bukan makna bisnis langsung — dipakai untuk troubleshooting, audit, tracking, soft-delete
- Catatan: `created_at` di tabel transaksi yang dipakai sebagai *waktu transaksi terjadi* lebih tepat **Transaksional**; tapi jika ia hanya menyimpan waktu insert ke DB (terpisah dari `transaction_date`), itu **Log**

**Lainnya** — pakai jika:
- Sample value tidak informatif (kolom internal/eksperimental, kolom kosong total, blob/file path tanpa konteks)
- Free-text catatan yang tidak jelas perannya (`catatan`, `keterangan` tanpa konteks bisnis spesifik) — boleh juga diklasifikasi Master jika jelas merupakan deskripsi entitas atau Transaksional jika jelas berisi keterangan transaksi
- Klasifikasi spekulatif: lebih baik isi `Lainnya` daripada salah label

#### Catatan reasoning

- **Konteks tabel penting.** Kolom `tanggal` di tabel `master_sekolah` (waktu data sekolah dimasukkan) cenderung Log; kolom `tanggal` di tabel `distribusi_mbg` (waktu makanan didistribusikan) cenderung Transaksional.
- **Boleh ambigu — ambil yang dominan.** Jika kolom punya dua peran, pilih yang paling menonjol secara semantik. Tulis alasan di `description` jika perlu.
- **Konsisten dengan dataset-level category.** Lihat field dataset-level `dataset_category` di Section 5 — kategori per kolom harus mendukung klasifikasi dataset secara keseluruhan.
- **JANGAN beri skor "kategori ini bagus/buruk".** Klasifikasi ini netral — deskripsi peran, bukan penilaian kualitas.

### Kelengkapan (Taksonomi DAMA: Completeness) — pelaporan kondisi, bukan score
| Field | Definisi |
|---|---|
| `total_record` | Jumlah baris dataset. |
| `total_filled_record` | Baris non-null pada kolom ini. |
| `pct_not_null` | `total_filled_record / total_record × 100`, 2 desimal. Angka deskriptif kondisi; **bukan** Completeness score. |

Token seperti `"NA"`, `"-"`, `"TBD"`, `""`, `"null"` dianggap null oleh script.

### Keunikan & Distribusi (Taksonomi DAMA: Uniqueness) — pelaporan kondisi
| Field | Definisi |
|---|---|
| `count_unique` | Jumlah nilai unik (drop null). |
| `is_unique` | True jika `count_unique == total_filled_record > 0`. Indikasi kunci natural. |
| `cardinality_level` | Label deskriptif level kardinalitas: Low (≤20 unik atau ratio <2%), Medium (ratio <50%), High (ratio ≥50%). **Catatan:** Ini adalah label deskriptif level kardinalitas — *bukan* skor kualitas Uniqueness. LLM boleh override berdasarkan konteks. |

### Deteksi Kategori (LLM Reasoning)
| Field | Cara Reasoning |
|---|---|
| `is_category` | True jika value bersifat diskrit (kode, label, status) DAN cardinality rendah relatif konteks. False untuk: ID unik, teks bebas, numerik kontinu, datetime. |
| `most_category` | Top value + persentase. Format: `"JATIM (32.1%)"`. Hanya jika `is_category=True`. |
| `least_category` | Bottom value + persentase (≥1 occurrence). Hanya jika `is_category=True`. |

Heuristik: numerik ≤10 unik + repeating → kategori (walau dtype int). String panjang + unique tinggi → bukan kategori. Boolean → kategori.

### Analisis String (Taksonomi DAMA: Validity/Conformity) — observasi format
Hanya diisi jika `data_type = string/object`.
| Field | Definisi |
|---|---|
| `max_length` | Panjang karakter maksimum (str-cast). |
| `min_length` | Panjang karakter minimum. |
| `avg_length` | Rata-rata panjang. |

Gunakan untuk: ID panjang fix (min≠max → suspect inkonsistensi format), teks bebas (varians besar), whitespace anomaly.

### Analisis Numerik (Taksonomi DAMA: Precision) — observasi sebaran
Hanya diisi jika `data_type = numeric (int/float)`.
| Field | Definisi |
|---|---|
| `min_value`, `max_value` | Min/max non-null. |
| `mean` | Rata-rata (round 4 desimal). |
| `median` / `p50` | Persentil 50. |
| `std_dev` | Standar deviasi sample (ddof=1). |
| `p25`, `p75` | Persentil 25 dan 75. |
| `numeric_subtype` | **Wajib diisi sebelum reasoning outlier/skew/distribution_shape.** Pilih satu dari: `continuous`, `boolean-flag`, `fk-categorical`, `enum-numeric`, `id-sequence`. Lihat aturan klasifikasi di sub-bagian *"Numeric Subtype Classification"* di bawah. |
| `outlier_eligible` | Boolean. `true` hanya bila `numeric_subtype = continuous`. Field ini menjadi guard supaya metode statistik dispersi (IQR, 3σ, skew, kurtosis, distribution_shape, bimodality) tidak diterapkan ke subtype kategorikal-yang-kebetulan-numerik. |

**Tip skewness sinyal:** gap besar antara mean dan median (>1 std_dev) = skewness atau outlier ekstrem — **valid hanya bila `outlier_eligible=true`** (subtype continuous). Pada boolean-flag/FK/enum, mean–median gap menggambarkan distribusi kelas, bukan skewness statistik.

### Numeric Subtype Classification

Kolom dengan tipe data numerik (int/float/smallint/bigint/numeric) tidak otomatis bisa diperlakukan sebagai variabel kontinu. Banyak kolom numerik di tabel transaksional/master sebenarnya menyimpan **kode kategoris** atau **identifier diskrit**. Klasifikasi subtype ini menentukan metode profiling mana yang relevan.

#### Aturan keputusan (urutan prioritas — pilih subtype pertama yang cocok)

| Subtype | Kriteria (semua harus terpenuhi kecuali ditandai OR) | Alasan IQR tidak relevan |
|---|---|---|
| **boolean-flag** | `distinct_count ≤ 2` DAN sample values ⊂ `{0, 1, true, false}` **ATAU** nama kolom diawali `is_` / `has_` / `can_` / `should_` / `allow_` | IQR=0 → semua nilai non-modus jadi "outlier". Yang dilaporkan: distribusi kelas (true/false ratio), minority share. |
| **id-sequence** | Kolom adalah PK **ATAU** nama kolom == `id` **ATAU** kolom adalah auto-increment sequence; DAN `cardinality_ratio ≥ 0.95` (hampir unik); DAN `max ≈ count_non_null` (range konsisten dengan running sequence) | Distribusi uniform 1..N → nilai akhir selalu di atas Q3+1.5×IQR. Yang dilaporkan: jumlah gap (`max - count`), apakah monotonik, duplikat ID. |
| **fk-categorical** | Nama kolom berakhiran `_id` (selain `id` saja); DAN `cardinality_ratio < 0.5`; DAN data type integer-like (smallint/integer/bigint) | Nilai FK adalah label kategoris, bukan magnitudo. ID besar bukan "lebih ekstrem" dari ID kecil — mereka cuma kode. Yang dilaporkan: kandidat orphan FK (LEFT JOIN ke parent), distribusi frekuensi referensi. |
| **enum-numeric** | `distinct_count ≤ 20` DAN `cardinality_ratio < 0.05` DAN nama kolom mengandung salah satu: `kode_`, `status_`, `tipe_`, `jenis_`, `kategori_`, `level_`, `tier_`, `golongan_`, `kelas_`, atau secara konteks ditandai Reference di `data_category` | Nilai enum adalah label berkode-angka, bukan magnitudo. Yang dilaporkan: distribusi frekuensi, nilai di luar set enum yang diharapkan. |
| **continuous** | Default — kolom numerik yang tidak cocok ke 4 subtype di atas | IQR/3σ/skew/distribution_shape VALID di sini. |

#### Penalaran tambahan (LLM judgment, bukan rule kaku)

- **Domain override**: Jika nama kolom secara semantik jelas kategoris (mis. `kode_pos` lima digit dengan distinct=37.000 — ini ID lokasi, bukan kontinu) atau jelas kontinu (mis. `umur_pegawai` smallint 18–60 dengan distinct=42 — ini diskrit numerik tapi semantiknya umur), gunakan **judgment** untuk override aturan mekanis. Sebut alasan override di `categorical_numeric_observation`.
- **Ordinal-numeric edge case**: Untuk kolom seperti `rating_1_5`, `skor_kepuasan_1_10`, `golongan_1_17` — secara statistik bisa dianggap ordinal numeric. IQR mungkin valid tapi interpretasinya berbeda dari kontinu. Boleh klasifikasi sebagai `enum-numeric` (lebih aman) dengan catatan ordinal di observation.
- **Sentinel values**: Banyak kolom numerik pakai sentinel seperti `-1` / `999` / `0` untuk "unknown". Sentinel BUKAN outlier statistik — laporkan terpisah sebagai placeholder/sentinel di `categorical_numeric_observation` walau subtype = `continuous`.

#### Field hasil yang wajib ditulis

Saat profiling kolom numerik:
1. **Selalu** tulis `numeric_subtype` (5 kemungkinan + `n_a` untuk non-numeric).
2. **Selalu** tulis `outlier_eligible` (true hanya untuk continuous).
3. Hanya bila `outlier_eligible=false`, isi `categorical_numeric_observation` dengan kondisi sesuai subtype.
4. Bila `outlier_eligible=true`, isi `outlier_detected` dengan hasil IQR/3σ.

Contoh CSV cell yang **valid**:

| column_name | numeric_subtype | outlier_eligible | outlier_detected | categorical_numeric_observation |
|---|---|---|---|---|
| `id` | id-sequence | false | Not applicable — id-sequence | Sequence 1..10,421 dengan 113 gap; tidak ada duplikat |
| `is_active` | boolean-flag | false | Not applicable — boolean-flag | 144/1061 baris is_active=0 (13.6%) — kelas minoritas |
| `department_id` | fk-categorical | false | Not applicable — fk-categorical | 4 baris dengan department_id=0 (kandidat orphan FK); 38 baris dengan dept_id 121-140 valid |
| `status_kepegawaian` | enum-numeric | false | Not applicable — enum-numeric | Kode 1=Aktif 89%, 2=Cuti 7%, 3=Resign 4%; ditemukan 12 baris kode 9 (luar enum) |
| `gaji_pokok` | continuous | true | Yes — 18 nilai >21.7M (p95), max 80M | (kosong, pakai outlier_detected) |
| `nama_lengkap` | n_a | false | n_a | n_a |

### Observasi Validitas & Konsistensi — pelaporan, bukan score
| Field | Cara Mengisi |
|---|---|
| `is_there_unvalid_value` | True/False + business rule yang dilanggar. Contoh: usia negatif, email tanpa @, kalori > berat bahan, koordinat out-of-range, tanggal masa depan untuk histori transaksi. **Pelaporan kondisi**, bukan skor Validity. |
| `is_consistent` | True/False. Inconsistency: campur date format, pemisah desimal mix, case mix, whitespace ekstra. **Pelaporan kondisi**, bukan skor Consistency. |
| `inconsistent_value_example` | 2-3 contoh konkret dari sample. Format: `"'DD/MM/YYYY' vs 'YYYY-MM-DD'"`. |

### Enrichment LLM
| Field | Cara Reasoning |
|---|---|
| `missing_value_pattern` | `random` = tersebar. `systematic` = mengelompok (semua row tahun 2023 null, atau hanya admin tertentu null). `none` = 100% terisi. Bila ragu: sebut hipotesis. |
| `outlier_detected` | **Hanya valid bila `outlier_eligible=true` (subtype `continuous`).** IQR: di luar [Q1-1.5×IQR, Q3+1.5×IQR]. 3σ untuk distribusi normal. Format: `"Yes — 4 nilai >p99 (contoh: 850, 920)"` atau `"No"`. Untuk subtype lain, isi `"Not applicable — <subtype>"` dan gunakan field `categorical_numeric_observation`. |
| `categorical_numeric_observation` | Wajib bila `outlier_eligible=false` dan kolom numerik. Sebut kondisi pengganti outlier yang relevan untuk subtype: minority share (boolean-flag), kandidat orphan FK (fk-categorical), distribusi enum + nilai luar set (enum-numeric), gap sequence + monotonisitas (id-sequence). Wajib menyebut angka. |
| `distribution_shape` | **Hanya valid bila `outlier_eligible=true`** untuk numerik. Numerik continuous: normal/right-skewed/left-skewed/bimodal/uniform/heavy-tail. Kategori: dominant/balanced/long-tail. Subtype numerik non-continuous: isi `n_a` (karena distribusi mereka mendeskripsikan kelas, bukan bentuk distribusi statistik). |
| `potential_data_leakage` | True jika kolom kemungkinan bocor info masa depan/target: `final_status`, `tanggal_bayar` saat memprediksi default. Tulis `False (no modeling context)` jika tidak ada konteks modeling. **Observasi kondisi**, bukan skor. |
| `suggested_data_type` | Tipe seharusnya: string `"2024-01-15"` → `datetime64`, `"Y/N"` → bool, `"Rp 1.000"` → int64 setelah strip. *(Catatan deskriptif tipe yang lebih tepat, bukan perintah cleaning.)* |
| `business_implication` | Narasi 1 kalimat tentang bagaimana kondisi kolom ini berpotensi mempengaruhi proses bisnis atau analisis lanjutan. Contoh: *"Null pada `tanggal_kirim` 12% akan menyebabkan baris terkait gugur saat join ke modul SLA pengiriman."* **JANGAN** mulai dengan kata kerja perintah (Trim/Imputasi/Drop). Itu sudah masuk ranah cleaning, bukan profiling. |

---

## 2. Advanced Statistical Methods

### Shannon Entropy
- **Formula:** `H(X) = -Σ p(x_i) * log2(p(x_i))`, range `[0, log2(N)]`
- **Normalized:** `H_norm = H / log2(N)` ∈ [0,1]
- **Interpretasi:** H_norm ≈ 0 → satu kategori dominan; ≈ 1 → distribusi uniform. *(Sifat deskriptif sebaran, bukan score.)*
- **Kapan:** Kategori dengan ≥500 rows.
- **CSV field:** `shannon_entropy` (normalized, 4 desimal)

### Bimodality Coefficient (BC)
- **Formula:** `BC = (g1² + 1) / (g2 + 3(n-1)²/((n-2)(n-3)))` dimana g1=skewness, g2=excess kurtosis.
- **Threshold:** BC > 0.555 → mengindikasikan bimodal atau heavy-tail (observasi bentuk distribusi).
- **Kapan:** Kolom numerik dengan ≥100 non-null values.
- **CSV field:** `bimodality_coefficient`

### Herfindahl-Hirschman Index (HHI)
- **Formula:** `HHI = Σ (share_i)²` dimana share_i = count_i / total. Range [1/N, 1].
- **Threshold praktis:** >0.25 concentrated; 0.15-0.25 moderate; <0.15 diverse. *(Label sebaran, bukan score kualitas.)*
- **DOJ convention (x10000):** <1500 unconcentrated, 1500-2500 moderate, >2500 highly concentrated.
- **Kapan:** Kolom kategori dengan `is_category=True`.
- **CSV field:** `hhi_concentration`

### Coefficient of Variation (CV)
- **Formula:** `CV = σ / |μ|` (dinyatakan dalam %).
- **Kapan:** Kolom numerik dengan μ ≠ 0. Berguna untuk membandingkan dispersi antar kolom dengan skala berbeda.
- **Skip:** Jika mean mendekati 0 (CV tidak bermakna).
- **CSV field:** `cv_pct`

### Normality Tests
| Test | Best for | H0 | Catatan |
|------|----------|----|---------|
| Shapiro-Wilk | n ≤ 5000 | Data ~ Normal | p<0.05 → reject normality |
| D'Agostino K² | n > 5000 | Skew=0, Kurt=3 | Robust untuk large samples |
- **Catatan:** n > 5000 sering reject normality untuk deviasi kecil → selalu komplemen dengan visualisasi Q-Q plot.
- **CSV field:** `normality_pvalue`

### Benford's Law (Financial Only)
- **Formula:** `P(d) = log10(1 + 1/d)` untuk digit pertama d ∈ {1..9}.
- **Expected:** 1→30.1%, 2→17.6%, 3→12.5%, 4→9.7%, 5→7.9%, 6→6.7%, 7→5.8%, 8→5.1%, 9→4.6%.
- **MAD Threshold (Nigrini):** <0.006 = close conformity, 0.006-0.012 = acceptable conformity, >0.015 = nonconformity (suspect anomaly). *(Label kesesuaian distribusi, bukan score kualitas.)*
- **SKIP:** Range <2 orde magnitudo, kolom kode/ID, sample <300, nilai dengan minimum buatan.
- **CSV fields:** `benford_mad`, `benford_status`

---

## 3. Context-Specific Metrics

### Time-Series
| CSV Field | Definisi |
|---|---|
| `temporal_frequency` | Inferred: hourly/daily/weekly/monthly/yearly/irregular |
| `gap_count` | Jumlah timestamp yang hilang dari sequence yang diharapkan |
| `is_stationary` | True (ADF p<0.05), False (ADF p≥0.05), null (tidak applicable) |
| `trend_direction` | up/down/flat/null |

**ADF Test:** H0 = ada unit root (non-stationary). Reject H0 (p<0.05) → stationary.
**KPSS Test:** H0 = stationary. Reject H0 (p<0.05) → non-stationary. Gunakan keduanya untuk konfirmasi.

### Geospatial
| CSV Field | Definisi |
|---|---|
| `coord_null_island_count` | Count (lat=0, lon=0) |
| `coord_invalid_count` | Count out-of-range coordinates |
| `coord_precision_std` | Std dev dari jumlah desimal |

### Financial
| CSV Field | Definisi |
|---|---|
| `benford_mad` | Mean Absolute Deviation dari Benford expected |
| `benford_status` | OK/acceptable/suspect/not_applicable |
| `round_number_pct` | % nilai yang habis dibagi 100 |
| `zero_count` | Count nilai nol |

### ID/Key
| CSV Field | Definisi |
|---|---|
| `id_format_pct_conforming` | % yang sesuai pola dominan |
| `sequence_gap_count` | Gap dalam integer sequence (null jika non-sequential) |

### Text/NLP
| CSV Field | Definisi |
|---|---|
| `avg_word_count` | Rata-rata jumlah kata per cell |
| `pii_detected` | Tipe PII ditemukan (pipe-separated: email|phone|nik) |
| `language_detected` | ind/eng/mix/other |
| `top_terms` | 5 term paling sering (pipe-separated) |

---

## 4. Inter-Column Metrics

### Correlation Matrix (bukan per-kolom, tapi dimasukkan ke Markdown)
- **Pearson r:** Numeric-Numeric, linear, range [-1,1]. Sensitif outlier.
- **Spearman ρ:** Numeric-Numeric/Ordinal, monotonic, robust ke outlier.
- **Cramér's V:** Categorical-Categorical, range [0,1]. Formula: `V = sqrt(χ² / (n * min(r-1, c-1)))`.
- **Point-biserial:** Binary-Numeric, linear.

**CSV field per kolom:** `max_correlation_with` (kolom yang paling kuat korelasinya), `max_correlation_value`.

### Functional Dependency Hints (LLM Reasoning, bukan komputasi)
Dari sample data, nalarkan: apakah ada kolom A yang memprediksi nilai kolom B? Contoh: `kode_pos` → `kota` (partial FD). Laporkan dalam Markdown sebagai hint untuk investigasi lebih lanjut.

---

## 5. Dataset-Level Condition Summary

Bagian ini menggantikan "DAMA Dimensions Scoring" dan "DQ Score" yang ada di versi sebelumnya. **Tidak ada perhitungan skor per dimensi dan tidak ada skor agregat.** Hanya pelaporan kondisi apa adanya.

### Field deskriptif yang wajib dihitung (level dataset):

| Field | Definisi |
|---|---|
| `total_rows` | Jumlah baris seluruh dataset. |
| `total_columns` | Jumlah kolom seluruh dataset. |
| `duplicate_rows` | Jumlah baris yang isinya persis sama dengan baris lain (full-row duplicate). |
| `total_empty_rows` | Jumlah baris yang **seluruh** kolomnya null/empty. |
| `overall_null_cell_pct` | Persentase total sel null dibanding total sel (rows × cols). Angka deskriptif. |
| `columns_with_null_count` | Berapa kolom punya ≥1 null. |
| `columns_with_inconsistency_count` | Berapa kolom yang `is_consistent = False`. |
| `columns_with_invalid_value_count` | Berapa kolom yang `is_there_unvalid_value = True`. |
| `columns_with_outlier_count` | Berapa kolom **continuous** (`outlier_eligible=true`) dengan `outlier_detected = "Yes — ..."`. **JANGAN** ikutkan kolom boolean-flag/FK/enum/ID di sini — mereka punya bucket sendiri di bawah. |
| `columns_with_orphan_fk_candidate_count` | Berapa kolom `fk-categorical` yang `categorical_numeric_observation` menyebut kandidat orphan FK (nilai 0/negatif/parent-not-found). |
| `columns_with_minority_class_imbalance_count` | Berapa kolom `boolean-flag` dengan distribusi sangat tidak seimbang (minority share <1% atau >99% — bukan masalah inheren, tapi layak diketahui). |
| `columns_with_enum_out_of_set_count` | Berapa kolom `enum-numeric` yang ditemukan nilai di luar set enum yang diharapkan. |
| `columns_with_sequence_gap_count` | Berapa kolom `id-sequence` yang punya gap (`max - count_non_null > 0`). |
| `numeric_subtype_counts` | Dict komposisi subtype numerik dataset: `{"continuous": N, "boolean-flag": N, "fk-categorical": N, "enum-numeric": N, "id-sequence": N}`. Membantu pimpinan/Tim Data cepat tahu rasio kolom yang benar-benar kontinu vs kategoris-yang-kebetulan-numerik. |
| `columns_with_pii_count` | Berapa kolom dengan PII terdeteksi (jika NLP/Text context aktif). |
| `column_category_counts` | Dict jumlah kolom per kategori: `{"Master": N, "Reference": N, "Transaksional": N, "Log": N, "Lainnya": N}`. |
| `dataset_category` | Klasifikasi dataset secara keseluruhan: salah satu dari `Master`, `Reference`, `Transaksional`, `Log`, atau `Mixed (kategori-dominan)`. Lihat panduan reasoning di bawah. |
| `dataset_category_rationale` | 1–2 kalimat menjelaskan kenapa dataset diklasifikasi demikian — sebut komposisi kolom + tanda-tanda khas (mis. *"Mayoritas kolom Transaksional (8 dari 12) — kolom `amount`, `qty`, `tanggal_distribusi`, dan FK `sekolah_id`/`menu_id` menunjukkan tabel ini menyimpan event distribusi MBG harian. 2 kolom Log audit (`created_at`, `updated_by`), 2 kolom Reference (`status_distribusi`, `kode_sppg`)."*). |

#### Panduan reasoning `dataset_category`

Gunakan komposisi `column_category_counts` + sifat baris untuk menentukan klasifikasi dataset:

- **Master** — mayoritas kolom Master, satu kolom adalah natural key unik dari entitas (PK), 1 baris = 1 entitas bisnis, baris relatif stabil. Contoh tabel: `customers`, `master_sekolah`, `master_yayasan`, `master_sppg`, `master_menu`, `master_bahan_makanan`.
- **Reference** — kardinalitas total rendah (jumlah baris ≤ beberapa ratus), kolom didominasi `code` + `label`/`description`, dipakai sebagai lookup. Contoh: `ref_provinsi`, `ref_status_distribusi`, `ref_satuan`, `ref_currency`.
- **Transaksional** — mayoritas kolom Transaksional + ada kolom event (timestamp + measurement + FK ke master), 1 baris = 1 event/transaksi, append-mostly. Contoh: `distribusi_mbg_harian`, `transaksi_pembayaran_yayasan`, `order_items`, `log_kupon_makan`.
- **Log** — mayoritas kolom Log/teknis, 1 baris = 1 entri audit/event sistem. Contoh: `audit_log_user`, `webhook_event_log`, `system_telemetry`. *(Perhatikan: tabel "log_X" yang isinya event bisnis tetap kemungkinan Transaksional, bukan Log — periksa apakah kolomnya bisnis atau teknis.)*
- **Mixed (kategori-dominan)** — jika tidak ada kategori yang dominan (mis. dataset wide-table hasil join lintas domain), pakai format `"Mixed (X-dominan)"` di mana X adalah kategori dengan kolom terbanyak. Contoh: `"Mixed (Master-dominan)"`.

> **Konsisten dengan klasifikasi kolom.** Jika `dataset_category = Transaksional` tetapi mayoritas kolom Master, ada inkonsistensi reasoning — periksa ulang.

### Field naratif yang harus diisi via reasoning:

| Field | Cara Mengisi |
|---|---|
| `condition_overview` | Narasi 2–4 kalimat menggambarkan kondisi keseluruhan dataset apa adanya. Sebut angka konkret. **Jangan tutup** dengan label kualitas atau skor. |
| `key_observations` | 3–5 kondisi paling menonjol secara faktual. Susun berdasarkan dampaknya ke proses bisnis (yang paling berdampak di atas). **Tanpa** label P0/P1/P2. Format: `"Kondisi: [fakta + angka]. Contoh: [baris/nilai konkret]."` |
| `business_implications` | **Disegmentasi per audiens** menjadi 3 sub-bagian. Lihat detail di bawah. **Tanpa** label score (Low/Medium/High) dan **tanpa** perintah cleaning. |
| `column_highlight_tier` (per kolom yang masuk Highlights) | Salah satu dari `🔴` (menghalangi proses bisnis inti / risiko keamanan-kepatuhan / fitur produk tidak bisa berjalan), `🟡` (perlu diketahui, partial coverage / inkonsistensi non-fatal), atau `🟢` (kondisi sehat yang layak disorot — jarang dipakai). **Ini indikator dampak ke proses bisnis, BUKAN skor kualitas data.** Tidak ada threshold % yang menentukan tier — pakai reasoning berdasar konteks bisnis. |

#### Struktur `business_implications` per audiens

`business_implications` HARUS terbagi menjadi 3 sub-bagian dengan bahasa berbeda sesuai audiens. Tujuannya supaya laporan bisa dipakai lintas peran tanpa harus terjemahan ulang:

| Sub-bagian | Audiens | Gaya Bahasa | Fokus |
|---|---|---|---|
| **Untuk Pimpinan / Pengambil Keputusan** | Direktur, Kepala Bidang, Manajer Senior | **Bahasa awam, no jargon.** Hindari "join", "schema", "primary key", "pipeline" tanpa terjemahan. | Apakah data ini bisa dipercaya untuk pelaporan eksternal/regulasi? Risiko reputasi/kepatuhan? Keputusan strategis apa yang berisiko salah? Value/cost yang berisiko hilang? |
| **Untuk Tim Product** | Product Manager, Product Designer, Product Owner | Semi-teknis OK. Sebut fitur dengan nama. | Fitur produk yang terdampak, UX yang berisiko salah, asumsi produk yang tidak terpenuhi, kemampuan tampilan/pencarian/filter yang berpotensi menyimpang. |
| **Untuk Tim Data / Engineering** | Data Engineer, Analytics Engineer, DBA, DevOps | **Boleh teknis penuh.** | Dampak ke pipeline (join, parsing, ingestion, model), dependency ke tabel lain, dampak ke warehouse/mart/dashboard, kebutuhan normalisasi/standardisasi schema. |

Setiap sub-bagian berisi 2–4 poin. Jika dataset terlalu sederhana untuk diisi semua audiens, cukup isi audiens yang relevan dan beri catatan singkat.

### Contoh `key_observations` yang BENAR:
- *"412 baris duplikat penuh ditemukan (3,3% dari total). Sample: baris 1240 dan 8451 identik di seluruh 18 kolom — berpotensi menggandakan agregasi laporan harian."*
- *"Kolom `tanggal_order` mencampur 2 format tanggal (DD/MM/YYYY dan YYYY-MM-DD) pada 1.823 baris — berpotensi salah parsing saat join temporal."*
- *"5 kolom punya >30% null dengan pola sistematis (null mengelompok pada periode Jan-Mar 2024) — periode tersebut akan kurang representatif jika diagregasi bulanan."*

### Contoh `key_observations` yang **SALAH** (mengandung scoring/perintah):
- ❌ *"[P0] Data quality LOW: deduplikasi sebelum analisis."* — mengandung label score (LOW) dan perintah (deduplikasi).
- ❌ *"Completeness score: 72% — di bawah threshold."* — mengandung scoring per dimensi.
- ❌ *"DQ Dimensi Validity gagal."* — mengandung penilaian.

### Contoh `business_implications` yang BENAR (audience-segmented):

**Untuk Pimpinan / Pengambil Keputusan:**
- *"Data ini belum bisa dipakai untuk pelaporan capaian gizi program MBG ke regulator — 15 zat gizi kunci belum direkam, sehingga klaim 'menu memenuhi standar gizi nasional' tidak punya dasar data yang bisa diaudit."*
- *"Risiko keamanan pangan: 68% bahan belum diberi label alergen padahal program melayani anak sekolah; perlu kebijakan apakah bahan tanpa label dianggap 'aman' atau 'perlu di-review dulu'."*

**Untuk Tim Product:**
- *"Fitur 'kalkulator gizi menu' tidak dapat menampilkan angka akurat untuk mikronutrien; pertimbangkan placeholder 'data belum tersedia' alih-alih angka 0 yang menyesatkan."*

**Untuk Tim Data / Engineering:**
- *"Duplikat 3,3% pada baris penuh akan menyebabkan total revenue overcount di laporan harian — agregasi SUM dampaknya 3,3% terlalu tinggi."*
- *"Inkonsistensi format tanggal di `tanggal_order` akan menyebabkan 1.823 baris (14,6%) gugur saat di-cast ke datetime dengan parser ketat."*

### Contoh `business_implications` yang **SALAH**:
- ❌ *"Lakukan deduplikasi via composite key (order_id, customer_id)."* — itu perintah cleaning.
- ❌ *"Overall data quality: Medium."* — itu skor agregat.
- ❌ *"NULL propagation akan menyebabkan referential integrity violation."* — terlalu teknis tanpa terjemahan; tidak bisa dipahami Pimpinan/Product.
- ❌ (Tanpa segmentasi audiens) *"3 implikasi tercampur untuk semua orang"* — laporan tidak bisa dipakai lintas peran.

---

## 5b. Index-Level Summary (Mode Multi-Tabel)

**Aktif HANYA jika ≥2 tabel diprofiling.** Output `index.md` adalah overview lintas seluruh data product (pengelompokan tabel yang diberikan oleh user). Tujuannya: memberi konsumen non-teknis satu entry point untuk memahami kondisi data lintas data product tanpa harus membaca laporan per-tabel.

### Field naratif yang harus diisi via reasoning:

| Field | Cara Mengisi |
|---|---|
| `executive_summary` | 3–5 kalimat **bahasa awam tanpa jargon**. Sebut data product mana yang siap pakai vs belum, dan konsekuensi terbesar untuk bisnis. Pimpinan harus bisa baca paragraf ini saja dan paham kondisi. **JANGAN** sebut istilah teknis seperti "join", "schema", "null cell", "outlier" tanpa terjemahan. |
| `scope_table` | Tabel: `Data Product | Tabel | Baris | Kolom | Klasifikasi | Kondisi Paling Menonjol`. Kolom "Kondisi Paling Menonjol" diisi 1 kalimat plain language. |
| `per_data_product[].business_context` | Untuk setiap data product: tujuan bisnis (1–2 kalimat), tabel yang dicakup, stakeholder utama, regulasi terkait. Sesuai info yang diberikan user di Step 1. |
| `per_data_product[].key_conditions` | 4–8 sorotan bahasa awam dengan ikon 🔴/🟡/🟢 yang **mengagregasi** highlight dari tabel-tabel di dalam data product. Bukan menyalin semua highlight per tabel — pilih yang paling berdampak lintas tabel. Sebut tabel asal di setiap sorotan (mis. "(dari `table_a`)"). |
| `per_data_product[].business_implications` | **Disegmentasi 3 audiens** (Pimpinan / Tim Product / Tim Data-Engineering) dengan aturan yang sama seperti level dataset. Ditulis di **level data product** (lintas tabel di dalamnya), bukan per-tabel. |
| `per_data_product[].next_discussion` | 2–4 pertanyaan/topik untuk diskusi stakeholder. |
| `cross_data_product_themes` | 3–6 kondisi yang muncul di **lebih dari satu data product**. Biasanya menandakan akar sistemik (mis. konvensi timezone tidak seragam, identifier tidak konsisten antar tabel, kolom enumerasi tanpa referensi terpusat). |
| `cross_data_product_implications` | Implikasi tema sistemik, **disegmentasi per audiens**. |

### Aturan kunci untuk `index.md`:

- **Executive Summary harus dapat dibaca utuh oleh non-teknis** — uji: jika direktur cuma baca paragraf pertama, apakah mereka paham kondisi keseluruhan dan dampaknya?
- **Setiap highlight & implikasi harus berbasis evidence dari laporan per-tabel** — jangan ada klaim tanpa angka pendukung. Boleh agregat angka lintas tabel (mis. "total 5 tabel master memiliki ≥1 kolom enumerasi dengan typo case-sensitivity").
- **Implikasi disegmentasi 3 audiens** di level data product dan di level lintas data product.
- **Tetap tanpa skor** — jangan tutup section dengan "Overall Data Product Quality: Medium". Cukup deskripsi kondisi.
- **File output naming**: `index.md`, `index.pdf` di root direktori output. Charts lintas-tabel (jika ada) di `_index_charts/`.

---

## 6. Conventions Output

**CSV:**
- Header sama dengan `assets/csv_template.csv`. Kolom advanced ditambah di akhir.
- Null → tulis `null` (4 huruf), bukan kosong atau "N/A".
- Numerik → tanpa thousand separator.
- String dengan koma → quote dengan `"..."`.
- **JANGAN tambah kolom** `data_quality_score`, `completeness_score`, `validity_score`, atau sejenisnya.

**Markdown:**
- Maks 2 tingkat heading di luar template.
- Jangan duplikasi tabel CSV di Markdown — pilih highlight.
- Setiap insight/kondisi WAJIB ada angka atau contoh nyata.
- Bahasa konsisten (Indonesia default, Inggris jika user minta).
- **JANGAN tutup section** dengan label kualitas (High/Medium/Low) atau skor agregat.

**Naming:**
- `<dataset-stem>_profile.csv`
- `<dataset-stem>_profile.md`
- `<dataset-stem>_profile.pdf`
- `<dataset-stem>_charts/` (folder PNG)
- Multi-sheet XLSX: `<stem>_<sheet>_profile.csv`
- **Mode multi-tabel (≥2 tabel):** tambah `index.md` dan `index.pdf` di root direktori output sebagai entry point lintas data product. Jika ada chart lintas-tabel, simpan di `_index_charts/`.

**Prinsip akhir:** Output harus bisa dibaca eksekutif non-teknis (PDF + Markdown) sekaligus cukup detail untuk data engineer (CSV). Output melaporkan kondisi apa adanya beserta implikasi bisnisnya — *tanpa* skor kualitas, *tanpa* prioritisasi risk, *tanpa* perintah cleaning. Keputusan apakah kondisi tertentu "baik" atau "buruk" diserahkan ke konsumen laporan yang punya konteks SLA.
