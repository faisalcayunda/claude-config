---
title: "RASCI Matrix — <Nama Data Product>"
sidebar_label: "RASCI Matrix"
sidebar_position: 2
description: "Matriks tanggung jawab seluruh aktivitas dan deliverable data product lifecycle"
tags: [project-management, rasci, responsibility, governance]
data_product_id: "<domain>/<data-product-name>/v<version>"
phase: bootstrap
last_updated: "<YYYY-MM-DD>"
---

# RASCI Matrix

> **Cara membaca RASCI:**
> - **R** = Responsible — Yang mengerjakan pekerjaan
> - **A** = Accountable — Yang bertanggung jawab penuh atas hasil akhir (hanya 1 per aktivitas)
> - **S** = Support — Yang mendukung, membantu mengerjakan
> - **C** = Consulted — Yang diminta pendapatnya sebelum keputusan
> - **I** = Informed — Yang dikabari setelah keputusan/pekerjaan selesai

---

## Legenda Role

| Kode | Peran | Nama |
|---|---|---|
| **DPO** | Data Product Owner | `<Nama>` |
| **DA** | Data Architect | `<Nama>` |
| **DE** | Data Engineer (Lead) | `<Nama>` |
| **DS** | Data Steward / Analyst | `<Nama>` |
| **PM** | Project Manager | `<Nama>` |
| **SRE** | Site Reliability Engineer | `<Nama>` |
| **LGL** | Legal / Compliance | `<Nama>` |
| **CON** | Consumer Representative | `<Nama>` |

---

## Fase 1 — Bootstrap

| Aktivitas / Deliverable | DPO | DA | DE | DS | PM | SRE | LGL | CON |
|---|---|---|---|---|---|---|---|---|
| Business Process Research | C | R | - | S | A | - | - | C |
| Stakeholder Interviews | A | C | - | R | S | - | - | C |
| Domain Mapping & Bounded Context | C | R | S | - | I | - | - | I |
| **Data Product Canvas** | A | R | C | S | S | - | C | C |
| **Data Product Proposal** | A | C | - | - | R | - | C | I |
| Preliminary Data Profiling | C | C | R | S | A | - | - | - |
| Bootstrap Sign-off | **A** | C | - | - | S | - | I | I |

---

## Fase 2 — Design

| Aktivitas / Deliverable | DPO | DA | DE | DS | PM | SRE | LGL | CON |
|---|---|---|---|---|---|---|---|---|
| **Data Product Design Document** | C | A/R | S | - | I | C | - | - |
| Architecture Decision Records (ADR) | C | **A/R** | S | - | I | C | - | I |
| **Data Contract Specification** | A | R | S | C | I | - | - | C |
| **Data Contract YAML** | C | R | S | - | - | - | - | C |
| Consumer Contract Review | A | C | - | - | S | - | - | R |
| **Data Catalog & Metadata** | C | C | R | **A/R** | I | - | - | I |
| **Data Quality Design** | C | C | S | **A/R** | I | - | - | C |
| **Risk Assessment** | C | R | - | S | I | - | A/R | I |
| **RoPA** | C | C | - | S | I | - | **A/R** | - |
| **DPIA** (jika diperlukan) | C | S | - | S | I | - | **A/R** | C |
| **Infrastructure Brief** | C | **A/R** | S | - | C | S | - | - |
| Security Design | C | A | S | - | I | R | C | - |
| DB Provisioning Script | - | C | R | - | - | A | - | - |
| EDA Report | C | C | R | A | I | - | - | - |
| Dashboard Design | A | C | - | R | S | - | - | C |
| Design Phase Gate Sign-off | **A** | C | C | C | S | C | C | C |

---

## Fase 3 — Development

