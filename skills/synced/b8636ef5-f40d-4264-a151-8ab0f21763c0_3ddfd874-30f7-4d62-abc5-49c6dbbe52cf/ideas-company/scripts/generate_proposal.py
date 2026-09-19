#!/usr/bin/env python3
"""
IDEAS Proposal & Pitch Deck Generator

Generates two types of client-facing documents:
  Type A: Pitch Deck (--type pitch) — for enterprise/BUMN first engagement
  Type B: Full Proposal (--type proposal) — for government procurement

Usage:
    # Full Proposal (government)
    python3 generate_proposal.py --type proposal --client "POLRI" --sector government --services S1.1,S1.2,S1.4 --headcount 20 --months 6

    # Pitch Deck (enterprise)
    python3 generate_proposal.py --type pitch --client "PT Bank XYZ" --sector enterprise --services S1.1,S1.2 --working-days 44 --price 170000000

    # Pitch Deck (BUMN)
    python3 generate_proposal.py --type pitch --client "PT KAI" --sector bumn --services S1.1,S1.2,S2.4 --working-days 132 --price 575250000

    # Pitch Deck without pricing (international/exploratory)
    python3 generate_proposal.py --type pitch --client "Negeri Perlis" --sector international --services S1.1,S1.2,S2.3 --no-pricing

    # Legacy mode (backward compatible)
    python3 generate_proposal.py --client "Pemkab Kutai" --sector government --services S1.1,S1.2 --level 10
"""

# Cross-Skill Integration:
#   web-scraper: Collect evidence for proposals — SPBE scores via
#     page_scraper.py, competitor data via domain_crawler.py, portal
#     status via sitemap_discoverer.py.
#   dama-research: Reference KA deliverable templates from
#     dama-research/templates/deliverables/INDEX.md for standardized
#     proposal sections. Use maturity-calculator.py for assessment data.


import argparse
import json
import sys
from datetime import date

# --- Configuration ---
# NOTE: These constants can be externalized to a YAML/JSON file for easier management.
DEFAULT_OUTPUT_DIR = "."
import os as _os
PROPOSAL_TEMPLATE_PATH = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "templates", "proposal-template.md")


try:
    from estimate_service_cost import SERVICES, estimate_service_cost
    from pricing_engine import (
        get_daily_rate, RATE_CARD,
        calculate_gov_proposal_pricing, format_gov_pricing_table,
        calculate_lumpsum_pricing, format_lumpsum_card,
    )
except ImportError as e:
    print(f"Error: Missing required script files. Please ensure estimate_service_cost.py and pricing_engine.py are in the same directory.", file=sys.stderr)
    sys.exit(1)

