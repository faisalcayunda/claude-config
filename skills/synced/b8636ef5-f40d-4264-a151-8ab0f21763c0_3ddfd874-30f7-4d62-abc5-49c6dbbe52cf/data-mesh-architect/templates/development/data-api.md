---
title: "Data API — <Nama API>"
sidebar_label: "Data API"
sidebar_position: 6
description: "Dokumentasi implementasi API data: endpoint aktual, autentikasi, skema request/response, rate limiting, dan panduan integrasi."
tags: [development, api, implementation, rest-api, openapi]
doc_id: "V-06"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: development
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Data API

> **Tujuan dokumen ini:** Dokumentasi API yang sudah di-deploy dan aktif. Dokumen ini adalah "living reference" bagi consumer dan integrator — selalu mencerminkan state API di production saat ini.

:::note V-06 vs V-02
**V-02 API Brief** = Spesifikasi desain *sebelum* implementasi (kontrak, arsitektur, SLA yang direncanakan).
**V-06 Data API** = Dokumentasi implementasi *aktual* yang sudah berjalan di production, lengkap dengan contoh nyata.
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Dokumentasi awal post-deployment | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `V-06` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Nama API** | `<Nama API>` |
| **API Version** | `v<N>` |
| **Status** | `<Stable \| Beta \| Deprecated>` |
| **Base URL (Production)** | `https://api.<domain>.org/v<N>` |
| **Base URL (Staging)** | `https://api-staging.<domain>.org/v<N>` |
| **OpenAPI Spec** | `https://api.<domain>.org/v<N>/openapi.json` |
| **Swagger UI** | `https://api.<domain>.org/v<N>/docs` |
| **Engineer Utama** | `<Nama, Email>` |
| **Dokumen terkait** | [V-02 API Brief](./api-brief.md) · [D-02 Data Contract](../design/data-contract-spec.md) · [G-02 Access Control](../../governance/data-access-control-matrix.md) · [DLV-01 Onboarding](../../delivery/consumer-onboarding-guide.md) |

---

## 1. Reference Data

### 1.1 Endpoints Aktif

`[Mandatory]` — *Update setiap kali ada endpoint baru atau deprecated*

| Method | Path | Deskripsi | Auth | Status |
|---|---|---|---|---|
| `GET` | `/v<N>/<resource>` | List resources dengan pagination | Bearer token | `Stable` |
| `GET` | `/v<N>/<resource>/{id}` | Get single resource by ID | Bearer token | `Stable` |
| `GET` | `/v<N>/<resource>/bulk` | Bulk export (max 10K rows) | Bearer token | `Stable` |
| `GET` | `/v<N>/health` | Health check | None | `Stable` |
| `GET` | `/v<N>/metrics` | Operational metrics (internal) | API Key | `Stable` |
| `GET` | `/v<N>/<resource>/stream` | Server-Sent Events stream | Bearer token | `Beta` |

### 1.2 Autentikasi dan Otorisasi

`[Mandatory]`

| Flow | Tipe Consumer | Token | Lifetime | Cara Mendapatkan |
|---|---|---|---|---|
| OAuth 2.0 Client Credentials | Machine (System-to-System) | JWT RS256 | 1 jam | `POST /oauth/token` di `auth.<domain>.org` |
| OAuth 2.0 Authorization Code | Human (via browser) | JWT RS256 | 15 menit + refresh 7 hari | Redirect flow via SSO |
| API Key | Internal trusted services | Static key di header `X-API-Key` | 180 hari (rotasi manual) | Vault: `secret/<env>/<domain>/api-key` |

**Mendapatkan token (Machine-to-Machine):**

```bash
curl -s -X POST https://auth.<domain>.org/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=${API_CLIENT_ID}" \
  -d "client_secret=${API_CLIENT_SECRET}" \
  -d "scope=read:<resource>"
```

### 1.3 Rate Limits dan Kuota

| Consumer Tier | Limit | Burst (10 detik) | Header Response |
|---|---|---|---|
| Standard | 100 req/menit | 200 req | `X-RateLimit-Remaining` |
| Premium | 1.000 req/menit | 2.000 req | `X-RateLimit-Remaining` |
| Internal | 10.000 req/menit | Unlimited | — |

