# IDEAS Data Ecosystem Platform: Products Catalog

*Last Updated: February 2026*

## 1. Platform Architecture

Platform Ekosistem Data IDEAS adalah solusi *end-to-end* yang terdiri dari tiga lapisan arsitektur utama, yang menaungi **delapan produk inti** yang didukung oleh **Core Data Engine** dengan 13 modul terintegrasi. Arsitektur ini dirancang untuk membangun fondasi pengelolaan data yang kuat, menjembatani kolaborasi antar sistem, hingga menghadirkan transparansi bagi publik dan pimpinan. Seluruh platform mendukung paradigma **Data Mesh** (domain-oriented, decentralized data ownership) dan **Data Fabric** (automated, metadata-driven data integration) secara hybrid untuk memaksimalkan kelincahan dan tata kelola.

| Lapisan Arsitektur | Fokus | Produk Terkait | Relevansi Service |
| :--- | :--- | :--- | :--- |
| **1. Core Engine** | Fondasi pertukaran dan pemrosesan data | IDEAS Data Engine (13 modul) | S2.1, S2.2, S2.4, S2.5 |
| **2. Internal Operations** | Jembatan data untuk kolaborasi lintas tim dan sistem | IDEAS DataSpace, IDEAS Data Hub, IDEAS Collect, IDEAS Control Center | S2.2, S2.4, S2.5, S3.1 |
| **3. Public & Leadership** | Platform transparansi untuk publik dan pimpinan | IDEAS Civic Insight, IDEAS MapEdge, IDEAS Executive | S2.3, S2.6, S1.1 |

### 1.1 Keunggulan Teknologi Tertanam

Seluruh produk IDEAS memiliki keunggulan teknologi berikut yang tertanam secara konsisten:

| Keunggulan | Deskripsi | Produk yang Menerapkan |
| :--- | :--- | :--- |
| **GenAI-Powered** | LLM-driven narrative generation, AI-powered profiling, NLP untuk formulir cerdas, agentic AI workflows. | Collect, DataSpace, Executive, Data Engine |
| **Zero-Trust Security** | Arsitektur keamanan Zero-Trust untuk pertukaran data antar organisasi, memastikan setiap permintaan diautentikasi dan diotorisasi. | Data Engine (Secure Data Exchange) |
| **Privacy-by-Design** | Manajemen privasi data, DPIA, DSAR compliance sesuai UU PDP (UU 27/2022) [1]. | Data Engine (Data Privacy Governance Hub) |
| **Real-time Monitoring** | Dashboard monitoring operasional secara real-time dengan deteksi anomali berbasis AI. | Control Center, Executive |
| **Data Mesh-Ready** | Mendukung kepemilikan data berorientasi domain, platform data swalayan, dan tata kelola terfederasi. | Data Hub, DataSpace, Data Engine |
| **Data Contract Support** | Dukungan kontrak data yang sesuai dengan standar Open Data Contract Standard (ODCS) untuk interoperabilitas. | Data Hub, Data Engine |
| **Responsible AI** | Tata kelola model AI, deteksi bias, explainability (XAI), dan jejak audit untuk memastikan penggunaan AI yang adil dan transparan. | Data Engine (Data Governance Platform Engine) |

### 1.2 Competitive Positioning

IDEAS Platform memiliki positioning unik sebagai **satu-satunya platform ekosistem data Indonesia** yang menggabungkan advisory dan implementasi. Berikut perbandingan dengan platform global:

