# Data Profiling Overview — {{PROJECT_OR_ORG_NAME}}

> **Tanggal profiling:** {{DATE}}
> **Cakupan:** {{N_TABLES}} tabel di {{N_DATA_PRODUCTS}} data product
> **Profiler:** data-profiling-baseline
> **Sifat laporan:** Deskriptif kondisi data (apa adanya). **Tidak mengandung skor kualitas data per dimensi maupun skor agregat.** Laporan ini bersifat dual-audience: bagian eksekutif dapat dibaca pimpinan tanpa konteks teknis; implikasi disegmentasi per audiens (Pimpinan / Tim Product / Tim Data-Engineering).

---

## 🎯 Ringkasan Eksekutif (untuk Pimpinan)

> **Aturan penulisan:** 3–5 kalimat **bahasa awam tanpa jargon teknis**. Jika seorang direktur cuma baca paragraf ini, mereka harus tahu kondisi keseluruhan dan dampaknya untuk operasi/keputusan bisnis. Sebut angka konkret tapi terjemahkan ke konsekuensi operasional. **JANGAN** tutup dengan label kualitas atau skor.

{{Contoh isi: "Profiling mencakup 5 tabel di 2 data product (Master Bahan Makanan dan Distribusi Harian MBG). Data product Master Bahan belum dapat dipakai untuk pelaporan capaian Angka Kecukupan Gizi (AKG) karena 15 zat gizi kunci belum direkam dan 32% bahan tidak punya kode pengenal unik. Data product Distribusi Harian sudah dapat dipakai untuk monitoring volume penyaluran, tetapi ada 412 baris duplikat yang akan menggandakan total porsi jika dipakai langsung dalam pelaporan harian. Tiga tabel master memiliki inkonsistensi format waktu (timezone) yang akan menyebabkan urutan kejadian terlihat tidak benar saat dianalisis lintas tabel."}}

---

## 📋 Cakupan Profiling

| Data Product | Tabel | Baris | Kolom | Klasifikasi | Kondisi Paling Menonjol |
|---|---|---|---|---|---|
| {{DP1_NAME}} | `{{table_a}}` | {{N}} | {{M}} | {{Master/Transaksional/...}} | {{Plain-language 1 kalimat — kondisi terkritis.}} |
| {{DP1_NAME}} | `{{table_b}}` | {{N}} | {{M}} | {{...}} | {{...}} |
| {{DP2_NAME}} | `{{table_c}}` | {{N}} | {{M}} | {{...}} | {{...}} |
| ... | ... | ... | ... | ... | ... |

---

## 📦 Sorotan per Data Product

> Untuk setiap data product, struktur yang sama: konteks bisnis → kondisi utama bahasa awam → implikasi 3-audiens → diskusi lanjutan.

---

### 📦 Data Product: {{DP1_NAME}}

**Tujuan bisnis:** {{1–2 kalimat plain language menjelaskan apa yang data product ini dukung di proses bisnis. Contoh: "Menyediakan referensi master bahan makanan beserta kandungan gizinya untuk perhitungan menu MBG sesuai standar AKG."}}

**Tabel yang dicakup:** `{{table_a}}` ({{N_a}} baris), `{{table_b}}` ({{N_b}} baris)

**Stakeholder utama:** {{Tim/peran yang menggunakan data ini.}}

**Regulasi/standar terkait:** {{Standar atau aturan yang berlaku, jika ada.}}

#### 🔍 Kondisi Utama yang Teramati

> Agregasikan 4–8 sorotan paling penting dari highlights tabel-tabel di dalam data product ini. Pakai format yang sama dengan section 3 di laporan per-tabel: ikon 🔴/🟡/🟢 + headline bahasa awam + paragraf penjelasan. Hindari menyalin semua highlight dari setiap tabel — pilih yang paling berdampak lintas tabel di data product ini.

🔴 **{{Headline plain language 1}}** — {{Paragraf penjelasan: peran kolom/kondisi → fakta + angka bold + contoh → konsekuensi konkret ke proses bisnis. Sebut tabel asalnya: "(dari `table_a`)".}}

🔴 **{{Headline plain language 2}}** — {{...}}

🟡 **{{Headline plain language 3}}** — {{...}}

🟡 **{{Headline plain language 4}}** — {{...}}

🟡 **{{Headline plain language 5}}** — {{...}}

#### 💼 Implikasi terhadap Proses Bisnis

##### 👔 Untuk Pimpinan / Pengambil Keputusan

> Bahasa awam. Fokus ke: bisa-tidaknya data dipakai untuk pelaporan eksternal/regulasi, risiko reputasi/kepatuhan, keputusan strategis yang berisiko salah, biaya/value yang berisiko hilang. Sebut data product mana yang siap pakai vs belum.

- **{{Implikasi 1}}** — {{Contoh: "Data product ini belum bisa dipakai untuk pelaporan capaian AKG program MBG ke pihak luar. 15 zat gizi kunci (kalsium, besi, vitamin C, dst.) belum direkam, sehingga klaim 'menu memenuhi standar gizi nasional' tidak punya dasar data yang bisa diaudit."}}
- **{{Implikasi 2}}** — {{...}}
- **{{Implikasi 3}}** — {{...}}

##### 🛠️ Untuk Tim Product

> Fokus ke fitur produk yang terdampak, UX yang berisiko salah, kemampuan tampilan/pencarian/filter yang berpotensi menyimpang, asumsi produk yang tidak terpenuhi.

