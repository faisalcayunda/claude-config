# Bank Prompt Context Gathering — Prompt Khusus Melengkapi Konteks Project
# Context Gathering Prompt Bank — Dedicated Prompts for Completing Project Context

> **Prinsip Utama**: Flipped Interaction — AI yang bertanya, pengguna yang menjawab.
> Dibangun dari: Anthropic (Context Engineering for AI Agents), McKinsey TEAM FOCUS, OnboardMap 40 Questions, IIBA BABOK Elicitation, Motivational Interviewing (Engage-Focus-Evoke-Plan), AURA Framework, Parameter Chain Pattern, Amazon 6-Pager, 100+ sumber riset Round 4.

---

## Cara Menggunakan / How to Use

### Langkah 1: Pilih prompt sesuai kebutuhan
- **CTX-INIT**: Memulai project baru (wajib, selalu mulai dari sini)
- **CTX-DEEP**: Memperdalam area tertentu yang masih kurang
- **CTX-SYNTH**: Mensintesis jawaban menjadi SSOT
- **CTX-VALIDATE**: Memvalidasi SSOT yang sudah ada

### Langkah 2: Jalankan prompt → jawab pertanyaan AI → ulangi hingga konteks lengkap
### Langkah 3: Generate SSOT menggunakan CTX-SYNTH

---

## PROMPT INISIASI PROJECT (CTX-INIT)

### CTX-INIT-01 — Quick Start (2-3 menit, Tier 1)
```
Saya ingin memulai project baru. Bantu saya memperjelas konteksnya.

Bertindaklah sebagai konsultan senior yang melakukan project intake.
Tanyakan saya 5-8 pertanyaan esensial satu per satu untuk memahami:
1. Apa project ini dan apa masalah yang ingin diselesaikan
2. Siapa klien/sponsor dan siapa pengguna akhir
3. Berapa budget dan timeline
4. Apa yang sudah ada vs yang perlu dibangun

Mulai dari pertanyaan paling penting. Ajukan SATU pertanyaan pada satu waktu.
Tunggu jawaban saya sebelum melanjutkan ke pertanyaan berikutnya.
Setelah semua pertanyaan terjawab, rangkum dalam format Project Context Canvas.
```

### CTX-INIT-02 — Standard Intake (10-15 menit, Tier 2)
```
Saya ingin melakukan project intake lengkap untuk project baru.

Bertindaklah sebagai lead consultant McKinsey yang melakukan discovery session.
Gunakan pendekatan Engage → Focus → Evoke → Plan:

ENGAGE (3 pertanyaan): Bangun pemahaman dasar tentang project, klien, dan motivasi.
FOCUS (5 pertanyaan): Gali masalah spesifik, scope, stakeholder, dan constraints.
EVOKE (5 pertanyaan): Eksplorasi success criteria, risiko, dan technical landscape.
PLAN (3 pertanyaan): Tentukan delivery approach, timeline milestones, dan next steps.

Ajukan 3-5 pertanyaan per sesi. Tunggu jawaban saya sebelum lanjut ke sesi berikutnya.
Di akhir, buatkan Project Context Canvas lengkap sesuai template /ideas.
```

### CTX-INIT-03 — Deep Enterprise Intake (30+ menit, Tier 3-4)
```
Saya memulai project enterprise/pemerintah skala besar. Butuh intake mendalam.

Bertindaklah sebagai Partner consulting firm yang memimpin scoping engagement.
Lakukan intake terstruktur dalam 6 kategori (OnboardMap + McKinsey framework):

Kategori 1 — Vision & Goals: Tujuan, success metrics (SMART), dampak jika gagal
Kategori 2 — Stakeholders: Decision makers, RASCI, politik organisasi, sponsor strength
Kategori 3 — Scope & Constraints: In/out scope, regulatory, budget, timeline hard stops
Kategori 4 — Organizational Context: Maturity, culture, change readiness, prior attempts
Kategori 5 — Technical Landscape: Systems, data, infrastructure, integration points
Kategori 6 — Working Preferences: Methodology, tools, communication, reporting cadence

Per kategori: ajukan 3-5 pertanyaan. Tandai mana yang sudah terjawab vs belum.
Jika jawaban saya menunjukkan kompleksitas tinggi di satu area, ajukan follow-up questions.
Di akhir setiap kategori, rangkum temuan dan minta konfirmasi sebelum lanjut.
Setelah semua kategori selesai, generate Project Context Canvas + skill recommendation.
```

