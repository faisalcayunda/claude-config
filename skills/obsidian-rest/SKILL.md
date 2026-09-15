---
name: obsidian-rest
description: >
  Thin wrapper around the Obsidian Local REST API (v4.0.2, http://127.0.0.1:27123).
  Delegates every operation to `python3 ~/.claude/scripts/obsidian.py`.
  Triggers on: "obsidian open", "open in obsidian", "show in obsidian",
  "obsidian read", "obsidian list", "obsidian tags",
  or whenever a skill needs to surface a note in the Obsidian UI after writing it.
  Does NOT modify notes — filesystem skills (save, wiki-ingest, etc.) own writes.
allowed-tools: Bash
---

# obsidian-rest: Obsidian Local REST API Wrapper

Single entry point for all Obsidian UI and vault-read operations within Claude Code.
The script handles auth, URL encoding, and error reporting.

---

## Commands

### Open a note in Obsidian UI

```bash
python3 ~/.claude/scripts/obsidian.py open "<vault-relative-path>"
```

Example: `python3 ~/.claude/scripts/obsidian.py open "wiki/concepts/LLM Wiki Pattern.md"`

Use after any skill writes a new note and the user wants to view it immediately in Obsidian.

---

### Read raw markdown content

```bash
python3 ~/.claude/scripts/obsidian.py read "<vault-relative-path>"
```

Returns the raw markdown of the file. Use when a skill needs to inspect a note's current content without going through the filesystem directly.

---

### List vault contents

```bash
python3 ~/.claude/scripts/obsidian.py list [subfolder]
```

No argument — lists the vault root.
With argument — lists the specified subfolder.

```bash
python3 ~/.claude/scripts/obsidian.py list wiki/concepts
```

---

### List all tags

```bash
python3 ~/.claude/scripts/obsidian.py tags
```

Returns JSON. Use when the user asks "what tags are in the vault?" or when a save/ingest skill needs to pick consistent tags.

---

## Scope Boundaries

This skill only runs `python3 ~/.claude/scripts/obsidian.py` via Bash.

It does NOT:
- Write or modify any file (use `save`, `wiki-ingest`, `python-pro` for that).
- Manage frontmatter or wiki structure.
- Perform multi-step workflows on its own.

When another skill (e.g., `save`) finishes writing a note, it may invoke this skill to open the result in Obsidian — that is the canonical integration pattern.

---

## Error Handling

The script exits with code 1 and prints a human-readable message on failure.

| Condition | Output |
|-----------|--------|
| Obsidian not running | `Obsidian not running` |
| 404 file not found | `Error 404: ...` |
| Auth failure | `Error 401: ...` |

If `Obsidian not running` appears, ask the user to start Obsidian and enable the Local REST API plugin before retrying.

---

## Token

Bearer token loaded automatically from `~/.claude/.obsidian-token`.
Never echo or log the token. Never pass it as a CLI argument.
