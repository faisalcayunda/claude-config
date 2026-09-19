#!/usr/bin/env python3
"""
IDEAS Service & Product Recommendation Engine

Usage:
    python3 recommend_service.py --need "<client need description>"
    python3 recommend_service.py --sector <government|enterprise|academia|media>
    python3 recommend_service.py --challenge "<challenge description>"
    python3 recommend_service.py --need "..." --json

Outputs a structured recommendation of IDEAS services and products
based on the client's needs, sector, or challenges.
"""

# Cross-Skill Integration:
#   web-scraper: Gather client context before recommendation — scrape
#     SPBE scores, portal status, and open data availability to inform
#     service matching.
#   dama-research: Map recommended services to DAMA-DMBOK knowledge areas
#     using references/dama-integration-map.md for theoretical grounding.
#
# Role Taxonomy:
#   All 141 roles are organized into 4 groups (Board, Biz&Digital, PDT, DAMA)
#   and 6 categories (Management, Managerial, Lead, Analyst, Engineer, Officer).
#   See references/role-definitions.md for DDaT-aligned role definitions.
#   See references/human-resources-and-pricing.md for salary and pricing details.


import argparse
import json
import sys
from pricing_engine import TYPICAL_TEAMS, get_external_price

# --- Configuration ---
# Centralized configuration for script behavior.
# Future improvement: Load this from an external file (e.g., YAML, JSON) for easier management.
CONFIG = {
    "DEFAULT_OUTPUT_FORMAT": "human-readable", # Options: "human-readable", "json"
    "ENABLE_COST_ESTIMATION": True, # Toggle for cost estimation feature
}

# --- Knowledge Base ---
# This section contains the core data about services, products, and sector priorities.
# Future improvement: Move this to a dedicated, easily updatable data file (e.g., a CSV or JSON file).
# This would allow non-developers to maintain the knowledge base.

