#!/usr/bin/env python3
"""One-way sync: wiki + Claude Code auto memory -> Hindsight bank `isal-knowledge`.

Usage:
  hindsight_sync.py             real run (needs HINDSIGHT_API_TOKEN; exits 0 with a stderr note if unset)
  hindsight_sync.py --dry-run   print create/update/delete plan, no network, no token needed
  hindsight_sync.py --self-test assert-based checks

Re-retaining an existing document_id is an upsert server-side (old document and its memory units are
deleted first, per the OpenAPI description of POST .../memories), so no delete-then-retain is needed.
Never fails a session: every error is logged to stderr and the exit code is 0.
Compatible with /usr/bin/python3 (3.9). Stdlib only (plus the shared hook helpers).
"""
from __future__ import annotations

import fcntl
import hashlib
import json
import os
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HOOKS = Path(__file__).resolve().parent
sys.path.insert(0, str(HOOKS))
sys.path.insert(0, "/Users/isal/.claude/scripts")

CLAUDE = Path("/Users/isal/.claude")
WIKI_ROOT = CLAUDE / "wiki"
PROJECTS = CLAUDE / "projects"
STATE_PATH = CLAUDE / "cache" / "hindsight-sync-state.json"
STATUS_PATH = CLAUDE / "cache" / "hindsight-sync-status.json"
LOCK_PATH = CLAUDE / "cache" / "hindsight-sync.lock"
BANK = "isal-knowledge"
DEFAULT_URL = "https://hindsight-api.cayunda.my.id"
TIMEOUT = 10
BATCH = 20
BUDGET_S = 40  # wall clock, under the 60s hook timeout
MAX_DELETE_FRACTION = 0.25
USER_AGENT = "hindsight-sync/1.0"  # Cloudflare 403s the default Python-urllib UA
ROOT_NAV_PAGES = {"wiki/hot.md", "wiki/index.md", "wiki/log.md"}

EXCLUDE_DRAFTS = True  # flip to False to also sync pages with `status: draft`
WIKI_SKIP_DIRS = {".git", "templates", "archive"}


def collect(wiki_root: Path = WIKI_ROOT, projects: Path = PROJECTS):
    """Yield (document_id, path, kind, project) for every non-excluded candidate (draft check is later)."""
    for p in sorted(wiki_root.rglob("*.md")):
        if not WIKI_SKIP_DIRS.isdisjoint(p.relative_to(wiki_root).parts[:-1]):
            continue
        did = "wiki/" + p.relative_to(wiki_root).as_posix()
        if did not in ROOT_NAV_PAGES:
            yield did, p, "wiki", None
    for p in sorted(projects.glob("*/memory/*.md")):
        if p.name != "MEMORY.md":
            yield "memory/%s/%s" % (p.parent.parent.name, p.name), p, "memory", p.parent.parent.name


def parse_frontmatter(text):
    from wiki_hooks import parse_frontmatter as pf  # lazy: an import failure must not break the hook
    return pf(text)


def is_draft(text: str) -> bool:
    return EXCLUDE_DRAFTS and str(parse_frontmatter(text).get("status", "")).lower() == "draft"


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def plan(state: dict, wiki_root: Path = WIKI_ROOT, projects: Path = PROJECTS, scan=None):
    """Return (upsert, delete, stats). upsert: {doc_id: (text, kind, project, hash, is_new)}."""
    if scan is None:
        import secret_scan
        scan = secret_scan.scan_text
    upsert, keep, stats = {}, set(), dict(create=0, update=0, skip=0, excluded=0, secret=0, delete=0)
    secret_files = []
    for doc_id, p, kind, project in collect(wiki_root, projects):
        try:
            text = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            stats["excluded"] += 1
            continue
        if kind == "wiki" and is_draft(text):
            stats["excluded"] += 1
            continue
        if scan(text):
            stats["secret"] += 1
            secret_files.append(doc_id)  # names only, never values
            continue
        keep.add(doc_id)
        h = sha(text)
        if state.get(doc_id) == h:
            stats["skip"] += 1
        else:
            stats["update" if doc_id in state else "create"] += 1
            upsert[doc_id] = (text, kind, project, h, doc_id not in state)
    delete = sorted(set(state) - keep)
    seen = {d.split("/", 1)[0] for d in keep}
    empty_root = [k for k in {d.split("/", 1)[0] for d in state} if k not in seen]
    stats["delete_blocked"] = ""
    if empty_root:
        stats["delete_blocked"] = "source root empty/missing: " + ",".join(sorted(empty_root))
    elif state and len(delete) > MAX_DELETE_FRACTION * len(state):
        stats["delete_blocked"] = "%d of %d tracked would be deleted (>25%%)" % (len(delete), len(state))
    if stats["delete_blocked"]:
        delete = []
    stats["delete"] = len(delete)
    stats["secret_files"] = secret_files
    return upsert, delete, stats


