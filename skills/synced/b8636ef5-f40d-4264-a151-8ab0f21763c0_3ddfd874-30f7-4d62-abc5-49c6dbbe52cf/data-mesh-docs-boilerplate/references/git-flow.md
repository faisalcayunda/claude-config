# Git Flow Strategy & Document History

## Branch Strategy untuk Dokumentasi

```
main ──────────────────────────────────────────────── (production: surge.sh live)
  │                                                     CHANGELOG updated on merge
  │
  ├── release/v1.1.0 ─────────────────────────────── (release branch)
  │       │                                             update-doc-history.sh runs here
  │       └── merge → main + develop
  │
develop ──────────────────────────────────────────── (staging: surge.sh preview)
  │
  ├── feature/B-02-proposal-domain-pendidikan
  ├── feature/D-01-design-doc-master-sekolah
  ├── feature/D-02-data-contract-peserta-didik
  ├── fix/D-04-catalog-typo-column-name
  └── hotfix/broken-mermaid-diagram (dari main)
```

### Branch Naming Convention

```
feature/[DOC_ID]-[short-kebab-description]
  Contoh: feature/D-01-design-doc-profil-sekolah
          feature/B-02-proposal-master-peserta-didik

fix/[DOC_ID]-[short-description]
  Contoh: fix/D-03-contract-yaml-missing-field

release/v[MAJOR].[MINOR].[PATCH]
  Contoh: release/v1.2.0
          release/v2.0.0

hotfix/[short-description]
  Contoh: hotfix/broken-confluence-sync
```

### Commit Message Convention (Conventional Commits)

```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

**Types:**
| Type | Digunakan Untuk |
|---|---|
| `feat` | Dokumen baru atau section baru |
| `fix` | Koreksi konten, typo, schema fix |
| `docs` | Update governance, vocabulary, ADR |
| `chore` | Pipeline, config, script changes |
| `refactor` | Restrukturisasi tanpa perubahan konten |
| `style` | Formatting, markdownlint fixes |

**Scope** = nama data product atau domain:
```
feat(master-data-sekolah): add bootstrap proposal document
fix(profil-peserta-didik): correct NIK field type in data contract
docs(governance): update data vocabulary for education domain
chore(pipeline): add Confluence sync stage to Jenkinsfile
```

---

## Document History (CHANGELOG.md)

Setiap data product memiliki `CHANGELOG.md` dengan format **Keep a Changelog**:

```markdown
# Changelog — {Data Product Name}

