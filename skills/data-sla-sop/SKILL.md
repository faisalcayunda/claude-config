---
name: data-sla-sop
description: >
  Membuat Panduan Lengkap SLA & SOP Data yang menggabungkan Service Level Agreement (SLA) dan Standard Operating Procedure (SOP) ke dalam satu dokumen terintegrasi, selalu berkaitan dengan pengelolaan data. Trigger skill ini setiap kali pengguna menyebut: SLA data, SOP data, panduan SLA SOP, service level agreement data, prosedur operasional data, data pipeline SLA, data quality SLA, data governance SOP, onboarding data SOP, ingestion SOP, data warehouse SLA, data catalog SLA, data incident SOP, panduan operasional data, atau membutuhkan dokumen gabungan SLA dan SOP untuk sistem/proses data apapun — baik pemerintahan (SPBE/Satu Data Indonesia), enterprise, maupun fintech. Trigger juga untuk SLA antar tim data, kontrak layanan data platform, SOP penanganan insiden data, SOP quality gate, SOP pipeline, dan SOP master data management.
---
 
# Skill: Data SLA & SOP — Panduan Lengkap Terintegrasi
 
Skill ini menghasilkan **Panduan Lengkap SLA & SOP Data** — satu dokumen terpadu yang menggabungkan Service Level Agreement (SLA) dan Standard Operating Procedure (SOP) untuk konteks pengelolaan data. Dokumen ini dirancang agar dapat langsung digunakan oleh tim data, data governance officer, product owner platform data, atau project manager — baik di lingkungan pemerintahan, enterprise, maupun startup fintech.
 
---
 
## Prinsip Dasar
 
SLA mendefinisikan **apa yang dijanjikan** (target, metrik, konsekuensi), sementara SOP mendefinisikan **bagaimana melakukannya** (langkah, penanggung jawab, alur kerja). Keduanya saling melengkapi dan wajib hadir bersama agar operasional data berjalan akuntabel. Panduan Lengkap menggabungkan keduanya sehingga pembaca tidak perlu berpindah dokumen.
 
---
 
## Cara Menggunakan Skill Ini
 
### Langkah 1 — Kumpulkan Konteks
 
Sebelum menulis, tanyakan atau inferensikan dari percakapan:
 
| Dimensi | Contoh Nilai |
|---|---|
| **Nama layanan/proses data** | Data Pipeline Ingestion, Data Catalog, Master Data Management, Data Warehouse, Data Quality Gate |
| **Domain organisasi** | Pemerintahan (SPBE), perbankan (OJK/SNAP), fintech syariah, enterprise retail |
| **Pihak penyedia (provider)** | Tim Data Engineering, Platform Data, BPS, BUMN |
| **Pihak penerima (consumer)** | Tim Analis, Aplikasi hilir, Dinas/Satker, Regulator |
| **Cakupan SLA** | Ketersediaan, latensi, freshness, akurasi, completeness |
| **Regulasi relevan** | Perpres 95/2018 (SPBE), UU PDP, PMK, OJK, ISO 8000, DAMA-DMBOK2 |
| **Format output** | DOCX siap cetak, Markdown, atau keduanya |
 
Jika pengguna tidak memberikan semua informasi ini, **gunakan asumsi yang masuk akal** dan tampilkan di bagian *Asumsi Dokumen* di awal output.
 
---
 
### Langkah 2 — Bangun Panduan Lengkap
 
Gunakan struktur di bawah ini **secara penuh**. Jangan menghilangkan bagian kecuali pengguna secara eksplisit memintanya.
 
---
 
## Struktur Dokumen Panduan Lengkap SLA & SOP Data
 
### HALAMAN DEPAN
 
```
PANDUAN LENGKAP
SERVICE LEVEL AGREEMENT (SLA) & STANDARD OPERATING PROCEDURE (SOP)
[NAMA LAYANAN / PROSES DATA]
 
Versi       : [X.Y]
Tanggal     : [DD Bulan YYYY]
Penyusun    : [Nama Tim / Unit]
Berlaku Untuk: [Nama Organisasi]
Status      : [Draft / Final / Aktif]
```
 
---
 
### BAB 1 — PENDAHULUAN
 
**1.1 Latar Belakang**
Jelaskan mengapa SLA dan SOP ini diperlukan. Sertakan konteks bisnis/regulasi yang relevan.
 
**1.2 Tujuan Dokumen**
- Menetapkan komitmen layanan data yang terukur
- Menyediakan prosedur operasional yang jelas dan dapat diaudit
- Menjadi acuan penyelesaian insiden dan eskalasi
**1.3 Ruang Lingkup**
Batas cakupan: layanan apa, proses apa, data apa, sistem apa.
 
**1.4 Definisi dan Singkatan**
Tabel istilah kunci:
 
