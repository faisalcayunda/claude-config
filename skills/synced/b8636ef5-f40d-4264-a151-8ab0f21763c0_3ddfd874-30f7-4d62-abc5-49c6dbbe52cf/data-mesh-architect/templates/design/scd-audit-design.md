---
title: "SCD & Audit Logging Design — <Nama Data Product>"
sidebar_label: "SCD & Audit Design"
sidebar_position: 12
description: "Desain Slowly Changing Dimensions dan audit logging untuk kebutuhan compliance, rekonstruksi historis, dan change tracking menggunakan PostgreSQL"
tags: [design, scd, audit-log, temporal, postgresql, data-history, compliance]
data_product_id: "<domain>/<data-product-name>/v<version>"
data_product_owner: "<Nama Domain>"
data_classification: "<Public|Internal|Restricted|Confidential>"
phase: design
version: "0.1.0"
last_updated: "<YYYY-MM-DD>"
pii_flag: <true|false>
---

# SCD & Audit Logging Design

> **Tujuan dokumen ini:** Mendefinisikan strategi Slowly Changing Dimensions (SCD) dan mekanisme audit logging untuk setiap tabel dalam data product. Keputusan ini menentukan kemampuan rekonstruksi historis, kepatuhan regulasi, dan kemampuan debug data yang tersimpan.

:::info Mengapa ini penting
Tanpa strategi SCD yang eksplisit, data product kehilangan kemampuan untuk: menjawab "bagaimana kondisi data pada tanggal X?", membuktikan kepatuhan terhadap UU PDP (retensi dan penghapusan), merekonstruksi state bisnis saat terjadi dispute, dan men-debug anomali yang terjadi di masa lalu.
:::

---

## Riwayat Versi

| Tanggal | Versi | Deskripsi | Penulis |
|---|---|---|---|
| `<YYYY-MM-DD>` | 0.1 | Versi awal | `<Nama>` |

---

## 1. Referensi Cepat: Tipe SCD

Gunakan tabel ini untuk memilih tipe SCD yang tepat per tabel sebelum membaca detail implementasi.

| Tipe | Nama | Cara Kerja | Kapan Digunakan | Ukuran Tabel |
|---|---|---|---|---|
| **Type 0** | Fixed / Immutable | Tidak ada perubahan diizinkan | Kode referensi, konstanta bisnis | Minimal |
| **Type 1** | Overwrite | Update nilai langsung, hapus riwayat | Data yang tidak butuh histori, koreksi kesalahan input | Kecil |
| **Type 2** | Row Versioning | Tambah baris baru per perubahan, tandai versi aktif | Standar gold standard untuk dimensi — butuh rekonstruksi historis | Besar (linear dengan jumlah perubahan) |
| **Type 3** | Previous Column | Tambah kolom `prev_nilai` | Hanya butuh 1 lapis histori, jarang berubah | Kecil |
| **Type 4** | Separate History Table | Tabel current + tabel audit terpisah | Data berubah sering, query perlu cepat untuk current, histori sebagai lampiran | Sedang — 2 tabel |
| **Type 6** | Hybrid (1+2+3) | Simpan current value di row aktif, full history di baris lama, prev column | Perlu akses cepat ke current state DAN full historical reconstruction | Besar |

**Rekomendasi umum untuk data product:**

| Konteks | Tipe yang Direkomendasikan |
|---|---|
| Master data (profil entitas, referensi wilayah) | Type 2 |
| Data transaksi / fact table | Type 1 atau Type 4 (tidak perlu ubah baris transaksi yang sudah terjadi) |
| Konfigurasi sistem | Type 2 |
| Tabel lookup / kode referensi | Type 0 atau Type 1 |
| Entitas dengan PII — wajib audit untuk UU PDP | Type 2 + Type 4 (kombinasi) |

---

## 2. Keputusan SCD per Tabel

`[Mandatory — isi untuk setiap tabel dalam data product]`

| Tabel | Tipe SCD | Alasan | Kolom Versi | Audit Log? |
|---|---|---|---|---|
| `<dim_entitas_a>` | `<Type 2>` | `<Profil entitas berubah, butuh rekonstruksi historis untuk audit keuangan>` | `<valid_from, valid_to, is_current, version>` | `<Ya — trigger audit>` |
| `<fact_transaksi_x>` | `<Type 1>` | `<Transaksi tidak berubah setelah di-commit; koreksi via jurnal baru>` | `<created_at saja>` | `<Ya — immutable audit log>` |
| `<dim_referensi_kode>` | `<Type 0>` | `<Kode referensi hanya tambah, tidak pernah hapus atau ubah>` | `<created_at saja>` | `<Tidak diperlukan>` |

---

## 3. Implementasi SCD per Tipe — PostgreSQL

### 3.1 SCD Type 0 — Fixed / Immutable

Digunakan untuk tabel kode referensi atau data master yang tidak boleh berubah setelah diinsert.