| Aspek | IDEAS Platform | Collibra | Atlan | Alation |
| :--- | :--- | :--- | :--- | :--- |
| **Fokus Utama** | End-to-end data ecosystem (governance + implementation + empowerment) | Enterprise data governance & catalog | Active metadata management & collaboration | AI-powered data discovery & catalog |
| **Deployment** | On-premise, hybrid cloud, SaaS | Cloud-native SaaS | Cloud-native SaaS | Cloud-native SaaS |
| **Advisory Integration** | Terintegrasi (DAMA-aligned advisory + platform) | Terpisah (partner ecosystem) | Terpisah | Terpisah |
| **Regulatory Compliance** | UU PDP, SPBE, Satu Data Indonesia, Perpres 46/2025 [2] | GDPR, CCPA, SOX | GDPR, SOC 2 | GDPR, SOC 2 |
| **Bahasa Indonesia** | Native support | Tidak | Tidak | Tidak |
| **Geospatial** | Terintegrasi (MapEdge) | Tidak | Tidak | Tidak |
| **Open Data / Civic** | Terintegrasi (Civic Insight) | Tidak | Tidak | Tidak |
| **Pricing Model** | Modular per modul, value-based, berbasis langganan | Enterprise license | Per-seat subscription | Enterprise license |

---

## 2. Core Engine: IDEAS Data Engine

Core platform yang menjadi fondasi seluruh ekosistem produk IDEAS. Menggabungkan platform dengan advisory support untuk solusi yang selaras dengan strategi, konteks, dan kebutuhan nyata. IDEAS Data Engine mendukung arsitektur **Data Fabric** dengan automated metadata-driven integration dan **Data Mesh** dengan federated computational governance. Engine ini juga mengintegrasikan kerangka kerja valuasi data untuk mengukur nilai aset data.

### 2.1 Thirteen Integrated Modules

| No | Modul | Fungsi | GenAI/AI Capabilities | DAMA KA Alignment |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Data Connector Modules** | Konektor ke berbagai sumber data (database, API, file, streaming) | Auto-discovery of data sources, intelligent schema mapping | KA-08 (Data Integration) |
| 2 | **Data Orchestration Hub** | Orkestrasi pipeline data dan workflow automation | AI-optimized pipeline scheduling, anomaly-triggered re-runs | KA-08 (Data Integration) |
| 3 | **Data Tables Engine** | Mesin pengelolaan tabel data terstruktur | Auto-indexing, intelligent partitioning recommendations | KA-06 (Data Storage) |
| 4 | **Data Quality Platform Engine** | Profiling otomatis, validasi aturan kualitas, scoring, dan monitoring | AI-powered anomaly detection, auto-generated DQ rules, predictive quality scoring | KA-11 (Data Quality) |
| 5 | **Metadata Platform Engine** | Katalog metadata, lineage tracking, dan discovery | LLM-powered semantic search, automated metadata enrichment, active metadata | KA-09 (Document & Content), KA-12 (Metadata) |
| 6 | **Master & Reference Data Platform Engine** | Pengelolaan master data dan data referensi terpusat | AI-assisted entity resolution, fuzzy matching, golden record creation | KA-10 (Reference & Master Data) |
| 7 | **Data Analytics Platform Engine** | Mesin analitik untuk pemrosesan dan transformasi data | Natural language querying (NLQ), AI-generated insights, automated visualization | KA-07 (Data Warehousing & BI) |
| 8 | **Data Streams (Unstructured Data) Engine** | Pemrosesan data tidak terstruktur (dokumen, gambar, teks) | Document AI (OCR + NLP), image classification, text extraction | KA-09 (Document & Content) |
| 9 | **Data Governance Platform Engine** | Enforcement kebijakan, kontrol akses, audit trail, dan AI governance. Mendukung DMBOK 3.0 [3]. | Automated policy enforcement, AI model registry, responsible AI monitoring | KA-01 (Data Governance) |
| 10 | **Geospatial Intelligence Engine** | Analisis data berbasis lokasi dan pemetaan | Spatial AI for pattern detection, geospatial anomaly detection | KA-07 (Data Warehousing & BI) |
| 11 | **Secure Data Exchange Platform Engine** | Pertukaran data antar organisasi dengan keamanan Zero-Trust | Encrypted data sharing, consent management, blockchain-ready audit trail | KA-04 (Data Security) |
| 12 | **Data Privacy Governance Hub** | Manajemen privasi data, DPIA, dan DSAR compliance | AI-powered PII detection, automated DPIA generation, consent lifecycle management | KA-04 (Data Security) |
| 13 | **Global Data Search Engine** | Pencarian data terpadu lintas seluruh ekosistem | LLM-powered semantic search, natural language data discovery, federated search | KA-12 (Metadata) |