| Istilah | Definisi |
|---|---|
| SLA | Service Level Agreement — komitmen tingkat layanan terukur |
| SOP | Standard Operating Procedure — prosedur standar operasional |
| RTO | Recovery Time Objective — target waktu pemulihan |
| RPO | Recovery Point Objective — target titik pemulihan data |
| Freshness | Kemutakhiran data (jarak antara waktu source dan waktu tersedia di target) |
| Data Quality Score | Skor kualitas data berdasarkan dimensi yang disepakati |
 
**1.5 Dokumen Terkait**
Referensi ke kebijakan, arsitektur, atau kontrak yang berlaku.
 
---
 
### BAB 2 — SERVICE LEVEL AGREEMENT (SLA)
 
**2.1 Pihak yang Terlibat**
- **Provider**: [nama tim/unit yang memberikan layanan data]
- **Consumer**: [nama tim/unit/aplikasi yang menggunakan data]
- **Governance Owner**: [PIC kebijakan, biasanya Data Governance Officer]
**2.2 Periode Berlaku & Review**
Tanggal mulai, tanggal berakhir, jadwal review berkala (contoh: tiap 6 bulan).
 
**2.3 Metrik SLA dan Target**
 
Sesuaikan tabel berikut dengan konteks layanan:
 
| Metrik | Definisi | Target | Metode Pengukuran | Periode |
|---|---|---|---|---|
| Ketersediaan (Availability) | % waktu layanan aktif | ≥ 99,5% | Monitoring tool / Uptime probe | Bulanan |
| Freshness / Keterlambatan | Jarak waktu antara source dan konsumsi | ≤ 15 menit | Timestamp audit log | Per batch/run |
| Completeness | % record yang berhasil diproses vs. expected | ≥ 99% | Row count validation | Per pipeline run |
| Akurasi Data | % record memenuhi aturan validasi bisnis | ≥ 98% | Data quality rule engine | Harian |
| Latensi Query | Waktu response query standar | ≤ 5 detik (p95) | APM / query log | Harian |
| RTO | Waktu pemulihan pasca insiden | ≤ 4 jam | Incident log | Per insiden |
| RPO | Maksimum kehilangan data saat failure | ≤ 1 jam | Backup/log audit | Per insiden |
 
> **Catatan**: Sesuaikan metrik dan angka target dengan kondisi aktual sistem.
 
**2.4 Pengecualian SLA**
Kondisi di mana SLA tidak berlaku: maintenance terjadwal, force majeure, kegagalan di luar sistem provider.
 
**2.5 Pelaporan SLA**
Format laporan, frekuensi, dan penerima laporan (contoh: dashboard mingguan + laporan bulanan PDF).
 
**2.6 Penalti dan Eskalasi**
Konsekuensi jika target tidak terpenuhi:
 
| Tingkat Breach | Kondisi | Tindakan |
|---|---|---|
| Warning | SLA turun < 2% dari target selama 3 hari | Notifikasi ke consumer + root cause analysis |
| Critical | SLA turun ≥ 5% dari target | Eskalasi ke manajer + action plan 24 jam |
| Breach | SLA tidak terpenuhi selama 1 siklus penuh | Review kontrak, kompensasi, atau rencana perbaikan formal |
 
**2.7 Mekanisme Review dan Amandemen**
Prosedur perubahan SLA: siapa yang mengajukan, proses persetujuan, dokumentasi perubahan.
 
---
 
### BAB 3 — STANDARD OPERATING PROCEDURE (SOP)
 
Setiap SOP dalam bab ini mengikuti format standar:
 
```
SOP-[KODE]: [NAMA PROSEDUR]
Versi      : X.Y
PIC        : [Nama Jabatan / Tim]
Trigger    : [Kondisi yang memicu prosedur ini]
Output     : [Hasil akhir yang diharapkan]
```
 
---
 
**SOP-01: Operasional Harian Data Pipeline**
 
*Trigger*: Jadwal harian (cron) atau inisiasi manual  
*PIC*: Data Engineer / DevOps Data
 
| Langkah | Aktivitas | Penanggung Jawab | Catatan |
|---|---|---|---|
| 1 | Validasi koneksi sumber data (source check) | Data Engineer | Cek credential, network, health endpoint |
| 2 | Jalankan pipeline ingestion | Orchestrator (Airflow / Prefect) | Log job ID, catat waktu mulai |
| 3 | Validasi completeness output | Data Quality Engine | Bandingkan row count source vs. target |
| 4 | Validasi freshness | Monitoring tool | Cek timestamp kolom `_loaded_at` |
| 5 | Publish status ke dashboard | Automated | Update status tile di data catalog |
| 6 | Notifikasi ke consumer jika ada anomali | Data Engineer | Via Slack/email sesuai runbook |
 