```sql
-- ============================================================
-- SCD TYPE 0: IMMUTABLE REFERENCE TABLE
-- Strategi: Hanya INSERT yang diizinkan. UPDATE dan DELETE
-- dicegah di level database melalui rule/trigger.
-- ============================================================
CREATE TABLE ref_kode_wilayah (
    kode_wilayah    VARCHAR(10)     NOT NULL,
    nama_wilayah    VARCHAR(255)    NOT NULL,
    level           VARCHAR(20)     NOT NULL CHECK (level IN ('provinsi','kabupaten','kecamatan','desa')),
    kode_induk      VARCHAR(10),
    berlaku_sejak   DATE            NOT NULL,   -- kapan kode ini mulai berlaku
    sumber          VARCHAR(100)    NOT NULL,   -- misal: Permendagri No. X/2025
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT now(),

    CONSTRAINT pk_ref_kode_wilayah PRIMARY KEY (kode_wilayah),
    CONSTRAINT fk_kode_induk FOREIGN KEY (kode_induk)
        REFERENCES ref_kode_wilayah(kode_wilayah)
);

-- Cegah UPDATE dan DELETE melalui rule
CREATE RULE no_update_ref_kode AS ON UPDATE TO ref_kode_wilayah
    DO INSTEAD NOTHING;

CREATE RULE no_delete_ref_kode AS ON DELETE TO ref_kode_wilayah
    DO INSTEAD NOTHING;

-- Atau alternatif menggunakan trigger (lebih informatif dengan pesan error):
CREATE OR REPLACE FUNCTION fn_prevent_mutation_ref()
RETURNS TRIGGER AS $$
BEGIN
    RAISE EXCEPTION 'Tabel % bersifat immutable. Gunakan kode baru untuk menggantikan kode yang tidak berlaku.', TG_TABLE_NAME;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_immutable_ref_kode
    BEFORE UPDATE OR DELETE ON ref_kode_wilayah
    FOR EACH ROW EXECUTE FUNCTION fn_prevent_mutation_ref();
```

---

### 3.2 SCD Type 1 — Overwrite (No History)

Digunakan untuk atribut yang tidak butuh riwayat. Nilai lama ditimpa.

```sql
-- ============================================================
-- SCD TYPE 1: OVERWRITE WITHOUT HISTORY
-- Strategi: UPDATE langsung. Tidak ada baris versi lama.
-- Gunakan untuk: koreksi kesalahan ketik, data tidak material.
-- CATATAN: Jika tabel ini berisi PII, wajib pasang audit trigger
--          di bawah (Bagian 6) untuk kepatuhan UU PDP.
-- ============================================================
CREATE TABLE dim_konfigurasi_sistem (
    konfigurasi_id  UUID            NOT NULL DEFAULT gen_random_uuid(),
    kunci           VARCHAR(100)    NOT NULL,   -- nama parameter
    nilai           TEXT            NOT NULL,   -- nilai parameter
    deskripsi       TEXT,
    diubah_oleh     TEXT            NOT NULL,   -- username/service account
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT now(),

    CONSTRAINT pk_konfigurasi PRIMARY KEY (konfigurasi_id),
    CONSTRAINT uq_konfigurasi_kunci UNIQUE (kunci)
);

-- Auto-update updated_at saat ada perubahan
CREATE OR REPLACE FUNCTION fn_set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_konfigurasi_updated_at
    BEFORE UPDATE ON dim_konfigurasi_sistem
    FOR EACH ROW EXECUTE FUNCTION fn_set_updated_at();
```

---

### 3.3 SCD Type 2 — Row Versioning (Full History)

**Standard untuk tabel dimensi di data product.** Setiap perubahan atribut menghasilkan baris baru. Baris lama ditutup dengan `valid_to`. Hanya satu baris `is_current = true` per `business_key`.

