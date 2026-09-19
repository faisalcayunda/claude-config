"""
llm_reasoning_helper.py — Helper untuk generate 7-step reasoning chain per gap.
Bagian dari skill `data-gap-analyst`.

Skill ini di-design supaya reasoning chain di-generate oleh LLM (yang
menjalankan skill), bukan oleh rule-based code. Tapi file ini menyediakan:

1. Prompt template yang LLM pakai untuk generate setiap step (anti-halusinasi
   guardrail built-in: cite metric, no speculation tanpa cite, mark uncertain).
2. Validator yang cek apakah output LLM lengkap 7 step + tidak ada banned phrase.
3. Layer 1 dan Layer 2 prompt template.
4. Helper untuk konversi raw gap finding (dari compute_gap.py) → enriched
   finding dengan reasoning_chain + layer1_text + layer2_text.

Pakai dari skill runtime:
    from llm_reasoning_helper import build_reasoning_prompt, validate_chain
    prompt = build_reasoning_prompt(gap_finding, context)
    # call LLM
    chain = parse_chain(llm_response)
    validate_chain(chain)
"""
from __future__ import annotations

import re
from typing import Any

# Banned phrases — anti-halusinasi guardrail (lihat SKILL.md Section "Anti-Halusinasi")
BANNED_PHRASES_TANPA_CITE = [
    "kemungkinan besar", "biasanya", "umumnya", "secara teori",
    "pada umumnya", "kebanyakan", "sering kali",
]

REQUIRED_STEPS = [
    "observation", "magnitude", "hypothesis", "evidence_test",
    "conclusion", "impact", "recommendation",
]


# ============================================================
# Prompts untuk LLM
# ============================================================

REASONING_CHAIN_PROMPT = """\
Kamu adalah Data Gap Analyst. Generate 7-step reasoning chain untuk gap berikut.

CONTEXT:
- Source A: {source_a_identity}
- Source B: {source_b_identity}
- Business entity: {business_entity}
- Purpose: {purpose}

GAP RAW DATA:
{gap_raw_json}

ATURAN BAKU:
1. WAJIB tulis dalam Bahasa Indonesia, narasi paragraf (BUKAN bullet).
2. WAJIB cite metric + value + source query/file di OBSERVATION.
3. JANGAN PERNAH tulis "kemungkinan", "biasanya", "umumnya" tanpa cite source
   DAMA-DMBOK (lihat references/dama_kafit.md) atau metrik aktual.
4. Jika evidence tidak cukup untuk konklusi → tulis eksplisit
   "[uncertain — butuh data tambahan: X]". JANGAN tebak.
5. Confidence harus jujur — low jika evidence tipis, high jika kuat.

OUTPUT FORMAT (7 paragraf, dipisahkan baris kosong):

### OBSERVATION
[1-3 kalimat. Apa angka yang berbeda, value A vs B, source query/file.]

### MAGNITUDE
[1-3 kalimat. Selisih absolut + relatif + threshold classification:
🟢 minor / 🟡 moderate / 🔴 critical sesuai assets/threshold_rubric.md.]

### HYPOTHESIS
[1 paragraf. 2-3 hipotesis penyebab gap, diurutkan dari paling probable,
masing-masing dengan rasional pendek.]

### EVIDENCE TEST
[1 paragraf. Untuk setiap hipotesis, data point apa yang bisa konfirmasi/refute.
Sebutkan query/check spesifik dan hasil aktualnya — atau "belum dicek" jika
memang belum ada data.]

### CONCLUSION
[1 paragraf. Hipotesis yang paling didukung evidence + confidence (low/medium/high).
Jika confidence low → sebutkan apa yang butuh investigasi tambahan.]

### IMPACT
[1 paragraf. Konsekuensi konkret untuk konsumen data downstream — dashboard,
laporan, decision-making, compliance risk. Sebutkan unit konkret (Rp, hari,
jumlah orang) bila relevan.]

### RECOMMENDATION
[1 paragraf. Action konkret + owner (role/tim) + urgency (now/sprint/backlog).]
"""


