---
title: "Backup & Disaster Recovery Plan — <Nama Data Product>"
sidebar_label: "Backup & DR Plan"
sidebar_position: 5
description: "Strategi backup, target RTO/RPO, prosedur disaster recovery, dan rencana pengujian untuk data product."
tags: [monitoring, backup, disaster-recovery, rto, rpo, sre]
doc_id: "M-05"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: monitoring
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# Backup & Disaster Recovery Plan

> **Tujuan dokumen ini:** Mendefinisikan strategi backup, target pemulihan, dan prosedur disaster recovery untuk data product ini — sehingga tim dapat memulihkan layanan dalam waktu yang sudah disepakati tanpa improvisasi.

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama, Role>` |

---

## Header Identifikasi

| Atribut | Nilai |
|---|---|
| **Doc ID** | `M-05` |
| **Domain** | `<Nama Domain>` |
| **Data Product** | `<Nama Data Product>` |
| **DR Coordinator** | `<Nama SRE, Email>` |
| **Backup Owner** | `<Nama DE/SRE, Email>` |
| **RTO Target** | `<4 jam>` |
| **RPO Target** | `<1 jam>` |
| **Dokumen terkait** | [M-07 Operations Runbook](./operations-runbook.md) · [D-09 Infra Brief](../design/infra-brief.md) · [G-04 Retention Policy](../../governance/data-retention-policy.md) |

---

## 1. Recovery Objectives

### 1.1 RTO dan RPO per Komponen

| Komponen | RTO Target | RPO Target | Prioritas |
|---|---|---|---|
| Database (Gold Layer) | `<4 jam>` | `<1 jam>` | P1 — Kritis |
| Pipeline Orchestration (Airflow) | `<2 jam>` | `<State terbaru>` | P2 |
| API Service | `<1 jam>` | `N/A (stateless)` | P1 — Kritis |
| Data Catalog Metadata | `<8 jam>` | `<24 jam>` | P3 |
| Pipeline Code (Git) | `<30 menit>` | `N/A (Git)` | P1 |

### 1.2 Definisi Recovery Points

| Istilah | Definisi |
|---|---|
| **RTO** (Recovery Time Objective) | Waktu maksimum sistem boleh down sebelum layanan pulih |
| **RPO** (Recovery Point Objective) | Jarak waktu maksimum data yang boleh hilang |
| **MTD** (Maximum Tolerable Downtime) | Batas atas absolut sebelum dampak bisnis tidak dapat diterima |

---

## 2. Inventori Komponen dan Strategi Backup

### 2.1 Database — PostgreSQL / Data Warehouse

| Atribut | Nilai |
|---|---|
| Host | `<db-host.domain.org>` |
| Database | `<nama_database>` |
| Schema | `<nama_schema>` |
| Volume Data | `<estimasi GB/TB>` |
| Growth Rate | `<GB per bulan>` |

**Strategi Backup:**

| Tipe Backup | Frekuensi | Retensi | Tool | Storage Lokasi |
|---|---|---|---|---|
| Full backup | Mingguan (Minggu 02:00) | 4 minggu | `pg_dump` / managed service | `s3://<bucket>/backups/db/full/` |
| Incremental (WAL) | Continuous (setiap 5 menit) | 7 hari | WAL-G / managed PITR | `s3://<bucket>/backups/db/wal/` |
| Schema-only backup | Setiap deploy | 90 hari | `pg_dump --schema-only` | `s3://<bucket>/backups/db/schema/` |

**Verifikasi Backup Otomatis:**

```bash
# Dijalankan setiap Senin jam 06:00 oleh Airflow DAG: dp_<product>_backup_verify
# Restore ke test environment dan jalankan smoke test

# Script verifikasi manual:
aws s3 ls s3://<bucket>/backups/db/full/ --recursive \
  | sort | tail -5  # cek 5 backup terbaru

# Test restore ke temporary DB
pg_restore -h <test-db-host> -d <test_db> \
  s3://<bucket>/backups/db/full/latest.dump
```

### 2.2 Pipeline Code dan Konfigurasi

