# QueryHive remaining work: advisor verdict

## Context
Second opinion on the 11 remaining items after Wave 3. Read-only investigation; findings below were checked against the repo on 2026-09-29.

## Facts that change the list
- ADR-0027 hole is reachable only through `SAFE_MODE_FLOOR`, which nothing in the app or MCP sets (grep: only `crates/qh-ffi/src/commands.rs:143` and tests). App sends `SAFE_MODE` only (`AppModel.swift:2850`); MCP forces `read_only`. CLI-only today, but `commands.rs:109-111` names SAFE_MODE_FLOOR as "the one input a configuration profile would set", so it must be closed before profiles.
- The ordinary guard is correct under the total strictness order (`classify.rs:173-188`). Only `guard_destructive` (`commands.rs:290-316`) breaks monotonicity. Per-kind resolution in `qh-sql` is unnecessary.
- MCP protocol-version refusal already shipped (`mcp.rs:776-796`, commit 310c03d; `docs/mcp-stability.md` "Versi protokol"). Plan §12.3 last sentence and the doc comment at `mcp.rs:79-83` are stale.
- Column format boundary is already documented at `Models/ColumnFormat.swift:3-12` ("rendering-only ... what an export writes").
- 14A editor items: line numbers and folding are always on (`SQLEditor.swift:76-79`), wrap hardcoded (`:61`); keyword case, tab width, invisibles do not exist as features. Grid: row height const (`ResultGrid.swift:23`), NULL text hardcoded (`:904`, `:1471`), `rowLimit = 1000` per tab (`QueryTab.swift:463`).
- Accent, tone, glow are global in `ThemeStore` (7 themes, dark/light slots), so an Appearance detail pane has nothing per-theme to show.

## Plan
1. Lane A (engine, serial): `guard_destructive` takes the floor's entries, not the resolved mode: any `no_ddl`/`read_only` entry refuses, else any `confirm` asks, else allow. Two tests in `crates/qh-ffi/tests/safe_mode.rs` (confirm+floor no_ddl+confirmed drop → refused before connect; no_ddl+floor confirm → refused). ADR-0027 addendum (Indonesian). Same lane: fix stale `mcp.rs:79-83` comment and plan §12.3 sentence. Gate: cargo test.
2. Lane B (app, while Lane A's cargo gate runs): SettingsView.swift only. (a) default row limit for new tabs in the Data pane; (b) Appearance master-detail: list grouped Dark/Light assigning the slot, detail = preview + existing global rows. Gate: swift build && swift test.
3. One batched decision message to the user: Profiles (first kind + payload schema + may it set SAFE_MODE_FLOOR), Notifications (yes/no), Wave 4 (recommend Open Quickly or nothing), MCP pane (stays deferred per settings study 14C).
4. User-only: rotate the kenari key now.

## Dropped or deferred
Item 11 (already documented), 12.2.2, MCP remainder (nothing left to build), Navicat/DataGrip research, min versions, notarization/EdDSA (blocked on Apple Developer ID), editor toggles for always-on features, Notifications, Profiles commands and UI until decided, Wave 4 except possibly Open Quickly.

## Verification
cargo test ≥ 770/0 with the two new tests; swift build && swift test ≥ 392/0; manual CLI run of `table_op` with `SAFE_MODE=confirm SAFE_MODE_FLOOR=no_ddl SAFE_MODE_CONFIRMED=1` shows the no_ddl refusal.
