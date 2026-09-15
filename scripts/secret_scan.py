#!/usr/bin/env python3
# secret-scan: allow-file
"""Scan text for credentials and personal IDs before they reach git, the wiki, or memory.

Usage:
  secret_scan.py FILE...              scan files; prints "path:line: KIND" (never the value)
  secret_scan.py --stdin [--name N]   scan stdin
  secret_scan.py --git-staged         scan staged blobs of the repo in the current directory
  secret_scan.py --selftest           run built-in checks
  --baseline FILE                     suppress findings whose fingerprint is listed in FILE
  --write-baseline FILE               write current findings as a baseline (only after human review)
  --redact FILE...                    replace secret values in place with <REDACTED>; prints counts only

Exit codes: 0 clean, 1 findings, 2 usage or runtime error.
Files whose first 5 lines contain the allow-file pragma are skipped (this file carries it).
Compatible with /usr/bin/python3 (3.9).
"""
import hashlib
import re
import subprocess
import sys

MAX_BYTES = 5 * 1024 * 1024
PRAGMA = "secret-scan: allow-file"

PLACEHOLDER_PREFIXES = ("$", "<", "{", "%", "*", "your_", "your-", "xxx", "os.environ", "process.env",
                        "env.", "getenv", "settings.", "config.", "self.")
PLACEHOLDER_WORDS = {"password", "changeme", "example", "redacted", "masked", "none", "null",
                     "true", "false", "secret", "placeholder"}


def _looks_like_placeholder(value):
    v = value.strip().strip("'\"")
    low = v.lower()
    if not v or low in PLACEHOLDER_WORDS or low.startswith(PLACEHOLDER_PREFIXES):
        return True
    if v.startswith(("~/", "/", "./")):             # file paths
        return True
    if "(" in v or "[" in v or "]" in v or "${" in v or "***" in v:
        return True
    if re.fullmatch(r"\d+", v):                      # plain numbers are not credentials
        return True
    if re.fullmatch(r"[A-Za-z_][A-Za-z_.\-]*", v):   # identifiers without digits: variable refs
        return True
    return False


DSN_PLACEHOLDERS = {"password", "pass", "pwd", "passwd", "changeme", "secret", "xxx", "placeholder"}


def _dsn_ok(m):
    # Only explicit placeholders are skipped: a plain word in the password slot is still a password.
    v = m.group(1)
    return not (v.lower() in DSN_PLACEHOLDERS or v.startswith(("$", "<", "{", "%(", "*")) or set(v) == {"x"})


def _assign_ok(m):
    return not _looks_like_placeholder(m.group(1))


# (kind, regex, validator or None)
PATTERNS = [
    ("DSN_WITH_PASSWORD",
     re.compile(r"\b[a-z][a-z0-9+.\-]{1,20}://[^\s:/@'\"<>\\]*:([^\s@'\"<>\\]+)@[^\s'\"<>\\]+"), _dsn_ok),
    ("SECRET_ASSIGNMENT",
     re.compile(r"(?i)\b[A-Z0-9_\-]*(?:PASSWORD|PASSWD|PASWORD|PWD|SECRET|TOKEN|API[_\-]?KEY|"
                r"ACCESS[_\-]?KEY|PRIVATE[_\-]?KEY|PAT)(?:[_\-]?VALUE)?\\?[\"']?\s*[:=]\s*\\?[\"']?([^\s\"'#,;)\\]{8,})"), _assign_ok),
    ("AUTH_HEADER",
     re.compile(r"(?i)\bauthorization[\"']?\s*[:=]\s*[\"']?(?:bearer|basic|token)\s+([A-Za-z0-9._~+/=\-]{16,})"),
     _assign_ok),
    ("PRIVATE_KEY", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), None),
    ("AWS_ACCESS_KEY", re.compile(r"\bAKIA[0-9A-Z]{16}\b"), None),
    ("GITHUB_TOKEN", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{22,})"), None),
    ("GITLAB_TOKEN", re.compile(r"\bglpat-[A-Za-z0-9_\-]{20,}"), None),
    ("SLACK_TOKEN", re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"), None),
    ("ANTHROPIC_OR_OPENAI_KEY", re.compile(r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_\-]{20,}"), None),
    ("GOOGLE_API_KEY", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"), None),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"), None),
    # Indonesian NIK: province, regency, district, birth day (+40 for women), month, year, serial.
    ("NIK",
     re.compile(r"(?<![\d.])(?:1[1-9]|[2-8][0-9]|9[0-4])(?:0[1-9]|[1-9][0-9])(?:0[1-9]|[1-9][0-9])"
                r"(?:0[1-9]|[12][0-9]|3[01]|4[1-9]|[56][0-9]|7[01])(?:0[1-9]|1[0-2])[0-9]{2}"
                r"(?:000[1-9]|00[1-9][0-9]|0[1-9][0-9]{2}|[1-9][0-9]{3})(?!\d|\.\d)"), None),
]