| Resource | Backup Method | Lokasi |
|---|---|---|
| Pipeline code | Git (automatic) | `https://github.com/org/<repo>` |
| Airflow DAG definitions | Git + S3 sync | `s3://<bucket>/backups/airflow/dags/` |
| dbt project | Git (automatic) | `https://github.com/org/<repo>/models` |
| Airflow connections & variables | Export tiap malam | `s3://<bucket>/backups/airflow/config/` |
| Kubernetes manifests | Git (automatic) | `https://github.com/org/<infra-repo>` |

### 2.3 Secrets dan Credentials

:::warning
Credentials TIDAK di-backup di S3. Recovery credentials dilakukan via Vault restore.
:::

| Resource | Backup Method | Prosedur Recovery |
|---|---|---|
| Vault secrets | Vault built-in snapshot | `vault operator raft snapshot restore <file>` |
| Kubernetes secrets | Velero / Vault-injected (tidak perlu backup terpisah) | Recreate dari Vault |

---

## 3. Skenario Disaster dan Prosedur Recovery

### Skenario DR-01: Database Corruption / Data Loss

**Trigger:** Data hilang, corrupt, atau terhapus tidak sengaja.

**Langkah Recovery:**

1. **Stop pipeline segera** untuk mencegah data corrupt menyebar:
   ```bash
   airflow dags pause dp_<domain>_<product>_daily
   ```

2. **Identifikasi scope** — berapa row terdampak dan sejak kapan:
   ```sql
   SELECT MIN(updated_at), MAX(updated_at), COUNT(*)
   FROM <schema>.<tabel>
   WHERE <kondisi kerusakan>;
   ```

3. **Tentukan recovery point** — pilih backup terdekat sebelum kejadian:
   ```bash
   aws s3 ls s3://<bucket>/backups/db/wal/ | grep "<tanggal>"
   ```

4. **Point-In-Time Recovery (PITR)** ke timestamp sebelum kejadian:
   ```bash
   # Contoh dengan WAL-G
   WALG_S3_PREFIX=s3://<bucket>/backups/db/wal \
   wal-g backup-fetch /var/lib/postgresql/data LATEST
   # Kemudian set recovery_target_time di postgresql.conf
   ```

5. **Verifikasi data** setelah restore:
   ```sql
   SELECT COUNT(*), MAX(updated_at) FROM <schema>.<tabel>;
   ```

6. **Jalankan data contract validation**:
   ```bash
   data-contract-cli test --contract design/data-contract.yaml
   ```

7. **Resume pipeline** dan informasikan consumer:
   ```bash
   airflow dags unpause dp_<domain>_<product>_daily
   ```

**RTO untuk skenario ini:** `<4 jam>`

---

### Skenario DR-02: Total Infrastructure Failure (Region Down)

**Trigger:** Cloud region primary tidak dapat diakses.

**Langkah Recovery:**

1. Aktifkan region failover (jika multi-region setup):
   ```bash
   # Update DNS ke region secondary
   aws route53 change-resource-record-sets \
     --hosted-zone-id <zone-id> \
     --change-batch file://failover-config.json
   ```

2. Restore database di region secondary dari latest backup:
   ```bash
   # Restore dari S3 cross-region bucket
   aws s3 cp s3://<bucket-secondary>/backups/db/full/latest.dump ./
   pg_restore -h <secondary-db-host> -d <database> latest.dump
   ```

3. Deploy pipeline dan API ke region secondary menggunakan Git:
   ```bash
   kubectl apply -f k8s/manifests/ --context=<secondary-cluster>
   ```

4. Restore Airflow connections dari backup:
   ```bash
   airflow connections import s3://<bucket-secondary>/backups/airflow/config/connections.json
   ```

5. Verifikasi semua komponen via health check [M-07 Prosedur 3]

6. Informasikan stakeholder dan consumer tentang status

**RTO untuk skenario ini:** `<8 jam>` (RPO: `<1 jam>`)

---

### Skenario DR-03: Accidental Schema Drop

**Trigger:** Tabel atau skema tidak sengaja terhapus.

1. Identifikasi DDL terakhir dari schema-only backup:
   ```bash
   aws s3 cp s3://<bucket>/backups/db/schema/latest.sql ./
   grep "CREATE TABLE <tabel>" latest.sql
   ```

