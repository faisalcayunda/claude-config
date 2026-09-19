---
title: "Data Contract & Interface Specification — <Nama Data Product>"
sidebar_label: "Data Contract Spec"
sidebar_position: 2
description: "Kontrak formal antara produsen dan konsumen data yang mendefinisikan schema, SLO, SLA, dan kebijakan"
tags: [design, data-contract, interface, slo, sla]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: design
version: "1.0.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Data Contract & Interface Specification

> **Tujuan dokumen ini:** Mendefinisikan perjanjian formal dan mengikat antara **Produsen Data** (tim domain pemilik data product) dan **Konsumen Data** (tim yang menggunakan data product). Dokumen ini menjadi dasar kepercayaan (*trustworthiness*) data product.

:::info Hubungan dengan Data Contract YAML
Dokumen ini adalah **narasi formal** dari kontrak. File YAML yang dapat dieksekusi secara komputasional ada di: `../design/data-contract.yaml`. Kedua dokumen harus sinkron.
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi Perubahan | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 1.0 | Versi pertama yang disetujui | `<Nama>` |

---

## Definisi Umum

| Atribut | Nilai |
|---|---|
| **Nama Data Product** | `<Nama Data Product>` |
| **Domain** | `<Nama Domain>` |
| **Versi Kontrak** | `<1.0.0>` |
| **Produsen Data** | `<Nama Tim Domain>` |
| **Pemilik Kontrak** | `<Nama Data Product Owner, Email>` |
| **Konsumen Utama** | `<Nama Tim / Sistem Consumer>` |
| **Klasifikasi Keamanan** | `<Public / Internal / Restricted / Confidential>` |
| **Tanggal Efektif** | `<YYYY-MM-DD>` |
| **Tanggal Kadaluarsa** | `<YYYY-MM-DD atau "Sampai digantikan versi baru">` |

---

## 1. Definisi Skema & Semantik Data

`[Mandatory]` — *Role: Data Architect + Domain Expert*

> Kontrak ini menjamin bahwa Produsen Data akan menyediakan tabel/API/stream sesuai format yang telah disepakati. Jika terdapat perubahan yang memutus kompatibilitas (*breaking changes*), Produsen **wajib** memberikan notifikasi minimum `<X bulan>` sebelumnya.

### 1.1 Output Port: `<Nama Port 1>` *(Tipe: Tabel/API/Stream/File)*

**Deskripsi:** `<Apa yang disediakan oleh output port ini>`

**Schema:**

| Field/Atribut | Tipe Data | Key | Nullable | Deskripsi Bisnis | PII | Contoh Value |
|---|---|---|---|---|---|---|
| `<field_name>` | `<VARCHAR(36)>` | `<PK>` | `<No>` | `<Definisi bisnis>` | `<No>` | `<"abc-123-...">` |
| `<field_name>` | `<DATE>` | | `<No>` | `<Definisi bisnis>` | `<No>` | `<"2024-01-15">` |
| `<field_name>` | `<VARCHAR(16)>` | `<AK>` | `<No>` | `<NIK Nasional>` | `<Ya - Restricted>` | `<"317XXXXXXXXXX001">` |
| | | | | | | |

**Constraints & Business Rules:**
- `<CONSTRAINT 1: field_x MUST be >= 0>`
- `<CONSTRAINT 2: status IN ('aktif', 'nonaktif', 'pending')>`
- `<CONSTRAINT 3: tanggal_lahir < CURRENT_DATE>`

*(Duplikasi seksi ini untuk setiap output port)*

### 1.2 Output Port: `<Nama Port 2>` *(Tipe: REST API)*

**Base URL:** `<https://api.domain.org/v1/resource>`

**Authentication:** `<OAuth 2.0 Client Credentials / API Key / mTLS>`

**Endpoints:**

| Method | Path | Deskripsi | Response Format |
|---|---|---|---|
| `GET` | `</resource>` | `<List semua resource>` | `<JSON array>` |
| `GET` | `</resource/{id}>` | `<Detail satu resource>` | `<JSON object>` |
| `POST` | `</resource/query>` | `<Query dengan filter>` | `<JSON array>` |

