"""Self-check for wiki_sync.py. Run: python3 -I test_wiki_sync.py (stdlib only, local repos, localhost only)."""
import fcntl
import http.server
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import traceback
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
SCRIPT = HERE / "wiki_sync.py"
REAL_GIT = shutil.which("git")
BASE = pathlib.Path(tempfile.mkdtemp(prefix="case-"))
GENV = {**os.environ, "GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_NOSYSTEM": "1"}
for k in [k for k in GENV if k.startswith(("GIT_DIR", "GIT_WORK", "GIT_INDEX"))]:
    del GENV[k]
COUNTER = [0]


class Syncthing(http.server.BaseHTTPRequestHandler):
    code = 200

    def do_GET(self):
        body = b'{"state": "idle", "needTotalItems": 0}'
        self.send_response(Syncthing.code)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


SRV = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Syncthing)
threading.Thread(target=SRV.serve_forever, daemon=True).start()
URL = f"http://127.0.0.1:{SRV.server_address[1]}"


def sh(*cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, env=GENV, text=True, encoding="utf-8", capture_output=True, check=True).stdout


class Case:
    """A bare origin, a working clone `wiki/` on main with one pushed commit, and a Syncthing config."""

    def __init__(self):
        COUNTER[0] += 1
        self.dir = BASE / f"c{COUNTER[0]}"
        self.dir.mkdir()
        self.origin = self.dir / "origin.git"
        self.wiki = self.dir / "wiki"
        sh("git", "init", "-q", "--bare", "-b", "main", str(self.origin))
        sh("git", "clone", "-q", str(self.origin), str(self.wiki))
        self.g("checkout", "-q", "-b", "main")
        self.g("config", "user.name", "Wiki Bot")
        self.g("config", "user.email", "bot@example.invalid")
        (self.wiki / "README.md").write_text("hi\n")
        self.g("add", "-A")
        self.g("commit", "-q", "-m", "init")
        self.g("push", "-q", "origin", "main")
        self.cfg = self.dir / "config.xml"
        self.cfg.write_text("<configuration><gui><apikey>TESTKEY-DO-NOT-LOG</apikey></gui></configuration>")
        Syncthing.code = 200
        self.base = self.head()

    def g(self, *a, cwd=None):
        return sh("git", *a, cwd=cwd or self.wiki)

    def write(self, name, content):
        p = self.wiki / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))

    def run(self, mode="finalize", **env):
        e = {**GENV, "WIKI_ROOT": str(self.wiki), "SYNCTHING_URL": URL, "SYNCTHING_CONFIG": str(self.cfg),
             "WIKI_SYNC_WAIT_SECONDS": "2", "https_proxy": "http://127.0.0.1:9", "http_proxy": "http://127.0.0.1:9"}
        e.update(env)
        r = subprocess.run([sys.executable, "-I", str(SCRIPT), mode], env=e, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=120)
        r.log = self.log()
        return r

    def log(self):
        p = self.dir / "wiki-sync.log"
        return p.read_text(encoding="utf-8") if p.exists() else ""

    def head(self):
        return self.g("rev-parse", "HEAD").strip()

    def origin_head(self, branch="main"):
        return sh("git", "rev-parse", branch, cwd=self.origin).strip()

    def staged(self):
        return self.g("diff", "--cached", "--name-only").strip()


def nfc(s):
    return unicodedata.normalize("NFC", s)


def assert_blocked(c, r, names, secrets=()):
    assert r.returncode == 1, f"rc={r.returncode} err={r.stderr!r}"
    assert c.staged() == "", "index not emptied"
    assert c.head() == c.base and c.origin_head() == c.base, "a commit happened"
    out = nfc(r.stderr + r.log)
    for n in names:
        assert nfc(n) in out, f"{n!r} not named in {out!r}"
    for s in secrets:
        assert s not in r.stderr + r.log, "secret value leaked"


