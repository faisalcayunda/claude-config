# Lifecycle Reference: Data Product Lifecycle + PM² + Ways of Working

## Sections in This File

| Seksi | Konten | Mulai Baris |
|---|---|---|
| 6 Fase Lifecycle | Ringkasan setiap fase | ~20 |
| Fase 1: Bootstrap | Aktivitas, deliverable, RASCI, tools | ~60 |
| Fase 2: Design | Aktivitas, deliverable, RASCI, tools | ~120 |
| Fase 3: Development | Aktivitas, deliverable, RASCI, tools | ~190 |
| Fase 4: Delivery | Aktivitas, deliverable, RASCI, tools | ~250 |
| Fase 5: Monitoring/Evolution | Aktivitas, deliverable, RASCI, tools | ~300 |
| Fase 6: EoSL | Aktivitas, deliverable, RASCI, tools | ~360 |
| PM² Integration | Fase PM² vs Lifecycle | ~410 |
| JIRA Structure | Epic/Story/Task per role | ~450 |
| Ways of Working | Ceremonies, rituals, norms | ~540 |
| RASCI Master Matrix | Semua peran × aktivitas | ~610 |

---

## 6 Fase Lifecycle Data Product

```
Bootstrap → Design → Development → Delivery → Monitoring/Evaluation → EoSL
```

| Fase | Tujuan | Gate/Exit Criteria |
|---|---|---|
| **1. Bootstrap** | Validasi bisnis case, scope, feasibility | Data Product Canvas disetujui DPO + Stakeholder |
| **2. Design** | Rancang arsitektur lengkap, contracts, privacy | Data Contract + DPIA disetujui, infra brief ter-sign-off |
| **3. Development** | Build pipeline, API, quality rules, testing | Semua test pass, staging deployment sukses |
| **4. Delivery** | Deploy ke production, UAT, go-live | UAT sign-off dari domain + consumer, monitoring aktif |
| **5. Monitoring/Evaluation** | Operate, measure, evaluate, improve | SLO terpenuhi, evaluasi berkala, versioning terkontrol |
| **6. EoSL** | Deprecate, archive, remove | Consumer notified 6+ bulan, data archived |

---

## Fase 1: Bootstrap

### Aktivitas Utama
1. Terima dan analisis Business Context Brief
2. Stakeholder identification dan alignment
3. Domain mapping workshop (Event Storming)
4. Feasibility assessment (teknis, regulasi, anggaran)
5. Initial data profiling dari source systems (jika tersedia)
6. Buat Data Product Canvas
7. Buat Data Product Proposal
8. Presentasi dan sign-off oleh DPO + stakeholder

### Deliverables
- `bootstrap/proposal.md` — Data Product Proposal
- `bootstrap/canvas.md` — Data Product Canvas (filled)
- `bootstrap/data-profiling-prelim.md` — Preliminary Data Profiling Report
- `bootstrap/business-process-research.md` — Business Process Research & Context

### RASCI Bootstrap
| Aktivitas | DPO | DA | DE | DS | PM | DME |
|---|---|---|---|---|---|---|
| Brief analysis | A | R | I | I | S | R |
| Domain mapping | A | R | S | S | S | R |
| Canvas creation | A | R | S | S | S | C |
| Feasibility | A | R | R | S | R | C |
| Proposal sign-off | A | C | I | I | R | C |

### Tools (Bootstrap Phase)
- Miro / FigJam (Event Storming workshop)
- DataHub / OpenMetadata (initial catalog entry)
- Jira (project setup, backlog init)
- Confluence / Docusaurus (document draft)

---

## Fase 2: Design

### Aktivitas Utama
1. Detailed data modeling dan schema design
2. Data Contract specification (YAML)
3. Output port design (tabel, API, stream, file)
4. SLO/SLA definition
5. Privacy assessment (DPIA jika diperlukan)
6. RoPA creation (jika ada data pribadi)
7. Data Catalog entry (metadata lengkap)
8. Data Quality rules design
9. Risk Assessment & Mitigation
10. Infra brief (topology, cost projection, security setup, DB provisioning)
11. Dashboard design (wireframe)
12. Preliminary EDA template

### Deliverables
- `design/design-document.md` — Data Product Design Document
- `design/data-contract.yaml` — Data Contract (YAML, DataContract spec)
- `design/data-catalog.md` — Data Catalog & Metadata
- `design/quality-design.md` — Data Quality Design
- `design/risk-assessment.md` — Risk Assessment & Mitigation
- `design/ropa.md` — Record of Processing Activities (jika ada PII)
- `design/dpia.md` — Data Protection Impact Assessment (jika diharuskan)
- `design/infra-brief.md` — Infrastructure Brief (Volume, Cost, Topology, Security, DB)
- `design/eda-template.md` — Preliminary EDA Template
- `design/dashboard-design.md` — Dashboard Design Document

