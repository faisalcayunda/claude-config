# Confluence Integration

## Overview

Script `sync-confluence.py` menggunakan tool `mark` (Markdown to Confluence) untuk
meng-push dokumentasi dari `docs/` ke Confluence space yang ditentukan.

Setiap file Markdown akan menjadi satu Confluence page. Hierarki halaman mengikuti
struktur direktori docs/.

## Required Environment Variables

```bash
# Confluence instance URL
CONFLUENCE_URL=https://your-org.atlassian.net

# Confluence Space Key (contoh: DATAMESH, PROJ, DOCS)
CONFLUENCE_SPACE=DATAMESH

# Autentikasi: gunakan API Token (bukan password)
# Buat di: id.atlassian.com/manage-profile/security/api-tokens
CONFLUENCE_USERNAME=your-email@example.com
CONFLUENCE_API_TOKEN=your-api-token

# Parent page ID di Confluence (opsional, untuk nested di bawah halaman tertentu)
# Dapatkan dari URL halaman: /wiki/spaces/SPACE/pages/{PAGE_ID}/Title
CONFLUENCE_PARENT_PAGE_ID=123456789

# Toggle
CONFLUENCE_ENABLED=true
```

## Instalasi mark CLI

```bash
# Via Go
go install github.com/kovetskiy/mark@latest

# Atau via Docker (tanpa Go install)
docker pull ghcr.io/kovetskiy/mark:latest
```

## Frontmatter Tambahan untuk Confluence

Tambahkan ke frontmatter Markdown jika perlu kontrol per-halaman:

```yaml
---
title: "Nama Dokumen"
# ... standard frontmatter ...

# Confluence-specific (opsional, override global config)
confluence_parent_id: "987654321"
confluence_labels:
  - data-product
  - design
  - restricted
---
```

## sync-confluence.py