```sql
-- ============================================================
-- SCD TYPE 2: ROW VERSIONING — FULL HISTORICAL RECORD
-- Kolom wajib:
--   surrogate_key : UUID — primary key unik per versi baris
--   business_key  : identitas bisnis entitas (bisa composite)
--   valid_from    : kapan versi ini mulai berlaku (inklusif)
--   valid_to      : kapan versi ini berakhir (eksklusif); 'infinity' = masih aktif
--   is_current    : shortcut untuk filter versi aktif
--   version       : urutan versi untuk entitas ini (1, 2, 3...)
-- ============================================================

CREATE TABLE dim_profil_entitas (
    -- Surrogate key (satu per versi)
    profil_id       UUID            NOT NULL DEFAULT gen_random_uuid(),

    -- Business key (tetap sama di semua versi)
    entitas_id      VARCHAR(36)     NOT NULL,   -- ID asli dari sistem sumber

    -- Atribut bisnis yang bisa berubah
    nama            VARCHAR(255)    NOT NULL,
    kategori        VARCHAR(50)     NOT NULL,
    status          VARCHAR(20)     NOT NULL CHECK (status IN ('aktif', 'nonaktif', 'pending')),
    alamat_kota     VARCHAR(100),
    -- Kolom PII — masking diterapkan di view
    nik             VARCHAR(16),

    -- SCD Type 2 control columns
    valid_from      TIMESTAMPTZ     NOT NULL DEFAULT now(),
    valid_to        TIMESTAMPTZ     NOT NULL DEFAULT 'infinity'::timestamptz,
    is_current      BOOLEAN         NOT NULL DEFAULT true,
    version         INTEGER         NOT NULL DEFAULT 1,

    -- Audit metadata
    created_at      TIMESTAMPTZ     NOT NULL DEFAULT now(),
    created_by      TEXT            NOT NULL DEFAULT current_user,
    source_system   VARCHAR(100),   -- sistem mana data ini berasal
    load_id         UUID,           -- ID pipeline run yang memuat baris ini

    CONSTRAINT pk_dim_profil_entitas PRIMARY KEY (profil_id),

    -- Satu business key hanya boleh punya SATU baris is_current = true
    CONSTRAINT uq_profil_entitas_current
        UNIQUE (entitas_id, is_current)
        WHERE (is_current = true),

    -- Validasi: valid_from harus sebelum valid_to
    CONSTRAINT chk_valid_period
        CHECK (valid_from < valid_to),

    -- Validasi: versi minimal 1
    CONSTRAINT chk_version_positive
        CHECK (version >= 1)
);

-- Index untuk performa query umum
CREATE INDEX idx_profil_entitas_business_key
    ON dim_profil_entitas (entitas_id);

CREATE INDEX idx_profil_entitas_current
    ON dim_profil_entitas (entitas_id, is_current)
    WHERE is_current = true;

CREATE INDEX idx_profil_entitas_valid_period
    ON dim_profil_entitas USING BTREE (entitas_id, valid_from, valid_to);

-- Untuk point-in-time query yang efisien menggunakan GIST index:
-- Memerlukan extension btree_gist
CREATE EXTENSION IF NOT EXISTS btree_gist;

-- Mencegah periode yang overlap untuk business_key yang sama
ALTER TABLE dim_profil_entitas
    ADD CONSTRAINT no_overlapping_versions
    EXCLUDE USING gist (
        entitas_id  WITH =,
        tstzrange(valid_from, valid_to, '[)') WITH &&
    );

-- View: hanya baris aktif (shortcut untuk consumer)
CREATE VIEW v_dim_profil_entitas_current AS
    SELECT * FROM dim_profil_entitas
    WHERE is_current = true;

-- View: query point-in-time (state pada waktu tertentu)
-- Penggunaan: SELECT * FROM fn_profil_at_time('entitas-001', '2024-06-01')
CREATE OR REPLACE FUNCTION fn_profil_at_time(
    p_entitas_id    VARCHAR,
    p_as_of         TIMESTAMPTZ
)
RETURNS TABLE (LIKE dim_profil_entitas)
LANGUAGE sql STABLE AS $$
    SELECT * FROM dim_profil_entitas
    WHERE entitas_id = p_entitas_id
      AND valid_from <= p_as_of
      AND valid_to    > p_as_of
    LIMIT 1;
$$;
```

**Prosedur upsert SCD Type 2 (dijalankan oleh pipeline):**

```sql
-- ============================================================
-- SCD TYPE 2 UPSERT PROCEDURE
-- Dipanggil oleh pipeline setiap batch run.
-- Input: staging table berisi baris baru dari sumber.
-- ============================================================

CREATE OR REPLACE PROCEDURE sp_upsert_scd2_profil(
    p_load_id       UUID,
    p_source_system TEXT
)
LANGUAGE plpgsql AS $$
DECLARE
    v_closed_count  INTEGER;
    v_inserted_count INTEGER;
BEGIN
    -- LANGKAH 1: Identifikasi baris yang BERUBAH
    -- (business_key ada di current, tapi atribut berbeda)
    CREATE TEMP TABLE tmp_changed AS
    SELECT
        stg.entitas_id,
        stg.nama,
        stg.kategori,
        stg.status,
        stg.alamat_kota,
        stg.nik
    FROM staging_profil_entitas stg
    INNER JOIN dim_profil_entitas cur
        ON stg.entitas_id = cur.entitas_id
        AND cur.is_current = true
    WHERE
        stg.nama        IS DISTINCT FROM cur.nama        OR
        stg.kategori    IS DISTINCT FROM cur.kategori    OR
        stg.status      IS DISTINCT FROM cur.status      OR
        stg.alamat_kota IS DISTINCT FROM cur.alamat_kota OR
        stg.nik         IS DISTINCT FROM cur.nik;

    -- LANGKAH 2: Tutup versi lama untuk baris yang berubah
    UPDATE dim_profil_entitas
    SET
        valid_to    = now(),
        is_current  = false
    WHERE
        entitas_id  IN (SELECT entitas_id FROM tmp_changed)
        AND is_current = true;

    GET DIAGNOSTICS v_closed_count = ROW_COUNT;

    -- LANGKAH 3: Insert versi BARU untuk baris yang berubah
    -- + Insert baris BARU (entitas_id belum pernah ada)
    INSERT INTO dim_profil_entitas (
        entitas_id, nama, kategori, status, alamat_kota, nik,
        valid_from, valid_to, is_current, version,
        created_by, source_system, load_id
    )
    SELECT
        stg.entitas_id,
        stg.nama,
        stg.kategori,
        stg.status,
        stg.alamat_kota,
        stg.nik,
        now()                           AS valid_from,
        'infinity'::timestamptz         AS valid_to,
        true                            AS is_current,
        COALESCE(max_ver.max_version, 0) + 1 AS version,
        p_source_system,
        p_source_system,
        p_load_id
    FROM staging_profil_entitas stg
    -- Ambil versi terakhir untuk menentukan version number
    LEFT JOIN (
        SELECT entitas_id, MAX(version) AS max_version
        FROM dim_profil_entitas
        GROUP BY entitas_id
    ) max_ver ON stg.entitas_id = max_ver.entitas_id
    -- Hanya baris yang berubah atau baru
    WHERE stg.entitas_id IN (SELECT entitas_id FROM tmp_changed)
       OR NOT EXISTS (
            SELECT 1 FROM dim_profil_entitas
            WHERE entitas_id = stg.entitas_id
       );

    GET DIAGNOSTICS v_inserted_count = ROW_COUNT;

    -- Cleanup
    DROP TABLE IF EXISTS tmp_changed;

    RAISE NOTICE 'SCD Type 2 upsert selesai: % baris ditutup, % baris baru diinsert',
        v_closed_count, v_inserted_count;
END;
$$;
```