def test_happy_path():
    c = Case()
    other = c.dir / "other"
    sh("git", "clone", "-q", str(c.origin), str(other))
    sh("git", "-c", "user.name=O", "-c", "user.email=o@example.invalid", "commit", "-q", "--allow-empty", "-m", "remote work", cwd=other)
    (other / "b.md").write_text("remote\n")
    sh("git", "add", "b.md", cwd=other)
    sh("git", "-c", "user.name=O", "-c", "user.email=o@example.invalid", "commit", "-q", "-m", "remote b", cwd=other)
    sh("git", "push", "-q", "origin", "main", cwd=other)
    c.write("a.md", "local note about a task, a skill and a risk\n")
    c.write("pic.png", b"\x89PNG\r\n\x00\x00\xff\xfe")
    r = c.run()
    assert r.returncode == 0, r.stderr + r.log
    assert c.origin_head() == c.head()
    assert re.fullmatch(r"docs: auto-commit wiki changes \(\d{4}-\d\d-\d\d \d\d:\d\d\)", c.g("log", "-1", "--format=%s").strip())
    assert c.g("log", "-1", "--format=%an <%ae>").strip() == "Wiki Bot <bot@example.invalid>"
    assert "Co-authored-by" not in c.g("log", "-1", "--format=%B")
    assert c.g("log", "--merges", "--format=%h").strip() == "", "history not linear"
    files = c.g("ls-tree", "-r", "--name-only", "HEAD").split()
    assert {"a.md", "b.md", "pic.png"} <= set(files), files


def test_b1_words_and_placeholders_pass_and_sk_blocked():
    c = Case()
    c.write("ok.md", "Ask about the task, skill and risk.\ntoken: ${GITHUB_TOKEN}\npassword=${PG_PASSWORD}\npassword: \"${PG_PASSWORD}\"\n")
    r = c.run()
    assert r.returncode == 0, r.stderr + r.log
    assert c.origin_head() == c.head() and "ok.md" in c.g("ls-tree", "-r", "--name-only", "HEAD")
    c.base = c.head()
    sk = "sk-" + "A1b2C3d4" * 3
    c.write("bad.md", f"key is {sk}\n")
    r = c.run()
    assert_blocked(c, r, ["bad.md"], [sk])
    assert "bad.md" in c.g("status", "--porcelain"), "working tree must be left alone"


B2_CONTENT = {
    "quoted.md": ('password = "hunter2"', "hunter2"),
    "json.md": ('{"api_key": "abc123"}', "abc123"),
    "aws.md": ("AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMIK7MDENG", "wJalrXUtnFEMIK7MDENG"),
    "akia.md": ("id AKIA" + "IOSFODNN7EXAMPLE", "IOSFODNN7EXAMPLE"),
    "slack.md": ("xoxb-" + "1234567890-abcdefghij", "1234567890-abcdefghij"),
    "jwt.md": ("eyJhbGciOiJIUzI1NiJ9" + ".eyJzdWIiOiIxMjM0NTY3ODkwIn0.sig", "eyJzdWIiOiIxMjM0NTY3ODkwIn0"),
    "pat.md": ("github_pat_" + "11ABCDEFG0abcdefghij_klmnop", "11ABCDEFG0abcdefghij_klmnop"),
    "dbpass.md": ("DB_PASS=s3cretpw99", "s3cretpw99"),
    "ghp.md": ("ghp_" + "a1B2c3D4e5F6" * 3, "a1B2c3D4e5F6"),
}
for _kind in ("RSA ", "DSA ", "EC ", "OPENSSH ", "ENCRYPTED ", ""):
    B2_CONTENT[f"pem-{_kind.strip() or 'plain'}.md"] = (f"-----BEGIN {_kind}PRIVATE KEY-----", f"BEGIN {_kind}PRIVATE")


def test_b2_formats_blocked():
    for name, (content, needle) in B2_CONTENT.items():
        c = Case()
        c.write(name, "line\n" + content + "\n")
        c.write("fine.md", "nothing here\n")
        r = c.run()
        try:
            assert_blocked(c, r, [name], [needle])
        except AssertionError as e:
            raise AssertionError(f"{name}: {e}")
        assert "fine.md" not in r.stderr, "innocent file named"


