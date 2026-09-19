---
title: "Sprint Plan — Sprint <N> — <Nama Data Product>"
sidebar_label: "Sprint <N> Plan"
sidebar_position: 4
description: "Rencana sprint detail: goal, backlog, kapasitas, dan success criteria"
tags: [project-management, sprint, planning, agile]
data_product_id: "<domain>/<data-product-name>/v<version>"
phase: "<bootstrap|design|development|delivery|monitoring>"
sprint_number: "<N>"
sprint_start: "<YYYY-MM-DD>"
sprint_end: "<YYYY-MM-DD>"
last_updated: "<YYYY-MM-DD>"
---

# Sprint `<N>` Plan — `<Nama Data Product>`

**Periode:** `<YYYY-MM-DD>` s.d. `<YYYY-MM-DD>`  
**Sprint Goal:** `<Satu kalimat yang menjelaskan tujuan sprint ini>`

---

## Kapasitas Tim

| Anggota | Role | Hari Tersedia | Capacity (SP) | Catatan |
|---|---|---|---|---|
| `<Nama DE>` | Data Engineer | `<10>` | `<15>` | |
| `<Nama DA>` | Data Architect | `<10>` | `<10>` | `<Review + design half-time>` |
| `<Nama DS>` | Data Steward | `<10>` | `<8>` | |
| `<Nama PM>` | Project Manager | `<10>` | `<5>` | |
| **Total** | | | **`<38 SP>`** | `<Buffer: 20% = 30 SP committed>` |

---

## Sprint Backlog

### Kritis Must Have (P0 — Sprint Goal blockers)

| Jira ID | Story / Task | Assignee | Estimasi | Status |
|---|---|---|---|---|
| `<PROJ-101>` | `<Story: Build Bronze ingestion pipeline for sumber_a>` | `<DE>` | `<8 SP>` | `<[ ] TODO>` |
| `<PROJ-102>` | `<Story: Implement DQ completeness rules>` | `<DE+DS>` | `<5 SP>` | `<[ ] TODO>` |
| `<PROJ-103>` | `<Task: DA review Bronze schema>` | `<DA>` | `<2 SP>` | `<[ ] TODO>` |

**Subtotal P0:** `<15 SP>`

### Tinggi Should Have (P1 — High value, tidak block sprint goal)

| Jira ID | Story / Task | Assignee | Estimasi | Status |
|---|---|---|---|---|
| `<PROJ-104>` | `<Story: Setup monitoring alerting untuk Bronze>` | `<SRE+DS>` | `<5 SP>` | `<[ ] TODO>` |
| `<PROJ-105>` | `<Task: Update Data Catalog entry>` | `<DS>` | `<2 SP>` | `<[ ] TODO>` |
| `<PROJ-106>` | `<Task: Write Pipeline Brief — ingestion section>` | `<DE>` | `<3 SP>` | `<[ ] TODO>` |

**Subtotal P1:** `<10 SP>`

### Sedang Nice to Have (P2 — jika ada sisa kapasitas)

| Jira ID | Story / Task | Assignee | Estimasi | Status |
|---|---|---|---|---|
| `<PROJ-107>` | `<Task: Performance benchmark Bronze ingestion>` | `<DE>` | `<3 SP>` | `<[ ] TODO>` |
| `<PROJ-108>` | `<Task: Document carryover dari Sprint sebelumnya>` | `<PM>` | `<2 SP>` | `<[ ] TODO>` |

**Subtotal P2:** `<5 SP>`

---

**Total Committed:** `<25 SP>` / `<30 SP kapasitas>`  
**Buffer untuk bugs & support:** `<5 SP>`

---

## Carryover dari Sprint Sebelumnya

| Jira ID | Story | Alasan Carryover | Estimasi Sisa |
|---|---|---|---|
| `<PROJ-098>` | `<Unfinished item>` | `<Blocker: akses DB sumber belum diberikan>` | `<3 SP>` |

---

## Dependensi & Risiko Sprint Ini

| Dependensi / Risiko | Probabilitas | Dampak | Mitigasi |
|---|---|---|---|
| `<Akses ke DB sumber belum dikonfirmasi>` | `<Tinggi>` | `<Tinggi>` | `<PM follow-up hari ini; jika tidak ada H+2, eskalasi ke DPO>` |
| `<DA availability — hanya 50% sprint ini>` | `<Confirmed>` | `<Sedang>` | `<Pre-align semua review items di Sprint Planning>` |
| `<Sumber API sedang dalam maintenance Rabu>` | `<Sedang>` | `<Sedang>` | `<Coordinate dengan tim sumber; plan test untuk Kamis>` |

---

## Success Criteria Sprint Ini

```
[ ] Bronze ingestion pipeline berjalan sukses di staging environment
[ ] Semua DQ completeness rules ter-implement dan passed
[ ] Zero P0 bugs open di akhir sprint
[ ] Pipeline Brief — section ingestion sudah di-commit ke Git
[ ] Sprint Review demo sudah dilaksanakan
[ ] Retrospective action items dari sprint lalu: X/Y resolved
```

---

## Agenda Sprint Ceremonies

| Ceremony | Tanggal & Waktu | Link |
|---|---|---|
| Sprint Planning | `<YYYY-MM-DD, 09:00–12:00 WIB>` | `<Zoom/Meet link>` |
| Daily Standup | `<Setiap hari, 09:15–09:30 WIB>` | `<Zoom/Meet link>` |
| Backlog Refinement | `<YYYY-MM-DD, 14:00–15:00 WIB>` | `<Zoom/Meet link>` |
| Sprint Review | `<YYYY-MM-DD, 14:00–15:00 WIB>` | `<Zoom/Meet link>` |
| Sprint Retrospective | `<YYYY-MM-DD, 15:30–16:30 WIB>` | `<Zoom/Meet link>` |

---

## Catatan Planning Session

`[Isi setelah Sprint Planning selesai]`

**Keputusan yang dibuat:**
- `<Keputusan 1>`
- `<Keputusan 2>`

**Action items dari Planning:**
| Aksi | Owner | Deadline |
|---|---|---|
| `<>` | `<>` | `<>` |