SERVICES = {
    "advisory": {
        "pillar": "Advisory & Governance",
        "services": {
            "data-strategy": {
                "name": "Data Strategy & Roadmap Development",
                "keywords": ["strategy", "roadmap", "transformasi", "perencanaan", "visi data", "kematangan", "maturity", "strategic planning", "GenAI readiness", "AI strategy", "digital transformation"],
                "target": ["C-Level", "CIO", "CDO", "VP IT"],
                "sectors": ["government", "enterprise"],
                "description": "Merancang strategi data dan peta jalan implementasi multi-tahun."
            },
            "governance-compliance": {
                "name": "Data Governance & Compliance Framework",
                "keywords": ["governance", "tata kelola", "compliance", "kepatuhan", "regulasi", "UU PDP", "SPBE", "SDI", "kebijakan", "policy", "GDPR", "AI governance", "responsible AI", "NIST AI RMF", "ISO 42001", "EU AI Act", "data contract"],
                "target": ["Compliance Manager", "DPO", "C-Level", "Legal"],
                "sectors": ["government", "enterprise"],
                "description": "Membangun kerangka kerja tata kelola data end-to-end berbasis DAMA-DMBOK."
            },
            "maturity-assessment": {
                "name": "Data Maturity Assessment & Benchmarking",
                "keywords": ["maturity", "kematangan", "assessment", "asesmen", "benchmark", "evaluasi", "audit"],
                "target": ["CDO", "CIO", "VP Data"],
                "sectors": ["government", "enterprise"],
                "description": "Memberikan gambaran objektif posisi kematangan data organisasi."
            },
            "sop-policy": {
                "name": "Data Governance SOP & Policy Framework",
                "keywords": ["SOP", "prosedur", "kebijakan", "policy", "standar operasional", "dokumentasi"],
                "target": ["Data Governance Office", "IT Operations"],
                "sectors": ["government", "enterprise"],
                "description": "Membangun dokumentasi operasional komprehensif untuk tata kelola data."
            },
            "data-valuation": {
                "name": "Data Asset Valuation & Monetization Advisory",
                "keywords": ["valuation", "valuasi", "monetisasi", "monetization", "infonomics", "aset data", "data asset", "balance sheet", "neraca", "ROI data"],
                "target": ["CFO", "CDO", "C-Level", "Board"],
                "sectors": ["government", "enterprise"],
                "description": "Menilai dan memonetisasi aset data menggunakan framework Infonomics."
            }
        }
    },
    "platform": {
        "pillar": "Platform & Solution Implementation",
        "services": {
            "product-dev": {
                "name": "Data-Centric Digital Product Development & UX Design",
                "keywords": ["product", "produk digital", "UX", "UI", "design", "aplikasi", "development"],
                "target": ["Product Manager", "CTO", "UX Team"],
                "sectors": ["enterprise"],
                "description": "Mengembangkan produk digital berpusat pada data."
            },
            "core-platform": {
                "name": "Core Data Platform & Modernization",
                "keywords": ["platform", "modernisasi", "data lake", "warehouse", "ETL", "cloud", "infrastruktur", "migration", "data mesh", "data fabric", "lakehouse", "GenAI platform", "vector database", "MLOps"],
                "target": ["CTO", "Data Engineering", "IT Infrastructure"],
                "sectors": ["enterprise"],
                "description": "Membangun atau memodernisasi infrastruktur data inti."
            },
            "gov-portal": {
                "name": "Government Data Portal Platform",
                "keywords": ["portal", "pemerintah", "government", "satu data", "open data", "transparansi", "publik"],
                "target": ["Instansi Pemerintah", "Walidata", "BPS"],
                "sectors": ["government"],
                "description": "Platform portal data siap pakai untuk pemerintahan."
            },
            "enterprise-portal": {
                "name": "Enterprise Data Portal & Self-Service Analytics",
                "keywords": ["portal enterprise", "self-service", "analytics", "dashboard", "BI", "visualisasi", "demokratisasi", "AI-powered analytics", "conversational analytics", "GenAI insights"],
                "target": ["Business Analyst", "BI Analyst", "CDO"],
                "sectors": ["enterprise"],
                "description": "Mendemokratisasi akses data dengan tata kelola enterprise."
            },
            "data-exchange": {
                "name": "Secure & Trusted Data Exchange & API Gateway",
                "keywords": ["exchange", "pertukaran", "API", "gateway", "integrasi", "interoperabilitas", "berbagi data"],
                "target": ["Data Engineer", "API Architect"],
                "sectors": ["government", "enterprise"],
                "description": "Pertukaran data aman dan terkelola antar sistem."
            },
            "analytics-viz": {
                "name": "Analytics & Visualization Solutions",
                "keywords": ["analytics", "visualization", "visualisasi", "dashboard", "reporting", "insight", "data storytelling"],
                "target": ["Business Analyst", "Data Scientist", "Executive"],
                "sectors": ["enterprise", "government"],
                "description": "Mengubah data menjadi visualisasi dan insight actionable."
            }
        }
    },
    "empowerment": {
        "pillar": "Empowerment & Managed Services",
        "services": {
            "dgo-service": {
                "name": "Data Governance Office (DGO) as a Service",
                "keywords": ["DGO", "governance office", "managed", "terkelola", "operasional tata kelola"],
                "target": ["Organisasi tanpa DGO", "CDO baru"],
                "sectors": ["government", "enterprise"],
                "description": "Fungsi DGO terkelola penuh atau pendampingan membangun DGO."
            },
            "data-literacy": {
                "name": "Data Literacy & Culture Program",
                "keywords": ["literacy", "literasi", "budaya data", "culture", "training", "pelatihan", "awareness", "change management"],
                "target": ["Seluruh level organisasi"],
                "sectors": ["government", "enterprise", "academia"],
                "description": "Membangun budaya berbasis data di seluruh organisasi."
            },
            "certified-training": {
                "name": "Data Management Certified Training",
                "keywords": ["sertifikasi", "certification", "CDMP", "BNSP", "training", "pelatihan", "DAMA"],
                "target": ["Data professionals", "IT staff"],
                "sectors": ["government", "enterprise", "academia"],
                "description": "Persiapan sertifikasi CDMP dan BNSP Data Management."
            },
            "knowledge-transfer": {
                "name": "Knowledge Transfer & Data Monetization as a Service",
                "keywords": ["knowledge transfer", "transfer pengetahuan", "sustainability", "keberlanjutan", "self-service", "monetisasi", "playbook"],
                "target": ["CDO", "Data Team", "Business Unit"],
                "sectors": ["government", "enterprise"],
                "description": "Transfer pengetahuan dan pendampingan monetisasi data berkelanjutan."
            }
        }
    }
}

