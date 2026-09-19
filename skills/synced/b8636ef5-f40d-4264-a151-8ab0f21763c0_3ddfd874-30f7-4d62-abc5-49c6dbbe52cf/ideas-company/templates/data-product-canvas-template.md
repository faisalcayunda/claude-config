# Data Product Canvas Template

*Version: 2.0.0 (Last Updated: 2026-02-20)*

## Sumber

Diadaptasi dari [datamesh-architecture.com/data-product-canvas](https://www.datamesh-architecture.com/data-product-canvas) oleh J. Majchrzak, S. Balk, H. Noorman, J. Gienger. Dilisensikan di bawah CC BY 4.0. Diperkaya dengan konteks dan standar dari PT Indonesian Data Ecosystem (IDEAS).

## Petunjuk Penggunaan

Canvas ini digunakan dalam workshop **Discovery** (tahap *Identify* dan *Define* dalam Data Product Lifecycle) untuk mendefinisikan data product sebelum pembangunan dimulai. Isi setiap building block secara berurutan (1-10) dalam sesi kolaboratif bersama domain expert, data engineer, dan product owner.

**Durasi workshop:** 90-120 menit per data product
**Peserta:** Product Owner, Domain Expert, Data Engineer, Data Architect, Business Analyst, Data Governance Lead.

> **Cross-Reference:** Proses ini merupakan bagian dari fase "Define" dalam `references/digital-data-product-lifecycle.md`.

---

## Canvas

### 1. Domain

| Field | Value |
| :--- | :--- |
| **Domain Name** | {Nama domain bisnis yang selaras dengan arsitektur data mesh, contoh: "Kependudukan", "Keuangan", "Transportasi"} |
| **Domain Owner** | {Nama dan jabatan pemilik domain, yang bertanggung jawab atas aset data di dalamnya, contoh: "Dr. Budi Santoso, Kepala Dinas Kependudukan"} |
| **Domain Team** | {Tim lintas fungsi yang bertanggung jawab atas domain ini, contoh: "Tim Data Kependudukan"} |
| **Contact** | {Email/telepon domain owner, contoh: "budi.santoso@prov.go.id"} |

### 2. Data Product Name

| Field | Value |
| :--- | :--- |
| **Product Name** | {Nama unik mengikuti naming convention `dp-<domain>-<nama>`, contoh: "dp-kependudukan-master"} |
| **Display Name** | {Nama yang mudah dipahami dan ditampilkan ke pengguna, contoh: "Master Data Kependudukan"} |
| **Version** | {Versi semantik, contoh: "1.0.0"} |
| **Classification** | {Pilih salah satu: `Source-aligned`, `Aggregate`, atau `Consumer-aligned`} |

### 3. Consumer and Use Case(s)

| Consumer | Use Case | Business Value |
| :--- | :--- | :--- |
| {Siapa (tim/aplikasi) yang akan menggunakan data product ini?} | {Untuk tujuan spesifik apa mereka menggunakannya?} | {Nilai bisnis terukur apa yang dihasilkan dari use case tersebut?} |
| {Contoh: Kepala Dinas Kesehatan} | {Monitoring prevalensi penyakit menular per kecamatan secara harian} | {Mempercepat alokasi sumber daya kesehatan hingga 48 jam} |
| {Contoh: Tim Perencanaan Bappeda} | {Proyeksi kebutuhan infrastruktur pendidikan untuk 5 tahun ke depan} | {Meningkatkan akurasi perencanaan APBD 2027 berbasis data} |
| {Contoh: Startup Logistik via API} | {Optimasi rute pengiriman real-time berdasarkan kepadatan penduduk} | {Potensi pengurangan biaya operasional logistik sebesar 15%} |

**North Star Metric (NSM):** {Satu metrik utama yang paling efektif menunjukkan keberhasilan data product ini, contoh: "Jumlah keputusan kebijakan strategis yang mengutip data product ini per kuartal"}

### 4. Data Contract (ODCS-Aligned)

> Selaras dengan Open Data Contract Standard (ODCS). Lihat `references/digital-data-product-lifecycle.md` untuk detail implementasi dan tata kelola, termasuk ODPQ (Open Data Product Quality) Framework.

**Output Ports:**

| Port Type | Format | Schema/Endpoint | SLA |
| :--- | :--- | :--- | :--- |
| [ ] Table/View | {PostgreSQL, BigQuery, dll.} | {nama_skema.nama_tabel, contoh: `kependudukan.master_penduduk_agregat`} | {Freshness: daily (06:00 WIB), Availability: 99.5%} |
| [ ] File | {CSV, Parquet, JSON} | {path/filename pattern, contoh: `s3://bucket/path/YYYY-MM-DD.parquet`} | {Delivery: T+1} |
| [ ] API | {REST, GraphQL} | {/api/v1/endpoint, contoh: `/api/v1/penduduk/nik/{nik}`} | {Latency: <500ms, Uptime: 99.9%} |
| [ ] Stream | {Kafka, Pub/Sub} | {nama_topik, contoh: `kependudukan.events.v1`} | {Lag: <5min} |
| [ ] Dashboard | {Tableau, Metabase} | {URL dashboard} | {Refresh: hourly} |

**Data Quality Expectations:**

| Dimension | Threshold | Measurement |
| :--- | :--- | :--- |
| Completeness | ≥ {99}% | {Persentase field non-null untuk kolom krusial (NIK, Nama, Alamat)} |
| Accuracy | ≥ {99.5}% | {Tingkat kecocokan NIK terhadap data Dukcapil Pusat sebagai sumber kebenaran} |
| Timeliness | ≤ {12} jam | {Waktu dari event (kelahiran/kematian) hingga tersedia di master data} |
| Uniqueness | = {100}% | {Tidak ada duplikasi NIK pada tabel master} |
| Consistency | ≥ {98}% | {Konsistensi kode wilayah (prov/kab/kec) dengan referensi `dp-referensi-wilayah-kemendagri`} |

**Terms of Service:**

| Term | Definition |
| :--- | :--- |
| {Retention} | {Data disimpan selama 10 tahun sesuai Peraturan Arsip Nasional} |
| {Access} | {Role-based (RBAC), hanya user dari Dinas Kependudukan dan Dinkes yang memiliki akses read} |
| {Privacy} | {PII (NIK, Nama, Tgl Lahir) di-mask untuk level akses publik, dienkripsi saat transit dan at-rest sesuai UU PDP} |
| {Pricing} | {Model biaya: Gratis untuk internal pemerintah, berbasis subscription untuk eksternal via API} |

### 5. Sources (Input Ports)

| Source System / Data Product | Type | Frequency | Owner |
| :--- | :--- | :--- | :--- |
| {Nama sistem sumber atau data product lain} | [ ] Operational DB [ ] API [ ] File [ ] Other DP | {Real-time / Daily / Weekly} | {Tim/orang yang mengelola sumber} |
| {Contoh: SIAK Terpusat} | Operational DB | Daily (sinkronisasi malam) | Dinas Dukcapil |
| {Contoh: Aplikasi Mobile LaporLahir} | API | Real-time | Tim Inovasi Digital |
| {Contoh: `dp-referensi-wilayah-kemendagri`} | Data Product | Weekly | Tim Data Referensi |

### 6. Data Product Architecture

**Internal Processing:**

```mermaid
graph TD
    A[Input: SIAK DB] --> B(Ingestion: Airbyte);
    C[Input: LaporLahir API] --> B;
    D[Input: DP Wilayah] --> B;
    B --> E{Storage: Data Lake (S3)};
    E --> F[Transformation: dbt];
    F --> G{Storage: DWH (BigQuery)};
    G --> H[Output: Tabel Agregat];
    G --> I[Output: API via FastAPI];
    G --> J[Output: Dashboard Metabase];
    subgraph Monitoring
        K(Great Expectations)
    end
    E --> K;
    F --> K;
    G --> K;
```

| Component | Technology | Description |
| :--- | :--- | :--- |
| Ingestion | {Airbyte, Kafka Connect, Custom ETL} | {Contoh: Menggunakan Airbyte untuk replikasi dari PostgreSQL SIAK ke Data Lake} |
| Storage | {MinIO S3, BigQuery, PostgreSQL} | {Contoh: MinIO S3 sebagai Data Lake (bronze), BigQuery sebagai DWH (silver, gold)} |
| Transformation | {dbt, Apache Spark, Python} | {Contoh: Model dbt untuk membersihkan, mendeduplikasi, dan mengagregasi data penduduk} |
| Serving | {FastAPI, Metabase, Direct Query} | {Contoh: FastAPI untuk menyediakan API RESTful, Metabase untuk dashboard internal} |
| Monitoring | {Great Expectations, Monte Carlo} | {Contoh: Great Expectations untuk validasi skema dan data quality di setiap tahap transformasi} |

### 7. Ubiquitous Language (Glossary)

| Term | Definition | Context |
| :--- | :--- | :--- |
| {Istilah domain kunci} | {Definisi tunggal yang disepakati bersama oleh tim bisnis dan teknis} | {Konteks penggunaan dan contoh} |
| {Contoh: "Penduduk Aktif"} | {Penduduk dengan status KTP-el aktif dan berdomisili di wilayah administrasi provinsi per tanggal data diproses} | {Digunakan dalam semua laporan kependudukan bulanan untuk perencanaan} |
| {Contoh: "Angka Partisipasi Kasar (APK)"} | {Rasio jumlah siswa, berapapun usianya, yang sedang sekolah di tingkat pendidikan tertentu terhadap jumlah penduduk kelompok usia yang sesuai dengan tingkat pendidikan tersebut.} | {Metrik utama dalam perencanaan pendidikan dan evaluasi program} |

### 8. Key Stakeholders & Team

| Role | Name / Team | Responsibilities |
| :--- | :--- | :--- |
| **Product Owner** | {Nama} | {Mendefinisikan visi produk, prioritas backlog, dan memastikan nilai bisnis tercapai} |
| **Domain Owner** | {Nama} | {Menjamin kualitas dan akurasi data dari sisi bisnis, memberikan konteks domain} |
| **Data Architect** | {Nama} | {Merancang arsitektur teknis, memastikan skalabilitas dan integrasi sistem} |
| **Data Engineer** | {Tim/Nama} | {Membangun dan memelihara pipeline data, dari ingestion hingga serving} |
| **Business Analyst** | {Nama} | {Menganalisis kebutuhan pengguna, menerjemahkannya menjadi requirement teknis} |
| **Data Governance** | {Tim/Nama} | {Memastikan kepatuhan terhadap kebijakan, standar kualitas, dan privasi data} |

### 9. Risks and Mitigations

| Risk Category | Description | Mitigation Strategy |
| :--- | :--- | :--- |
| **Data Quality** | {Data dari sistem sumber (SIAK) sering terlambat atau tidak lengkap} | {Implementasi DQ monitoring dengan Great Expectations di tahap ingestion; eskalasi otomatis ke Domain Owner jika SLA sumber terlewat} |
| **Regulatory** | {Perubahan pada UU PDP atau peraturan turunan yang mempengaruhi pemrosesan PII} | {Libatkan tim Data Governance sejak awal; lakukan Privacy Impact Assessment (PIA) secara berkala} |
| **Adoption** | {Calon konsumen (Dinas Kesehatan) enggan beralih dari sistem lama mereka} | {Lakukan roadshow dan sesi pelatihan; bangun dashboard yang menjawab langsung KPI mereka; sediakan support channel yang responsif} |
| **Technical** | {Kompleksitas transformasi data lebih tinggi dari perkiraan awal} | {Gunakan pendekatan agile dengan rilis inkremental; mulai dengan use case paling bernilai; alokasikan buffer 20% pada estimasi effort} |

### 10. Classification & Dependencies

| Aspect | Value |
| :--- | :--- |
| **Type** | [ ] Source-aligned [ ] Aggregate [X] Consumer-aligned |
| **Justification** | {Mengapa klasifikasi ini dipilih, contoh: "Data product ini dirancang khusus untuk use case perencanaan Bappeda, menggabungkan dan mengagregasi data dari beberapa domain."} |
| **Upstream Dependencies** | {Data product lain yang menjadi input, contoh: `dp-referensi-wilayah-kemendagri`, `dp-keuangan-belanja-daerah`} |
| **Downstream Consumers** | {Data product atau aplikasi lain yang menggunakan output ini, contoh: `app-dashboard-eksekutif`, `dp-agregat-kesehatan-dinkes`} |

---

## Metadata

| Field | Value |
| :--- | :--- |
| **Created Date** | {YYYY-MM-DD} |
| **Created By** | {Nama fasilitator workshop, contoh: "Ahmad Zaelani (IDEAS)"} |
| **Last Updated** | {YYYY-MM-DD} |
| **Status** | [X] Draft [ ] In Review [ ] Approved [ ] In Development [ ] Live [ ] Deprecated |
| **Related Service** | {S2.2 Core Data Platform & Modernization, S2.4 Data Mesh & Data Product Development} |
| **Related Epic** | {Link atau ID epic dalam backlog, contoh: "EPIC-345: Pembangunan Master Data Kependudukan"} |

---

## Workshop Facilitation Guide

### Persiapan (Sebelum Workshop)
1.  Identifikasi domain dan peserta yang relevan (lihat seksi 8).
2.  Kumpulkan daftar use case yang sudah diketahui dan metrik bisnis yang relevan.
3.  Siapkan whiteboard/Miro board dengan template canvas ini.
4.  Fasilitator membaca `references/digital-data-product-lifecycle.md` untuk memahami konteks.

### Urutan Pengisian (Selama Workshop)
1.  **Domain & Naming** (10 menit) — Tentukan kepemilikan dan identitas.
2.  **Consumer & Use Cases** (20 menit) — Mulai dari kebutuhan pengguna dan nilai bisnis.
3.  **Data Contract** (20 menit) — Definisikan janji (output, SLA, kualitas) kepada konsumen.
4.  **Sources** (10 menit) — Identifikasi input yang dibutuhkan.
5.  **Architecture** (15 menit) — Desain kasar bagaimana produk akan dibangun.
6.  **Stakeholders & Risks** (15 menit) — Petakan tim dan antisipasi masalah.
7.  **Ubiquitous Language & Classification** (10 menit) — Sepakati terminologi dan posisi dalam ekosistem.

### Tindak Lanjut (Setelah Workshop)
1.  Dokumentasikan canvas dalam format digital ini dan simpan di repositori Git.
2.  Validasi dengan stakeholder yang tidak hadir.
3.  Buat user stories/PBI berdasarkan canvas dan masukkan ke dalam backlog produk.
4.  Gunakan skrip `scripts/estimate_service_cost.py` untuk estimasi effort awal.

---

## AI/GenAI Readiness Assessment (Opsional)

| Aspek | Status | Catatan |
| :--- | :--- | :--- |
| **GenAI Use Case Potential** | [ ] High [ ] Medium [ ] Low [ ] N/A | {Apakah data product ini dapat menjadi input untuk model GenAI? Contoh: "Data demografi agregat dapat digunakan untuk fine-tuning model analisis sentimen publik terhadap kebijakan baru."} |
| **Vector Embedding Ready** | [ ] Ya [ ] Tidak [ ] Planned | {Apakah data (terutama tekstual) dapat di-embed untuk semantic search/RAG? Contoh: "Tidak, data mayoritas terstruktur. Namun, planned untuk membuat embedding dari deskripsi pekerjaan untuk job matching."} |
| **Data Quality for AI** | [ ] Sufficient [ ] Needs Improvement | {Apakah kualitas data (akurasi, kelengkapan, bias) memenuhi threshold untuk AI training? Contoh: "Kualitas data cukup untuk analisis statistik, namun perlu audit bias lebih lanjut sebelum training model prediktif."} |
| **Responsible AI Considerations** | {FATE: Fairness, Accountability, Transparency, Ethics} | {Pertimbangan bias dan etika. Contoh: "Potensi bias dalam data historis alokasi bantuan sosial perlu dianalisis dan dimitigasi sebelum digunakan untuk model prediksi kelayakan."} |

> **Cross-Reference:** Lihat `references/products-catalog.md` untuk kapabilitas GenAI per produk IDEAS. Lihat `references/thought-leadership-frameworks.md` (Seksi 16) untuk AI Governance Framework. Lihat `references/service-delivery-patterns.md` untuk panduan teknis implementasi AI yang bertanggung jawab.