def scan_lines(text):
    """Yield (line_number, kind, line). Callers must never print `line`."""
    for lineno, line in enumerate(text.splitlines(), 1):
        for kind, rx, ok in PATTERNS:
            for m in rx.finditer(line):
                if ok is None or ok(m):
                    yield lineno, kind, line
                    break


def scan_text(text):
    """Return a list of (line_number, kind). Values are never returned."""
    return [(n, k) for n, k, _ in scan_lines(text)]


REDACTION = "<REDACTED>"


def redact_text(text):
    """Return (new_text, count). Validated patterns redact their captured value, others the whole match."""
    out, count = [], 0
    for line in text.split("\n"):
        for kind, rx, ok in PATTERNS:
            def repl(m):
                nonlocal count
                if ok is not None and not ok(m):
                    return m.group(0)
                count += 1
                if m.groups() and m.group(1):
                    start, end = m.span(1)
                    base = m.start(0)
                    return m.group(0)[: start - base] + REDACTION + m.group(0)[end - base:]
                return REDACTION
            line = rx.sub(repl, line)
        out.append(line)
    return "\n".join(out), count


def fingerprint(name, kind, line):
    raw = "%s\0%s\0%s" % (name, kind, line.strip())
    return hashlib.sha256(raw.encode("utf-8", errors="replace")).hexdigest()[:20]


def load_baseline(path):
    known = set()
    with open(path, encoding="utf-8") as fh:
        for row in fh:
            row = row.strip()
            if row and not row.startswith("#"):
                known.add(row.split()[0])
    return known


def _decode(data):
    if b"\0" in data[:8192] or len(data) > MAX_BYTES:
        return None
    text = data.decode("utf-8", errors="replace")
    if PRAGMA in "\n".join(text.splitlines()[:5]):
        return None
    return text


def _report(name, data, known=frozenset(), collect=None):
    text = _decode(data)
    if text is None:
        return 0
    count = 0
    for lineno, kind, line in scan_lines(text):
        fp = fingerprint(name, kind, line)
        if fp in known:
            continue
        if collect is not None:
            collect.append("%s  %s  %s" % (fp, name, kind))
        print("%s:%d: %s" % (name, lineno, kind))
        count += 1
    return count


def _staged_paths():
    out = subprocess.run(["git", "diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR"],
                         check=True, capture_output=True).stdout
    return [p for p in out.decode("utf-8", errors="replace").split("\0") if p]