| Aktivitas / Deliverable | DPO | DA | DE | DS | PM | SRE | LGL | CON |
|---|---|---|---|---|---|---|---|---|
| Dev Environment Setup | I | C | S | - | I | **A/R** | - | - |
| CI/CD Pipeline Setup | I | C | S | - | I | **A/R** | - | - |
| Bronze (Ingestion) Layer | C | C | **A/R** | - | I | S | - | - |
| Silver (Cleansing) Layer | C | C | **A/R** | S | I | - | - | - |
| Gold (Business) Layer | C | S | **A/R** | S | I | - | - | - |
| DQ Rules Implementation | - | C | R | **A** | I | - | - | - |
| API Development | C | C | **A/R** | - | I | S | - | C |
| PII Masking Implementation | C | A | R | S | I | - | C | - |
| **Pipeline Brief** | C | C | **A/R** | - | I | - | - | - |
| **API Brief** | C | C | **A/R** | - | I | - | - | I |
| Code Review | - | R | S | - | - | S | - | - |
| Unit & Integration Tests | - | C | **A/R** | S | I | S | - | - |
| Performance Tuning | C | C | **A/R** | - | I | S | - | - |
| Security Hardening | C | A | S | - | I | R | C | - |
| Monitoring & Alerting Setup | I | C | S | S | I | **A/R** | - | - |
| **UAT Test Cases** | C | C | - | S | **A/R** | - | - | C |

---

## Fase 4 — Delivery

| Aktivitas / Deliverable | DPO | DA | DE | DS | PM | SRE | LGL | CON |
|---|---|---|---|---|---|---|---|---|
| UAT Execution | C | - | S | S | **A** | - | - | R |
| UAT Defect Resolution | C | C | **A/R** | - | S | - | - | C |
| UAT Sign-off | **A** | C | - | - | S | - | - | R |
| Production Deployment | C | C | S | - | A | **R** | - | I |
| Consumer Access Provisioning | C | - | S | - | I | **A/R** | - | C |
| Consumer Onboarding | A | - | S | **R** | S | - | - | C |
| Go-Live Announcement | **A/R** | - | - | - | S | I | I | I |
| Post-Launch Hypercare (2 minggu) | C | C | S | **R** | A | S | - | C |
| Data Catalog Finalization | C | C | S | **A/R** | I | - | - | - |

---

## Fase 5 — Monitoring/Evaluation

| Aktivitas / Deliverable | DPO | DA | DE | DS | PM | SRE | LGL | CON |
|---|---|---|---|---|---|---|---|---|
| Daily Pipeline Monitoring | I | - | S | - | - | **A/R** | - | - |
| Data Quality Monitoring | C | - | S | **A/R** | I | S | - | I |
| **Monthly Quality Report** | C | - | S | **A/R** | I | - | - | I |
| **Monthly Cost Report** | C | - | - | - | **A/R** | S | - | - |
| Consumer Feedback Collection | **A** | - | - | R | S | - | - | C |
| **Incident Management** | C | C | S | S | A | **R** | - | I |
| Post-Mortem | C | R | S | S | **A** | S | - | C |
| Version Planning | **A** | R | C | C | S | C | C | C |
| Breaking Change Notification | **A/R** | C | - | - | S | - | - | I |
| Quarterly Risk Review | C | R | - | S | A | - | **R** | I |
| Annual Data Governance Audit | C | S | - | S | I | - | **A/R** | - |

---

## Fase 6 — End of Service Life

| Aktivitas / Deliverable | DPO | DA | DE | DS | PM | SRE | LGL | CON |
|---|---|---|---|---|---|---|---|---|
| EoSL Decision | **A** | C | - | - | S | - | C | C |
| Consumer Migration Planning | A | C | S | S | **R** | - | - | C |
| EoSL Announcement | **A/R** | - | - | - | S | I | I | R |
| Data Archival | C | C | S | A | I | **R** | C | - |
| PII Deletion | C | C | S | S | I | R | **A** | - |
| Infrastructure Decommission | C | C | - | - | A | **R** | - | - |
| **EoSL Report** | **A** | C | - | - | R | S | C | I |
| Lessons Learned | A | R | S | S | S | S | - | C |

---

## Catatan Governance

| Aturan | Detail |
|---|---|
| Setiap aktivitas punya **tepat 1 Accountable (A)** | Jika ada 2 A, klarifikasi kepemilikan dulu |
| Responsible (R) boleh lebih dari 1 | Khususnya untuk pekerjaan kolaboratif |
| Setiap perubahan Data Contract | Wajib ada C dari Consumer + A dari DPO |
| Setiap perubahan yang menyentuh PII | Wajib ada C dari Legal (LGL) |
| Breaking changes ke consumer | Wajib ada I ke Consumer minimum 3 bulan sebelumnya |
