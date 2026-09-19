# Portfolio Showcase: Ekosistem Data Jawa Barat

Dokumen ini mendokumentasikan secara komprehensif Ekosistem Data Jawa Barat — flagship project yang dibangun oleh CEO IDEAS selama menjabat sebagai Head of Data / Head of Tribe Ekosistem Data di Jabar Digital Service (JDS), Pemerintah Provinsi Jawa Barat (2019–2024). Dokumen ini berfungsi sebagai referensi utama portfolio dan showcase kapabilitas IDEAS.

> **International Benchmark:** Estonia's X-Road platform saves 1,345 years of annual working time and has been adopted by 20+ countries. Jabar Data Exchange (launched December 5, 2024) represents Indonesia's local implementation of similar secure data exchange principles, demonstrating that the Jabar ecosystem is aligned with global best practices in government data infrastructure.

> **Catatan Evolusi & Aktualitas Data (Konteks per Februari 2026):** Proyek Ekosistem Data Jabar terus berevolusi dan berkembang di bawah manajemen Jabar Digital Service setelah periode kepemimpinan awal (2019-2024) yang didokumentasikan di sini. Metrik, statistik, dan jumlah dataset yang disajikan dalam dokumen ini merefleksikan pencapaian hingga akhir tahun 2024. Untuk analisis terkini, disarankan untuk merujuk pada data terbaru langsung dari portal resmi terkait.

## Table of Contents