---

### 3.4 SCD Type 3 — Previous Value Column

Digunakan ketika hanya butuh satu lapis histori (current dan previous). Jarang digunakan untuk data product yang serius karena keterbatasan histori.

```sql
-- ============================================================
-- SCD TYPE 3: PREVIOUS VALUE COLUMN
-- Cocok untuk: atribut yang jarang berubah dan hanya butuh
-- 1 lapis histori (misalnya: kategori setelah re-klasifikasi).
-- KETERBATASAN: Hanya simpan 1 perubahan terakhir.
-- ============================================================
CREATE TABLE dim_kategori_entitas (
    entitas_id          VARCHAR(36)     NOT NULL,

    -- Current value
    kategori_saat_ini   VARCHAR(50)     NOT NULL,
    berlaku_sejak       DATE            NOT NULL,

    -- Previous value (Type 3)
    kategori_sebelumnya VARCHAR(50),             -- NULL jika belum pernah berubah
    berlaku_sampai      DATE,                   -- NULL jika belum pernah berubah

    updated_at          TIMESTAMPTZ     NOT NULL DEFAULT now(),

    CONSTRAINT pk_dim_kategori PRIMARY KEY (entitas_id)
);

-- Prosedur update Type 3: geser current ke previous sebelum update
CREATE OR REPLACE FUNCTION fn_update_scd3_kategori(
    p_entitas_id        VARCHAR,
    p_kategori_baru     VARCHAR,
    p_berlaku_sejak     DATE
) RETURNS VOID LANGUAGE plpgsql AS $$
BEGIN
    UPDATE dim_kategori_entitas
    SET
        -- Geser current ke previous
        kategori_sebelumnya = kategori_saat_ini,
        berlaku_sampai      = p_berlaku_sejak - 1,
        -- Set current yang baru
        kategori_saat_ini   = p_kategori_baru,
        berlaku_sejak       = p_berlaku_sejak,
        updated_at          = now()
    WHERE entitas_id = p_entitas_id;
END;
$$;
```

---

### 3.5 SCD Type 4 — Separate History / Audit Table

Tabel utama hanya berisi state terkini (performa query optimal). Tabel history terpisah menyimpan semua perubahan sebagai ledger append-only. **Ini adalah pola yang digunakan untuk kebutuhan audit compliance.**

