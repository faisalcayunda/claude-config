---
name: affine-data-product-bootstrap
description: Bootstrap or update the documentation of ONE data product inside the BGN Digital AFFiNE workspace (PARA, data mesh, domain then data product). Reads the live MASTER_SHEET_DATA_PRODUCT Google Sheet, creates the product page, instantiates B-03 Canvas and D-02 Data Contract from the T-DP templates, files everything under the right domain folder, links the domain page, and verifies. Use whenever the user says bootstrap, initiate, init, start, or set up a data product in AFFiNE, gives a Domain plus Data Product plus shortcode (for example PEM, master-kelompok-pm), asks to add a doc such as D-05 or B-01 to an existing data product, or asks to sync a product page with the master sheet. Model-agnostic, works with any agent that has the AFFiNE MCP and Google Sheets MCP tools.
---

# AFFiNE Data Product Bootstrap

Creates (or incrementally extends) the documentation set of one data product in the
AFFiNE workspace **BGN Digital**. Domain and product naming always come from the live master sheet.
Nothing is invented: unknown values are written as `TBD`.

## 0. Constants

| Item | Value |
|---|---|
| AFFiNE base | `https://affine.nexakara.my.id` |
| Workspace ID | `b0b8ef97-b4c9-4099-a600-a905d15a23e4` (pass as `workspaceId` on EVERY AFFiNE call) |
| MCP server | `affine-bgn-digital` only. Never write BGN content to any other AFFiNE server or workspace |
| Master sheet | Google Sheet ID `17Sr9kM_4c76q4KZkUsSbWQzX4xo98UNsZelyN3hIgdE` (live source of truth) |
| START HERE doc | `vbzGWCuODtr_7rQWQSO5t` (conventions) |
| Template Manifest | `cKlWJaGbkC` (R1.0, lists every template ID) |
| Page URL | `https://affine.nexakara.my.id/workspace/<workspaceId>/<docId>` |

Template IDs used by default (all other IDs: read the manifest, section 4):

| Doc | Template ID | Instance title |
|---|---|---|
| B-03 Canvas | `VLC60dWSQL` | `B-03 · Data Product Canvas · <DOM>/<code>` |
| D-02 Data Contract | `KhDueypNuP` | `D-02 · Data Contract & Interface Specification · <DOM>/<code>` |

Known domain folders and pages (verify with `list_organize_nodes` before trusting):
PEM folder `6GdxD1S-xovw-8ejKKz6T` page `vwNcWzESRufOCYo1BZypc`; OPS folder `UjA9K6LZtYYkT38gZQqUj` page `y6cbd-9E72XalyI48TXYx`;
DIS folder `puegsovkRW1SZ8BLF1kI_` page `B7IY7QlcgxNjl7LhY1sQ3`; SIP folder `oLqRNiarfdMXrdZpXGMeJ` page `fy64wfENGSiU4jeOrdnNg`.
Parent of domain folders: `A2 · Domains` folder `H5PAhRZSbWN3w1hbUgznl` under `02 · Areas`.

Policy switch (change here if the organisation decides): `data_product_id` is **not used** by the organisation.
Identify products by `data_product_code` everywhere. Do not write `data_product_id` in pages you author.
The T-DP templates inherited from git still contain a `data_product_id` line; leave it as instantiated and mention it in the report.

## 1. Load tools

AFFiNE tools may be deferred and the name prefix differs per surface
(`mcp__affine-bgn-digital__`, `mcp__remote-devices__affine-bgn-digital__`, `mcp__claude-device__lcl-affine-bgn-digital-`).
Match by the suffix. Load in one ToolSearch call:
`list_organize_nodes, find_doc_by_title, create_doc_from_markdown, instantiate_template_native, create_folder, add_organize_link, move_organize_node, export_doc_markdown, replace_doc_with_markdown, append_semantic_section, update_doc_title`
and, for the sheet, `sheets_get_values` (and `sheets_get_metadata` if tab names are uncertain) from the Google Sheets MCP (`mcp-gsheets`).

If AFFiNE tools are absent or return "sign in first": stop and tell the user; do not try `sign_in` (it puts a password in a tool call).
If the sheet MCP is absent: ask the user for the row values, mark the product `registered_in_master_sheet: unverified`.

## 2. Inputs

