# Claude context consolidation plan

- Date: 2026-09-15
- Status: design agreed (Q1 to Q35). Phase 0 DONE 2026-09-15. Next: Phase 1 (needs user go-ahead).
- Role: single source of truth for this work until Phase 1 moves it into the wiki as a decision page.

## 0. Resume checklist (read first after compaction)

1. Read this whole file before doing anything else.
2. Phase 4 removed the stale SessionStart injections (`business-brain.md`, `wiki/hot.md`). If any old context still shows up, this plan wins.
3. Status: Phases 0 to 6, 8 and Side are done; Phase 7 (rotation) is the user's. See section 7.
4. Confirm with the user at the start of each phase before any destructive or outward-facing step (rm, uninstall, moving the vault, git init, editing settings.json or MCP config). Plan approval is not blanket approval.
5. Verification traps on this machine:
   - The `rtk` PreToolUse hook rewrites `head`, `grep`, `find`, `wc` into `rtk ...` and truncates output (a leading `// ...` marks truncation). For exact counts use `/usr/bin/<cmd>` or `python3`; those are not rewritten.
   - zsh expands unquoted globs: quote `--include='*.md'`.
   - `/usr/bin/python3` is 3.9: no backslashes inside f-string expressions.
   - macOS has no `timeout` command.
   - `pgrep -f <pattern>` inside a `while` loop matches its own shell command line; use a PID instead.

## 1. Goal and success test

- Primary: (a) read the wiki before working and cite the page; (b) write reusable findings without being asked.
- Side effect: one place for the user to browse in Obsidian. Constraint: small token footprint.
- Pass test: on a task whose topic is already in the wiki, Claude cites the page before acting; after a session with reusable findings, a new or updated page exists without a user request.

## 2. Decisions

