#!/usr/bin/env python3
"""Wiki retrieval hooks for Claude Code (Phase 2 of the context consolidation plan).

Subcommands (hook JSON arrives on stdin):
  retrieve   UserPromptSubmit: inject up to 3 relevant wiki pages (title, path, description)
  subagent   SubagentStart: inject the main session's latest hits plus a wiki pointer
  read-log   PostToolUse(Read): log reads of wiki pages for the scorecard
  index      rebuild the retrieval index now (no stdin)
  selftest   run built-in checks

Design notes:
- Reads wiki files directly; Obsidian does not need to be running.
- Never logs prompt text (prompts can hold secrets). Logs only page paths and scores.
- Any failure exits 0 silently so a prompt is never blocked.
- Compatible with /usr/bin/python3 (3.9), no third-party packages.
"""
import json
import os
import re
import sys
import tempfile
import time

WIKI_ROOT = "/Users/isal/.claude/wiki"
CACHE_DIR = "/Users/isal/.claude/cache/wiki-retrieval"
INDEX_PATH = "/Users/isal/.claude/cache/wiki-retrieval-index.json"
USAGE_LOG = "/Users/isal/.claude/metrics/wiki-usage.jsonl"

MAX_HITS = 3
MIN_SCORE = 6.0
MAX_CONTEXT_CHARS = 6000        # hook output cap is 10,000 chars; budget ~1,500 tokens
MAX_DESC_CHARS = 300
SESSION_TTL_SECONDS = 7 * 24 * 3600

SKIP_DIRS = {".obsidian", ".git", ".trash", "templates", "hubs", "log"}
NAV_PAGES = {"index.md", "log.md", "hot.md", "_index.md"}
ORG_BY_FOLDER = {"bgn": "BGN", "ideas": "IDEAS", "jds": "JDS", "trikintech": "Trikintech"}

# Short acknowledgements never trigger retrieval (extends wave0-enforce.py's list).
CONTINUATIONS = {
    "ya", "iya", "ok", "oke", "okay", "sip", "siap", "yes", "y", "lanjut", "lanjutkan",
    "teruskan", "gas", "proceed", "go", "next", "no", "ngga", "nggak", "gak", "tidak",
    "batal", "stop", "abort", "noted", "thanks", "thx", "makasih", "ty", "done",
    "setuju", "semua", "mantap", "betul", "benar", "boleh", "silakan", "continue",
}
STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "into", "what", "how", "why", "when",
    "where", "which", "are", "was", "were", "you", "your", "can", "does", "not", "all", "any",
    "please", "check", "wiki", "page", "data", "yang", "dan", "dari", "untuk", "dengan", "ini",
    "itu", "ada", "apa", "bagaimana", "gimana", "kenapa", "saja", "aja", "juga", "sudah",
    "udah", "belum", "bisa", "akan", "atau", "kalau", "kalo", "jadi", "pada", "dalam", "oleh",
    "lagi", "mau", "kamu", "saya", "aku", "nya", "dong", "sih", "deh", "cek", "tolong",
    "mohon", "buat", "bikin", "tahu", "cara", "coba", "terkait", "tentang", "sama",
}
TOKEN_RX = re.compile(r"[a-z0-9_]+")


# ---------------------------------------------------------------- frontmatter
def _unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def _strip_comment(v):
    v = v.strip()
    if v and v[0] in "\"'":                      # empty string is "in" every string
        end = v.find(v[0], 1)
        return v[: end + 1] if end > 0 else v
    return v.split(" #", 1)[0].strip()


def _split_inline(inner):
    items, buf, quote = [], "", None
    for ch in inner:
        if quote:
            buf += ch
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            buf += ch
        elif ch == ",":
            items.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        items.append(buf)
    return [_unquote(i) for i in items if i.strip()]


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    data, key = {}, None
    for raw in text[3:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w\-]*):\s*(.*)$", raw)
        if m and raw[:1] not in (" ", "\t", "-"):
            key, val = m.group(1), _strip_comment(m.group(2))
            if val == "":
                data[key] = []
            elif val.startswith("[") and val.endswith("]"):
                data[key] = _split_inline(val[1:-1])
            else:
                data[key] = _unquote(val)
        elif key and re.match(r"^\s*-\s+", raw):
            item = _unquote(_strip_comment(re.sub(r"^\s*-\s+", "", raw)))
            if not isinstance(data.get(key), list):
                data[key] = [] if data.get(key) in (None, "") else [data[key]]
            data[key].append(item)
    return data


