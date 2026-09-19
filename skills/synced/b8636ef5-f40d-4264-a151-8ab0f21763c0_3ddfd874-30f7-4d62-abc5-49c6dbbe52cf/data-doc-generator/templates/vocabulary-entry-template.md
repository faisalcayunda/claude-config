# Template: Vocabulary Entry (per atribut)

Setiap entry vocabulary harus pilih salah satu pola: **KATEGORIKAL** atau **NON-KATEGORIKAL**.

**Aturan wajib**: Setiap field HARUS punya salah satu dari dua seksi di bawah. Tidak boleh ada field yang tidak punya konten validasi/enum. Jika field non-kategorikal dan genuinely tidak punya constraint apapun, tulis secara eksplisit:
> `Tidak ada aturan bisnis yang berlaku — field ini adalah teks bebas tanpa constraint format, range, atau referensi. [tambahkan alasan bisnis]`

**Batas scope Vocabulary**: Vocabulary hanya memuat aturan yang mendefinisikan *nilai yang valid* — yaitu format, range, length, FK, cross-field rule, dan enum. Aturan tentang *keberadaan* (NOT NULL, null rate) dan *keunikan* (UNIQUE constraint) masuk ke **Data Dictionary Section 3**, bukan di sini.

---

## Pola 1: KATEGORIKAL (Enum)

```markdown
### `{field_name}`: {Display Name}

**Document ID:** `VOC-{DOMAIN_UPPER}-{FIELD_UPPER}`

| Metadata | Nilai |
|---|---|
| **Nama Field (Database)** | `{db_column_name}` |
| **Nama Bisnis** | {business_name} |
| **Deskripsi** | {description} |
| **Tipe Data** | `{data_type}` |
| **Sifat Field** | Kategorikal (Enum) |
| **Nullable** | {Ya/Tidak — alasan} |
| **Masked (PII)** | {Ya/Tidak} |
| **Klasifikasi** | {public/internal/restricted/confidential} |
| **Kategori PII** | {NULL atau kategori PII} |
| **Referensi Regulasi Utama** | {Regulasi atau "Aturan internal"} |
| **Sumber Otoritatif** | {Sistem sumber} |
| **SCD Type** | {0/1/2} |
| **Digunakan di Tabel** | `{schema.table1}`, `{schema.table2}` |

#### Nilai yang Valid (Enum)

Berdasarkan profiling full table scan ({N} baris):

| Kode | Display Name | Frekuensi | % | Definisi Bisnis | Makna untuk Tim Produk | Referensi |
|---|---|---|---|---|---|---|
| `{kode_1}` | {Display 1} | {freq_1} | {pct_1}% | {definisi_teknis_1} | {penjelasan_awam_1} | {ref_1} |
| `{kode_2}` | {Display 2} | {freq_2} | {pct_2}% | {definisi_teknis_2} | {penjelasan_awam_2} | {ref_2} |

> **Kolom "Makna untuk Tim Produk"**: tulis 1 kalimat singkat yang bisa dipahami orang di luar tim data. Jelaskan apa artinya nilai ini dalam proses bisnis sehari-hari, tanpa jargon teknis dan tanpa menyebut nama field database.
>
> Contoh untuk `current_status = 'Dispatched'`:
> - Definisi Bisnis: "Status task saat driver telah ditetapkan dan task belum diambil"
> - Makna untuk Tim Produk: "Makanan sudah disiapkan di dapur dan sedang menunggu diambil oleh pengantar"

**Catatan**: Kolom Frekuensi dan % hanya diisi jika profiling dilakukan (Workflow A atau B). Untuk Workflow C (schema manual), kolom tersebut dihilangkan.

#### Implementasi PostgreSQL

```sql
ALTER TABLE {schema}.{table}
    ADD CONSTRAINT chk_{field_name}
    CHECK ({field_name} IN (
        '{kode_1}',
        '{kode_2}'
    ));
```
```

---

## Pola 2: NON-KATEGORIKAL

Vocabulary entry untuk field non-kategorikal punya **dua lapisan**:

1. **Aturan Bisnis** — ringkasan plain-language untuk validasi oleh tim produk/bisnis. Setiap aturan diberi ID `BVR-{NNN}` agar bisa direferensikan dari Data Dictionary.
2. **Implementasi Teknis** — detail teknis (regex, range, FK, SQL) untuk engineer. Setiap blok SQL menyebut ID BVR yang relevan sebagai komentar.

Pilih satu atau lebih dari 5 jenis validasi:
- Format
- Range
- Length
- Referential Integrity
- Cross-field Business Rule

**Tampilkan SEMUA validasi yang berlaku** — jangan skip salah satu jika relevan untuk field ini.

Jika tidak ada satu pun dari 5 jenis di atas yang berlaku (field benar-benar bebas tanpa aturan):
> `Tidak ada aturan bisnis yang berlaku — field ini adalah teks bebas tanpa constraint format, range, atau referensi.`

**Ingat**: Uniqueness (UNIQUE constraint) dan Completeness (NOT NULL rationale, null rate) bukan termasuk ke-5 jenis validasi di atas. Jangan taruh di sini — keduanya masuk ke Data Dictionary Section 3.

```markdown
### `{field_name}`: {Display Name}

**Document ID:** `VOC-{DOMAIN_UPPER}-{FIELD_UPPER}`

| Metadata | Nilai |
|---|---|
| **Nama Field (Database)** | `{db_column_name}` |
| **Nama Bisnis** | {business_name} |
| **Deskripsi** | {description} |
| **Tipe Data** | `{data_type}` |
| **Sifat Field** | Non-Kategorikal ({sub-tipe: Identifier / Measure / FK / Free-text / Date}) |
| **Nullable** | {Ya/Tidak — alasan} |
| **Masked (PII)** | {Ya/Tidak} |
| **Klasifikasi** | {public/internal/restricted/confidential} |
| **Kategori PII** | {NULL atau kategori PII} |
| **Referensi Regulasi Utama** | {Regulasi atau "Aturan internal"} |
| **Sumber Otoritatif** | {Sistem sumber} |
| **Digunakan di Tabel** | `{schema.table1}`, `{schema.table2}` |

#### Aturan Bisnis

> Seksi ini ditulis untuk **tim produk dan bisnis** yang memvalidasi apakah aturan-aturan ini sudah benar dari perspektif operasional. Gunakan bahasa sehari-hari — hindari SQL, regex, dan nama field database. Fokus pada "apa yang harus dipenuhi" atau "apa yang tidak boleh terjadi".

| ID | Aturan | Field Terkait |
|---|---|---|
| `BVR-001` | {deskripsi aturan dalam bahasa awam} | `{field_terkait}` atau — |
| `BVR-002` | {deskripsi aturan lain} | — |

Contoh pengisian yang baik:
- `BVR-001` | "Tanggal pengiriman harus sebelum atau sama dengan tanggal penerimaan" | `tanggal_diterima`
- `BVR-002` | "Usia harus antara 0 dan 120 tahun" | —
- `BVR-003` | "Setiap pesanan harus terhubung ke SPPG yang sudah terdaftar di sistem" | `dim_sppg.sk_sppg`
- `BVR-004` | "NIK harus terdiri dari tepat 16 digit angka" | —

#### Implementasi Teknis

> Seksi ini untuk **engineer** yang mengimplementasikan constraint. Setiap sub-seksi dan blok SQL mencantumkan ID BVR asal yang diimplementasikan.

**1. Format (Regex)** — jika berlaku (BVR-{NNN})

| Atribut | Nilai |
|---|---|
| Pattern | `{regex_pattern}` |
| Contoh Valid | `{example_valid}` |
| Contoh Invalid | `{example_invalid_1}`, `{example_invalid_2}` |

**2. Range (Numeric/Date)** — jika berlaku (BVR-{NNN})

| Atribut | Nilai |
|---|---|
| Min | {min_value} |
| Max | {max_value} |
| Boundary | Inclusive [min, max] / Exclusive (min, max) |

**3. Length (String)** — jika berlaku (BVR-{NNN})

| Atribut | Nilai |
|---|---|
| Min Length | {min_length} |
| Max Length | {max_length} |

**4. Referential Integrity (FK)** — jika berlaku (BVR-{NNN})

| Atribut | Nilai |
|---|---|
| Reference Table | `{ref_schema.ref_table}` |
| Reference Column | `{ref_column}` |
| Cardinality | {One-to-One / One-to-Many / Many-to-One / Many-to-Many} |
| On Delete | {RESTRICT / CASCADE / SET NULL / NO ACTION} |
| On Update | {CASCADE / RESTRICT} |

**5. Cross-field Business Rule** — jika berlaku (BVR-{NNN})

| Rule | Field Terkait | Implementasi |
|---|---|---|
| {rule_description_1} | `{related_field_1}` | {how_to_enforce} |

```sql
-- BVR-001: {ringkasan aturan bisnis dalam 1 frasa}
ALTER TABLE {schema}.{table}
    ADD CONSTRAINT chk_{field_name}_format
    CHECK ({field_name} ~ '{regex_pattern}');

