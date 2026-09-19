# Google Drive Integration

## Overview

Script `sync-gdrive.py` mengkonversi file Markdown dari `docs/` ke format Google Docs
dan meng-upload ke Google Drive folder yang ditentukan. Struktur folder Google Drive
akan mirror struktur direktori docs/.

## Required Environment Variables

```bash
# Google Cloud Service Account credentials (JSON key file path atau inline JSON)
GDRIVE_SERVICE_ACCOUNT_JSON=/path/to/service-account.json
# atau
GDRIVE_SERVICE_ACCOUNT_JSON_INLINE='{"type":"service_account",...}'

# ID folder Google Drive tujuan (dari URL: drive.google.com/drive/folders/{FOLDER_ID})
GDRIVE_FOLDER_ID=1aBcDeFgHiJkLmNoPqRsTuVwXyZ

# Opsional: share ke email tertentu setelah upload
GDRIVE_SHARE_EMAILS=team@example.com,manager@example.com

# Toggle (set ke 'true' untuk mengaktifkan)
GDRIVE_ENABLED=true
```

## Setup Google Cloud Service Account

```bash
# 1. Buat project di Google Cloud Console
gcloud projects create your-project-id

# 2. Enable Google Drive API
gcloud services enable drive.googleapis.com --project=your-project-id

# 3. Buat service account
gcloud iam service-accounts create docs-sync \
  --display-name="Docs Sync SA" \
  --project=your-project-id

# 4. Download key JSON
gcloud iam service-accounts keys create service-account.json \
  --iam-account=docs-sync@your-project-id.iam.gserviceaccount.com

# 5. Share Google Drive folder dengan service account email
# Tambahkan docs-sync@your-project-id.iam.gserviceaccount.com sebagai Editor
# di folder Google Drive tujuan via Google Drive web UI
```

## sync-gdrive.py