---
 
**SOP-02: Penanganan Insiden Data**
 
*Trigger*: Alert otomatis dari monitoring, atau laporan manual dari consumer  
*PIC*: Data Engineer on-duty, berkoordinasi dengan Data Governance Officer
 
| Langkah | Aktivitas | PIC | SLA Internal |
|---|---|---|---|
| 1 | Terima dan catat insiden di sistem tiket | Support / DE on-duty | ≤ 15 menit |
| 2 | Klasifikasikan severity (P1/P2/P3) | DE Lead | ≤ 30 menit |
| 3 | Isolasi dampak (sistem apa, data apa, user apa) | DE on-duty | ≤ 1 jam |
| 4 | Lakukan triage dan identifikasi root cause | DE + Data Architect | ≤ 2 jam (P1) |
| 5 | Implementasi fix atau workaround | DE | Sesuai RTO SLA |
| 6 | Validasi pemulihan (data integrity check) | QA / Data Analyst | ≤ 1 jam post-fix |
| 7 | Notifikasi consumer bahwa insiden selesai | DE Lead | Segera |
| 8 | Tulis post-mortem dalam 48 jam | DE Lead + DGO | ≤ 48 jam |
 
**Klasifikasi Severity:**
- **P1 (Critical)**: Data tidak tersedia, pipeline berhenti total, dampak ke sistem produksi
- **P2 (High)**: Data terlambat > 2× target freshness, partial failure, kualitas di bawah threshold
- **P3 (Medium)**: Anomali minor, tidak ada dampak ke consumer, bisa di-queue ke sprint berikutnya
---
 
**SOP-03: Permintaan Akses Data Baru**
 
*Trigger*: Permintaan akses dari tim/pengguna baru  
*PIC*: Data Governance Officer, disetujui oleh Data Owner
 
| Langkah | Aktivitas | PIC | SLA Internal |
|---|---|---|---|
| 1 | Ajukan form permintaan akses (nama dataset, tujuan, durasi) | Pemohon | — |
| 2 | Verifikasi identitas dan keabsahan kebutuhan | DGO | ≤ 1 hari kerja |
| 3 | Cek klasifikasi data (publik/terbatas/rahasia) | DGO + Data Owner | ≤ 1 hari kerja |
| 4 | Approve/reject oleh Data Owner | Data Owner | ≤ 2 hari kerja |
| 5 | Provisioning akses di sistem (IAM / RBAC) | Data Engineer | ≤ 1 hari kerja post-approval |
| 6 | Sosialisasi ketentuan penggunaan ke pemohon | DGO | Bersamaan dengan provisioning |
| 7 | Logging di access registry | DGO | Segera |
 
---
 
**SOP-04: Pemeliharaan dan Maintenance Terjadwal**
 
*Trigger*: Jadwal maintenance, upgrade sistem, atau patching  
*PIC*: Data Engineer + Infra/DevOps
 
| Langkah | Aktivitas | PIC |
|---|---|---|
| 1 | Informasikan ke consumer minimal H-3 via notifikasi resmi | DE Lead |
| 2 | Catat window maintenance di status page | DevOps |
| 3 | Backup data kritis sebelum maintenance dimulai | DE |
| 4 | Lakukan maintenance sesuai runbook teknis | DE + DevOps |
| 5 | Jalankan post-maintenance health check | DE |
| 6 | Konfirmasi layanan kembali normal ke consumer | DE Lead |
| 7 | Update catatan change log | DGO / DE Lead |
 
---
 
**SOP-05: Manajemen Kualitas Data (Data Quality Gate)**
 
*Trigger*: Setiap pipeline run, atau review kualitas berkala  
*PIC*: Data Quality Engineer / Data Analyst
 
| Langkah | Aktivitas | PIC |
|---|---|---|
| 1 | Jalankan suite aturan kualitas (completeness, validity, consistency, uniqueness) | Automated (dbt test / Great Expectations) |
| 2 | Evaluasi hasil: pass/warn/fail per dimensi | Data Quality Engine |
| 3 | Jika fail: quarantine data ke zona staging, jangan publish ke downstream | Automated + DE |
| 4 | Notifikasi ke data owner dan consumer tentang anomali | Automated alert |
| 5 | Root cause analysis untuk fail berulang | Data Quality Engineer |
| 6 | Update aturan validasi jika ada perubahan skema bisnis | DE + Data Analyst |
| 7 | Dokumentasikan hasilnya di data quality report | DGO |
 
---
 
### BAB 4 — ROLES & RESPONSIBILITIES (RACI)
 