-- BVR-002: {ringkasan aturan bisnis}
ALTER TABLE {schema}.{table}
    ADD CONSTRAINT chk_{field_name}_range
    CHECK ({field_name} >= {min} AND {field_name} <= {max});

-- BVR-003: {ringkasan aturan bisnis}
ALTER TABLE {schema}.{table}
    ADD CONSTRAINT fk_{field_name}
    FOREIGN KEY ({field_name}) REFERENCES {ref_schema}.{ref_table}({ref_column})
    ON DELETE {action} ON UPDATE {action};

-- BVR-004: {ringkasan aturan bisnis} — cross-field via trigger
CREATE OR REPLACE FUNCTION validate_{field_name}_consistency()
RETURNS TRIGGER AS $$
BEGIN
    -- cross-field logic
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_{field_name}_consistency
BEFORE INSERT OR UPDATE ON {schema}.{table}
FOR EACH ROW EXECUTE FUNCTION validate_{field_name}_consistency();
```
```

---

## Aturan Pemilihan Pola

| Indicator | Pola |
|---|---|
| Distinct count <= 50 DAN values diskret labels | KATEGORIKAL |
| Distinct count rendah TAPI numeric continuous (counter, measurement) | NON-KATEGORIKAL (Range) |
| ID unik per record | NON-KATEGORIKAL (Identifier dengan Format) |
| Format terstruktur (NIK, kode pos, email) | NON-KATEGORIKAL (Format) |
| FK ke tabel lain | NON-KATEGORIKAL (Referential Integrity) |
| String bebas (nama, alamat, deskripsi) | NON-KATEGORIKAL (Length) — atau "Tidak ada aturan bisnis" jika benar-benar bebas |
| Tanggal/timestamp | NON-KATEGORIKAL (Range date) |
| Boolean / flag 2 nilai | KATEGORIKAL (enum dengan 2 nilai) |

Untuk detail reasoning, lihat `references/categorical-detection.md`.

---

## Penomoran BVR

- ID BVR di-reset per tabel: mulai dari `BVR-001` untuk setiap file vocabulary baru.
- Urutan: nomor berurutan mengikuti urutan field di tabel, lanjutkan antar-field tanpa reset ke 001.
- Format selalu 3 digit: `BVR-001`, `BVR-002`, `BVR-010`, dst.
- ID yang sama dipakai di Data Dictionary Section 3 kolom "Ref. Aturan Bisnis" untuk menghubungkan constraint teknis dengan aturan bisnis asalnya.

---

## Checklist Sebelum Finalisasi Vocabulary per Tabel

Sebelum menyimpan file vocabulary, pastikan:

- [ ] Semua kolom dari tabel ini sudah ada entrynya
- [ ] Setiap field non-kategorikal punya seksi "Aturan Bisnis" (atau pernyataan eksplisit tidak ada aturan)
- [ ] Setiap sub-seksi di "Implementasi Teknis" sudah mencantumkan ID BVR di header-nya
- [ ] Kolom "Makna untuk Tim Produk" di tabel enum sudah diisi dengan bahasa awam
- [ ] Tidak ada uniqueness rule (UNIQUE, PRIMARY KEY constraint) yang masuk ke sini
- [ ] Tidak ada completeness rule (NOT NULL rationale, null rate) yang masuk ke sini
- [ ] Enum values berasal dari data aktual (bukan tebakan), atau dari konfirmasi user untuk Workflow C
- [ ] Field uncertain sudah dikonfirmasi ke user