### RASCI Design
| Aktivitas | DPO | DA | DE | DS | PM | Legal |
|---|---|---|---|---|---|---|
| Data modeling | A | R | S | S | I | I |
| Data contract | A | R | R | C | I | I |
| DPIA / RoPA | A | S | I | C | I | R |
| Infra brief | A | R | R | I | S | I |
| Quality design | A | S | S | R | I | I |
| Risk assessment | A | R | S | R | S | C |
| Design sign-off | A | C | C | C | R | C |

### Tools (Design Phase)
- DataHub / OpenMetadata (catalog)
- datacontract-cli (lint + validate)
- Eraser.io / dbdiagram.io (data modeling)
- Lucidchart / draw.io (architecture diagrams)
- Great Expectations / Soda (quality rule authoring)

---

## Fase 3: Development

### Aktivitas Utama
1. Environment setup (dev/staging/prod)
2. Source system connectivity dan CDC setup
3. Data pipeline development (ingestion, transformation, loading)
4. API development (REST/GraphQL sesuai output port)
5. Data quality rule implementation
6. Unit testing dan integration testing
7. Security implementation (RLS, CLS, masking)
8. CI/CD pipeline setup
9. Documentation update (pipeline brief, API brief)
10. Staging deployment dan verification
11. UAT preparation (test cases, test data)
12. Performance testing

### Deliverables
- `development/pipeline-brief.md` — Data Pipeline Brief
- `development/api-brief.md` — Data API Brief
- `development/uat-template.md` — UAT Template
- `development/integration-test.md` — Integration Test Template
- CI/CD pipeline (Jenkinsfile / GitHub Actions)
- Data Contract tests (datacontract-cli test)

### RASCI Development
| Aktivitas | DPO | DA | DE | DS | PM | SRE |
|---|---|---|---|---|---|---|
| Pipeline dev | I | C | R | S | S | S |
| API dev | I | R | R | S | S | S |
| Quality impl | I | C | R | R | S | S |
| Security impl | I | R | R | S | I | R |
| CI/CD setup | I | C | S | I | I | R |
| UAT prep | A | C | S | S | R | I |

### Tools (Development Phase)
- dbt (transformation)
- Apache Airflow (orchestration)
- Apache Kafka (streaming, jika diperlukan)
- Great Expectations + Soda (quality testing)
- Jenkins / GitHub Actions (CI/CD)
- Postman / Insomnia (API testing)
- pytest (Python unit tests)

---

## Fase 4: Delivery

### Aktivitas Utama
1. Production deployment
2. Consumer onboarding dan access provisioning
3. UAT execution (bersama consumer)
4. Go/No-Go review
5. Go-live
6. Hypercare period (2 minggu pertama)
7. Data Contract registrasi formal di catalog
8. Internal handover ke operations team

### Deliverables
- UAT sign-off document (diisi dari `uat-template.md`)
- Production deployment record
- Consumer access manifest
- Monitoring dashboard aktif
- Runbook operasional

### RASCI Delivery
| Aktivitas | DPO | DA | DE | DS | PM | SRE | Consumer |
|---|---|---|---|---|---|---|---|
| Prod deployment | A | C | R | I | S | R | I |
| UAT execution | A | I | S | S | R | I | R |
| Go/No-Go | A | C | C | C | R | C | C |
| Monitoring setup | I | C | S | S | I | R | I |
| Handover | A | C | R | R | R | C | I |

---

## Fase 5: Monitoring & Evolution

### Aktivitas Utama
1. SLO monitoring (freshness, availability, quality)
2. Usage analytics (siapa mengakses, seberapa sering)
3. Consumer feedback collection
4. Incident management (P1/P2/P3 classification)
5. Version management (patch → minor → major releases)
6. Performance tuning
7. Cost monitoring dan optimization
8. Quarterly data product review
9. Schema evolution (backward-compatible changes)

### Deliverables (Template → diisi per periode)
- `monitoring/metrics-catalog.md` — Data Product Metrics & Insights Catalog
- `monitoring/quality-report-template.md` — Data Quality Report
- `monitoring/cost-report-template.md` — Cost Report
- `monitoring/incident-template.md` — Incident Management Template

### Ritme Monitoring
| Frekuensi | Aktivitas |
|---|---|
| Real-time | Alert SLO breach, pipeline failure, data quality alert |
| Harian | Quality scorecard, freshness check, pipeline run log |
| Mingguan | Usage analytics, consumer health check |
| Bulanan | Cost report, quality trend, consumer feedback |
| Kuartalan | Data product review, versioning decision |

---

## Fase 6: End of Service Life (EoSL)

