---
title: "Data Retention Policy — <Nama Domain / Data Product>"
sidebar_label: "Data Retention Policy"
sidebar_position: 4
description: "Kebijakan retensi data: jadwal retensi per klasifikasi, prosedur archival, purging, dan kepatuhan regulasi UU PDP dan peraturan sektoral."
tags: [governance, data-retention, privacy, compliance, uu-pdp, archival]
doc_id: "G-04"
scope: "<domain-level | data-product-level>"
domain: "<Nama Domain>"
data_product_id: "<domain>/<data-product-name>/v<version> | N/A jika domain-level>"
dgo_reviewer: "<Nama Data Governance Officer>"
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
next_review_date: "<YYYY-MM-DD>"
review_cycle: "Tahunan atau saat regulasi berubah"
---

# Data Retention Policy

> **Tujuan dokumen ini:** Mendefinisikan berapa lama setiap kategori data boleh disimpan, bagaimana prosedur archival dan penghapusan yang benar, dan dasar hukum setiap keputusan retensi — sesuai UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi dan regulasi sektoral yang berlaku.

:::warning Dokumen Legal-Binding
Kebijakan ini bersifat mengikat. Penyimpanan data melampaui periode retensi yang ditetapkan, atau penghapusan data sebelum periode minimum, adalah pelanggaran kepatuhan yang dapat berimplikasi hukum.
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis | Reviewer Legal |
|---|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama, Role>` | `<Nama Legal>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `G-04` |
| **Scope** | `<Domain-level>` / `<Data Product: nama>` |
| **Domain** | `<Nama Domain>` |
| **Policy Owner** | `<Nama DGO / Legal Officer, Email>` |
| **Data Steward** | `<Nama, Email>` |
| **DPO Organisasi** | `<Nama, Email>` |
| **Legal Reviewer** | `<Nama, Email>` |
| **Dokumen terkait** | [D-07 RoPA](../design/risk-assessment.md) · [D-08 DPIA](../design/risk-assessment.md) · [G-05 Governance Checklist](./federated-governance-checklist.md) · [M-05 Backup & DR Plan](../monitoring/backup-dr-plan.md) |

---

## 1. Dasar Hukum

### 1.1 Regulasi yang Berlaku

| Regulasi | Relevansi | Ketentuan Retensi |
|---|---|---|
| UU No. 27 Tahun 2022 tentang PDP | Data pribadi — dasar utama | Ps. 20: hapus setelah tujuan tercapai atau atas permintaan subjek |
| PP No. 71 Tahun 2019 (PSTE) | Penyelenggara sistem elektronik | Ps. 46: log transaksi minimum 3 tahun |
| `<Regulasi sektoral — contoh: POJK, PMK, dll.>` | `<Relevansi>` | `<Ketentuan spesifik>` |
| `<Regulasi internal organisasi>` | Kebijakan internal | `<Ketentuan>` |

### 1.2 Prinsip Minimalisasi Data

Sesuai Pasal 16 UU PDP, data hanya boleh disimpan selama:
1. Diperlukan untuk tujuan pemrosesan yang sah
2. Kewajiban hukum mengharuskan penyimpanan
3. Berkaitan dengan kepentingan publik atau penelitian ilmiah yang sah

---

## 2. Jadwal Retensi

### 2.1 Retensi berdasarkan Klasifikasi Data

| Klasifikasi | Contoh Data | Retensi Aktif | Retensi Arsip | Total Maksimum | Dasar Hukum |
|---|---|---|---|---|---|
| **Public** | Data agregat terpublikasi, kode referensi | Selama relevan | Tidak dibatasi | Tidak dibatasi | Tidak ada pembatasan khusus |
| **Internal** | Data operasional non-PII, log sistem | `<5 tahun>` | `<2 tahun>` | `<7 tahun>` | Kebijakan internal |
| **Restricted (PII Standar)** | Nama, NIK, nomor HP, email, alamat | `<2 tahun>` sejak tujuan tercapai | `<1 tahun>` (arsip aman) | `<3 tahun>` | UU PDP Ps. 20 |
| **Confidential (PII Sensitif)** | Data kesehatan, biometrik, agama | `<1 tahun>` sejak tujuan tercapai | Tidak diarsip — hapus langsung | `<1 tahun>` | UU PDP Ps. 4 + sektoral |

### 2.2 Retensi berdasarkan Kategori Data

| Kategori | Periode Aktif | Periode Arsip | Keterangan |
|---|---|---|---|
| Data transaksi bisnis | `<5 tahun>` sejak transaksi | `<2 tahun>` | Sesuai kebutuhan audit & perpajakan |
| Log akses sistem (non-PII) | `<1 tahun>` | `<2 tahun>` | PSTE Ps. 46 minimum 3 tahun total |
| Log audit data (siapa akses apa) | `<2 tahun>` | `<3 tahun>` | Total 5 tahun untuk keperluan forensik |
| Data untuk model ML / training | `<Durasi model aktif + 1 tahun>` | Tidak diarsip | Hapus saat model retired |
| Backup database | Backup terbaru + `<4 minggu>` rolling | `<3 bulan>` snapshot bulanan | Lihat [M-05 Backup Plan](../monitoring/backup-dr-plan.md) |
| Komunikasi consumer (log request API) | `<90 hari>` | Tidak diarsip | Hanya metadata, bukan konten |