### 2.2 Data Valuation Integration

IDEAS Data Engine mengintegrasikan kerangka kerja valuasi aset data berdasarkan **Deloitte 2025 Data Valuation Framework** [4]. Ini memungkinkan organisasi untuk mengukur nilai ekonomi dari data mereka menggunakan pendekatan standar industri.

- **Income Approach**: Menilai data berdasarkan pendapatan yang dihasilkannya (misalnya, melalui Multi-period Excess Earnings atau Relief-from-Royalty).
- **Cost Approach**: Menilai data berdasarkan biaya untuk mereproduksi atau menggantinya (Reproduction vs. Replacement Cost).
- **Market Approach**: Menilai data berdasarkan transaksi yang sebanding di pasar.

Integrasi ini juga memperkenalkan konsep **Data Debt**, yaitu biaya siklus hidup, masalah kualitas, dan risiko kepatuhan yang terkait dengan aset data, memungkinkan perhitungan **Data Debt Leverage Ratio** (Data Value / Data Debt) untuk pengambilan keputusan strategis.

### 2.3 Data Engine Use Cases

| Use Case | Modul Utama | Sektor Target | Contoh Implementasi | Mini Case Study |
| :--- | :--- | :--- | :--- | :--- |
| **Data Governance Foundation** | Governance Platform, Metadata Platform | Pemerintah, BUMN | Pembangunan kebijakan data terpusat dengan audit trail untuk kepatuhan SPBE. | **Kementerian X**: Membangun fondasi SPBE dengan tata kelola data terpusat, meningkatkan Indeks SPBE dari 2.5 menjadi 3.8 dalam 18 bulan, menghasilkan efisiensi Rp 15 Miliar dari konsolidasi sistem. |
| **Data Quality Improvement** | DQ Platform, Data Tables | Keuangan, Kesehatan | Automated profiling dan scoring untuk data nasabah/pasien. | **Bank Y**: Mengurangi kesalahan data nasabah sebesar 70% melalui DQ automation, mempercepat proses KYC dari 3 hari menjadi 4 jam dan mengurangi risiko fraud sebesar 25%. |
| **Master Data Management** | MDM Platform, Data Connector | Pemerintah, Retail | Golden record creation untuk data penduduk/pelanggan lintas sistem. | **Provinsi Z**: Menciptakan "Satu Data Kependudukan" dengan golden record dari 3 dinas berbeda, meningkatkan akurasi penyaluran bantuan sosial sebesar 40% dan menghemat anggaran Rp 200 Miliar. |
| **Data Integration & Pipeline** | Orchestration Hub, Data Connector | Semua sektor | ETL/ELT pipeline automation untuk konsolidasi data multi-sumber. | **Perusahaan Ritel A**: Mengkonsolidasikan data penjualan dari 5 sistem berbeda ke dalam satu data warehouse, memungkinkan analisis 360 derajat perilaku pelanggan dan meningkatkan cross-selling sebesar 15%. |
| **Privacy Compliance (UU PDP)** | Privacy Hub, Governance Platform | Keuangan, Telko | Kepatuhan UU PDP dengan otomatisasi DPIA dan manajemen DSAR. | **Operator Telko B**: Mengotomatisasi 80% proses pemenuhan Hak Subjek Data (DSAR), memenuhi tenggat waktu UU PDP dan meningkatkan kepercayaan pelanggan, menghindari potensi denda hingga 2% dari pendapatan tahunan. |
| **AI Governance** | Governance Platform, Analytics Platform | Teknologi, Keuangan | AI model registry, monitoring bias, dan pelaporan explainability. | **Fintech C**: Menerapkan AI model registry untuk melacak 50+ model machine learning, memastikan auditabilitas dan kepatuhan terhadap regulasi OJK, mengurangi risiko model sebesar 30%. |

---

## 3. Internal Operations Products

### 3.1 IDEAS Collect