def build_item(doc_id: str, text: str, kind: str, project) -> dict:
    fm = parse_frontmatter(text) if kind == "wiki" else {}
    if kind == "wiki":
        context = "Obsidian wiki page %s" % (fm.get("title") or doc_id)
        tags = ["source:wiki"] + (["org:%s" % fm["org"]] if fm.get("org") else [])
    else:
        context = "Claude Code auto memory, project %s" % project
        tags = ["source:memory", "project:%s" % project]
    return {"content": text, "document_id": doc_id, "context": context, "tags": tags, "timestamp": "unset"}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):  # urllib would forward Authorization to the new host
        return None


class Api:
    def __init__(self, base: str, token: str):
        if not base.lower().startswith("https://"):
            raise ValueError("HINDSIGHT_API_URL must be https")
        self.base, self.token = base.rstrip("/"), token
        self.opener = urllib.request.build_opener(_NoRedirect)

    def call(self, method: str, path: str, body=None):
        req = urllib.request.Request(
            self.base + path, method=method,
            data=None if body is None else json.dumps(body).encode(),
            headers={"Authorization": "Bearer " + self.token, "Content-Type": "application/json",
                     "User-Agent": USER_AGENT})
        with self.opener.open(req, timeout=TIMEOUT) as r:
            raw = r.read()
        return json.loads(raw) if raw else {}

    def ensure_bank(self):
        # no GET-bank endpoint in the spec; filter the list by name instead of paging it
        banks = self.call("GET", "/v1/default/banks?" + urllib.parse.urlencode({"q": BANK, "limit": 100})).get("banks", [])
        if BANK not in {b.get("bank_id") for b in banks}:
            self.call("PUT", "/v1/default/banks/" + BANK, {"name": BANK})

    def retain(self, items: list):
        self.call("POST", "/v1/default/banks/%s/memories" % BANK, {"items": items, "async": True})

    def delete(self, doc_id: str):
        try:
            self.call("DELETE", "/v1/default/banks/%s/documents/%s" % (BANK, urllib.parse.quote(doc_id, safe="")))
        except urllib.error.HTTPError as e:
            if e.code != 404:  # already gone is fine
                raise


def load_state() -> dict:
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent))
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=0, sort_keys=True)
    os.replace(tmp, path)


def save_state(state: dict):
    _write_json(STATE_PATH, state)


