#!/usr/bin/env python3
"""Validate gx_data_quality table config(s) OFFLINE — no network, no DB, no OpenMetadata.

Why this exists: the two ways a new config quietly breaks a run are (1) a malformed YAML
(missing fqn, no checks, a duplicate name) and (2) a check whose `expectation` isn't mapped
in src/om.py BUILTIN_DEFINITIONS (which crashes with a KeyError partway through the run).
Catch both here, before anything touches the database or the catalog.

It reads the repo's own src/om.py (via AST, so it does NOT import requests or connect to
anything) to learn exactly which expectations that repo supports — so it stays correct even
after you add a new mapping.

Usage:
    python validate_config.py <repo-root> <config.yaml> [<config2.yaml> ...]
    python validate_config.py <repo-root> --all        # every config/tables/*.yaml

Exit code 0 = all good, 1 = problems found.
"""
import ast
import glob
import os
import sys

# Recipes handled by runner.py that don't name a GX class directly but DO resolve to a
# mapped built-in inside om.py. Keep in sync with runner._build_expectation.
RECIPE_EXPECTATIONS = {"not_in_future"}


def load_builtin_defs(repo_root):
    """Return {expectation_name: level} parsed from src/om.py without importing it."""
    om_path = os.path.join(repo_root, "src", "om.py")
    if not os.path.exists(om_path):
        sys.exit(f"ERROR: {om_path} not found — is <repo-root> correct? "
                 f"Point it at the folder that contains src/om.py.")
    tree = ast.parse(open(om_path).read())
    defs = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            if any(isinstance(t, ast.Name) and t.id == "BUILTIN_DEFINITIONS" for t in node.targets):
                for k, v in zip(node.value.keys, node.value.values):
                    if isinstance(k, ast.Constant):
                        level = None
                        if isinstance(v, ast.Dict):
                            for vk, vv in zip(v.keys, v.values):
                                if (isinstance(vk, ast.Constant) and vk.value == "level"
                                        and isinstance(vv, ast.Constant)):
                                    level = vv.value
                        defs[k.value] = level
    if not defs:
        sys.exit("ERROR: could not find BUILTIN_DEFINITIONS in src/om.py.")
    return defs


def validate_file(path, defs):
    import yaml
    problems = []
    if not os.path.exists(path):
        return None, [], [f"file not found: {path}"]
    cfg = yaml.safe_load(open(path)) or {}
    tbl = cfg.get("table", {}) or {}
    for field in ("source", "schema", "name", "fqn"):
        if not tbl.get(field):
            problems.append(f"table.{field} is missing")
    if not cfg.get("columns_needed"):
        problems.append("columns_needed is missing or empty")
    checks = cfg.get("checks") or []
    if not checks:
        problems.append("no checks defined")
    seen = set()
    for i, c in enumerate(checks):
        nm = c.get("name")
        if not nm:
            problems.append(f"check[{i}] has no name")
            continue
        if nm in seen:
            problems.append(f"duplicate check name '{nm}'")
        seen.add(nm)
        exp = c.get("expectation")
        if not exp:
            problems.append(f"check '{nm}' has no expectation")
            continue
        if exp not in defs and exp not in RECIPE_EXPECTATIONS:
            problems.append(
                f"check '{nm}': expectation '{exp}' is NOT in BUILTIN_DEFINITIONS "
                f"— add a mapping in src/om.py (see derive-rules.md) or fix the name")
        if "value_set_from" in c:
            ref = c["value_set_from"] or {}
            if not ref.get("source") or not ref.get("query"):
                problems.append(f"check '{nm}': value_set_from needs both 'source' and 'query'")
    return cfg, checks, problems


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    repo = sys.argv[1]
    if sys.argv[2] == "--all":
        paths = sorted(glob.glob(os.path.join(repo, "config", "tables", "*.yaml")))
        if not paths:
            sys.exit(f"No configs found in {os.path.join(repo, 'config', 'tables')}")
    else:
        paths = sys.argv[2:]

    defs = load_builtin_defs(repo)
    print(f"Loaded {len(defs)} expectation mappings from src/om.py\n")

    total_problems = 0
    for p in paths:
        cfg, checks, problems = validate_file(p, defs)
        name = os.path.basename(p)
        if problems:
            total_problems += len(problems)
            print(f"✗ {name}")
            for pr in problems:
                print(f"    - {pr}")
        else:
            print(f"✓ {name}  ({len(checks)} checks, all mapped)")
            for c in checks:
                lvl = defs.get(c["expectation"],
                               "COLUMN" if c["expectation"] in RECIPE_EXPECTATIONS else "?")
                print(f"      {c['name']:38s} {c['expectation']:44s} [{lvl}]")
    print()
    if total_problems:
        print(f"FAIL: {total_problems} problem(s) found.")
        sys.exit(1)
    print("OK: all configs valid and every expectation is mapped.")
    sys.exit(0)


if __name__ == "__main__":
    main()
