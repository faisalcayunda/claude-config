#!/usr/bin/env python3
"""One-line wiki scorecard for the SessionStart drift check (decisions Q15, Q24, Q27).

Prints: pages injected and read in the last 7 days, drafts (and drafts older than 30 days),
last wiki commit, secret findings in wiki and memory files, and the size of startup injections
that sit outside the ~2,000-token budget (ponytail plugin, the project's MEMORY.md).
Adds a WARN line when the wiki has had no commit for more than 14 days despite recent sessions.
Never prints secret values or prompt text. Compatible with /usr/bin/python3 (3.9).
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys

HOME = "/Users/isal/.claude"
WIKI = HOME + "/wiki"
USAGE_LOG = HOME + "/metrics/wiki-usage.jsonl"
CACHE = HOME + "/cache/scorecard-plugin-sizes.json"
PONYTAIL_GLOB_ROOT = HOME + "/plugins/cache/ponytail/ponytail"
sys.path.insert(0, HOME + "/hooks")
sys.path.insert(0, HOME + "/scripts")


def _parse_ts(s):
    try:
        return dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z")
    except (TypeError, ValueError):
        return None


def usage(now, log_path=USAGE_LOG):
    injected, reads, sessions, recent_sessions = 0, 0, set(), set()
    try:
        with open(log_path, encoding="utf-8") as fh:
            for line in fh:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                ts = _parse_ts(rec.get("ts"))
                if not ts:
                    continue
                age = (now - ts).total_seconds() / 86400
                if rec.get("event") in ("inject", "no_match") and age <= 14:
                    recent_sessions.add(rec.get("session"))
                if age > 7:
                    continue
                if rec.get("event") == "inject":
                    injected += len(rec.get("hits") or [])
                    sessions.add(rec.get("session"))
                elif rec.get("event") == "read":
                    reads += 1
    except OSError:
        pass
    return injected, len(sessions), reads, len(recent_sessions)


def drafts(today, wiki=WIKI):
    import wiki_hooks
    total, stale = 0, 0
    for dp, dn, fn in os.walk(wiki):
        dn[:] = [d for d in dn if not d.startswith(".") and d != "templates"]
        for f in fn:
            if not f.endswith(".md"):
                continue
            try:
                with open(os.path.join(dp, f), encoding="utf-8", errors="replace") as fh:
                    fm = wiki_hooks.parse_frontmatter(fh.read(20000))
            except OSError:
                continue
            if fm.get("status") != "draft":
                continue
            total += 1
            stamp = str(fm.get("updated") or fm.get("created") or "")
            try:
                if (today - dt.date.fromisoformat(stamp[:10])).days > 30:
                    stale += 1
            except ValueError:
                pass
    return total, stale


def last_commit_date(wiki=WIKI):
    try:
        out = subprocess.run(["git", "-C", wiki, "log", "-1", "--format=%cs"],
                             capture_output=True, text=True, timeout=3).stdout.strip()
        return dt.date.fromisoformat(out) if out else None
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def secret_findings():
    import secret_scan
    count = 0
    roots = [WIKI, HOME + "/projects"]
    for root in roots:
        for dp, dn, fn in os.walk(root):
            dn[:] = [d for d in dn if d != ".git"]
            if root.endswith("projects") and "/memory" not in dp:
                continue
            for f in fn:
                if f.endswith(".md"):
                    try:
                        with open(os.path.join(dp, f), "rb") as fh:
                            text = secret_scan._decode(fh.read())
                    except OSError:
                        continue
                    if text:
                        count += len(secret_scan.scan_text(text))
    return count


def ponytail_kb():
    scripts = []
    for dp, dn, fn in os.walk(PONYTAIL_GLOB_ROOT):
        if "node_modules" in dp:
            continue
        if "ponytail-activate.js" in fn:
            scripts.append(os.path.join(dp, "ponytail-activate.js"))
    if not scripts:
        return None
    script = sorted(scripts)[-1]
    key = "%s:%d" % (script, int(os.stat(script).st_mtime))
    try:
        cache = json.load(open(CACHE))
    except (OSError, ValueError):
        cache = {}
    if key not in cache:
        try:
            env = dict(os.environ, CLAUDE_PLUGIN_ROOT=os.path.dirname(os.path.dirname(script)))
            out = subprocess.run(["node", script], capture_output=True, timeout=5, env=env, input=b"{}").stdout
            cache = {key: round(len(out) / 1024, 1)}
            os.makedirs(os.path.dirname(CACHE), exist_ok=True)
            json.dump(cache, open(CACHE, "w"))
        except (OSError, subprocess.SubprocessError):
            return None
    return cache.get(key)


def memory_kb(cwd):
    name = re.sub(r"[^A-Za-z0-9]", "-", cwd)
    p = os.path.join(HOME, "projects", name, "memory", "MEMORY.md")
    return round(os.path.getsize(p) / 1024, 1) if os.path.exists(p) else 0.0


def render(inj, sess, reads, recent, d_total, d_stale, last, today, secrets, pony, mem):
    age = (today - last).days if last else None
    parts = [
        "7d injected %d pages in %d sessions, read %d" % (inj, sess, reads),
        "drafts %d (%d >30d)" % (d_total, d_stale),
        "last wiki commit %s" % ("%s (%dd)" % (last.isoformat(), age) if last else "none"),
        "secrets in wiki/memory %d" % secrets,
        "outside budget: ponytail %s, MEMORY.md %sKB" % ("%sKB" % pony if pony is not None else "n/a", mem),
    ]
    lines = ["wiki scorecard: " + " | ".join(parts)]
    if age is not None and age > 14 and recent > 0:
        lines.append("WARN: no wiki commit for %d days despite %d sessions in the last 14 days" % (age, recent))
    if secrets:
        lines.append("WARN: %d secret finding(s) in wiki or memory files; run scripts/secret_scan.py" % secrets)
    return "\n".join(lines)


def selftest():
    import tempfile
    tmp = tempfile.mkdtemp()
    now = dt.datetime(2026, 9, 15, 12, 0, tzinfo=dt.timezone(dt.timedelta(hours=7)))
    log = os.path.join(tmp, "u.jsonl")
    with open(log, "w") as fh:
        for rec in [{"ts": "2026-09-15T10:00:00+0700", "event": "inject", "session": "a", "hits": [{}, {}]},
                    {"ts": "2026-09-14T10:00:00+0700", "event": "read", "session": "a"},
                    {"ts": "2026-09-01T10:00:00+0700", "event": "inject", "session": "old", "hits": [{}]},
                    {"ts": "2026-09-10T10:00:00+0700", "event": "no_match", "session": "b"}]:
            fh.write(json.dumps(rec) + "\n")
    assert usage(now, log) == (2, 1, 1, 2), usage(now, log)
    text = render(2, 1, 1, 2, 3, 1, dt.date(2026, 8, 20), now.date(), 0, 5.2, 1.4)
    assert text.startswith("wiki scorecard: 7d injected 2 pages") and "WARN: no wiki commit for 26 days" in text, text
    assert "WARN" not in render(0, 0, 0, 0, 0, 0, now.date(), now.date(), 0, None, 0.0)
    print("selftest OK")
    return 0


def main(argv):
    if argv[:1] == ["selftest"]:
        return selftest()
    try:
        now = dt.datetime.now().astimezone()
        today = now.date()
        inj, sess, reads, recent = usage(now)
        d_total, d_stale = drafts(today)
        print(render(inj, sess, reads, recent, d_total, d_stale, last_commit_date(), today,
                     secret_findings(), ponytail_kb(), memory_kb(os.getcwd())))
    except Exception as exc:                       # the scorecard must never break session start
        print("wiki scorecard: unavailable (%s)" % type(exc).__name__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