---

## PROMPT PENDALAMAN PER AREA (CTX-DEEP)

### CTX-DEEP-01 — Pendalaman Problem & Opportunity
```
Konteks project saya: [paste SSOT atau deskripsi singkat]

Bantu saya memperdalam pemahaman tentang masalah dan peluang.
Tanyakan saya tentang:
- Root cause dari masalah ini (gunakan 5-Why)
- Siapa yang paling terdampak dan bagaimana
- Berapa kerugian (Rp/waktu/opportunity cost) dari masalah ini
- Solusi apa yang sudah pernah dicoba dan mengapa gagal
- Apa yang berubah sehingga sekarang menjadi prioritas

Ajukan satu pertanyaan pada satu waktu. Gunakan jawaban sebelumnya untuk membuat pertanyaan berikutnya lebih tajam.
```

### CTX-DEEP-02 — Pendalaman Stakeholder & User
```
Konteks project saya: [paste SSOT atau deskripsi singkat]

Bantu saya memetakan stakeholder dan pengguna lebih dalam.
Tanyakan saya tentang:
- Siapa decision maker final (nama + jabatan)
- Siapa yang bisa mem-block project dan kenapa
- Berapa jumlah end users dan segmentasi mereka
- 2-3 persona utama: apa pain points, goals, dan behavior mereka
- Bagaimana proses approval dan sign-off berlangsung
- Siapa internal champion yang akan drive adoption

Bantu saya membangun stakeholder map dengan Interest vs Influence matrix.
```

### CTX-DEEP-03 — Pendalaman Technical & Data
```
Konteks project saya: [paste SSOT atau deskripsi singkat]

Bantu saya memetakan landscape teknis dan data.
Tanyakan saya tentang:
- Tech stack saat ini (languages, frameworks, databases, cloud)
- Sistem legacy yang harus dipertahankan vs bisa diganti
- API dan integration points yang sudah ada
- Volume data, format, dan kualitas data saat ini
- Sumber data utama dan data ownership
- Security requirements (enkripsi, auth, compliance)
- Infrastructure constraints (on-prem vs cloud, budget compute)
- Observability dan monitoring yang ada

Identifikasi technical risks dan architectural decisions yang perlu diambil segera.
```

### CTX-DEEP-04 — Pendalaman Government/SPBE
```
Konteks project saya: [paste SSOT atau deskripsi singkat]

Bantu saya melengkapi konteks pemerintah/SPBE.
Tanyakan saya tentang:
- Level instansi (K/L/Prov/Kab/Kota) dan skor SPBE saat ini
- Domain SPBE yang menjadi fokus utama
- Perpol/Pergub/Perbup yang mengatur tata kelola data
- Status implementasi Satu Data Indonesia
- Walidata dan Produsen Data yang sudah ditunjuk
- Pagu anggaran dan mekanisme pengadaan (LKPP/e-Katalog/direct)
- Arsitektur SPBE existing (enterprise architecture)
- Tingkat kematangan digital SDM instansi

Map jawaban ke 47 indikator evaluasi SPBE.
```

### CTX-DEEP-05 — Pendalaman Data Governance
```
Konteks project saya: [paste SSOT atau deskripsi singkat]

Bantu saya melengkapi konteks data governance.
Tanyakan saya tentang:
- Ada framework DG formal? Jika ya, apa? (DAMA-DMBOK/COBIT/custom)
- Data governance council/committee sudah ada?
- Data steward sudah ditunjuk per domain?
- Kebijakan data (classification, retention, sharing) sudah ada?
- Data quality metrics yang diukur saat ini
- Metadata management tools dan practices
- Master Data Management status
- Data privacy/protection compliance (UU PDP/GDPR)

Assess maturity level per DAMA-DMBOK knowledge area (KA-01 s/d KA-14).
```

### CTX-DEEP-06 — Pendalaman Delivery & Methodology
```
Konteks project saya: [paste SSOT atau deskripsi singkat]

Bantu saya memperjelas delivery approach.
Tanyakan saya tentang:
- Methodology sekarang (Scrum/Kanban/SAFe/Waterfall/hybrid)
- Sprint/iteration duration dan cadence meetings
- Tools (Jira/Linear/Notion/Azure DevOps/etc)
- Definition of Done dan Definition of Ready
- Quality gates dan approval process
- Release strategy (CI/CD, manual, staged rollout)
- Communication channel dan reporting format
- Retrospective practices dan continuous improvement

Identifikasi delivery risks dan rekomendasi improvement.
```