### 1.4 SLA Aktual (Production)

| Metrik | Target SLA | Aktual (30 hari terakhir) | Status |
|---|---|---|---|
| Uptime | ≥ 99.9% | `<___.__ %>` | `<✅ / ⚠️ / ❌>` |
| Latency P50 | ≤ 50ms | `<___>ms` | `<✅ / ⚠️ / ❌>` |
| Latency P95 | ≤ 500ms | `<___>ms` | `<✅ / ⚠️ / ❌>` |
| Latency P99 | ≤ 1.000ms | `<___>ms` | `<✅ / ⚠️ / ❌>` |
| Error Rate | ≤ 0.1% | `<___.__ %>` | `<✅ / ⚠️ / ❌>` |

---

## 2. Spesifikasi Endpoint

### 2.1 `GET /v<N>/<resource>` — List Resources

**Query Parameters:**

| Parameter | Tipe | Required | Default | Keterangan |
|---|---|---|---|---|
| `page` | integer | No | `1` | Halaman (offset-based, max 1.000 halaman) |
| `per_page` | integer | No | `50` | Records per halaman (max: `200`) |
| `cursor` | string | No | — | Cursor untuk cursor-based pagination (lebih efisien untuk dataset besar) |
| `<filter_field>` | string | No | — | Filter by nilai field. Contoh: `?status=aktif` |
| `updated_since` | ISO 8601 | No | — | Hanya records yang diupdate sejak timestamp ini |
| `sort` | string | No | `<tanggal_field>:desc` | Format: `field:asc\|desc` |

**Response 200:**

```json
{
  "data": [
    {
      "<id_field>": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "<kode_field>": "KD-001",
      "<status_field>": "aktif",
      "<jumlah_field>": 1500000,
      "<tanggal_field>": "2025-01-15",
      "updated_at": "2025-01-15T08:30:00+07:00"
    }
  ],
  "meta": {
    "total": 1284750,
    "page": 1,
    "per_page": 50,
    "total_pages": 25695,
    "has_next": true,
    "has_prev": false,
    "next_cursor": "eyJpZCI6IjEyMzQ1In0="
  },
  "links": {
    "self":  "/v<N>/<resource>?page=1",
    "next":  "/v<N>/<resource>?cursor=eyJpZCI6IjEyMzQ1In0=",
    "prev":  null
  }
}
```

---

### 2.2 `GET /v<N>/<resource>/{id}` — Get Single Resource

**Path Parameters:**

| Parameter | Tipe | Keterangan |
|---|---|---|
| `id` | UUID | ID unik resource |

**Response 200:**

```json
{
  "data": {
    "<id_field>": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "<kode_field>": "KD-001",
    "<status_field>": "aktif",
    "<jumlah_field>": 1500000,
    "<tanggal_field>": "2025-01-15",
    "<detail_1>": "<nilai>",
    "<detail_2>": "<nilai>",
    "created_at": "2024-06-01T09:00:00+07:00",
    "updated_at": "2025-01-15T08:30:00+07:00"
  }
}
```

**Response 404:**

```json
{
  "error": "NOT_FOUND",
  "message": "Resource dengan ID 'a1b2c3d4-...' tidak ditemukan",
  "request_id": "req_xyz123"
}
```

---

### 2.3 `GET /v<N>/<resource>/bulk` — Bulk Export

:::warning Batas Bulk Export
Endpoint ini dibatasi **10.000 records per request**. Untuk dataset lebih besar, gunakan pagination cursor di endpoint List atau output port File Export.
:::

**Query Parameters:** Sama dengan endpoint List, ditambah:

| Parameter | Tipe | Required | Keterangan |
|---|---|---|---|
| `format` | string | No | `json` (default) atau `csv` |
| `fields` | string | No | Comma-separated field names untuk partial response |

---

### 2.4 Error Reference (Semua Endpoint)

