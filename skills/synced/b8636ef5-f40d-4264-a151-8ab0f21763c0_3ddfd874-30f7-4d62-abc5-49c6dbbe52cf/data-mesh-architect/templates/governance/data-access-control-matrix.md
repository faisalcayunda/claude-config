---
title: "Data Access Control Matrix — <Nama Data Product>"
sidebar_label: "Access Control Matrix"
sidebar_position: 2
description: "Matriks kontrol akses data yang mendefinisikan hak akses setiap role terhadap setiap tabel, kolom, dan output port dalam data product, beserta dasar regulasi dan prosedur permohonan akses."
tags: [governance, access-control, rbac, security, uu-pdp, data-product]
document_id: "DACM-<DOMAIN>-<PRODUCT>"
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
review_cycle: "<Kuartalan / Semesteran>"
next_review_date: "<YYYY-MM-DD>"
---

# Data Access Control Matrix

> **Tujuan dokumen ini:** Mendefinisikan secara formal siapa yang boleh mengakses data apa, dengan operasi apa, dan dalam kondisi apa — di setiap lapisan data product. Dokumen ini menjadi dasar hukum teknis untuk implementasi RBAC di PostgreSQL, konfigurasi API gateway, dan sebagai bukti kepatuhan terhadap UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi.

:::note Hubungan dengan Dokumen Lain
- Definisi role dan tanggung jawab: `../project-management/rasci-matrix.md`
- Implementasi teknis RBAC: `../design/infra-brief.md`
- Data classification per kolom: `../design/data-catalog.md`
- Risk assessment & DPIA: `../design/risk-assessment.md`
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis | Reviewer |
|---|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama DA>` | `<Nama DS>` |

---

## Definisi Umum

| Atribut | Nilai |
|---|---|
| **Nama Data Product** | `<Nama Data Product>` |
| **Domain** | `<Nama Domain>` |
| **Data Product Owner** | `<Nama, Email>` |
| **Data Steward** | `<Nama, Email>` |
| **Security Contact** | `<Nama Tim Keamanan, Email>` |
| **Tanggal Efektif** | `<YYYY-MM-DD>` |

---

## Bagian 1 — Inventori Role

`[Mandatory]` — Definisikan semua role yang berinteraksi dengan data product ini sebelum mengisi matriks.

### 1.1 Role Teknis (Database Roles)

Role-role ini diimplementasikan langsung di PostgreSQL dan diwarisi oleh semua koneksi yang masuk.

| Role PostgreSQL | Deskripsi | Diberikan kepada | Cara Provisioning |
|---|---|---|---|
| `<domain>_engineer` | Akses penuh untuk membangun dan memelihara pipeline | Tim Data Engineering domain | Pemberian manual oleh DBA setelah approval DPO |
| `<domain>_analyst` | Akses baca ke Gold layer dengan masking PII | Data Analyst internal | Pemberian manual setelah approval DPO |
| `<domain>_consumer` | Akses baca ke output port yang telah ditetapkan | Sistem/aplikasi consumer eksternal | Melalui service account via Keycloak |
| `<domain>_audit_role` | Akses baca ke semua layer termasuk audit schema | Tim Internal Audit, Legal | Pemberian manual dengan time-bound (maksimal 90 hari) |
| `<domain>_dq` | Akses baca untuk tool DQ (Great Expectations, Soda) | Akun service Great Expectations | Automated via CI/CD |

### 1.2 Role Bisnis (Logical Roles)

Role-role ini merepresentasikan kelompok pengguna bisnis. Setiap role bisnis dipetakan ke satu atau lebih role teknis PostgreSQL.

| Role Bisnis | Deskripsi | Contoh Persona | Mapped to PostgreSQL Role |
|---|---|---|---|
| **Data Engineer** | Membangun, mengoperasikan, dan memperbaiki pipeline | `<Nama>` — tim `<nama tim>` | `<domain>_engineer` |
| **Data Analyst (Internal)** | Menganalisis data untuk kebutuhan operasional dan pelaporan | `<Nama>` — `<divisi>` | `<domain>_analyst` |
| **Data Scientist** | Membangun model ML menggunakan data | `<Nama>` — tim `<nama tim>` | `<domain>_analyst` + akses khusus via approval |
| **Consumer System (API)** | Sistem eksternal yang mengakses data via REST API | `<Nama aplikasi>` | `<domain>_consumer` (via API Gateway) |
| **Consumer System (SQL)** | Sistem eksternal yang query langsung ke Gold layer | `<Nama sistem>` | `<domain>_consumer` (read-only) |
| **Data Product Owner** | Bertanggung jawab atas keputusan produk | `<Nama>` | Tidak ada akses database langsung |
| **Data Steward** | Menjaga kualitas dan kesesuaian semantik data | `<Nama>` | `<domain>_analyst` + `<domain>_audit_role` |
| **Auditor Internal** | Audit kepatuhan dan governance | `<Nama>` — Legal/Compliance | `<domain>_audit_role` (time-bound) |
| **Eksekutif / Pimpinan** | Akses dashboard read-only untuk monitoring | `<Jabatan>` | Hanya via Apache Superset (tidak akses DB langsung) |

---

## Bagian 2 — Level Akses

Gunakan kode berikut secara konsisten di seluruh matriks:

| Kode | Level Akses | Definisi |
|---|---|---|
| **NONE** | Tidak Ada Akses | Tidak dapat melihat atau berinteraksi dengan resource ini sama sekali |
| **R-MASKED** | Baca Tersamarkan | Baca-saja dengan masking pada kolom PII/sensitif sesuai aturan masking |
| **R-FULL** | Baca Penuh | Baca-saja tanpa masking. Hanya untuk role privileged yang sudah disetujui DPO |
| **RW** | Baca-Tulis | INSERT, UPDATE, DELETE. Hanya untuk pipeline service account |
| **RW-ADMIN** | Baca-Tulis-Admin | DDL (CREATE, ALTER, DROP) + DML. Hanya untuk tim engineering |
| **AUDIT** | Audit Read | Baca-saja pada semua layer termasuk tabel audit. Time-bound maksimal 90 hari |

---

## Bagian 3 — Matriks Akses per Layer

### 3.1 Layer Bronze (Raw — Data Sumber Asli)

Layer paling sensitif — berisi data sebelum masking/transformasi apapun.

| Tabel / Dataset | Data Engineer | Data Analyst | Data Scientist | Consumer (API/SQL) | Auditor | Catatan |
|---|---|---|---|---|---|---|
| `bronze.<nama_tabel_raw_1>` | RW-ADMIN | NONE | NONE | NONE | AUDIT (terbatas) | Berisi raw PII dari sumber — tidak untuk analyst |
| `bronze.<nama_tabel_raw_2>` | RW-ADMIN | NONE | NONE | NONE | AUDIT (terbatas) | |

**Kebijakan layer Bronze:**
- Tidak ada akses langsung dari luar tim Data Engineering.
- Auditor hanya bisa akses dengan permohonan khusus, time-bound, dan diawasi.
- Seluruh akses ke Bronze wajib di-log di `audit.audit_log`.

---

### 3.2 Layer Silver (Cleaned — Data Bersih)

Data sudah dibersihkan dan divalidasi, namun belum di-aggregate. PII masih ada dalam bentuk penuh.

| Tabel / Dataset | Data Engineer | Data Analyst | Data Scientist | Consumer (API/SQL) | Auditor | Catatan |
|---|---|---|---|---|---|---|
| `silver.<nama_tabel_clean_1>` | RW-ADMIN | NONE | R-MASKED | NONE | AUDIT | Data Scientist perlu akses dengan approval khusus DPO |
| `silver.<nama_tabel_clean_2>` | RW-ADMIN | NONE | NONE | NONE | AUDIT | |

---

### 3.3 Layer Gold (Business-Ready — Siap Konsumsi)

Data bisnis yang sudah siap dikonsumsi. Ini adalah layer utama untuk analyst dan consumer.

| Tabel / View | Data Engineer | Data Analyst | Data Scientist | Consumer (API) | Consumer (SQL) | Auditor | Catatan |
|---|---|---|---|---|---|---|---|
| `<schema>.dim_<entitas>` | RW-ADMIN | R-MASKED | R-MASKED | R-MASKED (via API) | R-MASKED | AUDIT | PII di-mask sesuai aturan di Bagian 4 |
| `<schema>.fact_<transaksi>` | RW-ADMIN | R-FULL | R-FULL | R-MASKED (via API) | NONE | AUDIT | Fact table tidak berisi PII — analyst bisa akses penuh |
| `<schema>.v_<view_ringkasan>` | R-FULL | R-FULL | R-FULL | R-MASKED (via API) | R-FULL | R-FULL | View aggregate — sudah tidak ada PII individu |

---

### 3.4 Output Port — REST API

| Endpoint | Data Engineer | Data Analyst | Consumer (Authenticated) | Consumer (Public) | Catatan |
|---|---|---|---|---|---|
| `GET /v1/<resource>` | R-MASKED | R-MASKED | R-MASKED | NONE | Rate limit: 100 req/menit |
| `GET /v1/<resource>/{id}` | R-FULL | R-MASKED | R-MASKED | NONE | |
| `GET /v1/<resource>/aggregate` | R-FULL | R-FULL | R-FULL | R-FULL | Endpoint aggregate tidak berisi PII individu |
| `POST /v1/<resource>` | RW | NONE | NONE | NONE | Write endpoint hanya untuk pipeline |

---

### 3.5 Audit Schema

| Tabel | Data Engineer | Data Analyst | Consumer | Auditor | Catatan |
|---|---|---|---|---|---|
| `audit.audit_log` | R-FULL | NONE | NONE | R-FULL | Log tidak boleh dimodifikasi oleh siapapun — append-only |

---

### 3.6 Apache Superset Dashboard

| Dashboard | Data Analyst | Data Scientist | Eksekutif | Consumer (Eksternal) | Catatan |
|---|---|---|---|---|---|
| Dashboard Operasional | R-MASKED | R-MASKED | NONE | NONE | |
| Dashboard Eksekutif | R-FULL | R-FULL | R-MASKED | NONE | Eksekutif lihat summary, bukan data individu |
| Dashboard Analitik | R-FULL | R-FULL | NONE | NONE | Untuk analisis mendalam |

---

## Bagian 4 — Aturan Masking per Kolom

`[Mandatory untuk semua kolom dengan klasifikasi >= Restricted]`

### 4.1 Tabel `<schema>.dim_<entitas>`

| Kolom | Klasifikasi | Kategori PII | Aturan Masking | Terlihat Penuh oleh | Dasar Hukum Masking |
|---|---|---|---|---|---|
| `id` | public | NULL | Tidak ada masking | Semua role | N/A |
| `kode_referensi` | public | NULL | Tidak ada masking | Semua role | N/A |
| `nama` | internal | pii-umum | Tampilkan hanya nama depan: `SPLIT_PART(nama, ' ', 1)` | `<domain>_engineer` | UU-27-2022 Pasal 4 |
| `nik` | restricted | pii-umum | Tampilkan 6 digit pertama, mask sisanya: `LEFT(nik,6) || REPEAT('*',10)` | `<domain>_engineer` | UU-27-2022 Pasal 4 |
| `tanggal_lahir` | restricted | pii-umum | Tampilkan hanya tahun: `DATE_TRUNC('year', tanggal_lahir)` | `<domain>_engineer` | UU-27-2022 Pasal 4 |
| `golongan_darah` | confidential | pii-sensitif-kesehatan | Sembunyikan sepenuhnya (NULL) | `<domain>_engineer` + medical_role | UU-27-2022 Pasal 4 ayat (2) |
| `kondisi_disabilitas` | confidential | pii-sensitif-kesehatan | Sembunyikan sepenuhnya (NULL) | `<domain>_engineer` + medical_role | UU-27-2022 Pasal 4 ayat (2) |
| `agama` | restricted | pii-sensitif-kepercayaan | Sembunyikan sepenuhnya (NULL) | `<domain>_engineer` | UU-27-2022 Pasal 4 ayat (2) huruf c |
| `koordinat_lat` | restricted | pii-umum | Bulatkan ke 2 desimal (radius ~1km) | `<domain>_engineer` | UU-27-2022 Pasal 4 |
| `status` | public | NULL | Tidak ada masking | Semua role | N/A |

**Implementasi masking di PostgreSQL:**

```sql
-- View dengan masking otomatis berdasarkan role yang sedang mengakses
CREATE OR REPLACE VIEW <schema>.v_dim_<entitas>_masked AS
SELECT
    id,
    kode_referensi,
    -- Nama: mask untuk non-engineer
    CASE
        WHEN pg_has_role(current_user, '<domain>_engineer', 'MEMBER')
        THEN nama
        ELSE SPLIT_PART(nama, ' ', 1) || ' ***'
    END AS nama,
    -- NIK: mask untuk non-engineer
    CASE
        WHEN pg_has_role(current_user, '<domain>_engineer', 'MEMBER')
        THEN nik
        ELSE LEFT(nik, 6) || REPEAT('*', 10)
    END AS nik,
    -- Tanggal lahir: mask ke tahun saja untuk non-engineer
    CASE
        WHEN pg_has_role(current_user, '<domain>_engineer', 'MEMBER')
        THEN tanggal_lahir
        ELSE DATE_TRUNC('year', tanggal_lahir)::date
    END AS tanggal_lahir,
    -- Golongan darah: sembunyikan sepenuhnya untuk non-medical
    CASE
        WHEN pg_has_role(current_user, '<domain>_engineer', 'MEMBER')
            OR pg_has_role(current_user, 'medical_role', 'MEMBER')
        THEN golongan_darah
        ELSE NULL
    END AS golongan_darah,
    -- Kolom non-PII: tampil penuh
    status,
    kategori,
    valid_from,
    is_current,
    version