def test_b2_names_blocked():
    names = [".env", ".env.local", "sub/dir/.env", "a.pem", "b.key", "c.p12", "d.pfx", "id_rsa", "id_rsa.pub", "id_ed25519", "id_ed25519.pub"]
    for name in names:
        c = Case()
        c.write(name, "X=1\n" if "pem" not in name else b"\x00\x01\x02binary")
        r = c.run()
        try:
            assert_blocked(c, r, [name])
        except AssertionError as e:
            raise AssertionError(f"{name}: {e}")


def test_b3_unicode_noprefix_color_and_spaces():
    tok = "ghp_" + "Zy9X8w7V6u5T" * 3
    for cfg in ([], [("diff.noprefix", "true")], [("color.diff", "always")], [("diff.mnemonicPrefix", "true")]):
        c = Case()
        for k, v in cfg:
            c.g("config", k, v)
        c.write("catatan-\u00e9.md", f"x\n{tok}\n")
        c.write("my notes.md", f"password: hunter22\n")
        r = c.run()
        assert_blocked(c, r, ["catatan-\u00e9.md", "my notes.md"], [tok, "hunter22"])


def test_b4_hook_cannot_disable_scan_and_failing_hook_unstages():
    c = Case()
    hook = c.wiki / ".git" / "hooks" / "pre-commit"
    hook.write_text("#!/bin/sh\nexit 0\n")
    hook.chmod(0o755)
    sk = "sk-" + "Q1w2E3r4" * 3
    c.write("bad.md", sk + "\n")
    assert_blocked(c, c.run(), ["bad.md"], [sk])
    c = Case()
    hook = c.wiki / ".git" / "hooks" / "pre-commit"
    leak = "sk-" + "L3akL3ak" * 3
    hook.write_text(f"#!/bin/sh\necho {leak} >&2\nexit 1\n")
    hook.chmod(0o755)
    c.write("fine.md", "plain\n")
    r = c.run()
    assert r.returncode == 1 and "exit 1" in r.stderr
    assert c.staged() == "" and c.origin_head() == c.head()
    assert leak not in r.stderr + r.log


def test_b5_branch_and_rebase_guards():
    c = Case()
    c.g("checkout", "-q", "-b", "feature")
    c.write("a.md", "x\n")
    before = c.origin_head()
    r = c.run()
    assert r.returncode == 1 and "feature" in r.stderr, r.stderr
    assert c.origin_head() == before and c.g("log", "-1", "--format=%s").strip() == "init"
    assert sh("git", "branch", cwd=c.origin).split() == ["main"] or "feature" not in sh("git", "branch", cwd=c.origin)
    c = Case()
    c.write("a.md", "x\n")
    (c.wiki / ".git" / "rebase-merge").mkdir()
    r = c.run()
    assert r.returncode == 1 and "rebase in progress" in r.stderr
    assert c.origin_head() == c.head()
    c = Case()
    c.g("checkout", "-q", "--detach")
    assert c.run().returncode == 1


def shim(c, extra=""):
    """A `git` wrapper on PATH that records argv and then execs the real git."""
    d = c.dir / "shim"
    d.mkdir()
    (d / "git").write_text(f'#!/bin/sh\necho "$*" >> "{c.dir}/argv.log"\n{extra}exec "{REAL_GIT}" "$@"\n')
    (d / "git").chmod(0o755)
    return {"PATH": f"{d}:{os.environ['PATH']}"}


def argv(c):
    p = c.dir / "argv.log"
    return p.read_text().splitlines() if p.exists() else []


def test_b6_no_autostash():
    c = Case()
    c.g("config", "rebase.autoStash", "true")
    c.write("a.md", "x\n")
    r = c.run(**shim(c))
    assert r.returncode == 0, r.stderr + r.log
    pulls = [a for a in argv(c) if a.startswith("pull ")]
    assert pulls and all("--rebase" in a and "--no-autostash" in a for a in pulls), pulls
    assert not any("stash" in a and "--no-autostash" not in a for a in argv(c))


def test_n2_lock_held_exits_zero_without_git():
    c = Case()
    c.write("a.md", "x\n")
    with open(c.wiki / ".git" / "wiki-sync.lock", "a") as f:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        r = c.run(**shim(c))
    assert r.returncode == 0 and "lock" in r.log, r.stderr + r.log
    assert argv(c) == []
    assert c.head() == c.origin_head()