Required: **domain code** (for example PEM) and **data product code exactly as in the sheet** (for example `master-kelompok-pm`).
Nothing else is needed from the user; the sheet supplies names. If the user gave only names, resolve codes from the sheet and confirm in one line.
If either is missing and the user is present, ask once (AskUserQuestion with the domain list from the sheet). If unattended, stop and say what is missing.

Never convert the code (no underscores, no prefixes such as `ops_`). Titles use `<DOM>/<code>`.

## 3. Read the live sheet (never a pasted snapshot)

Read these tabs with `sheets_get_values` (whole tab, then filter in your head or with a short script):

| Tab | Use |
|---|---|
| `data_product` | the row for the code: name, category, alignment, status, priority, classification, owner, steward, description |
| `domain` | domain code, domain name, domain owner |
| `data_product_output` | outputs of this product (count + list) |
| `documentation_directory` | official docs URL and repo, Data Product Design name |
| `Perencanaan Data Product` | planning-only rows: sources, related products, entity, data type |
| `domain_product_output_map`, `squad` | only if owner or squad is asked for |

Decide the registration state:

- **Registered**: code found in `data_product`. Use sheet values verbatim. Description: sheet wording.
- **Planned only**: found in `Perencanaan Data Product` but not `data_product`. Create the page, `registered_in_master_sheet: false`, say so in the first quote block.
- **Not found anywhere**: ask the user to confirm the code and name. Do not guess. If unattended, stop.

Blank sheet cell becomes `TBD`. Never fill owner, steward, classification, `pii_flag`, URLs, repo, table names or SLAs from guesses.
`pii_flag` is `TBD` unless the sheet or user says so; if the user states PII exists, set `true`, classification at least `Terbatas`, and D-06 becomes mandatory.
Classification scale: `Publik | Terbatas | Tertutup | Sangat Rahasia`.

## 4. Pre-checks (idempotency)

1. `find_doc_by_title` with the exact product page title (section 5). If it exists and is not in trash: **do not create a duplicate**. Switch to update mode (section 8).
2. `list_organize_nodes` once. Find the domain folder under `A2 · Domains`. If the domain folder or domain page is missing, stop and tell the user (domain bootstrap is a separate job; offer to do it from T-DOM).
3. Check whether a product folder `<code> · <name>` already exists under the domain folder.
4. Check that no other product page already uses this code under a different domain; if so, tell the user.

## 5. Create the product page

Title: `<DOM>/<code> · <data_product_name>`.
Order of work: run section 7 instantiation (B-03, D-02) first, then create this page, so the index already holds their links.
Create with `create_doc_from_markdown` using the skeleton below. Fill from the sheet. Rules for the body:

- Front matter is NOT parsed by AFFiNE: use a fenced yaml block (note: three backticks plus `yaml`) as the first block.
- Tables: maximum **20 rows** each; split longer lists (outputs) into parts with a heading each.
- No admonitions (`:::`); use blockquotes.
- Never paste secrets, NIK or any personal data. Output URLs from the sheet are not copied; point to the sheet tab.
- Language of prose: Indonesian (matches existing pages). Identifiers stay as in the sheet.

Skeleton (replace everything in angle brackets; `TBD` where the sheet is blank):

````markdown
```yaml
para: areas
doc_type: data-product-readme
domain_code: <DOM>
data_product_code: <code>
data_product_name: <name>
data_product_category: <sheet or TBD>
data_product_alignment: <sheet or TBD>
data_product_status: <sheet or TBD>
data_product_priority: <sheet or TBD>
data_classification: <sheet or TBD>
pii_flag: <TBD | true | false>
owner: <sheet or TBD>
steward: <sheet or TBD>
registered_in_master_sheet: <true | false | unverified>
source_of_truth: MASTER_SHEET_DATA_PRODUCT (Google Sheet 17Sr9kM_4c76q4KZkUsSbWQzX4xo98UNsZelyN3hIgdE; tabs data_product, data_product_output, documentation_directory)
template_source: T-DP · Data Product Docs Template (R1 · Template Library)
status: draft
version: 0.1.0
last_reviewed: <YYYY-MM-DD today>
related: [<DOM> · <domain name>, <related product pages>]
```

> Atribut identitas mengikuti MASTER_SHEET_DATA_PRODUCT; nilai kosong di sheet ditulis `TBD`, tidak dikarang. Dokumen dibuat sesuai kebutuhan dari template T-DP.
> <If planned only: "Produk ini baru ada di sheet Perencanaan Data Product dan belum terdaftar di sheet data_product.">