LAYER1_PROMPT = """\
Generate Layer 1 insight (untuk Tim Data) berdasarkan reasoning chain berikut:

GAP ID: {gap_id}
SEVERITY: {severity}
DIMENSION: {dimension}
REASONING CHAIN:
{reasoning_chain}

ATURAN LAYER 1:
- Bahasa teknis — boleh pakai SQL, DDL, statistical test name, threshold numerik.
- Sertakan SQL snippet konkret (untuk reconciliation query atau ALTER TABLE).
- Sertakan monitoring rule (pilih: Great Expectations / Soda / dbt test).
- Sertakan referensi DAMA-DMBOK KA-04 atau KA-11 (lihat references/dama_kafit.md).
- Tone: peer-to-peer engineer. Boleh asumsi pembaca paham DDL, FK, ETL.

Format mengikuti assets/layer1_template.md.
"""


LAYER2_PROMPT = """\
Generate Layer 2 insight (untuk Stakeholder Awam) berdasarkan reasoning chain
berikut:

GAP ID: {gap_id}
SEVERITY: {severity}
REASONING CHAIN:
{reasoning_chain}

ATURAN LAYER 2 — CRITICAL:
- TANPA istilah teknis. JANGAN tulis "schema", "constraint", "cardinality",
  "NULL ratio", "Kolmogorov-Smirnov", "Jaccard", "primary key", "foreign key",
  "ETL", "query", "DDL", "stddev", "kurtosis".
- Pakai analogi sehari-hari (daftar absen, daftar tagihan, inventory toko).
- Konsekuensi bisnis WAJIB konkret — Rp, hari, jumlah pelanggan, jumlah laporan.
- Akhiri dengan 2-3 PERTANYAAN STRATEGIS untuk pimpinan (bukan to-do teknis).
- Test kelayakan: kalau dibaca seseorang yang baru join 1 minggu dan tidak
  pernah pegang database, harus bisa paham 80% isinya tanpa googling.

Format mengikuti assets/layer2_template.md.
"""


# ============================================================
# Builders & Validators
# ============================================================

def build_reasoning_prompt(gap: dict, context: dict) -> str:
    """Build prompt untuk LLM generate reasoning chain."""
    import json
    return REASONING_CHAIN_PROMPT.format(
        source_a_identity=context.get("source_a_identity", "?"),
        source_b_identity=context.get("source_b_identity", "?"),
        business_entity=context.get("business_entity", "?"),
        purpose=context.get("purpose", "?"),
        gap_raw_json=json.dumps(gap, indent=2, default=str, ensure_ascii=False),
    )


def build_layer1_prompt(gap: dict, reasoning_chain: dict) -> str:
    return LAYER1_PROMPT.format(
        gap_id=gap.get("gap_id", "?"),
        severity=gap["severity"],
        dimension=gap["dimension"],
        reasoning_chain=_chain_to_text(reasoning_chain),
    )


def build_layer2_prompt(gap: dict, reasoning_chain: dict) -> str:
    return LAYER2_PROMPT.format(
        gap_id=gap.get("gap_id", "?"),
        severity=gap["severity"],
        reasoning_chain=_chain_to_text(reasoning_chain),
    )


def parse_chain(llm_response: str) -> dict:
    """Parse LLM response → dict {step_name: paragraph}."""
    chain = {}
    pattern = re.compile(r"###\s*(\w[\w\s]*)\s*\n+(.*?)(?=\n###|\Z)", re.DOTALL)
    for match in pattern.finditer(llm_response):
        step = match.group(1).lower().strip().replace(" ", "_")
        text = match.group(2).strip()
        # Map flexible names ke REQUIRED_STEPS
        step_key = _normalize_step_name(step)
        if step_key:
            chain[step_key] = text
    return chain


def _normalize_step_name(name: str) -> str | None:
    mapping = {
        "observation": "observation",
        "magnitude": "magnitude",
        "hypothesis": "hypothesis",
        "hypotheses": "hypothesis",
        "evidence_test": "evidence_test",
        "evidence": "evidence_test",
        "conclusion": "conclusion",
        "impact": "impact",
        "recommendation": "recommendation",
        "recommendations": "recommendation",
    }
    return mapping.get(name)


