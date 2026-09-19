---
name: data-profiling-baseline
description: >-
  Laporan profiling baseline pre-EDA dari dataset apapun (CSV/XLSX/Parquet/
  JSON/DB) domain apapun. MEMOTRET KONDISI DATA APA ADANYA — null, baris
  kosong, duplikat, anomali, inkonsistensi format — TANPA skor kualitas
  (no High/Medium/Low, no %Completeness, no DAMA scorecard). Highlight
  kolom ditulis bahasa awam (🔴/🟡/🟢 + paragraf plain language) dan
  implikasi proses bisnis disegmentasi per audiens (Pimpinan, Tim Product,
  Tim Data). Mode multi-tabel: jika user unggah lebih dari 1 tabel, skill
  minta pengelompokan data product lalu hasilkan `index.md` overview
  lintas data product. WAJIB dipanggil saat user upload dataset ATAU minta
  profiling, baseline data, kondisi data, pre-EDA, kenali dataset, audit
  kondisi, snapshot data, atau data dictionary. Trigger juga jika user
  upload file tabular tanpa instruksi. Output: CSV per-kolom 30+ metrik,
  Markdown per tabel, 3-10 PNG chart, PDF, dan `index.md` lintas data
  product. Advanced methods otomatis untuk time-series, teks, geospasial,
  finansial, ID, hierarki.
---

# Data Profiling Baseline

Skill ini membuat laporan data profiling **komprehensif, kontekstual, dan multi-output** sebagai baseline awal sebelum EDA. Output siap pakai untuk memahami kondisi existing dataset — apa adanya — sebelum tim memutuskan strategi cleaning, transformasi, atau eksplorasi lanjutan.

## Filosofi

Profiling yang baik bukan sekadar `describe()` pandas — dan juga bukan penilaian kualitas data. Skill ini fokus pada **deskripsi kondisi**:

- **Adaptif** terhadap tipe kolom (numerik, string, kategori, datetime, ID, teks bebas, koordinat).
- **Kontekstual** — gunakan domain knowledge untuk membaca apakah nilai wajar bagi konteks bisnis (sumber metodologis: DAMA-DMBOK Ch.13 sebagai *background* taksonomi kondisi, Abedjan et al. 2015 "Profiling Relational Data: A Survey", ISO 8000 sebagai referensi taksonomi).
- **Tiered** — Core methods wajib semua data; Advanced methods aktif otomatis sesuai konteks.
- **Reasoning-driven** — beberapa pengamatan butuh penalaran LLM, bukan threshold mekanis.
- **Multi-format** — output CSV (detail), Markdown (narasi kondisi), Grafik PNG (visual), PDF (eksekutif).
- **Deskriptif, bukan evaluatif** — laporkan apa yang teramati, beserta implikasinya terhadap proses bisnis. **JANGAN** beri skor kualitas data per dimensi (no % Completeness, % Validity, dll.), **JANGAN** beri skor agregat (no High/Medium/Low overall), dan **JANGAN** beri label P0/P1/P2 atau "suggested cleaning action" yang sifatnya prescriptive.
- **Dual-audience writing** — laporan ini akan dibaca tiga jenis konsumen sekaligus: (a) **Tim Data/Engineering** yang butuh detail teknis untuk perbaikan pipeline/schema, (b) **Tim Product** yang butuh tahu fitur produk apa yang terdampak, (c) **Pimpinan/Decision Maker** yang butuh tahu apakah data bisa dipercaya untuk pengambilan keputusan. Karena itu, highlight kolom dan implikasi proses bisnis WAJIB ditulis dalam bahasa yang bisa dipahami orang awam — sebutkan istilah teknis seperlunya, tapi selalu terjemahkan ke konsekuensi operasional konkret (mis. "kolom alergen kosong 68%" → "bahan tanpa label alergen berisiko tinggi untuk program makan anak sekolah").

**Kenapa tidak ada scoring?** Karena scoring (mis. "DQ Score: Medium" atau "Completeness: 78%") membutuhkan threshold yang bergantung pada konteks bisnis spesifik dan SLA yang berbeda-beda per organisasi. Skill ini fokus melaporkan *fakta kondisi* (jumlah null, jumlah duplikat, jumlah outlier, contoh inkonsistensi) — penilaian apakah kondisi tersebut "baik" atau "buruk" diserahkan ke konsumen laporan yang punya konteks bisnis. Boleh menyebut **implikasi terhadap proses bisnis** secara naratif (mis. "412 duplikat baris penuh bisa membiaskan agregasi laporan penjualan harian"), tapi tidak boleh menyimpulkannya jadi sebuah angka skor.

Selalu asumsikan data **belum bersih**. Tugas profiling adalah memotret kondisi apa adanya, bukan menyembunyikannya, dan bukan pula menghakiminya.

## Workflow

### 1. Identifikasi Konteks Bisnis, Domain, & Data Product

