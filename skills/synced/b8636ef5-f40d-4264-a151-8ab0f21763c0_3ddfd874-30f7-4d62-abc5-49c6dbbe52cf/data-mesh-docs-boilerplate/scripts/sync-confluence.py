#!/usr/bin/env python3
"""
sync-confluence.py — Sync Data Mesh Docs to Confluence

Publishes every Markdown file under docs/ to a Confluence space,
mirroring the docs/ directory hierarchy as page parent/child relationships.

Strategy:
  - Uses `mark` CLI (github.com/kovetskiy/mark) to convert MD → Confluence Storage Format
  - Falls back to Confluence REST API directly for folder/parent pages
  - Idempotent: update existing pages, create new ones
  - Mermaid diagrams: wrapped in Confluence macro (requires Mermaid for Confluence app)
  - Respects data_classification frontmatter → applies Confluence page restrictions
  - Supports both Confluence Cloud and Server/DC

Requirements:
  pip install requests python-frontmatter pyyaml
  mark CLI: go install github.com/kovetskiy/mark@latest
            OR: docker pull ghcr.io/kovetskiy/mark:latest (set CONFLUENCE_MARK_USE_DOCKER=true)

Environment Variables (see .env.example):
  CONFLUENCE_ENABLED              - Must be 'true' to run
  CONFLUENCE_URL                  - e.g. https://your-org.atlassian.net
  CONFLUENCE_SPACE                - Space key, e.g. DATAMESH
  CONFLUENCE_USERNAME             - Your Confluence email / username
  CONFLUENCE_API_TOKEN            - API token (from id.atlassian.com/manage-profile/security)
  CONFLUENCE_PARENT_PAGE_ID       - Optional: root parent page ID for all synced docs
  CONFLUENCE_RESTRICTED_GROUP     - Confluence group for Restricted docs (optional)
  CONFLUENCE_CONFIDENTIAL_GROUP   - Confluence group for Confidential docs (optional)
  CONFLUENCE_MARK_USE_DOCKER      - If 'true', run mark via Docker
  CONFLUENCE_DRY_RUN              - If 'true', print actions without publishing
  DOCS_DIR                        - Docs directory (default: docs)
"""

import os
import sys
import json
import logging
import subprocess
import tempfile
import re
import time
from pathlib import Path
from typing import Optional

import requests
from requests.auth import HTTPBasicAuth
import frontmatter as fm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("sync-confluence")


# ── Config ────────────────────────────────────────────────────────────────────

class Config:
    def __init__(self):
        self.enabled = os.environ.get("CONFLUENCE_ENABLED", "").lower() == "true"
        self.url = os.environ.get("CONFLUENCE_URL", "").rstrip("/")
        self.space = os.environ.get("CONFLUENCE_SPACE", "")
        self.username = os.environ.get("CONFLUENCE_USERNAME", "")
        self.api_token = os.environ.get("CONFLUENCE_API_TOKEN", "")
        self.parent_page_id = os.environ.get("CONFLUENCE_PARENT_PAGE_ID", "")
        self.restricted_group = os.environ.get("CONFLUENCE_RESTRICTED_GROUP", "")
        self.confidential_group = os.environ.get("CONFLUENCE_CONFIDENTIAL_GROUP", "")
        self.use_docker = os.environ.get("CONFLUENCE_MARK_USE_DOCKER", "").lower() == "true"
        self.dry_run = os.environ.get("CONFLUENCE_DRY_RUN", "").lower() == "true"
        self.docs_dir = Path(os.environ.get("DOCS_DIR", "docs"))

    def validate(self):
        errors = []
        for key, val in [
            ("CONFLUENCE_URL", self.url),
            ("CONFLUENCE_SPACE", self.space),
            ("CONFLUENCE_USERNAME", self.username),
            ("CONFLUENCE_API_TOKEN", self.api_token),
        ]:
            if not val:
                errors.append(f"{key} is not set")
        if not self.docs_dir.exists():
            errors.append(f"DOCS_DIR '{self.docs_dir}' does not exist")
        if errors:
            for e in errors:
                log.error("Config error: %s", e)
            sys.exit(1)

    @property
    def api_base(self) -> str:
        return f"{self.url}/wiki/rest/api"

    @property
    def auth(self) -> HTTPBasicAuth:
        return HTTPBasicAuth(self.username, self.api_token)