def test_n1_index_lock_stale_fails_fresh_skips():
    c = Case()
    c.write("a.md", "x\n")
    lock = c.wiki / ".git" / "index.lock"
    lock.write_text("")
    r = c.run()
    assert r.returncode == 0 and "index.lock" in r.log and c.head() == c.origin_head()
    old = time.time() - 20 * 60
    os.utime(lock, (old, old))
    r = c.run()
    assert r.returncode == 1 and "index.lock" in r.stderr


def test_n1_syncthing_errors():
    c = Case()
    c.write("a.md", "x\n")
    Syncthing.code = 401
    r = c.run()
    assert r.returncode == 1 and "401" in r.stderr
    assert "TESTKEY" not in r.stderr + r.log
    Syncthing.code = 200
    r = c.run(SYNCTHING_CONFIG=str(c.dir / "missing.xml"))
    assert r.returncode == 1 and "config.xml" in r.stderr
    r = c.run(SYNCTHING_URL="http://127.0.0.1:9", WIKI_SYNC_WAIT_SECONDS="0")  # connection refused: normal skip
    assert r.returncode == 0 and "not idle" in r.log and c.head() == c.origin_head()
    assert "TESTKEY" not in r.log


def test_n3_pull_timeout_aborts_rebase():
    c = Case()
    c.write("a.md", "x\n")
    r = c.run(WIKI_GIT_NET_TIMEOUT="1", **shim(c, 'case " $* " in *" pull "*) exec sleep 5;; esac\n'))
    assert r.returncode == 1 and "timed out" in r.stderr, r.stderr + r.log
    assert any(a.startswith("rebase --abort") for a in argv(c))


def test_round2_kebab_slugs_nul_bytes_and_deleted_key():
    c = Case()
    c.write("slugs.md", "[[task-scheduling-with-airflow-dags]] flask-sqlalchemy-integration-notes risk-assessment-for-data-pipelines\n")
    r = c.run()
    assert r.returncode == 0, r.stderr + r.log
    assert "slugs.md" in c.g("ls-tree", "-r", "--name-only", "HEAD")
    c.base = c.head()
    tok = "ghp_" + "a1B2c3D4e5F6" * 3
    c.write("nul.md", b"x\0y\n" + tok.encode() + b"\n")  # a NUL in the first 8 KB makes git print "Binary files differ"
    assert_blocked(c, c.run(), ["nul.md"], [tok])
    (c.wiki / "nul.md").unlink()
    c.write("slides.key", "x")  # a tracked key file that is later deleted adds no text and must not block forever
    c.g("add", "slides.key")
    c.g("commit", "-q", "-m", "key")
    c.g("push", "-q", "origin", "main")
    c.base = c.head()
    (c.wiki / "slides.key").unlink()
    r = c.run()
    assert r.returncode == 0, r.stderr + r.log
    assert "slides.key" not in c.g("ls-tree", "-r", "--name-only", "HEAD") and c.origin_head() == c.head()


def test_round2_angle_placeholder_and_status_file():
    c = Case()
    st = c.dir / "wiki-sync.status"
    c.write("api.md", "header `X-Api-Key: <key>` and `api_key: <YOUR_KEY>`\n")
    r = c.run()
    assert r.returncode == 0, r.stderr + r.log
    assert st.read_text().startswith("ok 20"), st.read_text()
    c.base = c.head()
    c.write("bad.md", "password = hunter2hunter2\n")
    assert_blocked(c, c.run(), ["bad.md"], ["hunter2hunter2"])
    assert st.read_text().startswith("FAIL 20") and "bad.md" in st.read_text() and "hunter2" not in st.read_text()


def main():
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for n, f in tests:
        try:
            f()
            print("PASS", n)
        except Exception:
            failed += 1
            print("FAIL", n)
            traceback.print_exc()
    SRV.shutdown()
    shutil.rmtree(BASE, ignore_errors=True)
    print(f"{len(tests) - failed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
