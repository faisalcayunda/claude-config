# QueryHive release-readiness verdict (advisor, read-only)

## Framing correction
- v0.1.0 is already published: public repo, GitHub "Latest", not a pre-release, 2026-09-28 23:16Z, assets DMG + appcast.xml (`gh release list`, `gh release view v0.1.0`).
- Tag v0.1.0 = f5340a9. HEAD is 70 commits / 213 files / +39k lines past it.
- The EdDSA key exists: keychain item svce `https://sparkle-project.org`, acct `ed25519`, created 2026-09-28. The live appcast carries `sparkle:edSignature`.
- `crates/qh-ffi/Cargo.toml` still says 0.1.0, and `app/release.sh` refuses to run because the tag exists.
- So the real question is whether HEAD can go out as the next version (0.2.0) and be pushed by Sparkle onto an installed 0.1.0.

## Verdict
Ship HEAD as 0.2.0, a normal (non-pre-release) release, once four things are true:
1. Blocker: the 60 s statement timeout is on by default (`AppModel.swift:2427`, passed at :3098) and applies to export, to_table, preview and count (`commands.rs:808/985/1357/1614`). On Trino that means `query_max_run_time=60000ms`, so any export or CTAS longer than 60 s gets killed. This contradicts the README. Default it to 0, or leave export/to_table unbounded.
2. Version bump plus new release notes (`docs/releases/v0.2.0.md`). Fix the macOS 15+ install wording in the notes and at `README.md:40`.
3. Copy the real app DB, run the HEAD build against the copy (isolated path), and confirm the 6 new migrations apply with the data intact. v0.1.0 refuses a newer DB, so after the update the only way back is a file copy.
4. Postgres live suite at 0 unexplained failures, plus one manual `:name` run against live Postgres.
After publishing: watch the installed 0.1.0 take the update. This is the first real run of the Sparkle path.