1. [Konteks Organisasi: Jabar Digital Service](#1-konteks-organisasi-jabar-digital-service)
2. [Visi & Grand Design](#2-visi--grand-design)
3. [7 Komponen Ekosistem](#3-7-komponen-ekosistem)
4. [Core Data Jabar: Platform Inti](#4-core-data-jabar-platform-inti)
5. [Arsitektur Teknologi & Tech Stack](#5-arsitektur-teknologi--tech-stack)
6. [Data Quality Management Framework](#6-data-quality-management-framework)
7. [Program Pemberdayaan Data](#7-program-pemberdayaan-data)
8. [Use Cases & Policy Analytics](#8-use-cases--policy-analytics)
9. [Pencapaian & Penghargaan](#9-pencapaian--penghargaan)
10. [Landasan Hukum](#10-landasan-hukum)
11. [DAMA Knowledge Areas Applied](#11-dama-knowledge-areas-applied)
12. [Selling Points vs Competitors](#12-selling-points-vs-competitors)

---

## 1. Konteks Organisasi: Jabar Digital Service

**Jabar Digital Service (JDS)** adalah UPTD (Unit Pelaksana Teknis Daerah) di bawah Dinas Komunikasi dan Informatika Provinsi Jawa Barat, berfungsi sebagai "Pusat Layanan Digital, Data, dan Informasi Geospasial."

### Manajemen Agile (Tribe Model)

JDS mengadopsi sistem tribe (referensi McKinsey & Company) dengan 5 tribe utama:

| Tribe | Produk Utama |
| :--- | :--- |
| **Ekosistem Data Jabar** | Portal Data Jabar, Dashboard Jabar, Jabar Form |
| Gov. Operation & Services | SIDEBAR, SIPD, DigiTeam |
| Citizen Engagement (Program) | Jabar Digital Academy, Desa Digital, Hotline Jabar |
| Citizen Engagement (Product) | Sapawarga, Portal Jabar, J-Site |
| R&D | Riset & Analisis Kebijakan |

CEO IDEAS memimpin **Tribe Ekosistem Data Jabar** — tribe yang bertanggung jawab atas seluruh infrastruktur data dan analytics provinsi.

### Visi JDS

> "Menjadikan Jawa Barat sebagai provinsi terdepan dalam penggunaan data dan teknologi untuk mendukung layanan publik dan perumusan kebijakan yang lebih responsif, adaptif, dan inovatif."

### 3 Goals Strategis

1. **Pemanfaatan Data** — pengambilan keputusan & perumusan kebijakan berbasis data
2. **Pengembangan Kehidupan Masyarakat** melalui teknologi digital
3. **Transformasi Digital Pemerintahan**

---

## 2. Visi & Grand Design

### Visi Ekosistem Data Jabar

> "Menjadi *data ecosystem solutions* dalam pengembangan masyarakat dan pemerintah yang unggul melalui penyediaan data, informasi, dan pengetahuan yang berkualitas sehingga dapat memudahkan *data-driven decision making*."

### Grand Design Layanan Digital

Arsitektur grand design menghubungkan 3 tipe pengguna ke ekosistem data:

| Pengguna | Platform | Fungsi |
| :--- | :--- | :--- |
| ASN (Pegawai) | Portal Administrasi | Operasional pemerintahan |
| Gubernur/Wakil/Sekda/Kepala PD | Executive Dashboard | Data-driven decision making |
| Masyarakat/Bisnis | Sapawarga, Portal Jabarprov | Layanan publik & transparansi |

Seluruh platform terhubung melalui **Jabar Data Exchange (SPLP)** — Sistem Penghubung Layanan Pemerintah yang mengintegrasikan data dari SPLP Kota/Kabupaten hingga SPLP Pemerintah Pusat.

### Value Proposition

Ekosistem Data Jabar menyelesaikan 4 masalah fundamental:

| Masalah | Solusi |
| :--- | :--- |
| **Ketersediaan Data** — "data ada dimana-mana, tetapi mencari data kemana-mana" | Data Marketplace (3 klik untuk menemukan data) |
| **Standardisasi Data** — "belum memiliki standar, garbage in garbage out" | Kualitas terbaik, akurat, mutakhir |
| **Metadata** — "tidak memiliki identitas dan keterangan lengkap" | Informasi lengkap dan jelas |
| **Interoperabilitas Data** — "belum memiliki mekanisme integrasi" | Mudah terintegrasi |

Dampak: proses permintaan data yang sebelumnya memakan waktu **±1 bulan** (surat manual → surat menumpuk → penyediaan manual) kini dapat dilakukan dalam **hitungan detik** melalui Portal Data Jabar.

---

## 3. 7 Komponen Ekosistem

| # | Komponen | URL | Fungsi Utama |
| :-: | :--- | :--- | :--- |
| 1 | **Ekosistem Data Jabar** | [data.jabarprov.go.id](https://data.jabarprov.go.id) | Gateway utama, mengintegrasikan seluruh komponen data |
| 2 | **Satu Data Jabar** | [satudata.jabarprov.go.id](https://satudata.jabarprov.go.id) | Kelola dan berbagi data akurat di lingkungan Pemprov |
| 3 | **Open Data Jabar** | [opendata.jabarprov.go.id](https://opendata.jabarprov.go.id) | Transparansi data dan informasi publik |
| 4 | **Satu Peta Jabar** | [satupeta.jabarprov.go.id](https://satupeta.jabarprov.go.id) | Publikasi dan bagi pakai data geospasial |
| 5 | **Citizen Dashboard** | [dashboard.jabarprov.go.id](https://dashboard.jabarprov.go.id) | Dashboard publik: 12 sektor, 32 sub-sektor |
| 6 | **Executive Dashboard** | [dashboard.jabarprov.go.id/executive](https://dashboard.jabarprov.go.id/executive) | Dashboard eksekutif: kebijakan data-driven |
| 7 | **Jabar Form** | [form.jabarprov.go.id](https://form.jabarprov.go.id) | Platform formulir dan pengumpulan data |

### Satu Data Jabar

Platform internal untuk mengelola dan berbagi data akurat. Mencakup 10 kategori: Ekonomi, Kemiskinan, Kesehatan, Pariwisata & Kebudayaan, Pendidikan, Infrastruktur, Kependudukan, Lingkungan Hidup, Pemerintah & Desa, Sosial.

**Proses Input Data (3 langkah):**
1. **INPUT** — Tambah/Ubah Dataset oleh Pengelola Data dari OPD
2. **VERIFICATION** — Verifikasi kelengkapan dan kualitas data oleh Walidata
3. **RELEASE** — Rilis dataset sesuai klasifikasi

**Klasifikasi Data:**

| Klasifikasi | Warna | Akses |
| :--- | :--- | :--- |
| Data Publik | Hijau | Dapat diakses oleh publik |
| Data Internal | Kuning | Hanya internal OPD di Pemprov Jabar |
| Data Dikecualikan | Merah | Hanya beberapa OPD tertentu (akses terbatas) |

### Open Data Jabar

Portal transparansi data publik dengan konten yang kaya:

| Konten | Jumlah |
| :--- | ---: |
| Dataset | 2,946+ |
| Visualisasi | 54 |
| Infografik | 40 |
| Artikel Analitik | 12 |

### Satu Peta Jabar

Portal data geospasial dengan **207 dataset** dari **18 organisasi** dan **9 kota/kabupaten**. Termasuk integrasi data eksternal:
- **Waze** — data kepadatan lalu lintas, kecelakaan, jalan berlubang, banjir (realtime)
- **Satgas Citarum** — sensor ketinggian air IoT (update setiap 10-30 menit)

### Dashboard Jabar

**Citizen Dashboard:** 12 Sektor, 32 Sub Sektor (Kesehatan, Kependudukan, Industri, Pendidikan, Ekonomi & Keuangan, Sosial, Kemiskinan, Lingkungan Hidup, Infrastruktur, Pariwisata & Kebudayaan, Pemerintahan & Desa, Masjid Al-Jabar).

**Executive Dashboard:** Kepegawaian & Anggaran, Belanja Dinas, Keuangan Daerah (Pendapatan, Belanja, Pengadaan Barang & Jasa), Kesehatan (Covid-19, Fasyankes, BOR), Product Analytics JDS, Harga Pangan, Indikator Makro.

**3-Tier User Level (Piramida):**

| Level | Pengguna | Fokus | Frekuensi |
| :--- | :--- | :--- | :--- |
| **Strategic** | Gubernur, Wakil Gubernur, Sekda, Asisten Sekda | Policy, Helicopter View | Annual/Quarterly |
| **Tactical** | Kepala Dinas/Badan/Biro, Sekretaris | Procedure, Semi-Operational | Monthly |
| **Operational** | Kepala Bidang/Bagian/UPT, Pejabat Fungsional | Execution, Operational View | Daily/Weekly |

### Jabar Form

Platform formulir untuk pengumpulan data di seluruh Jawa Barat. Menyelesaikan 5 masalah: biaya berlangganan, limitasi export, limitasi submission, limitasi akun, dan verifikasi yang lama. Tersedia gratis untuk seluruh pegawai Pemprov dengan unlimited akun.

---

## 4. Core Data Jabar: Platform Inti

Core Data Jabar adalah platform utama proses Data Management di Pemprov Jawa Barat, menyediakan **12 kapabilitas end-to-end:**

| # | Kapabilitas | Fungsi |
| :-: | :--- | :--- |
| 1 | Data Ingestion Management | Scraping, Collecting, Extracting dari berbagai sumber |
| 2 | Data Pipeline Management | Automate Data Flow antar sistem |
| 3 | Data Exchange Management | Integration & Interoperability (X-Road) |
| 4 | Data Storage Management | Data Lake/Big Data, Data Warehouse, Data Marts |
| 5 | Master Data Management | Pengelolaan data induk terpusat |
| 6 | Reference Data Management | Kode referensi administrasi kewilayahan |
| 7 | Metadata Management | Identitas dan keterangan lengkap setiap dataset |
| 8 | Data Quality Management | 5-dimensi scoring (lihat Bagian 6) |
| 9 | Geospatial Data & MapService | Integrasi data spasial (PostGIS, ArcGIS) |
| 10 | Data Security & Privacy | Keamanan dan kepatuhan privasi data |
| 11 | DataOps Management | Operasionalisasi pipeline dan monitoring |
| 12 | API Management | Distribusi data ke seluruh platform |

### Full Architecture Diagram

```
DATA SOURCES → DATA INGESTION → DISTRIBUTED OBJECT STORAGE (DATA LAKE)
                                        ↓
                              DATA WAREHOUSE → ANALYTICAL DATAMARTS
                                        ↓
                    MASTER DATA / REFERENCE DATA / METADATA REPOSITORY
                                        ↓
                    DATA SCIENCE ALGORITHMS → BI TOOLS
                                        ↓
                              API MANAGEMENT
                                        ↓
            ┌──────────┬──────────┬──────────┬──────────┐
        Satu Data   Satu Peta  Open Data  Dashboard  Aplikasi
         Jabar       Jabar      Jabar      Jabar     Lainnya
```

Data sources meliputi: Spreadsheet/CSV (dari Perangkat Daerah), RDBMS (via API), NoSQL (via API), dan Streaming APIs (social media).

### Data Product Approach (Data Mesh)

Ekosistem Data Jabar menerapkan pendekatan **Data Product** di seluruh **46 OPD** (Organisasi Perangkat Daerah). Setiap OPD bertindak sebagai domain team yang bertanggung jawab atas data produknya, dengan Diskominfo Jabar sebagai hub sentral dan BAPPEDA sebagai konsumer utama untuk perencanaan pembangunan.

Domain OPD meliputi: Perhubungan, Sosial, Pendidikan (DiSDIK), Kesehatan, Kehutanan (DASHUT), Kepegawaian (BKD), Pendapatan (Bapanda), Perdagangan & Perindustrian (INDAG), Keuangan & Aset (BPKAD), Kependudukan (Disdukcapil), dan 36 OPD lainnya.

### R&D: Platform Pertukaran Data (X-Road)

Jabar melakukan R&D untuk platform pertukaran data antar instansi menggunakan arsitektur **X-Road** (referensi e-Estonia). Komponen utama:
- **Trust Services:** Certification Authority, Timestamping, OCSP
- **Central Services:** Configuration Proxy, Central Server, Central Security Server
- **Security Server:** Service Consumer ↔ Security Server ↔ Security Server ↔ Service Provider

### Jenis Dataset yang Dikelola

| Jenis | Contoh |
| :--- | :--- |
| **Data Master/Induk** | Penduduk, Guru, Pegawai, Dokter, Sekolah, Tempat Wisata, Kendaraan |
| **Data Referensi** | Negara, Administrasi Kewilayahan, Kode Pos, Kode Telepon, Perangkat Daerah |
| **Data Transaksi** | Pembayaran Pajak, Perencanaan APBD, Investasi, Sensor Air |
| **Data Agregat** | Jumlah Penduduk, Kasus Covid-19, Produksi Padi |
| **Data Indikator** | IPM, Indeks Desa Membangun, Angka Partisipasi Murni, Laju Pertumbuhan Ekonomi |

---

## 5. Arsitektur Teknologi & Tech Stack

### Application Stack

| Tool | Fungsi | Kategori | Lisensi |
| :--- | :--- | :--- | :--- |
| Apache Airflow | Pipeline, task orchestrator | Data Pipeline | Open-source |
| Apache Spark | Distributed Processing | Distributed Processing | Open-source |
| Apache Kafka | Streaming Data, Event Based Pipeline | Streaming Data | Open-source |
| Airbyte | Pipeline addon for Airflow | Data Pipeline | Open-source |
| Amundsen | Metadata Management | Data Discovery | Open-source |
| Apache OpenWhisk | Serverless Function | Serverless | Open-source |
| Flask & FastAPI | API Services | Backend | Open-source |
| Keycloak | Identity Management | IAM | Open-source |
| KrakenD | API Gateway | API Gateway | Open-source |
| RabbitMQ | Messaging | Message Queue | Open-source |
| Elastic (ELK) | Full-text search | Search | Freemium |
| HashiCorp Vault | Encryption Layer (transport) | Security | Open-source |
| Fider | Portal Request Data | CMS | Open-source |

### Data Storage Layer

| Tool | Fungsi |
| :--- | :--- |
| PostgreSQL | Primary RDBMS |
| CockroachDB | Distributed SQL |
| MongoDB | Document Store |
| Redis | Caching |
| PostGIS | Spatial Database |
| MinIO | Object Data Storage (Data Lake) |

### BI & Visualization

| Tool | Fungsi |
| :--- | :--- |
| Tableau | Enterprise BI |
| Metabase | Self-service BI |
| Apache Superset | Open-source BI |
| ArcGIS (ESRI) | Map Service |

### Infrastructure (On-Premise: Jabarcloud, Bandung)

| Cluster | CPU | RAM | Storage |
| :--- | :--- | :--- | :--- |
| **Production** | 9 × 16core = 144 core | 9 × 32GB = 288GB | 8TB (Ceph shared) |
| **Dev** | 3 × 4core = 48 core | 3 × 32GB = 96GB | Shared |
| **DataLake** | (3×8core) + (1×16core) = 40 core | (3×16GB) + (1×32GB) = 80GB | 4TB native |
| **GeoSpatial** | (3×8core) + (1×16core) = 40 core | (3×16GB) + (1×32GB) = 80GB | 4TB native |

Orchestration: **Kubernetes** dengan Ceph storage, Grafana + Prometheus monitoring, Pritunl VPN, Istio service mesh, GitLab CI/CD.

---

## 6. Data Quality Management Framework

### 6 Prinsip Data Quality Management

1. Memastikan kebutuhan pengguna data terpenuhi dengan standarisasi pengolahan dataset
2. Mendefinisikan standar, persyaratan dan spesifikasi Data Quality Control sebagai bagian dari lifecycle data
3. Mendefinisikan standar proses untuk mengukur, memantau dan melaporkan hasil assessment kualitas data
4. Mentranslasikan kualitas data dalam angka indeks (agregat)
5. Mengidentifikasi dan menyarankan perbaikan data untuk meningkatkan kualitas data
6. Kontrol kualitas data merupakan program berkesinambungan (bukan project)

### 5 Dimensi Kualitas Data

| Dimensi | Bobot | Penjelasan |
| :--- | ---: | :--- |
| **Completeness** | 5% | Kelengkapan setiap unsur dan elemen data |
| **Consistency** | 30% | Penggunaan kesamaan standar penulisan dan kode referensi |
| **Uniqueness** | 25% | Tidak ada duplikasi data dalam satu periode |
| **Conformity & Metadata** | 20% | Sinkronisasi antara metadata dan data aktual |
| **Timeliness** | 20% | Tingkat pemutakhiran dataset |

### Sistem Grading

| Skor | Grade |
| :--- | :--- |
| 0–60 | Kurang |
| 61–80 | Baik |
| 81–100 | Sangat Baik |

### Contoh Assessment Nyata

Dataset "Jumlah Organisasi Kemasyarakatan Berdasarkan Kabupaten/Kota di Jawa Barat":
- Conformity: 100, Uniqueness: 100, Completeness: 100, Consistency: 80, Timeliness: 20
- **Overall Score: 78.00 (BAIK)**

### 4 Aturan Penyusunan Data

1. Judul kolom harus termuat dalam satu baris
2. Gunakan satu tipe data per kolom (numerik, teks, kategori)
3. Pastikan pengisian data berbentuk baris, bukan kolom
4. Pisahkan data mentah dengan data hasil analisis

---

## 7. Program Pemberdayaan Data

### Jawara Data

**Jawara Data** adalah ASN yang ditugaskan oleh Kepala Perangkat Daerah sebagai tim khusus pengelola data dan Agent of Change. Bertugas membantu Walidata Pendukung dalam pengumpulan, pengolahan, analisis, dan visualisasi data.

| Jenis | Jumlah | OPD Tercakup |
| :--- | ---: | ---: |
| Jawara Data Statistik | 138 | 46 OPD |
| Jawara Data Geospasial | 20 | 12 OPD |

Struktur: Dinas/Badan/Biro → Jawara Data → Walidata (Diskominfo Jabar)

### Sekolah PDJ (Pelatihan Data Jabar)

Program pelatihan dengan **4 Kompetensi Dasar:**
1. Perencanaan Data (Data Discovery)
2. Pengumpulan Data (Data Collecting)
3. Pengolahan Data (Data Processing)
4. Diseminasi Data (Data Publish dan Use)

**5 Tahapan Implementasi:**
1. Survey Kapasitas Kompetensi Dasar Jawara Data
2. Penyusunan Kurikulum & Silabus Pelatihan
3. Penyusunan Pre-Test
4. Penyusunan Post-Test
5. Pelatihan Berdasarkan Kompetensi

### Jabar Data Visualization Festival

Kompetisi pemanfaatan data dari Open Data Jabar (tabular) dan Satu Peta Jabar (geospasial) oleh publik (ABCGM: Academia, Business, Community, Government, Media). Tujuan: menghasilkan insight untuk pengambilan keputusan dan perumusan kebijakan publik.

**DataViz Festival 2022:**
- Theme: "Think Globally, Act Locally"
- Total Prize: **Rp 75+ juta**
- Activities: Workshop, Talks & Seminar, Awards, Competition
- Sponsors: Tableau, Iykra, Bank BJB, UGM, BIM, DailySocial, C-Level

---

## 8. Use Cases & Policy Analytics

### Data Analytics Approach

Dua pendekatan:
- **Top Down:** Mulai dari problem question → tentukan data → cari jawaban melalui data
- **Bottom Up:** Mulai dari ketersediaan data → gali informasi → cari insight dari data potensial

**Data Analytics Activity Flow (5 langkah):**
1. Business Understanding — objectives, problem question, success criteria
2. Data Understanding — structure, metadata, quality, ownership
3. Analytical Approach & Methodology — EDA, methodology selection
4. Model Development & Evaluation — prescriptive analytics, optimization
5. Performing Insight & Storytelling — key findings, conclusion, recommendation

### Policy Analytics Ladder

6 level analytics (referensi Policy Lab, ResearchGate):

| Level | Konsep | Tujuan |
| :--- | :--- | :--- |
| Descriptive | Hindsight | Apa yang terjadi? |
| Investigative | Oversight | Dimana masalahnya? |
| Diagnostic | Insight | Mengapa terjadi? |
| Predictive | Foresight | Apa yang akan terjadi? |
| Prescriptive | Outsight | Apa yang harus dilakukan? |
| Optimization | - | Bagaimana mengoptimalkan? |

### Use Case: Penanganan Pandemi Covid-19

Integrasi data dari 8+ sumber: SIMLAB Pikobar, NAR Kemenkes, RS Online Kemenkes, Pelaporan Pikobar, KPCPEN Kemenkes, SIKS-NG Kemensos, Sapawarga, External Data (Facebook, WhatsApp, Google). Output: Satu Data, Open Data, Satu Peta, Integrated Dashboard, Dashboard Tableau.

Analytics yang dilakukan:
- **Angka Reproduksi Efektif (Rt):** Monitoring harian Rt Jawa Barat
- **Google Mobility & Facebook Stayput:** Analisis efektivitas PPKM
- **Vaccination Speed Trend:** Jabar max 437,123 dosis/hari (tertinggi dari 6 provinsi)
- **Quadrant Analysis:** Vaccination coverage vs 7-day growth per Kab/Kota
- **Forecasting Fasilitas Isoman:** ARIMA method untuk prediksi kebutuhan obat/vitamin

### Use Case: Analisa Kebijakan APBD

APBD 2022 (Rp 33.978T) vs APBD 2023 (Rp 33.003T) — selisih -2.87%. Executive Dashboard digunakan rutin untuk keputusan strategis anggaran. Breakdown: 42 Bidang, 38 Perangkat Daerah, 200 Sub Perangkat Daerah.

### Use Case: Arus Lalu Lintas Mudik

Analisis lalu lintas 27 Kab/Kota menggunakan data Waze. Metode: Wilcoxon Sign Rank Test untuk perbandingan pre vs post Lebaran 2022.

### Use Case: Supply Chain Minyak Goreng

Sankey diagram distribusi Produsen → Kab/Kota. Fraud Analysis untuk deteksi penimbunan. Data dari Kementerian Perdagangan + Sapawarga.

### Product Analytics

Dashboard analytics untuk monitoring produk digital JDS:
- **Open Data Jabar:** Unique Session 41,199, Total Visitor 147,177, Conversion Rate 2.84%, Bounce Rate 30.66%
- **Sidebar (Gov Operations):** 246 total users, 67.89% aktif
- **Sapawarga (Minyak Goreng):** 323,586 L minyak goreng dipesan, 175,095 KK

---

## 9. Pencapaian & Penghargaan

| Tahun | Penghargaan | Penyelenggara | Detail |
| :--- | :--- | :--- | :--- |
| 2022 | **idenTIK 2022** | KOMINFO RI | Karya Terpilih IV Public Sector — Open Data Jabar |
| 2022 | **Bhumandala Kanaka** | Badan Informasi Geospasial RI | Simpul Jaringan Terbaik kategori Provinsi (emas) |
| 2023 | **KIJB 2023** | BP2D Jabar | Peringkat II Inovator — Inovasi Open Data Jabar |
| 2022 | **ISO 20000-1:2018** | TÜV NORD Indonesia | Sertifikat Sistem Manajemen Layanan pada Hotline Ekosistem Data Jabar |

**Sertifikat ISO 20000-1:2018** mencakup layanan: Satu Data Jabar, Open Data Jabar, Satu Peta Jabar, Dashboard Jabar.

**Legalitas:**
- KepGub Jabar No. 049.05/Kep.734-Diskominfo/2020 — Tim Satu Peta dan Satu Data Daerah
- Surat Pencatatan Ciptaan (HAKI) — Aplikasi Satu Data Jawa Barat (Program Komputer)

**Interoperabilitas:** Seluruh Kabupaten dan Kota di Jawa Barat sudah terintegrasi dan replikasi dengan Portal Data Jabar. Contoh: Kab. Bogor (618 datasets), Kab. Bekasi (477 datasets), Kab. Bandung (246 datasets).

---

## 10. Landasan Hukum

10 regulasi yang menjadi landasan hukum tata kelola data Ekosistem Data Jabar:

| # | Regulasi | Tentang |
| :-: | :--- | :--- |
| 1 | UU No. 11/2008 | Informasi Dan Transaksi Elektronik |
| 2 | UU No. 14/2008 | Keterbukaan Informasi Publik |
| 3 | PP No. 82/2012 | Penyelenggaraan Sistem dan Transaksi Elektronik |
| 4 | **Perda Jabar No. 24/2012** | Satu Data Pembangunan Jawa Barat |
| 5 | **Pergub Jabar No. 80/2015** | Petunjuk Pelaksanaan Perda No. 24/2012 |
| 6 | Permenkominfo No. 4/2016 | Sistem Manajemen Pengamanan Informasi |
| 7 | Perpres No. 95/2018 | Sistem Pemerintahan Berbasis Elektronik (SPBE) |
| 8 | Permendagri No. 70/2019 | Sistem Informasi Pemerintahan Daerah |
| 9 | Peraturan BSSN No. 10/2019 | Pelaksanaan Persandian Untuk Pengamanan Informasi |
| 10 | Perpres No. 39/2019 | Satu Data Indonesia |

Regulasi #4 dan #5 (bold) adalah regulasi spesifik Jawa Barat yang mendahului regulasi nasional Satu Data Indonesia (2019), menunjukkan bahwa Jabar adalah pionir dalam tata kelola data daerah.

---

## 11. DAMA Knowledge Areas Applied

Ekosistem Data Jabar menerapkan **10 dari 11 knowledge area DAMA-DMBOK** secara komprehensif, masing-masing didokumentasikan dalam context diagram (Inputs → Activities → Deliverables):

| Knowledge Area | Penerapan di Jabar |
| :--- | :--- |
| Data Architecture | Core Data Jabar architecture, 12 capabilities |
| Data Modeling & Design | Conceptual/Logical/Physical models untuk 46 OPD |
| Data Storage & Operations | PostgreSQL, CockroachDB, MongoDB, MinIO, Ceph |
| Data Security | Keycloak IAM, HashiCorp Vault encryption, klasifikasi 3-tier |
| Data Integration & Interoperability | X-Road, Airflow pipelines, API Gateway (KrakenD) |
| Document & Content Management | Portal CMS, Jabar Form, content lifecycle |
| Reference & Master Data | Kode referensi kewilayahan (BPS + Kemendagri), data master 5 jenis |
| Data Warehousing & BI | Data Lake → DW → Data Marts → Tableau/Metabase/Superset |
| Metadata Management | Amundsen, metadata repository, data lineage |
| Data Quality Management | 5-dimensi scoring, weighted assessment, continuous program |

---

## 12. Selling Points vs Competitors

Saat pitching ke calon klien, highlight diferensiasi berikut:

**1. Integrated, Not Isolated.** Bukan portal standalone (CKAN/DKAN) — ini adalah ekosistem terintegrasi 7 komponen yang mencakup seluruh data value chain, dari collection (Jabar Form) hingga executive insight (Executive Dashboard).

**2. Proven at Scale.** 46 OPD terintegrasi, 2,946+ dataset, 207 dataset geospasial, 138 Jawara Data. Bukan solusi teoritis — ini sistem live yang sudah berjalan sejak 2019.

**3. Award-Winning & Certified.** idenTIK 2022 (KOMINFO), Bhumandala Kanaka 2022 (BIG), KIJB 2023 (BP2D Jabar), ISO 20000-1:2018 (TÜV NORD).

**4. Battle-Tested.** Terbukti dalam penanganan Covid-19 — integrasi 8+ sumber data, analytics real-time, mendukung keputusan kebijakan PPKM dan vaksinasi.

**5. Full-Stack Capability.** Bukan hanya advisory — IDEAS membangun platform end-to-end dengan tech stack enterprise-grade (Kubernetes, Spark, Kafka, Airflow) di infrastruktur on-premise pemerintah.

**6. Data Culture Builder.** Program Jawara Data (138 agents of change), Sekolah PDJ (pelatihan 4 kompetensi), DataViz Festival (kompetisi publik Rp 75M+) — bukan hanya teknologi, tapi membangun budaya data.

**7. Regulatory Pioneer.** Jabar memiliki Perda Satu Data sejak 2012 — 7 tahun sebelum Perpres Satu Data Indonesia (2019). IDEAS memahami regulasi dari hulu ke hilir.

---

**Related Documents:**
- Untuk detail produk IDEAS, lihat `products-catalog.md`
- Untuk framework thought leadership, lihat `thought-leadership-frameworks.md`
- Untuk case study ringkas, lihat `case-studies.md` (Bagian 1)
- Untuk regulasi nasional, lihat `regulatory-standards.md`