**Response Schema:**
```json
{
  "data": [
    {
      "<field>": "<tipe dan deskripsi>",
      "<field>": "<tipe dan deskripsi>"
    }
  ],
  "meta": {
    "total": "<integer — total records>",
    "page": "<integer — halaman saat ini>",
    "per_page": "<integer>"
  }
}
```

---

## 2. Service Level Indicators (SLI) & Service Level Objectives (SLO)

`[Mandatory]` — *Role: Data Product Owner + Data Architect*

> SLO adalah **target yang dijanjikan**. SLI adalah cara mengukurnya. Konsumen berhak menuntut eskalasi jika SLO dilanggar secara konsisten.

### 2.1 Kemutakhiran Data (Freshness)

- **SLI:** Latensi antara data tersedia di sumber hingga data tersedia di output port.
- **SLO:** `<99% dari batch harian tersedia sebelum pukul XX:00 WIB>` *atau* `<Latensi streaming < X menit (P95)>`
- **Cara Ukur:** `<Monitoring pipeline + alerting di Airflow/Grafana>`

### 2.2 Ketersediaan (Availability)

- **SLI:** Persentase waktu output port berhasil merespons permintaan baca.
- **SLO:** `<99.9% per bulan (maksimal downtime terencana 43 menit/bulan)>`
- **Maintenance Window:** `<Sabtu 02:00–04:00 WIB (2 jam terjadwal)>`

### 2.3 Kelengkapan (Completeness)

- **SLI:** Persentase kolom mandatory yang tidak null pada tabel output.
- **SLO:** `<>99.5% kolom mandatory terisi>`
- **Cara Ukur:** `<Great Expectations suite: expect_column_values_to_not_be_null>`

### 2.4 Keunikan (Uniqueness)

- **SLI:** Persentase record yang tidak duplikat berdasarkan business key.
- **SLO:** `<100% tidak ada duplikat pada primary key>`
- **Cara Ukur:** `<dbt test: unique(kolom_id)>`

### 2.5 Validitas (Validity)

- **SLI:** Persentase record yang lolos semua format/range/referential integrity checks.
- **SLO:** `<>99% record valid>`
- **Cara Ukur:** `<Great Expectations: expect_column_values_to_match_regex, expect_column_values_to_be_between>`

### 2.6 Performa Query (jika API/SQL)

- **SLI:** Waktu respons query P95.
- **SLO:** `<Sub-200ms untuk query standar (P95)>` atau `<Sub-5 detik untuk query aggregasi besar>`
- **Cara Ukur:** `<API latency monitoring / Query execution time log>`

---

## 3. Service Level Agreement (SLA) & Error Budget

`[Mandatory]` — *Role: Data Product Owner + PM*

> SLA mendefinisikan **konsekuensi operasional** jika SLO tidak terpenuhi. Ini bukan pinalti finansial, tetapi *operational commitment*.

### 3.1 Error Budget Policy

| Dimensi | Error Budget (Per Bulan) | Konsekuensi Jika Budget Habis |
|---|---|---|
| Freshness | `<0.5% keterlambatan yang diizinkan>` | `<Feature freeze + investigasi root cause>` |
| Availability | `<0.1% downtime = 43 menit>` | `<Post-mortem wajib dalam 48 jam>` |
| Completeness | `<0.5% missing data diizinkan>` | `<Prioritas perbaikan pipeline T+1>` |
| Uniqueness | `<0% duplikat diizinkan>` | `<Immediate incident response + rollback>` |

### 3.2 Support SLA

| Tingkat Insiden | Definisi | Waktu Respons | Waktu Resolusi |
|---|---|---|---|
| **P1 - Critical** | Data tidak tersedia / corruption total | `<1 jam>` | `<4 jam>` |
| **P2 - High** | SLO breached, konsumen terdampak | `<2 jam>` | `<8 jam>` |
| **P3 - Medium** | Degradasi performa, SLO near-breach | `<4 jam>` | `<24 jam>` |
| **P4 - Low** | Pertanyaan, minor issues | `<1 hari kerja>` | `<5 hari kerja>` |

### 3.3 Eskalasi

