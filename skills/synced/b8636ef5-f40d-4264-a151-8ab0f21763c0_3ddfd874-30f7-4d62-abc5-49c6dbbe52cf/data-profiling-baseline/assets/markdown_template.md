# Data Profiling Report — {{DATASET_NAME}}

> **Tanggal profiling:** {{DATE}}
> **Source file:** `{{SOURCE_FILE}}`
> **Profiler:** data-profiling-baseline
> **Sifat laporan:** Deskriptif kondisi data (apa adanya). **Tidak mengandung skor kualitas data per dimensi maupun skor agregat.**

---

## 1. Business Context

> Hapus seluruh section ini jika benar-benar tidak ada konteks bisnis yang diketahui.

- **Domain:** {{Domain — e.g., fintech, healthcare, logistics, government, nutrition, HR, e-commerce}}
- **Unit-of-analysis:** {{Apa yang direpresentasikan oleh 1 baris?}}
- **Sumber & frekuensi:** {{Asal data dan kapan di-refresh}}
- **Regulasi/standar terkait:** {{Standar yang berlaku}}
- **Stakeholder utama:** {{Tim/peran yang menggunakan data ini}}
- **Advanced context detected:** {{Time-series / Financial / Geospatial / Text / Hierarchy / ID — pilih yang aktif}}

---

## 2. Dataset Condition Snapshot

| Metrik Kondisi | Nilai |
|---|---|
| Total baris | **{{TOTAL_ROWS}}** |
| Total kolom | **{{TOTAL_COLUMNS}}** |
| Klasifikasi dataset | **{{DATASET_CATEGORY}}** *(Master / Reference / Transaksional / Log / Mixed)* |
| Komposisi kolom per kategori | Master: **{{N_MASTER}}** · Reference: **{{N_REFERENCE}}** · Transaksional: **{{N_TRANSAKSIONAL}}** · Log: **{{N_LOG}}** · Lainnya: **{{N_LAINNYA}}** |
| Baris duplikat (full-row) | **{{DUPLICATE_ROWS}}** |
| Baris kosong total (semua kolom null) | **{{TOTAL_EMPTY_ROWS}}** |
| Persentase sel null keseluruhan | **{{OVERALL_NULL_CELL_PCT}}%** |
| Kolom dengan ≥1 null | **{{COLUMNS_WITH_NULL_COUNT}}** |
| Kolom dengan inkonsistensi format | **{{COLUMNS_WITH_INCONSISTENCY_COUNT}}** |
| Kolom dengan nilai invalid (vs business rule) | **{{COLUMNS_WITH_INVALID_VALUE_COUNT}}** |
| Kolom dengan outlier terdeteksi | **{{COLUMNS_WITH_OUTLIER_COUNT}}** |
| Kolom dengan PII terdeteksi *(jika NLP aktif)* | **{{COLUMNS_WITH_PII_COUNT}}** |

**Rationale klasifikasi dataset:** {{DATASET_CATEGORY_RATIONALE — 1–2 kalimat menjelaskan kenapa dataset diklasifikasi demikian. Contoh: "Mayoritas kolom Transaksional (8 dari 12) — kolom `amount`, `qty`, `tanggal_distribusi`, dan FK `sekolah_id`/`menu_id` menunjukkan tabel ini menyimpan event distribusi MBG harian. 2 kolom Log audit (`created_at`, `updated_by`), 2 kolom Reference (`status_distribusi`, `kode_sppg`)."}}

### Condition Overview

{{Narasi 2–4 kalimat menggambarkan kondisi keseluruhan dataset apa adanya. Sebut angka konkret dari tabel di atas. Contoh: "Dataset 12.450 baris × 18 kolom. Ditemukan 412 baris duplikat penuh (3,3%) dan 27 baris yang seluruh kolomnya kosong. 5 kolom punya >30% null dengan pola sistematis (null mengelompok pada periode Jan–Mar 2024). 3 kolom mencampur format tanggal."

⚠️ JANGAN tutup paragraf ini dengan kalimat seperti "Overall data quality: Medium" atau "DQ Score: 75%". Cukup deskripsi kondisi.}}

---

## 3. Column Profiling Highlights