def selftest():
    def kinds(s):
        return {k for _, k in scan_text(s)}
    pw = "Ab3" + "xY9zQ"
    assert kinds("postgresql://kpm_data:" + pw + "@10.0.0.1:5432/db") >= {"DSN_WITH_PASSWORD"}
    assert kinds("postgresql://u:${PW}@host/db") == set()
    assert kinds("postgresql://u:***@host/db") == set()
    assert kinds("MDM_DB_PAS" + "WORD=" + "BGf" + "iZjBAu213") == {"SECRET_ASSIGNMENT"}
    assert kinds('password=_require_env("PUSDATIN_PASSWORD")') == set()
    assert kinds("password: self.db_password") == set()
    assert kinds('"apiKey": "' + "k9" + "Zx4mQ7wLp2" + '"') == {"SECRET_ASSIGNMENT"}
    assert kinds("max_tokens: 4096") == set()
    assert kinds("gh" + "p_" + "a" * 36) == {"GITHUB_TOKEN"}
    assert kinds("-----BEGIN " + "RSA PRIVATE KEY-----") == {"PRIVATE_KEY"}
    assert kinds("nik " + "3276" + "0145" + "0890" + "0012") == {"NIK"}
    assert kinds("id 1234567890123456") == set()          # day 78 is not a valid NIK birth day
    assert kinds("ts 1726372800000 and no secrets here") == set()
    assert _decode(b"# " + PRAGMA.encode() + b"\npassword=Zz9" + b"yy88xx") is None
    assert kinds("postgresql://admin:" + "local" + "@localhost:5432/localdb") == {"DSN_WITH_PASSWORD"}
    assert kinds("postgresql://user:password@localhost/db") == set()
    assert kinds('"PAT_VALUE": "' + "q7" + "Lk2mZ9xR4t" + '"') == {"SECRET_ASSIGNMENT"}
    assert kinds('"Authorization": "Bearer ' + "PMAK-" + "5f2a" + "9c1d7e3b4a6f8e2d" + '"') >= {"AUTH_HEADER"}
    assert kinds('"GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"') == set()
    assert kinds('"OPENAI_API_KEY": "your-api-key"') == set()
    assert kinds('"frame_duration_ms_p99": 2.' + "3276014508900012" + ",") == set()
    assert kinds("Obsidian REST API (port 27123, token: ~/.claude/.obsidian-token)") == set()
    assert kinds('let apiKey = ProcessInfo.processInfo.environment["API_KEY"]') == set()
    line = "password=" + "Qw8" + "rty55Zx"
    fp = fingerprint("docs/x.md", "SECRET_ASSIGNMENT", line)
    assert _report("docs/x.md", line.encode(), frozenset([fp])) == 0
    assert _report("docs/x.md", (line + "9").encode(), frozenset([fp])) == 1
    dirty = "a postgresql://svc:" + "Zx9" + "fake7Qq" + "@db.example.invalid/app b\nMDM_DB_PAS" + "WORD=" + "BGf" + "iZjBAu213\n" + "gh" + "p_" + "b" * 36
    clean, n = redact_text(dirty)
    assert n == 3 and scan_text(clean) == [] and "db.example.invalid" in clean and "MDM_DB_PAS" in clean, (n, clean)
    import json as _json
    embedded = _json.dumps({"display": 'use \"-e POSTGRES_PASSWORD=password\" on docker run'})
    assert scan_text(embedded) == []                                   # placeholder inside JSON escapes
    real = _json.dumps({"display": 'set \"DB_PASSWORD=' + "Qw8" + 'rty55Zx\" now'})
    red, n = redact_text(real)
    assert n == 1 and _json.loads(red) and scan_text(red) == [], red   # escape survives redaction
    print("selftest OK (%d patterns)" % len(PATTERNS))
    return 0


def main(argv):
    if not argv:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    if argv[0] == "--selftest":
        return selftest()
    total = 0
    known, collect, write_to = frozenset(), None, None
    try:
        if "--baseline" in argv:
            i = argv.index("--baseline")
            known = frozenset(load_baseline(argv[i + 1]))
            argv = argv[:i] + argv[i + 2:]
        if "--write-baseline" in argv:
            i = argv.index("--write-baseline")
            write_to, collect = argv[i + 1], []
            argv = argv[:i] + argv[i + 2:]
        if argv[0] == "--redact":
            for path in argv[1:]:
                with open(path, "rb") as fh:
                    text = _decode(fh.read())
                if text is None:
                    continue
                new, n = redact_text(text)
                if n:
                    with open(path, "w", encoding="utf-8") as fh:
                        fh.write(new)
                    print("%s: %d redacted" % (path, n))
            return 0
        if argv[0] == "--stdin":
            name = argv[argv.index("--name") + 1] if "--name" in argv else "<stdin>"
            total = _report(name, sys.stdin.buffer.read(), known, collect)
        elif argv[0] == "--git-staged":
            for path in _staged_paths():
                blob = subprocess.run(["git", "show", ":" + path], check=True, capture_output=True).stdout
                total += _report(path, blob, known, collect)
        else:
            for path in argv:
                with open(path, "rb") as fh:
                    total += _report(path, fh.read(), known, collect)
    except (OSError, subprocess.CalledProcessError, ValueError, IndexError) as exc:
        print("secret_scan: %s" % exc, file=sys.stderr)
        return 2
    if write_to is not None:
        with open(write_to, "w", encoding="utf-8") as fh:
            fh.write("# secret_scan baseline: reviewed example credentials in vendor docs.\n"
                     "# format: fingerprint  path  kind. Values are never stored.\n")
            fh.write("\n".join(sorted(collect)) + ("\n" if collect else ""))
        print("baseline written: %d entries -> %s" % (len(collect), write_to), file=sys.stderr)
        return 0
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