Platform pengumpulan data terintegrasi dengan NLP untuk formulir cerdas, dirancang untuk menyederhanakan dan mengotomatisasi proses akuisisi data dari berbagai sumber.

| Aspek | Detail |
| :--- | :--- |
| **Fungsi Utama** | Multi-channel data collection dengan intelligent form generation dan validasi real-time. |
| **Fitur Utama** | NLP-powered smart forms, multi-channel collection (web, mobile, API), validation rules engine, offline capability, auto-classification. |
| **GenAI Capabilities** | Natural language form generation, auto-validation rule suggestion, intelligent field mapping. |
| **Sektor Target** | Pemerintah (sensus, survei), Kesehatan (data pasien), Pendidikan (data siswa). |
| **Relevansi Service** | S2.2, S2.4 (Lihat [services-catalog.md](services-catalog.md)) |
| **DAMA KA** | KA-08 (Data Integration), KA-11 (Data Quality) |
| **Regulatory Compliance** | UU PDP (consent management), Satu Data Indonesia (standardized collection). |
| **Mini Case Study** | **BPS**: Digitalisasi survei ekonomi nasional menggunakan formulir cerdas, mengurangi waktu entri data sebesar 60% dan meningkatkan akurasi data awal hingga 98%, mempercepat rilis data PDB. |

### 3.2 IDEAS Data Hub

Hub data terpusat untuk integrasi, transformasi, dan manajemen data, berfungsi sebagai inti dari arsitektur Data Mesh.

| Aspek | Detail |
| :--- | :--- |
| **Fungsi Utama** | Centralized data integration hub dengan dukungan domain Data Mesh untuk data product management. |
| **Fitur Utama** | ETL/ELT pipelines, data catalog, lineage tracking, API management, data contract enforcement, domain-oriented data products. |
| **GenAI Capabilities** | AI-assisted pipeline generation, natural language data transformation, automated lineage documentation. |
| **Sektor Target** | Pemerintah (integrasi data lintas OPD), BUMN (konsolidasi data anak perusahaan). |
| **Relevansi Service** | S2.2, S2.4 (Lihat [services-catalog.md](services-catalog.md)) |
| **DAMA KA** | KA-08 (Data Integration), KA-12 (Metadata) |
| **Data Mesh Support** | Domain-oriented data products, self-serve data platform, ODCS-compliant data contracts. |
| **Mini Case Study** | **BUMN Karya**: Mengintegrasikan data proyek dari 5 anak perusahaan ke dalam satu Data Hub, memberikan visibilitas 360 derajat terhadap progres dan risiko proyek strategis nasional, mengurangi keterlambatan proyek sebesar 20%. |

### 3.3 IDEAS DataSpace

Ruang kerja data kolaboratif dengan AI untuk profiling otomatis, memungkinkan data steward dan analis untuk berkolaborasi dalam meningkatkan kualitas data.

| Aspek | Detail |
| :--- | :--- |
| **Fungsi Utama** | Collaborative data workspace untuk data stewards dan analysts dengan fitur data preparation dan quality. |
| **Fitur Utama** | Collaborative workspace, AI-powered profiling, quality rule recommendations, data preparation, version control, annotation. |
| **GenAI Capabilities** | AI-powered data profiling, automated quality rule generation, natural language data exploration, AI-assisted data preparation. |
| **Sektor Target** | Semua sektor (tim data stewardship). |
| **Relevansi Service** | S2.2, S2.5 (Lihat [services-catalog.md](services-catalog.md)) |
| **DAMA KA** | KA-11 (Data Quality), KA-12 (Metadata) |
| **Mini Case Study** | **Dinas Kesehatan**: Tim data steward menggunakan DataSpace untuk membersihkan dan mempersiapkan data dari 500+ puskesmas, menghasilkan dataset yang valid untuk analisis wabah penyakit, mempercepat waktu respons dari 7 hari menjadi 1 hari. |

### 3.4 IDEAS Control Center

Pusat kendali dan monitoring data operations untuk memastikan keandalan, performa, dan kepatuhan seluruh alur kerja data.