## 1. Ringkasan
<Sheet description verbatim or lightly condensed.> Domain: [<DOM> · <domain name>](<domain page URL>). Produk terkait: <links to existing sibling pages that the sheet or planning tab names; omit if none>.

## 2. Identitas
| **Atribut** | **Nilai** |
| --- | --- |
| Kode | `<DOM>/<code>` |
| Kategori | ... |
| Alignment | ... |
| Status | ... |
| Prioritas | ... |
| Klasifikasi | ... |
| PII | ... |
| Data Product Design (master sheet) | <documentation_directory name or TBD> |
| Dokumentasi resmi | <"terdaftar tanpa URL" / "belum terdaftar" / "lihat sheet documentation_directory"> |
| Owner / Steward | ... |

## 3. Sumber Data (dari sheet perencanaan)
<Table object data vs sumber data from Perencanaan Data Product; copy question marks as written. If no planning row: "Belum ada baris di sheet Perencanaan Data Product.">

## 4. Output Terdaftar (<N>)
<Table Output / Tipe / Format / Kategori / Arah from data_product_output. 20 rows max per table; otherwise 4.1, 4.2 ... If none: "Belum ada output terdaftar.">
<One line naming which of D-11, V-07, V-09 apply.>

## 5. Indeks Dokumen Siklus Hidup
<Use the index tables in section 6 of this skill verbatim: 5.1 Bootstrap, 5.2 Design, 5.3 Development, 5.4 Delivery/monitoring/EoSL, 5.5 Governance/PM. Mark B-03 and D-02 as draft with links after step 7; everything else "belum dibuat".>

## 6. Cara Membuat Dokumen Baru
Instantiate dari R1 · Template Library → T-DP dengan variabel domain_code=<DOM>, domain_code_lower=<dom>, domain_name=<domain name>, data_product_code=<code>, data_product_name=<name>, owner, author. Judul: `<Doc ID> · <Nama Dokumen> · <DOM>/<code>`. Tempatkan di folder produk ini, lalu perbarui tabel di atas.

## Riwayat Versi
| **Tanggal** | **Versi** | **Deskripsi** | **Penulis** |
| --- | --- | --- | --- |
| <today> | 0.1.0 | Inisiasi dari template T-DP: halaman produk, B-03, D-02 | <agent name> (draft) |
````

D-06 row: if `pii_flag` is `true`, write "WAJIB; belum dibuat". If `TBD`, write "wajib bila pii_flag true; belum dibuat".

## 6. Lifecycle index (embed in section 5 of the product page)

Doc IDs and names (status column starts as "belum dibuat"; `E-01` starts as "belum relevan"):

- 5.1 Bootstrap: B-01 Business Process Research & Data Context; B-02 Data Product Proposal; B-03 Data Product Canvas; B-04 Preliminary Data Profiling Report; B-05 Preliminary EDA.
- 5.2 Design: D-01 Data Product Design; D-02 Data Contract & Interface Specification; D-03 Data Contract (YAML); D-04 Data Catalog & Metadata; D-05 Data Quality Design; D-06 Data Risk Assessment & Privacy (RoPA, DPIA); D-09 Infrastructure Brief; D-11 Dashboard Design; D-12 SCD & Audit Logging Design; D-13 Data Product Metrics & Insights Catalog.
- 5.3 Development: V-01 Data Pipeline Brief; V-02 Data API Brief; V-03 UAT & Integration Test (includes V-04); V-05 Data Pipeline (as-built); V-06 Data API (as-built); V-07 Dashboard Development; V-08 Data Science Model; V-09 Dataset; V-10 Migration Report; V-11 Analytical Report.
- 5.4 Delivery, monitoring, EoSL: DLV-01 Consumer Onboarding Guide; DLV-02 Self-Service Infrastructure Guide; M-02 Data Quality Report (includes M-03, M-04); M-05 Backup & Disaster Recovery Plan; M-06 Change Log; M-07 Operations Runbook; E-01 End of Service Life Report.
- 5.5 Governance and PM: G-01 to G-05; PM-01 to PM-04 (may inherit the domain version); ADR-NNNN.

