---
title: "Data API Brief — <Nama API>"
sidebar_label: "API Brief"
sidebar_position: 2
description: "Spesifikasi teknis Data API: konteks, arsitektur, endpoint, SLA performa, keamanan, dan metadata workload"
tags: [development, api, data-engineering, rest-api, openapi]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: development
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Data API Brief

> **Tujuan dokumen ini:** Mendefinisikan spesifikasi teknis API yang menjadi output port dari data product. Dokumen ini melengkapi spesifikasi OpenAPI dan menjadi panduan bagi Data Engineer untuk implementasi.

:::tip Prinsip API Design
1. **Konsisten** — Ikuti konvensi naming dan response format yang ada
2. **Idempoten** — GET requests tidak mengubah state
3. **Versioned** — Perubahan breaking wajib menaikkan versi major
4. **Privacy-safe** — PII di-mask sesuai role konsumen
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Nama API** | `<Nama API yang deskriptif>` |
| **Port ID** | `<urn:dp:<domain>:<product>:port:v1>` |
| **Versi API** | `<v1>` |
| **Base URL Produksi** | `<https://api.<domain>.org/v1>` |
| **Base URL Staging** | `<https://api-staging.<domain>.org/v1>` |
| **OpenAPI Spec** | `<https://api.<domain>.org/v1/openapi.json>` |
| **Engineer Utama** | `<Nama, Email>` |

---

## 1. Konteks & Ruang Lingkup

### 1.1 Permasalahan Bisnis

`[Mandatory]` — *Role: Data Product Owner*

Mengapa API ini dibutuhkan? Apa masalah bisnis yang diselesaikan?

> `[Isi di sini — contoh: "API ini menyediakan akses real-time ke data profil beneficiary sehingga sistem downstream dapat melakukan verifikasi eligibilitas tanpa perlu membaca langsung ke database operasional."]`

### 1.2 Target Konsumen Data

`[Mandatory]` — *Role: Data Analyst*

| Persona / Sistem | Tipe Konsumen | Cara Akses | Frekuensi Panggilan Est. |
|---|---|---|---|
| `<Mobile App>` | `<Machine (System-to-System)>` | `<REST API + OAuth 2.0>` | `<~10K req/jam>` |
| `<Dashboard Tim Analitik>` | `<Human (via browser)>` | `<REST API + JWT>` | `<~500 req/jam>` |
| `<Pipeline Downstream>` | `<Machine>` | `<REST API + API Key>` | `<~50K req/hari (batch)>` |

### 1.3 Sistem Sumber Data (Input)

`[Mandatory]` — *Role: Data Analyst*

| ID | Sumber | Lokasi | Data yang Diekspos |
|---|---|---|---|
| SRC-01 | `<Gold layer database>` | `<<schema>.<table_gold>>` | `<Profil final setelah transformasi>` |
| SRC-02 | `<Reference table>` | `<<schema>.<dim_referensi>>` | `<Lookup values untuk enrichment>` |

### 1.4 Out of Scope

`[Opsional]`

- `<Write operations (POST/PUT/DELETE) — API ini read-only>`
- `<Real-time streaming — gunakan Kafka output port untuk kebutuhan event streaming>`
- `<Bulk export >1 juta record — gunakan file export output port>`

---

## 2. Arsitektur & Spesifikasi API

### 2.1 Tech Stack & Frameworks

`[Opsional]` — *Role: Data Architect*

| Komponen | Teknologi | Versi | Keterangan |
|---|---|---|---|
| `<Framework>` | `<FastAPI / Flask / Django REST>` | `<0.111>` | `<Async-first>` |
| `<API Gateway>` | `<Kong / AWS API Gateway / Nginx>` | `<3.x>` | `<Rate limiting, auth>` |
| `<Auth>` | `<Keycloak / Keycloak>` | `<->` | `<OAuth 2.0 provider>` |
| `<Database>` | `<PostgreSQL / ClickHouse>` | `<16>` | `<Gold layer>` |
| `<Cache>` | `<Redis>` | `<7.x>` | `<Response caching>` |

### 2.2 Interaction Model

`[Mandatory]` — *Role: Data Architect*

| Pola | Digunakan? | Keterangan |
|---|---|---|
| `<Synchronous REST>` | `<[x] Ya>` | `<Request-response standard>` |
| `<GraphQL>` | `<[ ] Tidak>` | `<Tidak diperlukan untuk use case ini>` |
| `<Async Webhook>` | `<[ ] Tidak>` | `<Gunakan Kafka untuk event-driven>` |
| `<gRPC>` | `<[ ] Tidak>` | `<Tidak diperlukan>` |