```sql
-- ============================================================
-- SCD TYPE 4: SEPARATE HISTORY TABLE
-- Tabel utama: state terkini, performa query tinggi.
-- Tabel history: append-only ledger semua perubahan.
-- Cocok untuk: fact tables, entitas yang sering berubah,
--              kebutuhan audit compliance.
-- ============================================================

-- Tabel utama — current state
CREATE TABLE dim_anggota (
    anggota_id      UUID            NOT NULL DEFAULT gen_random_uuid(),
    kode_anggota    VARCHAR(20)     NOT NULL,
    nama            VARCHAR(255)    NOT NULL,
    status          VARCHAR(20)     NOT NULL,
    tier            VARCHAR(20)     NOT NULL,
    updated_at      TIMESTAMPTZ     NOT NULL DEFAULT now(),
    updated_by      TEXT            NOT NULL DEFAULT current_user,

    CONSTRAINT pk_dim_anggota PRIMARY KEY (anggota_id),
    CONSTRAINT uq_dim_anggota_kode UNIQUE (kode_anggota)
);

-- Tabel history — semua versi, append-only
CREATE TABLE dim_anggota_history (
    history_id      BIGSERIAL       NOT NULL,
    anggota_id      UUID            NOT NULL,   -- FK ke tabel utama
    kode_anggota    VARCHAR(20)     NOT NULL,
    nama            VARCHAR(255)    NOT NULL,
    status          VARCHAR(20)     NOT NULL,
    tier            VARCHAR(20)     NOT NULL,
    operation       TEXT            NOT NULL CHECK (operation IN ('INSERT','UPDATE','DELETE')),
    changed_at      TIMESTAMPTZ     NOT NULL DEFAULT now(),
    changed_by      TEXT            NOT NULL DEFAULT current_user,
    client_app      TEXT,                       -- nama aplikasi yang melakukan perubahan
    old_values      JSONB,                      -- snapshot sebelum perubahan
    new_values      JSONB,                      -- snapshot setelah perubahan

    CONSTRAINT pk_anggota_history PRIMARY KEY (history_id)
);

-- Index untuk query histori per entitas
CREATE INDEX idx_anggota_history_id
    ON dim_anggota_history (anggota_id, changed_at DESC);

CREATE INDEX idx_anggota_history_operation
    ON dim_anggota_history (operation, changed_at DESC);

-- Trigger: otomatis isi tabel history setiap ada perubahan
CREATE OR REPLACE FUNCTION fn_audit_dim_anggota()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO dim_anggota_history (
        anggota_id, kode_anggota, nama, status, tier,
        operation, changed_by, client_app,
        old_values, new_values
    )
    VALUES (
        CASE WHEN TG_OP = 'DELETE' THEN OLD.anggota_id ELSE NEW.anggota_id END,
        CASE WHEN TG_OP = 'DELETE' THEN OLD.kode_anggota ELSE NEW.kode_anggota END,
        CASE WHEN TG_OP = 'DELETE' THEN OLD.nama ELSE NEW.nama END,
        CASE WHEN TG_OP = 'DELETE' THEN OLD.status ELSE NEW.status END,
        CASE WHEN TG_OP = 'DELETE' THEN OLD.tier ELSE NEW.tier END,
        TG_OP,
        current_user,
        current_setting('application_name', true),
        CASE WHEN TG_OP IN ('UPDATE','DELETE') THEN to_jsonb(OLD) ELSE NULL END,
        CASE WHEN TG_OP IN ('INSERT','UPDATE') THEN to_jsonb(NEW) ELSE NULL END
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER trg_audit_dim_anggota
    AFTER INSERT OR UPDATE OR DELETE ON dim_anggota
    FOR EACH ROW EXECUTE FUNCTION fn_audit_dim_anggota();
```

---

### 3.6 SCD Type 6 — Hybrid (Type 1 + Type 2 + Type 3)

Menggabungkan tiga pendekatan: full row history (Type 2), current value di setiap baris historis (Type 1 overwrite), dan previous value column (Type 3). Memberikan fleksibilitas query tertinggi dengan cost storage terbesar.

```sql
-- ============================================================
-- SCD TYPE 6: HYBRID
-- Setiap baris historis menyimpan:
--   - Nilai saat periode tersebut berlaku (attr_pada_waktu)
--   - Nilai SAAT INI dari entitas (attr_saat_ini) — di-overwrite setiap update
--   - Nilai SEBELUMNYA (attr_sebelumnya) — Type 3
--   - Kontrol periode Type 2 (valid_from, valid_to, is_current)
-- Kegunaan: analitik yang butuh perbandingan "dulu vs sekarang"
--           pada satu query tanpa subquery temporal.
-- ============================================================

CREATE TABLE dim_segmen_pelanggan_t6 (
    -- Surrogate key
    segmen_id           UUID            NOT NULL DEFAULT gen_random_uuid(),
    -- Business key
    pelanggan_id        VARCHAR(36)     NOT NULL,

    -- Atribut "pada waktu itu" (Type 2 — tidak berubah per baris)
    segmen_pada_waktu   VARCHAR(50)     NOT NULL,

    -- Atribut "saat ini" (Type 1 — di-overwrite ke semua baris saat ada perubahan)
    segmen_saat_ini     VARCHAR(50)     NOT NULL,

    -- Atribut "sebelumnya" (Type 3 — satu lapis histori di baris aktif)
    segmen_sebelumnya   VARCHAR(50),

    -- Type 2 control columns
    valid_from          TIMESTAMPTZ     NOT NULL DEFAULT now(),
    valid_to            TIMESTAMPTZ     NOT NULL DEFAULT 'infinity'::timestamptz,
    is_current          BOOLEAN         NOT NULL DEFAULT true,
    version             INTEGER         NOT NULL DEFAULT 1,

    CONSTRAINT pk_segmen_pelanggan_t6 PRIMARY KEY (segmen_id),
    CONSTRAINT uq_segmen_current
        UNIQUE (pelanggan_id, is_current)
        WHERE (is_current = true),
    CONSTRAINT chk_valid_period
        CHECK (valid_from < valid_to)
);

-- Saat ada perubahan segmen:
-- 1. Update segmen_saat_ini di SEMUA baris historis entitas ini
-- 2. Update segmen_sebelumnya di baris aktif
-- 3. Tutup baris aktif (set is_current = false, valid_to = now())
-- 4. Insert baris baru
CREATE OR REPLACE PROCEDURE sp_upsert_scd6_segmen(
    p_pelanggan_id      VARCHAR,
    p_segmen_baru       VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_segmen_lama   VARCHAR;
BEGIN
    -- Ambil nilai lama untuk Type 3
    SELECT segmen_saat_ini INTO v_segmen_lama
    FROM dim_segmen_pelanggan_t6
    WHERE pelanggan_id = p_pelanggan_id AND is_current = true;

    IF v_segmen_lama IS NOT NULL AND v_segmen_lama != p_segmen_baru THEN
        -- Step 1: Update segmen_saat_ini di semua baris historis (Type 1 overwrite)
        UPDATE dim_segmen_pelanggan_t6
        SET segmen_saat_ini = p_segmen_baru
        WHERE pelanggan_id = p_pelanggan_id;

        -- Step 2: Update previous column di baris aktif (Type 3)
        UPDATE dim_segmen_pelanggan_t6
        SET segmen_sebelumnya = v_segmen_lama
        WHERE pelanggan_id = p_pelanggan_id AND is_current = true;

        -- Step 3: Tutup versi aktif (Type 2 close)
        UPDATE dim_segmen_pelanggan_t6
        SET valid_to = now(), is_current = false
        WHERE pelanggan_id = p_pelanggan_id AND is_current = true;

        -- Step 4: Insert versi baru
        INSERT INTO dim_segmen_pelanggan_t6 (
            pelanggan_id, segmen_pada_waktu, segmen_saat_ini,
            segmen_sebelumnya, valid_from, version
        )
        SELECT
            p_pelanggan_id, p_segmen_baru, p_segmen_baru,
            v_segmen_lama, now(),
            MAX(version) + 1
        FROM dim_segmen_pelanggan_t6
        WHERE pelanggan_id = p_pelanggan_id;
    END IF;
END;
$$;
```