# ── Confluence REST API client ────────────────────────────────────────────────

class ConfluenceClient:
    def __init__(self, config: Config):
        self.config = config
        self.session = requests.Session()
        self.session.auth = config.auth
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def _get(self, path: str, params: dict = None) -> dict:
        resp = self.session.get(f"{self.config.api_base}{path}", params=params)
        resp.raise_for_status()
        return resp.json()

    def _post(self, path: str, data: dict) -> dict:
        resp = self.session.post(f"{self.config.api_base}{path}", json=data)
        resp.raise_for_status()
        return resp.json()

    def _put(self, path: str, data: dict) -> dict:
        resp = self.session.put(f"{self.config.api_base}{path}", json=data)
        resp.raise_for_status()
        return resp.json()

    def find_page(self, title: str, space: str) -> Optional[dict]:
        """Find a page by title in a space. Returns page dict or None."""
        data = self._get("/content", params={
            "title": title,
            "spaceKey": space,
            "type": "page",
            "expand": "version",
        })
        results = data.get("results", [])
        return results[0] if results else None

    def create_page(self, title: str, space: str, parent_id: Optional[str] = None, body: str = "") -> dict:
        """Create a new Confluence page."""
        payload = {
            "type": "page",
            "title": title,
            "space": {"key": space},
            "body": {"storage": {"value": body, "representation": "storage"}},
        }
        if parent_id:
            payload["ancestors"] = [{"id": parent_id}]
        page = self._post("/content", payload)
        log.info("Created page: '%s' (id=%s)", title, page["id"])
        return page

    def update_page(self, page_id: str, title: str, new_version: int, body: str) -> dict:
        """Update an existing Confluence page."""
        payload = {
            "version": {"number": new_version},
            "title": title,
            "type": "page",
            "body": {"storage": {"value": body, "representation": "storage"}},
        }
        page = self._put(f"/content/{page_id}", payload)
        log.info("Updated page: '%s' (id=%s)", title, page_id)
        return page

    def get_or_create_page(self, title: str, space: str, parent_id: Optional[str] = None) -> str:
        """Get page ID or create an empty placeholder page."""
        existing = self.find_page(title, space)
        if existing:
            return existing["id"]
        if self.config.dry_run:
            log.info("[DRY RUN] Would create placeholder page: %s", title)
            return f"dry-{title}"
        page = self.create_page(title, space, parent_id)
        return page["id"]

    def restrict_page(self, page_id: str, group_name: str):
        """Apply view restriction to a page (Confluence Cloud / Server DC)."""
        if not group_name or self.config.dry_run:
            return
        try:
            url = f"{self.config.api_base}/content/{page_id}/restriction/byOperation/read"
            self.session.put(url, json={
                "results": [{"type": "group", "name": group_name}]
            })
            log.info("Restricted page %s to group: %s", page_id, group_name)
        except Exception as e:
            log.warning("Could not restrict page %s: %s", page_id, e)

    def add_labels(self, page_id: str, labels: list[str]):
        """Add labels to a Confluence page."""
        if not labels or self.config.dry_run:
            return
        try:
            payload = [{"prefix": "global", "name": lbl} for lbl in labels]
            self.session.post(f"{self.config.api_base}/content/{page_id}/label", json=payload)
        except Exception as e:
            log.warning("Could not add labels to %s: %s", page_id, e)


# ── Markdown → Confluence Storage Format conversion ──────────────────────────