| ID | Decision |
|---|---|
| Q1 | Success = read-before-work plus write-after-work; token economy is a constraint. |
| Q2 | Wiki audience = Claude and the user, browsable in Obsidian. Machine-only data (transcripts, auto-memory) stays out of the wiki. |
| Q3 | Hooks enforce both moments (retrieve on prompt, capture on stop). Skills hold the how. CLAUDE.md shrinks to pointers. |
| Q4 | Domain and cross-project knowledge -> global wiki, namespaced by org. Facts that must travel with a repo -> that repo. Wiki links to repos. |
| Q5 | One home per fact. Tiers: always-loaded (tiny), retrieved on demand (wiki), ephemeral (transcripts, session summaries). |
| Q6 | Retrieval hook (UserPromptSubmit): fires per prompt only above a relevance threshold; skip continuation prompts; max 3 hits as title + path + 2-3 line summary, under ~1,500 tokens; never whole pages; no repeat of a page within a session; reads files directly, no Obsidian dependency. |
| Q7 | Capture writes drafts without asking: `status: draft`. Retrieval down-weights drafts. |
| Q8 | Page-worthy: hard-won facts about external systems not recorded in any repo; decisions with rationale; recurring gotchas; repeated how-tos. Not page-worthy: progress narration, one-off outputs, things already in git or a repo, raw data rows, anything with credentials or personal data. Update an existing page instead of creating a new one. |
| Q9 | Keep type-first folders (concepts, entities, sources, questions, comparisons, folds, meta). Org in frontmatter (`org: BGN`) plus tag, one hub per org rendered with Obsidian Bases. Non-org knowledge uses `org: personal`. Retrieval boosts pages whose org matches the cwd. |
| Q10 | Superseded by Q23. |
| Q11 | Always-loaded tier budget about 2,000 tokens. |
| Q12 | Capture trigger: Stop hook (per turn) does a cheap transcript check since the last capture and only fires when there was substantive work (>=15 tool calls, or any DB query result, WebFetch, or agent report) AND >=20 minutes since the last capture. Exit 2 with a reason makes Claude judge using Q8 and write drafts or reply that nothing qualifies. Guard with `stop_hook_active`. |
| Q13 | Drafts live in their type folder with `status: draft`. The "inbox" is one Bases view filtering drafts. Promotion = change one field. |
| Q14 | Drafts are never auto-deleted or excluded; retrieval keeps them low-weight; drafts older than 30 days are counted in the scorecard. |
| Q15 | One extra line in `drift-check` SessionStart output: pages injected and read (7 days), drafts pending and >30 days, last capture date, warning when >14 days without capture despite sessions, plus plugin and MEMORY.md sizes (Q24). |
| Q16 | Phased rollout with a backup before each phase and verification before moving on (see section 4). Seed content ships with retrieval; the always-loaded tier is trimmed only after retrieval is proven. |
| Q17 | SubagentStart hook injects the main session's latest retrieval hits (stored per session by the retrieval hook) plus one wiki pointer line. Upgrade to transcript parsing only if too coarse. |
| Q18 | Subagents never write to the wiki. Their reports come back to the main session, whose capture hook decides. |
| Q19 | Obsidian vault root moves from `~/.claude` to `~/.claude/wiki`. `.obsidian/` moves to `wiki/.obsidian/`. Remove the second registered vault `plugins/claude-obsidian`. |
| Q20 | Keep the local wiki skills and fix every path to an absolute `WIKI_ROOT`. Uninstall the `claude-obsidian` plugin and remove `commands/save.md`. |
| Q21 | Upstream demo content moves to `~/.claude/archive/claude-obsidian-demo/` (outside the vault, reversible). Delete outright only proven-empty or byte-identical files. Clean demo references from the 7 mixed navigation pages. |
| Q22 | Retire the `memory` MCP server (remove from config) and `~/.claude/memory/` (salvage still-true facts to the wiki). Auto-memory stays but holds only its documented types (user corrections, project pointers), never domain knowledge. Move the 6 global preferences to the CLAUDE.md core. |
| Q23 | Wiki pages are written in English with Indonesian `aliases` in frontmatter. Reason: user rule 2026-08-21 "docs and scripts in English". Chat stays Indonesian. |
| Q24 | The ~2,000-token budget covers the user's own context (CLAUDE.md core plus injected knowledge). Deliberately enabled behaviour plugins (ponytail) and native MEMORY.md sit outside the budget but are shown in the scorecard. |
| Q25 | Injection clean-up: remove the SessionStart `cat business-brain.md wiki/hot.md` (identity ~15 lines -> CLAUDE.md core; business-brain section 7 MPM -> wiki; drop the active-project list). Plugin hot.md hooks die with Q20. Disable ECC `session-start.js` and `session-end.js`. Scope `rules/ecc/web/*` with `paths:` to frontend files, move README out of rules, delete `common/*` content that duplicates or contradicts CLAUDE.md and scope the rest. Replace `wave0-enforce` with the retrieval hook. Remove `lesson-capture-prompt`, `skill-optimization-ready`, `skill-run-logger`. Keep `drift-check` plus scorecard; remove hardcoded agent count from CLAUDE.md. |
| Q26 | Retrieval matching in the hook: title, aliases, tags, frontmatter description, plus org boost. Semantic search stays an on-demand tool. Swap the wiki MCP embedding model from `all-MiniLM-L6-v2` to `paraphrase-multilingual-MiniLM-L12-v2`. |
| Q27 | PreToolUse Write/Edit guard on `wiki/` and `*/memory/` denies content matching secret patterns (DSN `user:pass@`, `PASSWORD=`, key/token patterns, private keys, 16-digit NIK). `drift-check` also scans existing files and reports a count. |
| Q28 | Secrets: contain locally (chmod 600, MCP DSNs -> `${VAR}`, scrub knowledge and session files, Obsidian REST API HTTPS 27124 only, disable HTTP 27123) AND the user rotates production DB passwords that appeared in plaintext. |
| Q29 | Keep `rtk`. CLAUDE.md core gets one rule: verification uses `/usr/bin/<cmd>` or python; `// ...` means rtk truncated output. |
| Q30 | Two local git repos with a pre-commit secret scan (same patterns as Q27): (1) `~/.claude/wiki`, committed by obsidian-git for manual edits and by the capture hook for drafts; (2) `~/.claude` config with a strict `.gitignore` (exclude `.mcp.json`, `backups/`, `history.jsonl`, `projects/`, `sessions/`, `session-data/`, `file-history/`, `cache/`, `paste-cache/`, `shell-snapshots/`, `telemetry/`, `.obsidian-token`, `mcp/`, `plugins/`, `wiki/`, `metrics/`, `debug/`). Commit before and after each phase. No remote until the scanner proves the repos clean. |
| Q31 | Usage log at `~/.claude/metrics/wiki-usage.jsonl` (outside vault and git). |
| Q32 | Migration: seed from this session's findings (section 3.3); normalize and re-verify the 17 owner pages; verify business-brain section 7 before moving (`data_sppg_27469` vs `data_sppg_27485`); triage `lessons_learned.md` into topic pages of still-valid recurring gotchas, rest archived; triage auto-memory per Q22 prioritising `portal-adpem-backend`, `trino-cms`, `mbg-cc-pipelines` and BGN folders, others when those projects are next touched; keep one copy of `governance/` in the archive and delete byte-identical `config-backup-20260625-104205` duplicates, move `drift-check.sh` to `hooks/`; do not migrate session summaries (scrub secrets, then archive). Rule "promote on touch": the archive stays greppable and CLAUDE.md core points to it; when the wiki misses and the archive has it, promote it (Q8 applies). |
| Q33 | Secrets reach Claude Code through a shell function wrapper: `claude` -> `infisical run --env=<env> -- claude "$@"`. Add a `guard-dangerous.sh` deny rule for bare `env`, `printenv`, `set`. |
| Q34 | CLAUDE.md core keeps only 5 to 8 non-obvious routing lines (e.g. Airflow/dbt/Spark -> data-engineer not python-pro; BGN/MBG/SIPGN -> badan-gizi-nasional skill first; overlap resolution code-review vs code-reviewer, tdd vs tdd-guide, diagnosing-bugs vs debugger). Full routing tables move to one wiki page. |
| Q35 | Convert this session's `sample_geotag/` artifacts (script docstrings, SQL comments, workbook `_readme` sheet) to English. |

