---
title: "Self-Service Infrastructure Guide — <Nama Data Product>"
sidebar_label: "Self-Service Infra Guide"
sidebar_position: 2
description: "Panduan infrastruktur mandiri bagi consumer: provisioning workload, konfigurasi monitoring, scaling, rotasi credentials, troubleshooting, dan decommission."
tags: [delivery, self-service, infrastructure, consumer, devops]
doc_id: "DLV-02"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: delivery
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Self-Service Infrastructure Guide

> **Tujuan dokumen ini:** Memandu consumer yang sudah onboarding untuk mengoperasikan infrastruktur konsumsinya secara mandiri — deploy workload, konfigurasi monitoring, scaling, dan troubleshooting — tanpa perlu membuka tiket ke tim Data Engineering.

:::note DLV-02 vs DLV-01
**DLV-01 Consumer Onboarding Guide** = Panduan dari zero sampai first successful query.
**DLV-02 Self-Service Infrastructure Guide** = Panduan operasional setelah onboarding — untuk consumer yang ingin mengelola infrastruktur konsumsinya sendiri.
Prasyarat: selesaikan [DLV-01](./consumer-onboarding-guide.md) terlebih dahulu.
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
| **Doc ID** | `DLV-02` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **Target Audience** | Consumer dengan technical background (DE / SRE / DevOps di sisi consumer) |
| **Platform Engineer** | `<Nama, Email>` |
| **Dokumen terkait** | [DLV-01 Consumer Onboarding](./consumer-onboarding-guide.md) · [V-06 Data API](../development/data-api.md) · [M-07 Operations Runbook](../monitoring/operations-runbook.md) · [M-06 Change Log](../monitoring/change-log.md) |

---

## 1. Pendahuluan

### 1.1 Target Audience

| Persona | Pengetahuan yang Diasumsikan |
|---|---|
| **Platform Engineer (Consumer)** | Kubernetes / Docker, cloud console, monitoring tools |
| **Data Engineer (Consumer)** | Python, SQL, Airflow atau workflow tool lain, REST API |

### 1.2 Batas Self-Service

| Aksi | Self-Service? | Cara |
|---|---|---|
| Deploy consumer workload baru | ✅ | Section 3 |
| Konfigurasi monitoring dan alert | ✅ | Section 4 |
| Rotasi credentials | ✅ | Section 5 |
| Scale resource | ✅ | Section 3.3 |
| Upgrade rate limit tier | ⚠️ Via portal | `https://portal.<domain>.org/rate-limit-upgrade` |
| Akses data Restricted / Confidential | ❌ Butuh approval | [DLV-01 §3.1](./consumer-onboarding-guide.md) |
| Perubahan SLA atau skema | ❌ Hubungi DPO | `#dp-<product>-support` |

---

## 2. Reference Data

### 2.1 Environment Inventory

| Environment | Base URL API | Auth URL | Tujuan |
|---|---|---|---|
| Production | `https://api.<domain>.org/v<N>` | `https://auth.<domain>.org/oauth/token` | Workload produksi |
| Staging | `https://api-staging.<domain>.org/v<N>` | `https://auth-staging.<domain>.org/oauth/token` | Testing integrasi |

### 2.2 Default Configuration Parameters

| Parameter | Default | Range Valid | Keterangan |
|---|---|---|---|
| `connection_pool_size` | `5` | `1–20` | Koneksi SQL paralel per instance |
| `api_timeout_seconds` | `30` | `5–120` | Timeout per API request |
| `api_retry_count` | `3` | `1–5` | Max retry sebelum exception |
| `batch_size` | `500` | `10–1000` | Records per API call |

### 2.3 Capacity Planning

| Volume Data (rows/hari) | CPU | Memory | Catatan |
|---|---|---|---|
| < 100K | 0.5 vCPU | 512 MB | Single container |
| 100K – 1M | 1 vCPU | 2 GB | Standard |
| 1M – 10M | 2 vCPU | 4 GB | Gunakan parallelism |
| > 10M | 4+ vCPU | 8+ GB | Konsultasi Platform Engineer domain |

---

## 3. Provisioning Consumer Workload

### 3.1 Setup Pipeline Consumer (Python)

**Langkah 1 — Environment file**

```bash
# .env — JANGAN commit ke Git
API_BASE_URL=https://api.<domain>.org/v<N>
API_TOKEN_URL=https://auth.<domain>.org/oauth/token
API_CLIENT_ID=<dari Vault>
API_CLIENT_SECRET=<dari Vault>
API_SCOPE=read:<resource>
```

**Langkah 2 — Template pipeline incremental**

```python
import os, time, requests, pandas as pd
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

_token_cache = {"token": None, "expires_at": 0}

def get_token() -> str:
    if time.time() < _token_cache["expires_at"] - 60:
        return _token_cache["token"]
    resp = requests.post(os.environ["API_TOKEN_URL"], data={
        "grant_type": "client_credentials",
        "client_id":     os.environ["API_CLIENT_ID"],
        "client_secret": os.environ["API_CLIENT_SECRET"],
        "scope":         os.environ["API_SCOPE"],
    })
    resp.raise_for_status()
    body = resp.json()
    _token_cache.update({"token": body["access_token"],
                         "expires_at": time.time() + body["expires_in"]})
    return _token_cache["token"]

def fetch_incremental(resource: str, since: datetime):
    headers = {"Authorization": f"Bearer {get_token()}"}
    params  = {"updated_since": since.isoformat() + "Z", "per_page": 500}
    records = []
    while True:
        resp = requests.get(
            f"{os.environ['API_BASE_URL']}/{resource}",
            headers=headers, params=params, timeout=30
        )
        resp.raise_for_status()
        body = resp.json()
        records.extend(body["data"])
        cursor = body["meta"].get("next_cursor")
        if not cursor:
            break
        params = {"cursor": cursor, "per_page": 500}
    return records
```