---

## 4. Generic Audit Log Table

Satu tabel audit yang dapat digunakan untuk seluruh tabel dalam data product. Lebih efisien dibanding membuat tabel history terpisah per tabel.

```sql
-- ============================================================
-- GENERIC AUDIT LOG TABLE
-- Digunakan untuk: compliance audit, forensics, debugging,
--                  kepatuhan UU PDP (siapa mengubah PII kapan).
-- Semua perubahan di semua tabel tercatat di sini.
-- ============================================================

CREATE TABLE audit_log (
    audit_id        BIGSERIAL           NOT NULL,
    schema_name     TEXT                NOT NULL,
    table_name      TEXT                NOT NULL,
    record_id       TEXT                NOT NULL,   -- cast to TEXT untuk fleksibilitas
    operation       TEXT                NOT NULL CHECK (operation IN ('INSERT','UPDATE','DELETE','TRUNCATE')),
    old_values      JSONB,                          -- NULL untuk INSERT
    new_values      JSONB,                          -- NULL untuk DELETE
    changed_columns TEXT[],                         -- kolom yang berubah pada UPDATE
    changed_by      TEXT                NOT NULL DEFAULT current_user,
    changed_at      TIMESTAMPTZ         NOT NULL DEFAULT now(),
    application     TEXT DEFAULT current_setting('application_name', true),
    client_addr     INET,                           -- IP client jika tersedia
    session_id      TEXT DEFAULT pg_backend_pid()::text,
    transaction_id  BIGINT DEFAULT txid_current(),  -- untuk group changes dalam 1 transaksi

    CONSTRAINT pk_audit_log PRIMARY KEY (audit_id)
) PARTITION BY RANGE (changed_at);   -- Partisi per bulan untuk manajemen retensi

-- Buat partisi bulanan (contoh untuk 2025)
CREATE TABLE audit_log_2025_01 PARTITION OF audit_log
    FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');
CREATE TABLE audit_log_2025_02 PARTITION OF audit_log
    FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');
-- dst. — atau gunakan pg_partman untuk otomatisasi

-- Index untuk query audit yang umum
CREATE INDEX idx_audit_log_table_record
    ON audit_log (table_name, record_id, changed_at DESC);

CREATE INDEX idx_audit_log_changed_by
    ON audit_log (changed_by, changed_at DESC);

CREATE INDEX idx_audit_log_changed_at
    ON audit_log (changed_at DESC);

-- ============================================================
-- GENERIC AUDIT TRIGGER FUNCTION
-- Satu fungsi untuk semua tabel.
-- Deteksi otomatis kolom yang berubah (untuk UPDATE).
-- ============================================================
CREATE OR REPLACE FUNCTION fn_generic_audit_trigger()
RETURNS TRIGGER AS $$
DECLARE
    v_old_values        JSONB;
    v_new_values        JSONB;
    v_changed_columns   TEXT[];
    v_record_id         TEXT;
BEGIN
    -- Tentukan nilai OLD dan NEW berdasarkan operasi
    CASE TG_OP
        WHEN 'INSERT' THEN
            v_old_values := NULL;
            v_new_values := to_jsonb(NEW);
            v_record_id  := NEW.id::TEXT;  -- Sesuaikan dengan nama PK tabel Anda

        WHEN 'UPDATE' THEN
            v_old_values := to_jsonb(OLD);
            v_new_values := to_jsonb(NEW);
            -- Deteksi kolom yang berubah
            SELECT ARRAY_AGG(key ORDER BY key)
            INTO v_changed_columns
            FROM jsonb_each(to_jsonb(NEW)) n
            JOIN jsonb_each(to_jsonb(OLD)) o USING (key)
            WHERE n.value IS DISTINCT FROM o.value;
            v_record_id := NEW.id::TEXT;

        WHEN 'DELETE' THEN
            v_old_values := to_jsonb(OLD);
            v_new_values := NULL;
            v_record_id  := OLD.id::TEXT;
    END CASE;

    -- Insert ke audit_log
    INSERT INTO audit_log (
        schema_name, table_name, record_id, operation,
        old_values, new_values, changed_columns,
        changed_by, client_addr
    )
    VALUES (
        TG_TABLE_SCHEMA,
        TG_TABLE_NAME,
        v_record_id,
        TG_OP,
        v_old_values,
        v_new_values,
        v_changed_columns,
        current_user,
        inet_client_addr()
    );

    RETURN COALESCE(NEW, OLD);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- ============================================================
-- CARA PASANG TRIGGER KE TABEL
-- Ganti <nama_tabel> dengan nama tabel target.
-- ============================================================
-- CREATE TRIGGER trg_audit_<nama_tabel>
--     AFTER INSERT OR UPDATE OR DELETE ON <schema>.<nama_tabel>
--     FOR EACH ROW EXECUTE FUNCTION fn_generic_audit_trigger();

-- Contoh:
CREATE TRIGGER trg_audit_dim_profil_entitas
    AFTER INSERT OR UPDATE OR DELETE ON dim_profil_entitas
    FOR EACH ROW EXECUTE FUNCTION fn_generic_audit_trigger();
```

