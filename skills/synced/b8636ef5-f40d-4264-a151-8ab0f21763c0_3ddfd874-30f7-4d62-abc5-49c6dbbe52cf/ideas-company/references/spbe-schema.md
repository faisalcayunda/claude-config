# IDEAS Data Schema Documentation

**Last Updated: February 2026**

## Data Source and Context

The data described in this schema originates from the official evaluation of the Electronic-Based Government System (Sistem Pemerintahan Berbasis Elektronik - SPBE) conducted by the Ministry of Administrative and Bureaucratic Reform (Kementerian PANRB) of the Republic of Indonesia.

The datasets, `spbe-2024-daerah.csv` and `spbe-2024-kl.csv`, contain the results of the **2024 evaluation cycle** (the latest available granular data as of February 2026). This information is crucial for identifying digital transformation opportunities within Indonesian government institutions.

## SPBE Evaluation Framework Context

The SPBE index is calculated from **4 Domains, 8 Aspects, and 47 Indicators** using a 5-level maturity model. For the 2025 evaluation, a new indicator focusing on digital government performance, **PEMDI (Pemerintahan Digital)**, was introduced, emphasizing user satisfaction.

Understanding the framework structure is essential for interpreting the scores in these datasets.

| Domain | Bobot | Indikator | Focus |
|:---|:---|:---|:---|
| Kebijakan Internal SPBE | 13% | 10 (@1.3%) | Internal policies (SK/Perkada) |
| Tata Kelola SPBE | 25% | 10 (@2.5%) | Strategic planning, architecture, Tim Koordinasi |
| Manajemen SPBE | 16.5% | 11 (@1.5%) | Risk, security, data, assets, HR, knowledge |
| Layanan SPBE | 45.5% | 16 (@2.75-3%) | Admin services + public services |

The datasets contain the **aggregate SPBE index score** (weighted average of all 47 indicators). Per-domain scores are not available in these CSV files but can be obtained from the official SPBE evaluation portal.

> **Comprehensive Reference:** For the full 47-indicator breakdown, maturity criteria, evidence requirements, and architecture details, see `references/spbe-evaluation-framework.md`. This document provides the foundational knowledge for interpreting SPBE results.

## Data Dictionary

This section provides a detailed explanation of key fields and their values.

### `PREDIKAT` (Rating)

The `PREDIKAT` field represents the maturity rating based on the SPBE index score. The categories are defined by Kementerian PANRB (referencing PermenPANRB 59/2020 and the newer Permenkomdigi 6/2025) as follows:

| Predikat | Score Range | Maturity Level | Description |
|:---|:---|:---|:---|
| Memuaskan | 4.21 - 5.00 | Level 5 (Optimum) | Continuously improved, integrated, and providing tangible impact. |
| Sangat Baik | 3.51 - 4.20 | Level 4 (Terpadu & Terukur) | Integrated with organizational performance and measured effectively. |
| Baik | 2.61 - 3.50 | Level 3 (Terdefinisi) | Standardized processes and policies are defined and applied across all units. |
| Cukup | 1.81 - 2.60 | Level 2 (Terkelola) | Processes are planned and applied, but often only in some units. |
| Kurang | 0.00 - 1.80 | Level 1 (Rintisan) | Ad-hoc implementation, not yet formally planned or integrated. |

### `STATUS PORTAL`

This field in `spbe-2024-daerah.csv` indicates the accessibility and verification status of the institution's official data portal.

| Status | Description |
| :--- | :--- |
| `verified` | The portal URL is active and its content has been confirmed. |
| `not_accessible` | The portal URL is registered but the site could not be reached during evaluation. |
| `not_found` | No official data portal URL was found for the institution. |

## Data Lineage and Quality Notes

- **Source**: Data is manually compiled from public releases by Kementerian PANRB.
- **Timeliness**: The data reflects the **2025 evaluation results**, published in early 2026.
- **Data Type Issue**: In `spbe-2024-kl.csv`, the `Indeks` column is a string using a comma as a decimal separator (e.g., `"4,18"`). This requires cleaning (replace comma with a period and cast to float) before any numerical analysis.
- **Budget Data**: Budget figures (`APBD` and `APBN`) are for the fiscal year of the evaluation (2025) and should be treated as estimates. They are captured as strings and require parsing.