Phase folder names: bootstrap, design, development, delivery, monitoring (not "operations"), eosl, governance, project-management, decisions.

## 7. Instantiate B-03 and D-02, then file everything

Variables for every `instantiate_template_native` call:

```
domain_code=<DOM>  domain_code_lower=<dom>  domain_name=<domain name>
data_product_code=<code>  data_product_name=<name>
owner=<sheet owner or TBD>  author=<agent name>  org_name=Badan Gizi Nasional
```

Call without `parentDocId`, with `preserveTags` default, `allowFallback` default.
Success check: result has `unresolvedVariables: []`. If not empty, report the leftover variables; do not hand-edit silently.

Then file in the sidebar (sidebar only; folder links do not change document content):

1. `create_folder` named `<code> · <data_product_name>` under the domain folder (skip if it exists).
2. `add_organize_link` for: product page, B-03, D-02 into that product folder. If a link already sits at a wrong place, use `move_organize_node` (never delete).
3. Update the product page index so B-03 and D-02 show "draft (dari template, belum diisi)" with links (use `replace_doc_with_markdown` on your own just-created page if needed, or build the links in before creation by instantiating first).

Tip: instantiate B-03 and D-02 first, create the product page second, so the index has the links on first write.

Other documents on request ("add D-05 to X"): look the template ID up in the manifest `cKlWJaGbkC`, instantiate with the title pattern from the manifest, file it in the product folder, flip that row in the index. Create documents only on demand; never instantiate the whole set.

## 8. Update mode (page already exists)

1. `export_doc_markdown` the page. Compare against the live sheet: status, priority, classification, owner, steward, outputs count, documentation_directory, registered state.
2. Show the user a short diff (field, page value, sheet value) before writing. Apply only differences the sheet supports.
3. Prefer `replace_doc_with_markdown` for a full rewrite of a page you own, `append_semantic_section` for adding a section. If `append_semantic_section` times out (it may be waiting for an approval prompt in the desktop app), do not retry more than once; report the pending change and the exact text to add.
4. Bump `version` (patch for sync, minor for new sections), set `last_reviewed`, add a Riwayat Versi row. Never delete rows or pages; retire by moving into the sidebar folder `04 · Archives` (folder `Y2h6rkJDL2m94YTr5DMfO`, hub page `NfwM2NYowO93GyjbrvNn5`).
5. Never edit pages titled `[TEMPLATE] ...` or `[TEMPLATE-DOM] ...`.

## 9. Link the domain page

Open the domain page (`export_doc_markdown`). If its product inventory table lacks this product, add a row: code, name, status, category, link. If the page marks the product as "belum terdaftar" but the sheet now registers it, fix the row. Use `append_semantic_section` or `replace_doc_with_markdown`; respect the 20-row table limit (split by status or add a second table).
Sibling products named in the product page "Produk terkait" get a back-link line only if the user asks (it edits other owners' pages).

If a write cannot be completed (timeout, approval), do not claim it; list it under "Pending" in the report with the exact content.

## 10. Verify (do not skip)

1. `list_organize_nodes`: product folder exists under the domain folder and holds the 3 links.
2. `export_doc_markdown` on the product page, B-03 and D-02:
   - no `{{` remains; title matches the pattern; `data_product_code` equals the sheet code character for character.
   - tables are intact (no truncated rows), no tokens, passwords or personal data.
3. `find_doc_by_title` on the product title returns exactly one non-trashed match.
4. Domain page row present (or listed as pending).

## 11. Report (short)

Give: product page link, B-03 and D-02 links, folder path in plain words, registration state (registered / planned only / unverified), and a **Pending** list (domain row, back-links, TBD fields that need an owner answer such as owner, steward, `pii_flag`).
Add one line proposing the next document, normally D-01 or B-01. Do not recap the steps.

## 12. Guardrails

- Master sheet is read live every run; an uploaded xlsx is stale by definition.
- Product code is used exactly as in the sheet; the organisation does not use `data_product_id`.
- Never write credentials, NIK or personal data into docs. Never delete; archive instead.
- Never invent owners, classification, PII flags, URLs, repo names, table names. Use `TBD`.
- One product per run. If asked for several, loop sequentially and verify each before the next.
- AFFiNE is the working copy; the git templates remain the authoring source for template changes.
- If any step fails twice, stop and report what failed rather than trying alternatives that write elsewhere.