def _as_list(v):
    if v is None or v == "":
        return []
    return v if isinstance(v, list) else [v]


# ---------------------------------------------------------------- index
def tokens(text):
    return [t for t in TOKEN_RX.findall(text.lower()) if len(t) >= 3 and t not in STOPWORDS]


def _page_files(root):
    for dp, dn, fn in os.walk(root):
        rel_dir = os.path.relpath(dp, root)
        dn[:] = [d for d in dn if d not in SKIP_DIRS and not d.startswith(".")]
        if rel_dir != "." and rel_dir.split(os.sep)[0] in SKIP_DIRS:
            continue
        for f in fn:
            if f.endswith(".md") and f not in NAV_PAGES:
                yield os.path.join(dp, f)


def build_index(root=WIKI_ROOT):
    pages = []
    for path in _page_files(root):
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                fm = parse_frontmatter(fh.read(20000))
        except OSError:
            continue
        stem = os.path.splitext(os.path.basename(path))[0]
        pages.append({
            "path": path,
            "title": str(fm.get("title") or stem),
            "aliases": [str(a) for a in _as_list(fm.get("aliases"))],
            "tags": [str(t) for t in _as_list(fm.get("tags"))],
            "org": str(fm.get("org") or ""),
            "status": str(fm.get("status") or ""),
            "type": str(fm.get("type") or ""),
            "description": str(fm.get("description") or "")[:MAX_DESC_CHARS],
        })
    return {"built_at": time.time(), "root": root, "pages": pages}


def _newest_mtime(root):
    newest = 0.0
    for path in _page_files(root):
        try:
            newest = max(newest, os.stat(path).st_mtime)
        except OSError:
            pass
    return newest


def load_index(root=WIKI_ROOT, index_path=INDEX_PATH):
    try:
        with open(index_path, encoding="utf-8") as fh:
            idx = json.load(fh)
        if idx.get("root") == root and idx.get("built_at", 0) >= _newest_mtime(root):
            return idx
    except (OSError, ValueError):
        pass
    idx = build_index(root)
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    tmp = index_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(idx, fh)
    os.replace(tmp, index_path)
    return idx


# ---------------------------------------------------------------- scoring
def is_continuation(prompt):
    low = prompt.strip().lower()
    words = re.findall(r"[a-z]+", low)
    if not words:
        return True
    return low in CONTINUATIONS or (len(words) <= 4 and all(w in CONTINUATIONS for w in words))


def org_from_cwd(cwd):
    m = re.search(r"/Organizations/([^/]+)", cwd or "")
    return ORG_BY_FOLDER.get(m.group(1).lower()) if m else None


def score_page(page, prompt_low, prompt_tokens, cwd_org):
    title_alias = set(tokens(page["title"] + " " + " ".join(page["aliases"])))
    tag_t = set(tokens(" ".join(page["tags"]).replace("/", " ").replace("-", " ")))
    desc_t = set(tokens(page["description"]))
    score, matched, phrase = 0.0, 0, False
    for t in set(prompt_tokens):
        w = 3 if t in title_alias else 2 if t in tag_t else 1 if t in desc_t else 0
        if w:
            score += w
            matched += 1
    for phrase_text in [page["title"]] + page["aliases"]:
        p = phrase_text.strip().lower()
        if len(p) >= 6 and p in prompt_low:
            score += 6
            phrase = True
    if not phrase and matched < 2:
        return 0.0
    if cwd_org and page["org"] == cwd_org:
        score *= 1.5
    if page["status"] == "draft":
        score *= 0.5
    return score