def sync(api, state: dict, upsert: dict, delete: list, deadline: float):
    """Apply the plan, persisting state after every successful request. Returns (done, last_error)."""
    err, done = "", 0
    try:
        if upsert:
            api.ensure_bank()
    except Exception as e:  # noqa: BLE001
        return 0, "ensure_bank: %s" % e
    for d in delete:
        if time.monotonic() > deadline:
            return done, err or "budget exhausted"
        try:
            api.delete(d)
            state.pop(d, None)
            save_state(state)
            done += 1
        except Exception as e:  # noqa: BLE001
            err = "delete %s: %s" % (d, e)
            print("hindsight_sync: " + err, file=sys.stderr)
    ids = list(upsert)
    for i in range(0, len(ids), BATCH):
        if time.monotonic() > deadline:
            return done, err or "budget exhausted"
        batch = ids[i:i + BATCH]  # document_ids are dict keys, so unique within a batch
        try:
            api.retain([build_item(d, upsert[d][0], upsert[d][1], upsert[d][2]) for d in batch])
            for d in batch:
                state[d] = upsert[d][3]
            save_state(state)
            done += len(batch)
        except Exception as e:  # noqa: BLE001
            err = "retain batch %d: %s" % (i // BATCH, e)
            print("hindsight_sync: " + err, file=sys.stderr)
    return done, err


def run(dry: bool) -> int:
    token = os.environ.get("HINDSIGHT_API_TOKEN")
    if not dry and not token:
        print("hindsight_sync: HINDSIGHT_API_TOKEN unset, skipping", file=sys.stderr)
        return 0
    lock = None
    if not dry:
        LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
        lock = open(LOCK_PATH, "w")
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            return 0  # another session is syncing
    state = load_state()
    upsert, delete, st = plan(state)
    summary = "create=%(create)d update=%(update)d skip=%(skip)d delete=%(delete)d excluded=%(excluded)d secret_flagged=%(secret)d" % st
    if st["delete_blocked"]:
        summary += " delete_blocked=(%s)" % st["delete_blocked"]
    for f in st["secret_files"]:
        print("hindsight_sync: secret match, skipped: " + f, file=sys.stderr)
    if dry:
        for d, v in upsert.items():
            print(("create " if v[4] else "update ") + d)
        for d in delete:
            print("delete " + d)
        print("[dry-run] " + summary)
        return 0
    err = ""
    try:
        api = Api(os.environ.get("HINDSIGHT_API_URL") or DEFAULT_URL, token)
        _, err = sync(api, state, upsert, delete, time.monotonic() + BUDGET_S)
    except Exception as e:  # noqa: BLE001
        err = str(e)
    if err:
        print("hindsight_sync: " + err, file=sys.stderr)
    _write_json(STATUS_PATH, {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "summary": summary, "last_error": err})
    print("hindsight_sync: " + summary, file=sys.stderr)
    return 0


def self_test() -> int:
    global EXCLUDE_DRAFTS, MAX_DELETE_FRACTION, STATE_PATH
    STATE_PATH = Path(tempfile.mkdtemp()) / "state.json"
    tmp = Path(tempfile.mkdtemp())
    w, pr = tmp / "wiki", tmp / "projects"
    files = {
        w / "concepts/A.md": "---\nstatus: reviewed\norg: personal\n---\nbody",
        w / "concepts/B.md": "keep", w / "concepts/D.md": "---\nstatus: draft\n---\nbody",
        w / "templates/T.md": "x", w / "archive/O.md": "x", w / ".git/G.md": "x",
        w / "concepts/S.md": "SECRETMARK", w / "hot.md": "nav", w / "index.md": "nav", w / "log.md": "nav",
        pr / "-proj-a/memory/MEMORY.md": "index",
        pr / "-proj-a/memory/feedback.md": "memo",
    }
    for p, t in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(t)
    scan = lambda t: [(1, "x")] if "SECRETMARK" in t else []  # noqa: E731
    up, de, st = plan({}, w, pr, scan)
    assert sorted(up) == ["memory/-proj-a/feedback.md", "wiki/concepts/A.md", "wiki/concepts/B.md"], sorted(up)
    assert (st["create"], st["excluded"], st["secret"]) == (3, 1, 1), st                      # nav pages hot/index/log not collected
    assert build_item("memory/-proj-a/feedback.md", "memo", "memory", "-proj-a")["tags"][1] == "project:-proj-a"
    state = {d: v[3] for d, v in up.items()}
    up, de, st = plan(state, w, pr, scan)
    assert not up and not de and st["skip"] == 3                       # unchanged -> nothing
    (w / "concepts/A.md").write_text("changed")
    up, _, st = plan(state, w, pr, scan)
    assert list(up) == ["wiki/concepts/A.md"] and st["update"] == 1    # changed -> update
    MAX_DELETE_FRACTION = 1.0
    (w / "concepts/A.md").unlink()
    _, de, _ = plan(state, w, pr, scan)
    assert de == ["wiki/concepts/A.md"]                                # disappeared -> delete
    (w / "concepts/A.md").write_text("---\nstatus: draft\n---\n")
    _, de, _ = plan(state, w, pr, scan)
    assert de == ["wiki/concepts/A.md"]                                # became draft -> delete
    EXCLUDE_DRAFTS = False
    up, _, _ = plan({}, w, pr, scan)
    assert "wiki/concepts/D.md" in up                                  # constant flips the rule
    EXCLUDE_DRAFTS = True
    MAX_DELETE_FRACTION = 0.25
    _, de, st = plan(state, w, pr, scan)
    assert de == [] and "25%" in st["delete_blocked"]                  # mass-delete guard
    _, de, st = plan({"wiki/x.md": "h", "memory/p/y.md": "h"}, tmp / "nowiki", pr, scan)
    assert de == [] and "wiki" in st["delete_blocked"]                 # missing root guard
    MAX_DELETE_FRACTION = 1.0

    class Resp:  # fake urlopen result
        def __enter__(self): return self
        def __exit__(self, *a): pass
        def read(self): return b"{}"
    class Opener:
        def __init__(self): self.reqs = []
        def open(self, req, timeout=None):
            self.reqs.append(req)
            return Resp()
    api = Api("https://example.invalid", "tok")
    api.opener = Opener()
    api.delete("wiki/a b.md")
    r = api.opener.reqs[0]
    assert r.get_header("User-agent") == USER_AGENT and "wiki%2Fa%20b.md" in r.full_url
    try:
        Api("http://example.invalid", "tok")
        raise SystemExit("http url accepted")
    except ValueError:
        pass

    class FakeApi:  # second batch fails, third succeeds
        def __init__(self): self.calls = []
        def ensure_bank(self): pass
        def retain(self, items):
            self.calls.append([i["document_id"] for i in items])
            if len(self.calls) == 2:
                raise RuntimeError("boom")
        def delete(self, d): pass
    n = BATCH * 2 + 5
    ups = {"wiki/n%d.md" % i: ("t", "wiki", None, "h%d" % i, True) for i in range(n)}
    st2 = {"wiki/old.md": "h"}
    fa = FakeApi()
    done, err = sync(fa, st2, ups, ["wiki/old.md"], time.monotonic() + 60)
    assert [len(c) for c in fa.calls] == [BATCH, BATCH, 5] and "batch 1" in err
    assert len(st2) == BATCH + 5 and "wiki/old.md" not in st2          # failed batch not recorded
    assert json.loads(STATE_PATH.read_text()) == st2                   # persisted incrementally
    fa2 = FakeApi()
    done, err = sync(fa2, {}, ups, [], time.monotonic() - 1)
    assert fa2.calls == [] and err == "budget exhausted"               # wall-clock budget
    print("self-test OK")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    try:
        sys.exit(run("--dry-run" in sys.argv))
    except Exception as e:  # never break a session
        print("hindsight_sync: unexpected error: %s" % e, file=sys.stderr)
        sys.exit(0)