---

## 3. Inventori Data dan Jadwal Retensi

### 3.1 Per Tabel / Objek Data

| Tabel / Objek | Berisi PII? | Klasifikasi | Periode Aktif | Periode Arsip | Metode Hapus | Catatan |
|---|---|---|---|---|---|---|
| `<schema>.v_<product>_daily` | `<Ya/Tidak>` | `<Internal>` | `<5 tahun>` | `<2 tahun cold storage>` | `DELETE WHERE tanggal < cutoff` | View — hapus dari tabel dasar |
| `<schema>.fct_<entity>` | `<Ya/Tidak>` | `<Internal>` | `<5 tahun>` | `<2 tahun cold storage>` | Partisi DROP | Dipartisi per bulan |
| `<schema>.dim_<entity>` | `<Ya: nama, NIK>` | `<Restricted>` | `<2 tahun>` sejak `valid_to` | Tidak diarsip | Pseudonimisasi → DELETE | SCD Type 2: hapus row expired |
| `bronze.<staging_table>` | `<Ya>` | `<Restricted>` | `<90 hari>` | Tidak diarsip | `TRUNCATE PARTITION` | Bronze tidak perlu retensi panjang |
| `s3://<bucket>/exports/` | `<Bervariasi>` | `<Internal/Restricted>` | `<1 tahun>` | `<2 tahun Glacier>` | S3 Lifecycle Policy | Lifecycle dikonfigurasi di S3 |
| Airflow task logs | Tidak | `Internal` | `<30 hari>` | Tidak diarsip | Airflow auto-cleanup | Konfigurasi di `airflow.cfg` |
| API access logs (metadata) | Tidak | `Internal` | `<90 hari>` | Tidak diarsip | Log rotation otomatis | Bukan konten request |

---

## 4. Prosedur Archival

### 4.1 Kriteria Data Masuk Arsip

Data dipindahkan ke cold storage / arsip jika:
- Melewati periode aktif (kolom 5 di Bagian 3.1)
- Tidak pernah diakses dalam `<12 bulan>` terakhir (auto-detect via access log)
- Data product masuk fase retirement (lihat [E-01 EoSL Report](../eosl/eosl-report.md))

### 4.2 Prosedur Archival untuk Database

```sql
-- Langkah 1: Identifikasi data yang perlu diarsip
SELECT COUNT(*), MIN(tanggal), MAX(tanggal)
FROM <schema>.fct_<entity>
WHERE tanggal < (CURRENT_DATE - INTERVAL '<periode aktif>');

-- Langkah 2: Export ke arsip sebelum delete
COPY (
    SELECT * FROM <schema>.fct_<entity>
    WHERE tanggal < (CURRENT_DATE - INTERVAL '<periode aktif>')
)
TO PROGRAM 'aws s3 cp - s3://<bucket>/archive/<domain>/<product>/$(date +%Y-%m)/archive_$(date +%Y%m%d).csv'
WITH (FORMAT CSV, HEADER);

-- Langkah 3: Verifikasi arsip berhasil
-- (cek row count di file S3 vs di database)

-- Langkah 4: Hapus dari production DB
DELETE FROM <schema>.fct_<entity>
WHERE tanggal < (CURRENT_DATE - INTERVAL '<periode aktif>');

-- Langkah 5: VACUUM untuk reclaim storage
VACUUM ANALYZE <schema>.fct_<entity>;
```

### 4.3 Prosedur Archival untuk S3

Dikonfigurasi via S3 Lifecycle Policy:

```json
{
  "Rules": [
    {
      "ID": "dp-<product>-archive-policy",
      "Filter": { "Prefix": "dp/<domain>/<product>/" },
      "Status": "Enabled",
      "Transitions": [
        { "Days": 365, "StorageClass": "STANDARD_IA" },
        { "Days": 730, "StorageClass": "GLACIER" }
      ],
      "Expiration": { "Days": 2555 }
    }
  ]
}
```

---

## 5. Prosedur Penghapusan (Purging)

### 5.1 Kriteria Penghapusan

Data dihapus permanen jika:
- Melewati total periode maksimum (aktif + arsip)
- Permintaan hak hapus dari subjek data (Right to Erasure per UU PDP Ps. 21)
- Perintah dari DPO Organisasi atau putusan hukum
- Data product masuk fase retirement final

### 5.2 Prosedur Penghapusan PII — Right to Erasure

**Trigger:** Request subjek data melalui kanal resmi.

1. Terima request dan verifikasi identitas subjek (via tim Legal)
2. Identifikasi seluruh record yang berisi data PII subjek tersebut:

```sql
-- Contoh: cari semua record dengan NIK tertentu
SELECT 'schema.tabel_1' AS lokasi, id FROM <schema>.dim_<entity>
WHERE nik = '<NIK_subjek>'
UNION ALL
SELECT 'schema.tabel_2' AS lokasi, id FROM <schema>.fct_<entity>
WHERE entity_id IN (SELECT id FROM <schema>.dim_<entity> WHERE nik = '<NIK_subjek>');
```

3. Pilih metode penghapusan:
   - **Hapus penuh** (`DELETE`) — jika tidak ada kewajiban hukum menyimpan
   - **Pseudonimisasi** — jika data masih diperlukan untuk keperluan statistik/audit namun identitas harus dihapus

```sql
-- Pseudonimisasi: ganti PII dengan hash irreversible
UPDATE <schema>.dim_<entity>
SET
    nama = 'REDACTED',
    nik  = SHA256(nik::bytea)::text,  -- hash irreversible
    updated_at = NOW()
WHERE nik = '<NIK_subjek>' AND is_current = TRUE;
```

4. Catat tindakan di audit log dan RoPA
5. Kirim konfirmasi ke subjek data dalam `<30 hari>` (sesuai UU PDP)

### 5.3 Jadwal Purging Berkala

| Jadwal | Tindakan | Dikerjakan Oleh | Diverifikasi Oleh |
|---|---|---|---|
| Harian (otomatis) | Bronze layer > 90 hari → DELETE | Airflow DAG | Alert monitoring |
| Bulanan | API logs > 90 hari → DELETE | Airflow DAG | SRE |
| Kuartalan | Review data yang melewati periode aktif → arsip | Data Steward | DGO |
| Tahunan | Review arsip yang melewati periode arsip → hapus permanen | DGO + Legal | DPO Organisasi |

---

## 6. Pengecualian Retensi

Retensi dapat diperpanjang melampaui jadwal default hanya dengan **persetujuan tertulis DGO dan Legal** dalam situasi berikut:

| Situasi | Dasar | Durasi Pengecualian | Siapa yang Menyetujui |
|---|---|---|---|
| Litigasi aktif atau investigasi hukum | Legal hold | Hingga kasus selesai + 1 tahun | Legal Officer + DPO |
| Pemeriksaan regulator | Regulatory hold | Sesuai permintaan regulator | DPO + Exec |
| Penelitian ilmiah berlisensi | Kepentingan publik (UU PDP Ps. 20c) | Sesuai jangka penelitian + 2 tahun | DGO + DPO |
| Audit eksternal ongoing | Audit hold | Hingga audit selesai + 6 bulan | Internal Audit + DGO |

Setiap pengecualian didokumentasikan dalam tabel berikut:

| ID | Tabel Terdampak | Alasan | Tanggal Mulai | Tanggal Berakhir | Disetujui Oleh |
|---|---|---|---|---|---|
| EX-001 | `<tabel>` | `<alasan>` | `<YYYY-MM-DD>` | `<YYYY-MM-DD>` | `<Nama>` |

---

## 7. Monitoring dan Kepatuhan

### 7.1 Dashboard Retensi

Pantau kepatuhan retensi di: `<https://catalog.domain.org/<domain>/<product>/retention>`

Metrik yang dipantau:
- Persentase data melampaui periode aktif yang belum diarsip
- Jumlah record PII yang melebihi batas retensi
- Status pengecualian aktif

### 7.2 Review Tahunan

Setiap tahun, kebijakan ini di-review oleh DGO + Legal untuk memastikan kesesuaian dengan:
- Perubahan regulasi (UU PDP, peraturan turunan, regulasi sektoral)
- Perubahan jenis data yang diproses
- Perubahan infrastruktur penyimpanan

---

## Annex A — Checklist Purging Kuartalan

```
PURGING CHECKLIST — Q<N> <YYYY>
Dikerjakan oleh: _______________
Tanggal      : _______________

REVIEW DATA PRODUKSI
[ ] Cek data melewati periode aktif: SELECT MIN(tanggal), MAX(tanggal) FROM ...
[ ] Jumlah record yang perlu diarsip: _____ records
[ ] Arsip berhasil dibuat di S3: s3://...
[ ] Row count arsip terverifikasi sama dengan source: _____ rows
[ ] DELETE dari production DB berhasil
[ ] VACUUM setelah DELETE dijalankan

REVIEW PII
[ ] Tidak ada NIK/nama yang tersisa di Bronze layer > 90 hari
[ ] Right-to-erasure requests bulan ini sudah diproses: _____ requests

PENGECUALIAN
[ ] Semua active holds masih valid dan dalam batas waktu
[ ] Tidak ada hold yang kadaluarsa tanpa diperpanjang atau dicabut

DOKUMENTASI
[ ] Tabel pengecualian di-update
[ ] Audit log mencatat semua tindakan purging
[ ] DGO di-notifikasi tentang hasil review

Catatan: _______________
Diverifikasi oleh DGO: _______________
```