Sebelum profiling, tentukan domain dataset dari nama file, nama kolom, dan sample value:

- Gunakan domain knowledge yang relevan untuk membaca apakah nilai wajar/tidak wajar di konteks bisnis (untuk pelaporan kondisi, bukan untuk scoring).
- **Catatan:** Jika user membutuhkan konteks BGN/MBG khusus, panggil skill `badan-gizi-nasional` secara terpisah.
- Catat unit-of-analysis (apa yang direpresentasikan 1 baris), expected range, dan standar yang berlaku — semuanya sebagai konteks untuk membaca kondisi, bukan sebagai threshold scoring.

#### Multi-tabel: minta pengelompokan Data Product

**Trigger:** Jika user mengunggah/menunjuk **>1 tabel** (CSV/sheet/file terpisah), aktifkan mode multi-tabel. Sebelum profiling dimulai, minta info berikut dari user (jika belum disampaikan):

1. **Pengelompokan data product** — apakah semua tabel termasuk 1 data product yang sama, atau dibagi ke beberapa data product? Untuk setiap data product, sebutkan nama dan tabel-tabel yang termasuk di dalamnya.
2. **Tujuan/peran bisnis** per data product (1–2 kalimat) — apa yang data product ini dukung dalam proses bisnis? Output/keputusan apa yang dihasilkan?
3. **Stakeholder utama / konsumen** per data product — tim/peran yang menggunakan data ini (opsional tapi memperkaya laporan).
4. **Regulasi atau standar terkait** per data product (opsional).

Jika user **tidak ingin/tidak bisa** mengelompokkan ke data product, perlakukan tiap tabel sebagai data product tersendiri dengan nama default `<table-name>` — tetap hasilkan `index.md`.

Jika hanya **1 tabel** yang diunggah, lewati elicitation ini; hanya hasilkan output per-tabel standar (tanpa `index.md`).

### 2. Deteksi Tipe Data & Seleksi Metode

Baca `references/context_detection.md` untuk panduan deteksi otomatis. Seleksi metode dalam dua tier:

**TIER 1 — Core Methods (SELALU dijalankan, semua dataset):**
Completeness *(jumlah & % null per kolom — deskriptif, bukan skor)*, Uniqueness/Cardinality, Data Type Inference, **Numeric Subtype Classification** *(continuous/boolean-flag/fk-categorical/enum-numeric/id-sequence — lihat Section 4a; menentukan apakah IQR outlier berlaku)*, Basic Stats (numeric), String Length Stats, Top-N Values, Duplicate rows, Pattern/Format profiling, **Outlier (IQR/Z-score — hanya untuk subtype `continuous`)**, **Orphan-FK candidates / minority-class observations / sequence gap (subtype non-continuous)**, Distribution shape (skew/kurtosis — hanya untuk `continuous`), Missing pattern, Category detection, Validity/Consistency observations.