### Aktivitas Utama
1. EoSL assessment (gunakan checklist di bawah)
2. Consumer impact analysis
3. Notifikasi consumer (minimum 6 bulan untuk major products)
4. Migration path recommendation
5. Deprecation announcement dan timeline
6. Data archival (sesuai retention policy)
7. Infrastructure decommissioning
8. Final EoSL report

### Trigger untuk EoSL Assessment
- No active consumers > 3 bulan
- Business domain ditutup atau di-merge
- Major breaking changes yang tidak bisa backward-compatible
- Data source underlying ditutup
- Regulatory requirement mengharuskan penghapusan
- Replacement data product sudah tersedia dan mature

### Deliverable
- `eosl/eosl-report.md` — End of Service Life Report

### Checklist EoSL Decision
```
[ ] Apakah ada consumer aktif dalam 3 bulan terakhir? 
    (Ya → jangan EoSL dulu, komunikasikan)
[ ] Apakah ada consumer yang kontrak/SLA-nya belum expired?
    (Ya → perpanjang periode atau negosiasikan transisi)
[ ] Apakah ada data product pengganti?
    (Tidak → pertimbangkan dulu untuk membuat sebelum EoSL)
[ ] Apakah data perlu diarsipkan sesuai regulasi?
    (Ya → execute data archival sebelum sistem dihapus)
[ ] Apakah notifikasi consumer sudah dilakukan?
    (Minimal 6 bulan untuk Tier-Gold/Silver)
```

---

## PM² Integration

PM² adalah metodologi project management Open Source dari Komisi Eropa (pm2.europa.eu), sangat sesuai untuk proyek pemerintah dan semi-pemerintah.

### Pemetaan Fase PM² → Lifecycle Data Product

| PM² Phase | Data Product Phase | PM² Artifact Relevan |
|---|---|---|
| **Initiating** | Bootstrap | Business Case, Project Charter, Stakeholder Matrix |
| **Planning** | Design | Project Handbook, Work Plan, Communication Plan |
| **Executing** | Development + Delivery | Progress Reports, Change Requests |
| **Monitor & Control** | (parallel semua fase) | Project Status Report, Issue Log, Risk Log |
| **Closing** | EoSL | Project-End Report, Lessons Learned |

### PM² Roles → Data Product Roles
| PM² Role | Data Product Equivalent |
|---|---|
| Project Owner | Data Product Owner (DPO) |
| Project Manager | Project Manager / Delivery Lead |
| Business Manager | Domain Lead / Business Analyst |
| Solution Provider | Data Engineer + Data Architect |
| Project Core Team | Data Team (DE + DA + DS + DS) |

---

## JIRA Structure untuk Data Product Development

### Hierarchy
```
Initiative (Program-level)
└── Epic (per Data Product per fase)
    └── Story (user-facing capability)
        └── Task (technical work item)
        └── Subtask (granular step)
    └── Bug (data quality issue)
    └── Spike (research, time-boxed)
```

### Epic Naming Convention
```
[DOMAIN] [PHASE] - [Data Product Name]
Contoh: [FINANCE] [DESIGN] - Transaction Ledger DP
```

### Story Template (per deliverable)

**Standard Story Format:**
```
Sebagai [role]
Saya ingin [aksi/kapabilitas]
Sehingga [benefit/outcome bisnis]

Acceptance Criteria:
- [ ] [Kriteria 1 - testable]
- [ ] [Kriteria 2 - testable]
- [ ] [Kriteria 3 - testable]

Definition of Done:
- [ ] Code review passed
- [ ] Unit tests written dan passing
- [ ] Documentation updated
- [ ] Data contract validated (datacontract-cli lint)
- [ ] Privacy checklist verified
```

### Task Breakdown per Role (Template)

**Data Architect Tasks (per fase):**
- Bootstrap: Domain boundary review, Canvas facilitation, Architecture feasibility
- Design: Schema design, Output port specification, ADR creation, Infra topology design
- Development: Code review (schema/contract), Architecture guardrail validation
- Monitoring: Architecture debt review, Evolution assessment

**Data Engineer Tasks (per fase):**
- Design: Source system investigation, Pipeline feasibility, Technical infra sizing
- Development: Pipeline development, API development, CI/CD setup, Quality rule implementation
- Delivery: Production deployment, Performance tuning, Consumer onboarding
- Monitoring: Pipeline maintenance, Incident resolution, Performance optimization

**Data Analyst Tasks (per fase):**
- Bootstrap: Business requirements analysis, Data profiling (preliminary)
- Design: EDA template, Metrics definition, Dashboard design
- Development: EDA execution, Quality rule validation, UAT test case creation
- Monitoring: Quality report, Usage analytics, Consumer insights

**Data Scientist Tasks (per fase):**
- Design: Feature requirements (jika ML use case), Statistical profiling approach
- Development: Statistical analysis, Anomaly detection model (jika diperlukan), ML feature validation
- Monitoring: Model drift monitoring (jika ada ML), Predictive quality alerting

