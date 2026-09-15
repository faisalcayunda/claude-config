#!/usr/bin/env python3
import json
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "https://127.0.0.1:27124"  # HTTP 27123 is disabled; HTTPS with the plugin cert pinned
TOKEN_PATH = Path.home() / ".claude" / ".obsidian-token"
CERT_PATH = Path.home() / ".claude" / ".obsidian-rest-cert.pem"  # exported from the plugin settings


def ssl_context() -> ssl.SSLContext:
    ctx = ssl.create_default_context(cafile=str(CERT_PATH))
    ctx.check_hostname = False  # the self-signed cert is pinned through cafile
    return ctx


def token() -> str:
    return TOKEN_PATH.read_text().strip()


def headers(content_type: str | None = None) -> dict[str, str]:
    h = {"Authorization": f"Bearer {token()}"}
    if content_type:
        h["Content-Type"] = content_type
    return h


def request(method: str, url: str, body: bytes | None = None, accept: str | None = None) -> tuple[int, bytes]:
    h = headers("text/markdown" if body is not None else None)
    if accept:
        h["Accept"] = accept
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, context=ssl_context()) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except ConnectionRefusedError:
        print("Obsidian not running")
        sys.exit(1)
    except OSError:
        print("Obsidian not running")
        sys.exit(1)


def encode_path(path: str) -> str:
    return urllib.parse.quote(path, safe="/")


def cmd_open(path: str) -> None:
    url = f"{BASE_URL}/open/{encode_path(path)}"
    status, _ = request("POST", url)
    if status < 300:
        print(f"Opened: {path}")
    else:
        print(f"Error {status}")
        sys.exit(1)


def cmd_read(path: str) -> None:
    url = f"{BASE_URL}/vault/{encode_path(path)}"
    status, body = request("GET", url, accept="text/markdown")
    if status == 200:
        print(body.decode("utf-8"))
    else:
        print(f"Error {status}: {body.decode('utf-8', errors='replace')}")
        sys.exit(1)


def cmd_write(path: str, content: str) -> None:
    url = f"{BASE_URL}/vault/{encode_path(path)}"
    status, body = request("PUT", url, body=content.encode("utf-8"))
    if status < 300:
        print(f"Written: {path}")
    else:
        print(f"Error {status}: {body.decode('utf-8', errors='replace')}")
        sys.exit(1)


def cmd_append(path: str, content: str) -> None:
    url = f"{BASE_URL}/vault/{encode_path(path)}"
    status, body = request("POST", url, body=content.encode("utf-8"))
    if status < 300:
        print(f"Appended: {path}")
    else:
        print(f"Error {status}: {body.decode('utf-8', errors='replace')}")
        sys.exit(1)


def cmd_list(subfolder: str = "") -> None:
    path = subfolder.rstrip("/") + "/" if subfolder else ""
    url = f"{BASE_URL}/vault/{encode_path(path)}"
    status, body = request("GET", url)
    if status == 200:
        data = json.loads(body)
        files = data.get("files", [])
        for f in files:
            print(f)
    else:
        print(f"Error {status}: {body.decode('utf-8', errors='replace')}")
        sys.exit(1)


def cmd_tags() -> None:
    url = f"{BASE_URL}/tags/"
    status, body = request("GET", url)
    if status == 200:
        print(body.decode("utf-8"))
    else:
        print(f"Error {status}: {body.decode('utf-8', errors='replace')}")
        sys.exit(1)


USAGE = """Usage:
  obsidian.py open <path>
  obsidian.py read <path>
  obsidian.py write <path> <content>
  obsidian.py append <path> <content>
  obsidian.py list [subfolder]
  obsidian.py tags"""


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        sys.exit(1)

    match args[0]:
        case "open" if len(args) == 2:
            cmd_open(args[1])
        case "read" if len(args) == 2:
            cmd_read(args[1])
        case "write" if len(args) == 3:
            cmd_write(args[1], args[2])
        case "append" if len(args) == 3:
            cmd_append(args[1], args[2])
        case "list" if len(args) in (1, 2):
            cmd_list(args[1] if len(args) == 2 else "")
        case "tags" if len(args) == 1:
            cmd_tags()
        case _:
            print(USAGE)
            sys.exit(1)


if __name__ == "__main__":
    main()