### 2.3 Spesifikasi Endpoint

`[Mandatory]` — *Role: Data Engineer*

:::info OpenAPI Spec
Dokumentasi endpoint lengkap dalam format OpenAPI ada di: `<https://api.<domain>.org/v1/openapi.json>`
Swagger UI: `<https://api.<domain>.org/v1/docs>`
:::

#### Endpoint 1: List Resource

```
GET /v1/<resource>
```

**Query Parameters:**

| Parameter | Tipe | Required | Default | Deskripsi | Contoh |
|---|---|---|---|---|---|
| `page` | `integer` | No | `1` | Nomor halaman | `?page=2` |
| `per_page` | `integer` | No | `50` | Records per page (max: 200) | `?per_page=100` |
| `status` | `string` | No | `all` | Filter berdasarkan status | `?status=aktif` |
| `updated_since` | `datetime` | No | - | Filter record diupdate sejak | `?updated_since=2024-01-01T00:00:00Z` |
| `search` | `string` | No | - | Full-text search | `?search=kata+kunci` |

**Response 200 (Success):**

```json
{
  "data": [
    {
      "<id>": "<UUID>",
      "<kode_referensi>": "<string>",
      "<nama>": "<string — atau masked jika non-privileged>",
      "<status>": "<aktif|nonaktif|pending>",
      "<jumlah>": "<integer>",
      "<updated_at>": "<ISO 8601 datetime>"
    }
  ],
  "meta": {
    "total": "<integer — total records>",
    "page": "<integer>",
    "per_page": "<integer>",
    "total_pages": "<integer>",
    "has_next": "<boolean>",
    "has_prev": "<boolean>"
  },
  "links": {
    "self": "/v1/<resource>?page=1",
    "next": "/v1/<resource>?page=2",
    "prev": null
  }
}
```

#### Endpoint 2: Get Single Resource

```
GET /v1/<resource>/{id}
```

**Path Parameters:**

| Parameter | Tipe | Required | Deskripsi |
|---|---|---|---|
| `id` | `UUID` | Yes | ID unik resource |

**Response 200 (Success):**

```json
{
  "data": {
    "<id>": "<UUID>",
    "<kode_referensi>": "<string>",
    "<nama>": "<string>",
    "<status>": "<string>",
    "<detail_field_1>": "<value>",
    "<detail_field_2>": "<value>",
    "<created_at>": "<ISO 8601>",
    "<updated_at>": "<ISO 8601>"
  }
}
```

#### Error Responses (Standar untuk Semua Endpoint)

```json
// 400 Bad Request
{
  "error": "VALIDATION_ERROR",
  "message": "Parameter 'status' harus salah satu dari: aktif, nonaktif, pending",
  "details": { "field": "status", "received": "aktiv" }
}

// 401 Unauthorized
{
  "error": "UNAUTHORIZED",
  "message": "Token tidak valid atau kadaluarsa"
}

// 403 Forbidden
{
  "error": "FORBIDDEN",
  "message": "Role Anda tidak memiliki akses ke resource ini"
}

// 404 Not Found
{
  "error": "NOT_FOUND",
  "message": "Resource dengan ID 'xxx' tidak ditemukan"
}

// 429 Too Many Requests
{
  "error": "RATE_LIMIT_EXCEEDED",
  "message": "Melebihi batas 100 request per menit",
  "retry_after": 30
}

// 500 Internal Server Error
{
  "error": "INTERNAL_ERROR",
  "message": "Terjadi kesalahan server. Silakan coba lagi atau hubungi support.",
  "trace_id": "<UUID untuk debugging>"
}
```

---

## 3. SLA Kualitas Performa & Keamanan

### 3.1 Ketersediaan (Uptime)

`[Mandatory]` — *Role: Data Product Owner*

| Metrik | Target | Cara Ukur |
|---|---|---|
| **Uptime bulanan** | `<99.9% (max downtime 43 menit/bulan)>` | `<Synthetic monitoring setiap 1 menit>` |
| **Planned maintenance** | `<Sabtu 02:00–04:00 WIB>` | `<Announced 48 jam sebelumnya>` |

### 3.2 Latensi Respons

`[Mandatory]` — *Role: Data Architect*

| Jenis Request | P50 Target | P95 Target | P99 Target |
|---|---|---|---|
| `<GET /resource (list, no filter)>` | `<50ms>` | `<200ms>` | `<500ms>` |
| `<GET /resource/{id} (single)>` | `<20ms>` | `<100ms>` | `<200ms>` |
| `<GET /resource?search=... (full-text)>` | `<200ms>` | `<500ms>` | `<1s>` |