## 3. Verified facts

### 3.1 Claude Code behaviour (official docs, code.claude.com/docs/en/hooks, hooks-guide, memory, mcp)

- Hook output strings (`additionalContext`, `systemMessage`, plain stdout) are capped at 10,000 characters; larger output is saved to a file and replaced with a preview plus path. This is why the 20.4KB business-brain injection reached the model as a 2KB preview.
- UserPromptSubmit input carries the prompt text in field `prompt`. Context goes in `hookSpecificOutput.additionalContext`; a top-level `additionalContext` is silently ignored. Default timeout 30 s.
- Stop fires after every assistant turn. Exit code 2 on Stop prevents stopping and continues the conversation. Input has `stop_hook_active`; Claude Code overrides a Stop hook after 8 consecutive blocks without progress.
- SubagentStart input: `agent_id`, `agent_type` (no task prompt). It can return `hookSpecificOutput.additionalContext`, injected at the start of the subagent's conversation.
- SessionEnd hooks share a 1.5 s budget (raised to the longest per-hook timeout, max 60 s). Not suitable for capture.
- Rules without `paths:` frontmatter load every session; `paths:` globs load them only when matching files are read.
- Auto memory loads the first 200 lines or 25KB of `MEMORY.md`; topic files are read on demand; main-session auto memory is not loaded into subagents (forks excepted). Auto-memory dir is per git repo or project root.
- `@path` imports in CLAUDE.md expand eagerly at launch, max 4 hops.
- MCP config supports `${VAR}` and `${VAR:-default}` in `command`, `args`, `env`, `url`, `headers`, including user-scope entries in `~/.claude.json`. Values come from Claude Code's own environment. Unset vars load unexpanded with a warning. `claude mcp list` shows unexpanded `${VAR}`, never resolved values.
- Other available events worth knowing: PostCompact, CwdChanged, InstructionsLoaded (debug which rules load).

### 3.2 ~/.claude inventory (2026-09-15)