| HTTP Status | Kode Error | Penyebab | Solusi |
|---|---|---|---|
| `400` | `VALIDATION_ERROR` | Parameter tidak valid | Periksa format parameter; lihat pesan detail |
| `401` | `UNAUTHORIZED` | Token expired atau tidak valid | Request token baru via `/oauth/token` |
| `403` | `FORBIDDEN` | Role tidak memiliki akses ke resource/field ini | Hubungi [DLV-01 §3.1](../../delivery/consumer-onboarding-guide.md) untuk eskalasi akses |
| `404` | `NOT_FOUND` | Resource tidak ditemukan | Verifikasi ID; resource mungkin sudah dihapus |
| `429` | `RATE_LIMIT_EXCEEDED` | Melebihi rate limit | Implementasi exponential backoff; lihat header `Retry-After` |
| `500` | `INTERNAL_ERROR` | Server error | Coba lagi; jika persisten, laporkan `request_id` ke support |
| `503` | `SERVICE_UNAVAILABLE` | Maintenance atau overload | Cek status page: `https://status.<domain>.org` |

---

## 3. Skema Data

### 3.1 Mapping Field ke Data Contract

`[Mandatory]` — *Setiap field di response harus terdaftar di D-02*

| Field (API) | Tipe | Nullable | Klasifikasi | Perlakuan per Role | Referensi |
|---|---|---|---|---|---|
| `<id_field>` | `string (UUID)` | No | `Internal` | Tampil penuh | [D-02 §4.1](../design/data-contract-spec.md) |
| `<kode_field>` | `string` | No | `Internal` | Tampil penuh | [D-02 §4.1](../design/data-contract-spec.md) |
| `<nama_field>` | `string` | Yes | `Internal` | `Standard`: nama depan saja · `Privileged`: penuh | [G-02](../../governance/data-access-control-matrix.md) |
| `<nik_field>` | `string` | Yes | `Restricted (PII)` | `Standard`: masked `"317104******0001"` · `Privileged`: penuh | [G-02](../../governance/data-access-control-matrix.md) |
| `<jumlah_field>` | `integer` | Yes | `Internal` | Tampil penuh | [D-02 §4.1](../design/data-contract-spec.md) |
| `<status_field>` | `string (enum)` | No | `Internal` | Tampil penuh | [G-01 §Status](../../governance/data-vocabulary-template.md) |
| `updated_at` | `string (ISO 8601)` | No | `Internal` | Tampil penuh | — |

### 3.2 Enum Values untuk `<status_field>`

| Nilai | Label Bisnis | Keterangan |
|---|---|---|
| `aktif` | Aktif | Record aktif dan valid |
| `nonaktif` | Tidak Aktif | Dinonaktifkan dari sistem |
| `pending` | Menunggu | Dalam proses verifikasi |
| `<nilai lain>` | `<label>` | `<keterangan>` |

*Daftar lengkap: [G-01 Kamus Data](../../governance/data-vocabulary-template.md)*

---

## 4. Panduan Integrasi

### 4.1 Python Client (Direkomendasikan)

```python
"""
Contoh integrasi Python — production-ready dengan retry dan token refresh.
Copy ke project Anda dan sesuaikan environment variables.
"""
import os
import time
import requests
from functools import lru_cache

BASE_URL  = os.environ["API_BASE_URL"]   # https://api.<domain>.org/v<N>
TOKEN_URL = os.environ["API_TOKEN_URL"]  # https://auth.<domain>.org/oauth/token

_token_cache = {"token": None, "expires_at": 0}

def get_token() -> str:
    if time.time() < _token_cache["expires_at"] - 60:
        return _token_cache["token"]
    resp = requests.post(TOKEN_URL, data={
        "grant_type": "client_credentials",
        "client_id":     os.environ["API_CLIENT_ID"],
        "client_secret": os.environ["API_CLIENT_SECRET"],
        "scope":         os.environ["API_SCOPE"],
    })
    resp.raise_for_status()
    body = resp.json()
    _token_cache["token"]      = body["access_token"]
    _token_cache["expires_at"] = time.time() + body["expires_in"]
    return _token_cache["token"]

def api_get(path: str, params: dict = None, retries: int = 3) -> dict:
    for attempt in range(retries):
        resp = requests.get(
            f"{BASE_URL}{path}",
            headers={"Authorization": f"Bearer {get_token()}"},
            params=params,
            timeout=10,
        )
        if resp.status_code == 429:
            time.sleep(int(resp.headers.get("Retry-After", 2 ** attempt)))
            continue
        if resp.status_code == 401:
            _token_cache["expires_at"] = 0      # force refresh
            continue
        resp.raise_for_status()
        return resp.json()
    raise RuntimeError(f"API call to {path} failed after {retries} retries")

def fetch_all(resource: str, filters: dict = None):
    """Fetch semua records menggunakan cursor pagination."""
    params = {"per_page": 500, **(filters or {})}
    while True:
        body = api_get(f"/{resource}", params)
        yield from body["data"]
        cursor = body["meta"].get("next_cursor")
        if not cursor:
            break
        params = {"cursor": cursor, "per_page": 500}
```