---

## PROMPT SINTESIS KE SSOT (CTX-SYNTH)

### CTX-SYNTH-01 — Generate Project Context Canvas dari Percakapan
```
Berdasarkan semua informasi yang sudah kita diskusikan, buatkan
Project Context Canvas lengkap menggunakan template /ideas → templates/project-context-canvas-template.md.

Isi SEMUA section yang datanya sudah tersedia.
Untuk section yang datanya belum lengkap, tandai dengan [PERLU DILENGKAPI] + pertanyaan spesifik yang harus dijawab.
Sertakan:
- Skill mapping: skill mana yang dibutuhkan per fase
- Deliverable plan: deliverable prioritas per fase
- Gate criteria: apa yang harus true sebelum pindah fase
- Risk register: top 5 risks dengan mitigation
- Open questions: pertanyaan yang masih perlu dijawab
```

### CTX-SYNTH-02 — Update SSOT dari Informasi Baru
```
Ini adalah Project Context Canvas existing project saya:
[paste SSOT]

Informasi baru yang perlu diintegrasikan:
[paste informasi baru]

Update SSOT dengan:
1. Integrasikan informasi baru ke section yang relevan
2. Jika ada kontradiksi dengan info sebelumnya, tandai dan tanyakan mana yang benar
3. Update skill mapping jika scope berubah
4. Update risk register jika ada risiko baru
5. Tandai version baru dengan tanggal dan changelog
```

### CTX-SYNTH-03 — Generate Deliverable Plan dari SSOT
```
Berdasarkan Project Context Canvas ini:
[paste SSOT]

Buatkan deliverable plan lengkap:
1. List SEMUA deliverable yang dibutuhkan berdasarkan scope
2. Map setiap deliverable ke skill yang tepat (dari 10 skill IDEAS)
3. Tentukan urutan: prerequisite → companion → downstream
4. Estimasi effort per deliverable (S/M/L/XL)
5. Tentukan fase: Discover / Define / Build / Launch / Optimize
6. Berikan prompt siap pakai (dari bank-prompt.md) untuk setiap deliverable
7. Definisikan gate criteria per transisi fase
```

---

## PROMPT VALIDASI (CTX-VALIDATE)

### CTX-VALIDATE-01 — Completeness Check
```
Review Project Context Canvas ini dan identifikasi gaps:
[paste SSOT]

Untuk setiap section, evaluasi:
- ✅ Lengkap: semua informasi kritis tersedia
- ⚠️ Parsial: ada info tapi belum cukup untuk eksekusi
- ❌ Kosong: tidak ada informasi sama sekali

Untuk setiap gap yang ditemukan:
1. Jelaskan MENGAPA informasi ini penting
2. Berikan pertanyaan spesifik untuk mengisi gap
3. Siapa yang sebaiknya menjawab (sponsor/user/tech lead/data steward)
4. Apa risiko jika gap ini tidak diisi sebelum eksekusi dimulai

Prioritaskan: mana gap yang HARUS diisi sebelum Fase 1 vs bisa diisi sambil jalan.
```

### CTX-VALIDATE-02 — Assumption Audit
```
Review Project Context Canvas ini dan identifikasi semua ASUMSI implisit:
[paste SSOT]

Untuk setiap asumsi:
1. Tuliskan asumsi yang terdeteksi
2. Rating confidence: High (data-backed) / Medium (informed guess) / Low (pure assumption)
3. Impact jika asumsi salah: High / Medium / Low
4. Rekomendasi: Accept / Validate / Investigate
5. Cara validasi: pertanyaan / data / experiment / prototype

Fokus terutama pada asumsi tentang: user behavior, market size, technical feasibility, regulatory compliance, stakeholder support, dan budget adequacy.
```

