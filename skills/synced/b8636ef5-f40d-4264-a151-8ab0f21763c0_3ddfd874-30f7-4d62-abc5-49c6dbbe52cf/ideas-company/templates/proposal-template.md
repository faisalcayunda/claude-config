# {{PROJECT_TITLE}}

**{{PROJECT_TAGLINE}}**

---

## 1. Latar Belakang dan Tujuan

### 1.1. Konteks Proyek

*Jelaskan secara singkat konteks dan masalah yang dihadapi klien. Hubungkan dengan tujuan strategis organisasi klien dan mengapa proyek ini penting untuk dilaksanakan sekarang.*

{{PROJECT_CONTEXT}}

### 1.2. Tujuan Proyek (SMART)

*Definisikan tujuan proyek secara spesifik, terukur, dapat dicapai, relevan, dan berbatas waktu untuk menyelaraskan ekspektasi.*

- **Specific:** {{SMART_SPECIFIC}}
- **Measurable:** {{SMART_MEASURABLE}}
- **Achievable:** {{SMART_ACHIEVABLE}}
- **Relevant:** {{SMART_RELEVANT}}
- **Time-Bound:** {{SMART_TIMEBOUND}}

---

## 2. Ruang Lingkup dan Hasil

### 2.1. Ruang Lingkup Proyek

*Detailkan batasan pekerjaan yang akan dilakukan dan yang tidak akan dilakukan untuk menghindari scope creep.*

**In-Scope (Termasuk dalam Lingkup):**

1.  {{INSCOPE_1}}
2.  {{INSCOPE_2}}
3.  {{INSCOPE_3}}
4.  {{INSCOPE_4}}
5.  {{INSCOPE_5}}

**Out-of-Scope (Tidak Termasuk dalam Lingkup):**

1.  {{OUTSCOPE_1}}
2.  {{OUTSCOPE_2}}
3.  {{OUTSCOPE_3}}

### 2.2. Deliverables Utama

*Sajikan daftar hasil kerja (deliverables) yang akan diserahkan kepada klien pada akhir proyek. Tabel ini akan diisi oleh skrip `generate_proposal.py` berdasarkan layanan yang dipilih.*

{{DELIVERABLES_TABLE}}

> **Catatan:** Untuk detail setiap deliverable dan template yang digunakan, silakan merujuk ke dokumen `references/service-deliverables-map.md`.

---

## 3. Pendekatan dan Metodologi

*Jelaskan bagaimana IDEAS akan melaksanakan proyek. Ini menunjukkan keunggulan proses dan metodologi yang kami gunakan.*

Kerangka kerja kami menyatukan praktik terbaik global yang telah teruji untuk memastikan kesuksesan proyek secara komprehensif:

-   **DAMA-DMBOK:** Sebagai basis pengetahuan fundamental untuk seluruh area manajemen data, termasuk tata kelola, kualitas, arsitektur, dan keamanan data. Kami juga mengantisipasi perkembangan DAMA-DMBOK 3.0 yang akan datang.
-   **Agile/CRISP-DM:** Untuk pengelolaan proyek yang adaptif, iteratif, dan fokus pada hasil, memastikan fleksibilitas terhadap perubahan dan pengiriman nilai secara berkala.
-   **PMBOK 6th & 7th Edition:** Untuk disiplin manajemen proyek yang terstruktur dan tata kelola yang kuat, memastikan proyek selesai tepat waktu dan sesuai anggaran.
-   **End-to-End Business Frameworks:** Mengintegrasikan analisis dari hulu ke hilir (BMC, VPC, BSC, Shipley, BABOK) untuk memastikan solusi data menjawab kebutuhan bisnis secara langsung.

---

## 4. Rencana Kerja dan Jadwal

### 4.1. Aktivitas Proyek per Bulan

*Gambarkan garis besar aktivitas yang akan dilakukan setiap bulan. Ini memberikan gambaran tentang alur kerja proyek.*

{{MONTHLY_ACTIVITIES}}

### 4.2. Jadwal Proyek (Timeline)

*Visualisasikan jadwal proyek dalam bentuk Gantt chart atau diagram lainnya untuk memberikan pemahaman yang jelas tentang durasi dan urutan setiap fase. Gambar ini dihasilkan oleh skrip `generate_timeline.py`.*

{{TIMELINE_VISUAL}}

---

## 5. Tim Proyek

*Perkenalkan tim yang akan bertanggung jawab atas keberhasilan proyek. Peran dan tanggung jawab yang jelas adalah kunci. Tabel ini diisi oleh `generate_proposal.py`.*

| # | Peran | Tanggung Jawab Utama |
| :--- | :--- | :--- |
{{TEAM_TABLE}}

> **Catatan:** Komposisi tim disesuaikan berdasarkan ruang lingkup dan layanan yang dipilih. Semua peran dan tarif mengacu pada `scripts/rate_card.py` untuk konsistensi.

---

## 6. Investasi dan Struktur Biaya

*Sajikan rincian investasi yang dibutuhkan secara transparan. Semua perhitungan dihasilkan oleh `calculate_project_cost.py`.*

| Item | Biaya |
| :--- | ---: |
| A. Jasa Profesional ({{HEADCOUNT}} Orang × {{MONTHS}} Bulan) | Rp {{PERSONNEL_COST}} |
| B. Biaya Operasional (Transportasi, Akomodasi, dll.) | Rp {{OPERATIONAL_COST}} |
| C. Manajemen Risiko (10% dari A+B) | Rp {{RISK_COST}} |
| **D. Total Anggaran yang Dibutuhkan (Sebelum PPN)** | **Rp {{TOTAL_COST}}** |
| E. PPN (11%) | Rp {{VAT_COST}} |
| **F. Total Investasi** | **Rp {{GRAND_TOTAL_COST}}** |