---

## 5. Soft Delete Pattern

Untuk entitas yang tidak boleh dihapus secara fisik (diperlukan untuk audit trail dan referential integrity).

```sql
-- ============================================================
-- SOFT DELETE PATTERN
-- Gunakan bersama SCD Type 2 untuk penghapusan entitas.
-- deleted_at = NULL  → entitas aktif
-- deleted_at != NULL → entitas dihapus (soft delete)
-- ============================================================

-- Tambahkan kolom ke tabel SCD Type 2
ALTER TABLE dim_profil_entitas
    ADD COLUMN deleted_at       TIMESTAMPTZ DEFAULT NULL,
    ADD COLUMN deleted_by       TEXT        DEFAULT NULL,
    ADD COLUMN deletion_reason  TEXT        DEFAULT NULL;

-- View yang menyembunyikan soft-deleted records
CREATE OR REPLACE VIEW v_dim_profil_entitas_active AS
    SELECT * FROM dim_profil_entitas
    WHERE is_current = true
      AND deleted_at IS NULL;

-- Prosedur soft delete
CREATE OR REPLACE PROCEDURE sp_soft_delete_profil(
    p_entitas_id    VARCHAR,
    p_reason        TEXT,
    p_deleted_by    TEXT DEFAULT current_user
)
LANGUAGE plpgsql AS $$
BEGIN
    -- Tutup versi aktif dengan menandai sebagai deleted
    UPDATE dim_profil_entitas
    SET
        valid_to        = now(),
        is_current      = false,
        deleted_at      = now(),
        deleted_by      = p_deleted_by,
        deletion_reason = p_reason
    WHERE entitas_id = p_entitas_id
      AND is_current = true
      AND deleted_at IS NULL;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Entitas % tidak ditemukan atau sudah dihapus', p_entitas_id;
    END IF;
END;
$$;

-- Prosedur permanent purge PII (untuk pemenuhan UU PDP pasal 32 — right to erasure)
-- CATATAN: Ini menghapus PII dari record historis, tapi mempertahankan
-- aggregate/anonymized data untuk keperluan audit keuangan.
CREATE OR REPLACE PROCEDURE sp_anonymize_pii_profil(
    p_entitas_id    VARCHAR,
    p_legal_basis   TEXT    -- dokumentasi dasar hukum penghapusan
)
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE dim_profil_entitas
    SET
        nama    = 'ANONYMIZED_' || LEFT(MD5(nama), 8),
        nik     = '0000000000000000',    -- ganti dengan token kosong
        -- Kolom non-PII dipertahankan untuk keperluan statistik
        deletion_reason = 'PII_ERASED: ' || p_legal_basis,
        updated_at      = now()
    WHERE entitas_id = p_entitas_id;

    -- Catat di audit log bahwa PII sudah dihapus
    INSERT INTO audit_log (
        schema_name, table_name, record_id, operation,
        new_values, changed_by
    )
    VALUES (
        'public', 'dim_profil_entitas', p_entitas_id,
        'UPDATE',
        jsonb_build_object(
            'action', 'PII_ANONYMIZATION',
            'legal_basis', p_legal_basis,
            'anonymized_at', now()
        ),
        current_user
    );
END;
$$;
```

---

## 6. Query Patterns untuk Audit & Rekonstruksi Historis

