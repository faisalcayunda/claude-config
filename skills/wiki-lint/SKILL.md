---
name: wiki-lint
description: >
  Health check the Obsidian wiki vault. Finds orphan pages, dead wikilinks, stale claims,
  missing cross-references, frontmatter gaps, and empty sections. Creates or updates
  Dataview dashboards. Generates canvas maps. Triggers on: "lint", "health check",
  "clean up wiki", "check the wiki", "wiki maintenance", "find orphans", "wiki audit".
---

# wiki-lint: Wiki Health Check

Wiki root: /Users/isal/.claude/wiki

Run lint after every 10-15 ingests, or weekly. Ask before auto-fixing anything. Output a lint report to `/Users/isal/.claude/wiki/meta/lint-report-YYYY-MM-DD.md`.

---

## Lint Checks

Work through these in order:

1. **Orphan pages**. Wiki pages with no inbound wikilinks. They exist but nothing points to them.
2. **Dead links**. Wikilinks that reference a page that does not exist.
3. **Stale claims**. Assertions on older pages that newer sources have contradicted or updated.
4. **Missing pages**. Concepts or entities mentioned in multiple pages but lacking their own page.
5. **Missing cross-references**. Entities mentioned in a page but not linked.
6. **Frontmatter gaps**. Pages missing required fields (see Page conventions).
7. **Empty sections**. Headings with no content underneath.
8. **Stale index entries**. Items in `/Users/isal/.claude/wiki/index.md` pointing to renamed or deleted pages.

---

## Page conventions

- Pages are written in English. Add Indonesian `aliases` in frontmatter so Indonesian prompts still match.
- Folders stay by type (concepts, entities, sources, questions, comparisons, folds, meta). The organization goes in frontmatter, not in the folder.
- Required frontmatter:
  ```yaml
  ---
  title: "Page title"
  aliases: ["alias Bahasa Indonesia", "another alias"]
  type: concept        # concept | entity | source | question | comparison | decision | meta | fold
  org: BGN             # BGN | IDEAS | JDS | Trikintech | personal
  status: draft        # draft | reviewed
  description: "One sentence used by retrieval: what this page answers."
  tags: [org/bgn, topic]
  sources: ["where the facts come from"]
  verified: 2026-09-15 # last date facts were checked against reality; omit if never checked
  created: 2026-09-15
  updated: 2026-09-15
  related: ["[[Other Page]]"]
  ---
  ```
- Page-worthy: hard-won facts about external systems not recorded in any repo; decisions with their rationale; recurring gotchas; repeated how-tos. Not page-worthy: progress narration, one-off outputs, things already in git or a repo, raw data rows.
- If a page on the topic exists, update it instead of creating a new one.
- Never write credentials, tokens, DSNs with passwords, or personal data (NIK, phone numbers). A PreToolUse guard will reject them.
- Keep `hot.md` under 500 words.

---

## Lint Report Format

Create at `/Users/isal/.claude/wiki/meta/lint-report-YYYY-MM-DD.md`:

```markdown
---
type: meta
title: "Lint Report YYYY-MM-DD"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [meta, lint]
status: reviewed
---

# Lint Report: YYYY-MM-DD

## Summary
- Pages scanned: N
- Issues found: N
- Auto-fixed: N
- Needs review: N

## Orphan Pages
- [[Page Name]]: no inbound links. Suggest: link from [[Related Page]] or delete.

## Dead Links
- [[Missing Page]]: referenced in [[Source Page]] but does not exist. Suggest: create stub or remove link.

## Missing Pages
- "concept name": mentioned in [[Page A]], [[Page B]], [[Page C]]. Suggest: create a concept page.

## Frontmatter Gaps
- [[Page Name]]: missing fields: status, tags

## Stale Claims
- [[Page Name]]: claim "X" may conflict with newer source [[Newer Source]].

## Cross-Reference Gaps
- [[Entity Name]] mentioned in [[Page A]] without a wikilink.
```

---

## Naming Conventions

Enforce these during lint:

| Element | Convention | Example |
|---------|-----------|---------|
| Filenames | Title Case with spaces | `Machine Learning.md` |
| Folders | lowercase with dashes | `data-models/` |
| Tags | lowercase, hierarchical | `#domain/architecture` |
| Wikilinks | match filename exactly | `[[Machine Learning]]` |

Filenames must be unique across the vault. Wikilinks work without paths only if filenames are unique.

---

## Writing Style Check

During lint, flag pages that violate the style guide:

- Not declarative present tense ("X basically does Y" instead of "X does Y")
- Missing source citations where claims are made
- Uncertainty not flagged with `> [!gap]`
- Contradictions not flagged with `> [!contradiction]`

---

## Dataview Dashboard

Create or update `/Users/isal/.claude/wiki/meta/dashboard.md` with these queries:

````markdown
---
type: meta
title: "Dashboard"
updated: YYYY-MM-DD
---
# Wiki Dashboard

## Recent Activity
```dataview
TABLE type, status, updated SORT updated DESC LIMIT 15
```

## Seed Pages (Need Development)
```dataview
LIST WHERE status = "seed" SORT updated ASC
```

## Entities Missing Sources
```dataview
LIST FROM "entities" WHERE !sources OR length(sources) = 0
```

## Open Questions
```dataview
LIST FROM "questions" WHERE answer_quality = "draft" SORT created DESC
```
````

---

## Canvas Map

Create or update `/Users/isal/.claude/wiki/meta/overview.canvas` for a visual domain map:

```json
{
  "nodes": [
    {
      "id": "1",
      "type": "file",
      "file": "overview.md",
      "x": 0, "y": 0,
      "width": 300, "height": 140,
      "color": "1"
    }
  ],
  "edges": []
}
```

Add one node per domain page. Connect domains that have significant cross-references. Colors map to the CSS scheme: 1=blue, 2=purple, 3=yellow, 4=orange, 5=green, 6=red.

---

## Before Auto-Fixing

Always show the lint report first. Ask: "Should I fix these automatically, or do you want to review each one?"

Safe to auto-fix:
- Adding missing frontmatter fields with placeholder values
- Creating stub pages for missing entities
- Adding wikilinks for unlinked mentions

Needs review before fixing:
- Deleting orphan pages (they might be intentionally isolated)
- Resolving contradictions (requires human judgment)
- Merging duplicate pages
