# Data Quality Output Patterns

Use these patterns to produce operational artifacts quickly and consistently. Prefer adapting these structures rather than inventing a new format for each request.

## 1. Profiling Brief

Use this structure whenever the user asks for profiling or a brief data quality assessment.

### Suggested sections

1. Ringkasan dataset atau tabel
2. Indikator profiling utama
3. Temuan kualitas data
4. Mapping ke enam dimensi kualitas data
5. Risiko dan dampak bisnis
6. Prioritas isu
7. Rekomendasi tindakan

### Minimum profiling indicators

| Indicator | What to inspect |
|---|---|
| Row volume | Record count, partition count, batch count, or sample scope |
| Structural coverage | Column list, data types, key candidates, mandatory fields |
| Null analysis | Null rate, blank rate, conditional completeness gaps |
| Uniqueness | Duplicate keys, duplicate entities, one-current-row violations |
| Validity | Domain match, type or format mismatch, invalid codes, range violations |
| Consistency | Cross-field contradictions, cross-table mismatches, reconciliation gaps |
| Timeliness | Last refresh, event lag, late arrivals, stale snapshots |
| Distribution | Outliers, unusual spikes, unexpected default values, drift |

### Short finding format

| Finding ID | Field or object | Dimension | Observation | Risk | Priority | Recommended action |
|---|---|---|---|---|---|---|

## 2. Data Quality Rule Matrix

Use this exact column set whenever the user asks for rules.

| subject_area | source_system | source_table | source_column / variable_name | business_definition | data_type | dq_dimension | rule_id | rule_name | rule_description | validation_logic | threshold / acceptance_criteria | severity | business_impact | owner / steward | monitoring_frequency | exception_handling | remediation_action | sample_sql_or_logic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### Rule-writing guidance

- Keep one rule per row unless a combined rule is genuinely inseparable.
- Use business language in `rule_description` and executable logic in `validation_logic`.
- Put the operational expectation in `threshold / acceptance_criteria`.
- Use `sample_sql_or_logic` for a short executable example, not an essay.
- When the source is uncertain, keep the logic generic and mark the assumption.

### Severity starter

| Severity | Use when |
|---|---|
| Critical | The issue can break regulatory, financial, customer-facing, or decision-critical processes. |
| High | The issue materially distorts key operations, KPIs, or trusted reporting. |
| Medium | The issue degrades usability or efficiency but has bounded impact. |
| Low | The issue is cosmetic, isolated, or low-risk, but still worth tracking. |

## 3. Scorecard And KPI Pattern

Use this when the user asks for a scorecard, dashboard metric set, or monthly monitoring view.

| Metric ID | DQ dimension | Metric name | Formula | Threshold | Current status | Trend | Owner | Escalation trigger |
|---|---|---|---|---|---|---|---|---|

Suggested scorecard metrics:

- Completeness percentage for mandatory fields.
- Duplicate rate for key entities.
- Invalid domain rate for controlled code sets.
- Source-to-target reconciliation rate.
- Freshness compliance percentage against SLA.
- Incident volume and aging.
- Mean time to detect and mean time to resolve.

## 4. Issue Log Pattern

Use this when the user asks for issue management, audit follow-up, or remediation planning.

| issue_id | detected_date | data_object | dq_dimension | issue_summary | severity | business_impact | root_cause_hypothesis | preventive_control | detective_control | corrective_action | owner | target_resolution_date | status | escalation_level |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 5. SOP Or Procedure Pattern

Use this structure for SOP, procedure, or work instruction requests.

1. Document control.
2. Tujuan.
3. Ruang lingkup.
4. Definisi dan singkatan.
5. Peran dan tanggung jawab.
6. Prasyarat dan input.
7. Prosedur langkah demi langkah.
8. KPI atau control checkpoints.
9. Exception handling.
10. Escalation path.
11. Output records and evidence.
12. Lampiran.

## 6. SLA Pattern

Use this structure for data quality SLA drafts.

1. Purpose and business objective.
2. Covered data domains and systems.
3. Service commitments by data element or rule family.
4. Measurement method and data source.
5. Threshold and acceptance criteria.
6. Monitoring frequency.
7. Notification rules.
8. Response and resolution timeline.
9. Escalation path.
10. Roles and responsibilities.
11. Exception handling and waiver process.
12. Review cadence.

### SLA table pattern

| data_element | dq_dimension | measurement_method | threshold | monitoring_frequency | response_time | resolution_time | owner | steward | escalation_path |
|---|---|---|---|---|---|---|---|---|---|

## 7. Report Template Pattern

Use this structure for monthly reports, audit reports, incident reports, management summaries, and operational monitoring reports.

1. Executive summary.
2. Scope and period.
3. Key metrics and scorecard.
4. Major findings.
5. Top incidents or exceptions.
6. Root-cause themes.
7. Remediation progress.
8. Risks and decisions needed.
9. Planned next actions.
10. Appendix.

### Operational monitoring appendix

| rule_id | rule_name | execution_time | records_tested | exceptions_found | pass_rate | threshold | status | owner |
|---|---|---|---|---|---|---|---|---|

## 8. Automation And Engineering Design Pattern

Use this when the user asks for monitoring architecture, SQL checks, or validation-layer design.

### Required design elements

1. Business objective and failure impact.
2. Data flow summary.
3. Control points by pipeline layer.
4. Pre-OLAP validations.
5. Post-OLAP validations.
6. Execution mode: batch, micro-batch, or near-real-time.
7. Scheduler or orchestration cadence.
8. Alerting and notification flow.
9. Evidence store, issue log, and rerun handling.
10. Sample SQL, pseudocode, or Python logic.

### Pipeline control pattern

| Layer | Control objective | Check examples | Action on failure |
|---|---|---|---|
| Source | Prevent bad data creation | Mandatory fields, UI edits, reference lookup, key validation | Reject, block submission, guided correction |
| Ingestion | Enforce contract and delivery quality | File count, schema match, freshness, duplicate batch ID | Reject, quarantine, replay |
| Staging | Validate raw landing quality | Null spikes, type mismatch, malformed values, referential check | Quarantine rows, tag exceptions |
| Transformation | Protect business-rule integrity | Cross-field rules, derivation checks, mapping completeness | Fail job, branch to exception path |
| Warehouse | Preserve trusted history and reconciliation | Source-target count match, key uniqueness, SCD correctness | Stop publish, reconciliation ticket |
| Mart or semantic | Protect analytical logic | Metric consistency, dimensional conformity, snapshot completeness | Hold downstream refresh |
| Reporting | Protect user-facing outputs | KPI tie-out, threshold breach, stale report detection | Suppress publication, notify owners |

## 9. SQL And Logic Response Pattern

When users ask for executable validation logic:

- Start with a short statement of the rule intent.
- Provide the SQL or pseudocode.
- State assumptions such as table names, date fields, or system-of-record.
- Explain what constitutes pass, warning, and fail.

Example skeleton:

```sql
-- Rule intent: ensure one active customer row per customer_id
select
  customer_id,
  count(*) as active_row_count
from dim_customer
where is_current = 1
group by customer_id
having count(*) > 1;
```

Interpretation:

- No returned rows: pass.
- Returned rows above threshold: fail and open a duplicate-entity incident.

## 10. Assumption Pattern

When the input is incomplete, add a short block such as:

```text
Assumptions:
1. `customer_id` is the business key.
2. `crm_customer` is the source of record.
3. Monitoring is daily unless otherwise noted.
```

Use assumptions to keep momentum while making uncertainty explicit.
