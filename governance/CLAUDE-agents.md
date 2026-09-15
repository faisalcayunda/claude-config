---
title: "CLAUDE-agents.md — §13 Agent Registry"
parent: "CLAUDE.md"
included_via: "@-reference from CLAUDE.md"
effective_date: "2026-04-20"
---

> **Governance:** Pointer-include of CLAUDE.md §13. Change control per §0.4. Gate contracts for reviewer agents in §6 (CLAUDE-gates.md).

---

## 13. Agent Registry

Each entry: role, timing, I-O contract, constraints, and paired agents. Tier per §3.

### 13.1 Wave 0 Agents

#### `context-manager` *(Tier 2 — Sonnet)*
- **Role:** Session memory. Retrieves prior state at Wave 0; saves snapshot at pipeline end.
- **Runs:** Wave 0 (parallel with `prompt-engineer`) + final step of every pipeline.
- **Input:** Current task description + project path.
- **Output:** Prior decisions, active work streams, blockers, relevant patterns.
- **Do NOT use for:** Storing code or file contents — those live in the repo.

#### `prompt-engineer` *(Sonnet)*
- **Role:** Mandatory translator. Converts raw user intent into precise, agent-ready instructions.
- **Runs:** Wave 0 (parallel with `context-manager`) — before any classification, planning, or dispatch.
- **Input:** Raw user prompt + `context-manager` output.
- **Output:** Refined prompt(s), task class suggestion, decomposed sub-tasks, flagged assumptions.
- **Do NOT skip:** For any task. The orchestrator never acts on a raw user prompt.

### 13.2 Planning & Exploration

#### `Plan` *(inherits orchestrator model)*
- **Role:** Authoritative task list. No specialist runs without a plan.
- **Runs:** After Wave 0 completes, before any specialist.
- **Input:** Refined prompt from `prompt-engineer` + context.
- **Output:** Ordered task list, agent assignments, parallel/sequential groupings, identified risks.
- **Do NOT use for:** Tasks classified as Trivial.

#### `Explore` *(inherits orchestrator model)*
- **Role:** Codebase intelligence. Maps structure, finds definitions, traces call chains.
- **Input:** Specific questions about the codebase.
- **Output:** File paths, function locations, dependency maps, pattern summaries.
- **Paired with:** Runs parallel with `Plan` in Complex/Critical Wave 1.
- **Do NOT use for:** Tasks where the exact file to edit is already known.

### 13.3 Design

#### `backend-architect` *(Sonnet)*
- **Role:** Design authority for new systems. Produces API contracts, schemas, event flows — before any code is written.
- **Input:** Refined prompt + existing system context from `Explore`.
- **Output:** Service design, API spec, DB schema, event topology, ADR.
- **Paired with:** After `Explore`, before implementation. Always followed by `/autoresearch:reason` in Critical.
- **Do NOT use for:** Implementation — hand off to `python-pro` once design is done.

#### `architecture-modernizer` *(Sonnet)*
- **Role:** Migration specialist. Applies Strangler Fig, CQRS, event-driven patterns to existing systems.
- **Input:** Current architecture map (from `Explore`) + modernization goals.
- **Output:** Migration strategy, phased decomposition plan, service boundary definitions.
- **Paired with:** Replaces `backend-architect` for existing-system migration.
- **Do NOT use for:** Greenfield design — use `backend-architect`.

### 13.4 Implementation

#### `python-pro` *(Tier 2 — Sonnet)*
- **Role:** Python implementation. Writes production-quality, type-safe, async-ready code.
- **Input:** Task from `Plan` + architecture decisions + relevant file context.
- **Output:** Code changes, new files, type annotations.
- **Paired with:** Always followed by `code-reviewer`. `test-engineer` runs in parallel if scope is independent.
- **Do NOT use for:** Frontend (→ `frontend-developer`); any [DATA-WORK]-flagged work — DAG/ETL/ELT/Airflow/Prefect/Dagster/Spark/Flink/dbt/warehouse DDL (→ `data-engineer`). Exception: performance profiling of an existing non-pipeline Python codebase remains in scope.
- **Override to Opus when:** crypto, distributed consensus, or algorithm-heavy work.

