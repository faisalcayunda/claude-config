# Template Index — Data Mesh Architect

Master daftar semua template dokumen output. Setiap dokumen memiliki **Doc ID unik** yang dapat di-cross-reference antar dokumen.

> **Cara pakai:** Baca baris yang relevan → buka file template → isi placeholder `<...>` dengan konteks dari business brief.
>
> **Konvensi Doc ID:** `B-` Bootstrap · `D-` Design · `V-` Development · `DLV-` Delivery · `M-` Monitoring · `E-` EoSL · `G-` Governance · `PM-` Project Management · `ADR-` Architecture Decision

---

## Bootstrap Phase

| Doc ID | Template | File | Phase | Role Pengisi | Mandatory? |
|---|---|---|---|---|---|
| **B-01** | Business Process Research & Context | `bootstrap/business-process-research.md` | Bootstrap | DA + BA + DPO | ✅ |
| **B-02** | Data Product Proposal | `bootstrap/proposal.md` | Bootstrap | DPO + PM | ✅ |
| **B-03** | Data Product Canvas | `bootstrap/canvas.md` | Bootstrap | DA + DPO | ✅ |
| **B-04** | Preliminary Data Profiling Report | `bootstrap/data-profiling-prelim.md` | Bootstrap | DE + DA | ✅ |
| **B-05** | Preliminary EDA Report | `design/eda-template.md` | Bootstrap *(reklasifikasi dari Design)* | DA | ✅ |

---

## Design Phase

| Doc ID | Template | File | Role Pengisi | Mandatory? |
|---|---|---|---|---|
| **D-01** | Data Product Design Document | `design/design-document.md` | DA + DE | ✅ |
| **D-02** | Data Contract & Interface Specification | `design/data-contract-spec.md` | DA + DPO | ✅ |
| **D-03** | Data Contract YAML | `design/data-contract.yaml` | DA + DE | ✅ |
| **D-04** | Data Catalog & Metadata | `design/data-catalog.md` | DS + DA | ✅ |
| **D-05** | Data Quality Design | `design/quality-design.md` | DS + DE | ✅ |
| **D-06** | Data Risk Assessment & Mitigation | `design/risk-assessment.md` | DA + Legal | ✅ |
| **D-07** | Record of Processing Activities (RoPA) | `design/risk-assessment.md` §RoPA | Legal + DS | Jika ada PII |
| **D-08** | Data Protection Impact Assessment (DPIA) | `design/risk-assessment.md` §DPIA | Legal + DA | Jika high-risk |
| **D-09** | Infrastructure Brief | `design/infra-brief.md` | DA + DE + SRE | ✅ |
| **D-11** | Dashboard Design Document | `design/dashboard-design.md` | DA + DPO | Jika ada dashboard |
| **D-12** | SCD & Audit Logging Design | `design/scd-audit-design.md` | DA + DE | Jika tabel butuh histori |
| **D-13** | Data Product Metrics & Insights Catalog | `monitoring/metrics-catalog.md` | DS + DPO | ✅ *(reklasifikasi dari Monitoring)* |
| **ADR-01** | Architecture Decision Record | `decisions/ADR-NNNN-template.md` | DA | Per keputusan |

---

## Development Phase

| Doc ID | Template | File | Role Pengisi | Mandatory? |
|---|---|---|---|---|
| **V-01** | Data Pipeline Brief | `development/pipeline-brief.md` | DE + DA | ✅ |
| **V-02** | Data API Brief | `development/api-brief.md` | DE + DA | Jika ada API output |
| **V-03** | UAT Template | `development/uat-integration-test.md` §UAT | PM + DA + Consumer | ✅ |
| **V-04** | Integration Test Template | `development/uat-integration-test.md` §IntTest | DE + SRE | ✅ |
| **V-05** | Data Pipeline *(artefak)* | `development/data-pipeline.md` | DE | ✅ — **🔲 BELUM DIBUAT** |
| **V-06** | Data API *(artefak)* | `development/data-api.md` | DE | Jika API — **🔲 BELUM DIBUAT** |
| **V-07** | Dashboard Development | `development/dashboard-development.md` | DA + FE | Jika dashboard — **🔲 BELUM DIBUAT** |
| **V-08** | Data Science Model | `development/data-science-model.md` | DS + DE | Jika ML model — **🔲 BELUM DIBUAT** |
| **V-09** | Dataset (Table-View / Spreadsheet) | `development/dataset-artifact.md` | DE + DA | Jika output dataset — **🔲 BELUM DIBUAT** |
| **V-10** | Migration Report | `development/migration-report.md` | DE + DA | Jika ada migrasi — **🔲 BELUM DIBUAT** |
| **V-11** | Analytical Report | `development/analytical-report.md` | DA + DS | Per laporan — **🔲 BELUM DIBUAT** |

---

## Delivery Phase

| Doc ID | Template | File | Role Pengisi | Mandatory? |
|---|---|---|---|---|
| **DLV-01** | Consumer Onboarding Guide | `delivery/consumer-onboarding-guide.md` | DS + DPO | ✅ |
| **DLV-02** | Self-Service Infrastructure Guide | `delivery/self-service-infra-guide.md` | SRE + DE | Jika self-serve — **🔲 BELUM DIBUAT** |

---

## Monitoring & Operations Phase

