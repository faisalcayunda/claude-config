---
name: self-improve
description: Self-improvement loop — log lessons, audit recurring patterns, and create new skills from deep research. Never guesses; always evidence-first.
argument-hint: "[--log-lesson] [--audit] [--create-skill <name>]"
---

EXECUTE IMMEDIATELY — do not deliberate, do not ask clarifying questions before reading the protocol.

## Argument Parsing (do this FIRST)

Extract these from $ARGUMENTS:
- `--log-lesson` — capture a mistake interactively and append to lessons_learned.md
- `--audit` — scan lessons_learned.md for recurring patterns and propose prevention rules
- `--create-skill <name>` — research and build a new skill file at ~/.claude/commands/<name>.md

If no flag is provided, default to `--log-lesson`.

---

## Mode 1: `--log-lesson`

Capture a confirmed mistake and record it permanently.

1. Use `AskUserQuestion` to collect (batch all questions in one call):
   - What was wrong or assumed without verification?
   - What is the correct answer?
   - What source or evidence confirms the correct answer?
   - What trigger pattern led to the error?
   - What prevention rule should apply next time?

2. Append a new entry to:
   `~/.claude/projects/-Users-isal-Workspaces-Organizations-IDEAS-apps-datahub-backend/memory/lessons_learned.md`

   Format:
   ```
   ## <today's date> — <short title>

   **Mistake:** <what was wrong>
   **Correct answer:** <the verified truth>
   **Source:** <URL, file path, or command>
   **Trigger:** <what prompt pattern led to this>
   **Prevention rule:** <concrete rule for next time>
   ```

3. Confirm to user: "Lesson logged. Prevention rule: [rule]."

CRITICAL: Do not log non-mistakes. Purely additive work (new features, new files) does not belong here. Only confirmed wrong answers, bad assumptions, or speculative fixes.

---

## Mode 2: `--audit`

Identify recurring patterns in lessons and propose rule upgrades.

1. Read the full contents of:
   `~/.claude/projects/-Users-isal-Workspaces-Organizations-IDEAS-apps-datahub-backend/memory/lessons_learned.md`

2. Identify entries sharing the same trigger pattern (2+ entries with the same root cause category).

3. For each recurring pattern, draft a proposed addition to `~/.claude/CLAUDE.md` or `~/.claude/hooks/wave0-enforce.sh` as a new enforcement rule.

4. Present ALL proposals to the user with the supporting lessons as evidence. Do NOT apply any change automatically.

5. Wait for explicit user confirmation before invoking `update-config` or editing any file.

CRITICAL: The orchestrator never modifies CLAUDE.md without user confirmation. Proposals are surfaced; decisions belong to the user.

---

## Mode 3: `--create-skill <name>`

Build a new skill from evidence, never from imagination.

1. Run deep research first — dispatch two agents in parallel:
   - `Explore`: scan `~/.claude/commands/` to map all existing skill files and extract their exact format (frontmatter schema, body structure, argument parsing pattern, workflow reference pattern)
   - `general-purpose`: research the skill's domain from external sources (docs, GitHub, official guides) to gather concrete, citable evidence for what the skill should do

2. Wait for both research agents to return.

3. Synthesize findings into a complete skill specification:
   - Frontmatter: name, description, argument-hint
   - Argument parsing section (required + optional flags)
   - Execution steps (referencing verified patterns from research)
   - Bounded iteration support if the skill involves loops
   - "Stream all output live" footer

4. Write the skill file to `~/.claude/commands/<name>.md`

5. Pipe-test any associated hook scripts before registering them.

CRITICAL: Never write a skill body based on assumption. Every behavioral claim in the skill must trace back to a source found in step 1 or 2. If research returns nothing actionable, report that to the user instead of fabricating content.

---

Stream all output live — never run in background.
