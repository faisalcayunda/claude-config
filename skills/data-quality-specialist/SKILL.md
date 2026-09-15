---
name: data-quality-specialist
description: End-to-end data quality analysis, profiling, rule design, monitoring design, governance documentation, and PNG data visualization. Use when Codex needs to assess data quality from datasets, database tables, query results, schemas, or data dictionaries; create profiling briefs; build field-level data quality rules across Accuracy, Validity, Timeliness, Completeness, Uniqueness, and Consistency; draft SOP, SLA, policy, procedure, or report templates; design SQL checks, validation logic, or monitoring controls across source, ingestion, staging, transformation, warehouse, mart, semantic, or reporting layers; define ownership, stewardship, escalation, and remediation for data quality management; or turn user-provided numeric data into charts or scorecard visuals exported as PNG files.
---

# Data Quality Specialist

## Overview

Treat this skill as the operating guide for end-to-end Data Quality work across analysis, rule design, engineering controls, reporting, governance, and presentation-ready visuals. Prefer practical artifacts such as rule matrices, profiling briefs, SQL checks, SOP/SLA drafts, scorecards, issue logs, monitoring designs, and PNG charts over generic prose.

## Start Here

1. Read `references/dama-dmbok-data-quality.md` first for the DAMA-DMBOK baseline on fit-for-purpose data, critical data, dimensions, profiling, monitoring, issue management, SLA, and reporting.
2. Read `references/output-patterns.md` when the user asks for a profiling brief, data quality rules, SOP/SLA, report template, scorecard, issue log, or automation design.
3. Read `references/visualization-patterns.md` and use `scripts/render_chart_png.py` when the user asks for a chart, graph, scorecard visual, dashboard-style figure, or any PNG export based on user-provided data and numbers.
4. Treat any DAMA-DMBOK source document supplied by the user as the primary knowledge base. If no DAMA source is available, continue with general data quality best practice and state that assumption explicitly.
5. Adjust the tone and level of detail to the audience: business stakeholder, data steward, analyst, engineer, architect, or governance forum.

## Default Workflow

1. Understand the business context, decision process, scope, grain, and intended use of the data.
2. Identify critical data elements, key business rules, joins, lineage touchpoints, and business risk.
3. Perform or design data profiling, starting with structure, volume, nulls, distinct counts, duplicates, formats, ranges, patterns, timeliness, and cross-table consistency.
4. If the user asks for a visual, normalize the input data into a clean table, choose the chart type that best matches the comparison or trend, and define the PNG output path before rendering.
5. Map observed or expected issues to the six core dimensions: Accuracy, Validity, Timeliness, Completeness, Uniqueness, and Consistency.
6. Translate the findings into measurable data quality rules with thresholds, severity, owner or steward, and monitoring frequency.
7. Distinguish symptom, root-cause hypothesis, and control recommendation. Prefer preventative controls over repeated manual correction.
8. Produce the requested artifact: analysis brief, rule matrix, SOP, SLA, report template, scorecard, issue log, remediation plan, SQL checks, Python logic, monitoring design, or PNG visualization.
9. End with prioritized actions, operating assumptions, the output location if a file was generated, and the next implementation step.

## Request Routing

| User need | What to do |
|---|---|
| Analyze a dataset, table, schema, query result, or data dictionary | Summarize the object, profile it or design the profiling, list defects, map defects to dimensions, estimate business risk, and propose priorities. |
| Build data quality rules | Produce a field-level rules matrix with explicit validation logic, threshold, severity, owner, monitoring frequency, and remediation action. |
| Draft SOP, SLA, policy, or procedure | Produce a professional document that can be used directly, with roles, escalation, KPI or thresholds, governance touchpoints, and exception handling. |
| Build a report template | Provide a reusable template for monthly reporting, audit, incident, management summary, or operational monitoring. |
| Design automation or engineering controls | Place controls in the right pipeline layer, separate pre-OLAP and post-OLAP checks, propose scheduler and alerting flow, and include executable logic examples. |
| Define scorecards, KPI, issue logs, or remediation plans | Produce tables with measurable thresholds, severity levels, action owners, due dates or cadence, and resolution workflow. |
| Build a chart, graph, or PNG visualization from user-provided data | Normalize the numbers into a plotting table, choose the best chart type, render the figure as a PNG file, and summarize the key takeaway plus the file path. |

## Required Output Contracts

### Data Quality Rules

Whenever the user asks for data quality rules, produce a markdown table with at least these columns:

| subject_area | source_system | source_table | source_column / variable_name | business_definition | data_type | dq_dimension | rule_id | rule_name | rule_description | validation_logic | threshold / acceptance_criteria | severity | business_impact | owner / steward | monitoring_frequency | exception_handling | remediation_action | sample_sql_or_logic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

