#!/usr/bin/env python3
"""
IDEAS Company Skill — Comprehensive Multi-Tier Validation Script
================================================================
Run after every skill improvement to validate integrity, consistency,
and cross-file dependencies across the entire skill.

Usage:
    python3 scripts/validate_skill.py                    # Full validation (all tiers)
    python3 scripts/validate_skill.py --tier 1           # Quick check only
    python3 scripts/validate_skill.py --tier 2           # Up to structural audit
    python3 scripts/validate_skill.py --tier 3           # Up to dependency analysis
    python3 scripts/validate_skill.py --tier 4           # Up to runtime tests
    python3 scripts/validate_skill.py --tier 5           # Full + change impact
    python3 scripts/validate_skill.py --report report.md # Save report to file
    python3 scripts/validate_skill.py --baseline         # Save current state as baseline
    python3 scripts/validate_skill.py --diff             # Compare against baseline

Tiers:
    1. Quick Check      — SKILL.md format, YAML frontmatter, line count, description length
    2. Structural Audit — File inventory, compile all scripts, file count consistency
    3. Dependency Sync  — Cross-references, orphan detection, service code sync, branding sync
    4. Runtime Tests    — Execute key scripts, test document generators
    5. Change Impact    — Compare against baseline, identify affected files, generate report
"""

import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import textwrap
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SKILL_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = SKILL_DIR / "scripts"
REFS_DIR = SKILL_DIR / "references"
TEMPLATES_DIR = SKILL_DIR / "templates"
SKILL_MD = SKILL_DIR / "SKILL.md"
BASELINE_FILE = SKILL_DIR / ".validation_baseline.json"

LEGAL_NAME = "PT Indonesian Data Ecosystem"
BRAND_NAME = "IDEAS — Indonesian Data Ecosystem Agency & Solutions"
COMPANY_WEB = "https://data-ecosystem.id"
COMPANY_TAGLINE = "Empowering Innovation Through Data"

MAX_SKILL_MD_LINES = 500
MAX_DESCRIPTION_CHARS = 1024
MAX_SKILL_SIZE_MB = 10

# Branding constants expected in generators
BRANDING_KEYS = {
    "company_name": LEGAL_NAME,
    "company_tagline": COMPANY_TAGLINE,
    "company_web": COMPANY_WEB,
}

# Service codes from services-catalog.md
EXPECTED_SERVICE_PREFIXES = ["S1", "S2", "S3"]

# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------
class Colors:
    """ANSI color codes for terminal output."""
    PASS = "\033[92m"   # green
    FAIL = "\033[91m"   # red
    WARN = "\033[93m"   # yellow
    INFO = "\033[94m"   # blue
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"

    @staticmethod
    def strip(text):
        """Remove ANSI codes for file output."""
        return re.sub(r'\033\[[0-9;]*m', '', text)


class ValidationResult:
    """Stores results for a single check."""
    def __init__(self, name, passed, detail="", severity="error"):
        self.name = name
        self.passed = passed
        self.detail = detail
        self.severity = severity  # error, warning, info

    def __str__(self):
        if self.passed:
            icon = f"{Colors.PASS}✓{Colors.RESET}"
        elif self.severity == "warning":
            icon = f"{Colors.WARN}⚠{Colors.RESET}"
        else:
            icon = f"{Colors.FAIL}✗{Colors.RESET}"
        line = f"  {icon} {self.name}"
        if self.detail:
            line += f" — {self.detail}"
        return line


class TierResult:
    """Stores results for an entire tier."""
    def __init__(self, tier_num, tier_name):
        self.tier_num = tier_num
        self.tier_name = tier_name
        self.checks = []
        self.start_time = datetime.now()
        self.end_time = None

    def add(self, result):
        self.checks.append(result)

    def finish(self):
        self.end_time = datetime.now()

    @property
    def passed(self):
        return all(c.passed or c.severity != "error" for c in self.checks)

    @property
    def errors(self):
        return [c for c in self.checks if not c.passed and c.severity == "error"]

    @property
    def warnings(self):
        return [c for c in self.checks if not c.passed and c.severity == "warning"]

    @property
    def duration_ms(self):
        if self.end_time:
            return int((self.end_time - self.start_time).total_seconds() * 1000)
        return 0


