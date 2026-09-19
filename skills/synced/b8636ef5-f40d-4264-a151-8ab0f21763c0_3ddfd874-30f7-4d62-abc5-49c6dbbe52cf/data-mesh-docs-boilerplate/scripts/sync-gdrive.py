#!/usr/bin/env python3
"""
sync-gdrive.py — Sync Data Mesh Docs to Google Drive

Converts every Markdown file under docs/ to Google Docs format and uploads
to a target Google Drive folder, mirroring the docs/ directory structure.

Strategy:
  - Markdown → DOCX via pandoc → upload as Google Docs (native format)
  - Idempotent: update existing docs, create new ones
  - Mirrors folder hierarchy from docs/ into Google Drive
  - Optionally shares the root folder with configured email addresses
  - Respects data_classification frontmatter:
      Public / Internal  → no restrictions
      Restricted         → share only with GDRIVE_RESTRICTED_EMAILS
      Confidential       → share only with GDRIVE_CONFIDENTIAL_EMAILS + log to audit file

Requirements:
  pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib \
              python-frontmatter pyyaml
  system: pandoc (apt-get install pandoc  OR  brew install pandoc)

Environment Variables (see .env.example):
  GDRIVE_ENABLED                  - Must be 'true' to run
  GDRIVE_SERVICE_ACCOUNT_JSON     - Path to service account JSON key file
  GDRIVE_SERVICE_ACCOUNT_JSON_INLINE - Or inline JSON string (overrides path)
  GDRIVE_FOLDER_ID                - Target Google Drive folder ID
  GDRIVE_SHARE_EMAILS             - Comma-separated emails for reader access (optional)
  GDRIVE_RESTRICTED_EMAILS        - Emails allowed to see Restricted docs
  GDRIVE_CONFIDENTIAL_EMAILS      - Emails allowed to see Confidential docs
  GDRIVE_AUDIT_LOG                - Path for audit log file (default: gdrive-sync-audit.log)
  DOCS_DIR                        - Docs directory path (default: docs)
  GDRIVE_DRY_RUN                  - If 'true', print actions without executing
"""

import os
import sys
import json
import logging
import subprocess
import tempfile
import time
from datetime import datetime
from pathlib import Path

import frontmatter as fm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("sync-gdrive")

# ── Late imports (avoid hard failure if google libs not installed at parse time) ──

def _import_google():
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
        return service_account, build, MediaFileUpload
    except ImportError:
        log.error("Missing Google libraries. Run: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib")
        sys.exit(1)


# ── Config ────────────────────────────────────────────────────────────────────

class Config:
    enabled: bool
    service_account_json: str | None
    service_account_json_inline: str | None
    folder_id: str
    share_emails: list[str]
    restricted_emails: list[str]
    confidential_emails: list[str]
    audit_log: str
    docs_dir: Path
    dry_run: bool
    pandoc_reference_doc: Path | None

    def __init__(self):
        self.enabled = os.environ.get("GDRIVE_ENABLED", "").lower() == "true"
        self.service_account_json = os.environ.get("GDRIVE_SERVICE_ACCOUNT_JSON")
        self.service_account_json_inline = os.environ.get("GDRIVE_SERVICE_ACCOUNT_JSON_INLINE")
        self.folder_id = os.environ.get("GDRIVE_FOLDER_ID", "")
        self.share_emails = self._split_emails("GDRIVE_SHARE_EMAILS")
        self.restricted_emails = self._split_emails("GDRIVE_RESTRICTED_EMAILS")
        self.confidential_emails = self._split_emails("GDRIVE_CONFIDENTIAL_EMAILS")
        self.audit_log = os.environ.get("GDRIVE_AUDIT_LOG", "gdrive-sync-audit.log")
        self.docs_dir = Path(os.environ.get("DOCS_DIR", "docs"))
        self.dry_run = os.environ.get("GDRIVE_DRY_RUN", "").lower() == "true"
        ref = os.environ.get("GDRIVE_PANDOC_REFERENCE_DOC", "static/reference.docx")
        self.pandoc_reference_doc = Path(ref) if Path(ref).exists() else None

    @staticmethod
    def _split_emails(env_key: str) -> list[str]:
        raw = os.environ.get(env_key, "")
        return [e.strip() for e in raw.split(",") if e.strip()]

    def validate(self):
        errors = []
        if not self.folder_id:
            errors.append("GDRIVE_FOLDER_ID is not set")
        if not self.service_account_json and not self.service_account_json_inline:
            errors.append("Set GDRIVE_SERVICE_ACCOUNT_JSON or GDRIVE_SERVICE_ACCOUNT_JSON_INLINE")
        if not self.docs_dir.exists():
            errors.append(f"DOCS_DIR '{self.docs_dir}' does not exist")
        if errors:
            for e in errors:
                log.error("Config error: %s", e)
            sys.exit(1)