#### `frontend-developer` *(Tier 2 — Sonnet)*
- **Role:** Frontend implementation across React/Vue/Angular.
- **Input:** UI requirements + API contracts + design tokens + existing component patterns.
- **Output:** TypeScript components, state management, responsive styling, accessibility compliance.
- **Paired with:** Parallel to `python-pro` when scopes don't overlap; followed by `code-reviewer` + `test-engineer`.
- **Do NOT use for:** Backend logic, API design, or infrastructure.

#### `data-engineer` *(Tier 2 — Sonnet)*
- **Role:** Data platform specialist. Designs and builds ETL/ELT pipelines, data lakes, warehouse schemas, orchestration.
- **Input:** Source/sink specs + data volume/velocity + SLA + quality requirements.
- **Output:** Pipeline code, orchestration DAGs (Airflow/Prefect/Dagster), data quality checks, cost optimization plan.
- **Paired with:** `backend-architect` for upstream API design; `test-engineer` for pipeline testing.
- **Includes:** `dags/`, `pipelines/`, `transforms/`, `jobs/`, `warehouse/`, `etl/` directories; files importing `airflow`/`prefect`/`dagster`/`dbt`/`pyspark`; warehouse DDL; pipeline SLA/quality instrumentation. Set [DATA-WORK] flag per §16.1 step 0.
- **Do NOT use for:** Application-level ORM queries or service-layer Python without pipeline context (→ `python-pro`).

#### `test-engineer` *(Tier 2 — Sonnet)*
- **Role:** Test strategy and automation. Writes unit, integration, E2E tests; enforces coverage gates; sets up CI.
- **Input:** Changed files + test requirements + coverage targets + `/autoresearch:scenario` output (if available).
- **Output:** Test files, coverage report, CI/CD test config.
- **Paired with:** Runs after implementation; parallel to `documentation-expert` in Wave 3.
- **Do NOT use for:** Running an existing test suite (→ `general-purpose`).

#### `performance-engineer` *(Sonnet) — v2.1.0*
- **Role:** Performance specialist. Profiles applications, identifies bottlenecks, designs caching strategies, runs load tests, optimizes queries.
- **Input:** Target system + current perf baseline + user-facing SLOs + load characteristics.
- **Output:** Flamegraphs, load-test scripts + results, caching plan with TTLs, ranked optimization recommendations, before/after benchmarks, monitoring dashboard spec.
- **Paired with:** After correctness confirmed; `code-reviewer` after code changes; may feed `data-engineer` if DB is the bottleneck.
- **Do NOT use for:** Functional bug debugging (→ `debugger`); infrastructure capacity planning (→ `cloud-architect`).

### 13.5 Debugging

#### `debugger` *(Sonnet)*
- **Role:** Root cause investigator for known, isolated failures.
- **Input:** Error message/stack trace + relevant code + reproduction steps.
- **Output:** Root cause + targeted fix.
- **Paired with:** `code-reviewer` after fix is applied.
- **Do NOT use for:** Multi-service cascading failures — use `error-detective`.

#### `error-detective` *(Sonnet)*
- **Role:** Cross-service failure analyst. Correlates errors across services, maps cascades, prevents recurrence.
- **Input:** Error logs, metrics, deployment timeline, service dependency map.
- **Output:** Root cause chain, cascade map, monitoring improvements, prevention recommendations.
- **Paired with:** Before `debugger` when source is unknown; after incidents for post-mortem.
- **Do NOT use for:** Single-service bugs with a known stack trace — use `debugger`.

#### `incident-responder` *(Sonnet) — v2.1.0*
- **Role:** Live-incident commander. Mobilizes response, preserves evidence, coordinates communication, drives containment and recovery, runs post-incident review.
- **Input:** Active incident signal (alert, page, ticket) + affected systems + team availability + compliance obligations.
- **Output:** Severity classification, containment actions, evidence package, stakeholder updates, recovery plan, post-incident report with action items.
- **Paired with:** `error-detective` (diagnosis) + `security-auditor` (security incidents) + `deployment-engineer` (rollback) + `cloud-architect` (infra).
- **Do NOT use for:** Post-incident debugging (→ `debugger`); past-breach audit (→ `security-auditor`).