| Level | Kondisi | Kontak |
|---|---|---|
| L1 | Insiden P3-P4 | `<Tim Data Engineering — Slack: #data-product-support>` |
| L2 | Insiden P1-P2 atau SLA breach | `<Data Product Owner — `<email/no HP>``>` |
| L3 | Eskalasi governance | `<Chief Data Officer / Governance Council>` |

---

## 4. Keamanan & Tata Kelola Komputasional

`[Mandatory]`

### 4.1 Access Control (RBAC)

| Role | Deskripsi | Level Akses | Masking | Cara Request |
|---|---|---|---|---|
| `<admin_role>` | `<Tim Data Engineering>` | `<Full>` | `<None>` | `<By default>` |
| `<read_role>` | `<Tim Consumer A>` | `<Read-only Gold>` | `<PII masked>` | `<Submit request + DPO approval>` |
| `<api_consumer>` | `<Sistem Consumer B>` | `<Output port only>` | `<Per contract>` | `<OAuth client credentials>` |
| `<audit_role>` | `<Tim Internal Audit>` | `<Read-only all>` | `<None>` | `<Security team approval>` |

### 4.2 Data Masking Policy

| Kolom | Klasifikasi | Masking Rule | Visible Penuh kepada |
|---|---|---|---|
| `<nik>` | `<PII - Restricted>` | `<Tampilkan 6 digit pertama, masking sisanya: "317104******0001">` | `<admin_role>` |
| `<nama>` | `<PII - Internal>` | `<Tampilkan nama depan saja>` | `<read_role+>` |
| `<diagnosis>` | `<PHI - Confidential>` | `<Sembunyikan sepenuhnya>` | `<medical_role only>` |

### 4.3 Audit Trail

> Semua akses ke data dengan klasifikasi Restricted atau Confidential akan dicatat secara otomatis meliputi: *who* (identitas pengguna), *what* (data yang diakses), *when* (timestamp), *where* (IP/sistem asal).

---

## 5. Kebijakan Evolusi Kontrak (Versioning Policy)

`[Mandatory]`

### 5.1 Semantic Versioning

Data product ini menggunakan **Semantic Versioning (SemVer)** format `MAJOR.MINOR.PATCH`:

| Tipe Perubahan | Versi yang Berubah | Contoh | Notifikasi Consumer |
|---|---|---|---|
| **Non-breaking** (tambah kolom baru, default baru) | `PATCH / MINOR` | `1.0.1 / 1.1.0` | Best-effort, 2 minggu |
| **Breaking** (hapus kolom, ubah tipe data, rename field) | `MAJOR` | `2.0.0` | **Wajib minimum `<3 bulan>`** |
| **Deprecation** (kontrak ini akan digantikan) | Deprecated flag | - | **Wajib minimum `<6 bulan>`** |

### 5.2 Backward Compatibility Guarantee

- Versi `MINOR` dan `PATCH` dijamin backward compatible.
- Versi `MAJOR` sebelumnya akan tetap tersedia selama `<3 bulan>` *sunset period*.
- Selama sunset period, kedua versi berjalan paralel.

### 5.3 Breaking Change Process

```
1. Buat versi baru (MAJOR bump) → Deploy parallel dengan versi lama
2. Notifikasi semua registered consumer → via email + catalog announcement
3. Consumer migration period (minimum 3 bulan)
4. Sunset announcement (1 bulan sebelum versi lama ditutup)
5. Versi lama dinonaktifkan
```

---

## 6. Sign-Off Kontrak

`[Mandatory sebelum Development dimulai]`

| Pihak | Nama | Role | Persetujuan | Tanggal |
|---|---|---|---|---|
| Produsen | `<Nama>` | Data Product Owner | `☐ Setuju / ☐ Perlu Revisi` | |
| Konsumen Utama | `<Nama>` | `<Lead Consumer Team>` | `☐ Setuju / ☐ Perlu Revisi` | |
| Data Architect | `<Nama>` | Data Architect | `☐ Setuju / ☐ Perlu Revisi` | |
| Governance | `<Nama>` | Data Steward / Legal | `☐ Setuju / ☐ Perlu Revisi` | |

**Catatan Persetujuan:**
> `[Isi catatan khusus jika ada]`