# ── Google Drive helpers ──────────────────────────────────────────────────────

class DriveClient:
    def __init__(self, config: Config):
        service_account, build, self._MediaFileUpload = _import_google()
        info = self._load_credentials(config)
        creds = service_account.Credentials.from_service_account_info(
            info, scopes=["https://www.googleapis.com/auth/drive"]
        )
        self.service = build("drive", "v3", credentials=creds)
        self.config = config

    @staticmethod
    def _load_credentials(config: Config) -> dict:
        if config.service_account_json_inline:
            return json.loads(config.service_account_json_inline)
        with open(config.service_account_json) as f:
            return json.load(f)

    def get_or_create_folder(self, name: str, parent_id: str) -> str:
        """Return folder ID, creating it if it doesn't exist."""
        q = (
            f"name='{name}' and "
            f"'{parent_id}' in parents and "
            f"mimeType='application/vnd.google-apps.folder' and "
            f"trashed=false"
        )
        res = self.service.files().list(q=q, fields="files(id)").execute()
        items = res.get("files", [])
        if items:
            return items[0]["id"]

        if self.config.dry_run:
            log.info("[DRY RUN] Would create folder: %s", name)
            return f"dry-run-folder-{name}"

        meta = {
            "name": name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_id],
        }
        folder = self.service.files().create(body=meta, fields="id").execute()
        log.info("Created folder: %s (%s)", name, folder["id"])
        return folder["id"]

    def find_existing_doc(self, name: str, parent_id: str) -> str | None:
        q = (
            f"name='{name}' and "
            f"'{parent_id}' in parents and "
            f"mimeType='application/vnd.google-apps.document' and "
            f"trashed=false"
        )
        res = self.service.files().list(q=q, fields="files(id)").execute()
        items = res.get("files", [])
        return items[0]["id"] if items else None

    def upload_or_update(
        self, doc_name: str, docx_path: Path, parent_id: str, existing_id: str | None = None
    ) -> str:
        """Upload a DOCX file as a Google Doc (converting it on upload)."""
        MediaFileUpload = self._MediaFileUpload
        media = MediaFileUpload(
            str(docx_path),
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            resumable=True,
        )

        if existing_id:
            self.service.files().update(fileId=existing_id, media_body=media).execute()
            log.info("Updated  : %s", doc_name)
            return existing_id
        else:
            meta = {
                "name": doc_name,
                "parents": [parent_id],
                "mimeType": "application/vnd.google-apps.document",
            }
            created = self.service.files().create(
                body=meta, media_body=media, fields="id"
            ).execute()
            log.info("Created  : %s (%s)", doc_name, created["id"])
            return created["id"]

    def set_permissions(self, file_id: str, emails: list[str], role: str = "reader"):
        """Share a file with specific email addresses."""
        for email in emails:
            try:
                self.service.permissions().create(
                    fileId=file_id,
                    body={"type": "user", "role": role, "emailAddress": email},
                    sendNotificationEmail=False,
                ).execute()
                log.info("Shared   : %s → %s (%s)", file_id, email, role)
            except Exception as e:
                log.warning("Failed to share %s with %s: %s", file_id, email, e)

    def add_labels(self, file_id: str, labels: list[str]):
        """Add description labels to a file (Drive doesn't support tags natively)."""
        try:
            desc = ", ".join(labels)
            self.service.files().update(
                fileId=file_id, body={"description": desc}
            ).execute()
        except Exception:
            pass  # Non-critical


# ── Pandoc conversion ─────────────────────────────────────────────────────────

def check_pandoc():
    result = subprocess.run(["pandoc", "--version"], capture_output=True)
    if result.returncode != 0:
        log.error("pandoc not found. Install: apt-get install pandoc  OR  brew install pandoc")
        sys.exit(1)