FROM <schema>.dim_<entitas>
WHERE is_current = true;

-- Berikan akses ke view ini, bukan ke tabel langsung
GRANT SELECT ON <schema>.v_dim_<entitas>_masked
    TO <domain>_analyst, <domain>_consumer, <domain>_dq;
REVOKE SELECT ON <schema>.dim_<entitas>
    FROM <domain>_analyst, <domain>_consumer, <domain>_dq;
```

---

## Bagian 5 — Prosedur Permohonan Akses

### 5.1 Alur Permohonan Akses Baru

```
Pemohon mengisi formulir permohonan akses
  |
  v
Data Steward verifikasi kebutuhan bisnis (1 hari kerja)
  |
  v
DPO review jika melibatkan akses ke data restricted/confidential (2 hari kerja)
  |
  v
DBA provisioning akses (1 hari kerja)
  |
  v
Pemohon menerima akses + onboarding brief tentang kebijakan penggunaan
  |
  v
Akses dicatat di Access Registry (Bagian 7)
```

### 5.2 Matriks Approval

| Tipe Akses yang Dimohon | Approval Diperlukan | SLA Proses |
|---|---|---|
| Akses ke Gold layer non-PII (public/internal) | Data Steward | 2 hari kerja |
| Akses ke Gold layer dengan PII (R-MASKED) | Data Steward + DPO | 3 hari kerja |
| Akses ke Gold layer dengan PII penuh (R-FULL) | Data Steward + DPO + Data Product Owner | 5 hari kerja |
| Akses ke Silver/Bronze layer | Data Steward + DPO + CISO | 7 hari kerja |
| Akses Audit (audit schema, time-bound) | DPO + CISO | 5 hari kerja |
| Perpanjangan akses (setelah review tahunan) | Data Steward | 2 hari kerja |

### 5.3 Syarat Permohonan

Pemohon wajib menyertakan dalam formulir:

- Nama lengkap dan jabatan pemohon
- Nama tim/organisasi
- Tabel/view/API yang akan diakses
- Tujuan penggunaan yang spesifik (bukan generik seperti "untuk analisis")
- Perkiraan durasi kebutuhan akses
- Pernyataan kesanggupan mematuhi kebijakan penggunaan data
- Tanda tangan atasan langsung pemohon (untuk akses ke data restricted/confidential)

### 5.4 Pencabutan Akses

Akses dicabut secara otomatis atau manual dalam kondisi berikut:

| Kondisi | Tindakan | Siapa yang Memicu |
|---|---|---|
| Pegawai resign atau pindah divisi | Cabut akses dalam 1 hari kerja | HR + Data Steward |
| Akses time-bound sudah habis | Cabut otomatis via script harian | DBA (automated) |
| Pelanggaran kebijakan penggunaan data | Cabut segera, investigasi, laporan ke DPO | CISO + DPO |
| Audit tahunan menemukan akses tidak lagi diperlukan | Cabut setelah notifikasi 14 hari | Data Steward |

---

## Bagian 6 — Row-Level Security (RLS)

Untuk data product yang perlu membatasi akses tidak hanya per kolom tapi juga per baris data, definisikan policy RLS di sini.

| Tabel | Role | Kondisi RLS | Alasan |
|---|---|---|---|
| `<schema>.dim_<entitas>` | `<domain>_analyst` | `is_current = true AND deleted_at IS NULL` | Analyst hanya perlu lihat data aktif saat ini |
| `<schema>.fact_<regional>` | `consumer_wilayah_a` | `kode_wilayah = current_setting('app.kode_wilayah')` | Consumer dari wilayah A hanya bisa lihat data wilayah mereka |
| `<schema>.fact_<regional>` | `consumer_wilayah_b` | `kode_wilayah = current_setting('app.kode_wilayah')` | Idem untuk wilayah B |

**Implementasi RLS multi-tenant (jika applicable):**

```sql
-- Aktifkan RLS pada tabel
ALTER TABLE <schema>.fact_<regional> ENABLE ROW LEVEL SECURITY;