- Wiki `~/.claude/wiki`: 73 md. By content: 41 upstream demo, 17 owner (BGN, IDEAS, MDM, Trino, AdPem/SmartASN), 7 mixed navigation (`index`, `hot`, `log`, `concepts/_index`, `meta/2026-05-18-claude-structure-cleanup`, `meta/lint-report-2026-06-25`, `meta/obsidian-config`), 8 neutral (templates, 2 logs, dashboard). No writes since 2026-06-26. `hot.md` 1,054 words, frontmatter says updated 2026-05-18.
- Wiki MCP `mcp/wiki_mcp`: `WIKI_ROOT=/Users/isal/.claude/wiki`, `DB_PATH=mcp/wiki.db`, `EMBED_MODEL=all-MiniLM-L6-v2`; `mcp/` is 991MB (venv plus model). Reindexed by Stop hook `hooks/wiki-reindex.sh`. 1 call in 90 days.
- Local skills `save` uses absolute and relative wiki paths; `wiki-query`, `wiki-ingest`, `wiki-lint`, `wiki-fold` use only relative `wiki/` (break outside `~/.claude`).
- Obsidian: vault root is `~/.claude` (plus a second vault `plugins/claude-obsidian`); `newFileLocation=root`; 34 ignore filters; obsidian-git configured but no repo; Local REST API with HTTP 27123 enabled. No git anywhere under `~/.claude`.
- `memory` MCP: no `MEMORY_FILE_PATH`, no storage file, 0 entities, 0 calls.
- Auto-memory: `projects/-Users-isal--claude/memory/` holds 16 md incl. 6 global prefs (`feedback_commit_authorship`, `feedback_communication_style`, `feedback_devil_advocate`, `feedback_english_for_docs_and_code`, `feedback_multi_agent_default`, `feedback_no_premature_completion`); it loads only when cwd is `~/.claude` (1.9% of prompts). `projects/-Users-isal/memory/` is empty. `feedback_multi_agent_default` was already refined to "one correct specialist, fan out only when wide" and does not conflict with CLAUDE.md.
- SessionStart injections today: inline `cat business-brain.md wiki/hot.md` (~21KB), `governance/drift-check.sh`, ECC session-start (up to 8KB), ponytail (5 to 6.6KB); plus CLAUDE.md 8.3KB, 18 unscoped `rules/ecc` files 36.7KB. `wave0-enforce` adds ~1.2KB per prompt. `lesson-capture-prompt` nudges on every Edit.
- `lessons_learned.md` 216KB, ~240 entries, read twice in 90 days. `business-brain.md` 11.7KB, stale (claims CLAUDE.md v3.6.2, Wave 0 always, Sonnet 4.6), section 7 is MPM context citing `data_sppg_27469`.
- Top cwds since 2026-06-17: `portal-adpem-backend` (628 prompts), `trino-cms` (344), `mbg-cc-pipelines` (291).
- Secrets (types only): `~/.claude.json` 644 (5 DSNs with passwords, API key, PAT); `backups/.claude.json.backup.*` x5 644; `.mcp.json` 600 (3 DSNs, 2 keys); `history.jsonl` (2 DSNs, ~14 password/key assignments); `context-snapshot.md` (DSN); `session-data/*.tmp` (password, token); one datahub-backend memory file (`PASSWORD=`); portfolio memory (phone, email); `.obsidian-token` and REST API `data.json` 644 (API key, TLS key material). During this session, `claude mcp list` and an `.env` read with a missed mask (`PASWORD` typo) printed production DB passwords into model context.

### 3.3 Findings from this session (seed content for Phase 1)

- MPM `kpm_production` (DML-level account; host and user live in the Keychain-backed MCP config). Registered as MCP `dbhub-mpm` (user scope, inline DSN, fix in Phase 6).
  - Tables: `sppg` (19 cols; `city_code` etc. with dots like `32.76`; `coordinate` PostGIS point SRID 4326 stored as hex EWKB; `is_active`; dummy rows `created_by='dummy'`); `institution` = KPM (20 cols; `status` values `aktif-menerima`, `belum-terlayani`, `menolak`, `non-aktif-permanen`); `sppg_institution` (`sppg_id` -> `sppg.id_sppg`, `institution_code` -> `institution.code`, `is_active`); `beneficiary` = PM (~71M rows, 28GB, index on `institution_code`; ANALYZE temp key tables so the planner uses it); `institution_subcategory`, `institution_identity`, `person_in_charge`, `kpm_opt_out` (realocation preferences), `category` (17), `subcategory` (105), `classification_target` (8).
  - Empty lookup tables: `institution_status`, `beneficiary_status`, `sppg_verification`. `identity` (135M) and `beneficiary_identity` (134M) hold NIK.
  - `v_kinops_mpm` hardcodes 13 non-operational SPPG ids.