def md_to_docx(md_path: Path, reference_doc: Path | None = None) -> Path:
    """Convert Markdown file to DOCX using pandoc. Returns temp file path."""
    tmp = tempfile.NamedTemporaryFile(suffix=".docx", delete=False)
    tmp.close()
    out = Path(tmp.name)

    cmd = [
        "pandoc", str(md_path),
        "--from", "markdown+yaml_metadata_block+fenced_code_blocks",
        "--to", "docx",
        "--output", str(out),
        "--standalone",
        "--highlight-style", "pygments",
        "--toc",
        "--toc-depth", "3",
    ]
    if reference_doc:
        cmd += ["--reference-doc", str(reference_doc)]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        out.unlink(missing_ok=True)
        raise RuntimeError(f"pandoc error for {md_path}:\n{result.stderr}")

    return out


# ── Audit log ─────────────────────────────────────────────────────────────────

class AuditLog:
    def __init__(self, path: str):
        self.path = path

    def record(self, action: str, file: str, doc_id: str, classification: str):
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "action": action,
            "file": file,
            "google_doc_id": doc_id,
            "classification": classification,
        }
        with open(self.path, "a") as f:
            f.write(json.dumps(entry) + "\n")


# ── Main sync logic ───────────────────────────────────────────────────────────

def sync(config: Config):
    config.validate()
    check_pandoc()

    client = DriveClient(config)
    audit = AuditLog(config.audit_log)

    md_files = sorted(config.docs_dir.rglob("*.md"))
    log.info("Found %d Markdown files to sync", len(md_files))

    stats = {"created": 0, "updated": 0, "skipped": 0, "failed": 0}
    folder_cache: dict[str, str] = {}

    for md_file in md_files:
        rel = md_file.relative_to(config.docs_dir)
        parts = rel.parts  # e.g. ('education', 'master-sekolah', 'design', 'design-document.md')
        doc_name = md_file.stem  # filename without .md

        # ── Resolve parent folder in Drive ────────────────────────────────
        current_parent = config.folder_id
        for part in parts[:-1]:
            cache_key = "/".join(parts[:parts.index(part) + 1])
            if cache_key not in folder_cache:
                if config.dry_run:
                    folder_cache[cache_key] = f"dry-{cache_key}"
                else:
                    folder_cache[cache_key] = client.get_or_create_folder(part, current_parent)
            current_parent = folder_cache[cache_key]

        # ── Read frontmatter for classification ───────────────────────────
        try:
            post = fm.load(str(md_file))
            classification = post.metadata.get("data_classification", "Internal")
            pii_flag = post.metadata.get("pii_flag", False)
            tags = post.metadata.get("tags", [])
        except Exception:
            classification = "Internal"
            pii_flag = False
            tags = []

        # ── Convert Markdown → DOCX ───────────────────────────────────────
        docx_path = None
        try:
            if config.dry_run:
                log.info("[DRY RUN] Would upload: %s (classification=%s)", rel, classification)
                stats["created"] += 1
                continue

            docx_path = md_to_docx(md_file, config.pandoc_reference_doc)
            existing_id = client.find_existing_doc(doc_name, current_parent)
            action = "update" if existing_id else "create"
            doc_id = client.upload_or_update(doc_name, docx_path, current_parent, existing_id)

            # ── Apply classification-based permissions ─────────────────────
            if classification in ("Restricted", "Confidential"):
                permitted = (
                    config.confidential_emails
                    if classification == "Confidential"
                    else config.restricted_emails
                )
                if permitted:
                    client.set_permissions(doc_id, permitted, role="reader")
            elif config.share_emails:
                client.set_permissions(doc_id, config.share_emails, role="reader")

            # ── Labels ────────────────────────────────────────────────────
            label_list = [classification.lower()]
            if pii_flag:
                label_list.append("pii")
            label_list += [str(t) for t in tags[:3]]  # first 3 tags
            client.add_labels(doc_id, label_list)

            audit.record(action, str(rel), doc_id, classification)
            stats["created" if action == "create" else "updated"] += 1

            time.sleep(0.3)  # rate limit courtesy

        except Exception as e:
            log.error("FAILED: %s — %s", rel, e)
            stats["failed"] += 1
        finally:
            if docx_path and docx_path.exists():
                docx_path.unlink()

    log.info(
        "✅ Sync complete — created:%d  updated:%d  skipped:%d  failed:%d",
        stats["created"], stats["updated"], stats["skipped"], stats["failed"],
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
        log.info("GDRIVE_ENABLED is not 'true'. Set it to activate sync. Exiting.")
        sys.exit(0)

    sync(config)