PRODUCTS = {
    "mapedge": {
        "name": "IDEAS MapEdge",
        "keywords": ["geospasial", "geospatial", "peta", "map", "GIS", "lokasi", "KSP", "KUGI"],
        "category": "Public & Leadership",
        "description": "Pengelolaan data geospasial."
    },
    "dataspace": {
        "name": "IDEAS DataSpace",
        "keywords": ["tabular", "data quality", "kualitas data", "metadata", "master data", "reference data"],
        "category": "Internal Operations",
        "description": "Pengelolaan data tabular, kualitas, dan integritas."
    },
    "civic-insight": {
        "name": "IDEAS Civic Insight",
        "keywords": ["katalog", "catalog", "publik", "citizen", "transparansi", "open data"],
        "category": "Public & Leadership",
        "description": "Katalog data dan wawasan publik."
    },
    "control-center": {
        "name": "IDEAS Control Center",
        "keywords": ["admin", "manajemen", "publikasi", "user management", "RBAC", "kontrol"],
        "category": "Internal Operations",
        "description": "Manajemen terpusat publikasi dan administrasi."
    },
    "data-hub": {
        "name": "IDEAS Data Hub",
        "keywords": ["exchange", "pertukaran", "API", "integrasi", "data contract", "monitoring"],
        "category": "Internal Operations",
        "description": "Pertukaran data aman dan terkelola."
    },
    "collect": {
        "name": "IDEAS Collect",
        "keywords": ["form", "formulir", "survei", "pengumpulan", "collection", "survey"],
        "category": "Internal Operations",
        "description": "Pengumpulan data fleksibel."
    },
    "executive": {
        "name": "IDEAS Executive",
        "keywords": ["executive", "eksekutif", "dashboard", "KPI", "insight", "decision", "keputusan", "AI insights", "GenAI", "conversational BI"],
        "category": "Public & Leadership",
        "description": "Wawasan eksekutif dan insight actionable."
    },
    "core-engine": {
        "name": "IDEAS Core Data Engine",
        "keywords": ["engine", "infrastruktur", "pipeline", "ETL", "orchestration", "connector"],
        "category": "Core Engine",
        "description": "Infrastruktur teknis inti ekosistem."
    }
}

SECTOR_PRIORITIES = {
    "government": {
        "primary_services": ["governance-compliance", "gov-portal", "maturity-assessment", "data-strategy"],
        "primary_products": ["civic-insight", "mapedge", "control-center", "data-hub"],
        "key_regulations": ["SPBE", "SDI", "UU PDP", "DTSEN", "KSP"],
        "description": "Instansi pemerintah membutuhkan kepatuhan regulasi, portal data publik, dan tata kelola data yang kuat."
    },
    "enterprise": {
        "primary_services": ["data-strategy", "enterprise-portal", "core-platform", "governance-compliance"],
        "primary_products": ["dataspace", "executive", "data-hub", "core-engine"],
        "key_regulations": ["UU PDP", "ISO 27001"],
        "description": "Perusahaan swasta membutuhkan strategi data, platform analytics, dan keunggulan kompetitif berbasis data."
    },
    "bumn": {
        "primary_services": ["data-strategy", "governance-compliance", "enterprise-portal", "core-platform", "maturity-assessment"],
        "primary_products": ["dataspace", "executive", "data-hub", "control-center"],
        "key_regulations": ["UU PDP", "PP BUMN", "SPBE", "ISO 27001"],
        "description": "BUMN membutuhkan transformasi digital, tata kelola data enterprise, platform analytics, dan kepatuhan regulasi ganda (pemerintah + korporasi)."
    },
    "international": {
        "primary_services": ["data-strategy", "governance-compliance", "maturity-assessment", "certified-training"],
        "primary_products": ["dataspace", "executive", "civic-insight"],
        "key_regulations": ["GDPR", "ISO 27001", "DAMA-DMBOK"],
        "description": "Organisasi internasional membutuhkan strategi data lintas batas, kepatuhan regulasi global, dan transfer pengetahuan."
    },
    "academia": {
        "primary_services": ["certified-training", "data-literacy", "maturity-assessment"],
        "primary_products": ["dataspace", "civic-insight"],
        "key_regulations": ["SDI"],
        "description": "Institusi akademik membutuhkan pelatihan, literasi data, dan pengelolaan data penelitian."
    },
    "media": {
        "primary_services": ["analytics-viz", "data-literacy"],
        "primary_products": ["civic-insight", "executive", "collect"],
        "key_regulations": ["UU PDP"],
        "description": "Organisasi media membutuhkan analytics, visualisasi data, dan pengelolaan konten."
    }
}