- SPPG master list: `data_temp.data_sppg_27485` in Pusdatin DWH (27,485 rows, unique `id_sppg`, all Beroperasi; includes wilayah_dialur, KPPG, deputi, biro, Dagri codes, zona_waktu). MPM active non-dummy SPPG match it exactly (Depok 199 + Jakarta Selatan 134 = 333). `data_mart.mart_master_sppg` is a superset (94,641 rows, 29,983 ids, 35 extra ids for those two kabkota); do not use it as the master. `data_sppg_27469` (cited in business-brain and sppg memory) not yet checked.
- SPPG suspend status: MPM has no suspend column. Source is Tauwas (letters numbered `.../D.TWS/...`).
  - `data_lake.t_spgg_suspend` (Pusdatin): grain one row per suspension letter; key `id` = `id_sppg`; fresh to 2026-08-25. National (valid 8-char ids): 6,840 rows, 6,212 SPPG; 948 open rows ("Masih berhenti Ops") for 866 SPPG; 66 SPPG with 2 open letters, 5 with 3, 2 with 4.
  - Rule: SPPG is suspended if ANY letter is still open. "Latest letter" misreads 9 SPPG nationally.
  - 9 groups of exact duplicates (id + date + letter); `MFR5ZWZE` has one letter with two conflicting statuses. `alasan_pemberhentian` holds unnormalized comma-joined values. `tanggal_surat_pembukaan` often empty even when the letter number is set.
  - `data_lake.t_tauwas`: name-keyed only (no id), stale (last incident 2026-05-31); inferring status from letters gives 1,940 (wrong). Use only for incident detail, joined via `nama_sppg`.
- Coordinate quality (MPM, national):
  - `institution` with coordinates 567,264: 18.8% valid, 64.9% lat/lon swapped (recoverable; after swap, median distance to kabkota centre 5 km for cities, 19 km for Kab. Bogor), 15.1% at (0,0), 1.2% other.
  - `sppg` active with coordinates 27,419: 90.8% inside Indonesia bbox, 0.3% swapped, 1.8% (0,0), 7.0% outside; 1,490 (5.4%) have a missing latitude minus sign that passes a bbox check.
  - A bbox check alone is insufficient; compare against the kabkota median.
- Matching signals (Depok + Jakarta Selatan sample): no KPM is served by an SPPG from another kabkota (0 of 5,417); ~45% of KPM with computable distance have an operational SPPG more than 500 m closer than their assigned one.
- Deliverable: `~/Workspaces/Organizations/BGN/scripts/sppg/sample_geotag/`. Run `1_extract_pusdatin.sql` then `2_extract_mpm.sql`, then `build_xlsx_raw.py` -> `sample_mpm_depok_jaksel.xlsx` (source columns only; `t_spgg_suspend` sheet deduped to one row per SPPG using the earliest open letter; per-letter raw in `raw_t_spgg_suspend.csv`). Older derived analysis: `build_xlsx.py` -> `sample_geotag_depok_jaksel.xlsx`. Adjacent pair chosen: Kota Depok 3276 + Kota Adm. Jakarta Selatan 3174 (minimum SPPG distance 685 m).
- Local machine gotchas (org: personal):
  - `brew uninstall` auto-removes orphaned dependencies. `node` was only a dependency of `gemini-cli`; `node`, `mpdecimal`, `readline` are now marked installed-on-request. asdf Pythons link brew `gdbm`, `mpdecimal`, `openssl@3`, `readline`, `sqlite`, `tcl-tk`, `xz`, `zlib`, `zstd`; never let brew remove them.
  - A venv breaks when its folder is moved (script shebangs keep the old path); 8 of 15 were broken. Recreate instead of moving.
  - `venv-clean` (abandoned 0.1.0) missed 14 of 15 venvs (regex on `activate` fails for Python 3.13+ templates) and `eval`s file content. Find venvs with `find <dir> -name pyvenv.cfg`.
  - Pre-existing: `tkinter` fails in asdf Python 3.11.9, 3.13.7, 3.14.0.