def check_mark(use_docker: bool) -> bool:
    """Check if mark CLI is available."""
    if use_docker:
        result = subprocess.run(["docker", "inspect", "ghcr.io/kovetskiy/mark:latest"],
                                capture_output=True)
        return result.returncode == 0
    result = subprocess.run(["mark", "--version"], capture_output=True)
    return result.returncode == 0

def preprocess_markdown(content: str, space: str, parent_id: Optional[str], title: str) -> str:
    """
    Inject mark-compatible metadata and convert Mermaid code blocks
    to Confluence macro format.
    """
    # mark metadata header
    header = f"<!-- Space: {space} -->\n"
    if parent_id:
        header += f"<!-- Parent: {parent_id} -->\n"
    header += f"<!-- Title: {title} -->\n\n"

    # Convert mermaid fenced blocks → Confluence Mermaid macro
    content = re.sub(
        r"```mermaid\n(.*?)```",
        lambda m: (
            '<ac:structured-macro ac:name="mermaid" ac:schema-version="1">\n'
            f'<ac:plain-text-body><![CDATA[\n{m.group(1).strip()}\n]]>'
            '</ac:plain-text-body>\n</ac:structured-macro>'
        ),
        content,
        flags=re.DOTALL,
    )

    # Convert generic fenced code blocks → Confluence Code Block macro
    def code_to_macro(m: re.Match) -> str:
        lang = m.group(1) or "none"
        code = m.group(2).strip()
        return (
            f'<ac:structured-macro ac:name="code" ac:schema-version="1">\n'
            f'<ac:parameter ac:name="language">{lang}</ac:parameter>\n'
            f'<ac:parameter ac:name="theme">Confluence</ac:parameter>\n'
            f'<ac:plain-text-body><![CDATA[\n{code}\n]]></ac:plain-text-body>\n'
            f'</ac:structured-macro>'
        )
    content = re.sub(r"```(\w*)\n(.*?)```", code_to_macro, content, flags=re.DOTALL)

    # Convert Docusaurus admonitions → Confluence info/warning macros
    admonition_map = {
        "note": "info", "tip": "tip", "info": "info",
        "warning": "warning", "danger": "warning",
    }
    def admonition_to_macro(m: re.Match) -> str:
        kind = admonition_map.get(m.group(1).lower(), "info")
        body = m.group(2).strip()
        return (
            f'<ac:structured-macro ac:name="{kind}" ac:schema-version="1">\n'
            f'<ac:rich-text-body>\n<p>{body}</p>\n</ac:rich-text-body>\n'
            f'</ac:structured-macro>'
        )
    content = re.sub(r":::(note|tip|info|warning|danger)\n(.*?):::", admonition_to_macro,
                     content, flags=re.DOTALL | re.IGNORECASE)

    return header + content