-- Policy: consumer hanya bisa lihat data wilayah mereka sendiri
-- kode_wilayah disetel oleh API saat membuka koneksi:
-- SET app.kode_wilayah = 'JKT01';
CREATE POLICY policy_consumer_wilayah
    ON <schema>.fact_<regional>
    FOR SELECT
    TO <domain>_consumer
    USING (
        kode_wilayah = current_setting('app.kode_wilayah', true)
        OR current_setting('app.kode_wilayah', true) = 'ALL'
    );

-- Policy: analyst bisa lihat semua wilayah
CREATE POLICY policy_analyst_all_regions
    ON <schema>.fact_<regional>
    FOR SELECT
    TO <domain>_analyst
    USING (true);

-- Policy: engineer bisa akses segalanya
CREATE POLICY policy_engineer_all
    ON <schema>.fact_<regional>
    FOR ALL
    TO <domain>_engineer
    USING (true) WITH CHECK (true);
```

---

## Bagian 7 — Access Registry (Daftar Akses Aktif)

`[Mandatory — perbarui setiap ada perubahan akses]`

Daftar semua individu dan sistem yang saat ini memiliki akses aktif ke data product ini.

| # | Nama / Sistem | Role Bisnis | Role PostgreSQL | Tanggal Diberikan | Tanggal Kadaluarsa | Approval | Tujuan |
|---|---|---|---|---|---|---|---|
| 1 | `<Nama DE 1>` | Data Engineer | `<domain>_engineer` | `<YYYY-MM-DD>` | Tidak terbatas | DPO | Pipeline development |
| 2 | `<Nama Analyst 1>` | Data Analyst | `<domain>_analyst` | `<YYYY-MM-DD>` | `<YYYY-MM-DD>` | DS + DPO | Analisis operasional bulanan |
| 3 | `<Nama Aplikasi>` | Consumer System | `<domain>_consumer` | `<YYYY-MM-DD>` | Tidak terbatas | DS + DPO | Layanan mobile app |
| 4 | `<Nama Auditor>` | Auditor Internal | `<domain>_audit_role` | `<YYYY-MM-DD>` | `<YYYY-MM-DD + 90 hari>` | DPO + CISO | Audit kepatuhan Q1 2025 |

---

## Bagian 8 — Jadwal Review Akses

| Tipe Review | Frekuensi | Pelaksana | Cakupan |
|---|---|---|---|
| Access Registry Review | Kuartalan | Data Steward | Verifikasi semua entri masih relevan dan tidak kadaluarsa |
| Full Access Audit | Semesteran | Data Steward + DPO | Verifikasi alignment antara Access Registry dan akses aktual di database |
| Emergency Review | Ad-hoc (saat insiden) | DPO + CISO | Tinjau semua akses setelah insiden keamanan atau data breach |
| Annual Re-certification | Tahunan | DPO | Setiap pemegang akses wajib re-certify kebutuhan akses mereka |

**Query verifikasi akses aktual di PostgreSQL:**

```sql
-- Cek semua role dan hak akses yang aktual di database
-- Gunakan untuk verifikasi saat audit
SELECT
    grantee,
    table_schema,
    table_name,
    privilege_type,
    is_grantable