## 4. Execution phases

| Phase | Work | Done when |
|---|---|---|
| 0 Safety | chmod 600 on secret-bearing files; secret pattern scanner script; init both git repos with `.gitignore` and pre-commit scan; baseline commit | Baseline committed and the scanner reports zero secrets in tracked files |
| 1 Vault | Vault root -> `wiki/`; archive demo content; uninstall `claude-obsidian`; absolute `WIKI_ROOT` in skills; write this plan as a wiki decision page; seed pages from 3.3; normalize the 17 owner pages; org hubs and draft view in Bases | Obsidian shows only wiki content; wiki skills work from a project cwd |
| 2 Retrieval | Frontmatter index built by `wiki-reindex.sh`; UserPromptSubmit retrieval hook; per-session hit file; SubagentStart injection; usage log | A prompt about "status suspend SPPG" from a BGN folder injects the right page |
| 3 Capture | Stop capture hook; secret guard PreToolUse; hook-driven git commit | A test session produces a draft; a write containing a DSN is denied |
| 4 Trim | Rewrite CLAUDE.md core (identity, 6 prefs, language rules, rtk rule, secrets rule, compact routing, wiki and archive pointers); remove old injections and nudges per Q25; `paths:` scoping for `rules/ecc` | `/context` shows the startup footprint reduced; retrieval already proven |
| 5 Migration | Triage lessons and priority auto-memory; dedupe governance and config-backup; retire `memory` MCP and `~/.claude/memory/` | Every migrated fact verified or marked draft |
| 6 Secrets | `${VAR}` DSNs; `infisical run` wrapper; scrub files; REST API HTTPS only; deny bare env/printenv/set | `claude mcp list` connects and shows no passwords; scanner clean |
| 7 Rotation (user) | Rotate production DB passwords, update Infisical | MCP servers connect with the new passwords |
| 8 Scorecard | Scorecard line in drift-check; multilingual embedding model | Line appears in a fresh session |
| Side | Q35 English conversion of `sample_geotag/` artifacts | Done |

Rotation (7) must follow `${VAR}` (6), otherwise the new passwords get pasted into plaintext config again.

## 5. Owned by the user

- Rotating production DB credentials (Phase 7).
- Choosing the Infisical project/env/path for MCP secrets (needed in Phase 6).
- Per-phase go-ahead for destructive steps.

## 6. Unrelated pending items from this session

- `~/.gemini` (13MB) holds Google Antigravity IDE data created 2026-09-14 (implicit context, builtin skills, 3 empty crash logs, no saved conversations); the app is not installed. Awaiting the user's decision to delete. gemini-cli itself is already removed.
- Optional: `brew cleanup` would free ~235MB of installer cache.

## 7. Progress log

### Phase 0 (done 2026-09-15)

- Permissions: 84 secret-bearing files set to 600 (`~/.claude.json`, `.obsidian-token`, REST API `data.json`, `context-snapshot.md`, `history.jsonl`, all of `backups/` and `session-data/`); `backups/` and `session-data/` dirs 700.
  - Correction: this machine has a single account (`isal`, UID 501) and `/Users/isal` is 750, so the earlier 644 files were not readable by another account. The real exposure is plaintext duplication plus secrets printed into model context. chmod is defence in depth.
- Scanner: `scripts/secret_scan.py` (12 patterns: DSN with password, secret assignments incl. `PASWORD` typo and `PAT_VALUE`, Authorization headers, private keys, AWS, GitHub, GitLab, Slack, Anthropic/OpenAI, Google keys, JWT, NIK). Runs on `/usr/bin/python3` 3.9. `--selftest` covers regressions found against real files. `--baseline` suppresses reviewed examples by fingerprint (sha256 of path, kind, line); values are never stored or printed.
  - First version missed lowercase DSN passwords, `PAT_VALUE`, Authorization headers, and flagged floats as NIK. Found only by testing against files known to hold secrets. Keep testing new patterns the same way.
  - `hooks/secret-scanner.py` already existed but is not wired anywhere and misses unquoted `.env` passwords, `postgresql+psycopg2://`, NIK and Authorization. Archive it in Phase 5.