```python
#!/usr/bin/env python3
"""
Sync Markdown docs to Confluence using mark CLI.
Builds a page hierarchy mirroring docs/ directory structure.

Requirements:
  pip install python-frontmatter pyyaml requests
  go install github.com/kovetskiy/mark@latest
  (mark must be in PATH)
"""

import os
import subprocess
import logging
import tempfile
import shutil
from pathlib import Path
import frontmatter as fm
import yaml

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
log = logging.getLogger(__name__)

DOCS_DIR = Path('docs')

def get_env(key: str, required: bool = True) -> str:
    val = os.environ.get(key, '')
    if required and not val:
        raise ValueError(f"Missing required env var: {key}")
    return val

def get_or_create_confluence_page(
    base_url: str, space: str, username: str, token: str,
    title: str, parent_id: str | None = None
) -> str:
    """Get existing page ID or create a blank parent page via REST API."""
    import requests
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(username, token)
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    search_url = f"{base_url}/wiki/rest/api/content"

    # Search for existing
    resp = requests.get(
        search_url,
        params={'title': title, 'spaceKey': space, 'type': 'page'},
        auth=auth, headers=headers
    )
    resp.raise_for_status()
    results = resp.json().get('results', [])

    if results:
        return str(results[0]['id'])

    # Create blank page
    body = {
        'type': 'page',
        'title': title,
        'space': {'key': space},
        'body': {'storage': {'value': '', 'representation': 'storage'}},
    }
    if parent_id:
        body['ancestors'] = [{'id': parent_id}]

    resp = requests.post(search_url, json=body, auth=auth, headers=headers)
    resp.raise_for_status()
    page_id = str(resp.json()['id'])
    log.info(f"Created Confluence page: '{title}' ({page_id})")
    return page_id

def add_mark_header(md_path: Path, space: str, parent_id: str | None) -> Path:
    """
    Add mark-compatible metadata comment to Markdown file.
    mark expects: <!-- Space: SPACE_KEY -->
                  <!-- Parent: Page Title or ID -->
    Returns path to modified temp file.
    """
    post = fm.load(str(md_path))
    title = post.metadata.get('title', md_path.stem)

    # mark header
    mark_header = f"<!-- Space: {space} -->\n"
    if parent_id:
        mark_header += f"<!-- Parent: {parent_id} -->\n"
    mark_header += f"<!-- Title: {title} -->\n\n"

    # Handle Mermaid: wrap in confluence-mermaid macro placeholder
    content = post.content
    content = content.replace('```mermaid', '<ac:structured-macro ac:name="mermaid">\n<ac:plain-text-body><![CDATA[')
    content = content.replace('```', ']]></ac:plain-text-body>\n</ac:structured-macro>')

    tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8')
    tmp.write(mark_header + content)
    tmp.close()
    return Path(tmp.name)

def run_mark(md_path: Path, base_url: str, username: str, token: str):
    """Run mark CLI to publish a Markdown file to Confluence."""
    cmd = [
        'mark',
        '--url', f"{base_url}/wiki",
        '--user', username,
        '--token', token,
        '--file', str(md_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        log.error(f"mark failed for {md_path}: {result.stderr}")
        raise RuntimeError(result.stderr)

    log.info(f"✅ Published: {md_path.name}")

def sync_docs():
    if os.environ.get('CONFLUENCE_ENABLED', '').lower() != 'true':
        log.info("CONFLUENCE_ENABLED is not set to 'true'. Skipping.")
        return

    base_url = get_env('CONFLUENCE_URL')
    space = get_env('CONFLUENCE_SPACE')
    username = get_env('CONFLUENCE_USERNAME')
    token = get_env('CONFLUENCE_API_TOKEN')
    root_parent_id = os.environ.get('CONFLUENCE_PARENT_PAGE_ID')

    # Track folder→page_id mapping for hierarchy
    folder_page_map: dict[str, str] = {}

    # Process sorted so parent folders come before children
    for md_file in sorted(DOCS_DIR.rglob('*.md')):
        rel = md_file.relative_to(DOCS_DIR)
        parts = rel.parts

        # Resolve parent page ID
        if len(parts) == 1:
            parent_id = root_parent_id
        else:
            parent_dir = str(Path(*parts[:-1]))
            if parent_dir not in folder_page_map:
                # Ensure parent folder pages exist
                current = root_parent_id
                for i in range(1, len(parts)):
                    key = str(Path(*parts[:i]))
                    if key not in folder_page_map:
                        folder_title = parts[i-1].replace('-', ' ').title()
                        page_id = get_or_create_confluence_page(
                            base_url, space, username, token,
                            folder_title, current
                        )
                        folder_page_map[key] = page_id
                    current = folder_page_map[key]
            parent_id = folder_page_map.get(parent_dir, root_parent_id)

        try:
            tmp_file = add_mark_header(md_file, space, parent_id)
            run_mark(tmp_file, base_url, username, token)
        except Exception as e:
            log.error(f"Failed: {md_file} — {e}")
        finally:
            if tmp_file and tmp_file.exists():
                tmp_file.unlink()

    log.info("✅ Confluence sync complete.")

if __name__ == '__main__':
    sync_docs()
```

## Confluence Labels Mapping

Data classification → Confluence label:
| Classification | Label |
|---|---|
| Public | `public` |
| Internal | `internal` |
| Restricted | `restricted` ← restrict page view in Confluence |
| Confidential | `confidential` ← restrict + audit log |

Untuk halaman dengan `data_classification: Restricted`, tambahkan page restriction
via Confluence REST API setelah upload.

## Notes

- `mark` CLI mendukung Confluence Cloud dan Server/DC
- Mermaid diagrams di Confluence memerlukan Mermaid for Confluence app (marketplace)
  atau dikonversi ke gambar PNG menggunakan `mmdc` (mermaid CLI)
- Table format dari Markdown biasanya dirender dengan baik di Confluence
- Code blocks dengan syntax highlighting memerlukan Confluence Code Block macro
