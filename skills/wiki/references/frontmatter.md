# Frontmatter Schema

Every wiki page starts with flat YAML frontmatter. No nested objects. Obsidian's Properties UI requires flat structure.

---

## Universal Fields

Every page, no exceptions. This is the required frontmatter from the Page conventions section of `/Users/isal/.claude/skills/wiki/SKILL.md`:

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

---

## Type-Specific Additions

### source

Add these fields after the universal fields:

```yaml
source_type: article    # article | video | podcast | paper | book | transcript | data
author: ""
date_published: YYYY-MM-DD
url: ""
confidence: high        # high | medium | low
key_claims:
  - "First key claim from this source"
  - "Second key claim"
```

### entity

```yaml
entity_type: person     # person | organization | product | repository | place
role: ""
first_mentioned: "[[Source Title]]"
```

### concept

```yaml
complexity: intermediate  # basic | intermediate | advanced
domain: ""
```

### comparison

```yaml
subjects:
  - "[[Thing A]]"
  - "[[Thing B]]"
dimensions:
  - "performance"
  - "cost"
  - "ease of use"
verdict: "One-line conclusion."
```

### question

```yaml
question: "The original query as asked."
answer_quality: solid   # draft | solid | definitive
```

### domain

```yaml
subdomain_of: ""        # leave empty for top-level domains
page_count: 0
```

---

## Rules

1. Use flat YAML only. Never nest objects.
2. Dates as `YYYY-MM-DD` strings, not ISO datetime.
3. Lists use inline `[a, b]` or the `- item` format.
4. Wikilinks in YAML fields must be quoted: `"[[Page Name]]"`.
5. Keep `related` as wikilinks, not plain URLs.
6. Update `updated` every time you edit the page content.