- Git pre-commit: `scripts/git-pre-commit-secret-scan.sh`, symlinked as `.git/hooks/pre-commit` in both repos.
- Config repo `~/.claude`: whitelist `.gitignore`, `.secret-scan-baseline` with 30 reviewed vendor-doc example credentials (ECC skills/rules, test-engineer, kotlin/rust test commands, data-engineer-boilerplate, old secret-scanner regex source). Baseline commit `016c7ff`.
- Wiki repo `~/.claude/wiki`: `.gitignore` ready for `.obsidian` (workspace files, REST API `data.json`). Baseline commit `9f3ceaf`.
- Verified: full scan of tracked files is 0 in both repos; a staged fake DSN is rejected by pre-commit in both repos; working trees clean.
- Author on commits: user identity only, no Claude attribution (feedback_commit_authorship).

### Phase 1 Vault (done 2026-09-15)

- Obsidian registry points the vault at `~/.claude/wiki`; the second vault entry is gone. REST API root lists only wiki folders.
- Demo content (41 pages, assets, canvases, root docs, `.raw`, `_templates`, plugin clone, DragonScale scripts) moved to `archive/claude-obsidian-demo/` with a manifest. `claude-obsidian` plugin entries removed from settings.
- 11 wiki skills use the absolute vault path, `.raw` at `~/.claude/.raw/`, a shared "Page conventions" section in `save`, and aligned types and statuses (`fold` added).
- Seed pages from 3.3, 17 owner pages normalized to the new frontmatter, org hubs as Bases (`hubs/BGN|IDEAS|personal|Drafts.base`). Wiki commits `8f4d37c`, `277939f`; config `5ff53ad`, `8235b3c`.

### Phase 2 Retrieval (done 2026-09-15)

- `hooks/wiki_hooks.py`: `retrieve` (UserPromptSubmit), `subagent` (SubagentStart), `read-log` (PostToolUse Read), `index`, `selftest`. Max 3 hits, min score 6, 6000 chars. Usage log never stores prompt text.
- Containment matching and `-nya` stripping fixed missed personal pages; 10 of 10 scenarios pass. Config `9e33327`, `83fe7c2`.

### Phase 3 Capture (done 2026-09-15)

- `hooks/wiki_capture.py check` (Stop, exit 2 after 15 tools or a strong tool, at most every 20 min) and `autocommit` (async, resets the index on a pre-commit rejection).
- `hooks/secret_guard.py` denies Write/Edit on wiki and memory paths with findings and fails closed. Verified live with a fake DSN.

### Phase 4 Trim (done 2026-09-15)