# --- Service Catalog Metadata ---
# FUTURE IMPROVEMENT: This dictionary could be loaded from a separate JSON or YAML file
# to decouple it from the script logic, making it easier to update services.
SERVICE_DESCRIPTIONS = {
    "S1.1": {
        "name": "Data Strategy & Roadmap Development",
        "short": "Menetapkan arah strategis melalui asesmen kematangan dan perencanaan roadmap yang terukur.",
        "deliverables": [
            ("Laporan Asesmen Kematangan Data", "Evaluasi objektif posisi kematangan data organisasi berdasarkan DAMA-DMBOK", "PDF/PPTX"),
            ("Dokumen Strategi Data", "Visi, misi, tujuan strategis, dan inisiatif data", "PDF"),
            ("Roadmap Implementasi", "Peta jalan implementasi multi-tahun dengan prioritas", "PDF/Excel"),
            ("Blueprint Arsitektur Data", "Desain arsitektur data target-state", "PDF"),
        ],
    },
    "S1.2": {
        "name": "Data Governance & Compliance Framework",
        "short": "Merancang kerangka tata kelola data yang selaras dengan standar global dan regulasi Indonesia.",
        "deliverables": [
            ("Kerangka Tata Kelola Data", "Framework governance end-to-end berbasis DAMA-DMBOK", "PDF"),
            ("Dokumen Kebijakan Data", "Kebijakan, standar, dan prosedur pengelolaan data", "PDF"),
            ("Model RASCI", "Matriks kepemilikan dan stewardship data", "Excel"),
            ("Piagam Dewan Data", "Charter dan struktur Data Governance Council", "PDF"),
            ("AI Governance Framework", "Kerangka tata kelola AI berbasis NIST AI RMF dan ISO/IEC 42001 (opsional)", "PDF"),
        ],
    },
    "S1.3": {
        "name": "Data Maturity Assessment & Benchmarking",
        "short": "Evaluasi objektif untuk menilai kekuatan dan kelemahan kapabilitas data organisasi.",
        "deliverables": [
            ("Laporan Asesmen Kematangan", "Skor kematangan per 14 Knowledge Area DAMA", "PDF/PPTX"),
            ("Analisis Benchmark", "Perbandingan dengan standar industri dan regulasi", "PDF"),
            ("Roadmap Perbaikan", "Rekomendasi prioritas perbaikan dengan quick wins", "PDF"),
        ],
    },
    "S1.4": {
        "name": "Data Governance & Policy Framework Development",
        "short": "Menyusun SOP dan kerangka kebijakan yang mencakup seluruh siklus hidup data.",
        "deliverables": [
            ("Dokumen SOP Tata Kelola Data", "Prosedur operasional standar untuk seluruh siklus data", "PDF"),
            ("Kerangka Kebijakan Data", "Kebijakan data yang selaras dengan regulasi nasional", "PDF"),
            ("Panduan Klasifikasi Data", "Framework klasifikasi dan sensitivitas data", "PDF"),
            ("Framework Kualitas Data", "Aturan kualitas data dan SLA", "Excel"),
        ],
    },
    "S2.1": {
        "name": "Data-Centric Digital Product Development & UX Design",
        "short": "Mengembangkan produk digital yang menempatkan data dan pengalaman pengguna sebagai pusat desain.",
        "deliverables": [
            ("Product Requirements Document (PRD)", "Spesifikasi kebutuhan produk", "PDF"),
            ("UI/UX Design", "Desain antarmuka dan pengalaman pengguna", "Figma/PDF"),
            ("Aplikasi/Platform", "Produk digital yang siap digunakan", "Web App"),
            ("Dokumentasi Teknis", "Dokumentasi API dan arsitektur sistem", "PDF"),
        ],
    },
    "S2.2": {
        "name": "Core Data Platform & Modernization",
        "short": "Membangun pondasi data yang modern untuk lingkungan cloud, hybrid, maupun on-premise.",
        "deliverables": [
            ("Arsitektur Data Platform", "Desain arsitektur data warehouse/lake/mesh", "PDF"),
            ("Data Platform", "Platform data yang terbangun dan terkonfigurasi", "Infrastructure"),
            ("Pipeline Data", "ETL/ELT pipeline yang berjalan", "Code"),
            ("Dokumentasi Operasional", "Runbook dan monitoring guide", "PDF"),
        ],
    },
    "S2.3": {
        "name": "Government Data Portal Platform",
        "short": "Platform portal data pemerintah yang memenuhi mandat Satu Data Indonesia dan SPBE.",
        "deliverables": [
            ("Portal Data Terintegrasi", "Platform portal data dengan 7 komponen ekosistem", "Web App"),
            ("Katalog Data & Metadata", "Sistem katalog data yang terstandarisasi", "Web App"),
            ("Dashboard Eksekutif", "Dashboard real-time untuk pimpinan", "Web App"),
            ("Dokumentasi & Pelatihan", "Manual pengguna dan materi pelatihan", "PDF"),
        ],
    },
    "S2.4": {
        "name": "Enterprise Data Portal & Self-Service Analytics",
        "short": "Memberdayakan unit bisnis untuk melakukan analisis mandiri tanpa ketergantungan pada tim IT.",
        "deliverables": [
            ("Portal Data Enterprise", "Platform self-service analytics", "Web App"),
            ("Data Catalog", "Katalog data dengan metadata terkelola", "Web App"),
            ("Dokumentasi & Pelatihan", "Manual dan materi pelatihan pengguna", "PDF"),
        ],
    },
    "S2.5": {
        "name": "Secure & Trusted Data Exchange — API Gateway Platform",
        "short": "Membangun platform pertukaran data dan API yang aman dan terpercaya.",
        "deliverables": [
            ("API Gateway Platform", "Platform pertukaran data dan API terkelola", "Infrastructure"),
            ("Dokumentasi API", "Spesifikasi API dan panduan integrasi", "PDF/Swagger"),
            ("Security Assessment", "Laporan pengujian keamanan", "PDF"),
        ],
    },
    "S2.6": {
        "name": "Analytics and Visualization Solutions",
        "short": "Mengubah data kompleks menjadi narasi visual yang jelas dan mudah dipahami.",
        "deliverables": [
            ("Dashboard & Visualisasi", "Dashboard interaktif dan laporan visual", "Web App"),
            ("Laporan Analitik", "Insight dan rekomendasi berbasis data", "PDF/PPTX"),
        ],
    },
    "S3.1": {
        "name": "Data Governance Office (DGO) as a Service",
        "short": "Fungsi kantor tata kelola data sebagai layanan terkelola yang cost-effective.",
        "deliverables": [
            ("Setup DGO", "Pembentukan struktur dan proses DGO", "PDF"),
            ("Laporan Berkala", "Laporan kinerja tata kelola data bulanan", "PDF"),
            ("Pendampingan Operasional", "Dukungan operasional DGO selama kontrak", "Service"),
        ],
    },
    "S3.2": {
        "name": "Data Literacy & Culture Program",
        "short": "Meningkatkan literasi data di semua tingkatan organisasi.",
        "deliverables": [
            ("Kurikulum Pelatihan", "Program pelatihan multi-level", "PDF"),
            ("Materi Pelatihan", "Modul pelatihan per level (awareness, role-based)", "PDF/PPTX"),
            ("Laporan Evaluasi", "Hasil evaluasi dan rekomendasi tindak lanjut", "PDF"),
        ],
    },
    "S3.3": {
        "name": "Data Management Certified Training",
        "short": "Pelatihan dan sertifikasi resmi berbasis DAMA-DMBOK dan BNSP.",
        "deliverables": [
            ("Materi Pelatihan", "Modul pelatihan CDMP/BNSP", "PDF/PPTX"),
            ("Pelaksanaan Pelatihan", "Sesi pelatihan tatap muka/virtual", "Service"),
            ("Sertifikasi", "Pendampingan ujian sertifikasi", "Service"),
        ],
    },
    "S1.5": {
        "name": "Data Asset Valuation & Monetization Advisory",
        "short": "Menilai dan memonetisasi aset data menggunakan framework Infonomics dan standar internasional.",
        "deliverables": [
            ("Inventaris Aset Data", "Katalog aset data terklasifikasi per domain bisnis", "Excel"),
            ("Laporan Valuasi Data", "Penilaian aset data menggunakan 6 model Infonomics (IVA, BVA, PVA, CVA, EVA, MVA)", "PDF/PPTX"),
            ("Data Balance Sheet", "Neraca aset data untuk pelaporan eksekutif", "Excel/PDF"),
            ("Strategi Monetisasi", "Roadmap monetisasi data dengan model pendapatan", "PDF"),
            ("Framework Governance Valuasi", "Proses review dan update valuasi berkala", "PDF"),
        ],
    },
    "S3.4": {
        "name": "Knowledge Transfer & Thought Leadership (Narasumber)",
        "short": "Transfer pengetahuan dan pendampingan monetisasi data untuk keberlanjutan organisasi.",
        "deliverables": [
            ("Kurikulum Knowledge Transfer", "Program transfer pengetahuan terstruktur", "PDF"),
            ("Data Monetization Playbook", "Panduan monetisasi data dengan use case library", "PDF"),
            ("Workshop Report", "Hasil workshop valuasi data dan design thinking", "PDF/PPTX"),
            ("Self-Service Analytics Guide", "Panduan analitik mandiri untuk keberlanjutan", "PDF"),
            ("Laporan Evaluasi Kapabilitas", "Asesmen kematangan pasca-transfer", "PDF"),
        ],
    },
}

