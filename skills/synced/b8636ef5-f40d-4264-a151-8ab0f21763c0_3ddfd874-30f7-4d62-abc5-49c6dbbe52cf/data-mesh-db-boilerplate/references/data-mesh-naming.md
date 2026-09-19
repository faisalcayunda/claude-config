# Data Mesh Naming Conventions for Database Boilerplate

Referensi ini mengikuti standar `/data-mesh-architect` dan framework dari
**Zhamak Dehghani's Data Mesh**, **DAMA-DMBOK2**, dan **INNOQ Data Product Canvas**.

---

## 1. Database Name Convention

### Format
```
{DOMAIN_SHORTCODE}_{DATA_PRODUCT_SHORTCODE}
```

### Rules
- Lowercase, snake_case
- `DOMAIN_SHORTCODE`: ≤ 8 karakter (abreviasi domain bisnis)
- `DATA_PRODUCT_SHORTCODE`: ≤ 16 karakter (abreviasi data product)
- Tidak boleh ada spasi, dash, atau uppercase
- Hindari kata reserved PostgreSQL (`user`, `order`, `group` → gunakan `users`, `orders`, `groups`)

### Domain Shortcode Examples

| Domain Bisnis | Shortcode |
|---|---|
| Customer Relationship Management | `crm` |
| Finance & Accounting | `fin` |
| Human Resources | `hr` |
| Operations | `ops` |
| Supply Chain | `schain` |
| Marketing | `mktg` |
| Product Management | `prod` |
| Risk & Compliance | `risk` |
| Logistics | `logis` |
| Pendidikan (Education) | `edu` |
| Kesehatan (Health) | `health` |
| Gizi (Nutrition) | `gizi` |

### Data Product Shortcode Examples

| Data Product | Shortcode |
|---|---|
| Customer 360 | `cust360` |
| Transaction Ledger | `txn_ldgr` |
| Payroll | `payroll` |
| Inventory | `inventory` |
| User Profile | `usr_prof` |
| Master Data Sekolah | `mst_sklh` |
| Profil Peserta Didik | `ppd` |
| Makan Bergizi Gratis | `mbg` |
| Sumber Pangan Utama | `spu` |

### Full Examples

```
crm_cust360         # CRM domain → Customer 360 data product
fin_txn_ldgr        # Finance domain → Transaction Ledger
hr_payroll          # HR domain → Payroll
ops_inventory       # Operations domain → Inventory
edu_mst_sklh        # Pendidikan domain → Master Data Sekolah
gizi_mbg            # Gizi domain → Makan Bergizi Gratis
```

---

## 2. Schema Object Naming

### Tables
- Plural, lowercase snake_case
- Prefix boleh digunakan jika ada namespace collision antar data product

```sql
customers           -- OK
transaction_lines   -- OK
user_profiles       -- OK
CustomerData        -- ❌ No PascalCase
tbl_customers       -- ❌ Avoid Hungarian notation
```

### Columns
- Lowercase snake_case
- Boolean: `is_*` or `has_*` prefix
- Timestamps: `*_at` suffix (`created_at`, `updated_at`, `deleted_at`)
- Foreign keys: `{referenced_table_singular}_id` (e.g., `customer_id`, `order_id`)

```
id               -- UUID primary key
external_id      -- Source system identifier
name             -- Business name
created_at       -- Audit: creation timestamp
updated_at       -- Audit: last update timestamp
created_by       -- Audit: creator service/user
is_active        -- Boolean flag
has_consent      -- Boolean flag
customer_id      -- FK to customers
```

### Indexes
```
idx_{table}_{column(s)}           -- Regular index
uq_{table}_{column(s)}            -- Unique constraint
fk_{table}_{referenced_table}     -- Foreign key constraint
pk_{table}                        -- Primary key (auto by Atlas)
```

Examples:
```
idx_customers_external_id
uq_customers_email
fk_orders_customer
idx_transaction_lines_created_at
```

### Migrations
Use **descriptive snake_case** names following conventional commits:

```
initial                     -- First migration
add_customers_table         -- New table
add_email_to_customers      -- New column
rename_col_phone_to_mobile  -- Rename column
add_idx_customers_email     -- New index
drop_legacy_audit_table     -- Remove table
```

---

## 3. Repository Structure Naming

```
{domain-shortcode}-{data-product-shortcode}-db/
│
├── schema/
│   ├── schema.pg.hcl          # Main schema (tables, indexes, FKs)
│   ├── extensions.pg.hcl      # PostgreSQL extensions
│   ├── functions.pg.hcl       # Stored functions/triggers
│   └── views.pg.hcl           # Views (if any)
│
├── migrations/
│   ├── 20240101000000_initial.sql
│   ├── 20240201000000_add_orders_table.sql
│   └── atlas.sum
│
├── atlas.hcl
├── .envrc
├── .env.example
├── .gitignore
├── Makefile
└── README.md
```

---

## 4. Standard Audit Columns (Data Mesh Mandatory)

Setiap table dalam data mesh wajib memiliki audit columns berikut.
Ini memungkinkan **data lineage**, **SCD Type 2**, dan **compliance tracking**.

```hcl
column "created_at" {
  type    = timestamptz
  null    = false
  default = sql("now()")
  comment = "Timestamp when record was created"
}
column "updated_at" {
  type    = timestamptz
  null    = false
  default = sql("now()")
  comment = "Timestamp when record was last updated"
}
column "created_by" {
  type    = character_varying(255)
  null    = false
  default = "system"
  comment = "Service account or user that created this record"
}
column "is_deleted" {
  type    = boolean
  null    = false
  default = false
  comment = "Soft delete flag — never hard delete in data mesh"
}
```

**Why soft delete?** Data mesh consumers may rely on historical records.
Hard deletes break lineage and can violate data contracts.

---

## 5. Data Classification Annotations

Gunakan `comment` di Atlas HCL untuk annotate PII/sensitivity:

```hcl
column "email" {
  type    = character_varying(255)
  null    = true
  comment = "PII:email — data classification: RESTRICTED"
}
column "national_id" {
  type    = character_varying(50)
  null    = true
  comment = "PII:national_id — data classification: CONFIDENTIAL"
}
column "birth_date" {
  type    = date
  null    = true
  comment = "PII:date_of_birth — data classification: RESTRICTED"
}
```

Anotasi ini digunakan oleh data catalog (Atlan, DataHub, OpenMetadata) untuk
**auto-classify** kolom saat metadata crawl.

---

## 6. Multi-Environment DB Names

```
{DOMAIN_SHORTCODE}_{DATA_PRODUCT_SHORTCODE}           # production
{DOMAIN_SHORTCODE}_{DATA_PRODUCT_SHORTCODE}_staging   # staging
{DOMAIN_SHORTCODE}_{DATA_PRODUCT_SHORTCODE}_dev       # development
```

Contoh:
```
crm_cust360             # production
crm_cust360_staging     # staging
crm_cust360_dev         # development (lokal)
```

Ini memungkinkan semua environments berada di server yang sama tanpa collision.