> Pilih 5–10 kolom paling menonjol kondisinya (paling banyak null, paling banyak inkonsistensi, paling banyak outlier, atau yang paling berdampak ke proses bisnis). Tabel lengkap ada di CSV pendamping.
>
> **Format penulisan (dual-audience — bisa dibaca tim non-teknis):**
> Untuk setiap highlight, gunakan struktur:
> 1. Heading dengan ikon dampak ke proses bisnis: 🔴 (menghalangi proses bisnis inti / risiko keamanan-kepatuhan), 🟡 (perlu diketahui, tidak fatal), 🟢 (kondisi sehat yang layak disorot, jarang dipakai). **Ikon adalah indikator dampak proses bisnis, BUKAN skor kualitas data.**
> 2. Headline 1 baris **bahasa awam** setelah nama kolom.
> 3. Paragraf yang menjelaskan: (a) apa peran kolom seharusnya, (b) kondisi yang teramati dengan angka konkret bold + contoh nilai, (c) kalimat penutup "Ini kritis/penting karena…" yang menerjemahkan ke konsekuensi proses bisnis yang bisa dipahami non-teknis.
>
> **JANGAN** pakai jargon teknis tanpa terjemahan (NULL propagation, schema drift, primary key violation). **JANGAN** beri perintah cleaning. **JANGAN** beri skor.
>
> Sertakan **data_category** (Master/Reference/Transaksional/Log/Lainnya) di akhir headline untuk konteks peran kolom.

### {{🔴 atau 🟡 atau 🟢}} `{{COLUMN_NAME_1}}` — {{Headline plain language, 1 baris}} *(Kategori: {{DATA_CATEGORY}})*

{{Kalimat 1: Kolom ini seharusnya untuk [peran bisnis kolom — plain language].}} {{Kalimat 2–3: Kondisi aktual dengan **angka konkret bold** dan contoh nilai dalam `backtick`.}} {{Kalimat penutup: "Ini kritis/penting karena… [konsekuensi konkret ke proses bisnis yang bisa dipahami orang non-teknis — sebut fitur, keputusan, laporan, atau proses operasional yang terdampak].".}}

### {{ICON}} `{{COLUMN_NAME_2}}` — {{...}} *(Kategori: {{DATA_CATEGORY}})*

{{...}}

### {{ICON}} `{{COLUMN_NAME_3}}` — {{...}} *(Kategori: {{DATA_CATEGORY}})*

{{...}}

> **Contoh referensi (dari domain bahan makanan MBG — gaya yang dimaksud):**
>
> > ### 🔴 `kode_bahan` — Kode bahan tidak lengkap dan ada duplikat *(Kategori: Master)*
> >
> > Kolom ini seharusnya menjadi identifikasi unik setiap bahan (format 5 karakter: huruf + 3 digit, contoh `AP004`). Namun **347 baris (32,4%) tidak memiliki kode** dan **23 kode terduplikat** ditemukan (contoh: `AP019`, `BR018` masing-masing muncul 2 kali). Panjang karakter konsisten 5 untuk yang terisi — artinya format sudah standar, hanya pengisian yang bermasalah. Ini kritis karena kode bahan digunakan sebagai referensi lintas sistem; tanpa kode unik, bahan yang sama bisa tercatat ganda di menu, atau dua bahan beda dianggap sama.

---

## 4. Advanced Profiling Results

> Section ini hanya diisi jika metode Tier 2 diaktifkan.

### {{Time-Series Analysis — isi jika aktif}}
- Temporal frequency detected: {{daily/weekly/monthly/etc.}}
- Timestamp gaps: {{count}} missing periods detected
- Stationarity: {{ADF p-value: X.XX → stationary/non-stationary}}
- Trend: {{up/down/flat}} in column `{{col}}`

### {{Financial/Benford Analysis — isi jika aktif}}
- Benford's Law MAD for `{{col}}`: {{X.XXXX}} → {{close conformity/acceptable/suspect (label distribusi, bukan score kualitas)}}
- Round number concentration: {{X%}} of `{{col}}` values are round numbers

### {{Geospatial Analysis — isi jika aktif}}
- Null island (0,0) count: {{N}}
- Out-of-range coordinates: {{N}}

### {{Text/NLP Analysis — isi jika aktif}}
- PII detected in: {{columns}}
- Language distribution: {{primary language(s)}}

