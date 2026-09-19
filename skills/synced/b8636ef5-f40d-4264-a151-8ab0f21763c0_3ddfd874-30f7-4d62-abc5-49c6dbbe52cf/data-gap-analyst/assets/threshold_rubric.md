# Threshold & Severity Rubric — `data-gap-analyst`

Default threshold yang dipakai skill jika user tidak override. Severity dipakai untuk klasifikasi gap di reasoning chain Step 2 (MAGNITUDE) dan untuk warna heatmap di Field-Level Gap Matrix XLSX.

Severity:

- 🟢 **Minor** — variance yang masih masuk akal, tidak perlu action segera, cukup catat
- 🟡 **Moderate** — perlu investigasi, mungkin butuh action di sprint berikutnya
- 🔴 **Critical** — block downstream, butuh action segera, calon incident

## D1 — Volume & Completeness Gap

| Indikator | Formula | 🟢 Minor | 🟡 Moderate | 🔴 Critical |
|---|---|---|---|---|
| Row count diff | `|count_A − count_B| / max(count_A, count_B)` | <2% | 2–10% | >10% |
| Table coverage | tabel di A tapi tidak di B (atau sebaliknya) | — | tabel non-critical | tabel critical (PK source) |
| NULL ratio delta | `|null%_A − null%_B|` per kolom | <2pp | 2–10pp | >10pp |
| Distinct count delta | `|distinct_A − distinct_B| / max(distinct_A, distinct_B)` per kolom kunci | <2% | 2–10% | >10% |

Catatan: pp = percentage point (selisih absolut dua persen).

## D2 — Schema & Structural Gap

| Indikator | 🟢 Minor | 🟡 Moderate | 🔴 Critical |
|---|---|---|---|
| Tipe data widening (`INT→BIGINT`, `VARCHAR(50)→VARCHAR(255)`) | catat | — | — |
| Tipe data narrowing (`BIGINT→INT`, `VARCHAR(255)→VARCHAR(100)`) | — | — | flag (destructive) |
| Tipe data conversion (`VARCHAR→INT`, `TEXT→JSON`) | — | flag | flag jika lossy |
| Add column nullable | catat | — | — |
| Add column NOT NULL tanpa default | — | flag | — |
| Drop column | — | — | flag (destructive) |
| Add NOT NULL constraint | — | flag (risk: existing NULL) | — |
| Remove NOT NULL constraint | catat | — | — |
| Drop PK / change PK | — | — | flag |
| Drop FK | — | flag | flag jika referential integrity broken |
| Drop UNIQUE constraint | — | flag | — |
| Drop index | — | flag (performance) | flag jika kolom join-key |

Definisi **destructive**: perubahan yang bisa menyebabkan data loss, query break, atau referential integrity violation tanpa migrasi data eksplisit.

## D3 — Value Distribution & Semantic Gap

| Indikator | Formula / Test | 🟢 Minor | 🟡 Moderate | 🔴 Critical |
|---|---|---|---|---|
| KS test numeric | `scipy.stats.ks_2samp(A, B).pvalue` | >0.05 | 0.01–0.05 | <0.01 |
| Jaccard similarity (enum/categorical) | `|A ∩ B| / |A ∪ B|` | >0.95 | 0.80–0.95 | <0.80 |
| Cardinality delta enum | `|distinct_A − distinct_B|` | 0 | 1–2 nilai | >2 nilai |
| Mean delta (numeric) | `|mean_A − mean_B| / mean_A` | <5% | 5–20% | >20% |
| Stddev delta (numeric) | `|stddev_A − stddev_B| / stddev_A` | <10% | 10–30% | >30% |
| Unit/format delta (currency, date, phone) | manual flag | — | — | flag |

Catatan KS-test: hanya valid untuk distribusi continuous. Untuk kolom kategorikal, gunakan Jaccard atau Chi-square test (skill akan auto-pilih berdasarkan tipe kolom).

## D4 — Temporal & Freshness Gap

| Indikator | Formula | 🟢 Minor | 🟡 Moderate | 🔴 Critical |
|---|---|---|---|---|
| Lag vs SLA | `max(updated_at_A) − max(updated_at_B)` vs SLA target | <50% SLA | 50–100% SLA | >SLA |
| Coverage period delta | `(MAX−MIN)_A − (MAX−MIN)_B` | <1 hari | 1–7 hari | >7 hari |
| Update frequency delta | `avg_rows_per_day_A − avg_rows_per_day_B` ratio | within 10% | 10–50% | >50% |
| Stale data | `now() − max(updated_at)` > SLA | within SLA | <2× SLA | >2× SLA |

Catatan SLA: jika user tidak specify SLA, skill akan ASUMSI SLA T+1 (24 jam) untuk DWH dan T+0 (real-time, <1 jam) untuk OLTP. Asumsi ini WAJIB dicatat eksplisit di output dengan flag `[ASUMSI — user belum konfirmasi SLA]`.

## Override Mechanism

User boleh kirim `config.yaml` di awal sesi:

```yaml
# config.yaml — override threshold default
thresholds:
  d1:
    row_count_diff_minor: 0.01      # 1% bukan 2%
    row_count_diff_critical: 0.05   # 5% bukan 10%
  d3:
    ks_pvalue_critical: 0.001       # 0.1% bukan 1%
  d4:
    sla_hours: 6                    # SLA 6 jam bukan 24

# Catatan reasoning untuk audit
override_reason: "Project migrasi finansial, toleransi lebih ketat"
override_approved_by: "Head of Data Governance"
```

Skill MUST merge override dengan default, dan catat di `Scope & Method` section di report bahwa override aktif + alasan + approver. Jika tidak ada `config.yaml`, pakai default rubric di atas dan catat eksplisit "default rubric dipakai (tidak ada override)".

## Catatan Filosofis

Threshold ini adalah **opinionated default**, bukan ground truth universal. Setiap organisasi punya konteks bisnis, SLA, dan toleransi risiko berbeda. Skill ini memilih default berdasarkan pattern umum di project IDEAS (pemerintahan, fintech, healthcare) — tapi user PALING TAHU konteks bisnis mereka. Itulah kenapa override mekanis disediakan dan didorong dipakai untuk proyek serius.

Yang TIDAK boleh di-override: prinsip dual-audience writing, 7-step reasoning chain, dan anti-halusinasi guardrail. Itu adalah fondasi skill, bukan parameter.