| Aspek | Detail |
| :--- | :--- |
| **Fungsi Utama** | Centralized operations monitoring, data observability, dan incident management. |
| **Fitur Utama** | Real-time monitoring, SLA tracking, incident management, governance dashboard, data observability, alert management. |
| **GenAI Capabilities** | AI-powered anomaly detection, predictive incident alerting, automated root cause analysis. |
| **Sektor Target** | Pemerintah (monitoring SPBE), BUMN (operations center). |
| **Relevansi Service** | S2.2, S3.1 (Lihat [services-catalog.md](services-catalog.md)) |
| **DAMA KA** | KA-01 (Data Governance), KA-06 (Data Storage) |
| **Data Observability** | End-to-end pipeline monitoring, data freshness tracking, schema change detection (sebanding dengan Monte Carlo). |
| **Mini Case Study** | **Pemprov Jabar**: Memonitor lebih dari 100 pipeline data SPBE secara real-time, memungkinkan deteksi anomali dan insiden dalam hitungan menit, bukan hari, meningkatkan uptime layanan digital hingga 99.9%. |

---

## 4. Public & Leadership Products

### 4.1 IDEAS Executive

Dashboard eksekutif dengan AI-generated narrative insights dalam bahasa alami, menyajikan informasi kompleks menjadi ringkasan yang mudah dipahami.

| Aspek | Detail |
| :--- | :--- |
| **Fungsi Utama** | Executive decision support dengan GenAI narrative generation dan analisis prediktif. |
| **Fitur Utama** | AI narrative generation (Bahasa Indonesia), KPI tracking, trend analysis, executive briefing automation, what-if scenario modeling. |
| **GenAI Capabilities** | LLM-powered narrative generation dalam Bahasa Indonesia, automated executive briefing, natural language querying, agentic AI for automated report generation. |
| **Sektor Target** | Pemerintah (Kepala Daerah, Sekda), BUMN (Direksi, Komisaris). |
| **Relevansi Service** | S2.6, S1.1 (Lihat [services-catalog.md](services-catalog.md)) |
| **DAMA KA** | KA-07 (Data Warehousing & BI) |
| **Mini Case Study** | **Gubernur Provinsi X**: Menerima ringkasan naratif otomatis setiap pagi tentang status inflasi, kemiskinan, dan serapan anggaran, memungkinkan pengambilan keputusan yang 50% lebih cepat dan berbasis data. |

### 4.2 IDEAS Civic Insight

Portal data terbuka dan analitik layanan publik untuk mendorong transparansi, akuntabilitas, dan partisipasi masyarakat.

| Aspek | Detail |
| :--- | :--- |
| **Fungsi Utama** | Open data portal, public service analytics, dan platform keterbukaan informasi publik. |
| **Fitur Utama** | Open data portal, citizen dashboard, public service analytics, transparency reporting, civic engagement tools. |
| **GenAI Capabilities** | AI-powered public sentiment analysis dari media sosial, automated transparency report generation. |
| **Sektor Target** | Pemerintah Daerah, Kementerian/Lembaga. |
| **Relevansi Service** | S2.3, S2.6 (Lihat [services-catalog.md](services-catalog.md)) |
| **DAMA KA** | KA-07 (Data Warehousing & BI), KA-13 (Data Ethics) |
| **Regulatory Compliance** | SPBE (Indeks SPBE), Satu Data Indonesia, Keterbukaan Informasi Publik (UU 14/2008). |
| **Mini Case Study** | **Kota Y**: Meluncurkan portal data terbuka yang dikunjungi 10.000+ warga per bulan, meningkatkan Indeks SPBE di domain layanan publik sebesar 0.5 poin dan memungkinkan partisipasi publik dalam musrenbang. |

### 4.3 IDEAS MapEdge

Platform geospasial untuk analisis data berbasis lokasi, mengubah data spasial menjadi wawasan strategis.