| Aktivitas | Data Engineer | Data Governance Officer | Data Owner | Consumer / Pengguna | Management |
|---|---|---|---|---|---|
| Menjalankan pipeline harian | R | I | I | I | — |
| Menangani insiden P1 | R | C | I | I | I |
| Menyetujui akses data | C | R | A | I | — |
| Review SLA bulanan | C | R | A | I | I |
| Update aturan kualitas | R | A | C | C | — |
| Menyusun post-mortem | R | A | I | I | C |
 
*R = Responsible, A = Accountable, C = Consulted, I = Informed*
 
---
 
### BAB 5 — MONITORING, PELAPORAN, DAN CONTINUOUS IMPROVEMENT
 
**5.1 Dashboard Monitoring**
Metrik yang harus tampil di dashboard real-time: uptime, freshness, completeness, jumlah insiden aktif, SLA compliance rate.
 
**5.2 Laporan Berkala**
 
| Frekuensi | Isi | Penerima |
|---|---|---|
| Harian | Status pipeline, alert kualitas | Tim Data |
| Mingguan | SLA scorecard, ringkasan insiden | Data Governance Officer, Tim Lead |
| Bulanan | SLA compliance report, tren kualitas, rekomendasi | Data Owner, Management |
 
**5.3 Review dan Continuous Improvement**
- Review SLA dan SOP minimal setiap 6 bulan atau setelah insiden P1
- Setiap post-mortem P1/P2 wajib menghasilkan minimal 1 action item perbaikan
- Action item ditrack di backlog tim data
---
 
### BAB 6 — LAMPIRAN
 
**Lampiran A — Formulir Permintaan Akses Data**
*(Template form: nama pemohon, unit, dataset yang diminta, tujuan, durasi, tanda tangan persetujuan)*
 
**Lampiran B — Template Laporan Insiden (Post-Mortem)**
- Ringkasan insiden
- Timeline kejadian
- Root cause
- Dampak
- Action item dan PIC
- Lessons learned
**Lampiran C — Daftar Kontak Eskalasi**
 
| Level | Jabatan | Kontak | Jam Operasional |
|---|---|---|---|
| L1 | Data Engineer on-duty | [email/slack] | 08.00 – 17.00 WIB |
| L2 | DE Lead / Data Governance Officer | [email/HP] | 24/7 untuk P1 |
| L3 | CTO / Head of Data | [email/HP] | P1 only |
 
**Lampiran D — Referensi Regulasi**
*(Sesuaikan dengan konteks. Contoh:)*
- Perpres 95/2018 tentang SPBE
- Perpres 39/2019 tentang Satu Data Indonesia
- UU No. 27/2022 tentang Pelindungan Data Pribadi
- DAMA-DMBOK2 (Data Management Body of Knowledge)
- ISO 8000 (Data Quality)
- PMK / OJK terkait (jika konteks keuangan)
---
 
## Panduan Kustomisasi Cepat
 
Gunakan tabel ini untuk memutuskan bagian mana yang perlu dimodifikasi berdasarkan konteks:
 
| Konteks | Bagian yang Paling Perlu Dikustomisasi |
|---|---|
| **Government / SPBE** | Regulasi (Bab 1.5), metrik ketersediaan SPBE, SOP akses berbasis RBAC Satu Data |
| **Data Warehouse / Lakehouse** | Freshness SLA per zone (Bronze/Silver/Gold), SOP quality gate dbt |
| **Fintech / Perbankan** | RTO/RPO sesuai POJK, SOP pelaporan insiden ke regulator, data retention policy |
| **Data Catalog / Metadata** | SLA kelengkapan metadata, SOP onboarding dataset baru, SOP update business glossary |
| **Master Data Management** | SOP golden record creation, SLA stewardship, SOP data deduplication |
| **Real-time / Streaming** | SLA latensi end-to-end (ms/s), SOP penanganan consumer lag, SOP schema evolution |
 
---
 
## Format Output Default
 
- **Dokumen utama**: Markdown dengan heading hierarkis, siap dikonversi ke DOCX/PDF
- **Tabel**: Markdown table (compatible dengan semua renderer)
- **Kode/template**: Code block
- **File DOCX**: Jika pengguna meminta, gunakan skill `docx` untuk menghasilkan file siap cetak dengan kop surat dan page numbering
## Catatan Kualitas
 
Setiap Panduan Lengkap yang dihasilkan harus:
1. Menggunakan bahasa Indonesia formal (atau bilingual jika diminta)
2. Menyertakan versi, tanggal, dan status dokumen
3. Memiliki setidaknya 5 SOP (bisa lebih sesuai kebutuhan)
4. Setiap SOP memiliki PIC yang jelas, bukan hanya "tim"
5. Metrik SLA harus kuantitatif dan terukur, bukan deskriptif samar
6. Menyertakan tabel RACI
7. Konsisten antara komitmen SLA (Bab 2) dan prosedur SOP (Bab 3)