### 13.6 Review Gates

#### `code-reviewer` *(Sonnet)*
- **Role:** Quality gate. Reviews every code change for correctness, maintainability, and best practices.
- **Input:** All changed files + task description + any prior rejection feedback.
- **Output:** **approved** OR specific revision requests with line-level feedback.
- **Timing:** Standard — alone; Complex — parallel with `architect-reviewer`; Critical — sequential after `architect-reviewer`.
- **Do NOT skip:** Any code change, regardless of size.

#### `architect-reviewer` *(Sonnet)*
- **Role:** Structural gate. Validates SOLID compliance, layer boundaries, pattern consistency.
- **Input:** Changed files + existing architecture map + relevant ADRs.
- **Output:** **compliant** OR architectural violations with refactor recommendations.
- **Timing:** Complex — parallel with `code-reviewer`; Critical — sequential before `code-reviewer`.
- **Do NOT use for:** Logic or security review — that's `code-reviewer` and `security-auditor`.

#### `security-auditor` *(Sonnet)*
- **Role:** Security assessment gate. Reviews auth, authz, input validation, data exposure, injection vectors.
- **Input:** Changed files + API surface description + data sensitivity classification.
- **Output:** **clear** OR findings with severity levels and remediation steps.
- **Paired with:** Complex/Critical security gate; re-runs after remediation.
- **Do NOT use for:** Building security infrastructure — use `security-engineer`.

### 13.7 Infrastructure & Delivery

#### `security-engineer` *(Tier 2 — Sonnet)*
- **Role:** Security infrastructure builder. Implements IAM, WAF, KMS, GuardDuty, compliance-as-code.
- **Input:** Security requirements + existing cloud config + compliance targets (SOC2/PCI/HIPAA).
- **Output:** IaC (Terraform/CDK), security automation, compliance reports, incident response runbooks.
- **Paired with:** Critical K8; followed by `security-auditor` to validate implementation.
- **Do NOT use for:** Auditing existing code — use `security-auditor`.
- **Override to Opus when:** designing novel compliance architecture for a regulated industry.

#### `deployment-engineer` *(Tier 2 — Sonnet)*
- **Role:** Delivery infrastructure. Builds CI/CD pipelines, containerization, rollout strategies, rollback automation.
- **Input:** Application stack + deployment targets + SLA/uptime requirements.
- **Output:** Pipeline config, Dockerfile, deployment strategy, health check config, rollback runbook.
- **Paired with:** Critical K10 alongside `/autoresearch:ship --dry-run`; parallel to `documentation-expert` if possible.
- **Do NOT use for:** Application code changes — route to `python-pro`.

#### `cloud-architect` *(Sonnet) — v2.1.0*
- **Role:** Cloud topology authority. Designs multi-cloud strategies, landing zones, migration plans, DR architectures, cost optimization, Well-Architected Framework compliance.
- **Input:** Business requirements, current infra, compliance targets, SLA/SLO, budget, growth projections.
- **Output:** Architecture diagrams, IaC templates (Terraform/CDK/Bicep), cost model, DR runbooks, landing-zone design, service-selection rationale.
- **Paired with:** Before `deployment-engineer` on greenfield cloud; feeds `security-engineer`; collaborates with `backend-architect` on service/cloud boundary.
- **Do NOT use for:** Application-level architecture (→ `backend-architect`); CI/CD pipeline specifics (→ `deployment-engineer`).

### 13.8 Documentation

#### `api-documenter` *(Tier 2 — Sonnet)*
- **Role:** API documentation specialist. Writes OpenAPI specs, integration guides, migration docs.
- **Input:** Route definitions + request/response schemas + versioning info.
- **Output:** OpenAPI 3.1 spec, multi-language code examples, integration guide.
- **Paired with:** Always parallel to `documentation-expert` when API surface changes.
- **Do NOT use for:** General README or architecture docs — use `documentation-expert`.

