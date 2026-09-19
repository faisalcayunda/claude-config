---
title: "Operations Runbook — <Nama Data Product>"
sidebar_label: "Operations Runbook"
sidebar_position: 7
description: "Prosedur operasional step-by-step untuk data product: health check, incident response, maintenance, dan eskalasi."
tags: [monitoring, operations, runbook, incident-response, sre]
doc_id: "M-07"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: monitoring
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Operations Runbook

> **Tujuan dokumen ini:** Panduan operasional mandiri bagi on-call engineer — berisi prosedur step-by-step untuk setiap skenario insiden atau tugas maintenance yang dapat terjadi pada data product ini. Dokumen ini harus bisa dijalankan tanpa perlu bertanya ke siapapun.

:::tip Cara Menggunakan Runbook Ini
Navigasi langsung ke seksi yang relevan menggunakan nomor prosedur di Tabel Konten. Setiap prosedur berisi: trigger, langkah-langkah bernomor, dan kriteria selesai.
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
| **Doc ID** | `M-07` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **On-call DE** | Rotasi mingguan — cek `#dp-oncall` |
| **Eskalasi L1** | `<Nama Data Steward, Slack @handle>` |
| **Eskalasi L2** | `<Nama Data Product Owner, Slack @handle>` |
| **Eskalasi L3** | `<Nama Engineering Manager, Slack @handle>` |
| **Dokumen terkait** | [V-05 Data Pipeline](../development/data-pipeline.md) · [V-06 Data API](../development/data-api.md) · [M-04 Incident Template](./operational-reports.md) · [G-05 Governance Checklist](../../governance/federated-governance-checklist.md) |

---

## 1. Quick Reference — Kontak dan Links

| Resource | Link / Info |
|---|---|
| Airflow UI | `https://airflow.<domain>.org` |
| Grafana Dashboard | `https://grafana.<domain>.org/d/<dashboard-id>` |
| Data Catalog | `https://catalog.<domain>.org/<domain>/<product>` |
| Alert Channel | `#dp-<product>-alerts` (Slack) |
| Support Channel | `#dp-<product>-support` (Slack) |
| Status Page | `https://status.<domain>.org` |
| Vault (Secrets) | `https://vault.<domain>.org` |
| Incident Log | `https://jira.<domain>.org/projects/<key>/issues?label=incident` |

---

## 2. Klasifikasi Insiden

| Severity | Kriteria | Response Time | Eskalasi |
|---|---|---|---|
| **SEV-1** | Pipeline total down, data tidak tersedia, atau SLA breach berdampak ke produksi consumer | **< 15 menit** (24/7) | Langsung ke L2 + L3 |
| **SEV-2** | Kualitas data degraded signifikan, freshness SLO breach, atau API error rate > 1% | **< 1 jam** (jam kerja) | L1 → L2 jika tidak selesai dalam 2 jam |
| **SEV-3** | Minor quality issue terisolasi, single endpoint lambat, atau downstream non-kritis terdampak | **< 4 jam** (jam kerja) | L1 menangani |
| **SEV-4** | Cosmetic issue, dokumentasi salah, atau improvement request | **Next sprint** | Masuk backlog |

---

## 3. Prosedur: Health Check Harian

**Trigger:** Setiap pagi jam `<08:00 WIB>`, atau saat menerima notifikasi dari monitoring.

**Langkah-langkah:**

1. Buka Grafana dashboard: `https://grafana.<domain>.org/d/<id>`
2. Verifikasi semua panel "pipeline status" menunjukkan `✅ SUCCESS`
3. Periksa freshness data — jalankan query berikut:

```sql
SELECT
    MAX(updated_at)                              AS last_update,
    NOW() - MAX(updated_at)                      AS age,
    CASE
        WHEN NOW() - MAX(updated_at) > INTERVAL '<2 hours>'
        THEN '⚠️ STALE'
        ELSE '✅ FRESH'
    END                                          AS status
FROM <schema>.<nama_tabel>;
```

4. Periksa error rate API 24 jam terakhir:

```bash
curl -s -H "X-API-Key: ${MONITORING_API_KEY}" \
  "https://api.<domain>.org/v<N>/metrics" \
  | python3 -c "import sys,json; m=json.load(sys.stdin); \
    print(f'Error rate: {m[\"error_rate_24h\"]}%')"
```

5. Jika semua `✅` → catat "Health check OK" di `#dp-<product>-alerts`
6. Jika ada `⚠️` atau `❌` → lanjutkan ke prosedur yang sesuai di bawah

---

## 4. Prosedur: Pipeline Gagal (SEV-1 / SEV-2)

**Trigger:** Alert Airflow task failure di `#dp-<product>-alerts`, atau ditemukan saat health check.

**Langkah-langkah:**

1. Buka Airflow UI → cari DAG `dp_<domain>_<product>_daily` → identifikasi task yang gagal
2. Klik task yang merah → lihat logs → identifikasi root cause

**Routing berdasarkan error:**

| Error Message | Root Cause | Prosedur |
|---|---|---|
| `connection refused` / `timeout` ke source | Source system down atau network issue | → [Prosedur 4a](#4a-source-system-tidak-dapat-diakses) |
| `SSL certificate expired` | Sertifikat koneksi kadaluarsa | → [Prosedur 4b](#4b-ssl-certificate-expired) |
| `dbt test failed` | Data quality issue di source | → [Prosedur 4c](#4c-data-quality-test-gagal) |
| `out of memory` / `OOM killed` | Volume data melebihi kapasitas | → [Prosedur 4d](#4d-pipeline-oom-out-of-memory) |
| `unique constraint violation` | Duplikat data dari source | → [Prosedur 4e](#4e-duplikat-data-dari-source) |
| Error lain | Unknown | → Eskalasi ke L2, sertakan log |

### 4a. Source System Tidak Dapat Diakses

1. Ping source: `curl -v <source-host>:<port>` — verifikasi konektivitas
2. Cek VPN/network: `traceroute <source-host>`
3. Hubungi tim pemilik source system via `<channel Slack / nomor HP>`, sertakan Ticket ID
4. Jika source akan down > 30 menit → eskalasi ke L2, informasikan consumer di `#dp-<product>-support`
5. Setelah source kembali online → re-trigger DAG: `airflow dags trigger dp_<domain>_<product>_daily`

### 4b. SSL Certificate Expired

1. Verifikasi: `openssl s_client -connect <source-host>:<port> 2>&1 | grep "Verify return code"`
2. Ambil sertifikat baru dari Vault: `vault kv get secret/<env>/<domain>/source-ssl-cert`
3. Update di Airflow connection: Airflow UI → Admin → Connections → `<connection-id>` → update SSL fields
4. Test koneksi: `airflow connections test <connection-id>`
5. Re-trigger DAG

### 4c. Data Quality Test Gagal

1. Lihat output test di Airflow logs atau dbt test report
2. Identifikasi rule yang gagal dan tabel yang terdampak
3. Jalankan query investigasi:

```sql
-- Contoh: cek distribusi nilai yang gagal validasi
SELECT <field_bermasalah>, COUNT(*) AS jumlah
FROM <schema>.<tabel>
WHERE <kondisi_yang_gagal>
GROUP BY 1 ORDER BY 2 DESC LIMIT 20;
```

4. Tentukan apakah ini **data issue di source** (eskalasi ke source team) atau **bug di transformation logic** (fix di kode dbt)
5. Jika data issue di source → tandai data dengan flag `dq_flag = 'QUARANTINE'`, jangan block pipeline
6. Jika bug di transformation → buat hotfix branch, deploy setelah review
7. Dokumentasikan di incident log

### 4d. Pipeline OOM (Out of Memory)

1. Identifikasi task yang OOM di Airflow logs (`Killed` atau `OOMKilled`)
2. Estimasi volume data run ini vs baseline:

```sql
SELECT COUNT(*) FROM <schema>.<tabel>
WHERE <tanggal_field> = CURRENT_DATE - 1;
```

3. Jika volume anomali tinggi → cek apakah ada backlog data di source system
4. Naikkan sementara Airflow worker memory: edit Helm values → `worker.resources.memory: <nilai baru>` → apply
5. Re-trigger DAG setelah resource update
6. Buat tiket untuk memory right-sizing di sprint berikutnya

### 4e. Duplikat Data dari Source

1. Hitung duplikat:

```sql
SELECT <composite_key_fields>, COUNT(*) AS cnt
FROM bronze.<nama_tabel>
WHERE <tanggal_field> = CURRENT_DATE - 1
GROUP BY <composite_key_fields>
HAVING COUNT(*) > 1;
```

2. Jika jumlah duplikat < 0.1% → dedup otomatis sudah ada di Silver layer; pipeline bisa dilanjutkan
3. Jika > 0.1% → tahan pipeline, eskalasi ke source team, dokumentasikan di incident log
4. Setelah source fix → jalankan full-refresh Bronze untuk tanggal terdampak:

```bash
dbt run --select bronze.<nama_tabel> --full-refresh \
  --vars '{"date_filter": "<YYYY-MM-DD>"}' --target prod
```

---

## 5. Prosedur: Freshness SLO Breach (SEV-2)

**Trigger:** Alert monitoring — data age > `<2 jam>` setelah cut-off.

1. Jalankan query freshness check di [Prosedur 3 langkah 3]
2. Cek status DAG di Airflow — apakah pipeline berjalan atau macet?
3. Jika pipeline berjalan normal tapi data belum update → cek apakah source terlambat:

```bash
# Cek timestamp data terbaru di source (via Airbyte / koneksi langsung)
curl -s "https://api.airbyte.<domain>.org/api/v1/jobs/list" \
  -H "Authorization: Bearer ${AIRBYTE_TOKEN}" \
  | python3 -c "import sys,json; jobs=json.load(sys.stdin)['jobs']; \
    print(jobs[0]['status'], jobs[0]['lastUpdatedAt'])"
```

4. Jika pipeline macet → ikuti [Prosedur 4](#4-prosedur-pipeline-gagal-sev-1--sev-2)
5. Jika source terlambat → notifikasi consumer di `#dp-<product>-support`:

```
⚠️ DATA FRESHNESS ALERT
Data product: <nama>
Status: Data delayed — estimasi tersedia <HH:MM WIB>
Penyebab: Source system terlambat
Update: Akan diinformasikan setiap 30 menit
```

6. Catat di incident log jika delay > 2× SLO threshold

---

## 6. Prosedur: API Error Rate Tinggi (SEV-2)

**Trigger:** Alert Grafana — error rate > 1% dalam 5 menit terakhir.

1. Buka Grafana panel "API Error Rate" → identifikasi error code yang dominan
2. **Jika mayoritas 4xx (client errors):**
   - Cek apakah ada perubahan client yang deploy baru
   - Lihat request logs untuk melihat pola request yang salah
   - Tidak perlu tindakan di server; informasikan consumer jika perlu
3. **Jika mayoritas 5xx (server errors):**
   - Cek application logs: `kubectl logs -n <namespace> dp-<product>-api-<pod-id> --tail=100`
   - Cek koneksi DB API ke DWH: `kubectl exec -it dp-<product>-api-<pod-id> -- python3 -c "import psycopg2; ..."`
   - Jika DB connection pool exhausted → restart pod: `kubectl rollout restart deployment/dp-<product>-api`
4. **Jika 503 (service unavailable):**
   - Cek health endpoint: `curl https://api.<domain>.org/v<N>/health`
   - Cek pod status: `kubectl get pods -n <namespace> -l app=dp-<product>-api`
   - Scale up jika load terlalu tinggi: `kubectl scale deployment dp-<product>-api --replicas=<N+1>`

---

## 7. Prosedur: Planned Maintenance

**Trigger:** Scheduled maintenance window — setiap `<Sabtu 02:00–04:00 WIB>` atau saat ada deployment baru.

**H-48: Persiapan**

1. Kirim notifikasi ke `#dp-<product>-announce`:

```
🔧 PLANNED MAINTENANCE NOTICE
Data Product: <nama>
Waktu: <Sabtu, DD MMM YYYY, 02:00–04:00 WIB>
Dampak: <API tidak tersedia / data stale selama maintenance>
```

2. Pastikan last successful pipeline run tersedia sebelum window mulai

**Saat Maintenance:**

1. Pause DAG: `airflow dags pause dp_<domain>_<product>_daily`
2. Set API ke maintenance mode (jika tersedia): update Ingress annotation atau deploy maintenance page
3. Lakukan aktivitas maintenance (deploy, upgrade, schema migration)
4. Jalankan smoke tests post-maintenance:

```bash
# Verifikasi DB connection
psql $DB_DW_CONN -c "SELECT COUNT(*) FROM <schema>.<tabel>;"

# Verifikasi API health
curl -s https://api.<domain>.org/v<N>/health | python3 -m json.tool

# Verifikasi data contract
data-contract-cli test --contract design/data-contract.yaml
```

5. Resume DAG: `airflow dags unpause dp_<domain>_<product>_daily`
6. Kirim update ke `#dp-<product>-announce`: `✅ Maintenance selesai. Layanan normal kembali.`

---

## 8. Prosedur: Rotasi Kredensial

**Trigger:** Kredensial mendekati expiry (30 hari sebelum) atau ada security incident.

1. Generate kredensial baru di sistem yang relevan (DB, OAuth, API key)
2. Simpan di Vault:

```bash
vault kv put secret/<env>/<domain>/<service>-credentials \
  password="<new-password>" \
  rotated_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
```

3. Update environment variable di Kubernetes secret:

```bash
kubectl create secret generic dp-<product>-secrets \
  --from-literal=DB_PASSWORD="<new-password>" \
  --dry-run=client -o yaml | kubectl apply -f -
```

4. Restart aplikasi agar secret baru diambil: `kubectl rollout restart deployment/dp-<product>-api`
5. Verifikasi koneksi: jalankan health check [Prosedur 3]
6. Catat rotasi di version history dokumen ini

---

## 9. Prosedur: Eskalasi dan Komunikasi Insiden

### Template Notifikasi Awal (kirim dalam 15 menit sejak deteksi)

```
🚨 INCIDENT ALERT — <SEV-1/SEV-2>
Data Product  : <nama> v<versi>
Waktu Deteksi : <HH:MM WIB, DD MMM YYYY>
Status        : Investigating
Dampak        : <deskripsi singkat — siapa terdampak, apa yang tidak bisa dilakukan>
On-call       : <nama DE>
Ticket        : <JIRA-ID>

Update berikutnya dalam: 30 menit
```

### Template Update Berkala (setiap 30 menit)

```
🔄 INCIDENT UPDATE — <SEV-N> — <waktu>
Root Cause    : <ditemukan / masih diselidiki>
Progress      : <langkah yang sudah dilakukan>
ETA Resolved  : <estimasi, atau "TBD">
```

### Template Resolved

```
✅ INCIDENT RESOLVED — <SEV-N>
Waktu Selesai  : <HH:MM WIB, DD MMM YYYY>
Durasi         : <X jam Y menit>
Root Cause     : <ringkasan>
Fix Applied    : <apa yang dilakukan>
Post-mortem    : <link ke post-mortem doc, atau "dijadwalkan DD MMM">
```

---

## Annex A — Perintah Cepat

```bash
# Trigger DAG manual
airflow dags trigger dp_<domain>_<product>_daily

# Pause / resume DAG
airflow dags pause   dp_<domain>_<product>_daily
airflow dags unpause dp_<domain>_<product>_daily

# Lihat task log terbaru
airflow tasks logs dp_<domain>_<product>_daily <task_id> <execution_date>

# dbt run single model
dbt run --select <model_name> --target prod

# dbt run dengan full-refresh
dbt run --select <model_name> --full-refresh --target prod

# Test data contract
data-contract-cli test --contract design/data-contract.yaml

# Restart API deployment
kubectl rollout restart deployment/dp-<product>-api -n <namespace>

# Scale API pods
kubectl scale deployment dp-<product>-api --replicas=<N> -n <namespace>

# Cek pod logs
kubectl logs -n <namespace> -l app=dp-<product>-api --tail=200 -f
```