**TIER 2 — Advanced Methods (AKTIF otomatis jika terdeteksi):**
| Sinyal Deteksi | Metode Tambahan |
|---|---|
| Kolom datetime sortable (≥1) | Time-series: ADF/KPSS stationarity, ACF/PACF, seasonality, gap analysis, trend |
| Teks panjang avg_length > 50 | NLP: TTR, n-gram freq, language detection, PII regex scan |
| Kolom lat/lon atau koordinat | Geospatial: boundary check, null island (0,0), precision profiling |
| Dataset finansial (price/amount/transaksi) | Benford's Law, round number detection, velocity check |
| Kolom parent_id atau hierarki | Hierarchy: orphan detection, cycle check, depth analysis |
| Kolom kode/ID format fix | ID/Key: format validation, checksum hint, sequence gap analysis |
| Kolom numerik ≥5 | Correlation matrix (Pearson/Spearman/Cramér's V), Mutual Information hints |
| Dataset >500 baris numerik | Shannon Entropy, Bimodality Coefficient, HHI per kategori |

Baca `references/metrics_definitions.md` untuk formula dan panduan reasoning lengkap.

### 3. Jalankan Profiling Deterministik

```bash
python scripts/profile_dataset.py <path-to-dataset> --out <output-dir>
```

Script menghasilkan `_profile_raw.json` dan `_dataset_meta.json`. Opsi:
- `--sheet <name>` untuk XLSX multi-sheet
- `--no-na-tokens` untuk menonaktifkan null-token auto-detection

### 4. Tambahkan Reasoning LLM (WAJIB)

Untuk setiap kolom, baca `sample_non_null` dan `top_values` dari `_profile_raw.json` lalu reasoning:

| Field | Cara reasoning |
|---|---|
| `description` | Infer dari nama + sample + domain. 1 kalimat, sebut unit. |
| `data_category` | Klasifikasi peran kolom: **Master** (atribut entitas inti yang stabil), **Reference** (lookup/code list), **Transaksional** (kuantitas/event/FK di tabel event), **Log** (audit/metadata teknis), atau **Lainnya** (tak jelas). Pakai nama kolom + sample value + konteks tabel. Panduan sinyal lengkap di `references/metrics_definitions.md` sub-bagian "Kategori Data". |
| `is_category` | True jika diskrit + cardinality rendah. False untuk ID, teks bebas, numerik kontinu, datetime. |
| `most_category` / `least_category` | Hanya jika `is_category=True`. Format: `"Nilai (XX.X%)"`. |
| `is_there_unvalid_value` | Cek vs business rule konteks: usia negatif, email tanpa @, nilai fisik tidak mungkin. Laporkan sebagai **kondisi yang teramati**, bukan skor. |
| `is_consistent` | Cek format seragam: campur date format, pemisah desimal, case inconsistency. |
| `inconsistent_value_example` | 2-3 contoh nyata dari sample. |
| `missing_value_pattern` | `random` / `systematic` / `none`. Sistematik = null mengelompok pada subset. |
| `numeric_subtype` | **Wajib diisi untuk setiap kolom bertipe numerik** sebelum reasoning outlier. Pilih satu: `continuous` / `boolean-flag` / `fk-categorical` / `enum-numeric` / `id-sequence`. Aturan lengkap di sub-bagian *"4a. Numeric Subtype Reasoning (kontinu vs kategorikal)"* di bawah. Kolom non-numerik: isi `n_a`. |
| `outlier_detected` | **Hanya valid bila `numeric_subtype = continuous`.** Pakai IQR (di luar [Q1−1.5×IQR, Q3+1.5×IQR]) atau 3σ + business range. Tulis `Yes — [contoh + jumlah]` atau `No`. Untuk subtype lain, isi `Not applicable — [alasan]` (mis. `Not applicable — boolean-flag: "outlier" IQR di sini hanya kelas minoritas, bukan anomali`). **JANGAN** terapkan IQR ke `boolean-flag` / `fk-categorical` / `enum-numeric` / `id-sequence` — IQR menghasilkan false positive sistematis (IQR=0 pada boolean membuat semua nilai non-modus dianggap outlier; FK dengan ID kode besar dianggap outlier padahal hanya kode kategoris valid yang berbeda). Pengganti yang sesuai dilaporkan di `categorical_numeric_observation`. |
| `categorical_numeric_observation` | **Khusus bila `numeric_subtype` ∈ {`boolean-flag`, `fk-categorical`, `enum-numeric`, `id-sequence`}.** Pengganti outlier sesuai subtype: minority-class share (boolean-flag), kandidat orphan FK / nilai 0 / nilai negatif yang tidak ada di parent (fk-categorical), distribusi enum + nilai luar set yang diharapkan (enum-numeric), gap urutan + non-monotonik (id-sequence). Wajib sebut angka. Contoh format: `"144 baris (13.6%) dengan is_active=0 — kelas minoritas; perlu konfirmasi apakah semua non-aktif sah"`. |
| `distribution_shape` | **Hanya valid bila `numeric_subtype = continuous`.** Untuk subtype lain, isi `n_a`. Pilihan: normal / right-skewed / left-skewed / bimodal / uniform / heavy-tail. |
| `business_implication` | (Pengganti `suggested_cleaning_action`) — narasi 1–2 kalimat **bahasa awam** tentang bagaimana kondisi kolom ini berpotensi mempengaruhi proses bisnis atau analisis lanjutan. Pola yang baik: *"[Kolom seharusnya untuk X]. Karena [kondisi yang teramati], [konsekuensi operasional konkret yang bisa dipahami orang non-teknis]."* Contoh: *"Kolom ini menyimpan kode alergen bahan, namun 68% baris kosong — bahan tanpa label belum diketahui statusnya, berisiko untuk program makan anak sekolah yang punya potensi alergi."* **JANGAN** mulai dengan kata kerja perintah ("Trim...", "Imputasi...", "Drop...") — itu sudah masuk ranah cleaning, bukan profiling. **JANGAN** pakai jargon teknis berat tanpa terjemahan (mis. "akan menyebabkan NULL propagation pada left join" → cukup: "akan menyebabkan 32% baris hilang saat digabungkan dengan tabel menu"). |
| **Advanced fields** | Isi jika Tier 2 aktif: `entropy`, `hhi`, `benford_mad`, `normality_pval`, `is_stationary`, dll. |

**Reasoning wajib evidence** — jangan kasih label tanpa angka/sample pendukung. **Reasoning JANGAN scoring** — jangan beri label "Low quality", "Bad", "Acceptable", dsb.

### 4a. Numeric Subtype Reasoning (kontinu vs kategorikal)

Kolom bertipe numerik di tabel nyata jarang seragam — ada yang benar-benar **kontinu** (gaji, jam kerja, jumlah porsi), ada yang **diskrit-kategorikal** yang kebetulan dikodekan sebagai integer (flag `is_active=0/1`, FK `department_id=14`, enum `status_kode=3`, ID auto-increment `id=10421`). Sebelum menerapkan metode statistik seperti IQR/3σ untuk deteksi outlier, klasifikasikan dulu **numeric subtype** kolom — karena metode yang relevan berbeda untuk masing-masing subtype, dan menerapkan IQR ke subtype kategorikal akan menghasilkan **false positive sistematis** yang menyesatkan konsumen laporan.

**Pohon keputusan (urutan prioritas, top-down — pilih subtype pertama yang cocok):**

```
broad_type == numeric ?
├─ Ya → cek subtype:
│   1. boolean-flag    : distinct_count ≤ 2 DAN sample_non_null ⊆ {0, 1, true, false}
│                         ATAU nama kolom diawali `is_`, `has_`, `can_`, `should_`
│   2. id-sequence     : kolom adalah PK ATAU nama kolom == `id` / berakhiran `_id`
│                         DAN cardinality_ratio ≥ 0.95 (hampir unik)
│                         DAN min/max selaras dengan running sequence (max ≈ jumlah baris)
│   3. fk-categorical  : nama kolom berakhiran `_id` (selain `id` sendiri)
│                         DAN cardinality_ratio < 0.5 (banyak baris merujuk ID yang sama)
│                         DAN tipe data integer-like
│   4. enum-numeric    : distinct_count ≤ 20 DAN cardinality_ratio < 0.05
│                         DAN nama kolom mengandung salah satu dari: `kode_`, `status_`,
│                         `tipe_`, `kategori_`, `level_`, `tier_`, `golongan_`, atau cocok
│                         dengan signal Reference di metrics_definitions.md
│   5. continuous      : default — pertimbangkan IQR/3σ valid di sini
└─ Tidak → numeric_subtype = n_a
```

**Konsekuensi reasoning per subtype:**

| Subtype | Metode pengganti outlier | Field laporan |
|---|---|---|
| `continuous` | IQR `[Q1−1.5×IQR, Q3+1.5×IQR]` atau 3σ; sebut nilai konkret outlier dari `top_values`/`sample_non_null` | `outlier_detected = "Yes — N nilai di luar batas, contoh: ..."` atau `"No"` |
| `boolean-flag` | Laporkan **distribusi kelas + minority-class share**. **JANGAN** sebut minority sebagai outlier. | `outlier_detected = "Not applicable — boolean-flag"`, `categorical_numeric_observation = "144 baris (13.6%) dengan is_active=0 — kelas minoritas (pegawai non-aktif), bukan anomali statistik"` |
| `fk-categorical` | Laporkan **kandidat orphan FK**: nilai 0/negatif/NULL yang mencurigakan, distinct values yang sangat jarang muncul (1-2 baris), atau nilai di luar rentang ID parent table jika diketahui. Sarankan **LEFT JOIN ke parent** untuk validasi. | `outlier_detected = "Not applicable — fk-categorical"`, `categorical_numeric_observation = "4 baris dengan department_id=0 (kandidat orphan FK — tidak ada departments.id=0); 38 baris dengan department_id 121–140 valid sebagai department aktif"` |
| `enum-numeric` | Laporkan **distribusi kode + nilai di luar set enum yang diharapkan** (jika domain mengenal set valid). | `outlier_detected = "Not applicable — enum-numeric"`, `categorical_numeric_observation = "Kode 1=Aktif 89%, 2=Cuti 7%, 3=Resign 4%; ditemukan 12 baris dengan kode 9 yang tidak terdaftar di enum standar"` |
| `id-sequence` | Laporkan **gap urutan + non-monotonik** (mis. `id` mestinya kontinu 1..N). | `outlier_detected = "Not applicable — id-sequence"`, `categorical_numeric_observation = "Sequence min=1, max=10,421, expected ~10,421 baris tapi hanya 10,308 — 113 gap; tidak ada non-monotonik"` |

**Contoh BAIK (subtype reasoning yang benar):**

> Kolom `is_active` (smallint, distinct=2: nilai 0 dan 1) → `numeric_subtype = boolean-flag`. IQR menghasilkan Q1=Q3=1 sehingga IQR=0; semua nilai 0 (n=144) akan ditandai outlier — ini false positive metodologis. `outlier_detected = "Not applicable — boolean-flag"`. `categorical_numeric_observation = "144 baris (13.6%) dengan is_active=0 — kelas minoritas (pegawai non-aktif), bukan anomali. Perlu konfirmasi apakah seluruh 144 baris memang sah ditandai non-aktif atau ada yang harusnya aktif tapi belum di-update."`

> Kolom `department_id` (bigint, distinct=55, FK ke `departments`) → `numeric_subtype = fk-categorical`. IQR menghasilkan batas [−12.5, 55.5]; 42 baris di luar batas, tapi 38 di antaranya valid (department dengan ID 121–140 adalah sub-unit Pusdatin/Tauwas yang dibuat belakangan). 4 baris dengan `department_id=0` tidak punya parent di `departments` → ini orphan FK, masalah real. `outlier_detected = "Not applicable — fk-categorical"`. `categorical_numeric_observation = "4 baris (0.4%) dengan department_id=0 berpotensi orphan FK (tidak ada departments.id=0); 38 baris dengan department_id 121–140 valid sebagai sub-unit Pusdatin/Tauwas, bukan outlier."`

> Kolom `salary_base` (numeric, continuous, range 4M–80M IDR) → `numeric_subtype = continuous`. IQR `[Q1=5.2M, Q3=11.8M]` → batas atas 21.7M. 18 baris di atas batas atas (>21.7M), nilai 45M–80M konsisten dengan golongan tinggi. `outlier_detected = "Yes — 18 nilai >21.7M (p95), maksimum 80M IDR — kemungkinan pejabat eselon atas, bukan error input. Perlu konfirmasi rentang gaji wajar per golongan."`

**Contoh BURUK (yang harus dihindari):**

> ❌ `is_active` outlier_detected = "Yes — 144 di luar [1.0, 1.0]" *(IQR diterapkan ke boolean, false positive)*
> ❌ `department_id` outlier_detected = "Yes — 42 di luar [-12.5, 55.5]" *(IQR diterapkan ke FK, mencampur orphan FK (real) dengan ID kategoris valid (bukan masalah))*
> ❌ `id` outlier_detected = "Yes — 4 nilai di luar [10, 8500]" *(IQR diterapkan ke sequence; nilai akhir sequence selalu "di atas batas" karena distribusinya uniform 1..N)*

**Kenapa ini penting:** Konsumen laporan tidak akan tahu metode IQR salah-terapan kalau hanya membaca "Yes — 144 outlier". Mereka akan menganggap 144 pegawai itu **anomali yang perlu diinvestigasi**, padahal sebetulnya itu hanya pegawai non-aktif yang sah. Klasifikasi `numeric_subtype` di awal reasoning menyaring false positive metodologis dan mengarahkan investigasi ke kondisi yang relevan untuk subtype (mis. orphan FK, gap sequence, minority-class concentration).

### 4b. Format Penulisan Column Profiling Highlights (Bahasa Awam)

Section "Column Profiling Highlights" di Markdown per-tabel BUKAN sekadar dump field CSV. Pilih **5–10 kolom paling menonjol kondisinya** lalu tulis ulang dalam format **dual-audience** berikut. Tujuannya supaya orang non-teknis (Tim Product, Pimpinan) juga bisa memahami tanpa harus paham `cardinality_level` atau `IQR rule`.

**Skema setiap highlight:**

```
### {ICON} `{nama_kolom}` — {Headline 1 baris bahasa awam, tanpa jargon}

{Kalimat 1: Apa peran kolom ini seharusnya — plain language, 1 kalimat.}
{Kalimat 2–3: Apa kondisi yang sebenarnya teramati — sebutkan angka konkret (bold angka kunci) dan contoh nilai nyata.}
{Kalimat opsional: Observasi format/distribusi yang relevan, jika ada.}
{Kalimat penutup: "Hal ini berpengaruh karena..." / "Ini kritis karena..." — terjemahkan ke konsekuensi proses bisnis konkret yang bisa dipahami orang non-teknis. Sebut dampaknya ke operasi/fitur/keputusan, bukan ke "data quality".}
```

**Pemilihan ICON (tingkat dampak ke proses bisnis, BUKAN skor kualitas):**

| Ikon | Kapan dipakai | Catatan |
|---|---|---|
| 🔴 | Kondisi yang menghalangi proses bisnis inti / menimbulkan risiko keamanan-kepatuhan / membuat fitur produk tidak bisa berjalan. Contoh: kolom mandatori untuk regulasi 100% kosong, primary key duplikat, nilai fisik tidak mungkin pada metrik utama. | Pakai hemat — biasanya 2–4 highlight per tabel. |
| 🟡 | Kondisi yang notabene perlu diketahui — partial coverage, inkonsistensi format, placeholder value, ambiguitas null yang bukan kritis. Berpotensi mengganggu analisis tertentu tapi tidak fatal untuk operasi inti. | Biasanya 3–6 highlight per tabel. |
| 🟢 | Kondisi yang relatif standar / sudah konsisten tapi layak dicatat sebagai "baseline yang sehat". **Jarang dipakai** — kalau kolom OK biasanya tidak masuk highlights sama sekali; pakai 🟢 hanya jika ingin secara eksplisit memuji konsistensi yang relevan dengan bisnis (mis. "format kode konsisten 100%"). | 0–2 highlight per tabel. |

**Aturan penulisan:**

- Sebutkan **angka konkret** dengan bold (mis. `**347 baris (32,4%) tidak memiliki kode**`).
- Beri **contoh nilai nyata** dalam backtick (mis. `` `AP019` `` muncul 2 kali).
- Frasa kalimat penutup yang baik: *"Ini kritis karena…"*, *"Hal ini berpengaruh karena…"*, *"Akibatnya, [proses/fitur/keputusan bisnis] berisiko…"*.
- **JANGAN** pakai jargon teknis berat tanpa terjemahan: "NULL propagation", "schema drift", "primary key violation", "left outer join cardinality", "type coercion". Jika harus pakai istilah teknis, jelaskan singkat di dalam kurung.
- **JANGAN** beri perintah cleaning ("imputasi pakai median", "drop baris", "trim spasi") — itu ranah governance/cleaning, bukan profiling.
- **JANGAN** beri skor ("Low quality column", "Validity 72%") — laporkan kondisi apa adanya.

**Contoh BAIK (dari domain bahan makanan MBG):**

> ### 🔴 `kode_bahan` — Kode bahan tidak lengkap dan ada duplikat
>
> Kolom ini seharusnya menjadi identifikasi unik setiap bahan (format 5 karakter: huruf + 3 digit, contoh `AP004`). Namun **347 baris (32,4%) tidak memiliki kode** dan **23 kode terduplikat** ditemukan (contoh: `AP019`, `BR018` masing-masing muncul 2 kali). Panjang karakter konsisten 5 untuk yang terisi — artinya format sudah standar, hanya pengisian yang bermasalah. Ini kritis karena kode bahan digunakan sebagai referensi lintas sistem; tanpa kode unik, bahan yang sama bisa tercatat ganda di menu, atau sebaliknya, dua bahan beda dianggap sama.

**Contoh BURUK:**

> ❌ `kode_bahan` — **Completeness: 67.6%, Validity: Low.** Recommend imputation via lookup table. Pareto principle suggests 80/20 split. *(Mengandung skor, perintah cleaning, jargon tanpa konteks bisnis.)*

### 5. Susun Dataset-Level Condition Summary

Dari `_dataset_meta.json` + agregasi kolom:
- `total_rows`, `total_columns`, `duplicate_rows`, `total_empty_rows`, `overall_null_cell_pct` *(angka deskriptif, bukan skor)*
- `column_category_counts` — dict jumlah kolom per kategori `{"Master": N, "Reference": N, "Transaksional": N, "Log": N, "Lainnya": N}`.
- `dataset_category` — klasifikasi peran dataset secara keseluruhan: `Master` / `Reference` / `Transaksional` / `Log` / `Mixed (X-dominan)`. Lihat panduan di `references/metrics_definitions.md` Section 5.
- `dataset_category_rationale` — 1–2 kalimat menjelaskan kenapa dataset diklasifikasi demikian (sebut komposisi kolom + tanda khas).
- `condition_overview` — narasi 2–4 kalimat yang menggambarkan kondisi keseluruhan dataset apa adanya. Contoh: *"Dataset 12.450 baris × 18 kolom, diklasifikasikan sebagai **Transaksional** (mayoritas kolom kuantitas + FK ke master sekolah/menu). Ditemukan 412 baris duplikat penuh (3,3%) dan 27 baris yang seluruh kolomnya kosong. 5 kolom punya >30% null, dengan pola sistematis (null mengelompok pada periode Jan-Mar 2024). 3 kolom mencampur format tanggal (DD/MM/YYYY dan YYYY-MM-DD). 8 outlier ekstrem ditemukan pada kolom `nilai_transaksi` (>p99,5)."* **JANGAN** tutup dengan kalimat seperti "Overall data quality: Medium." atau "DQ Score: 75%".
- `key_observations` (3–5 kondisi paling menonjol secara faktual, tanpa prioritisasi P0/P1/P2 — disusun berdasarkan **dampak terhadap proses bisnis** dengan narasi singkat).
- `business_implications` — terbagi **per audiens** supaya bisa dibaca lintas peran. Struktur:
  - **Untuk Pimpinan / Pengambil Keputusan** (2–4 poin) — bahasa awam, sebut konsekuensi ke pelaporan/kepatuhan/keputusan strategis/risiko reputasi. Jangan pakai istilah teknis seperti "join", "schema", "primary key" tanpa terjemahan.
  - **Untuk Tim Product** (2–4 poin) — sebut fitur produk yang terdampak, kemampuan tampilan/pencarian/filter yang berisiko salah, pengalaman pengguna yang berpotensi menyimpang.
  - **Untuk Tim Data / Engineering** (2–4 poin) — di sini boleh teknis: dampak ke pipeline (join, parsing, ingestion, downstream model), dependency ke tabel lain, dampak ke warehouse/mart.

  Boleh menyebut "berisiko membiaskan…", "berpotensi gugur saat join ke…", "akan menyebabkan dashboard menampilkan angka tidak akurat…", tapi **tanpa** memberi skor ataupun perintah cleaning. Jika dataset terlalu sederhana untuk diisi semua audiens, cukup isi audiens yang relevan dan beri catatan singkat.

**TIDAK ADA** field `data_quality_score`, **TIDAK ADA** field score per dimensi DAMA (Completeness %, Validity %, dll.), **TIDAK ADA** label High/Medium/Low overall.

### 6. Generate Visualisasi (WAJIB, minimal 3 grafik)

```bash
python scripts/visualize_profile.py \
  --meta <output-dir>/_dataset_meta.json \
  --profile <output-dir>/_profile_raw.json \
  --out <output-dir>/charts/ \
  --dataset <path-to-original-dataset>
```

Script menghasilkan **3–10 file PNG** sesuai konten. **Tidak ada narasi teks di dalam gambar** — hanya title, label axis, dan legend. Lihat `scripts/visualize_profile.py` untuk daftar chart yang dihasilkan berdasarkan konten data.

Core charts (selalu):
1. Completeness bar chart per kolom *(menampilkan % non-null per kolom — angka deskriptif kondisi, bukan skor)*
2. Data type distribution pie chart
3. Missing pattern matrix (jika missing >5%)

Conditional charts (berdasarkan data):
4. Distribution histograms top-5 kolom numerik
5. Categorical frequency bar charts
6. Correlation heatmap (jika ≥3 numerik kolom)
7. Outlier boxplots — **hanya untuk kolom dengan `numeric_subtype = continuous`**. Boxplot pada boolean/FK/enum/ID tidak bermakna (Q1=Q3 atau quartile berkorespondensi dengan kategori, bukan dispersi).
8. Time series line (jika datetime ada)
9. Cardinality Pareto chart
10. **Dataset Condition Snapshot** — chart yang menampilkan **jumlah kolom yang terkena tiap kondisi** (kolom dengan null, kolom dengan inkonsistensi format, kolom continuous dengan outlier IQR, kolom fk-categorical dengan kandidat orphan FK, kolom boolean-flag dengan distribusi tidak seimbang ekstrem, kolom kategorikal, kolom bertipe datetime, dll.) sebagai bar chart deskriptif. **Pisahkan bucket "outlier IQR" hanya untuk subtype `continuous`** — jangan mencampur outlier IQR dengan orphan FK / minority-class flag di bucket yang sama, karena mereka berasal dari metode reasoning yang berbeda. **BUKAN** scorecard kualitas data — tidak ada sumbu "Score (%)" atau "Quality Dimension". Sumbu X = jenis kondisi/observasi, sumbu Y = jumlah kolom atau jumlah baris terdampak.
11. **Column Category Distribution** — bar chart distribusi kolom per kategori peran data: Master / Reference / Transaksional / Log / Lainnya. Sumbu X = kategori, sumbu Y = jumlah kolom. Membantu konsumen laporan cepat melihat komposisi tabel (mis. tabel transaksional dengan beberapa FK ke master vs tabel master murni).

### 7. Generate PDF Report

```bash
python scripts/generate_pdf.py \
  --markdown <output-dir>/<name>_profile.md \
  --charts-dir <output-dir>/charts/ \
  --out <output-dir>/<name>_profile.pdf
```

PDF = Cover page + Narasi kondisi lengkap + Charts disisipkan pada posisi relevan + Tabel ringkas kolom. **Cover PDF tidak menampilkan badge "Data Quality Score"** — boleh menampilkan ringkasan kondisi (jumlah baris, jumlah kolom, jumlah duplikat) sebagai info card.

### 7.5. Generate `index.md` Overview (HANYA mode multi-tabel)

**Trigger:** Lewati step ini jika hanya 1 tabel yang diprofiling. Jika ≥2 tabel diprofiling, langkah ini WAJIB dijalankan setelah seluruh laporan per-tabel selesai.

Gunakan template `assets/index_template.md` sebagai kerangka. File ini diletakkan di root direktori output sebagai `index.md` (juga PDF: `index.pdf` via `scripts/generate_pdf.py`). Isinya adalah overview lintas seluruh tabel & data product yang telah diprofiling — **bukan** salinan ringkas dari laporan per-tabel.

Struktur `index.md`:

1. **Ringkasan Eksekutif (untuk Pimpinan)** — 3–5 kalimat **bahasa awam tanpa jargon**. Sebut data product mana yang siap pakai, mana yang belum, dan apa konsekuensi terbesar untuk bisnis. Sebut angka konkret tapi terjemahkan ke konsekuensi operasional.
2. **Cakupan Profiling** — tabel `Data Product | Tabel | Baris | Kolom | Klasifikasi | Kondisi Paling Menonjol`.
3. **Sorotan per Data Product** — untuk setiap data product:
   - Konteks bisnis (tujuan, tabel, stakeholder, regulasi)
   - **Kondisi Utama yang Teramati** — list highlights bahasa awam dengan emoji 🔴/🟡/🟢 yang mengkombinasikan/menyatukan highlight dari tabel-tabel di dalamnya. Pilih 4–8 highlights paling penting per data product (bukan semua dari setiap tabel).
   - **Implikasi terhadap Proses Bisnis** — disegmentasi per audiens (Pimpinan, Tim Product, Tim Data/Engineering) seperti di Step 5, namun ditulis di level data product (lintas tabel di dalamnya), bukan per tabel.
   - **Diskusi Lanjutan yang Disarankan** — 2–4 poin
4. **Tema Lintas Data Product** — kondisi yang muncul di lebih dari satu data product. Biasanya menandakan akar masalah sistemik (mis. konvensi timezone audit yang tidak seragam, identifier yang tidak konsisten antar tabel, kolom enumerasi tanpa referensi terpusat). 3–6 poin.
5. **Lampiran — Laporan per Tabel** — tabel link ke `<tabel>_profile.md`, `<tabel>_profile.csv`, `<tabel>_profile.pdf`, `<tabel>_charts/`.

**Aturan kunci untuk `index.md`:**

- **Ringkasan Eksekutif harus dapat dibaca utuh oleh non-teknis** — jika seorang direktur cuma baca paragraf pertama, mereka harus tahu kondisi keseluruhan dan dampaknya.
- **Setiap highlight & implikasi harus berbasis evidence dari laporan per-tabel** — jangan ada klaim tanpa angka pendukung. Boleh agregat angka lintas tabel (mis. "total 5 tabel master memiliki ≥1 kolom enumerasi dengan typo case-sensitivity").
- **Implikasi disegmentasi 3 audiens** sama seperti per-tabel: Pimpinan → bahasa awam konsekuensi bisnis; Tim Product → fitur/UX terdampak; Tim Data/Engineering → boleh teknis.
- **Tetap tanpa skor** — jangan tutup section dengan "Overall Data Product Quality: Medium". Cukup deskripsi kondisi.

```bash
# Setelah semua laporan per-tabel selesai, generate PDF dari index.md
python scripts/generate_pdf.py \
  --markdown <output-dir>/index.md \
  --charts-dir <output-dir>/_index_charts/  # opsional jika ada chart lintas-tabel
  --out <output-dir>/index.pdf
```

### 8. Sajikan ke User

- **Mode 1 tabel**: Tampilkan lokasi 4 file: CSV, Markdown, folder charts, PDF. Tulis 1 paragraf **ringkasan kondisi**: kondisi yang teramati (jumlah null/duplikat/inkonsistensi/outlier paling menonjol) + 2–3 highlight bahasa awam dari section "Column Profiling Highlights" + 1 kalimat implikasi level bisnis. **JANGAN** tutup dengan skor atau label kualitas.
- **Mode multi-tabel**: Tampilkan lokasi `index.md` + `index.pdf` di paling atas (ini entry point utama), lalu daftar pendamping `<tabel>_profile.{md,csv,pdf}` + folder charts per tabel. Tulis 1 paragraf **ringkasan eksekutif lintas data product**: data product yang siap pakai vs yang belum + 2–3 highlight paling kritis bahasa awam.
- Jangan salin seluruh konten Markdown ke chat.

## Aturan & Prinsip

**Adaptif:** Dataset 3 kolom — jangan tulis "Top 10 Columns". Tanpa numerik — skip distribution.

**Beri contoh nyata.** "Ada inkonsistensi format tanggal" lemah. "Kolom `tanggal_order` mencampur `2024-03-15` dan `15/03/2024` (baris 120, 245)" kuat.

**Fokus deskriptif kondisi.** Setiap observasi harus berupa fakta terverifikasi dengan angka/contoh — bukan penilaian (Bad/Good) dan bukan perintah (Drop/Imputasi/Trim).

**Boleh sebut implikasi bisnis, jangan sebut score.** "412 duplikat baris penuh berpotensi membiaskan agregasi penjualan harian" → OK. "Data quality: Medium karena duplikat 3,3%" → TIDAK OK. "Suggested action: deduplikasi via composite key" → TIDAK OK (itu sudah ranah cleaning, bukan profiling).

**Prinsip DAMA-DMBOK (sebagai background metodologis, bukan output):** Profiling adalah langkah *Measure* dalam siklus DQM. Output dari skill ini adalah baseline pengamatan kondisi yang menjadi input untuk diskusi cleaning/governance — tapi keputusan kualitas dan tindakan diserahkan ke tim downstream yang punya konteks SLA.

## Detail Tambahan

- **Definisi metrik lengkap** → `references/metrics_definitions.md`
- **Context detection & method selection guide** → `references/context_detection.md`
- **Template output CSV** → `assets/csv_template.csv`
- **Template output Markdown per-tabel** → `assets/markdown_template.md`
- **Template output `index.md` lintas data product (multi-tabel)** → `assets/index_template.md`
- **Script profiling deterministik** → `scripts/profile_dataset.py`
- **Script visualisasi** → `scripts/visualize_profile.py`
- **Script PDF generation** → `scripts/generate_pdf.py`