def rank(index, prompt, cwd_org, exclude=()):
    low, toks = prompt.lower(), tokens(prompt)
    scored = []
    for page in index["pages"]:
        if page["path"] in exclude:
            continue
        s = score_page(page, low, toks, cwd_org)
        if s >= MIN_SCORE:
            scored.append((s, page))
    scored.sort(key=lambda x: (-x[0], x[1]["title"]))
    return scored[:MAX_HITS]


def render(hits):
    lines = ["Wiki pages that may be relevant (read the file before relying on it; "
             "deeper search: mcp__wiki__search):"]
    for _, p in hits:
        meta = ", ".join(x for x in (p["type"], p["org"], p["status"]) if x)
        lines.append("- %s [%s]: %s" % (p["title"], meta, p["path"]))
        if p["description"]:
            lines.append("  " + p["description"])
    text = "\n".join(lines)
    return text[:MAX_CONTEXT_CHARS]


# ---------------------------------------------------------------- state and logging
def _session_file(session_id):
    safe = re.sub(r"[^A-Za-z0-9_\-]", "_", session_id or "unknown")
    return os.path.join(CACHE_DIR, safe + ".json")


def load_session(session_id):
    try:
        with open(_session_file(session_id), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {"injected": [], "last_hits": []}


def save_session(session_id, state):
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(_session_file(session_id), "w", encoding="utf-8") as fh:
        json.dump(state, fh)
    now = time.time()
    for f in os.listdir(CACHE_DIR):
        full = os.path.join(CACHE_DIR, f)
        try:
            if now - os.stat(full).st_mtime > SESSION_TTL_SECONDS:
                os.remove(full)
        except OSError:
            pass


def log_event(event, **fields):
    try:
        os.makedirs(os.path.dirname(USAGE_LOG), exist_ok=True)
        rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "event": event}
        rec.update(fields)
        with open(USAGE_LOG, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec) + "\n")
    except OSError:
        pass


def _emit(event_name, text):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": event_name, "additionalContext": text}}))


# ---------------------------------------------------------------- subcommands
def cmd_retrieve(payload):
    prompt = payload.get("prompt") or ""
    session = payload.get("session_id") or "unknown"
    if is_continuation(prompt):
        return
    cwd_org = org_from_cwd(payload.get("cwd"))
    state = load_session(session)
    hits = rank(load_index(), prompt, cwd_org, exclude=set(state.get("injected", [])))
    if not hits:
        log_event("no_match", session=session, org=cwd_org)
        return
    state["injected"] = list(dict.fromkeys(state.get("injected", []) + [p["path"] for _, p in hits]))
    state["last_hits"] = [p for _, p in hits]
    save_session(session, state)
    log_event("inject", session=session, org=cwd_org,
              hits=[{"path": p["path"], "score": round(s, 1)} for s, p in hits])
    _emit("UserPromptSubmit", render(hits))


def cmd_subagent(payload):
    session = payload.get("session_id") or "unknown"
    hits = load_session(session).get("last_hits", [])
    pointer = ("Wiki root: %s (English pages with Indonesian aliases in frontmatter; search titles "
               "and aliases with /usr/bin/grep, or mcp__wiki__search)." % WIKI_ROOT)
    text = pointer
    if hits:
        text = render([(0, p) for p in hits]).replace(
            "Wiki pages that may be relevant", "Wiki pages the main session found relevant", 1) + "\n" + pointer
    log_event("subagent", session=session, agent_type=payload.get("agent_type"), hits=len(hits))
    _emit("SubagentStart", text[:MAX_CONTEXT_CHARS])


def cmd_read_log(payload):
    path = (payload.get("tool_input") or {}).get("file_path") or ""
    if path.startswith(WIKI_ROOT + "/") and path.endswith(".md"):
        log_event("read", session=payload.get("session_id"), path=path)