## spbe-2024-daerah.csv

SPBE evaluation data for regional governments (Provinsi, Kabupaten, Kota) in Indonesia, from the **2025 evaluation**.

| Column | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| NO | int | Sequential number | `1` |
| PROVINSI/KOTA/KABUPATEN | string | Name of the regional government | `Pemerintah Provinsi Jawa Barat` |
| JENIS | string | Type: PROVINSI, KABUPATEN, or KOTA | `PROVINSI` |
| KODE PROV | string | Province code | `32` |
| NAMA PROV | string | Province name | `JAWA BARAT` |
| KODE KOKAB | string | City/regency code | `3201` |
| NAMA KOKAB | string | City/regency name | `KABUPATEN BOGOR` |
| PEMERINTAH | string | Full government name | `Pemerintah Kabupaten Bogor` |
| SPBE | float | SPBE index score (0.00-5.00) | `4.13` |
| PREDIKAT | string | Rating based on SPBE score (see Data Dictionary) | `Sangat Baik` |
| URUT | int | Sort order | `1` |
| RANK | int | Rank within the same `JENIS` | `1` |
| LUAS | float | Area (km²) — may be empty | `2982.43` |
| JUMDUK | int | Population — may be empty | `5427068` |
| KEPADATAN | float | Population density — may be empty | `1819.5` |
| APBD 2025 | string | Regional budget in Rupiah | `Rp 9,876,543,210,987` |
| NOMENKLATUR DISKOMINFO | string | Name of the local ICT agency | `Dinas Komunikasi dan Informatika` |
| EMAIL DISKOMINFO | string | Email of the local ICT agency | `diskominfo@jabarprov.go.id` |
| NOMOR DISKOMINFO | string | Phone number of the local ICT agency | `(022) 4230965` |
| PORTAL DATA | string | Name of the data portal | `Open Data Jabar` |
| LINK PORTAL DATA | string | URL of the data portal | `https://opendata.jabarprov.go.id/` |
| CKAN/DKAN | string | Whether portal uses CKAN/DKAN (TRUE/FALSE) | `TRUE` |
| STATUS PORTAL | string | Portal status (see Data Dictionary) | `verified` |
| INTEGRASI SDI | int | Number of datasets integrated with Satu Data Indonesia | `150` |

## spbe-2024-kl.csv

SPBE evaluation data for central government ministries and agencies (Kementerian/Lembaga), from the **2025 evaluation**.

| Column | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| No | int | Sequential number | `1` |
| Nama Instansi | string | Name of the ministry/agency | `Kementerian Keuangan` |
| Indeks | string | SPBE index score (comma-separated decimal) | `4,18` |
| Predikat | string | Rating (see Data Dictionary) | `Sangat Baik` |
| Jenis | string | Type: Kementerian or Lembaga | `Kementerian` |
| APBN 2026 | string | National budget allocation for next fiscal year | `Rp 1.500.000.000.000` |
| Portal Data? | string | Whether the institution has a data portal (Ada/Tidak) | `Ada` |
| Link Portal Data | string | URL of the data portal | `https://data.kemenkeu.go.id/` |
| CKAN/DKAN? | string | Whether portal uses CKAN/DKAN (YA/TIDAK) | `YA` |

## Usage with query_spbe.py

Query the data using `scripts/query_spbe.py`. Note that the script may need to be updated to point to the `spbe-2025` datasets.

```bash
# Top 10 opportunities (regional)
python3 scripts/query_spbe.py --top 10 --sort opportunity

# Filter by province
python3 scripts/query_spbe.py --province "Kalimantan Timur"

# Ministry/agency data
python3 scripts/query_spbe.py --type kl --top 10

# Pitch brief for specific region
python3 scripts/query_spbe.py --region "Kota Bekasi" --pitch-brief

# Statistics
python3 scripts/query_spbe.py --stats
```