Semua perubahan signifikan pada dokumentasi data product ini dicatat di sini.
Format mengacu pada [Keep a Changelog](https://keepachangelog.com/).
Versi mengikuti [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

---

## [1.1.0] — 2025-04-10

### Ditambahkan
- Data Contract YAML untuk endpoint v2 (D-03)
- SCD Type 2 design untuk tabel `peserta_didik` (D-12)

### Diubah
- Risk Assessment: update likelihood score setelah security review (D-06)
- Data Catalog: tambah kolom `kebutuhan_khusus` (D-04)

### Diperbaiki
- Typo pada field `tanggal_lahir` di data-contract-spec.md (D-02)

---

## [1.0.0] — 2025-03-01

### Ditambahkan
- Initial release — semua dokumen fase Bootstrap dan Design
```

### Aturan Update CHANGELOG

1. **CHANGELOG hanya diupdate saat release** — bukan setiap feature commit
2. Script `update-doc-history.sh` dijalankan otomatis oleh Jenkins saat merge ke `main`
3. Commit messages dari `develop` sejak release terakhir dikompilasi menjadi CHANGELOG entries
4. Format entry dikelompokkan per: Ditambahkan / Diubah / Diperbaiki / Dihapus

---

## update-doc-history.sh

```bash
#!/usr/bin/env bash
# update-doc-history.sh
# Dipanggil oleh Jenkins saat release merge ke main.
# Generates CHANGELOG.md entries dari git log sejak tag terakhir.
#
# Usage:
#   bash scripts/update-doc-history.sh [version] [date]
#   Example: bash scripts/update-doc-history.sh 1.2.0 2025-05-01

set -euo pipefail

VERSION="${1:-}"
RELEASE_DATE="${2:-$(date +%Y-%m-%d)}"

if [[ -z "$VERSION" ]]; then
  echo "❌ Version argument required: bash update-doc-history.sh 1.2.0"
  exit 1
fi

DOCS_DIR="docs"
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
GIT_LOG_RANGE="${LAST_TAG:+${LAST_TAG}..HEAD}"

echo "📝 Generating CHANGELOG entries for v${VERSION} (${RELEASE_DATE})"
echo "   Git range: ${GIT_LOG_RANGE:-'(all commits)'}"

# Extract commits per data product (by file path)
find "$DOCS_DIR" -type d | while read -r domain_dir; do
  # Find CHANGELOG.md in each data product dir
  changelog="$domain_dir/CHANGELOG.md"
  [[ -f "$changelog" ]] || continue

  product_path="${domain_dir#$DOCS_DIR/}"

  # Get commits touching files under this data product
  if [[ -n "$GIT_LOG_RANGE" ]]; then
    commits=$(git log "$GIT_LOG_RANGE" --pretty=format:"%s" -- "$domain_dir/" 2>/dev/null || true)
  else
    commits=$(git log --pretty=format:"%s" -- "$domain_dir/" 2>/dev/null || true)
  fi

  [[ -z "$commits" ]] && continue

  # Categorize commits
  added=()
  changed=()
  fixed=()
  removed=()

  while IFS= read -r msg; do
    [[ -z "$msg" ]] && continue
    case "$msg" in
      feat*) added+=("- ${msg#*: }") ;;
      fix*)  fixed+=("- ${msg#*: }") ;;
      refactor*|docs*|style*) changed+=("- ${msg#*: }") ;;
      chore*) ;; # skip chore in changelog
      *) changed+=("- $msg") ;;
    esac
  done <<< "$commits"

  # Build new entry
  new_entry="## [${VERSION}] — ${RELEASE_DATE}\n\n"
  [[ ${#added[@]} -gt 0 ]] && new_entry+="### Ditambahkan\n$(printf '%s\n' "${added[@]}")\n\n"
  [[ ${#changed[@]} -gt 0 ]] && new_entry+="### Diubah\n$(printf '%s\n' "${changed[@]}")\n\n"
  [[ ${#fixed[@]} -gt 0 ]] && new_entry+="### Diperbaiki\n$(printf '%s\n' "${fixed[@]}")\n\n"
  [[ ${#removed[@]} -gt 0 ]] && new_entry+="### Dihapus\n$(printf '%s\n' "${removed[@]}")\n\n"

  # Insert after [Unreleased] section
  python3 - "$changelog" "$new_entry" <<'PYEOF'
import sys, re
path = sys.argv[1]
entry = sys.argv[2]
content = open(path).read()
# Insert new version entry after ## [Unreleased] block
pattern = r'(## \[Unreleased\].*?)(\n---\n)'
replacement = r'\1\2\n' + entry + '\n---\n'
updated = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
open(path, 'w').write(updated)
print(f"✅ Updated CHANGELOG: {path}")
PYEOF
done

# Commit CHANGELOG updates
git add "$DOCS_DIR/**/CHANGELOG.md" 2>/dev/null || true
git diff --cached --quiet || git commit -m "chore(release): update CHANGELOG for v${VERSION}"

echo "✅ Document history update complete for v${VERSION}"
```

---

## PR & Review Process

```
1. Branch: feature/D-02-data-contract-peserta-didik (dari develop)
   ↓
2. Commit: feat(profil-peserta-didik): add data contract spec v1
   ↓
3. PR ke develop
   ├── Required reviewers: Data Product Owner + 1 Data Engineer
   ├── CI checks: markdownlint + frontmatter validation + build
   └── Auto-preview: surge.sh/preview/feature-branch-name
   ↓
4. Merge ke develop → staging deploy
   ↓
5. Release branch: release/v1.1.0 (dari develop)
   ├── update-doc-history.sh runs → CHANGELOG updated
   ├── Version bump in frontmatter (via script atau manual)
   └── PR ke main + develop
   ↓
6. Merge ke main → production deploy + optional sync
```

## CODEOWNERS

```
# .github/CODEOWNERS
# Global
*                              @data-mesh-team

# Per domain
/docs/education/               @education-domain-team
/docs/health/                  @health-domain-team
/docs/governance/              @data-governance-team
/docs/project-management/      @project-management-team
/Jenkinsfile                   @devops-team
/scripts/                      @devops-team
```