**Project Manager Tasks (per fase):**
- Bootstrap: Project charter, Stakeholder alignment, Timeline planning
- Design: Resource planning, Risk tracking, Sprint planning
- Development: Sprint management, Impediment removal, Progress reporting
- Delivery: UAT coordination, Go-live planning, Stakeholder communication
- Monitoring: Monthly review facilitation, KPI tracking, Cost reporting

### Sprint Cadence Recommendation

| Sprint | Durasi | Fokus |
|---|---|---|
| Sprint 0 | 2 minggu | Setup infrastruktur, tooling, team onboarding |
| Sprint 1-2 | 2 minggu/sprint | Bootstrap + awal Design |
| Sprint 3-4 | 2 minggu/sprint | Design selesai + Development mulai |
| Sprint 5-8 | 2 minggu/sprint | Development (pipeline, API, testing) |
| Sprint 9 | 2 minggu | Delivery (UAT, staging, pre-prod) |
| Sprint 10 | 2 minggu | Go-live + hypercare |
| Sprint 11+ | Rolling | Monitoring & Evolution |

---

## Ways of Working

### Ceremonies

| Ceremony | Frekuensi | Durasi | Peserta | Tujuan |
|---|---|---|---|---|
| Daily Standup | Harian | 15 menit | Tim inti | Sinkronisasi, blockers |
| Sprint Planning | Per sprint | 2-4 jam | Tim inti | Commit sprint backlog |
| Sprint Review | Per sprint | 1 jam | Tim + Stakeholder | Demo dan feedback |
| Sprint Retrospective | Per sprint | 1 jam | Tim inti | Improvement |
| Backlog Refinement | Mingguan | 1 jam | DPO + Tim | Prioritas dan estimasi |
| Data Contract Review | Ad-hoc | 1 jam | DA + DE + DS + Consumer | Validasi contract changes |
| Architecture Decision | Ad-hoc | 1-2 jam | DA + DE + PM | ADR creation |
| Monthly Data Review | Bulanan | 1 jam | DPO + Stakeholder | KPI, health, roadmap |
| Governance Council | Bulanan | 1 jam | Semua DPO + CDO | Global policy update |

### Definition of Done (Data Product Stories)

```
Sebuah Story dianggap Done ketika:
Technical:
- [ ] Code dicommit ke main branch (setelah review)
- [ ] Semua automated tests pass (unit + integration)
- [ ] datacontract-cli lint dan test pass
- [ ] No critical security findings
- [ ] Performance benchmark terpenuhi

Documentation:
- [ ] Markdown docs diupdate di Git
- [ ] Data catalog entry diupdate
- [ ] Changelog entry ditambahkan

Compliance:
- [ ] Privacy checklist diverifikasi
- [ ] Data classification tag diaplikasikan
- [ ] Audit log berfungsi

Stakeholder:
- [ ] DPO review dan approve
- [ ] Consumer (jika impacted) dikonfirmasi
```

### Branching Strategy (Git)

```
main          → production-ready (protected)
├── develop   → integration branch
│   ├── feature/[JIRA-ID]-[deskripsi]   → development work
│   ├── fix/[JIRA-ID]-[deskripsi]       → bug fixes
│   └── docs/[JIRA-ID]-[deskripsi]      → documentation only
└── release/[semver]                    → release candidate
```

---

## RASCI Master Matrix

Legenda: R=Responsible, A=Accountable, S=Support, C=Consulted, I=Informed, —=Tidak Terlibat

| Aktivitas | DPO | DA | DE | DS | DS(ci) | PM | SRE | Legal | Consumer |
|---|---|---|---|---|---|---|---|---|---|
| Business case | A | C | I | I | I | R | I | C | C |
| Domain mapping | A | R | S | S | S | S | I | I | C |
| Canvas creation | A | R | S | S | S | S | I | I | C |
| Schema design | A | R | R | C | S | I | S | I | C |
| Data contract | A | R | R | C | S | I | S | C | C |
| DPIA/RoPA | A | S | I | S | S | S | I | R | I |
| Infra design | A | R | R | I | I | I | R | I | I |
| Pipeline dev | I | C | R | S | S | S | S | I | I |
| API dev | I | R | R | S | I | S | S | I | C |
| Quality impl | I | C | R | R | S | I | S | I | I |
| Security impl | A | R | R | S | I | I | R | C | I |
| UAT | A | C | S | S | S | R | S | I | R |
| Production deploy | A | C | R | I | I | S | R | I | I |
| SLO monitoring | A | I | S | R | S | I | R | I | I |
| Incident mgmt | A | C | R | R | S | S | R | I | I |
| Version release | A | R | R | S | S | S | S | C | I |
| EoSL decision | A | C | I | C | I | R | C | C | C |