SECTOR_CONTEXT = {
    "government": {
        "label": "Pemerintah",
        "regulations": "Perpres 39/2019 (Satu Data Indonesia), UU 27/2022 (PDP), Perpres 132/2022 (SPBE)",
        "challenges": [
            "Data tersebar di berbagai OPD/Satker tanpa standar yang seragam",
            "Portal data belum memenuhi mandat Satu Data Indonesia",
            "Rendahnya indeks SPBE pada domain manajemen data",
            "Kebutuhan kepatuhan terhadap UU Perlindungan Data Pribadi",
        ],
        "pain_points": [
            "Data Silos — data tersebar tanpa integrasi",
            "Inconsistent Data — format dan standar berbeda antar unit",
            "No Metadata Standards — tidak ada standar metadata bersama",
            "Poor Data Quality — kualitas data rendah dan tidak tervalidasi",
            "Lack of Data Governance — tidak ada kerangka tata kelola",
            "Unclear Ownership — tidak jelas siapa penanggung jawab data",
        ],
    },
    "enterprise": {
        "label": "Enterprise",
        "regulations": "UU 27/2022 (PDP), ISO/IEC 27001, COBIT 2019",
        "challenges": [
            "Data silo antar departemen menghambat pengambilan keputusan",
            "Kurangnya standar kualitas data yang konsisten",
            "Kebutuhan kepatuhan terhadap UU Perlindungan Data Pribadi",
            "Belum optimalnya pemanfaatan data untuk keunggulan kompetitif",
        ],
        "pain_points": [
            "Fragmented Truth — setiap tim punya versi data sendiri",
            "Snowball Effect — masalah kecil terakumulasi menjadi krisis",
            "Unclear Ownership — tidak jelas siapa bertanggung jawab atas data apa",
        ],
    },
    "bumn": {
        "label": "BUMN",
        "regulations": "UU 27/2022 (PDP), Permen BUMN, ISO/IEC 27001",
        "challenges": [
            "Pengelolaan data masih terpisah-pisah dan tidak terdokumentasi",
            "Belum sepenuhnya selaras dengan proses bisnis inti",
            "Ketergantungan tinggi pada individu tertentu",
            "Kesulitan dalam memenuhi tuntutan regulasi dan audit",
        ],
        "pain_points": [
            "Inkonsistensi dan rendahnya kualitas data",
            "Ketergantungan tinggi pada individu tertentu",
            "Kesulitan dalam memenuhi tuntutan regulasi dan audit",
            "Terbatasnya pemanfaatan data untuk kebutuhan strategis",
        ],
    },
    "international": {
        "label": "Pemerintah Internasional",
        "regulations": "GDPR, ISO/IEC 38505, DAMA-DMBOK",
        "challenges": [
            "Data silos across government agencies",
            "No unified metadata standards",
            "Limited data sharing and interoperability",
            "Need for comprehensive digital transformation",
        ],
        "pain_points": [
            "Data Silos", "Inconsistent Data", "No Metadata Standards",
            "Poor Data Quality", "Lack of Data Governance", "Limited Data Sharing",
            "No Data Catalog", "Unclear Ownership", "Manual Processes",
            "No Data Lineage", "Compliance Risks", "Limited Analytics",
        ],
    },
    "academia": {
        "label": "Akademik",
        "regulations": "Perpres 39/2019 (Satu Data Indonesia)",
        "challenges": [
            "Pengelolaan data penelitian yang belum terstandarisasi",
            "Kurangnya literasi data di kalangan civitas akademika",
            "Kebutuhan sertifikasi kompetensi data management",
        ],
        "pain_points": [
            "Data penelitian tidak terstandarisasi",
            "Kurangnya literasi data",
            "Tidak ada framework governance akademik",
        ],
    },
}

PILLAR_NAMES = {1: "Advisory & Governance", 2: "Platform & Solution Implementation", 3: "Empowerment & Managed Services"}

# --- Government team composition patterns ---
GOV_TEAM_FULL = [
    ("Project Manager", 1, "Perencanaan keseluruhan, eksekusi, monitoring, dan SPOC utama proyek"),
    ("Project Officer", 1, "Administrasi proyek, penjadwalan, pelaporan, dan logistik"),
    ("Business Analyst", 4, "Analisis proses bisnis as-is, perancangan workflow to-be"),
    ("Data Architect", 4, "Arsitektur database, integrasi skema, spesifikasi teknis"),
    ("Data Governance Analyst", 4, "Framework governance, RASCI, standar, kepatuhan regulasi"),
    ("Data Quality Analyst", 4, "Prosedur kualitas data, validasi, pembersihan, metrik"),
    ("Technical Writer", 2, "Penulisan dokumen, formatting, quality assurance"),
]

GOV_TEAM_PARTIAL = [
    ("Project Manager", 1, "Perencanaan keseluruhan, eksekusi, monitoring, dan SPOC utama proyek"),
    ("Project Officer", 1, "Administrasi proyek, penjadwalan, pelaporan, dan logistik"),
    ("Business Analyst", 2, "Analisis proses bisnis as-is, perancangan workflow to-be"),
    ("Data Governance Analyst", 1, "Framework governance, RASCI, standar, kepatuhan regulasi"),
    ("Technical Writer", 1, "Penulisan dokumen, formatting, quality assurance"),
]


def fmt(val):
    # FUTURE IMPROVEMENT: This could be enhanced to support multiple currencies (e.g., USD, EUR)
    # based on an additional argument or configuration setting.
    if not isinstance(val, (int, float)):
        return val
    return "Rp {:,.0f}".format(val)


# ============================================================
# TYPE A: PITCH DECK GENERATOR
# ============================================================