| Doc ID | Template | File | Role Pengisi | Mandatory? |
|---|---|---|---|---|
| **M-02** | Data Quality Report | `monitoring/operational-reports.md` §QualityReport | DS + DE | ✅ Bulanan |
| **M-03** | Cost Report | `monitoring/operational-reports.md` §CostReport | PM + SRE | ✅ Bulanan |
| **M-04** | Incident Management Template | `monitoring/operational-reports.md` §Incident | SRE + DE | Per insiden |
| **M-05** | Backup & DR Plan | `monitoring/backup-dr-plan.md` | SRE + DA | ✅ — **🔲 BELUM DIBUAT** |
| **M-06** | Change Log | `monitoring/change-log.md` | DE + DPO | ✅ — **🔲 BELUM DIBUAT** |
| **M-07** | Operations Runbook | `monitoring/operations-runbook.md` | SRE + DE | ✅ — **🔲 BELUM DIBUAT** |

---

## Governance & Lifecycle

| Doc ID | Template | File | Role Pengisi | Mandatory? |
|---|---|---|---|---|
| **G-01** | Data Vocabulary & Business Glossarium | `governance/data-vocabulary-template.md` | DS + DA | Per domain |
| **G-02** | Data Access Control Matrix | `governance/data-access-control-matrix.md` | DA + DPO + CISO | Per data product restricted/confidential |
| **G-03** | Data Dictionary | `governance/data-dictionary.md` | DS + DA | ✅ — **🔲 BELUM DIBUAT** |
| **G-04** | Data Retention Policy | `governance/data-retention-policy.md` | Legal + DA + DPO | ✅ — **🔲 BELUM DIBUAT** |
| **G-05** | Federated Governance Checklist | `governance/federated-governance-checklist.md` | DPO + DGO | ✅ |
| **E-01** | End of Service Life Report | `eosl/eosl-report.md` | DPO + PM | Saat retirement |

---

## Project Management

| Doc ID | Template | File | Role Pengisi | Mandatory? |
|---|---|---|---|---|
| **PM-01** | Ways of Working Document | `project-management/ways-of-working.md` | PM + Seluruh Tim | ✅ |
| **PM-02** | RASCI Matrix | `project-management/rasci-matrix.md` | PM + DA + DPO | ✅ |
| **PM-03** | JIRA Structure & Epic Breakdown | `project-management/jira-structure.md` | PM | ✅ |
| **PM-04** | Sprint Plan Template | `project-management/sprint-plan.md` | PM | Per Sprint |

---

## Status Gap Analysis

### ✅ Dokumen Selesai — 32 dari 47

Semua entri di atas **kecuali** yang diberi label `🔲 BELUM DIBUAT`.

### 🔲 Dokumen Belum Dibuat — 15 dari 47

| Prioritas | Doc ID | Dokumen | Phase |
|---|---|---|---|
| 🔴 Tinggi | **DLV-02** | Self-Service Infrastructure Guide | Delivery |
| 🔴 Tinggi | **M-07** | Operations Runbook | Monitoring & Operations |
| 🔴 Tinggi | **M-05** | Backup & DR Plan | Monitoring & Operations |
| 🔴 Tinggi | **M-06** | Change Log | Monitoring & Operations |
| 🔴 Tinggi | **G-03** | Data Dictionary | Governance & Lifecycle |
| 🔴 Tinggi | **G-04** | Data Retention Policy | Governance & Lifecycle |
| 🟡 Sedang | **V-05** | Data Pipeline (artefak) | Development |
| 🟡 Sedang | **V-06** | Data API (artefak) | Development |
| 🟡 Sedang | **V-07** | Dashboard Development | Development |
| 🟡 Sedang | **V-08** | Data Science Model | Development |
| 🟢 Normal | **V-09** | Dataset (Table-View / Spreadsheet) | Development |
| 🟢 Normal | **V-10** | Migration Report | Development |
| 🟢 Normal | **V-11** | Analytical Report | Development |

### 🔀 Reklasifikasi Phase (sudah dieksekusi)

| Doc ID | Dokumen | Phase Lama | Phase Baru |
|---|---|---|---|
| **B-05** | Preliminary EDA Report | Design | Bootstrap |
| **D-13** | Data Product Metrics & Insights Catalog | Monitoring | Design |
| **ADR-01** | Architecture Decision Record | `decisions/` standalone | Design cross-linked |
| **E-01** | End of Service Life Report | EoSL standalone | Governance & Lifecycle |

---

## Konvensi Doc ID

```
B-NN    → Bootstrap phase documents
D-NN    → Design phase documents
V-NN    → Development phase artifacts & briefs
DLV-NN  → Delivery phase documents
M-NN    → Monitoring & Operations documents
E-NN    → End of Service Life documents
G-NN    → Governance & Lifecycle documents (cross-phase)
PM-NN   → Project Management documents (cross-phase)
ADR-NN  → Architecture Decision Records
```

**Format referensi antar dokumen:** `[D-02 Data Contract](../design/data-contract-spec.md)`

---

## Legenda Role

| Kode | Peran |
|---|---|
| DPO | Data Product Owner |
| DA | Data Architect |
| DE | Data Engineer |
| DS | Data Steward / Data Analyst |
| PM | Project Manager |
| SRE | Site Reliability Engineer / DevOps |
| BA | Business Analyst |
| Legal | Legal / Compliance Officer |
| CISO | Chief Information Security Officer |
| DGO | Data Governance Officer |
| FE | Frontend / Dashboard Developer |
| Consumer | Pengguna / Konsumen Data Product |