- CLAUDE.md 8.3KB to 3.3KB (v5.0, `3881885`), then 4.4KB v5.1 after closing the preference gaps found in Phase 5 (per-action git confirmation, delegation default, language and devil's advocate detail). v5.1 is not committed yet.
- `rules/ecc` scoped with `paths:`; 7 generic rule files archived. Unscoped rules 36.7KB to 0.
- Removed hooks: wave0-enforce, skill-optimization-ready, skill-run-logger, lesson-capture-prompt, SessionStart business-brain and hot.md, ECC session bootstrap and session end.

### Phase 5 Migration (done 2026-09-15)

- Governance (13 files), config-backup leftovers, retired hooks, session data (redacted) moved to `archive/legacy/` (`e2e2eb7`). `memory` MCP removed from both MCP configs.
- `lessons_learned.md`: 241 entries mapped by 281 manifest rows (wiki 209, archive 46, domain 26). 11 gotcha pages plus `concepts/Engineering hard rules.md`; 10 lessons were wrong when re-checked and the pages carry the checked version. Domain rows went to BGN and IDEAS pages with Contradiction notes where sources disagree.
- Auto memory: 176 manifest entries over 160 files. 160 files moved: 151 to `archive/legacy/project-memory/` (including 16 old `MEMORY.md` saved as `MEMORY.pre-triage.md`), 9 with personal data or credentials to `archive/pending-delete/` (700/600, not deleted). 18 project `MEMORY.md` files rewritten to one-line entries (max 10 lines). Every move sha256-checked.
- `lessons_learned.md` and `business-brain.md` archived to `archive/legacy/` after coverage checks; `~/.claude/memory/` removed (only empty dirs were left).
- CLAUDE.md v5.1 absorbed the preference memories (git confirmation per action, delegation sized to the work, language, devil's advocate with evidence, done vs pending). Not committed yet.
- 41 stale references to `business-brain.md`, `lessons_learned.md` and `~/.claude/memory/` in skills and commands repointed to CLAUDE.md, wiki pages or the archive. `hooks/drift-check.sh` already skips a missing `lessons_learned.md`.
- Wiki: 59 pages, navigation regenerated from frontmatter, search index rebuilt (364 chunks). Full scan of tracked wiki files: 0 findings.

### Phase 6 Secrets (done 2026-09-15, without Infisical)

- Done earlier: `secret_scan.py --redact` (`d8da0d2`, `69c2240`); guard denies bare `env`/`printenv`/`set`/`export -p` (`5727647`); REST API HTTPS only with a pinned cert (`b72cdde`).
- The user chose not to use Infisical. Secrets live in the macOS login Keychain (service `claude-mcp`, account `<scope>:<server>:<field>`, 15 items, round-trip sha256 checked). Configs hold `{{kc:<account>}}` tokens only.
- `scripts/mcp_secret.py`: `exec` resolves tokens in args and env, then execs the server (stdio servers run `/usr/bin/python3 mcp_secret.py exec -- <original command>`); `headers` prints JSON for `headersHelper` on HTTP servers. `${VAR}` was rejected because values in Claude's environment are readable from the Bash tool.
- User scope rewritten through `claude mcp remove` and `add-json`; `~/.claude/.mcp.json` edited directly. Secret scan of both configs and the Desktop config: 0. `drift-check.sh` placeholder regex now accepts `{{kc:...}}` and no longer prints the CRITICAL lines.
- Guard denies Keychain reads (password lookups with `-w`/`-g`, any `claude-mcp` lookup, `dump-keychain`) and running the resolver's `exec`/`headers` modes; 14 guard cases pass. String matching is not a boundary against obfuscated commands, and it also blocks harmless commands whose text quotes those strings (write such text through a file).
- `claude mcp list` after migration: `dbhub-individu`, `dbhub-kelompok`, `dbhub-datawarehouse`, `dbhub-mpm`, `zai-mcp-server`, `tableau`, `dbhub-dwh-pusdatin` connect through the resolver. Still failing and not caused by the migration: project `dbhub` and `postgresql` (their DSN targets local Postgres on 5432, which refuses connections), the three zai HTTP servers (endpoint not found), `browser-server` (binary not installed), `postman-api-http-server` (URL still a `{minimal | mcp}` template). `dbhub` is defined in both scopes.
- Redacted: the CLI's pre-migration `~/.claude.json` backup (10 values). Not redacted: `history.jsonl` (12 findings), 287 transcript files under `projects/`, 207 `file-history/` snapshots. Rotation (Phase 7) makes those values useless; redacting them is optional follow-up work.

### Phase 8 Scorecard (done 2026-09-15)

- `hooks/wiki_scorecard.py` appended to `hooks/drift-check.sh` (0.38s). Embedding model `paraphrase-multilingual-MiniLM-L12-v2` with a title, aliases and description header per chunk; Indonesian queries hit@3 3/5 to 5/5 (`572e562`). The wiki MCP needs a session restart to load it.

### Side Q35 (done 2026-09-15)

- `sample_geotag/` comments, notes and messages in English; `gen_2_extract_mpm.py` regenerates the suspended id list; geotag sheets renamed to `Summary` and `KPM Coordinate Issues`. Every data sheet hash matches the pre-conversion backup. "Extraction date" now comes from the CSV mtime (2026-08-29 and 2026-08-28) instead of the build date.