#### `documentation-expert` *(Tier 2 — Sonnet)*
- **Role:** Documentation authority. Keeps README, architecture docs, and onboarding guides in sync.
- **Input:** Summary of changes + current README + new architecture decisions.
- **Output:** Updated README, architecture doc changes, onboarding guide updates.
- **Paired with:** Final Wave 3 in all pipelines; parallel to `api-documenter`.
- **Do NOT use for:** The orchestrator never writes documentation directly.

#### `adr-generator` *(Tier 2 — Sonnet) — v2.1.0*
- **Role:** Architectural Decision Record specialist. Produces ADRs with structured Status / Context / Decision / Consequences / Alternatives sections, sequential numbering, and slug-based filenames in `/docs/adr/`.
- **Input:** Decision title, context, chosen option, alternatives considered, stakeholders, positive/negative consequences.
- **Output:** `adr-NNNN-[title-slug].md` markdown file with YAML frontmatter + standardized sections.
- **Paired with:** After architect decisions land; feeds `documentation-expert` for cross-linking.
- **Do NOT use for:** General docs (→ `documentation-expert`); API specs (→ `api-documenter`).

### 13.9 Catch-All

#### `general-purpose` *(inherits orchestrator model)*
- **Role:** Runtime verification + catch-all for multi-step research not covered by specialists.
- **Input:** Specific verification checklist or investigation question.
- **Output:** Pass/fail result with evidence, or research findings.
- **Paired with:** Runtime verification gate in all pipelines.
- **Do NOT use for:** Tasks that clearly fit a specialist — always prefer the specialist.

### 13.10 Deputy Orchestrators *(new in v2.1.0)*

All three run on **Sonnet** per 2026-05-12 operator override. Wave 0 semantics per §3.5.

#### `multi-agent-coordinator` *(Sonnet, deputy)*
- **Role:** Real-time inter-agent coordination. Designs message passing, dependency graphs, scatter-gather, saga patterns, distributed transactions, and failure propagation between agents/services.
- **Runs:** On primary delegation, or user direct invocation (Wave 0 per §3.5b).
- **Input:** Set of cooperating agents/services + their dependencies + consistency/timeout/rollback requirements.
- **Output:** Coordination topology, communication protocols, dependency graph, compensation logic, failure-handling plan.
- **Collaborates with:** `workflow-orchestrator` (business-process state), `task-distributor` (workload allocation), `error-detective` (cascade analysis).
- **Do NOT use for:** Primary orchestration; single-agent tasks; stateful processes (→ `workflow-orchestrator`); queue distribution (→ `task-distributor`).

#### `workflow-orchestrator` *(Sonnet, deputy)*
- **Role:** Business-process workflow designer. Models state machines, transitions, error/compensation paths, transactional guarantees, audit trails.
- **Runs:** On primary delegation of a stateful workflow, or user direct invocation (Wave 0 per §3.5b).
- **Input:** Business process steps + states + error conditions + SLA + compliance requirements.
- **Output:** State-machine diagram, transition rules, compensation map, dead-letter handling, monitoring/audit plan.
- **Collaborates with:** `multi-agent-coordinator` when workflow spans multiple agents; `deployment-engineer` for orchestration-engine runtimes.
- **Do NOT use for:** Technical-only workflows without business state (→ `multi-agent-coordinator`); ETL scheduling (→ `data-engineer`).

#### `task-distributor` *(Sonnet, deputy)*
- **Role:** Workload allocation across heterogeneous workers/agents. Builds priority queues, load-balancing, SLA-aware scheduling, bin-packing, starvation prevention.
- **Runs:** On primary delegation of a queue/worker-pool problem, or user direct invocation (Wave 0 per §3.5b).
- **Input:** Task set (with skills + priority + deadline) + worker pool (with capacity + skills + cost).
- **Output:** Distribution policy, queue topology, scheduling algorithm, monitoring + rebalancing rules.
- **Collaborates with:** `multi-agent-coordinator` (cross-worker coordination); `performance-engineer` (throughput tuning).
- **Do NOT use for:** Single-worker systems; sequential workflows; ETL/data-pipeline scheduling (→ `data-engineer`); stateful processes (→ `workflow-orchestrator`).

---