### 3.2 Kubernetes CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: dp-<product>-consumer
  namespace: <consumer-namespace>
spec:
  schedule: "0 7 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: pipeline
            image: <registry>/<image>:<tag>
            envFrom:
            - secretRef:
                name: dp-<product>-consumer-secrets
            resources:
              requests: { cpu: "500m", memory: "512Mi" }
              limits:   { cpu: "1000m", memory: "2Gi" }
          restartPolicy: OnFailure
```

### 3.3 Scaling

```bash
# Scale up (saat volume peak)
kubectl patch deployment dp-<product>-consumer \
  -p '{"spec":{"template":{"spec":{"containers":[{"name":"pipeline",
      "resources":{"limits":{"cpu":"2000m","memory":"4Gi"}}}]}}}}'

# Scale down (saat volume normal)
kubectl rollout restart deployment/dp-<product>-consumer
```

---

## 4. Monitoring Consumer-Side

### 4.1 Metrics yang Wajib Dipantau

| Metrik | Cara Ukur | Alert Threshold |
|---|---|---|
| Pipeline success rate | Count sukses / total run | < 95% dalam 7 hari |
| Freshness di target | `MAX(loaded_at)` di tabel target | > 2× jadwal update |
| API error rate | Count 4xx+5xx / total request | > 1% |
| Row count delta | Hari ini vs 7-hari moving average | > ±30% |

### 4.2 Alert Slack

```python
def send_alert(msg: str):
    requests.post(os.environ["SLACK_WEBHOOK"], json={"text": msg})

# Contoh: integrasi dengan Airflow on_failure_callback
def on_failure(context):
    send_alert(
        f"❌ Pipeline consumer gagal\n"
        f"Task: {context['task_instance'].task_id}\n"
        f"Error: {context['exception']}"
    )
```

---

## 5. Rotasi Credentials

Lakukan **sebelum expiry** — reminder dikirim 30 hari sebelumnya ke `#dp-<product>-announce`.

```bash
# 1. Generate credentials baru di portal
#    https://portal.<domain>.org/credentials/rotate/<credential-id>

# 2. Update Kubernetes secret
kubectl create secret generic dp-<product>-consumer-secrets \
  --from-literal=API_CLIENT_ID="<new-id>" \
  --from-literal=API_CLIENT_SECRET="<new-secret>" \
  --dry-run=client -o yaml | kubectl apply -f -

# 3. Restart deployment
kubectl rollout restart deployment/<consumer-deployment>

# 4. Verifikasi
curl -s https://api.<domain>.org/v<N>/health
```

---

## 6. Troubleshooting

| Gejala | Kemungkinan Penyebab | Solusi |
|---|---|---|
| Data stale di target | Pipeline gagal atau data product delayed | Cek logs pipeline; cek [DLV-01 §4.2](./consumer-onboarding-guide.md) |
| `401 Unauthorized` berulang | Token expired atau credentials salah | → Section 5: Rotasi credentials |
| `429 Too Many Requests` | Rate limit terlampaui | Implementasi backoff; pertimbangkan upgrade tier |
| Row count drop signifikan | Masalah upstream atau filter terlalu ketat | Hubungi `#dp-<product>-support` |
| Koneksi timeout ke DB | Connection pool exhausted | Naikkan `connection_pool_size`; scale workload |

**Eskalasi ke data product team** jika masalah tidak selesai dalam 1 jam, atau jika semua error 5xx (bukan masalah consumer-side). Format laporan di [DLV-01 §8.2](./consumer-onboarding-guide.md).

---

## 7. Decommission Consumer Workload

```bash
# 1. Stop workload
kubectl delete cronjob dp-<product>-consumer-pipeline -n <namespace>

# 2. Hapus secrets
kubectl delete secret dp-<product>-consumer-secrets -n <namespace>

# 3. Revoke credentials
#    https://portal.<domain>.org/credentials/revoke/<credential-id>

# 4. Notifikasi data product team di #dp-<product>-support
#    agar akses dicabut dari G-02 Access Control Matrix
```

---

## Annex A — Consumer Workload Go-Live Checklist

```
CONSUMER WORKLOAD GO-LIVE CHECKLIST

INFRASTRUKTUR
[ ] Credentials di secrets manager (bukan hardcode atau .env yang di-commit)
[ ] Resource limits sesuai capacity planning (Section 2.3)
[ ] Retry logic dan timeout dikonfigurasi

MONITORING
[ ] Alert pipeline failure aktif
[ ] Alert freshness data di target aktif
[ ] Dashboard monitoring dikonfigurasi

OPERASIONAL
[ ] Jadwal pipeline tidak overlap dengan maintenance window producer
[ ] On-call contact terdefinisi di sisi consumer
[ ] Rotasi credentials dijadwalkan (sesuai lifecycle di Vault)

Disetujui oleh: _______________   Tanggal: _______________
```