### 4.2 Incremental Load Pattern (untuk Pipeline)

```python
from datetime import datetime, timedelta

def incremental_load(resource: str, last_run: datetime) -> list:
    """
    Load hanya records yang berubah sejak last_run.
    Simpan timestamp run sekarang untuk digunakan sebagai last_run berikutnya.
    """
    current_run = datetime.utcnow()
    records = list(fetch_all(resource, filters={
        "updated_since": last_run.isoformat() + "Z"
    }))
    print(f"Loaded {len(records)} updated records since {last_run}")
    return records, current_run
```

### 4.3 Power BI / Tableau Integration

**Power BI (menggunakan Web connector):**

1. Get Data → Web → URL: `https://api.<domain>.org/v<N>/<resource>?per_page=200`
2. Add header: `Authorization: Bearer <token>`
3. Untuk refresh otomatis: gunakan Power BI Gateway dengan stored credentials

**Tableau (menggunakan Web Data Connector):**

1. Connect → Other → Web Data Connector
2. URL: `<link ke WDC jika disediakan, atau gunakan REST API connector>`

---

## 5. Versioning dan Deprecation

### 5.1 Kebijakan Versioning

| Tipe Perubahan | Contoh | Versi yang Naik | Notice |
|---|---|---|---|
| Breaking | Hapus field, ubah tipe, rename endpoint | **MAJOR** (v1 → v2) | ≥ 90 hari sebelum |
| Non-breaking additive | Tambah field baru, tambah endpoint | **MINOR** (v1.1 → v1.2) | 7 hari sebelum |
| Bug fix / data fix | Perbaikan nilai tanpa perubahan skema | **PATCH** | Immediate |

### 5.2 Versi yang Aktif

| Versi | Status | Sunset Date | Pengganti |
|---|---|---|---|
| `v<N>` | `Stable (current)` | — | — |
| `v<N-1>` | `Deprecated` | `<YYYY-MM-DD>` | Migrasi ke `v<N>` |

*Changelog lengkap: [M-06 Change Log](../monitoring/change-log.md)*

---

## Annex A — OpenAPI Spec

Spesifikasi OpenAPI lengkap tersedia di:

- **JSON:** `https://api.<domain>.org/v<N>/openapi.json`
- **YAML:** `https://api.<domain>.org/v<N>/openapi.yaml`
- **Swagger UI (interaktif):** `https://api.<domain>.org/v<N>/docs`
- **File di repo:** `design/openapi-v<N>.yaml`

## Annex B — Postman Collection

```bash
# Import collection ke Postman
curl -o dp-<product>-api.postman_collection.json \
  https://api.<domain>.org/v<N>/postman-collection.json
```

Atau import manual dari: `<https://www.postman.com/collections/<collection-id>>`

## Annex C — Health Check dan Status

| Endpoint | Tujuan | Autentikasi |
|---|---|---|
| `GET /v<N>/health` | Liveness check | None |
| `GET /v<N>/health/ready` | Readiness check (koneksi DB OK) | None |
| `GET /v<N>/metrics` | Prometheus metrics | API Key (internal) |

Status page: `https://status.<domain>.org/services/dp-<product>-api`