def publish_with_mark(tmp_md: Path, config: Config) -> bool:
    """Run mark CLI to publish file to Confluence."""
    if config.use_docker:
        cmd = [
            "docker", "run", "--rm",
            "-v", f"{tmp_md.parent}:/docs",
            "ghcr.io/kovetskiy/mark:latest",
            "--url", f"{config.url}/wiki",
            "--user", config.username,
            "--token", config.api_token,
            "--file", f"/docs/{tmp_md.name}",
        ]
    else:
        cmd = [
            "mark",
            "--url", f"{config.url}/wiki",
            "--user", config.username,
            "--token", config.api_token,
            "--file", str(tmp_md),
        ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        log.error("mark failed: %s", result.stderr)
        return False
    return True


# ── Main sync logic ───────────────────────────────────────────────────────────

def sync(config: Config):
    config.validate()
    mark_available = check_mark(config.use_docker)
    if not mark_available:
        log.warning("mark CLI not found. Falling back to direct REST API (limited MD support).")

    client = ConfluenceClient(config)

    md_files = sorted(config.docs_dir.rglob("*.md"))
    log.info("Found %d Markdown files to sync", len(md_files))

    folder_page_map: dict[str, str] = {}
    stats = {"published": 0, "skipped": 0, "failed": 0}

    for md_file in md_files:
        rel = md_file.relative_to(config.docs_dir)
        parts = rel.parts

        # ── Read frontmatter ───────────────────────────────────────────────
        try:
            post = fm.load(str(md_file))
            title = post.metadata.get("title", md_file.stem)
            classification = post.metadata.get("data_classification", "Internal")
            pii_flag = post.metadata.get("pii_flag", False)
            tags = post.metadata.get("tags", [])
            content = post.content
        except Exception as e:
            log.error("Could not parse frontmatter for %s: %s", rel, e)
            stats["failed"] += 1
            continue

        # ── Resolve parent page ID ─────────────────────────────────────────
        if len(parts) == 1:
            parent_id = config.parent_page_id or None
        else:
            parent_dir = str(Path(*parts[:-1]))
            if parent_dir not in folder_page_map:
                # Build hierarchy from root
                current = config.parent_page_id or None
                for i in range(1, len(parts)):
                    key = str(Path(*parts[:i]))
                    if key not in folder_page_map:
                        folder_title = parts[i - 1].replace("-", " ").title()
                        if config.dry_run:
                            log.info("[DRY RUN] Would create parent page: %s", folder_title)
                            folder_page_map[key] = f"dry-{key}"
                        else:
                            pid = client.get_or_create_page(folder_title, config.space, current)
                            folder_page_map[key] = pid
                    current = folder_page_map[key]
            parent_id = folder_page_map.get(parent_dir)

        # ── Dry run ────────────────────────────────────────────────────────
        if config.dry_run:
            log.info("[DRY RUN] Would publish: %s → Confluence page '%s'", rel, title)
            stats["published"] += 1
            continue

        # ── Publish via mark or REST ───────────────────────────────────────
        tmp_file = None
        try:
            processed = preprocess_markdown(content, config.space, parent_id, title)

            if mark_available:
                tmp_file = Path(tempfile.mktemp(suffix=".md"))
                tmp_file.write_text(processed, encoding="utf-8")
                ok = publish_with_mark(tmp_file, config)
                if not ok:
                    stats["failed"] += 1
                    continue
            else:
                # Direct REST API: simple HTML body (tables and basic formatting only)
                existing = client.find_page(title, config.space)
                if existing:
                    new_ver = existing["version"]["number"] + 1
                    client.update_page(existing["id"], title, new_ver, f"<p>{processed[:5000]}</p>")
                    page_id = existing["id"]
                else:
                    page = client.create_page(title, config.space, parent_id,
                                              f"<p>{processed[:5000]}</p>")
                    page_id = page["id"]

                # Apply restrictions and labels when using REST directly
                if classification == "Confidential" and config.confidential_group:
                    client.restrict_page(page_id, config.confidential_group)
                elif classification == "Restricted" and config.restricted_group:
                    client.restrict_page(page_id, config.restricted_group)

                label_list = [classification.lower()]
                if pii_flag:
                    label_list.append("pii")
                label_list += [str(t) for t in tags[:5]]
                client.add_labels(page_id, label_list)

            log.info("Published: %s → '%s'", rel, title)
            stats["published"] += 1
            time.sleep(0.4)  # rate limit courtesy

        except Exception as e:
            log.error("FAILED: %s — %s", rel, e)
            stats["failed"] += 1
        finally:
            if tmp_file and tmp_file.exists():
                tmp_file.unlink()

    log.info(
        "✅ Sync complete — published:%d  skipped:%d  failed:%d",
        stats["published"], stats["skipped"], stats["failed"],
    )
    if stats["failed"] > 0:
        sys.exit(1)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Load .env if present (dev convenience)
    env_file = Path(".env")
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                os.environ.setdefault(key.strip(), val.strip())

    config = Config()

    if not config.enabled:
        log.info("CONFLUENCE_ENABLED is not 'true'. Set it to activate sync. Exiting.")
        sys.exit(0)

    sync(config)