### {{Hierarchy Analysis — isi jika aktif}}
- Orphan records: {{N}}
- Circular references: {{Yes/No}}

---

## 5. Key Observations & Business Implications

### Kondisi yang Teramati (Key Observations)

> Susun 3–5 kondisi paling menonjol berdasarkan dampaknya ke proses bisnis (yang paling berdampak di atas). **Tanpa** label P0/P1/P2. **Tanpa** label kualitas.

1. **{{Judul kondisi}}** — {{Fakta + angka konkret + contoh baris/nilai. Contoh: "412 baris duplikat penuh (3,3%) — baris 1240 dan 8451 identik di seluruh 18 kolom."}}
2. **{{Judul kondisi}}** — {{...}}
3. **{{Judul kondisi}}** — {{...}}

### Implikasi terhadap Proses Bisnis (Per Audiens)

> Implikasi dipisah per audiens supaya bisa dibaca lintas peran. **Tanpa** perintah cleaning, **tanpa** skor.
>
> Jika dataset terlalu sederhana untuk diisi semua audiens, isi audiens yang relevan saja dan beri catatan singkat.

#### 👔 Untuk Pimpinan / Pengambil Keputusan

> Bahasa awam, no jargon. Fokus ke: apakah data ini bisa dipercaya untuk pelaporan eksternal/regulasi? Apa risiko reputasi/kepatuhan? Keputusan strategis apa yang berisiko salah? Sebut angka konkret tapi terjemahkan ke konsekuensi.

1. **{{Implikasi 1}}** — {{Contoh: "Data product master bahan belum bisa dipakai untuk melaporkan kepatuhan Angka Kecukupan Gizi (AKG) ke regulator — 15 zat gizi kunci belum direkam, sehingga klaim 'menu memenuhi AKG' tidak punya dasar data."}}
2. **{{Implikasi 2}}** — {{...}}

#### 🛠️ Untuk Tim Product

> Fokus ke fitur produk yang terdampak, pengalaman pengguna yang berisiko salah, kemampuan tampilan/pencarian/filter yang berpotensi menyimpang.

1. **{{Implikasi 1}}** — {{Contoh: "Fitur kalkulator gizi menu tidak dapat menampilkan angka akurat untuk kalsium/besi/vitamin C selama kolom mikronutrien belum diisi — pertimbangkan menampilkan placeholder 'data belum tersedia' alih-alih angka 0 yang menyesatkan."}}
2. **{{Implikasi 2}}** — {{...}}

#### ⚙️ Untuk Tim Data / Engineering

> Boleh teknis di sini. Fokus ke: dampak ke pipeline (join, parsing, ingestion), dependency ke tabel lain, dampak ke warehouse/mart, kebutuhan transformasi/normalisasi.

1. **{{Implikasi 1}}** — {{Contoh: "Saat join `master_bahan_makanan` ke `menu_komposisi` via `kode_bahan_correct`, 32,4% baris bahan akan orphan. Pertimbangkan join via primary key `id` sebagai fallback."}}
2. **{{Implikasi 2}}** — {{...}}

---

## 6. Next Discussion Points

> Topik yang layak dibahas dengan stakeholder berdasarkan kondisi yang teramati. **Bukan** rekomendasi cleaning — hanya pointer untuk diskusi lanjutan.

- **{{Pertanyaan diskusi 1}}** — {{Mengapa relevan berdasarkan kondisi yang ditemukan. Contoh: "Apakah duplikat full-row pada baris 1240/8451 berasal dari import ganda? Cek sumber ingestion."}}
- **{{Pertanyaan diskusi 2}}** — {{...}}
- **{{Pertanyaan diskusi 3}}** — {{...}}

### Saran arah EDA lanjutan

- **{{Pertanyaan analitis 1}}** — {{Mengapa relevan + kolom + jenis chart.}}
- **{{Pertanyaan analitis 2}}** — {{...}}

---

*Dibuat dengan skill `data-profiling-baseline`. File pendamping: `{{DATASET_NAME}}_profile.csv` (detail per kolom), `{{DATASET_NAME}}_charts/` (visualisasi kondisi), `{{DATASET_NAME}}_profile.pdf` (laporan lengkap). Laporan ini bersifat deskriptif kondisi — tidak mengukur kualitas data secara terskor.*