def generate_pitch(client, sector, service_ids, working_days, price, include_tax, no_pricing, scope_label, output_path):
    """Generate a pitch deck in Markdown format."""
    ctx = SECTOR_CONTEXT.get(sector, SECTOR_CONTEXT["enterprise"])
    today = date.today().strftime("%d %B %Y")

    # Collect deliverables
    all_deliverables = []
    for sid in service_ids:
        if sid in SERVICE_DESCRIPTIONS:
            for d in SERVICE_DESCRIPTIONS[sid]["deliverables"]:
                all_deliverables.append(d)

    service_names = [SERVICE_DESCRIPTIONS.get(sid, {}).get("name", sid) for sid in service_ids]
    if len(service_names) == 1:
        title = service_names[0]
    elif len(service_names) == 2:
        title = " dan ".join(service_names)
    else:
        title = f"{service_names[0]} dan {len(service_names)-1} Layanan Lainnya"

    lines = []

    # Cover
    lines.append(f"# {title}")
    lines.append(f"")
    lines.append(f"**Menata Fondasi Data untuk Keputusan Strategis**")
    lines.append(f"")
    lines.append(f"Disiapkan untuk: **{client}**")
    lines.append(f"")
    lines.append(f"**Tanggal**: {today}")
    lines.append(f"")
    lines.append(f"**Versi**: 1.0")
    lines.append(f"")
    lines.append(f"Dokumen ini adalah hak milik intelektual dari PT Indonesian Data Ecosystem (IDEAS).")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # Prakata
    lines.append(f"## PRAKATA")
    lines.append(f"")
    lines.append(f"### Data adalah Aset Pendorong Inovasi dan Keunggulan yang Kompetitif")
    lines.append(f"")
    lines.append(f"Kita hidup di persimpangan jalan paling transformatif dalam sejarah bisnis modern. "
                  f"Era di mana intuisi dan pengalaman tidak lagi cukup untuk memenangkan persaingan. "
                  f"Kita telah memasuki era digital, di mana mata uang baru yang paling berharga "
                  f"bukanlah mesin atau modal, melainkan data.")
    lines.append(f"")
    lines.append(f"Saya mengamati sebuah fakta yang tak terbantahkan: Perusahaan yang unggul bukanlah "
                  f"mereka yang memiliki data paling banyak, melainkan mereka yang paling cerdas dalam "
                  f"memanfaatkannya. Perjalanan mengubah data menjadi nilai adalah sebuah maraton, "
                  f"bukan lari cepat.")
    lines.append(f"")
    lines.append(f"**Rizki Rusdiwijaya**")
    lines.append(f"Chief Executive Officer, PT Indonesian Data Ecosystem (IDEAS)")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # Quote
    lines.append(f"> *Good data, good decision* — **\'keputusan terbaik lahir dari pemahaman yang utuh\'**")
    lines.append(f">")
    lines.append(f"> IDEAS tumbuh dari prinsip bahwa data bukan sekadar angka, tapi realita yang bisa "
                  f"menuntun arah perubahan.")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # Agenda
    lines.append(f"## Agenda")
    lines.append(f"")
    lines.append(f"1. Menjadikan Data sebagai Aset {client}")
    lines.append(f"2. Tujuan Utama")
    lines.append(f"3. Deliverable & Outcomes")
    lines.append(f"4. Langkah Selanjutnya")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # Section 01: Latar Belakang
    lines.append(f"## 01 LATAR BELAKANG")
    lines.append(f"")
    lines.append(f"### Menjadikan Data sebagai Aset")
    lines.append(f"")
    lines.append(f"Banyak organisasi, pengelolaan data masih bersifat terpisah-pisah, tidak terdokumentasi "
                  f"dengan baik, serta belum sepenuhnya selaras dengan proses bisnis inti.")
    lines.append(f"")
    lines.append(f"Kondisi tersebut berpotensi menimbulkan berbagai risiko, antara lain:")
    lines.append(f"")
    for pp in ctx.get("pain_points", []):
        lines.append(f"- {pp}")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # Section 02: Tujuan Utama
    lines.append(f"## 02 TUJUAN UTAMA")
    lines.append(f"")
    lines.append(f"### Arah Gerak Transformasi")
    lines.append(f"")
    svc_descriptions = [SERVICE_DESCRIPTIONS.get(sid, {}).get("short", "") for sid in service_ids if sid in SERVICE_DESCRIPTIONS]
    if svc_descriptions:
        lines.append(f"*{ ' '.join(svc_descriptions[:2])}*")
    lines.append(f"")
    lines.append(f"**Pentahapan:**")
    lines.append(f"")
    lines.append(f"1. Menetapkan arah strategis pengelolaan data organisasi")
    lines.append(f"2. Menilai tingkat kematangan kapabilitas data secara objektif")
    lines.append(f"3. Mengidentifikasi kesenjangan antara kondisi saat ini dan kondisi target")
    lines.append(f"4. Menyusun kerangka tata kelola data yang patuh terhadap standar global dan regulasi nasional")
    lines.append(f"5. Menghasilkan dokumen kebijakan dan SOP pengelolaan data yang siap diterapkan")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # Section 03: Deliverable & Outcomes
    lines.append(f"## 03 DELIVERABLE & OUTCOMES")
    lines.append(f"")
    lines.append(f"### Key Milestones")
    lines.append(f"")
    milestone_num = 1
    for sid in service_ids:
        if sid in SERVICE_DESCRIPTIONS:
            lines.append(f"{milestone_num}. {SERVICE_DESCRIPTIONS[sid]['name']}")
            milestone_num += 1
    lines.append(f"")
    lines.append(f"### Deliverables")
    lines.append(f"")
    for i, (name, desc, fmt_str) in enumerate(all_deliverables, 1):
        lines.append(f"{i}. **{name}** — {desc}")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # Pricing (optional)
    if not no_pricing and price is not None:
        lines.append(f"## Investasi")
        lines.append(f"")
        lines.append(f"### {fmt(price)}")
        lines.append(f"")
        tax_status = "Sudah termasuk pajak" if include_tax else "Belum termasuk pajak"
        lines.append(f"*({tax_status})*")
        lines.append(f"")
        if working_days:
            lines.append(f"Estimasi durasi: **{working_days} hari kerja**.")
        lines.append(f"")
        lines.append(f"---")
        lines.append(f"")

    # Section 04: Langkah Selanjutnya
    lines.append(f"## 04 LANGKAH SELANJUTNYA")
    lines.append(f"")
    lines.append(f"1. Diskusi pendalaman kebutuhan dan ruang lingkup")
    lines.append(f"2. Penyesuaian proposal teknis dan komersial")
    lines.append(f"3. Penandatanganan kontrak dan kick-off proyek")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # Tentang IDEAS
    lines.append(f"## Tentang IDEAS")
    lines.append(f"")
    lines.append(f"**PT Indonesian Data Ecosystem (IDEAS)** adalah firma penasihat dan penyedia solusi data " 
                  f"terkemuka di Indonesia. Kami membantu organisasi menavigasi kompleksitas " 
                  f"transformasi digital dengan menempatkan data sebagai fondasi pengambilan keputusan.")
    lines.append(f"")
    lines.append(f"**Misi kami** adalah memberdayakan organisasi untuk membuka nilai penuh dari aset data mereka.")
    lines.append(f"")
    lines.append(f"**Kontak:**")
    lines.append(f"- **Website:** https://data-ecosystem.id")
    lines.append(f"- **Email:** contact@data-ecosystem.id")
    lines.append(f"")

    # Save to file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"Pitch deck generated successfully at {output_path}")
    except IOError as e:
        print(f"Error writing to file {output_path}: {e}", file=sys.stderr)
        sys.exit(1)


# ============================================================
# TYPE B: PROPOSAL GENERATOR (GOVERNMENT)
# ============================================================