def get_all_files():
    """Get all files excluding __pycache__ and hidden files."""
    files = []
    for root, dirs, filenames in os.walk(SKILL_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__" and not d.startswith('.')]
        for f in filenames:
            if not f.startswith('.'):
                files.append(Path(root) / f)
    return sorted(files)


def read_text(path):
    """Read file as text, return None for binary."""
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return None


def file_hash(path):
    """SHA256 hash of file content."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


# ---------------------------------------------------------------------------
# Tier 1: Quick Check
# ---------------------------------------------------------------------------
def tier1_quick_check():
    """SKILL.md format, YAML, line count, description."""
    tier = TierResult(1, "Quick Check")

    # 1.1 SKILL.md exists
    tier.add(ValidationResult(
        "SKILL.md exists",
        SKILL_MD.exists(),
        str(SKILL_MD) if SKILL_MD.exists() else "MISSING"
    ))
    if not SKILL_MD.exists():
        tier.finish()
        return tier

    content = SKILL_MD.read_text(encoding="utf-8")
    lines = content.split("\n")

    # 1.2 YAML frontmatter
    has_frontmatter = content.startswith("---")
    tier.add(ValidationResult(
        "YAML frontmatter present",
        has_frontmatter,
        "Starts with ---" if has_frontmatter else "Missing --- delimiter"
    ))

    # 1.3 Required YAML fields
    name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
    desc_match = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)
    tier.add(ValidationResult(
        "YAML 'name' field",
        bool(name_match),
        f"'{name_match.group(1).strip()}'" if name_match else "MISSING"
    ))
    tier.add(ValidationResult(
        "YAML 'description' field",
        bool(desc_match),
        f"{len(desc_match.group(1).strip())} chars" if desc_match else "MISSING"
    ))

    # 1.4 Description length
    if desc_match:
        desc_len = len(desc_match.group(1).strip())
        tier.add(ValidationResult(
            f"Description length ≤ {MAX_DESCRIPTION_CHARS}",
            desc_len <= MAX_DESCRIPTION_CHARS,
            f"{desc_len} / {MAX_DESCRIPTION_CHARS} chars"
        ))

    # 1.5 Line count
    line_count = len(lines)
    tier.add(ValidationResult(
        f"SKILL.md lines ≤ {MAX_SKILL_MD_LINES}",
        line_count <= MAX_SKILL_MD_LINES,
        f"{line_count} / {MAX_SKILL_MD_LINES} lines"
    ))

    # 1.6 Version tag present
    version_match = re.search(r'v(\d+\.\d+)', content)
    tier.add(ValidationResult(
        "Version tag present",
        bool(version_match),
        f"v{version_match.group(1)}" if version_match else "NOT FOUND"
    ))

    # 1.7 Legal entity info
    has_legal = "PT Indonesian Data Ecosystem" in content
    has_nib = "2207250135544" in content
    tier.add(ValidationResult(
        "Legal entity name in SKILL.md",
        has_legal,
        LEGAL_NAME if has_legal else "MISSING"
    ))
    tier.add(ValidationResult(
        "NIB number in SKILL.md",
        has_nib,
        "2207250135544" if has_nib else "MISSING",
        severity="warning"
    ))

    # 1.8 Total skill size
    total_size = sum(f.stat().st_size for f in get_all_files())
    size_mb = total_size / (1024 * 1024)
    tier.add(ValidationResult(
        f"Skill size ≤ {MAX_SKILL_SIZE_MB} MB",
        size_mb <= MAX_SKILL_SIZE_MB,
        f"{size_mb:.1f} MB"
    ))

    tier.finish()
    return tier


# ---------------------------------------------------------------------------
# Tier 2: Structural Audit
# ---------------------------------------------------------------------------
def tier2_structural_audit():
    """File inventory, compile scripts, file count consistency."""
    tier = TierResult(2, "Structural Audit")

    all_files = get_all_files()
    refs = [f for f in all_files if REFS_DIR in f.parents or f.parent == REFS_DIR]
    scripts = [f for f in all_files if (SCRIPTS_DIR in f.parents or f.parent == SCRIPTS_DIR) and f.suffix == ".py"]
    templates = [f for f in all_files if TEMPLATES_DIR in f.parents or f.parent == TEMPLATES_DIR]

    # 2.1 File inventory
    tier.add(ValidationResult(
        "File inventory",
        True,
        f"Total={len(all_files)}, Refs={len(refs)}, Scripts={len(scripts)}, Templates={len(templates)}"
    ))

    # 2.2 SKILL.md file count consistency
    skill_content = read_text(SKILL_MD) or ""
    count_match = re.search(r'(\d+)\s+files?\s+across', skill_content)
    if count_match:
        claimed = int(count_match.group(1))
        actual = len(all_files)
        tier.add(ValidationResult(
            "File count matches SKILL.md",
            claimed == actual,
            f"SKILL.md claims {claimed}, actual {actual}"
        ))
    else:
        tier.add(ValidationResult(
            "File count in SKILL.md",
            False,
            "No 'X files across' pattern found",
            severity="warning"
        ))

    # 2.3 Folder count consistency
    for folder_name, folder_files, pattern in [
        ("references", refs, r"`references/`\s*\((\d+)\s+files?\)"),
        ("scripts", scripts, r"`scripts/`\s*\((\d+)\s+files?\)"),
        ("templates", templates, r"`templates/`\s*\((\d+)\s+files?\)"),
    ]:
        match = re.search(pattern, skill_content)
        if match:
            claimed = int(match.group(1))
            actual = len(folder_files)
            tier.add(ValidationResult(
                f"{folder_name}/ count matches SKILL.md",
                claimed == actual,
                f"SKILL.md claims {claimed}, actual {actual}"
            ))

    # 2.4 Compile all Python scripts
    py_files = list(SCRIPTS_DIR.glob("*.py"))
    compile_pass = 0
    compile_fail = []
    for pf in sorted(py_files):
        try:
            with open(pf) as fh:
                compile(fh.read(), pf.name, "exec")
            compile_pass += 1
        except SyntaxError as e:
            compile_fail.append(f"{pf.name}: {e}")

    tier.add(ValidationResult(
        "Python script compilation",
        len(compile_fail) == 0,
        f"{compile_pass}/{len(py_files)} PASS" + (f", FAIL: {compile_fail}" if compile_fail else "")
    ))

    # 2.5 No empty files
    empty_files = [f for f in all_files if f.stat().st_size == 0 and f.name != "__init__.py"]
    tier.add(ValidationResult(
        "No empty files (except __init__.py)",
        len(empty_files) == 0,
        f"{len(empty_files)} empty" + (f": {[f.name for f in empty_files]}" if empty_files else "")
    ))

    # 2.6 No __pycache__ directories
    pycache_dirs = list(SKILL_DIR.rglob("__pycache__"))
    tier.add(ValidationResult(
        "No __pycache__ directories",
        len(pycache_dirs) == 0,
        f"{len(pycache_dirs)} found" if pycache_dirs else "Clean"
    ))

    # 2.7 Logo files are valid PNG
    logo_files = [f for f in templates if f.suffix.lower() == ".png"]
    for logo in logo_files:
        with open(logo, "rb") as lf:
            header = lf.read(8)
        is_png = header[:4] == b'\x89PNG'
        tier.add(ValidationResult(
            f"Logo {logo.name} is valid PNG",
            is_png,
            "Valid PNG header" if is_png else f"Invalid: {header[:4]}"
        ))

    # 2.8 CSV files are valid
    csv_files = [f for f in all_files if f.suffix.lower() == ".csv"]
    for cf in csv_files:
        try:
            with open(cf, newline='', encoding='utf-8') as csvf:
                reader = csv.reader(csvf)
                rows = sum(1 for _ in reader)
            tier.add(ValidationResult(
                f"CSV {cf.name} is valid",
                True,
                f"{rows} rows"
            ))
        except Exception as e:
            tier.add(ValidationResult(
                f"CSV {cf.name} is valid",
                False,
                str(e)
            ))

    tier.finish()
    return tier


# ---------------------------------------------------------------------------
# Tier 3: Dependency Sync
# ---------------------------------------------------------------------------
def tier3_dependency_sync():
    """Cross-references, orphans, service codes, branding, company name."""
    tier = TierResult(3, "Dependency Sync")

    all_files = get_all_files()
    skill_content = read_text(SKILL_MD) or ""

    # 3.1 Cross-reference analysis
    refs_map = defaultdict(set)
    referenced_by = defaultdict(set)

    for f in all_files:
        content = read_text(f)
        if content is None:
            continue
        rel = str(f.relative_to(SKILL_DIR))
        for other in all_files:
            if other == f:
                continue
            other_rel = str(other.relative_to(SKILL_DIR))
            other_name = other.name
            other_stem = other.stem
            if other_name in content or other_stem in content:
                refs_map[rel].add(other_rel)
                referenced_by[other_rel].add(rel)

    total_links = sum(len(v) for v in refs_map.values())
    tier.add(ValidationResult(
        "Cross-reference links",
        total_links > 0,
        f"{total_links} dependency links across {len(refs_map)} files"
    ))

    # 3.2 Orphan detection
    orphans = []
    for f in all_files:
        rel = str(f.relative_to(SKILL_DIR))
        if rel == "SKILL.md" or f.name == "__init__.py":
            continue
        if rel not in referenced_by:
            orphans.append(rel)

    tier.add(ValidationResult(
        "No orphan files",
        len(orphans) == 0,
        f"{len(orphans)} orphans" + (f": {orphans}" if orphans else "")
    ))

    # 3.3 All files referenced in SKILL.md
    files_not_in_skillmd = []
    for f in all_files:
        if f == SKILL_MD or f.name == "__init__.py":
            continue
        name = f.name
        stem = f.stem
        if name not in skill_content and stem not in skill_content:
            files_not_in_skillmd.append(str(f.relative_to(SKILL_DIR)))

    tier.add(ValidationResult(
        "All files referenced in SKILL.md",
        len(files_not_in_skillmd) == 0,
        f"{len(files_not_in_skillmd)} missing" + (f": {files_not_in_skillmd}" if files_not_in_skillmd else ""),
        severity="warning" if files_not_in_skillmd else "error"
    ))

    # 3.4 Service code sync
    services_file = REFS_DIR / "services-catalog.md"
    if services_file.exists():
        svc_content = read_text(services_file) or ""
        catalog_codes = set(re.findall(r'\b(S\d+\.\d+)\b', svc_content))

        # Check scripts that use service codes
        for script_name in ["generate_proposal.py", "estimate_service_cost.py"]:
            script_path = SCRIPTS_DIR / script_name
            if script_path.exists():
                sc = read_text(script_path) or ""
                script_codes = set(re.findall(r'["\']S(\d+\.\d+)["\']', sc))
                script_codes = {f"S{c}" for c in script_codes}
                missing_in_script = catalog_codes - script_codes
                extra_in_script = script_codes - catalog_codes
                if extra_in_script:
                    tier.add(ValidationResult(
                        f"Service codes in {script_name}",
                        False,
                        f"Extra codes not in catalog: {extra_in_script}",
                        severity="warning"
                    ))

        tier.add(ValidationResult(
            "Service catalog codes",
            True,
            f"{len(catalog_codes)} codes found in services-catalog.md"
        ))

    # 3.5 Branding consistency across generators
    generators = ["generate_pdf.py", "generate_pptx.py", "generate_docx.py", "generate_document.py"]
    branding_values = {}
    for gen in generators:
        gen_path = SCRIPTS_DIR / gen
        if not gen_path.exists():
            continue
        content = read_text(gen_path) or ""
        values = {}
        for key, expected in BRANDING_KEYS.items():
            # Search for the constant in various patterns
            patterns = [
                rf'{key.upper()}\s*=\s*["\'](.+?)["\']',
                rf'"{key}":\s*["\'](.+?)["\']',
                rf"'{key}':\s*[\"'](.+?)[\"']",
            ]
            found = None
            for pat in patterns:
                m = re.search(pat, content, re.IGNORECASE)
                if m:
                    found = m.group(1)
                    break
            values[key] = found
        branding_values[gen] = values

    if len(branding_values) >= 2:
        ref_gen = list(branding_values.keys())[0]
        ref_vals = branding_values[ref_gen]
        mismatches = []
        for gen, vals in branding_values.items():
            for key in BRANDING_KEYS:
                if vals.get(key) and ref_vals.get(key) and vals[key] != ref_vals[key]:
                    mismatches.append(f"{gen}.{key}='{vals[key]}' vs {ref_gen}.{key}='{ref_vals[key]}'")

        tier.add(ValidationResult(
            "Branding consistency across generators",
            len(mismatches) == 0,
            f"{len(branding_values)} generators checked" + (f", mismatches: {mismatches}" if mismatches else "")
        ))

    # 3.6 Company name consistency
    old_wrong_names = [
        "PT Indonesian Data Ecosystem Agency & Solutions",
    ]
    name_issues = []
    for f in all_files:
        content = read_text(f)
        if content is None:
            continue
        rel = str(f.relative_to(SKILL_DIR))
        # Skip self — this script contains old names as validation constants
        if f.name == "validate_skill.py":
            continue
        for old_name in old_wrong_names:
            if old_name in content:
                # Check context: brand name references are OK
                for i, line in enumerate(content.split("\n"), 1):
                    if old_name in line:
                        # Allow if it's clearly a brand reference
                        if any(ctx in line for ctx in ["Brand:", "brand:", "IDEAS —", "IDEAS -"]):
                            continue
                        name_issues.append(f"{rel}:{i}")

    tier.add(ValidationResult(
        "No old/wrong legal entity names",
        len(name_issues) == 0,
        f"{len(name_issues)} occurrences" + (f": {name_issues}" if name_issues else ""),
        severity="warning" if name_issues else "error"
    ))

    # 3.7 Broken markdown links
    md_files = [f for f in all_files if f.suffix == ".md"]
    broken_links = []
    for mf in md_files:
        content = read_text(mf) or ""
        rel = str(mf.relative_to(SKILL_DIR))
        # Find references to skill files
        for ref_match in re.finditer(r'`((?:references|scripts|templates)/[^`]+)`', content):
            ref_path = ref_match.group(1)
            full_path = SKILL_DIR / ref_path
            if not full_path.exists():
                broken_links.append(f"{rel} → {ref_path}")

    tier.add(ValidationResult(
        "No broken file references in markdown",
        len(broken_links) == 0,
        f"{len(broken_links)} broken" + (f": {broken_links[:5]}" if broken_links else "")
    ))

    tier.finish()
    return tier


# ---------------------------------------------------------------------------
# Tier 4: Runtime Tests
# ---------------------------------------------------------------------------
def tier4_runtime_tests():
    """Execute key scripts and test document generators."""
    tier = TierResult(4, "Runtime Tests")

    # Create a test markdown file
    test_md = textwrap.dedent("""\
    ---
    title: "Validation Test Document"
    subtitle: "Automated Test"
    client: "Test Client"
    doc_number: "IDEAS/TEST/2026/001"
    cover: true
    font_size: 10
    table_font_size: 8.5
    ---

    ## Test Section

    This is a test document for validation.

    | Column A | Column B | Column C |
    | :--- | :--- | :--- |
    | Data 1 | Data 2 | Data 3 |
    | Data 4 | Data 5 | Data 6 |

    ### Subsection

    - Item one
    - Item two
    - Item three
    """)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as tmp:
        tmp.write(test_md)
        test_md_path = tmp.name

    try:
        # 4.1 Test unified generator — PDF
        for fmt, ext in [("PDF", ".pdf"), ("PPTX", ".pptx"), ("DOCX", ".docx"), ("XLSX", ".xlsx")]:
            with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as out:
                out_path = out.name
            try:
                result = subprocess.run(
                    [sys.executable, str(SCRIPTS_DIR / "generate_document.py"),
                     "--input", test_md_path, "--output", out_path],
                    capture_output=True, text=True, timeout=60, cwd=str(SCRIPTS_DIR)
                )
                success = result.returncode == 0 and os.path.exists(out_path) and os.path.getsize(out_path) > 0
                detail = f"{os.path.getsize(out_path)} bytes" if success else f"Error: {result.stderr[:200]}"
                tier.add(ValidationResult(
                    f"generate_document.py → {fmt}",
                    success,
                    detail
                ))
            except subprocess.TimeoutExpired:
                tier.add(ValidationResult(f"generate_document.py → {fmt}", False, "Timeout (60s)"))
            except Exception as e:
                tier.add(ValidationResult(f"generate_document.py → {fmt}", False, str(e)[:200]))
            finally:
                if os.path.exists(out_path):
                    os.unlink(out_path)

        # 4.2 Test --list-formats
        try:
            result = subprocess.run(
                [sys.executable, str(SCRIPTS_DIR / "generate_document.py"), "--list-formats"],
                capture_output=True, text=True, timeout=10, cwd=str(SCRIPTS_DIR)
            )
            has_all = all(f in result.stdout for f in ["pdf", "pptx", "docx", "xlsx"])
            tier.add(ValidationResult(
                "generate_document.py --list-formats",
                result.returncode == 0 and has_all,
                "All 4 formats available" if has_all else f"Output: {result.stdout[:100]}"
            ))
        except Exception as e:
            tier.add(ValidationResult("generate_document.py --list-formats", False, str(e)[:200]))

        # 4.3 Test estimate_service_cost.py --list-services
        try:
            result = subprocess.run(
                [sys.executable, str(SCRIPTS_DIR / "estimate_service_cost.py"), "--list-services"],
                capture_output=True, text=True, timeout=10, cwd=str(SCRIPTS_DIR)
            )
            tier.add(ValidationResult(
                "estimate_service_cost.py --list-services",
                result.returncode == 0,
                f"OK ({len(result.stdout.split(chr(10)))} lines)" if result.returncode == 0 else f"Error: {result.stderr[:200]}"
            ))
        except Exception as e:
            tier.add(ValidationResult("estimate_service_cost.py --list-services", False, str(e)[:200]))

        # 4.4 Test pricing_engine.py import
        try:
            result = subprocess.run(
                [sys.executable, "-c",
                 "import sys; sys.path.insert(0, '.'); from pricing_engine import get_cost_breakdown, calculate_gov_proposal_pricing; print('OK')"],
                capture_output=True, text=True, timeout=10, cwd=str(SCRIPTS_DIR)
            )
            tier.add(ValidationResult(
                "pricing_engine.py importable",
                result.returncode == 0 and "OK" in result.stdout,
                "Import OK" if result.returncode == 0 else f"Error: {result.stderr[:200]}"
            ))
        except Exception as e:
            tier.add(ValidationResult("pricing_engine.py importable", False, str(e)[:200]))

        # 4.4a SALARY_MASTER, RATE_CARD, ROLE_MULTIPLIER integrity
        try:
            test_code = textwrap.dedent("""\
                import sys, json; sys.path.insert(0, '.')
                from rate_card import RATE_CARD, SALARY_MASTER, ROLE_MULTIPLIER
                rc = set(RATE_CARD.keys())
                sm = set(SALARY_MASTER.keys())
                rm = set(ROLE_MULTIPLIER.keys())
                result = {
                    'rc': len(rc), 'sm': len(sm), 'rm': len(rm),
                    'rc_sm_sync': rc == sm,
                    'rc_rm_sync': rc == rm,
                    'missing_sm': sorted(rc - sm),
                    'missing_rm': sorted(rc - rm),
                }
                # Check SALARY_MASTER structure: all roles must have 'levels' dict with int keys 1-24
                bad_roles = []
                for role in sm:
                    data = SALARY_MASTER[role]
                    # Structure: {"group": str, "category": str, "levels": {1: {...}, 2: {...}, ...}}
                    levels = data.get('levels', data)  # fallback to data itself for flat structure
                    if isinstance(levels, dict):
                        int_keys = {k for k in levels if isinstance(k, int)}
                        expected = set(range(1, 25))
                        if not expected.issubset(int_keys):
                            missing_levels = sorted(expected - int_keys)
                            bad_roles.append(f"{role}(missing:{missing_levels})")
                    else:
                        bad_roles.append(f"{role}(no levels dict)")
                result['bad_structure'] = bad_roles
                print(json.dumps(result))
            """)
            result = subprocess.run(
                [sys.executable, "-c", test_code],
                capture_output=True, text=True, timeout=30, cwd=str(SCRIPTS_DIR)
            )
            if result.returncode == 0:
                data = json.loads(result.stdout.strip())
                # RATE_CARD ↔ SALARY_MASTER sync
                tier.add(ValidationResult(
                    "RATE_CARD ↔ SALARY_MASTER sync",
                    data['rc_sm_sync'],
                    f"RC={data['rc']}, SM={data['sm']}" + (f", missing: {data['missing_sm'][:5]}" if data['missing_sm'] else "")
                ))
                # RATE_CARD ↔ ROLE_MULTIPLIER sync
                tier.add(ValidationResult(
                    "RATE_CARD ↔ ROLE_MULTIPLIER sync",
                    data['rc_rm_sync'],
                    f"RC={data['rc']}, RM={data['rm']}" + (f", missing: {data['missing_rm'][:5]}" if data['missing_rm'] else "")
                ))
                # SALARY_MASTER structure (all roles have int keys 1-24)
                tier.add(ValidationResult(
                    "SALARY_MASTER structure (int keys 1-24)",
                    len(data['bad_structure']) == 0,
                    f"{len(data['bad_structure'])} bad roles" + (f": {data['bad_structure'][:5]}" if data['bad_structure'] else "")
                ))
            else:
                tier.add(ValidationResult("Rate card data integrity", False, f"Error: {result.stderr[:200]}"))
        except Exception as e:
            tier.add(ValidationResult("Rate card data integrity", False, str(e)[:200]))

        # 4.4b Test ROLE_MULTIPLIER applied in get_cost_breakdown
        try:
            test_code = textwrap.dedent("""\
                import sys, json; sys.path.insert(0, '.')
                from pricing_engine import get_cost_breakdown
                # GenAI Specialist has mult=1.22, Data Analyst has mult=1.00
                genai = get_cost_breakdown('GenAI Specialist', 10)
                analyst = get_cost_breakdown('Data Analyst', 10)
                ok = (genai.get('role_multiplier') == 1.22 and
                      analyst.get('role_multiplier') == 1.0 and
                      genai['harga_eksternal_client_price'] > analyst['harga_eksternal_client_price'])
                ratio = genai['harga_eksternal_client_price'] / analyst['harga_eksternal_client_price']
                print(json.dumps({'ok': ok, 'ratio': round(ratio, 3)}))
            """)
            result = subprocess.run(
                [sys.executable, "-c", test_code],
                capture_output=True, text=True, timeout=10, cwd=str(SCRIPTS_DIR)
            )
            if result.returncode == 0:
                data = json.loads(result.stdout.strip())
                tier.add(ValidationResult(
                    "ROLE_MULTIPLIER applied in pricing",
                    data['ok'],
                    f"GenAI/Analyst ratio: {data['ratio']}x (expected >1.2)"
                ))
            else:
                tier.add(ValidationResult("ROLE_MULTIPLIER applied in pricing", False, f"Error: {result.stderr[:200]}"))
        except Exception as e:
            tier.add(ValidationResult("ROLE_MULTIPLIER applied in pricing", False, str(e)[:200]))

        # 4.4c Test role-definitions.md covers all RATE_CARD roles
        try:
            role_defs_path = REFS_DIR / "role-definitions.md"
            if role_defs_path.exists():
                rd_content = read_text(role_defs_path) or ""
                test_code = "import sys, json; sys.path.insert(0, '.'); from rate_card import RATE_CARD; print(json.dumps(sorted(RATE_CARD.keys())))"
                result = subprocess.run(
                    [sys.executable, "-c", test_code],
                    capture_output=True, text=True, timeout=10, cwd=str(SCRIPTS_DIR)
                )
                if result.returncode == 0:
                    all_roles = json.loads(result.stdout.strip())
                    # Use heading-based matching: look for '## Role Name' pattern
                    import re as _re
                    rd_headings = set(_re.findall(r'^## (.+)$', rd_content, _re.MULTILINE))
                    missing_in_defs = [r for r in all_roles if r not in rd_headings]
                    tier.add(ValidationResult(
                        "role-definitions.md covers all RATE_CARD roles",
                        len(missing_in_defs) == 0,
                        f"{len(all_roles) - len(missing_in_defs)}/{len(all_roles)} roles covered" +
                        (f", missing: {missing_in_defs[:5]}" if missing_in_defs else "")
                    ))
            else:
                tier.add(ValidationResult(
                    "role-definitions.md exists",
                    False,
                    "File not found"
                ))
        except Exception as e:
            tier.add(ValidationResult("role-definitions.md coverage", False, str(e)[:200]))

        # 4.5 Test query_spbe.py --top 3
        try:
            result = subprocess.run(
                [sys.executable, str(SCRIPTS_DIR / "query_spbe.py"), "--top", "3"],
                capture_output=True, text=True, timeout=10, cwd=str(SCRIPTS_DIR)
            )
            tier.add(ValidationResult(
                "query_spbe.py --top 3",
                result.returncode == 0,
                "OK" if result.returncode == 0 else f"Error: {result.stderr[:200]}"
            ))
        except Exception as e:
            tier.add(ValidationResult("query_spbe.py --top 3", False, str(e)[:200]))

        # 4.6 Test recommend_service.py
        try:
            result = subprocess.run(
                [sys.executable, str(SCRIPTS_DIR / "recommend_service.py"),
                 "--need", "data management assessment"],
                capture_output=True, text=True, timeout=10, cwd=str(SCRIPTS_DIR)
            )
            tier.add(ValidationResult(
                "recommend_service.py",
                result.returncode == 0,
                "OK" if result.returncode == 0 else f"Error: {result.stderr[:200]}"
            ))
        except Exception as e:
            tier.add(ValidationResult("recommend_service.py", False, str(e)[:200]))

    finally:
        if os.path.exists(test_md_path):
            os.unlink(test_md_path)

    tier.finish()
    return tier


# ---------------------------------------------------------------------------
# Tier 5: Change Impact Analysis
# ---------------------------------------------------------------------------
def tier5_change_impact():
    """Compare against baseline, identify changes."""
    tier = TierResult(5, "Change Impact Analysis")

    current_state = {}
    for f in get_all_files():
        rel = str(f.relative_to(SKILL_DIR))
        current_state[rel] = {
            "hash": file_hash(f),
            "size": f.stat().st_size,
            "mtime": f.stat().st_mtime,
        }

    if not BASELINE_FILE.exists():
        tier.add(ValidationResult(
            "Baseline comparison",
            True,
            "No baseline found. Run with --baseline to create one.",
            severity="info"
        ))
        tier.add(ValidationResult(
            "Current state snapshot",
            True,
            f"{len(current_state)} files tracked"
        ))
        tier.finish()
        return tier

    # Load baseline
    baseline = json.loads(BASELINE_FILE.read_text())
    baseline_files = baseline.get("files", {})
    baseline_version = baseline.get("version", "unknown")

    # Compare
    added = set(current_state.keys()) - set(baseline_files.keys())
    removed = set(baseline_files.keys()) - set(current_state.keys())
    modified = set()
    unchanged = set()

    for rel in set(current_state.keys()) & set(baseline_files.keys()):
        if current_state[rel]["hash"] != baseline_files[rel]["hash"]:
            modified.add(rel)
        else:
            unchanged.add(rel)

    tier.add(ValidationResult(
        f"Baseline comparison (vs {baseline_version})",
        True,
        f"Added={len(added)}, Modified={len(modified)}, Removed={len(removed)}, Unchanged={len(unchanged)}"
    ))

    if added:
        tier.add(ValidationResult("New files", True, ", ".join(sorted(added)), severity="info"))
    if removed:
        tier.add(ValidationResult("Removed files", True, ", ".join(sorted(removed)), severity="warning"))
    if modified:
        tier.add(ValidationResult("Modified files", True, ", ".join(sorted(modified)), severity="info"))

    # Impact analysis: which files reference modified/added files?
    if modified or added:
        affected = set()
        changed_names = set()
        for rel in modified | added:
            name = Path(rel).name
            stem = Path(rel).stem
            changed_names.add(name)
            changed_names.add(stem)

        for f in get_all_files():
            content = read_text(f)
            if content is None:
                continue
            rel = str(f.relative_to(SKILL_DIR))
            if rel in modified or rel in added:
                continue
            for cn in changed_names:
                if cn in content:
                    affected.add(rel)
                    break

        if affected:
            tier.add(ValidationResult(
                "Potentially affected files",
                True,
                f"{len(affected)} files reference changed files: {', '.join(sorted(affected))}",
                severity="info"
            ))

    tier.finish()
    return tier


# ---------------------------------------------------------------------------
# Baseline Management
# ---------------------------------------------------------------------------
def save_baseline():
    """Save current state as baseline."""
    state = {"files": {}, "version": "", "timestamp": datetime.now().isoformat()}

    # Extract version from SKILL.md
    content = read_text(SKILL_MD) or ""
    version_match = re.search(r'v(\d+\.\d+)', content)
    state["version"] = f"v{version_match.group(1)}" if version_match else "unknown"

    for f in get_all_files():
        rel = str(f.relative_to(SKILL_DIR))
        state["files"][rel] = {
            "hash": file_hash(f),
            "size": f.stat().st_size,
            "mtime": f.stat().st_mtime,
        }

    BASELINE_FILE.write_text(json.dumps(state, indent=2))
    print(f"{Colors.PASS}✓{Colors.RESET} Baseline saved: {len(state['files'])} files, version {state['version']}")
    print(f"  File: {BASELINE_FILE}")


# ---------------------------------------------------------------------------
# Report Generation
# ---------------------------------------------------------------------------
def generate_report(tiers, report_path=None):
    """Generate markdown validation report."""
    lines = []
    lines.append(f"# IDEAS Company Skill — Validation Report")
    lines.append(f"")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"")

    # Summary table
    total_checks = sum(len(t.checks) for t in tiers)
    total_pass = sum(1 for t in tiers for c in t.checks if c.passed)
    total_errors = sum(len(t.errors) for t in tiers)
    total_warnings = sum(len(t.warnings) for t in tiers)
    overall = "PASS" if total_errors == 0 else "FAIL"

    lines.append(f"## Summary")
    lines.append(f"")
    lines.append(f"| Metric | Value |")
    lines.append(f"|:---|:---|")
    lines.append(f"| Overall | **{overall}** |")
    lines.append(f"| Total checks | {total_checks} |")
    lines.append(f"| Passed | {total_pass} |")
    lines.append(f"| Errors | {total_errors} |")
    lines.append(f"| Warnings | {total_warnings} |")
    lines.append(f"")

    # Tier details
    for t in tiers:
        status = "PASS" if t.passed else "FAIL"
        lines.append(f"## Tier {t.tier_num}: {t.tier_name} — {status} ({t.duration_ms}ms)")
        lines.append(f"")
        lines.append(f"| Check | Status | Detail |")
        lines.append(f"|:---|:---|:---|")
        for c in t.checks:
            s = "PASS" if c.passed else ("WARN" if c.severity == "warning" else "FAIL")
            detail = c.detail.replace("|", "\\|") if c.detail else ""
            lines.append(f"| {c.name} | {s} | {detail} |")
        lines.append(f"")

    report_text = "\n".join(lines)

    if report_path:
        Path(report_path).write_text(report_text)
        print(f"\n{Colors.INFO}📄 Report saved: {report_path}{Colors.RESET}")

    return report_text


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="IDEAS Company Skill — Comprehensive Multi-Tier Validation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
        Tiers:
          1  Quick Check      — SKILL.md format, YAML, line count
          2  Structural Audit — File inventory, compile, counts
          3  Dependency Sync  — Cross-refs, orphans, branding, service codes
          4  Runtime Tests    — Execute scripts, test generators
          5  Change Impact    — Compare against baseline, affected files
        """)
    )
    parser.add_argument("--tier", type=int, default=5, choices=[1, 2, 3, 4, 5],
                        help="Run up to this tier (default: 5 = all)")
    parser.add_argument("--report", type=str, default=None,
                        help="Save report to markdown file")
    parser.add_argument("--baseline", action="store_true",
                        help="Save current state as baseline for future comparisons")
    parser.add_argument("--diff", action="store_true",
                        help="Show changes since last baseline")
    parser.add_argument("--json", action="store_true",
                        help="Output results as JSON")

    args = parser.parse_args()

    if args.baseline:
        save_baseline()
        return

    # Header
    print(f"\n{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    print(f"{Colors.BOLD}  IDEAS COMPANY SKILL — MULTI-TIER VALIDATION{Colors.RESET}")
    print(f"{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    print(f"  Skill dir: {SKILL_DIR}")
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Max tier:  {args.tier}")

    tier_funcs = [
        (1, tier1_quick_check),
        (2, tier2_structural_audit),
        (3, tier3_dependency_sync),
        (4, tier4_runtime_tests),
        (5, tier5_change_impact),
    ]

    tiers = []
    overall_pass = True

    for tier_num, tier_func in tier_funcs:
        if tier_num > args.tier:
            break

        print(f"\n{Colors.BOLD}{'─' * 70}{Colors.RESET}")
        print(f"{Colors.BOLD}  TIER {tier_num}: {tier_func.__doc__.strip().split(chr(10))[0]}{Colors.RESET}")
        print(f"{Colors.BOLD}{'─' * 70}{Colors.RESET}")

        tier_result = tier_func()
        tiers.append(tier_result)

        for check in tier_result.checks:
            print(str(check))

        status_color = Colors.PASS if tier_result.passed else Colors.FAIL
        status_text = "PASS" if tier_result.passed else "FAIL"
        print(f"\n  {status_color}{Colors.BOLD}Tier {tier_num}: {status_text}{Colors.RESET} "
              f"{Colors.DIM}({tier_result.duration_ms}ms, "
              f"{len(tier_result.errors)} errors, {len(tier_result.warnings)} warnings){Colors.RESET}")

        if not tier_result.passed:
            overall_pass = False

    # Overall summary
    total_checks = sum(len(t.checks) for t in tiers)
    total_pass = sum(1 for t in tiers for c in t.checks if c.passed)
    total_errors = sum(len(t.errors) for t in tiers)
    total_warnings = sum(len(t.warnings) for t in tiers)

    print(f"\n{Colors.BOLD}{'=' * 70}{Colors.RESET}")
    overall_color = Colors.PASS if overall_pass else Colors.FAIL
    overall_text = "PASS" if overall_pass else "FAIL"
    print(f"  {overall_color}{Colors.BOLD}OVERALL: {overall_text}{Colors.RESET}")
    print(f"  Checks: {total_pass}/{total_checks} passed, {total_errors} errors, {total_warnings} warnings")
    print(f"{Colors.BOLD}{'=' * 70}{Colors.RESET}\n")

    # Generate report if requested
    if args.report:
        generate_report(tiers, args.report)

    # JSON output
    if args.json:
        json_result = {
            "overall": overall_text,
            "timestamp": datetime.now().isoformat(),
            "tiers": []
        }
        for t in tiers:
            json_result["tiers"].append({
                "tier": t.tier_num,
                "name": t.tier_name,
                "passed": t.passed,
                "duration_ms": t.duration_ms,
                "checks": [
                    {"name": c.name, "passed": c.passed, "detail": c.detail, "severity": c.severity}
                    for c in t.checks
                ]
            })
        print(json.dumps(json_result, indent=2))

    sys.exit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