| Aspek | Detail |
| :--- | :--- |
| **Fungsi Utama** | Location intelligence dan geospatial analytics untuk perencanaan dan operasi. |
| **Fitur Utama** | Spatial analysis, map visualization, geospatial data integration, location intelligence, multi-layer overlay, thematic mapping. |
| **GenAI Capabilities** | Spatial AI for pattern detection, geospatial anomaly detection, natural language geospatial querying (e.g., "tunjukkan semua sekolah di area rawan banjir"). |
| **Sektor Target** | Pemerintah (perencanaan tata ruang), Agrikultur (analisis lahan), Logistik (optimasi rute). |
| **Relevansi Service** | S2.3, S2.6 (Lihat [services-catalog.md](services-catalog.md)) |
| **DAMA KA** | KA-07 (Data Warehousing & BI) |
| **Regulatory Compliance** | Kebijakan Satu Peta (Perpres 23/2021). |
| **Mini Case Study** | **Dinas Pertanian**: Menganalisis data citra satelit untuk memetakan potensi kekeringan, memungkinkan intervensi dini dan mitigasi gagal panen bagi 5.000+ petani, menyelamatkan potensi kerugian Rp 50 Miliar. |

---

## 5. Pricing Model

Model harga IDEAS dirancang untuk fleksibilitas dan penciptaan nilai, menawarkan beberapa opsi yang dapat disesuaikan dengan kebutuhan dan skala klien.

- **Modular Licensing**: Klien dapat memilih modul spesifik dari IDEAS Data Engine atau produk individual, membayar hanya untuk fungsionalitas yang mereka butuhkan. Ini memungkinkan adopsi bertahap dan skalabilitas.
- **Value-Based Subscription**: Harga didasarkan pada nilai yang diciptakan, seperti jumlah data yang dikelola, jumlah pengguna, atau metrik dampak bisnis yang disepakati. Model ini menyelaraskan investasi dengan hasil.
- **Enterprise Package**: Paket komprehensif yang mencakup seluruh platform dengan dukungan penuh, dirancang untuk transformasi data skala besar di tingkat enterprise.

Untuk detail lebih lanjut tentang estimasi biaya dan komposisi tim, silakan merujuk ke dokumen [human-resources-and-pricing.md](./human-resources-and-pricing.md) dan [task-decomposition.md](./task-decomposition.md).

## 6. Glossary

- **DAMA-DMBOK**: Data Management Body of Knowledge dari DAMA International.
- **DSAR**: Data Subject Access Request, permintaan dari individu untuk mengakses data pribadi mereka.
- **DPIA**: Data Protection Impact Assessment, proses untuk mengidentifikasi dan meminimalkan risiko perlindungan data.
- **GenAI**: Generative Artificial Intelligence, AI yang mampu menghasilkan konten baru.
- **LLM**: Large Language Model, model AI besar yang dilatih pada data teks masif.
- **ODCS**: Open Data Contract Standard, standar terbuka untuk kontrak data.
- **SPBE**: Sistem Pemerintahan Berbasis Elektronik.
- **UU PDP**: Undang-Undang Pelindungan Data Pribadi (UU No. 27 Tahun 2022).

## 7. References

[1] Undang-Undang No. 27 Tahun 2022 tentang Pelindungan Data Pribadi.
[2] Peraturan Presiden No. 46 Tahun 2025 tentang Perubahan Kedua atas Perpres 16/2018 tentang Pengadaan Barang/Jasa Pemerintah.
[3] DAMA International, "DAMA-DMBOK3 Project," diakses Februari 2026.
[4] Deloitte, "Data Valuation: A practical guide to measuring the value of data," 2025.


## Cross-Skill Integration

- **`web-scraper`**: Support product development with automated data collection — use `domain_crawler.py` for market research, `page_scraper.py` for feature benchmarking against competitor products, and `data_pipeline.py` for processing collected data into product analytics.
- **`dama-research`**: Ground product design in DAMA-DMBOK best practices — KA-02 for data architecture patterns, KA-06 for integration standards, KA-08 for BI/analytics features, and KA-11 for built-in data quality capabilities. See `dama-research/knowledge-areas/` for detailed frameworks.
