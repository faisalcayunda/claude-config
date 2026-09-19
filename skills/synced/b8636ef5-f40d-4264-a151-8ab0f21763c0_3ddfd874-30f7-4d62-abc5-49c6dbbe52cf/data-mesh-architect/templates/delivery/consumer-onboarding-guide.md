---
title: "Consumer Onboarding Guide — <Nama Data Product>"
sidebar_label: "Consumer Onboarding Guide"
sidebar_position: 1
description: "Panduan onboarding lengkap bagi consumer baru data product: akses, kredensial, quick start, pola konsumsi, dan support."
tags: [delivery, onboarding, consumer, data-product]
doc_id: "DLV-01"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: delivery
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Consumer Onboarding Guide

> **Tujuan dokumen ini:** Memandu consumer baru dari nol hingga berhasil mengonsumsi data product secara mandiri — tanpa perlu bertanya ke tim Data Engineering.

:::tip Sebelum Membaca
Dokumen ini bersifat **self-contained**. Semua yang Anda butuhkan untuk onboarding pertama ada di sini. Jika ada langkah yang tidak dapat diselesaikan, lihat [Section 8 — Support & Eskalasi](#8-support--eskalasi).
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `DLV-01` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Versi Data Product** | `<vX.Y.Z>` |
| **Data Product Owner** | `<Nama, Email>` |
| **Data Steward** | `<Nama, Email>` |
| **Dokumen ini berlaku sejak** | `<YYYY-MM-DD>` |
| **Dokumen terkait** | [D-02 Data Contract](../design/data-contract-spec.md) · [D-04 Data Catalog](../design/data-catalog.md) · [DLV-02 Self-Service Infra Guide](./self-service-infra-guide.md) |

---

## 1. Pendahuluan

### 1.1 Target Audience

`[Mandatory]`

Dokumen ini ditujukan untuk:

| Persona | Deskripsi | Pengetahuan yang Diasumsikan |
|---|---|---|
| **Analyst / Data Scientist** | Mengonsumsi data untuk analisis, modeling, atau pelaporan | SQL atau Python dasar; familiar dengan konsep tabel dan skema |
| **Application Developer** | Mengintegrasikan data product ke dalam sistem atau aplikasi | REST API, JSON, autentikasi berbasis token |
| **Business Intelligence Engineer** | Membangun dashboard atau laporan dari data product | BI tools (Tableau, Power BI, Looker); SQL |

:::note Bukan Target Audience
Dokumen ini **tidak** ditujukan untuk Data Engineer yang ingin membangun pipeline di atas data product ini. Lihat [V-02 Data API Brief](../development/api-brief.md) dan [V-01 Data Pipeline Brief](../development/pipeline-brief.md) untuk keperluan tersebut.
:::

---

### 1.2 Lingkup Dokumen

**Yang dicakup dokumen ini:**

- Proses permintaan akses hingga kredensial aktif
- Verifikasi akses pertama kali
- Overview isi data dan keterbatasannya
- Contoh query / konsumsi yang siap dijalankan
- Pola penggunaan yang direkomendasikan dan anti-pattern
- Prosedur support dan eskalasi

**Yang TIDAK dicakup dokumen ini:**

- Cara membangun pipeline mengonsumsi data product ini → lihat [V-01](../development/pipeline-brief.md)
- Cara melakukan deployment infrastruktur consumer → lihat [DLV-02](./self-service-infra-guide.md)
- Detail teknis skema lengkap → lihat [D-02](../design/data-contract-spec.md)
- Definisi bisnis setiap atribut → lihat [G-01 Kamus Data](../../governance/data-vocabulary-template.md)

---

### 1.3 Dokumen Terkait

| Kode | Judul | Relevansi |
|---|---|---|
| [D-02](../design/data-contract-spec.md) | Data Contract & Interface Specification | Schema lengkap, SLA formal, semantic definitions |
| [D-03](../design/data-contract.yaml) | Data Contract YAML | Machine-readable contract |
| [D-04](../design/data-catalog.md) | Data Catalog & Metadata | Metadata, lineage, tags, discovery |
| [D-05](../design/quality-design.md) | Data Quality Design | Quality rules, thresholds, known quality issues |
| [G-01](../../governance/data-vocabulary-template.md) | Kamus Data | Definisi bisnis setiap atribut dan enum |
| [G-02](../../governance/data-access-control-matrix.md) | Data Access Control Matrix | Hak akses per role per atribut |
| [DLV-02](./self-service-infra-guide.md) | Self-Service Infrastructure Guide | Panduan infrastruktur mandiri setelah onboarding |
| [M-07](../monitoring/operational-reports.md) | Operations Runbook | Prosedur operasional dan health check |

---

### 1.4 Istilah dan Singkatan

| Istilah | Definisi |
|---|---|
| **Data Product** | Unit data yang dikelola seperti produk: memiliki owner, kontrak, SLA, dan lifecycle |
| **Output Port** | Antarmuka yang disediakan data product untuk diakses consumer (REST API, SQL, file) |
| **Data Contract** | Perjanjian formal antara producer dan consumer tentang skema, SLA, dan semantik |
| **SLO** | Service Level Objective — target kualitas layanan internal (mis. freshness ≤ 1 jam) |
| **SLA** | Service Level Agreement — komitmen resmi kepada consumer dengan konsekuensi jika dilanggar |
| **Consumer** | Pihak yang mengonsumsi data product (aplikasi, tim analitik, pipeline downstream) |
| `<Istilah domain spesifik>` | `<Definisi>` |

> Untuk daftar istilah domain yang lebih lengkap, lihat [G-01 Kamus Data](../../governance/data-vocabulary-template.md).

---

## 2. Prasyarat Onboarding

### 2.1 Persyaratan Akses

`[Mandatory]` — *Role: Consumer + Data Steward*

Pastikan semua item berikut terpenuhi sebelum memulai proses permintaan akses:

| # | Persyaratan | Cara Verifikasi | PIC Approver |
|---|---|---|---|
| P-01 | Memiliki akun aktif di sistem SSO organisasi | Login ke `<https://sso.domain.org>` | IT Helpdesk |
| P-02 | Memiliki justifikasi bisnis terdokumentasi untuk mengakses data ini | Dokumen tersedia di JIRA / Google Drive | Data Product Owner |
| P-03 | Telah membaca dan menyetujui Data Sharing Agreement | Form consent di `<link>` | Data Steward |
| P-04 | Role `<nama_role>` telah di-assign di sistem IAM | Cek di `<https://iam.domain.org/my-roles>` | IT Security |

:::warning Akses Bertahap untuk Data Classified ≥ Restricted
Jika data product ini diklasifikasikan sebagai **Restricted** atau **Confidential**, akses hanya diberikan setelah persetujuan tambahan dari Data Product Owner **dan** DPO. Proses ini dapat memakan waktu `<3–5 hari kerja>`.
:::

---

### 2.2 Tools yang Dibutuhkan

`[Mandatory]`

| Tool | Versi Minimum | Tujuan | Link Unduh / Instalasi |
|---|---|---|---|
| `<Database client (DBeaver / pgAdmin)>` | `<23.x>` | Akses SQL output port | `<https://dbeaver.io>` |
| `<Python>` | `<3.10>` | Script konsumsi, analisis | `<https://python.org>` |
| `<curl / Postman>` | `<any>` | Testing REST API | `<https://postman.com>` |
| `<BI Tool (Tableau / Power BI)>` | `<sesuai lisensi organisasi>` | Dashboard & reporting | `<Link portal internal>` |

:::note Tool Opsional
Untuk konsumsi skala besar (>1 juta baris), direkomendasikan menggunakan `<Apache Spark / dbt>`. Lihat [Section 7 — Pola Penggunaan](#7-pola-penggunaan--best-practices).
:::

---

### 2.3 Kebutuhan Jaringan

`[Mandatory]` — *Hubungi IT Network jika ada firewall rule yang diperlukan*

| # | Endpoint | Port | Protokol | Tujuan |
|---|---|---|---|---|
| N-01 | `<host.domain.org>` | `5432` | `TCP` | PostgreSQL — SQL output port |
| N-02 | `<api.domain.org>` | `443` | `HTTPS` | REST API output port |
| N-03 | `<auth.domain.org>` | `443` | `HTTPS` | OAuth 2.0 / SSO token endpoint |
| N-04 | `<catalog.domain.org>` | `443` | `HTTPS` | Data catalog (discovery) |
| N-05 | `<kafka.domain.org>` | `9093` | `TLS` | Kafka — streaming output port (jika applicable) |

:::tip VPN
Seluruh endpoint di atas membutuhkan koneksi **VPN korporat aktif**. Pastikan VPN terhubung sebelum mencoba akses.
:::

---

## 3. Provisioning Akses

### 3.1 Cara Mengajukan Permintaan Akses

`[Mandatory]` — *Role: Consumer*

Ikuti langkah-langkah berikut secara berurutan:

**Langkah 1 — Buka form permintaan akses**

Navigasi ke: `<https://portal.domain.org/data-access-request>`

**Langkah 2 — Isi form dengan informasi berikut**

| Field | Yang Harus Diisi |
|---|---|
| Data Product | `<domain>/<nama-data-product>` |
| Versi | `<vX.Y>` |
| Role yang Diminta | `<dp_<product>_read_standard \| dp_<product>_read_privileged>` |
| Justifikasi Bisnis | Jelaskan use case spesifik (min. 2 kalimat) |
| Durasi Akses | `<Permanen \| Temporary: 30/60/90 hari>` |
| Supervisor Approval | Email atasan langsung |

**Langkah 3 — Submit dan catat Ticket ID**

Setelah submit, simpan **Ticket ID** (format: `DAR-NNNN`) untuk keperluan follow-up.

**SLA Pemrosesan Permintaan:**

| Klasifikasi Data | SLA Approval | Catatan |
|---|---|---|
| Public / Internal | `<1 hari kerja>` | Auto-approved jika role standar |
| Restricted | `<3 hari kerja>` | Membutuhkan approval Data Product Owner |
| Confidential | `<5 hari kerja>` | Membutuhkan approval DPO + Data Product Owner |

---

### 3.2 Setup Kredensial

`[Mandatory]` — *Role: Consumer*

Setelah akses disetujui, Anda akan menerima notifikasi via email. Ikuti langkah berikut sesuai output port yang akan digunakan:

#### 3.2.1 SQL Output Port (PostgreSQL)

```bash
# Kredensial akan dikirim via Vault / password manager organisasi
# Ambil kredensial dari:
vault kv get secret/<env>/consumer/<ticket-id>/db-credentials

# Atau via portal:
# https://vault.domain.org/ui/vault/secrets/consumer/<ticket-id>
```

Simpan nilai berikut dari respons Vault:

| Parameter | Nama Environment Variable | Keterangan |
|---|---|---|
| Host | `DB_HOST` | `<host.domain.org>` |
| Port | `DB_PORT` | `5432` |
| Database | `DB_NAME` | `<nama_database>` |
| Username | `DB_USER` | Unik per consumer |
| Password | `DB_PASSWORD` | Rotasi setiap `<90 hari>` |
| Schema | `DB_SCHEMA` | `<nama_schema>` |

#### 3.2.2 REST API Output Port

```bash
# Dapatkan OAuth Client ID dan Client Secret dari Vault
vault kv get secret/<env>/consumer/<ticket-id>/api-credentials
```

| Parameter | Nama Environment Variable |
|---|---|
| Client ID | `API_CLIENT_ID` |
| Client Secret | `API_CLIENT_SECRET` |
| Token URL | `API_TOKEN_URL` = `<https://auth.domain.org/oauth/token>` |
| Base URL | `API_BASE_URL` = `<https://api.domain.org/v1>` |
| Scope | `API_SCOPE` = `<read:<product>>` |

:::danger Jangan Simpan Kredensial di Kode
JANGAN hardcode `API_CLIENT_SECRET`, `DB_PASSWORD`, atau kredensial lainnya di source code, notebook, atau file konfigurasi yang di-commit ke Git. Gunakan environment variables atau secrets manager.
:::

---

### 3.3 Verifikasi Akses

`[Mandatory]` — *Jalankan verifikasi ini sebelum melanjutkan ke Section 4*

#### 3.3.1 Verifikasi SQL

```sql
-- Jalankan query ini. Jika berhasil, akses SQL Anda aktif.
SELECT
    '<nama_schema>' AS schema_verified,
    current_user   AS connected_as,
    now()          AS verified_at;
```

**Output yang diharapkan:**

```
schema_verified  | connected_as              | verified_at
-----------------+---------------------------+----------------------------
<nama_schema>    | dp_<product>_<your-user>  | 2025-01-15 09:23:41.123+07
```

#### 3.3.2 Verifikasi REST API

```bash
# Step 1: Dapatkan access token
export TOKEN=$(curl -s -X POST "$API_TOKEN_URL" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=$API_CLIENT_ID&client_secret=$API_CLIENT_SECRET&scope=$API_SCOPE" \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

# Step 2: Panggil health endpoint
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API_BASE_URL/health" | python3 -m json.tool
```

**Output yang diharapkan:**

```json
{
  "status": "healthy",
  "data_product": "<nama-data-product>",
  "version": "<vX.Y.Z>",
  "last_updated": "<ISO 8601 timestamp>"
}
```

:::warning Jika Verifikasi Gagal
Jika salah satu verifikasi di atas menghasilkan error, jangan lanjutkan ke section berikutnya. Lihat [Section 8.1 — Kanal Support](#81-kanal-support) dan sertakan Ticket ID akses Anda saat menghubungi tim support.
:::

---

## 4. Overview Data Product

### 4.1 Apa yang Tersedia

`[Mandatory]` — *Role: Data Product Owner*

`[Isi deskripsi bisnis data product ini dalam 2–3 kalimat. Jelaskan: apa yang direpresentasikan data ini, dari proses bisnis apa data ini berasal, dan untuk keputusan apa data ini berguna.]`

> **Contoh:** "Data product ini menyajikan rekap harian transaksi pengiriman bantuan sosial per penerima manfaat di seluruh wilayah Indonesia. Data bersumber dari sistem disbursement operasional dan diproses setiap hari pukul 02:00 WIB. Data ini digunakan untuk monitoring distribusi, rekonsiliasi anggaran, dan pelaporan ke Kementerian."

**Output Port yang Tersedia:**

| Output Port | Tipe | Alamat / Endpoint | Format | Keterangan |
|---|---|---|---|---|
| `<SQL View>` | SQL | `<schema.v_nama_view>` | Tabel relasional | Direkomendasikan untuk query ad-hoc & BI |
| `<REST API>` | HTTP | `<https://api.domain.org/v1/<resource>>` | JSON | Direkomendasikan untuk integrasi aplikasi |
| `<File Export>` | Batch File | `<s3://bucket/path/>` | CSV / Parquet | Untuk bulk export (>1 juta baris) |
| `<Kafka Topic>` | Streaming | `<topic: dp.<domain>.<product>.v1>` | Avro / JSON | Untuk kebutuhan real-time (jika applicable) |

---

### 4.2 Freshness Data & SLA

`[Mandatory]` — *Referensi: [D-02 Data Contract §3](../design/data-contract-spec.md)*

| Metrik | Target SLO | Cara Ukur | Cara Monitor |
|---|---|---|---|
| **Data Freshness** | Data tersedia dalam `<1 jam>` setelah cut-off source | `MAX(updated_at)` pada tabel utama | `<https://monitoring.domain.org/dp/<product>/freshness>` |
| **Uptime (SQL Port)** | `≥ 99.5%` per bulan | Synthetic query setiap 5 menit | `<https://monitoring.domain.org/dp/<product>/uptime>` |
| **Uptime (API Port)** | `≥ 99.9%` per bulan | Synthetic request setiap 1 menit | `<https://monitoring.domain.org/dp/<product>/api-health>` |
| **Completeness** | `≥ 99%` record dari source terkonsumsi | Row count vs source reconciliation | `<https://monitoring.domain.org/dp/<product>/quality>` |
| **Latency API (P95)** | `≤ 500ms` | Percentile dari request log | Dashboard di atas |

**Jadwal Update:**

| Sumber | Frekuensi Update | Waktu Cut-Off | Estimasi Tersedia |
|---|---|---|---|
| `<Sistem Sumber A>` | `<Harian>` | `<23:59 WIB>` | `<01:30 WIB (H+1)>` |
| `<Sistem Sumber B>` | `<Real-time (5 menit lag)>` | `N/A` | `N/A` |

---

### 4.3 Klasifikasi Data & Pembatasan Akses

`[Mandatory]` — *Referensi: [G-02 Access Control Matrix](../../governance/data-access-control-matrix.md)*

| Kelompok Atribut | Klasifikasi | Role yang Diperlukan | Perlakuan untuk Role Standard |
|---|---|---|---|
| ID teknis, kode referensi, status, tanggal | `Internal` | `dp_<product>_read_standard` | Tampil penuh |
| Nama, alamat (non-spesifik), jumlah agregat | `Internal` | `dp_<product>_read_standard` | Tampil penuh |
| NIK, nomor rekening, nomor HP | `Restricted (PII)` | `dp_<product>_read_privileged` | Masked / tidak tersedia |
| Data kesehatan, biometrik, data anak | `Confidential` | Persetujuan DPO khusus | Tidak tersedia |

:::warning Larangan Penggunaan Data
Data yang diperoleh dari data product ini **dilarang** digunakan untuk:
- Profiling individu di luar tujuan yang tercantum dalam Data Sharing Agreement
- Digabungkan dengan sumber eksternal tanpa persetujuan DPO
- Disimpan di sistem personal (laptop, Google Drive personal, dsb.)

Pelanggaran dapat mengakibatkan pencabutan akses dan tindakan disiplin sesuai kebijakan organisasi.
:::

---

### 4.4 Keterbatasan yang Diketahui

`[Mandatory]` — *Perbarui section ini setiap kali ada known issue baru*

| # | Keterbatasan | Dampak | Workaround | Berlaku Sejak |
|---|---|---|---|---|
| L-01 | `<Data periode >3 tahun lalu tidak tersedia di SQL View — ada di cold storage>` | `<Query historis panjang tidak bisa langsung>` | `<Gunakan file export endpoint untuk data >3 tahun>` | `<YYYY-MM-DD>` |
| L-02 | `<Field <nama_field> bisa NULL untuk record sebelum YYYY-MM-DD>` | `<COUNT / aggregasi mungkin tidak akurat untuk periode lama>` | `<Filter: WHERE record_date >= 'YYYY-MM-DD'>` | `<YYYY-MM-DD>` |
| L-03 | `<API endpoint /v1/<resource>/bulk dibatasi 10.000 record per request>` | `<Bulk export besar perlu pagination>` | `<Gunakan cursor pagination — lihat Section 7.1>` | `<YYYY-MM-DD>` |

---

## 5. Quick Start

> Tujuan section ini: membawa Anda dari kredensial aktif ke **hasil query pertama dalam 10 menit**.

### 5.1 Quick Start SQL (Analyst / BI Engineer)

**Langkah 1 — Koneksi ke database**

```
Host:     <DB_HOST>
Port:     5432
Database: <DB_NAME>
Username: <DB_USER dari Vault>
Password: <DB_PASSWORD dari Vault>
Schema:   <DB_SCHEMA>
SSL Mode: require
```

**Langkah 2 — Query pertama Anda**

```sql
-- Tampilkan ringkasan 10 record terbaru
-- Aman dijalankan: tidak mengandung PII, tidak ada side effect
SELECT
    <id_field>,
    <kode_field>,
    <nama_singkat_field>,
    <status_field>,
    <jumlah_field>,
    <tanggal_field>
FROM <schema>.<nama_view_atau_tabel>
ORDER BY <tanggal_field> DESC
LIMIT 10;
```

**Langkah 3 — Verifikasi hasilnya**

Anda seharusnya melihat `10 rows` dengan kolom seperti yang terdaftar di atas. Jika tidak ada hasil, cek [Section 5.3 — Error Umum](#53-error-umum--resolusi).

---

### 5.2 Quick Start REST API (Application Developer)

**Langkah 1 — Ambil access token**

```python
import requests
import os

response = requests.post(
    os.environ["API_TOKEN_URL"],
    data={
        "grant_type": "client_credentials",
        "client_id": os.environ["API_CLIENT_ID"],
        "client_secret": os.environ["API_CLIENT_SECRET"],
        "scope": os.environ["API_SCOPE"],
    }
)
response.raise_for_status()
token = response.json()["access_token"]
print("Token berhasil didapat:", token[:20], "...")
```

**Langkah 2 — Panggil endpoint pertama**

```python
import requests

headers = {"Authorization": f"Bearer {token}"}
base_url = os.environ["API_BASE_URL"]

# Ambil 5 record terbaru
resp = requests.get(
    f"{base_url}/<resource>",
    headers=headers,
    params={"per_page": 5, "sort": "<tanggal_field>:desc"}
)
resp.raise_for_status()

data = resp.json()
print(f"Total records tersedia: {data['meta']['total']}")
print(f"Records di halaman ini: {len(data['data'])}")
```

**Langkah 3 — Contoh output yang diharapkan**

```json
{
  "data": [
    {
      "<id_field>": "a1b2c3d4-...",
      "<kode_field>": "KD-001",
      "<status_field>": "aktif",
      "<jumlah_field>": 1500000,
      "<tanggal_field>": "2025-01-15"
    }
  ],
  "meta": {
    "total": 1284750,
    "page": 1,
    "per_page": 5,
    "total_pages": 256950,
    "has_next": true
  }
}
```

*Keterangan field lengkap tersedia di [D-02 Data Contract](../design/data-contract-spec.md) dan [G-01 Kamus Data](../../governance/data-vocabulary-template.md).*

---

### 5.3 Error Umum & Resolusi

| Kode Error / Pesan | Penyebab Paling Umum | Langkah Resolusi |
|---|---|---|
| `FATAL: password authentication failed` | Password DB sudah expired atau salah | Ambil ulang kredensial dari Vault — lihat [Section 3.2](#32-setup-kredensial) |
| `HTTP 401 Unauthorized` | Token expired (lifetime: `<1 jam>`) | Request token baru — lihat [Section 5.2 Langkah 1](#52-quick-start-rest-api-application-developer) |
| `HTTP 403 Forbidden` | Role tidak memiliki akses ke resource/field ini | Cek [G-02 Access Control Matrix](../../governance/data-access-control-matrix.md); ajukan eskalasi via [Section 8](#8-support--eskalasi) |
| `HTTP 429 Too Many Requests` | Melebihi rate limit | Implementasi exponential backoff — lihat [Section 7.3](#73-rate-limits--kuota) |
| `relation "<schema>.<table>" does not exist` | Typo nama schema/tabel, atau schema belum di-set | Jalankan `SET search_path = <schema>;` atau gunakan qualified name |
| `No data returned` | Filter terlalu ketat, atau data memang belum tersedia | Cek jadwal update di [Section 4.2](#42-freshness-data--sla); hapus filter satu per satu |
| `SSL connection required` | SSL Mode tidak dikonfigurasi di client | Set `sslmode=require` di connection string |
| `CONNECTION REFUSED` / `timeout` | VPN tidak aktif atau firewall block | Aktifkan VPN; cek [Section 2.3 Kebutuhan Jaringan](#23-kebutuhan-jaringan) |

---

## 6. Penemuan Data (Data Discovery)

### 6.1 Temukan Dataset yang Tersedia

`[Mandatory]` — *Role: Consumer*

Gunakan **Data Catalog** untuk menjelajahi seluruh data yang tersedia dalam data product ini:

**Link Catalog:** `<https://catalog.domain.org/data-products/<domain>/<product>>`

Di catalog, Anda dapat menemukan:
- Daftar semua tabel / view / endpoint yang tersedia
- Preview data (sample rows)
- Statistik kualitas data terkini
- Lineage: data ini berasal dari mana
- Tag dan klasifikasi

**Navigasi cepat di catalog:**

```
Data Product: <nama-data-product>
  └── Output Ports
       ├── SQL View: <schema>.<view_name>        → Schema, sample data
       ├── REST API: /v1/<resource>               → OpenAPI spec
       └── File Export: s3://bucket/path/         → File listing
```

---

### 6.2 Referensi Schema

Untuk deskripsi setiap kolom secara teknis (nama, tipe data, nullable, constraint), gunakan:

- **D-02 Data Contract:** [data-contract-spec.md](../design/data-contract-spec.md) — Section 4 (Output Port Schema)
- **D-03 Data Contract YAML:** [data-contract.yaml](../design/data-contract.yaml) — Machine-readable, untuk validasi otomatis

**Preview skema utama:**

| Kolom | Tipe | Nullable | Keterangan Singkat |
|---|---|---|---|
| `<id_field>` | `UUID` | `NOT NULL` | Identifier unik record |
| `<kode_field>` | `VARCHAR(20)` | `NOT NULL` | Kode referensi dari sistem sumber |
| `<nama_field>` | `VARCHAR(255)` | `NULL` | `[Restricted: perlu privileged role]` |
| `<status_field>` | `VARCHAR(20)` | `NOT NULL` | Enum — lihat [G-01 Kamus Data](../../governance/data-vocabulary-template.md) untuk nilai valid |
| `<jumlah_field>` | `BIGINT` | `NULL` | Dalam satuan `<Rupiah / unit>` |
| `<tanggal_field>` | `DATE` | `NOT NULL` | Tanggal record |
| `<created_at>` | `TIMESTAMPTZ` | `NOT NULL` | Timestamp insert ke data product |
| `<updated_at>` | `TIMESTAMPTZ` | `NOT NULL` | Timestamp update terakhir |

*Untuk skema lengkap semua tabel / endpoint, lihat [D-02](../design/data-contract-spec.md).*

---

### 6.3 Definisi Semantik & Kamus Data

Untuk memahami **apa yang dimaksud** oleh setiap atribut secara bisnis (bukan hanya tipe teknis), gunakan:

- **G-01 Kamus Data:** [data-vocabulary-template.md](../../governance/data-vocabulary-template.md)
- **G-03 Data Dictionary:** `<link ke G-03 jika sudah ada>`

**Nilai enum yang penting:**

| Kolom | Nilai Valid | Definisi Bisnis |
|---|---|---|
| `<status_field>` | `aktif` | `<Consumer aktif yang sedang menerima manfaat>` |
| `<status_field>` | `nonaktif` | `<Consumer yang telah dinonaktifkan dari program>` |
| `<status_field>` | `pending` | `<Consumer dalam proses verifikasi>` |
| `<tipe_field>` | `<nilai_1>` | `<Definisi>` |

*Daftar lengkap enum dan konteks bisnis setiap nilai ada di [G-01](../../governance/data-vocabulary-template.md).*

---

## 7. Pola Penggunaan & Best Practices

### 7.1 Pola yang Direkomendasikan

`[Mandatory]` — *Ikuti pola berikut untuk performa dan kepatuhan optimal*

#### Pola 1 — Pagination Cursor untuk Dataset Besar (API)

```python
import requests

def fetch_all_records(base_url, token, resource, filters=None):
    """
    Gunakan cursor pagination untuk dataset >10.000 records.
    Hindari offset pagination untuk dataset besar (lambat di server).
    """
    headers = {"Authorization": f"Bearer {token}"}
    params = {"per_page": 1000, **(filters or {})}
    cursor = None
    all_records = []

    while True:
        if cursor:
            params["cursor"] = cursor

        resp = requests.get(f"{base_url}/{resource}", headers=headers, params=params)
        resp.raise_for_status()
        body = resp.json()

        all_records.extend(body["data"])

        cursor = body["meta"].get("next_cursor")
        if not cursor:
            break

    return all_records
```

#### Pola 2 — Incremental Load berdasarkan `updated_at` (SQL)

```sql
-- DIREKOMENDASIKAN: Incremental load hanya record yang berubah
-- Lebih efisien dari full-scan untuk pipeline harian

SELECT *
FROM <schema>.<nama_tabel>
WHERE updated_at > :last_run_timestamp   -- Ganti dengan timestamp run terakhir
  AND updated_at <= :current_run_timestamp
ORDER BY updated_at ASC;

-- Simpan :current_run_timestamp untuk digunakan sebagai
-- :last_run_timestamp di run berikutnya
```

#### Pola 3 — Caching Response API untuk Lookup Data

```python
import functools
import time

# Data referensi (enum, lookup) jarang berubah — cache agresif
# Data transaksional — jangan di-cache atau cache singkat (< 5 menit)

@functools.lru_cache(maxsize=128)
def get_reference_data(endpoint: str) -> dict:
    """Cache data referensi selama runtime."""
    resp = requests.get(f"{base_url}/{endpoint}", headers=headers)
    return resp.json()["data"]
```

---

### 7.2 Anti-Pattern yang Harus Dihindari

:::danger Anti-Pattern — Hindari Ini

**1. `SELECT *` pada tabel besar tanpa filter**
Membebani server dan memperlambat query lain. Selalu gunakan `WHERE`, `LIMIT`, atau filter waktu.

**2. Polling API setiap detik**
Menyebabkan rate limit hit. Gunakan jadwal yang sesuai dengan freshness SLO data ([Section 4.2](#42-freshness-data--sla)).

**3. Menyimpan seluruh dataset di memori**
Untuk dataset >100K baris, gunakan streaming / chunked reads — lihat Pola 1 dan 2 di atas.

**4. JOIN data product ini dengan data eksternal tanpa persetujuan DPO**
Melanggar Data Sharing Agreement dan regulasi privasi.

**5. Hardcode timestamp cut-off yang statis**
Pipeline menjadi rapuh. Selalu buat cut-off dinamis dari run terakhir.
:::

---

### 7.3 Rate Limits & Kuota

`[Mandatory]`

| Consumer Tier | Rate Limit | Burst | Cara Cek Sisa Kuota |
|---|---|---|---|
| Standard (default) | `<100 req/menit>` | `<200 req/menit (10 detik)>` | Header `X-RateLimit-Remaining` |
| Premium (perlu request) | `<1.000 req/menit>` | `<2.000 req/menit>` | Header `X-RateLimit-Remaining` |

**Implementasi exponential backoff saat kena rate limit:**

```python
import time
import requests

def api_call_with_retry(url, headers, max_retries=5):
    for attempt in range(max_retries):
        resp = requests.get(url, headers=headers)

        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 2 ** attempt))
            print(f"Rate limited. Tunggu {retry_after} detik...")
            time.sleep(retry_after)
            continue

        resp.raise_for_status()
        return resp.json()

    raise Exception("Max retries exceeded")
```

**Untuk upgrade ke tier Premium,** ajukan permintaan via `<https://portal.domain.org/rate-limit-upgrade>` dengan justifikasi use case.

---

## 8. Support & Eskalasi

### 8.1 Kanal Support

`[Mandatory]` — *Pilih kanal sesuai jenis isu*

| Jenis Isu | Kanal | SLA Respons | Jam Operasional |
|---|---|---|---|
| Akses ditolak / kredensial tidak berfungsi | Slack: `#dp-<product>-support` | `<2 jam kerja>` | `<08:00–17:00 WIB>` |
| Data tidak fresh / kualitas data mencurigakan | Slack: `#dp-<product>-support` | `<4 jam kerja>` | `<08:00–17:00 WIB>` |
| Bug atau error di API / SQL port | JIRA: `<Project Key>` — label `bug` | `<1 hari kerja>` | `<08:00–17:00 WIB>` |
| Pertanyaan tentang semantik / definisi data | Slack: `#dp-<product>-support` | `<1 hari kerja>` | `<08:00–17:00 WIB>` |
| Request fitur baru / kolom baru | JIRA: `<Project Key>` — label `feature-request` | `<Diproses di sprint berikutnya>` | — |
| **Insiden kritikal** (data hilang / produksi terdampak) | Telepon langsung: `<No. HP On-call DE>` | `<30 menit>` | `<24/7>` |

**Kontak Utama:**

| Role | Nama | Email | Slack |
|---|---|---|---|
| Data Product Owner | `<Nama>` | `<email>` | `@<handle>` |
| Data Steward (harian) | `<Nama>` | `<email>` | `@<handle>` |
| On-call Data Engineer | _Rotasi mingguan_ | `<oncall@domain.org>` | `#dp-oncall` |

---

### 8.2 Cara Melaporkan Insiden Data

`[Mandatory]` — *Ikuti format ini saat melaporkan di Slack atau JIRA*

Sertakan informasi berikut dalam laporan Anda:

```
🚨 DATA INCIDENT REPORT

Data Product  : <domain>/<nama-product>/v<versi>
Waktu Terdeteksi : <YYYY-MM-DD HH:MM WIB>
Dampak        : <Apa yang terdampak — query gagal / data stale / dll.>
Output Port   : <SQL / REST API / File / Kafka>
Ticket Akses  : DAR-XXXX (jika relevan)

Langkah yang sudah dicoba:
1. <...>
2. <...>

Error message (jika ada):
<paste error message di sini>
```

Referensi klasifikasi insiden: [M-07 Operations Runbook](../monitoring/operational-reports.md) — Section Severity Classification.

---

### 8.3 Proses Notifikasi Perubahan

Consumer akan dinotifikasi untuk setiap perubahan yang berdampak pada cara konsumsi data:

| Jenis Perubahan | Kanal Notifikasi | Notice Minimum |
|---|---|---|
| **Breaking change** (hapus kolom, ubah tipe, rename) | Email + Slack + Data Catalog | `<30 hari sebelum>` |
| **Non-breaking change** (tambah kolom baru) | Slack + Data Catalog | `<7 hari sebelum>` |
| **Perubahan SLA / jadwal update** | Email + Slack | `<14 hari sebelum>` |
| **Planned maintenance** (downtime terjadwal) | Slack + Status Page | `<48 jam sebelum>` |
| **Hotfix / patch tanpa downtime** | Slack (info) | Saat deploy |
| **Deprecation data product** | Email + Slack | `<90 hari sebelum sunset>` |

**Subscribe notifikasi:**

```
1. Join channel Slack: #dp-<product>-announce
2. Subscribe di Data Catalog: https://catalog.domain.org/<product> → klik "Watch"
3. Untuk email digest: hubungi Data Steward untuk didaftarkan ke mailing list
```

---

## Annex A — Referensi Kredensial Lengkap

`[Internal — Jangan dibagikan ke pihak yang tidak berwenang]`

| Secret | Lokasi di Vault | Environment Variable | Rotasi |
|---|---|---|---|
| DB Password | `secret/<env>/consumer/<user>/db-password` | `DB_PASSWORD` | `<90 hari>` |
| API Client Secret | `secret/<env>/consumer/<user>/api-secret` | `API_CLIENT_SECRET` | `<180 hari>` |
| Kafka API Key | `secret/<env>/consumer/<user>/kafka-key` | `KAFKA_API_KEY` | `<180 hari>` |

**Rotasi kredensial:**

1. Dapatkan kredensial baru dari Vault sebelum masa berlaku habis
2. Update environment variable / secrets manager di sistem Anda
3. Verifikasi ulang menggunakan prosedur di [Section 3.3](#33-verifikasi-akses)
4. Hapus / revoke kredensial lama jika ada opsi manual rotation

---

## Annex B — Checklist Onboarding Mandiri

Gunakan checklist ini untuk memastikan seluruh proses onboarding Anda selesai:

```
ONBOARDING CHECKLIST — DLV-01
Data Product: <nama-data-product> v<X.Y>
Consumer: <Nama, Tim>
Tanggal mulai: <YYYY-MM-DD>

PRASYARAT
[ ] P-01 — Akun SSO aktif
[ ] P-02 — Justifikasi bisnis terdokumentasi
[ ] P-03 — Data Sharing Agreement ditandatangani
[ ] P-04 — Role IAM di-assign

AKSES & KREDENSIAL
[ ] Permintaan akses diajukan (Ticket: DAR-_____)
[ ] Akses disetujui oleh Data Product Owner
[ ] Kredensial diterima dari Vault
[ ] Verifikasi SQL berhasil (Section 3.3.1)
[ ] Verifikasi REST API berhasil (Section 3.3.2)

PEMAHAMAN DATA
[ ] Membaca Overview Data Product (Section 4)
[ ] Memahami klasifikasi data dan pembatasan
[ ] Mengetahui jadwal update dan SLA freshness
[ ] Mengetahui keterbatasan yang ada (Section 4.4)

OPERASIONAL
[ ] Quick Start berhasil dijalankan (Section 5)
[ ] Schema referensi dipahami (Section 6.2)
[ ] Subscribe ke channel notifikasi (Section 8.3)
[ ] Kontak support disimpan (Section 8.1)

Onboarding selesai: ___________
Diverifikasi oleh Data Steward: ___________
```

---

*Dokumen ini dikelola oleh **<Nama Domain>** dan diperbarui setiap kali ada perubahan pada data product. Untuk melaporkan ketidakakuratan dalam dokumen ini, hubungi Data Steward di [Section 8.1](#81-kanal-support).*