def score_match(text: str, keywords: list) -> int:
    """Calculates a simple keyword matching score.
    Future improvement: Enhance scoring with NLP techniques like TF-IDF, word embeddings (e.g., Word2Vec, GloVe),
    or semantic similarity from transformer models to better understand the user's intent.
    """
    text_lower = text.lower()
    # Simple keyword counting. A more advanced version could weigh keywords.
    return sum(1 for kw in keywords if kw.lower() in text_lower)


def _add_cost_estimates(results_list):
    """Add cost estimates to a list of service recommendations."""
    # Future improvement: The cost estimation could be more sophisticated.
    # It could factor in project duration, complexity, and specific roles more dynamically.
    # Integrating with a proper financial system or a more detailed pricing model would be a significant upgrade.
    if not CONFIG["ENABLE_COST_ESTIMATION"]:
        return results_list

    for r in results_list:
        if r["id"] in TYPICAL_TEAMS:
            try:
                team_spec = TYPICAL_TEAMS[r["id"]]
                total_cost = 0
                for member in team_spec:
                    monthly_cost = get_external_price(member["role"], member["level"])
                    total_cost += monthly_cost * member["months"] * member["qty"]
                r["estimated_cost"] = "Rp {:,.0f}".format(total_cost)
                r["estimated_team_size"] = sum(m["qty"] for m in team_spec)
            except Exception as e:
                # Gracefully handle errors in cost estimation (e.g., missing pricing data)
                r["estimated_cost"] = "Not Available"
                r["error_in_costing"] = str(e)
    return results_list


def recommend_by_need(need: str) -> dict:
    """Recommends services and products based on a textual description of client needs."""
    results = {"query": need, "services": [], "products": []}

    for pillar_data in SERVICES.values():
        for svc_id, svc in pillar_data["services"].items():
            score = score_match(need, svc["keywords"])
            if score > 0:
                results["services"].append({
                    "id": svc_id,
                    "name": svc["name"],
                    "pillar": pillar_data["pillar"],
                    "description": svc["description"],
                    "relevance_score": score
                })

    for prod_id, prod in PRODUCTS.items():
        score = score_match(need, prod["keywords"])
        if score > 0:
            results["products"].append({
                "id": prod_id,
                "name": prod["name"],
                "category": prod["category"],
                "description": prod["description"],
                "relevance_score": score
            })

    # Sort results by relevance to show the most likely matches first.
    results["services"].sort(key=lambda x: x["relevance_score"], reverse=True)
    results["products"].sort(key=lambda x: x["relevance_score"], reverse=True)

    _add_cost_estimates(results["services"])

    return results


def recommend_by_sector(sector: str) -> dict:
    """Recommends a standard set of services and products for a given client sector."""
    sector = sector.lower()
    if sector not in SECTOR_PRIORITIES:
        return {"error": "Unknown sector: {}. Valid: government, enterprise, bumn, international, academia, media".format(sector)}

    sp = SECTOR_PRIORITIES[sector]
    results = {
        "sector": sector,
        "description": sp["description"],
        "key_regulations": sp["key_regulations"],
        "recommended_services": [],
        "recommended_products": []
    }

    for svc_id in sp["primary_services"]:
        for pillar_data in SERVICES.values():
            if svc_id in pillar_data["services"]:
                svc = pillar_data["services"][svc_id]
                results["recommended_services"].append({
                    "id": svc_id,
                    "name": svc["name"],
                    "pillar": pillar_data["pillar"],
                    "description": svc["description"]
                })

    for prod_id in sp["primary_products"]:
        if prod_id in PRODUCTS:
            prod = PRODUCTS[prod_id]
            results["recommended_products"].append({
                "id": prod_id,
                "name": prod["name"],
                "category": prod["category"],
                "description": prod["description"]
            })

    _add_cost_estimates(results["recommended_services"])

    return results