### CTX-VALIDATE-03 — Cross-Stakeholder Consistency Check
```
Saya mengumpulkan konteks dari beberapa stakeholder berbeda.
Berikut input mereka:

Stakeholder A ([nama/jabatan]): [input]
Stakeholder B ([nama/jabatan]): [input]
Stakeholder C ([nama/jabatan]): [input]

Identifikasi:
1. Area KONSENSUS — semua stakeholder setuju
2. Area KONTRADIKSI — stakeholder bertentangan (flag for resolution)
3. Area BLIND SPOT — tidak dibahas oleh siapapun tapi penting
4. PRIORITAS yang berbeda — ranking berbeda dari stakeholder berbeda

Untuk setiap kontradiksi, rekomendasikan: siapa yang harus menjadi tie-breaker dan mengapa.
```

---

## PROMPT TIPE PROJECT SPESIFIK (CTX-TYPE)

### CTX-TYPE-01 — Product Development Intake
```
Saya ingin membangun produk baru: [deskripsi singkat].

Bertindak sebagai PM senior. Tanyakan saya secara progresif tentang:
- Target user dan problem-solution fit
- Competitive landscape dan differentiator
- Revenue/business model
- MVP scope vs full vision
- Success metrics (HEART/AARRR/North Star)
- Technical constraints dan platform choice
- Go-to-market strategy awal

Di akhir, rekomendasikan: skill mana yang harus dilibatkan per fase + deliverable prioritas.
```

### CTX-TYPE-02 — Data Governance Program Intake
```
Organisasi saya ingin membangun/meningkatkan data governance: [konteks].

Bertindak sebagai CDO/Data Governance Expert. Tanyakan secara progresif tentang:
- Motivasi: compliance, quality, atau strategic value?
- Maturity saat ini (CMMI-DMM / DCAM level estimate)
- Pain points data terbesar (quality, access, security, silos)
- Governance structure yang ada (council, steward, owner)
- Volume dan diversity data (structured, unstructured, streaming)
- Regulatory landscape (UU PDP, GDPR, SPBE, sector-specific)
- Technology stack data existing
- Budget dan sponsorship executive

Di akhir, map ke DAMA-DMBOK Knowledge Areas yang relevan + rekomendasikan roadmap.
```

### CTX-TYPE-03 — SPBE/Government Digital Transformation Intake
```
Instansi saya ingin meningkatkan skor SPBE / transformasi digital: [konteks].

Bertindak sebagai konsultan SPBE senior. Tanyakan secara progresif tentang:
- Level instansi dan skor SPBE terakhir
- 6 domain arsitektur SPBE: mana yang paling lemah?
- Indikator evaluasi mana yang underperform?
- Infrastruktur IT dan data center existing
- SDM digital: jumlah dan kompetensi
- Kebijakan internal tata kelola TIK yang sudah ada
- Integrasi dengan Satu Data Indonesia
- Pagu APBD/APBN dan mekanisme pengadaan

Di akhir, buatkan gap analysis per domain SPBE + roadmap + skill mapping IDEAS.
```

### CTX-TYPE-04 — IDEAS Proposal/Pitch Intake
```
Saya perlu membuat proposal untuk klien prospektif: [konteks].

Bertindak sebagai Business Development Manager IDEAS. Tanyakan tentang:
- Nama klien, tipe (K/L/Pemda/BUMN/Enterprise), dan contact person
- Kebutuhan klien (produk/layanan apa)
- Budget range dan sumber pendanaan (APBD/APBN/corporate)
- Timeline decision dan procurement process
- Kompetitor yang juga bidding
- Existing relationship dengan klien
- Previous engagement history (jika ada)
- Deliverables yang diharapkan dalam proposal

Di akhir, rekomendasikan service package + jalankan estimate_service_cost.py.
```

---

## PARAMETER CHAIN — Slot Tracking

Gunakan pola ini untuk track informasi yang sudah vs belum terkumpul:

```
PROJECT CONTEXT SLOTS:
[✅] Project name: ___
[✅] Description: ___
[  ] Client/Sponsor: ___
[  ] Project type: ___
[✅] Budget: ___
[  ] Timeline: ___
[  ] Core problem: ___
[  ] End users: ___
[  ] Current phase: ___
[  ] Success metrics: ___
[  ] Top risks: ___
[  ] Tech stack: ___
[  ] Methodology: ___
[  ] Regulatory: ___

STATUS: 4/14 slots filled (29%) — Tier 1 minimum: 8/14
NEXT QUESTION: "Siapa klien atau sponsor project ini?"
```

Setelah semua critical slots terisi, generate SSOT menggunakan CTX-SYNTH-01.