2. Recreate schema dari DDL backup:
   ```bash
   psql $DB_DW_CONN -f latest.sql
   ```

3. Restore data dari WAL atau full backup terdekat ([Skenario DR-01 langkah 4])

4. Verifikasi row counts dan jalankan pipeline verification:
   ```bash
   dbt test --select <tabel> --target prod
   ```

**RTO untuk skenario ini:** `<2 jam>`

---

## 4. Jadwal Pengujian DR

:::warning DR Test adalah Wajib
Disaster Recovery Plan yang tidak diuji bukan DR Plan — itu fiksi. Pengujian di bawah adalah mandatory, bukan opsional.
:::

| Jenis Test | Frekuensi | Last Tested | Result | Next Test |
|---|---|---|---|---|
| Backup restoration (partial) | Bulanan | `<YYYY-MM-DD>` | `<PASS/FAIL>` | `<YYYY-MM-DD>` |
| Full DR simulation (DR-01) | Semesteran | `<YYYY-MM-DD>` | `<PASS/FAIL>` | `<YYYY-MM-DD>` |
| Failover test (DR-02) | Tahunan | `<YYYY-MM-DD>` | `<PASS/FAIL>` | `<YYYY-MM-DD>` |
| Schema restore test (DR-03) | Kuartalan | `<YYYY-MM-DD>` | `<PASS/FAIL>` | `<YYYY-MM-DD>` |

**Prosedur test bulanan (minimal):**

```bash
# 1. Ambil backup terbaru
aws s3 cp s3://<bucket>/backups/db/full/latest.dump /tmp/test-restore.dump

# 2. Restore ke test DB
createdb -h <test-db-host> dp_dr_test_$(date +%Y%m%d)
pg_restore -h <test-db-host> -d dp_dr_test_$(date +%Y%m%d) /tmp/test-restore.dump

# 3. Smoke test
psql -h <test-db-host> -d dp_dr_test_$(date +%Y%m%d) \
  -c "SELECT COUNT(*) FROM <schema>.<tabel>;"

# 4. Catat hasil di tabel di atas
# 5. Drop test DB
dropdb -h <test-db-host> dp_dr_test_$(date +%Y%m%d)
```

---

## 5. Komunikasi saat Disaster

### Komunikasi Internal (dalam 30 menit)

| Pihak | Media | Konten |
|---|---|---|
| On-call SRE | PagerDuty / telepon | Aktivasi DR plan, severity, scope |
| Data Product Owner | Slack + telepon | Status, ETA, dampak consumer |
| Engineering Manager | Slack | Severity, tim yang terlibat |

### Komunikasi Consumer (dalam 1 jam)

```
🔴 DATA PRODUCT OUTAGE — <nama data product>
Status    : Tidak tersedia / data tidak akurat
Sejak     : <HH:MM WIB DD MMM YYYY>
Estimasi  : Pemulihan target <HH:MM WIB>
Penyebab  : <singkat — "infrastructure failure" / "data corruption" / dll.>
Update    : Setiap 30 menit di channel ini
```

---

## Annex A — Backup Verification Checklist

Dijalankan setiap Senin oleh on-call engineer:

```
BACKUP VERIFICATION CHECKLIST — <YYYY-MM-DD>

DB Full Backup
[ ] Backup terbaru ada di S3: aws s3 ls s3://<bucket>/backups/db/full/ | tail -3
[ ] Timestamp backup ≤ 7 hari yang lalu
[ ] File size reasonable (tidak 0 bytes): _____ GB

WAL / Incremental Backup
[ ] WAL files terbaru ada: aws s3 ls s3://<bucket>/backups/db/wal/ | tail -5
[ ] Gap antara WAL terakhir ≤ 10 menit

Airflow Config Backup
[ ] Export config ada: aws s3 ls s3://<bucket>/backups/airflow/config/ | tail -3

Restore Test (bulanan)
[ ] Test restore berhasil: _____ rows dipulihkan
[ ] Smoke test PASS

Catatan: _______________
Dikerjakan oleh: _______________
```
