---
name: save
description: >
  Global ~/.claude save skill. File conversation insights, decisions, and analyses
  as structured notes in the wiki knowledge base.
  Wiki root: /Users/isal/.claude/wiki/
  Triggers on: "save this", "save that answer", "/save", "file this",
  "save to wiki", "save this session", "file this conversation", "keep this",
  "save this analysis", "add this to the wiki".
allowed-tools: Read Write Edit Glob Grep
---

# save: File Conversations Into the Wiki

Good answers and insights shouldn't disappear into chat history. This skill takes what was just discussed and files it as a permanent wiki page.

The wiki compounds. Save often.

---

## Note Type Decision

Determine the best type from the conversation content:

| Type | Folder | Use when |
|------|--------|---------|
| synthesis | questions/ | Multi-step analysis, comparison, or answer to a specific question |
| concept | concepts/ | Explaining or defining an idea, pattern, or framework |
| source | sources/ | Summary of external material discussed in the session |
| decision | meta/ | Architectural, project, or strategic decision that was made |
| session | meta/ | Full session summary: captures everything discussed |

If the user specifies a type, use that. If not, pick the best fit based on the content. When in doubt, use `synthesis`.

---

## Save Workflow

1. **Scan** the current conversation. Identify the most valuable content to preserve.
2. **Ask** (if not already named): "What should I call this note?" Keep the name short and descriptive.
3. **Determine** note type using the table above.
4. **Extract** all relevant content from the conversation. Rewrite it in declarative present tense (not "the user asked" but the actual content itself).
5. **Create** the note at `/Users/isal/.claude/wiki/[folder]/[Note Title].md` with full frontmatter.
6. **Check for duplicates**: before writing, check if a file with the same name already exists at that path. If it does, offer to update it instead of creating a duplicate.
7. **Update** `/Users/isal/.claude/wiki/index.md`. Add the new entry at the top of the relevant section.
8. **Append** to `/Users/isal/.claude/wiki/log.md`. New entry at the TOP:
   ```
   ## [YYYY-MM-DD] save | Note Title
   - Type: [note type]
   - Location: wiki/[folder]/Note Title.md
   - From: conversation on [brief topic description]
   ```
9. **Update** `/Users/isal/.claude/wiki/hot.md` to reflect the new addition.
10. **Confirm**: "Saved as [Note Title] in wiki/[folder]/."

---

## Frontmatter Template

```yaml
---
type: <synthesis|concept|source|decision|session>
title: "Note Title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - <relevant-tag>
status: developing
related:
  - "Any Wiki Page Mentioned"
---
```

For `synthesis` type, add:
```yaml
question: "The original query as asked."
answer_quality: solid
```

For `decision` type, add:
```yaml
decision_date: YYYY-MM-DD
status: active
```

---

## Writing Style

- Declarative, present tense. Write the knowledge, not the conversation.
- Not: "The user asked about X and Claude explained..."
- Yes: "X works by doing Y. The key insight is Z."
- Include all relevant context. Future sessions should be able to read this page cold.
- Reference related concepts by name where applicable.
- Cite sources where applicable: "(Source: Page Title)".

---

## What to Save vs. Skip

Save:
- Non-obvious insights or synthesis
- Decisions with rationale
- Analyses that took significant effort
- Comparisons that are likely to be referenced again
- Research findings

Skip:
- Mechanical Q&A (lookup questions with obvious answers)
- Setup steps already documented elsewhere
- Temporary debugging sessions with no lasting insight
- Anything already in the wiki (update the existing page instead)