```python
#!/usr/bin/env python3
"""
Sync Markdown docs to Google Drive as Google Docs.
Converts MD → DOCX via pandoc, then uploads to Drive.
Mirrors docs/ directory structure in the target Google Drive folder.

Requirements:
  pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
  apt-get install pandoc  # or brew install pandoc
"""

import os
import json
import subprocess
import tempfile
import logging
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
log = logging.getLogger(__name__)

SCOPES = ['https://www.googleapis.com/auth/drive']
DOCS_DIR = Path('docs')

def get_drive_service():
    """Authenticate and return Drive API service."""
    sa_json_path = os.environ.get('GDRIVE_SERVICE_ACCOUNT_JSON')
    sa_json_inline = os.environ.get('GDRIVE_SERVICE_ACCOUNT_JSON_INLINE')

    if sa_json_inline:
        info = json.loads(sa_json_inline)
    elif sa_json_path:
        with open(sa_json_path) as f:
            info = json.load(f)
    else:
        raise ValueError('Set GDRIVE_SERVICE_ACCOUNT_JSON or GDRIVE_SERVICE_ACCOUNT_JSON_INLINE')

    creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)

def get_or_create_folder(service, name: str, parent_id: str) -> str:
    """Get existing folder ID or create new one."""
    query = (
        f"name='{name}' and "
        f"'{parent_id}' in parents and "
        f"mimeType='application/vnd.google-apps.folder' and "
        f"trashed=false"
    )
    results = service.files().list(q=query, fields='files(id, name)').execute()
    items = results.get('files', [])

    if items:
        return items[0]['id']

    metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    folder = service.files().create(body=metadata, fields='id').execute()
    log.info(f"Created folder: {name} ({folder['id']})")
    return folder['id']

def md_to_docx(md_path: Path) -> Path:
    """Convert Markdown to DOCX using pandoc."""
    tmp = tempfile.NamedTemporaryFile(suffix='.docx', delete=False)
    tmp.close()

    cmd = [
        'pandoc', str(md_path),
        '-o', tmp.name,
        '--from', 'markdown+yaml_metadata_block',
        '--to', 'docx',
        '--standalone',
        '--highlight-style', 'pygments',
    ]

    # Use reference doc if it exists
    ref_doc = Path('static/reference.docx')
    if ref_doc.exists():
        cmd += ['--reference-doc', str(ref_doc)]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f'pandoc failed for {md_path}: {result.stderr}')

    return Path(tmp.name)

def upload_or_update(service, name: str, docx_path: Path, parent_id: str, file_id: str = None):
    """Upload new or update existing Google Doc."""
    media = MediaFileUpload(
        str(docx_path),
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        resumable=True
    )

    if file_id:
        # Update existing file
        service.files().update(fileId=file_id, media_body=media).execute()
        log.info(f"Updated: {name}")
    else:
        # Create new file, convert to Google Docs format
        metadata = {
            'name': name.replace('.md', ''),
            'parents': [parent_id],
            'mimeType': 'application/vnd.google-apps.document',
        }
        created = service.files().create(
            body=metadata,
            media_body=media,
            fields='id',
        ).execute()
        log.info(f"Created: {name} ({created['id']})")
        return created['id']

def find_existing_doc(service, name: str, parent_id: str) -> str | None:
    """Find existing Google Doc by name in parent folder."""
    query = (
        f"name='{name.replace('.md', '')}' and "
        f"'{parent_id}' in parents and "
        f"mimeType='application/vnd.google-apps.document' and "
        f"trashed=false"
    )
    results = service.files().list(q=query, fields='files(id)').execute()
    items = results.get('files', [])
    return items[0]['id'] if items else None

def share_folder(service, folder_id: str, emails: list[str]):
    """Share a folder with given email addresses (reader access)."""
    for email in emails:
        service.permissions().create(
            fileId=folder_id,
            body={'type': 'user', 'role': 'reader', 'emailAddress': email},
            sendNotificationEmail=False,
        ).execute()
        log.info(f"Shared folder with {email}")

def sync_docs():
    if os.environ.get('GDRIVE_ENABLED', '').lower() != 'true':
        log.info("GDRIVE_ENABLED is not set to 'true'. Skipping.")
        return

    service = get_drive_service()
    root_folder_id = os.environ['GDRIVE_FOLDER_ID']
    share_emails_raw = os.environ.get('GDRIVE_SHARE_EMAILS', '')
    share_emails = [e.strip() for e in share_emails_raw.split(',') if e.strip()]

    # Walk docs directory
    for md_file in sorted(DOCS_DIR.rglob('*.md')):
        # Build mirrored folder path in Drive
        rel_parts = md_file.relative_to(DOCS_DIR).parts
        current_parent = root_folder_id

        # Create/get intermediate folders
        for part in rel_parts[:-1]:
            current_parent = get_or_create_folder(service, part, current_parent)

        # Convert and upload
        try:
            docx_path = md_to_docx(md_file)
            existing_id = find_existing_doc(service, md_file.name, current_parent)
            upload_or_update(service, md_file.name, docx_path, current_parent, existing_id)
        except Exception as e:
            log.error(f"Failed to sync {md_file}: {e}")
        finally:
            if docx_path.exists():
                docx_path.unlink()

    # Share root folder
    if share_emails:
        share_folder(service, root_folder_id, share_emails)

    log.info("✅ Google Drive sync complete.")

if __name__ == '__main__':
    sync_docs()
```

## Notes

- Pandoc diperlukan sebagai dependency sistem: `apt-get install pandoc` atau `brew install pandoc`
- Google Doc hasil konversi tidak 100% identik dengan Markdown — tabel dan code blocks
  mungkin perlu manual adjustment
- Script ini idempotent: jika dokumen sudah ada di Drive, akan di-update; jika belum, dibuat baru
- Untuk Google Workspace domain: ganti `'type': 'user'` ke `'type': 'domain'` di share_folder