---

## 7. Asumsi, Risiko, dan Kepatuhan

### 7.1. Asumsi Proyek

*Sebutkan asumsi-asumsi yang menjadi dasar perencanaan proyek ini. Ini penting untuk menyamakan pemahaman.*

1.  Ketersediaan stakeholder dari pihak klien untuk wawancara dan diskusi sesuai jadwal.
2.  Akses yang diperlukan ke sistem, data, dan dokumentasi relevan diberikan tepat waktu.
3.  Lingkup pekerjaan tidak berubah secara signifikan selama proyek berlangsung.

### 7.2. Risiko dan Mitigasi

*Identifikasi potensi risiko yang dapat menghambat proyek dan jelaskan strategi mitigasi yang telah disiapkan.*

| Risiko | Dampak (T/S/R) | Probabilitas (T/S/R) | Rencana Mitigasi |
| :--- | :--- | :--- | :--- |
| Keterlambatan penyediaan data | Sedang | Sedang | Komunikasi proaktif dan eskalasi jika diperlukan. |
| Perubahan prioritas bisnis klien | Tinggi | Rendah | Proses manajemen perubahan yang terstruktur. |
| Keterbatasan SDM internal klien | Sedang | Tinggi | Program capacity building dan pendampingan intensif. |

### 7.3. Kepatuhan Regulasi dan Standar

*Jelaskan bagaimana proyek ini akan mematuhi regulasi yang berlaku untuk menjamin tata kelola yang baik.*

| Regulasi / Standar | Relevansi dengan Proyek |
| :--- | :--- |
| {{REGULATION_1}} | {{RELEVANCE_1}} |
| {{REGULATION_2}} | {{RELEVANCE_2}} |
| {{REGULATION_3}} | {{RELEVANCE_3}} |

> **Catatan Kepatuhan (Update 2025-2026):** Proyek ini dirancang selaras dengan kerangka hukum terbaru. Untuk **sektor pemerintah**, kami memastikan keselarasan dengan **UU PDP 27/2022** (berlaku penuh Okt 2024), **Perpres SDI 39/2019**, **Perpres SPBE 95/2018 & 132/2022**, serta regulasi pengadaan terbaru seperti **Perpres 46/2025**. Untuk **sektor swasta/BUMN**, kami merujuk pada standar internasional seperti **ISO 27001:2022** dan **ISO/IEC 42001** untuk tata kelola AI. Referensi lengkap tersedia di `references/regulatory-standards.md`.

---

## 8. Manajemen Perubahan dan Pemberdayaan

### 8.1. Pendekatan Manajemen Perubahan

*Adopsi solusi baru memerlukan manajemen perubahan yang efektif. Kami menerapkan pendekatan terstruktur untuk memastikan transisi yang mulus.*

| Fase | Aktivitas | Output |
| :--- | :--- | :--- |
| **Awareness** | Sosialisasi kepada stakeholder kunci | Pemahaman dan dukungan stakeholder |
| **Knowledge** | Workshop dan pelatihan sesuai peran | Peningkatan kompetensi tim |
| **Adoption** | Pendampingan implementasi (pilot project) | Proses kerja baru yang diadopsi |
| **Sustainability** | Monitoring dan rencana perbaikan berkelanjutan | Kemampuan mandiri untuk berkembang |

### 8.2. Rencana Capacity Building

*Jelaskan program pelatihan atau transfer pengetahuan yang akan dilakukan untuk membangun kemandirian klien.*

{{CAPACITY_BUILDING_PLAN}}

> **Catatan:** Rencana capacity building dapat disesuaikan, merujuk pada studi kasus sukses seperti program Jawara Data di `references/case-studies.md`.

---

## 9. Tentang IDEAS: Mitra Transformasi Data Anda

**PT Indonesian Data Ecosystem (IDEAS)** adalah firma konsultansi dan implementasi yang berfokus secara eksklusif pada ekosistem data. Kami membantu organisasi merancang, membangun, dan mengelola aset data untuk menghasilkan nilai berkelanjutan.

**Tiga Pilar Layanan Holistik:**

1.  **Advisory & Governance (Layanan S1.1–S1.5):** Merumuskan fondasi strategis, dari peta jalan, valuasi data (infonomics), hingga tata kelola AI.
2.  **Platform & Solution Implementation (Layanan S2.1–S2.6):** Implementasi teknis end-to-end, dari arsitektur data modern hingga solusi GenAI.
3.  **Empowerment & Managed Services (Layanan S3.1–S3.4):** Memastikan keberlanjutan melalui peningkatan kapasitas SDM dan layanan terkelola.

> Untuk katalog layanan lengkap, silakan lihat `references/services-catalog.md`.

---

## 10. Glosarium

*Daftar istilah dan akronim yang digunakan dalam proposal ini untuk memastikan pemahaman yang sama.*

| Istilah | Definisi |
| :--- | :--- |
| **AI** | Artificial Intelligence (Kecerdasan Buatan) |
| **DAMA-DMBOK** | Data Management Body of Knowledge dari DAMA International |
| **PDP** | Pelindungan Data Pribadi |
| **SPBE** | Sistem Pemerintahan Berbasis Elektronik |
| **GenAI** | Generative Artificial Intelligence |

---

**PT Indonesian Data Ecosystem (IDEAS)**
Komplek Margahayu Raya, Jl. Uranus IV Blok C3 No.59, Bandung 40286, Indonesia
contact@data-ecosystem.id | https://data-ecosystem.id