- **{{Implikasi 1}}** — {{Contoh: "Fitur 'kalkulator gizi menu' tidak dapat menampilkan angka akurat untuk mikronutrien — pertimbangkan menampilkan placeholder 'data belum tersedia' alih-alih angka 0 yang berisiko menyesatkan pengguna."}}
- **{{Implikasi 2}}** — {{...}}
- **{{Implikasi 3}}** — {{...}}

##### ⚙️ Untuk Tim Data / Engineering

> Boleh teknis. Fokus ke dampak ke pipeline (join, parsing, ingestion), dependency ke tabel lain (master/reference), dampak ke warehouse/mart/dashboard, kebutuhan normalisasi/standardisasi schema.

- **{{Implikasi 1}}** — {{Contoh: "Join `master_bahan_makanan` ↔ `menu_komposisi` via `kode_bahan` akan menyebabkan 32,4% baris bahan orphan. Pertimbangkan join via primary key `id` sebagai jalur utama; `kode_bahan` dipakai hanya untuk display."}}
- **{{Implikasi 2}}** — {{...}}
- **{{Implikasi 3}}** — {{...}}

#### 💬 Diskusi Lanjutan yang Disarankan

> 2–4 pertanyaan/topik yang layak dibahas dengan stakeholder berdasarkan kondisi yang teramati di data product ini. **Bukan** perintah cleaning — hanya pointer untuk diskusi lanjutan.

- **{{Pertanyaan 1}}** — {{Mengapa relevan berdasarkan kondisi yang teramati.}}
- **{{Pertanyaan 2}}** — {{...}}

---

### 📦 Data Product: {{DP2_NAME}}

**Tujuan bisnis:** {{...}}

**Tabel yang dicakup:** {{...}}

**Stakeholder utama:** {{...}}

**Regulasi/standar terkait:** {{...}}

#### 🔍 Kondisi Utama yang Teramati

🔴 **{{...}}** — {{...}}

🟡 **{{...}}** — {{...}}

#### 💼 Implikasi terhadap Proses Bisnis

##### 👔 Untuk Pimpinan / Pengambil Keputusan
- **{{...}}** — {{...}}

##### 🛠️ Untuk Tim Product
- **{{...}}** — {{...}}

##### ⚙️ Untuk Tim Data / Engineering
- **{{...}}** — {{...}}

#### 💬 Diskusi Lanjutan yang Disarankan
- **{{...}}** — {{...}}

---

{{Ulangi blok "📦 Data Product:" untuk setiap data product yang dicakup.}}

---

## 🔗 Tema Lintas Data Product

> Kondisi yang muncul di **lebih dari satu data product** — biasanya menandakan akar masalah sistemik di proses ingest, schema design, atau governance organisasi. 3–6 tema. Pakai bahasa awam di kalimat pertama, baru ke detail teknis di lanjutan.

- **{{Tema 1: Headline bahasa awam}}** — {{Penjelasan: kondisi apa yang muncul, di data product/tabel mana saja, mengapa ini sistemik. Contoh: "Inkonsistensi konvensi waktu antar tabel — 3 dari 5 tabel master menyimpan `created_at` dengan timezone (+07:00) tapi `updated_at` tanpa timezone. Mengindikasikan pola implementasi yang tidak seragam antar developer/batch yang menulis ke tabel ini. Akibatnya, urutan kejadian saat melacak perubahan data lintas tabel bisa terlihat tidak konsisten."}}
- **{{Tema 2}}** — {{...}}
- **{{Tema 3}}** — {{...}}

### 💼 Implikasi Lintas Data Product (Per Audiens)

##### 👔 Untuk Pimpinan / Pengambil Keputusan
- **{{Implikasi sistemik 1}}** — {{Contoh: "Belum adanya konvensi waktu yang seragam di seluruh data product berarti laporan audit/forensik lintas tabel bisa terlihat tidak akurat di mata regulator/pihak eksternal."}}
- **{{Implikasi sistemik 2}}** — {{...}}

##### 🛠️ Untuk Tim Product
- **{{Implikasi sistemik 1}}** — {{...}}

##### ⚙️ Untuk Tim Data / Engineering
- **{{Implikasi sistemik 1}}** — {{Contoh: "Perlu kebijakan tunggal untuk format timestamp (mis. selalu UTC + ISO 8601) yang diberlakukan via constraint di schema atau via lapisan validasi ingest."}}

---

## 📚 Lampiran — Laporan per Tabel

| Data Product | Tabel | Markdown | CSV | PDF | Charts |
|---|---|---|---|---|---|
| {{DP1_NAME}} | `{{table_a}}` | [`{{table_a}}_profile.md`](./{{table_a}}_profile.md) | [`{{table_a}}_profile.csv`](./{{table_a}}_profile.csv) | [`{{table_a}}_profile.pdf`](./{{table_a}}_profile.pdf) | [`{{table_a}}_charts/`](./{{table_a}}_charts/) |
| {{DP1_NAME}} | `{{table_b}}` | ... | ... | ... | ... |
| {{DP2_NAME}} | `{{table_c}}` | ... | ... | ... | ... |

---

*Laporan ini dibuat dengan skill `data-profiling-baseline`. Bersifat deskriptif kondisi (apa adanya) — tidak mengandung skor kualitas data dan tidak mengandung perintah cleaning. Keputusan tindak lanjut (cleaning, transformasi, kebijakan governance) diserahkan ke tim yang punya konteks SLA dan kebijakan organisasi.*