FROM information_schema.role_table_grants
WHERE table_schema = '<domain_schema>'
ORDER BY grantee, table_schema, table_name;

-- Cek keanggotaan role
SELECT
    r.rolname                   AS role_name,
    m.rolname                   AS member_of,
    pg_catalog.pg_get_userbyid(gm.roleid) AS granted_by
FROM pg_catalog.pg_auth_members gm
JOIN pg_catalog.pg_roles r ON r.oid = gm.member
JOIN pg_catalog.pg_roles m ON m.oid = gm.roleid
WHERE r.rolname LIKE '<domain>%'
ORDER BY role_name;

-- Cek akses tabel yang efektif untuk user tertentu
SELECT
    table_schema,
    table_name,
    privilege_type
FROM information_schema.role_table_grants
WHERE grantee = '<username_atau_role>'
ORDER BY table_schema, table_name;
```

---

## Bagian 9 — Dasar Hukum dan Kepatuhan

| Regulasi | Kewajiban | Implementasi dalam Dokumen Ini |
|---|---|---|
| **UU No. 27 Tahun 2022 (UU PDP) Pasal 16** | Pengendali data wajib membatasi penggunaan data pribadi sesuai tujuan pemrosesan | Kolom pembatasan penggunaan di Bagian 5.2 |
| **UU PDP Pasal 20** | Pemrosesan wajib ada dasar hukum yang sah | Kolom dasar hukum masking di Bagian 4.1 |
| **UU PDP Pasal 34** | Pengendali wajib melindungi keamanan data pribadi secara teknis dan organisasional | Implementasi RBAC + masking + RLS di Bagian 3-6 |
| **UU PDP Pasal 47** | Wajib mencatat seluruh kegiatan pemrosesan | Access Registry di Bagian 7 + audit log |
| **PP 71/2019 Pasal 17** | Sistem elektronik yang memproses data pribadi wajib memiliki kontrol akses | Seluruh dokumen ini |
| **ISO 27001:2022 A.5.15** | Access control policy wajib didokumentasikan dan direview berkala | Review cycle di Bagian 8 |
| **ISO 27001:2022 A.8.4** | Akses ke source code dan data harus dikelola secara eksplisit | Access Registry + prosedur di Bagian 5 |

---

## Sign-Off

`[Mandatory sebelum dokumen ini berlaku efektif]`

| Role | Nama | Persetujuan | Tanggal |
|---|---|---|---|
| Data Product Owner | `<Nama>` | Disetujui / Perlu Revisi | |
| Data Steward | `<Nama>` | Disetujui / Perlu Revisi | |
| DPO / Legal Officer | `<Nama>` | Disetujui / Perlu Revisi | |
| CISO / Security | `<Nama>` | Disetujui / Perlu Revisi | |