def validate_chain(chain: dict) -> tuple[bool, list[str]]:
    """Cek apakah chain lengkap 7 step + tidak ada banned phrase tanpa cite."""
    errors = []
    for step in REQUIRED_STEPS:
        if step not in chain:
            errors.append(f"Missing step: {step}")
            continue
        text = chain[step]
        for phrase in BANNED_PHRASES_TANPA_CITE:
            if phrase.lower() in text.lower():
                # Cek apakah ada cite (DMBOK / source / query)
                if not _has_citation(text):
                    errors.append(
                        f"Step '{step}' pakai '{phrase}' tanpa citation"
                    )
    return len(errors) == 0, errors


def _has_citation(text: str) -> bool:
    """Cek apakah ada citation pattern di text."""
    patterns = [
        r"DMBOK2\s*§",
        r"DMBOK2\s*KA-",
        r"source[_\s]trace",
        r"SELECT\s",
        r"COUNT\s*\(",
        r"\.csv\s",
        r"\[uncertain",
    ]
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False


def _chain_to_text(chain: dict) -> str:
    """Convert chain dict → text untuk feed ke prompt berikutnya."""
    parts = []
    for step in REQUIRED_STEPS:
        if step in chain:
            parts.append(f"### {step.upper().replace('_', ' ')}\n{chain[step]}")
    return "\n\n".join(parts)


# ============================================================
# Enrich findings (full orchestration)
# ============================================================

def enrich_finding(gap: dict, context: dict,
                   llm_caller: callable,
                   strict_validation: bool = True) -> dict:
    """Enrich satu gap dengan reasoning chain + layer1 + layer2.

    Args:
        gap: raw gap finding dari compute_gap.py
        context: metadata (source identity, business entity, purpose)
        llm_caller: callable(prompt: str) -> str  (LLM API wrapper)
        strict_validation: jika True, raise error jika validation gagal

    Returns:
        Enriched gap finding (gap dengan tambahan reasoning_chain, layer1_text,
        layer2_text, confidence).
    """
    # Step 1: reasoning chain
    chain_prompt = build_reasoning_prompt(gap, context)
    chain_response = llm_caller(chain_prompt)
    chain = parse_chain(chain_response)
    ok, errors = validate_chain(chain)
    if not ok and strict_validation:
        raise ValueError(f"Reasoning chain validation failed: {errors}")
    gap["reasoning_chain"] = chain
    gap["validation_errors"] = errors

    # Step 2: layer 1
    layer1_prompt = build_layer1_prompt(gap, chain)
    gap["layer1_text"] = llm_caller(layer1_prompt)

    # Step 3: layer 2
    layer2_prompt = build_layer2_prompt(gap, chain)
    gap["layer2_text"] = llm_caller(layer2_prompt)

    # Extract confidence dari conclusion (best effort)
    conclusion = chain.get("conclusion", "")
    for level in ("high", "medium", "low"):
        if f"confidence: {level}" in conclusion.lower() or f"confidence {level}" in conclusion.lower():
            gap["confidence"] = level
            break
    else:
        gap["confidence"] = "medium"

    return gap


def enrich_all(findings: list[dict], context: dict,
               llm_caller: callable) -> list[dict]:
    """Enrich semua findings. Lewati yang error jika strict_validation=False."""
    enriched = []
    for f in findings:
        try:
            enriched.append(enrich_finding(f, context, llm_caller, strict_validation=False))
        except Exception as e:
            f["enrichment_error"] = str(e)
            enriched.append(f)
    return enriched


if __name__ == "__main__":
    # Demo: print sample prompts
    sample_gap = {
        "gap_id": "D1-001",
        "dimension": "D1",
        "metric": "row_count_diff",
        "severity": "🔴",
        "value_a": 1247892,
        "value_b": 1103456,
        "absolute": 144436,
        "relative": 0.1158,
        "context": "orders vs fact_orders",
    }
    sample_ctx = {
        "source_a_identity": "prod_oltp.public",
        "source_b_identity": "dwh.mart",
        "business_entity": "Order Management",
        "purpose": "Rekonsiliasi pre-audit Q1 2026",
    }
    print("=== REASONING CHAIN PROMPT ===")
    print(build_reasoning_prompt(sample_gap, sample_ctx))
    print("\n=== LAYER 1 PROMPT (sample) ===")
    print(build_layer1_prompt(sample_gap, {"observation": "...", "conclusion": "..."}))