def generate_proposal(client, sector, service_ids, headcount, months, output_path):
    """Generate a fully-enriched proposal in Markdown format for government clients.

    Fills ALL 34 template placeholders with context-aware content derived from:
    - SERVICE_DESCRIPTIONS catalog (deliverables, descriptions)
    - SECTOR_CONTEXT (challenges, pain points, regulations)
    - estimate_service_cost (man-days, task breakdown)
    - pricing_engine (personnel, operational, risk costs)
    """
    ctx = SECTOR_CONTEXT.get(sector, SECTOR_CONTEXT["government"])
    today = date.today().strftime("%d %B %Y")

    # Load template
    try:
        with open(PROPOSAL_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Error: Proposal template not found at {PROPOSAL_TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading template file: {e}", file=sys.stderr)
        sys.exit(1)

    # Collect service metadata
    svc_names = [SERVICE_DESCRIPTIONS[s]["name"] for s in service_ids if s in SERVICE_DESCRIPTIONS]
    pillar_ids = sorted(set(int(s.split('.')[0][1]) for s in service_ids))
    pillar_labels = [PILLAR_NAMES.get(p, f"Pilar {p}") for p in pillar_ids]

    # --- ENRICHMENT: Compute costs via pricing engine ---
    pricing_data = calculate_gov_proposal_pricing(headcount, months)
    personnel_cost = pricing_data.get("a_personnel", 0)
    operational_cost = pricing_data.get("b_operational", 0)
    risk_cost = pricing_data.get("c_risk_management", 0)
    total_cost = personnel_cost + operational_cost + risk_cost
    vat_cost = total_cost * 0.11
    grand_total = total_cost + vat_cost

    # --- ENRICHMENT: Compute man-days per service ---
    svc_mandays = {}
    svc_tasks = {}
    for sid in service_ids:
        try:
            est = estimate_service_cost(sid, 10)
            svc_mandays[sid] = est.get("total_man_days", 0)
            svc_tasks[sid] = est.get("tasks", [])
        except Exception:
            svc_mandays[sid] = 0
            svc_tasks[sid] = []
    total_mandays = sum(svc_mandays.values())

    # ================================================================
    # PLACEHOLDER REPLACEMENTS (all 34)
    # ================================================================

    # {{PROJECT_TITLE}}
    if len(svc_names) <= 2:
        scope_short = " dan ".join(svc_names)
    else:
        scope_short = f"{svc_names[0]}, {svc_names[1]}, dan {len(svc_names)-2} Layanan Lainnya"
    project_title = f"Konsultansi {scope_short} untuk {client}"
    template = template.replace("{{PROJECT_TITLE}}", project_title)

    # {{PROJECT_TAGLINE}}
    tagline = " | ".join(svc_names[:4])
    template = template.replace("{{PROJECT_TAGLINE}}", f"Disiapkan oleh PT Indonesian Data Ecosystem (IDEAS) — {today}")

    # {{CLIENT_NAME}}
    template = template.replace("{{CLIENT_NAME}}", client)

    # {{DATE}}
    template = template.replace("{{DATE}}", today)

    # {{PROJECT_CONTEXT}}
    challenges_narrative = ctx.get("challenges", [])
    pain_points = ctx.get("pain_points", [])
    context_lines = []
    context_lines.append(f"{client} menghadapi tantangan transformasi digital yang membutuhkan pengelolaan data secara "
                         f"terstruktur, terstandar, dan berkelanjutan. Beberapa kondisi yang mendorong kebutuhan ini:")
    context_lines.append("")
    for c in challenges_narrative:
        context_lines.append(f"- {c}")
    context_lines.append("")
    context_lines.append(f"Proyek ini dirancang untuk menjawab tantangan tersebut melalui {len(service_ids)} layanan "
                         f"terintegrasi yang mencakup {', '.join(pillar_labels)}, dengan total estimasi "
                         f"**{total_mandays:.0f} man-days** selama **{months} bulan**.")
    template = template.replace("{{PROJECT_CONTEXT}}", "\n".join(context_lines))

    # {{SMART_*}} — 5 SMART objectives
    template = template.replace("{{SMART_SPECIFIC}}",
        f"Melaksanakan {len(service_ids)} layanan konsultansi data ({', '.join(service_ids)}) "
        f"untuk {client} mencakup {', '.join(svc_names[:3])}{'.' if len(svc_names)<=3 else f', dan {len(svc_names)-3} layanan lainnya.'}")
    total_deliverables = sum(len(SERVICE_DESCRIPTIONS.get(s, {}).get('deliverables', [])) for s in service_ids)
    template = template.replace("{{SMART_MEASURABLE}}",
        f"Menghasilkan {total_deliverables} deliverables terukur "
        f"dengan total {total_mandays:.0f} man-days effort.")
    template = template.replace("{{SMART_ACHIEVABLE}}",
        f"Dilaksanakan oleh tim {headcount} tenaga ahli berpengalaman dengan metodologi DAMA-DMBOK, PMBOK, dan Agile.")
    template = template.replace("{{SMART_RELEVANT}}",
        f"Selaras dengan {ctx.get('regulations', 'regulasi yang berlaku')} dan kebutuhan transformasi digital {client}.")
    template = template.replace("{{SMART_TIMEBOUND}}",
        f"Diselesaikan dalam {months} bulan sejak tanggal kick-off proyek.")

    # {{INSCOPE_*}} — 5 in-scope items from services
    inscope_items = []
    for sid in service_ids:
        svc = SERVICE_DESCRIPTIONS.get(sid)
        if svc:
            inscope_items.append(f"**{svc['name']}** — {svc['short']}")
    # Pad to 5
    while len(inscope_items) < 5:
        inscope_items.append("*(Disesuaikan berdasarkan hasil kick-off dan kebutuhan detail)*")
    for i in range(5):
        template = template.replace(f"{{{{INSCOPE_{i+1}}}}}", inscope_items[i])

    # {{OUTSCOPE_*}} — 3 out-of-scope items
    all_sids = set(SERVICE_DESCRIPTIONS.keys())
    selected_sids = set(service_ids)
    excluded_sids = sorted(all_sids - selected_sids)
    outscope_items = []
    if excluded_sids:
        for sid in excluded_sids[:2]:
            svc = SERVICE_DESCRIPTIONS.get(sid)
            if svc:
                outscope_items.append(f"Layanan {sid}: {svc['name']}")
    outscope_items.append("Pengadaan infrastruktur hardware dan lisensi software pihak ketiga")
    while len(outscope_items) < 3:
        outscope_items.append("Operasional dan pemeliharaan sistem pasca-serah terima")
    for i in range(3):
        template = template.replace(f"{{{{OUTSCOPE_{i+1}}}}}", outscope_items[i])

    # {{DELIVERABLES_TABLE}} — formatted markdown table
    deliv_lines = ["| No | Layanan | Deliverable | Format |", "| :---: | :--- | :--- | :---: |"]
    deliv_no = 1
    for sid in service_ids:
        svc = SERVICE_DESCRIPTIONS.get(sid)
        if svc:
            for name, desc, fmt_str in svc["deliverables"]:
                deliv_lines.append(f"| {deliv_no} | {svc['name']} | **{name}** — {desc} | {fmt_str} |")
                deliv_no += 1
    template = template.replace("{{DELIVERABLES_TABLE}}", "\n".join(deliv_lines))

    # {{MONTHLY_ACTIVITIES}} — month-by-month plan
    activity_lines = ["| Bulan | Fase | Aktivitas Utama | Layanan |", "| :---: | :--- | :--- | :--- |"]
    months_per_svc = max(1, months // len(service_ids)) if service_ids else months
    current_month = 1
    for idx, sid in enumerate(service_ids):
        svc = SERVICE_DESCRIPTIONS.get(sid, {})
        svc_name = svc.get("name", sid)
        start_m = current_month
        end_m = min(current_month + months_per_svc - 1, months)
        if idx == len(service_ids) - 1:
            end_m = months  # last service takes remaining months
        month_range = f"{start_m}" if start_m == end_m else f"{start_m}-{end_m}"

        # Generate activities from tasks
        tasks = svc_tasks.get(sid, [])
        task_names = [t.get("description", t.get("task_id", "Task"))[:60] for t in tasks[:3]]
        activities = "; ".join(task_names) if task_names else svc.get("short", "Pelaksanaan layanan")

        phase_names = ["Inisiasi & Asesmen", "Analisis & Desain", "Implementasi", "Evaluasi & Serah Terima"]
        phase = phase_names[min(idx, len(phase_names)-1)]

        activity_lines.append(f"| {month_range} | {phase} | {activities} | {sid}: {svc_name} |")
        current_month = end_m + 1
    template = template.replace("{{MONTHLY_ACTIVITIES}}", "\n".join(activity_lines))

    # {{TIMELINE_VISUAL}}
    timeline_note = (f"*Timeline detail dalam format Gantt Chart tersedia sebagai lampiran terpisah. "
                     f"Gunakan `generate_timeline.py --services {','.join(service_ids)} --start [TANGGAL]` "
                     f"untuk menghasilkan diagram interaktif.*\n\n"
                     f"**Estimasi Durasi Total:** {months} bulan ({total_mandays:.0f} man-days)")
    template = template.replace("{{TIMELINE_VISUAL}}", timeline_note)

    # {{TEAM_TABLE}} — formatted team table
    team = GOV_TEAM_FULL if headcount > 10 else GOV_TEAM_PARTIAL
    team_lines = []
    for i, (role, count, desc) in enumerate(team, 1):
        team_lines.append(f"| {i} | {role} ({count} orang) | {desc} |")
    template = template.replace("{{TEAM_TABLE}}", "\n".join(team_lines))

    # {{HEADCOUNT}} {{MONTHS}}
    template = template.replace("{{HEADCOUNT}}", str(headcount))
    template = template.replace("{{MONTHS}}", str(months))

    # {{PERSONNEL_COST}} {{OPERATIONAL_COST}} {{RISK_COST}} {{TOTAL_COST}} {{VAT_COST}} {{GRAND_TOTAL_COST}}
    template = template.replace("{{PERSONNEL_COST}}", f"{personnel_cost:,.0f}")
    template = template.replace("{{OPERATIONAL_COST}}", f"{operational_cost:,.0f}")
    template = template.replace("{{RISK_COST}}", f"{risk_cost:,.0f}")
    template = template.replace("{{TOTAL_COST}}", f"{total_cost:,.0f}")
    template = template.replace("{{VAT_COST}}", f"{vat_cost:,.0f}")
    template = template.replace("{{GRAND_TOTAL_COST}}", f"{grand_total:,.0f}")

    # {{REGULATION_1-3}} {{RELEVANCE_1-3}} — compliance table
    reg_text = ctx.get("regulations", "")
    regs = [r.strip() for r in reg_text.split(",") if r.strip()]
    reg_relevance = {
        "Perpres 39/2019 (Satu Data Indonesia)": "Mandat portal data terbuka dan standar data nasional",
        "UU 27/2022 (PDP)": "Kepatuhan perlindungan data pribadi dalam pengelolaan data",
        "Perpres 132/2022 (SPBE)": "Peningkatan indeks SPBE melalui manajemen data terstruktur",
        "ISO/IEC 27001": "Standar keamanan informasi untuk perlindungan data",
        "COBIT 2019": "Tata kelola TI enterprise untuk pengelolaan data",
        "GDPR": "Kepatuhan perlindungan data pribadi standar Eropa",
        "ISO/IEC 38505": "Standar tata kelola data internasional",
        "DAMA-DMBOK": "Framework pengelolaan data sebagai basis metodologi",
        "Permen BUMN": "Kepatuhan tata kelola data BUMN",
    }
    while len(regs) < 3:
        regs.append("DAMA-DMBOK")
    for i in range(3):
        reg = regs[i] if i < len(regs) else "DAMA-DMBOK"
        relevance = reg_relevance.get(reg, f"Standar acuan untuk pelaksanaan proyek {', '.join(svc_names[:2])}")
        template = template.replace(f"{{{{REGULATION_{i+1}}}}}", reg)
        template = template.replace(f"{{{{RELEVANCE_{i+1}}}}}", relevance)

    # {{CAPACITY_BUILDING_PLAN}}
    cb_lines = ["| Program | Target Peserta | Durasi | Output |", "| :--- | :--- | :--- | :--- |"]
    cb_lines.append(f"| Workshop Tata Kelola Data | Pimpinan & Manajer Data | 2 hari | Pemahaman framework governance |")
    cb_lines.append(f"| Pelatihan Teknis Operasional | Tim Teknis & Data Steward | 3 hari | Kemampuan operasional platform |")
    cb_lines.append(f"| Pendampingan Post Go-Live | Seluruh Tim Proyek | 2 minggu | Kemandirian operasional |")
    # Add S3.x specific items if selected
    for sid in service_ids:
        if sid.startswith("S3."):
            svc = SERVICE_DESCRIPTIONS.get(sid, {})
            cb_lines.append(f"| {svc.get('name', sid)} | Seluruh organisasi | Sesuai kebutuhan | {svc.get('short', 'Transfer pengetahuan')} |")
    template = template.replace("{{CAPACITY_BUILDING_PLAN}}", "\n".join(cb_lines))

    # --- Also replace old-style placeholders for backward compat ---
    template = template.replace("{{SECTOR_CHALLENGES}}", "\n".join(f"- {c}" for c in challenges_narrative))
    template = template.replace("{{REGULATIONS}}", reg_text)
    template = template.replace("{{SERVICES_SUMMARY}}", "\n".join(
        f"**{SERVICE_DESCRIPTIONS[s]['name']}** — *{SERVICE_DESCRIPTIONS[s]['short']}*"
        for s in service_ids if s in SERVICE_DESCRIPTIONS))
    template = template.replace("{{DELIVERABLES_LIST}}", "")  # replaced by DELIVERABLES_TABLE
    template = template.replace("{{TEAM_COMPOSITION}}", "")  # replaced by TEAM_TABLE
    template = template.replace("{{TIMELINE}}", f"{months} bulan")
    template = template.replace("{{PRICING_TABLE}}", "")  # replaced by cost table in § 6
    template = template.replace("{{TOTAL_PRICE}}", f"Rp {grand_total:,.0f}")

    # --- POST-PROCESSING: Clean output for document generation ---
    import re as _re
    cleaned_lines = []
    for line in template.split("\n"):
        stripped = line.strip()
        # Remove template instruction lines (italic guidance text)
        if _re.match(r'^\*[A-Z].*\*$', stripped):
            continue
        # Remove script/file references
        if '`generate_' in stripped or '`calculate_' in stripped or '`references/' in stripped:
            # Keep the line but strip the backtick reference
            cleaned = _re.sub(r'\s*`[a-z_/\-]+\.(py|md|csv)`', '', stripped)
            cleaned = _re.sub(r'Tabel ini akan diisi oleh skrip.*berdasarkan layanan yang dipilih\.', '', cleaned)
            cleaned = _re.sub(r'Gambar ini dihasilkan oleh skrip.*\.', '', cleaned)
            cleaned = _re.sub(r'Untuk detail setiap deliverable.*\.', 
                             'Untuk detail setiap deliverable, silakan merujuk ke dokumen terpisah.', cleaned)
            cleaned = _re.sub(r'Gunakan.*untuk menghasilkan diagram interaktif\.\*', '', cleaned)
            if cleaned.strip():
                cleaned_lines.append(cleaned)
        else:
            cleaned_lines.append(line)
    template = "\n".join(cleaned_lines)

    # Save to file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"Proposal generated successfully at {output_path}")
    except IOError as e:
        print(f"Error writing to file {output_path}: {e}", file=sys.stderr)
        sys.exit(1)


# ============================================================
# STRUCTURED DATA COLLECTOR (for PPTX/DOCX direct build)
# ============================================================

def _collect_proposal_data(client, sector, service_ids, headcount, months):
    """Collect all proposal data into a structured dict for document builders."""
    ctx = SECTOR_CONTEXT.get(sector, SECTOR_CONTEXT["government"])
    today = date.today().strftime("%d %B %Y")

    svc_names = [SERVICE_DESCRIPTIONS[s]["name"] for s in service_ids if s in SERVICE_DESCRIPTIONS]
    if len(svc_names) <= 2:
        scope_short = " dan ".join(svc_names)
    else:
        scope_short = f"{svc_names[0]}, {svc_names[1]}, dan {len(svc_names)-2} Layanan Lainnya"
    project_title = f"Konsultansi {scope_short} untuk {client}"

    # Costs
    pricing_data = calculate_gov_proposal_pricing(headcount, months)
    personnel = pricing_data.get("a_personnel", 0)
    operational = pricing_data.get("b_operational", 0)
    risk = pricing_data.get("c_risk_management", 0)
    total = personnel + operational + risk
    vat = total * 0.11

    # Man-days per service
    svc_tasks = {}
    for sid in service_ids:
        try:
            est = estimate_service_cost(sid, 10)
            svc_tasks[sid] = est.get("tasks", [])
        except Exception:
            svc_tasks[sid] = []
    total_mandays = sum(sum(t.get("adjusted_man_days", 0) for t in tasks) for tasks in svc_tasks.values())

    # Deliverables
    deliverables = []
    for sid in service_ids:
        svc = SERVICE_DESCRIPTIONS.get(sid, {})
        for name, desc, fmt in svc.get("deliverables", []):
            deliverables.append({"service": svc.get("name", sid), "name": name, "description": desc, "format": fmt})

    # In-scope / out-scope
    inscope = [{"name": SERVICE_DESCRIPTIONS[s]["name"], "desc": SERVICE_DESCRIPTIONS[s]["short"]}
               for s in service_ids if s in SERVICE_DESCRIPTIONS]
    all_sids = set(SERVICE_DESCRIPTIONS.keys())
    excluded = sorted(all_sids - set(service_ids))
    outscope = [f"Layanan {s}: {SERVICE_DESCRIPTIONS[s]['name']}" for s in excluded[:2]]
    outscope.append("Pengadaan infrastruktur hardware dan lisensi software pihak ketiga")

    # Monthly activities
    months_per_svc = max(1, months // len(service_ids)) if service_ids else months
    activities = []
    cur_m = 1
    phase_names = ["Inisiasi & Asesmen", "Analisis & Desain", "Implementasi", "Evaluasi & Serah Terima"]
    for idx, sid in enumerate(service_ids):
        svc = SERVICE_DESCRIPTIONS.get(sid, {})
        start_m, end_m = cur_m, min(cur_m + months_per_svc - 1, months)
        if idx == len(service_ids) - 1: end_m = months
        tasks = svc_tasks.get(sid, [])
        task_names = [t.get("description", "")[:55] for t in tasks[:3]]
        activities.append({
            "month": f"{start_m}" if start_m == end_m else f"{start_m}-{end_m}",
            "phase": phase_names[min(idx, len(phase_names) - 1)],
            "service_id": sid,
            "activities": "; ".join(task_names) if task_names else svc.get("short", ""),
        })
        cur_m = end_m + 1

    # Team
    team_raw = GOV_TEAM_FULL if headcount > 10 else GOV_TEAM_PARTIAL
    team = [{"role": r, "count": c, "desc": d} for r, c, d in team_raw]

    # SMART
    total_deliverables = sum(len(SERVICE_DESCRIPTIONS.get(s, {}).get("deliverables", [])) for s in service_ids)
    smart = {
        "specific": f"Melaksanakan {len(service_ids)} layanan konsultansi data untuk {client} "
                     f"mencakup {', '.join(svc_names[:3])}.",
        "measurable": f"Menghasilkan {total_deliverables} deliverables terukur dengan total "
                      f"{total_mandays:.0f} man-days effort.",
        "achievable": f"Dilaksanakan oleh tim {headcount} tenaga ahli berpengalaman dengan "
                      f"metodologi DAMA-DMBOK, PMBOK, dan Agile.",
        "relevant": f"Selaras dengan {ctx.get('regulations', '')} dan kebutuhan transformasi digital {client}.",
        "timebound": f"Diselesaikan dalam {months} bulan sejak tanggal kick-off proyek.",
    }

    # Regulations
    reg_text = ctx.get("regulations", "")
    regs = [r.strip() for r in reg_text.split(",") if r.strip()]
    reg_map = {
        "Perpres 39/2019 (Satu Data Indonesia)": "Mandat portal data terbuka dan standar data nasional",
        "UU 27/2022 (PDP)": "Kepatuhan perlindungan data pribadi",
        "Perpres 132/2022 (SPBE)": "Peningkatan indeks SPBE melalui manajemen data",
        "ISO/IEC 27001": "Standar keamanan informasi",
        "DAMA-DMBOK": "Framework pengelolaan data sebagai basis metodologi",
        "Permen BUMN": "Kepatuhan tata kelola data BUMN",
        "GDPR": "Kepatuhan data pribadi standar Eropa",
    }
    while len(regs) < 3: regs.append("DAMA-DMBOK")
    regulations = [{"name": r, "relevance": reg_map.get(r, "Standar acuan pelaksanaan proyek")} for r in regs[:3]]

    # Capacity building
    cb = [
        {"program": "Workshop Tata Kelola Data", "target": "Pimpinan & Manajer", "duration": "2 hari", "output": "Pemahaman framework"},
        {"program": "Pelatihan Teknis Operasional", "target": "Tim Teknis & Data Steward", "duration": "3 hari", "output": "Kemampuan operasional"},
        {"program": "Pendampingan Post Go-Live", "target": "Seluruh Tim", "duration": "2 minggu", "output": "Kemandirian operasional"},
    ]

    return {
        "project_title": project_title,
        "client": client,
        "sector": sector,
        "date": today,
        "headcount": headcount,
        "months": months,
        "total_services": len(service_ids),
        "total_mandays": total_mandays,
        "challenges": ctx.get("challenges", []),
        "smart": smart,
        "inscope": inscope,
        "outscope": outscope,
        "deliverables": deliverables,
        "monthly_activities": activities,
        "team": team,
        "costs": {"personnel": personnel, "operational": operational, "risk": risk,
                  "total": total, "vat": vat, "grand_total": total + vat},
        "regulations": regulations,
        "capacity_building": cb,
    }


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    """Main function to parse arguments and run the generator."""
    parser = argparse.ArgumentParser(description="IDEAS Proposal & Pitch Deck Generator")

    # Common arguments
    parser.add_argument("--client", required=True, help="Client name (e.g., 'Kementerian X')")
    parser.add_argument("--sector", required=True, choices=SECTOR_CONTEXT.keys(), help="Client sector")
    parser.add_argument("--services", required=True, help="Comma-separated list of service IDs (e.g., 'S1.1,S1.2')")
    parser.add_argument("--output", help="Output file path (default: [client_name]_[type].md)")

    # Type-specific arguments
    parser.add_argument("--type", default="proposal", choices=["proposal", "pitch"], help="Document type to generate")

    # Pitch-specific arguments
    pitch_group = parser.add_argument_group("Pitch Deck Options")
    pitch_group.add_argument("--working-days", type=int, help="Estimated working days (for pitch deck)")
    pitch_group.add_argument("--price", type=int, help="Lump sum price for the project (for pitch deck)")
    pitch_group.add_argument("--include-tax", action="store_true", help="Flag if the price includes tax (for pitch deck)")
    pitch_group.add_argument("--no-pricing", action="store_true", help="Generate pitch deck without pricing information")
    pitch_group.add_argument("--scope-label", help="Custom scope label for pitch deck (e.g., 'Phase 1')")

    # Proposal-specific arguments
    proposal_group = parser.add_argument_group("Proposal Options")
    proposal_group.add_argument("--headcount", type=int, default=10, help="Total personnel for government proposal")
    proposal_group.add_argument("--months", type=int, default=6, help="Project duration in months for government proposal")

    # Legacy arguments
    parser.add_argument("--level", type=int, help="Legacy argument for backward compatibility (maps to headcount)")

    args = parser.parse_args()

    # --- Argument Validation and Processing ---

    # Handle legacy --level argument
    if args.level is not None:
        args.headcount = args.level
        print("Warning: --level is a legacy argument. Please use --headcount instead.", file=sys.stderr)

    service_ids = [s.strip() for s in args.services.split(',')]

    # Validate services
    for sid in service_ids:
        if sid not in SERVICE_DESCRIPTIONS:
            print(f"Error: Service ID '{sid}' is not valid. Please check available services.", file=sys.stderr)
            sys.exit(1)

    # Determine output path
    client_slug = args.client.lower().replace(" ", "_")
    output_path = args.output or f"{client_slug}_{args.type}.md"

    # --- Generate Document ---
    if args.type == "pitch":
        # Validation for pitch deck
        if not args.no_pricing and args.price is None:
            print("Error: --price is required for pitch decks unless --no-pricing is specified.", file=sys.stderr)
            sys.exit(1)

        generate_pitch(
            client=args.client,
            sector=args.sector,
            service_ids=service_ids,
            working_days=args.working_days,
            price=args.price,
            include_tax=args.include_tax,
            no_pricing=args.no_pricing,
            scope_label=args.scope_label,
            output_path=output_path,
        )
    else:  # proposal
        ext = output_path.rsplit(".", 1)[-1].lower() if "." in output_path else "md"

        if ext in ("pptx", "docx"):
            # Build structured data and generate directly
            proposal_data = _collect_proposal_data(
                args.client, args.sector, service_ids, args.headcount, args.months)
            try:
                from build_proposal_docs import build_pptx, build_docx
                if ext == "pptx":
                    result = build_pptx(proposal_data, output_path)
                else:
                    result = build_docx(proposal_data, output_path)
                if result:
                    print(f"Proposal generated successfully at {result}")
                else:
                    print("Error: Document generation failed.", file=sys.stderr)
                    sys.exit(1)
            except ImportError as e:
                print(f"Error: Missing dependency: {e}", file=sys.stderr)
                sys.exit(1)
        else:
            # Generate markdown (original behavior)
            generate_proposal(
                client=args.client,
                sector=args.sector,
                service_ids=service_ids,
                headcount=args.headcount,
                months=args.months,
                output_path=output_path,
            )

if __name__ == "__main__":
    main()
