# DAMA-DMBOK Data Quality Reference

Use this file as the primary conceptual baseline for the skill. It condenses the user-supplied `DAMA-DMBOK 2nd Edition.pdf`, especially Chapter 13 on Data Quality. If the original DAMA document is available in the thread or workspace, treat it as the authoritative source and use this file as the quick-start summary.

## Source Scope

- Source document: `DAMA-DMBOK 2nd Edition.pdf`
- Primary section used: Chapter 13, "Data Quality"
- Useful span in the supplied PDF: PDF pages 453-489
- Useful span in the printed book pages: pages 449-485

## Core DAMA Position

- High-quality data is data that is fit for purpose for its consumers. Quality depends on context and on how the data will be used.
- Data Quality Management is a program, not a one-time project. It combines planning, operational monitoring, reporting, issue management, and continuous improvement.
- Every data management discipline contributes to data quality. Strong quality requires cross-functional ownership across business, stewardship, and technology.

## Main Goals And Principles

Use these as design guardrails:

- Focus on critical data first, especially data tied to regulatory, financial, operational, or reputational risk.
- Manage quality across the full data lifecycle, not only at the point of reporting.
- Prefer prevention over repeated correction.
- Drive remediation to root cause, not only symptom cleanup.
- Anchor quality expectations in governance, standards, and measurable rules.
- Measure quality objectively and transparently.
- Embed responsibility into business processes and system controls.
- Tie reporting, issue management, and expectations to service levels.

These points come from the chapter introduction and goals or principles discussion around PDF pages 454-457.

## Critical Data

The chapter emphasizes that not all data is equally important. Prioritize data that affects:

- Regulatory reporting.
- Financial reporting.
- Business policy.
- Ongoing operations.
- Strategic differentiation.

Master Data is treated as critical by default. Use this idea when choosing which fields deserve the strictest checks, the fastest monitoring cadence, and the strongest escalation.

## Six Core Data Quality Dimensions

The skill should center its rules and findings on six commonly adopted dimensions discussed in DAMA-DMBOK via DAMA UK:

| Dimension | Working interpretation for this skill | Typical checks |
|---|---|---|
| Accuracy | Whether the data correctly represents the real-world object, event, or trusted reference. | Match to source of record, external reference match, derived-value verification, manual sampling. |
| Validity | Whether the value conforms to the allowed domain, type, format, range, or rule set. | Type checks, regex or pattern checks, code-list validation, range checks, conditional business rules. |
| Timeliness | Whether the data is current enough and available within the required latency window. | Freshness checks, SLA arrival checks, event lag, snapshot age, late-arrival rate. |
| Completeness | Whether the required records and attributes are present at the expected level. | Null analysis, mandatory-field population, dataset completeness, conditional completeness. |
| Uniqueness | Whether an entity is represented once where only one valid representation should exist. | Duplicate detection, one-current-row checks, key uniqueness, survivorship logic review. |
| Consistency | Whether representations agree within and across records, systems, time slices, or derivations. | Cross-field rules, cross-table reconciliation, temporal consistency, source-target comparison. |

The chapter also discusses related concepts such as integrity, reasonability, accessibility, and confidence. Use them when needed, but keep the six dimensions as the default framework unless the user asks for a broader model.

## DAMA-Backed Profiling Guidance

The chapter describes data profiling as statistical inspection used to discover structure, content, and quality. The summary below reflects the discussion around PDF pages 474 and 489:

- Count nulls to test presence and identify unexpected gaps.
- Inspect minimum and maximum values to spot outliers.
- Inspect minimum and maximum lengths to detect malformed content.
- Review frequency distributions to assess reasonability and defaulted values.
- Check type and format conformance, including unexpected patterns.
- Perform cross-column analysis to uncover dependencies, overlaps, or duplicate meanings.
- Perform inter-table analysis to reveal value-set overlap and likely foreign key relationships.

Profiling is only the first step. Use it to surface potential issues, then deepen the work with process analysis, lineage review, stakeholder validation, and root-cause investigation.

## DAMA View Of Rules, Metrics, And Thresholds

The chapter frames data quality dimensions as a vocabulary for measurable rules. Rules should be directly tied to business risk and important processes. Apply that idea in this skill by ensuring:

- Each important rule has a clear condition.
- Each rule has a measure or calculation.
- Each rule has a threshold or acceptance criterion.
- Each rule has a business impact statement.
- Each rule has an owner or steward and a monitoring cadence.

The chapter also shows that metrics can be expressed as positive conformance percentages or negative exception rates. Use whichever is easier to interpret for the audience, but keep it consistent within a report.

## DAMA View Of Operational Monitoring

The chapter recommends continuous monitoring by integrating controls into processing flows and by using batch measurements where set-level checks are required. Map that guidance as follows:

- In-stream checks: use for element-level or record-level controls during entry, ingestion, validation services, or stage handoff.
- Batch checks: use for dataset completeness, duplicates, reconciliation, distribution shifts, and period-close validation.
- Report both detailed rule outcomes and roll-up summaries.
- Focus monitoring on critical data elements and on relationships that have failed before or could fail after process changes.

## DAMA View Of Issue Management

The chapter recommends defined operational procedures for:

1. Diagnosing issues.
2. Formulating remediation options.
3. Resolving issues and documenting decisions.

Use an issue log or incident tracking structure that captures:

- Issue description.
- Symptom and impacted data object.
- Suspected or confirmed root cause.
- Business impact.
- Remediation options.
- Chosen resolution.
- Owner, assignee, and escalation path.
- Response time and resolution time.

This supports both operational improvement and transparency for data consumers.

## DAMA View Of SLA And Reporting

The chapter ties operational data quality control to service levels. A good Data Quality SLA should specify:

- Covered data elements.
- Associated business impacts.
- Quality dimensions for each element.
- Measurement method.
- Acceptability thresholds.
- Notification targets.
- Resolution deadlines.
- Escalation approach.

The chapter also highlights reporting categories that this skill should support:

- Data quality scorecards.
- Trend reporting.
- SLA metrics.
- Issue management status.
- Conformance to policy and governance.
- Positive effects of improvement work.

## How To Apply This Reference In The Skill

- Start with fit-for-purpose and business impact, not tool-first thinking.
- Narrow scope to critical data elements before writing a large rule inventory.
- Convert stakeholder expectations into measurable rules and thresholds.
- Use profiling to reveal candidates for rules, then confirm with stewards or SMEs.
- Prefer preventive controls and root-cause fixes where practical.
- Translate outputs into operational artifacts: rule matrix, scorecard, issue log, SLA, SOP, or monitoring design.

## Fallback Rule

If the original DAMA material is not available in a future session, continue using the six dimensions and the operational practices above as general best-practice guidance, and explicitly state that the output is based on best-practice assumptions rather than a live DAMA source check.