**Cache strategy:**
- Single resource GET: cached `<5 menit>` di Redis
- List GET: cached `<1 menit>` di Redis
- Cache invalidated saat data di-update

### 3.3 Autentikasi & Access Control

`[Mandatory]` — *Role: Data Architect*

| Flow | Tipe Konsumen | Token | Durasi Token |
|---|---|---|---|
| `<OAuth 2.0 Client Credentials>` | `<Machine (System-to-System)>` | `<JWT (RS256)>` | `<1 jam>` |
| `<OAuth 2.0 Authorization Code>` | `<Human (browser app)>` | `<JWT (RS256)>` | `<15 menit (+ refresh 7 hari)>` |
| `<API Key>` | `<Internal services (trusted)>` | `<API Key header>` | `<Tidak kadaluarsa — rotasi manual>` |

**Token request:**
```bash
# Machine-to-Machine
curl -X POST https://auth.domain.org/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&scope=read:resource"

# Gunakan token:
curl -H "Authorization: Bearer <token>" https://api.domain.org/v1/<resource>
```

### 3.4 Rate Limiting

`[Mandatory]` — *Role: Data Architect*

| Consumer Tier | Rate Limit | Burst Limit | Scope |
|---|---|---|---|
| `<Standard (default)>` | `<100 req/menit>` | `<200 req/menit (10 detik)>` | `<Per consumer>` |
| `<Premium (approved)>` | `<1.000 req/menit>` | `<2.000 req/menit>` | `<Per consumer>` |
| `<Internal service>` | `<10.000 req/menit>` | `<Tidak dibatasi>` | `<Per service>` |

Response headers:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 75
X-RateLimit-Reset: 1714530000
```

### 3.5 Klasifikasi Data & Masking

`[Mandatory]` — *Role: Data Architect*

| Field | Klasifikasi | Perlakuan untuk Standard Role | Perlakuan untuk Privileged Role |
|---|---|---|---|
| `<id, kode, status>` | `<Public>` | `<Tampil penuh>` | `<Tampil penuh>` |
| `<nama>` | `<Internal>` | `<Nama depan saja>` | `<Tampil penuh>` |
| `<nik>` | `<Restricted (PII)>` | `<Masked: "317104******0001">` | `<Tampil penuh>` |
| `<kondisi_kesehatan>` | `<Confidential (PHI)>` | `<Field tidak ada dalam response>` | `<Tampil penuh (medical_role)>` |

### 3.6 Manajemen Rahasia (Secrets Management)

`[Mandatory]` — *Role: Data Engineer*

:::danger Dilarang Hardcode
JANGAN hardcode API keys, client secrets, atau credentials di kode sumber.
:::

| Secret | Path di Vault / SSM | Cara Inject |
|---|---|---|
| `<DB connection string>` | `<secret/prod/domain/product/api-db-conn>` | `<Environment variable via k8s secret>` |
| `<OAuth client secret>` | `<secret/prod/domain/product/oauth-client>` | `<Environment variable via k8s secret>` |
| `<Redis connection>` | `<secret/prod/domain/product/redis-conn>` | `<Environment variable>` |

---

## 4. Metadata Workload (DPDS)

`[Mandatory]` — *Role: Data Engineer + Data Product Owner*

```yaml
# ---------------------------------------------------------------
# DATA PRODUCT DESCRIPTOR — API Workload
# ---------------------------------------------------------------

Port_ID: "urn:dp:<domain>:<product>:port:api:v1"
Name: "<Nama API>"
Description: "<Deskripsi singkat fungsi API>"
Business_Owner: "<email@domain.org>"
OutputPortType: "REST API"

DataContract:
  Schema_Reference: "<https://api.domain.org/v1/openapi.json>"
  SLA:
    UpTime: "99.9%"
    Max_Latency_P95: "200ms"
    Rate_Limit: "100 req/menit per consumer"
  DataSharingAgreement:
    IntendedUsage: "<Tujuan penggunaan API ini>"
    Security_Requirements: "OAuth 2.0 Client Credentials. PII masking aktif sesuai role."
    Versioning: "SemVer. Breaking changes: minimum 3 bulan notice."

Observability:
  HealthCheck: "<https://api.domain.org/v1/health>"
  Metrics: "<https://monitoring.domain.org/api/<product>>"
  Logs: "<https://logs.domain.org/api/<product>>"
```