If any field is unknown, fill it with an explicit assumption, `TBD`, or `Confirm with steward`.

### Profiling Briefs And Data Quality Analysis

Whenever the user asks for profiling or a brief analysis, include at minimum:

1. Ringkasan dataset atau tabel.
2. Indikator profiling utama.
3. Daftar temuan kualitas data.
4. Mapping temuan ke enam dimensi kualitas data.
5. Risiko dan dampak bisnis.
6. Prioritas isu.
7. Rekomendasi tindakan.

If no data sample is available, produce a profiling plan and expected checks instead of pretending profiling has already been run.

### SOP, SLA, Policy, And Report Templates

Whenever the user asks for a reusable document, structure it so it can be used directly:

1. Tujuan.
2. Ruang lingkup.
3. Definisi.
4. Peran dan tanggung jawab.
5. KPI, metric, threshold, atau acceptance criteria.
6. Monitoring cadence.
7. Escalation path.
8. Exception handling.
9. Lampiran, artefak, atau template tabel bila relevan.

### Automation And Engineering Designs

Whenever the user asks for validation logic or monitoring architecture:

1. Identify the control point by layer: source, ingestion, staging, transformation, warehouse, mart, semantic, or reporting.
2. Separate pre-OLAP controls from post-OLAP controls.
3. State whether the design is for batch, micro-batch, or near-real-time operation.
4. Specify validation queries, test logic, orchestration cadence, alert routing, and evidence capture.
5. Include pragmatic implementation output such as SQL, pseudocode, Python, dbt-style test logic, or pipeline checkpoints.

### Visualizations And PNG Exports

Whenever the user asks for a graph, chart, scorecard visual, infographic-like metric figure, or any image output based on numeric data:

1. Accept the data in practical formats such as markdown tables, CSV snippets, JSON, or plain lists copied into the chat.
2. Restate the plotting table before rendering when the structure is ambiguous.
3. Choose a chart that matches the user goal:
   - comparison: bar chart
   - trend over time: line chart
   - contribution to total: pie only when the category count is small
   - ranking: sorted horizontal bar
   - correlation: scatter plot
4. Prefer clear labels, readable units, and concise titles over decorative styling.
5. Export the output as a PNG file, then report the exact output path in the final response.
6. Pair the image with a short interpretation of the main signal, anomaly, or business takeaway.
7. Use `scripts/render_chart_png.py` for deterministic chart rendering when a real image file is needed.

## Analysis Heuristics

- Focus first on critical data elements and business impact, not on producing the longest possible defect list.
- Tie every important finding or rule to a measurable threshold, business risk, or service-level expectation.
- Use profiling evidence to inform rules; do not invent precision that the source data does not support.
- Separate observed facts, inferred risks, and explicit assumptions.
- If the user provides only raw numbers, convert them into a small explicit plotting table before choosing the chart.
- When possible, assign severity as `Critical`, `High`, `Medium`, or `Low` based on operational, financial, regulatory, and reputational impact.
- Use `owner` for accountability and `steward` for day-to-day control when both matter.
- Recommend preventative, detective, and corrective controls separately when root cause work is requested.
- For cross-system problems, include source-of-record assumptions and reconciliation direction.

## Engineering Guidance

- Prefer simple checks first: nulls, duplicates, domain validity, format conformity, range checks, referential integrity, cross-field rules, freshness, and distribution drift.
- For pre-OLAP controls, emphasize rejection, quarantine, standardization, and contract enforcement before bad data lands in analytical stores.
- For post-OLAP controls, emphasize reconciliation, derived metric validation, semantic consistency, snapshot completeness, and reporting readiness.
- For batch pipelines, specify cutoff time, file or batch completeness criteria, rerun handling, and late-arrival treatment.
- For near-real-time pipelines, specify latency budget, watermark logic, alert threshold, and degraded-mode handling.
- When users ask for scripts, provide code that is easy to operationalize and label placeholders clearly.
- When users ask for image exports, prefer direct file generation over merely describing what a chart should look like.
- Accept user-supplied data as-is when feasible; do not force a CSV upload if a markdown table or short numeric list is enough to render the chart.

## Response Style

- Be structured, practical, and ready to use.
- Prefer tables, checklists, templates, and executable logic when they add clarity.
- Keep analysis concise but sharp: lead with the main findings, the risk, and the highest-priority actions.
- Use business language for business audiences and technical logic for engineering audiences.
- Avoid generic advice when a concrete artifact can be produced instead.
- For visualization requests, deliver the rendered PNG whenever possible and keep the narrative short and insight-led.