```sql
-- ============================================================
-- QUERY PATTERNS YANG SERING DIGUNAKAN
-- ============================================================

-- 1. State entitas pada tanggal tertentu (point-in-time)
SELECT *
FROM dim_profil_entitas
WHERE entitas_id = 'ENT-001'
  AND valid_from <= '2024-06-15 00:00:00+07'::timestamptz
  AND valid_to    > '2024-06-15 00:00:00+07'::timestamptz;

-- 2. Riwayat lengkap semua perubahan satu entitas
SELECT
    version,
    valid_from,
    valid_to,
    is_current,
    nama,
    status,
    kategori,
    created_by,
    source_system
FROM dim_profil_entitas
WHERE entitas_id = 'ENT-001'
ORDER BY version;

-- 3. Entitas yang berubah dalam rentang waktu tertentu
SELECT DISTINCT entitas_id
FROM dim_profil_entitas
WHERE valid_from BETWEEN '2024-01-01'::timestamptz
                     AND '2024-03-31'::timestamptz;

-- 4. Audit trail perubahan PII — untuk compliance report
SELECT
    al.changed_at,
    al.changed_by,
    al.operation,
    al.changed_columns,
    al.client_addr,
    al.application
FROM audit_log al
WHERE al.table_name = 'dim_profil_entitas'
  AND al.record_id  = 'ENT-001'
  AND (
      al.changed_columns && ARRAY['nik','nama','tanggal_lahir']  -- berisi kolom PII
      OR al.operation IN ('DELETE')
  )
ORDER BY al.changed_at DESC;

-- 5. Summary perubahan per periode untuk monitoring anomali
SELECT
    DATE_TRUNC('day', changed_at) AS tanggal,
    table_name,
    operation,
    COUNT(*) AS jumlah_perubahan,
    COUNT(DISTINCT changed_by) AS jumlah_user
FROM audit_log
WHERE changed_at >= now() - INTERVAL '30 days'
GROUP BY 1, 2, 3
ORDER BY 1 DESC, 4 DESC;

-- 6. Deteksi update tidak wajar (banyak perubahan dalam waktu singkat)
SELECT
    changed_by,
    COUNT(*) AS total_changes,
    COUNT(DISTINCT record_id) AS unique_records
FROM audit_log
WHERE changed_at >= now() - INTERVAL '1 hour'
  AND operation = 'UPDATE'
GROUP BY changed_by
HAVING COUNT(*) > 1000;    -- threshold anomali — sesuaikan dengan volume normal

-- 7. Rekonsiliasi: bandingkan state entitas sebelum dan sesudah periode
SELECT
    prev.entitas_id,
    prev.status AS status_awal,
    curr.status AS status_akhir,
    prev.valid_from AS mulai_awal,
    curr.valid_from AS mulai_akhir
FROM dim_profil_entitas curr
JOIN dim_profil_entitas prev
    ON curr.entitas_id = prev.entitas_id
    AND prev.version = curr.version - 1
WHERE curr.valid_from BETWEEN '2024-Q1-start' AND '2024-Q1-end'
  AND curr.status != prev.status;
```

---

## 7. Retensi dan Lifecycle Audit Data

`[Mandatory — sesuaikan dengan kebijakan retensi organisasi dan UU PDP]`

| Layer | Data | Retensi | Strategi |
|---|---|---|---|
| Tabel utama (current) | State terkini | Selama entitas aktif | Soft delete saat entitas dihentikan |
| SCD history (versi lama) | Riwayat perubahan | Minimal sesuai periode audit (5 tahun untuk data keuangan, 2 tahun untuk operasional) | Partisi per tahun, purge PII otomatis setelah retensi |
| Audit log | Siapa mengubah apa | Minimal 2 tahun untuk operasional, 7 tahun untuk keuangan/fiskal | Partisi per bulan, archive ke cold storage setelah 1 tahun aktif |
| Anonymized aggregate | Statistik historis | Permanen | Hapus PII, pertahankan aggregate |

**Automated purge policy menggunakan pg_partman (open source):**

```sql
-- Menggunakan pg_partman untuk manajemen partisi otomatis
-- Instalasi: https://github.com/pgpartman/pg_partman

-- Setup retention untuk audit_log: hapus partisi > 2 tahun
SELECT partman.create_parent(
    p_parent_table  => 'public.audit_log',
    p_control       => 'changed_at',
    p_type          => 'range',
    p_interval      => 'monthly',
    p_premake       => 3,           -- buat 3 partisi ke depan
    p_retention     => '24 months', -- hapus partisi > 2 tahun
    p_retention_keep_table => false -- benar-benar hapus, bukan keep
);
```

---

## 8. Keputusan Implementasi per Tabel

`[Mandatory — isi sebelum implementasi dimulai]`

| Tabel | SCD Type | Audit Trigger? | Soft Delete? | PII Anonymization? | Partisi History? | Owner |
|---|---|---|---|---|---|---|
| `<dim_profil_entitas>` | `<Type 2>` | `<Ya>` | `<Ya>` | `<Ya — 5 tahun>` | `<Per tahun>` | `<DE>` |
| `<fact_transaksi>` | `<Type 1>` | `<Ya>` | `<Tidak — immutable>` | `<Tidak — non-PII>` | `<Per bulan>` | `<DE>` |
| `<dim_referensi>` | `<Type 0>` | `<Tidak>` | `<Tidak>` | `<Tidak>` | `<Tidak perlu>` | `<DS>` |