# ---------------------------------------------------------------- selftest
def selftest():
    global CACHE_DIR, USAGE_LOG
    fm = parse_frontmatter('---\ntitle: "SPPG suspend status"\naliases: ["status suspend SPPG", '
                           '"SPPG berhenti operasi"]\ntags:\n  - org/bgn\n  - suspend\norg: BGN  # org\n'
                           'status: reviewed\ndescription: "Why # stays, and more"\n---\nbody')
    assert fm["title"] == "SPPG suspend status", fm
    assert fm["aliases"] == ["status suspend SPPG", "SPPG berhenti operasi"], fm
    assert fm["tags"] == ["org/bgn", "suspend"] and fm["org"] == "BGN", fm
    assert fm["description"] == "Why # stays, and more", fm
    assert parse_frontmatter("no frontmatter") == {}

    for p in ("ya", "setuju semua", "lanjutkan", "ok gas", "  "):
        assert is_continuation(p), p
    assert not is_continuation("status suspend SPPG di Depok")
    assert org_from_cwd("/Users/isal/Workspaces/Organizations/BGN/scripts/sppg") == "BGN"
    assert org_from_cwd("/Users/isal/.claude") is None

    tmp = tempfile.mkdtemp()
    CACHE_DIR, USAGE_LOG = os.path.join(tmp, "cache"), os.path.join(tmp, "usage.jsonl")

    def page(rel, **fields):
        full = os.path.join(tmp, "wiki", rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        body = "---\n" + "".join("%s: %s\n" % (k, json.dumps(v)) for k, v in fields.items()) + "---\ntext\n"
        with open(full, "w") as fh:
            fh.write(body)
    page("concepts/SPPG suspend status.md", title="SPPG suspend status", org="BGN", status="reviewed",
         aliases=["status suspend SPPG", "SPPG berhenti operasi"], tags=["org/bgn", "suspend"],
         description="How to derive whether an SPPG is currently suspended.")
    page("concepts/SPPG master list.md", title="SPPG master list", org="BGN", status="reviewed",
         aliases=["daftar SPPG resmi"], description="Which table is the official SPPG list.")
    page("concepts/Draft suspend note.md", title="Suspend note", org="BGN", status="draft",
         aliases=["catatan suspend SPPG"], description="Draft about suspend.")
    page("concepts/macOS gotchas.md", title="macOS dev environment gotchas", org="personal",
         status="reviewed", aliases=["jebakan brew"], description="brew autoremove removes node.")
    page("templates/note.md", title="status suspend SPPG template")
    page("hot.md", title="status suspend SPPG hot")
    idx = build_index(os.path.join(tmp, "wiki"))
    titles = {p["title"] for p in idx["pages"]}
    assert "status suspend SPPG template" not in titles and "status suspend SPPG hot" not in titles, titles

    hits = rank(idx, "cek status suspend SPPG di Depok", "BGN")
    assert hits and hits[0][1]["title"] == "SPPG suspend status", hits
    assert all(h[1]["title"] != "macOS dev environment gotchas" for h in hits)
    draft = [h for h in hits if h[1]["status"] == "draft"]
    assert not draft or draft[0][0] < hits[0][0]
    assert rank(idx, "sppg", "BGN") == []                        # one weak token is not enough
    assert rank(idx, "jebakan brew autoremove node", None)[0][1]["org"] == "personal"
    assert len(render(hits)) <= MAX_CONTEXT_CHARS

    state = {"injected": [hits[0][1]["path"]], "last_hits": []}
    again = rank(idx, "cek status suspend SPPG di Depok", "BGN", exclude=set(state["injected"]))
    assert all(h[1]["path"] != hits[0][1]["path"] for h in again)  # no repeat within a session
    save_session("s1", {"injected": [], "last_hits": [hits[0][1]]})
    assert load_session("s1")["last_hits"][0]["title"] == "SPPG suspend status"
    print("selftest OK")
    return 0


def main(argv):
    cmd = argv[0] if argv else ""
    if cmd == "selftest":
        return selftest()
    if cmd == "index":
        idx = load_index()
        print("indexed %d pages -> %s" % (len(idx["pages"]), INDEX_PATH))
        return 0
    try:
        payload = json.load(sys.stdin)
        {"retrieve": cmd_retrieve, "subagent": cmd_subagent, "read-log": cmd_read_log}[cmd](payload)
    except Exception as exc:                                      # never block the session
        log_event("error", command=cmd, error=type(exc).__name__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
