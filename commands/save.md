---
name: save
description: Save current conversation to wiki. Files insights, decisions, and session summaries as structured notes in the ~/.claude wiki knowledge base.
argument-hint: "[session] [concept <name>] [decision <name>] [<name>]"
---

EXECUTE IMMEDIATELY — do not deliberate.

## Argument Parsing

Extract from $ARGUMENTS:

- *(empty)* — auto-classify and save the most valuable content from the current conversation
- `session` — save a full session summary covering everything discussed
- `concept <name>` — save as a concept note with the given name
- `decision <name>` — save as a decision record with the given name
- `<name>` — save with the specified note title; auto-classify the note type

## Step 1 — Load the Skill

Read `/Users/isal/.claude/skills/save/SKILL.md` to load the note type routing table, save workflow, frontmatter template, and writing style guide. This is mandatory — do not skip.

## Step 2 — Execute the Save Workflow

Follow the 10-step workflow defined in SKILL.md exactly, in order.

## Constraints

- Wiki root is `/Users/isal/.claude/wiki/` — never write outside this path.
- Do not create a new page if one with the same name already exists; update instead.
- Write knowledge, not conversation transcript. Declarative present tense only.
- Do not run in background — confirm completion inline.