def print_need_results(results):
    """Print need-based recommendation results in human-readable format."""
    print("Recommendation for: {}".format(results.get("query", "N/A")))
    print()

    if results["services"]:
        print("--- Recommended Services ---")
        for s in results["services"]:
            cost_str = ""
            if "estimated_cost" in s:
                cost_str = " | Est. Cost: {}".format(s["estimated_cost"])
            print("  - {} [{}] (Score: {}){}".format(
                s["name"], s["pillar"], s["relevance_score"], cost_str))
            print("    {}".format(s["description"]))
        print()

    if results["products"]:
        print("--- Recommended Products ---")
        for p in results["products"]:
            print("  - {} [{}] (Score: {})".format(
                p["name"], p["category"], p["relevance_score"]))
            print("    {}".format(p["description"]))
        print()

    if not results["services"] and not results["products"]:
        print("No matching services or products found. Please try a different query.")


def print_sector_results(results):
    """Print sector-based recommendation results in human-readable format."""
    print("Recommendation for sector: {}".format(results["sector"].upper()))
    print("> {}".format(results["description"]))
    print("> Key Regulations: {}".format(", ".join(results["key_regulations"])))
    print()

    if results["recommended_services"]:
        print("--- Primary Services ---")
        for s in results["recommended_services"]:
            cost_str = ""
            if "estimated_cost" in s:
                cost_str = " | Est. Cost: {}".format(s["estimated_cost"])
            print("  - {} [{}]{}".format(s["name"], s["pillar"], cost_str))
            print("    {}".format(s["description"]))
        print()

    if results["recommended_products"]:
        print("--- Primary Products ---")
        for p in results["recommended_products"]:
            print("  - {} [{}]".format(p["name"], p["category"]))
            print("    {}".format(p["description"]))
        print()


def main():
    """Main function to parse arguments and run the recommendation engine."""
    # Future improvement: Add a --verbose flag for debug logging.
    # Future improvement: Could be refactored into a class `RecommendationEngine` to better encapsulate state and logic.
    parser = argparse.ArgumentParser(
        description="IDEAS Service & Product Recommendation Engine",
        epilog="Example: python3 recommend_service.py --need \"Saya butuh strategi AI untuk transformasi digital.\""
    )
    parser.add_argument("--need", type=str, help="Client need description")
    parser.add_argument("--sector", type=str, choices=["government", "enterprise", "bumn", "international", "academia", "media"],
                        help="Client sector")
    parser.add_argument("--challenge", type=str, help="Client challenge description (alias for --need)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    try:
        if args.need or args.challenge:
            query = args.need or args.challenge
            results = recommend_by_need(query)
            output_format = "json" if args.json else CONFIG["DEFAULT_OUTPUT_FORMAT"]
            if output_format == "json":
                print(json.dumps(results, indent=2, ensure_ascii=False))
            else:
                print_need_results(results)
        elif args.sector:
            results = recommend_by_sector(args.sector)
            output_format = "json" if args.json else CONFIG["DEFAULT_OUTPUT_FORMAT"]
            if "error" in results and output_format != "json":
                print(f"Error: {results['error']}", file=sys.stderr)
                sys.exit(1)
            if output_format == "json":
                print(json.dumps(results, indent=2, ensure_ascii=False))
            else:
                print_sector_results(results)
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        # Basic error handling for unexpected issues.
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        print("Please check the input parameters and try again.", file=sys.stderr)
        # Future improvement: Implement more specific exception handling for different error types (e.g., file not found for pricing, invalid input). 
        # For a production system, log this error to a monitoring service.
        sys.exit(1)


if __name__ == "__main__":
    # Future improvement: Consider adding a simple test suite that can be run from the command line,
    # e.g., `python3 recommend_service.py --test` to validate the logic.
    main()
