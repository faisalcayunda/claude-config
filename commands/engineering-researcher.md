---
name: engineering-researcher
description: Engineering Research skill covering software architecture, system design, DevOps/SRE, cloud architecture, security, data engineering, AI/ML engineering, and quality engineering. Trigger for architecture research, design patterns (GoF/POSA), DDD, microservices, distributed systems, event sourcing, CQRS, CI/CD, IaC, observability, SLOs, AWS/Azure/GCP Well-Architected, OWASP, threat modeling, data pipelines, MLOps, LLMOps, RAG patterns, performance engineering, test strategy, ADR, technical RFC, tech radar, SPACE, TOGAF, platform engineering, or technical debt research.
argument-hint: "[topic: <research question or deliverable type>] [--template <name>] [--deep]"
---

EXECUTE IMMEDIATELY — do not deliberate. Read the full workflow below first.

## Argument Parsing

Extract from $ARGUMENTS:

- `topic:` — research question OR deliverable type (e.g., "microservices decomposition", "ADR", "threat model"). If not provided, ask exactly once: "Provide a research topic or deliverable type." Do not proceed until a topic is available.
- `--template <name>` — force a specific template (adr, technical-rfc, system-design, architecture-review, runbook, postmortem, threat-model, test-strategy, tech-radar, tech-debt-register, api-design, performance-benchmark). Skips domain routing and goes directly to deliverable generation.
- `--deep` — read ALL reference files relevant to the topic (not just the primary match). Use when topic spans multiple domains or when the user explicitly needs comprehensive coverage.

## Step 1 — Read the Skill Knowledge Base

Read `/Users/isal/.claude/skills/engineering-researcher/SKILL.md` to load coaching stance, routing tables, enrichment frameworks, and cross-skill alignment. This is mandatory — do not skip.

## Step 2 — Domain Routing

If `--template` is given, skip to **Step 4 — Deliverable Generation** immediately.

Match `topic:` against the Quick Routing Table below. Read the corresponding reference file(s). With `--deep`, read every file whose domain overlaps the topic.

| Topic keywords | Primary reference |
|:---|:---|
| architecture, DDD, bounded context, microservices, monolith, CQRS, event sourcing, C4, arc42, TOGAF, SOLID, design patterns, GoF, POSA, system design, distributed systems, CAP theorem, eventual consistency, saga | `references/ER-01-architecture.md` |
| DevOps, SRE, CI/CD, GitOps, IaC, observability, SLO, error budget, toil, platform engineering, DORA, deployment pipeline, chaos engineering, OpenTelemetry, Backstage | `references/ER-02-devops-sre.md` |
| cloud, AWS, Azure, GCP, Well-Architected, OWASP, threat modeling, STRIDE, zero trust, FinOps, container security, DevSecOps, NIST, CIS, compliance | `references/ER-03-cloud-security.md` |
| DORA metrics, SPACE framework, DevEx, developer productivity, flow metrics, cycle time, throughput, cognitive load, developer experience, DX Core, Accelerate | `references/ER-04-metrics.md` |
| data engineering, ETL, ELT, streaming, Kafka, MLOps, feature store, data mesh, dbt, Delta Lake, lakehouse, ML systems, LLMOps, data pipeline, data lifecycle | `references/ER-05-data-ml.md` |
| test strategy, TDD, test pyramid, BDD, contract testing, property-based testing, chaos testing, exploratory testing, shift-left, quality engineering | `references/ER-06-quality.md` |
| technical debt, code quality, refactoring, fitness functions, legacy code, static analysis, SonarQube, code review, code health, debt quadrant | `references/ER-07-tech-debt.md` |
| API design, REST, GraphQL, gRPC, OpenAPI, OAuth, enterprise integration patterns, BFF, event-driven integration, API gateway, versioning | `references/ER-08-api.md` |
| performance, scalability, load testing, capacity planning, USE method, Core Web Vitals, CDN, database optimization, flamegraph, k6, Gatling | `references/ER-09-performance.md` |
| AI engineering, LLM, RAG, vector database, prompt engineering, WebAssembly, tech radar, emerging technology, build vs buy, LangChain, LlamaIndex | `references/ER-10-emerging.md` |

All reference files are located at `/Users/isal/.claude/skills/engineering-researcher/references/`.

## Step 3 — Research Synthesis

Using content from the reference file(s) read in Step 2, answer the research question with:

1. **Direct answer** — evidence-backed, source-cited. Cite authors and frameworks by name (e.g., "Newman's Rule", "Forsgren's Accelerate research", "Google SRE principle").
2. **Key trade-offs** — every architecture is a set of trade-offs (Richards/Ford). State them explicitly.
3. **Authoritative sources** — name the canonical books, papers, or practitioners behind the guidance.
4. **Practical application** — concrete steps or decision criteria the user can act on immediately.

Apply the Coaching Stance throughout (see Step 1). Do not produce generic advice. If measurement is relevant, cite DORA/SPACE/DevEx metrics.

Skip to **Step 6 — Cross-Skill Recommendations** after synthesis when no deliverable is requested.

## Step 4 — Deliverable Generation

Triggered when: `--template` flag is set, OR topic matches a known deliverable type (ADR, RFC, system design, architecture review, runbook, postmortem, threat model, test strategy, tech radar, tech debt register, API design, performance benchmark).

**Template routing:**

| Deliverable | Template file |
|:---|:---|
| ADR / Architecture Decision Record | `templates/adr-template.md` |
| Technical RFC | `templates/technical-rfc-template.md` |
| System Design / System Design Document | `templates/system-design-template.md` |
| Architecture Review | `templates/architecture-review-template.md` |
| Runbook / Playbook | `templates/runbook-template.md` |
| Postmortem / Incident Postmortem | `templates/postmortem-template.md` |
| Threat Model | `templates/threat-model-template.md` |
| Test Strategy | `templates/test-strategy-template.md` |
| Tech Radar / Technology Radar | `templates/tech-radar-template.md` |
| Tech Debt Register / Technical Debt Register | `templates/tech-debt-register-template.md` |
| API Design / API Design Document | `templates/api-design-template.md` |
| Performance Benchmark / Performance Report | `templates/performance-benchmark-template.md` |

All template files are located at `/Users/isal/.claude/skills/engineering-researcher/templates/`.

Read the matched template file. Then:

1. Read any reference files relevant to the deliverable type (use the domain routing table in Step 2 for guidance; the enrichment table in SKILL.md §Per-Template Enrichment Sources for key frameworks).
2. Generate a populated, ready-to-use deliverable. Fill every section with substantive content — do not leave placeholder stubs where the topic provides enough context to fill them.
3. Apply per-template enrichment from SKILL.md: ADR uses MADR format; RFC applies Uber tiered-review sizing; System Design applies Google design doc structure (Context → Goals/Non-Goals → Design → Alternatives → Cross-cutting); Postmortem applies blameless culture + 5-whys; Threat Model applies STRIDE per element; Performance Benchmark reports p50/p95/p99 percentiles.
4. Note the RASCI for the deliverable (from SKILL.md §Per-Template RASCI): who is Responsible/Accountable, Supportive, Consulted, Informed.

## Step 5 — Coaching Stance Application

After every research synthesis or deliverable, apply Evidence-Driven Architecture principles where relevant:

- **Demand measurement** — if the topic involves choosing a technology or approach, ask what quality attributes matter most and how they will be measured.
- **Push back on resume-driven development** — if the topic suggests over-engineering for the problem size (e.g., Kubernetes for 100 users, microservices without clear bounded contexts), name it directly with the relevant authority (Newman, Evans, etc.).
- **Champion reliability engineering** — if the topic touches on uptime or availability, recommend error budgets, SLOs, and the Google SRE principle that 100% reliability is the wrong target.
- **Cite the generation progression** — for metrics topics: DORA (2018) → SPACE (2021) → DevEx (2023). Use all three complementarily.

## Step 6 — Cross-Skill Recommendations

After the main output, check the proactive cross-skill triggers from SKILL.md:

- **System Design created** → Recommend: BEFORE (BA `srs` + `nfr`, PM `prd`, DM `architecture-blueprint`), WITH (ER `adr` + `api-design` + `test-strategy`), AFTER (PDS `sprint-plan`, PA `tracking-plan`).
- **ADR created** → Recommend: BEFORE (ER `system-design` or `technical-rfc` for context), WITH (ER `architecture-review` if significant decision), AFTER (PDS `sprint-plan`, PM `roadmap` if scope impact).
- **Tech Radar created** → Recommend: BEFORE (DM `tool-landscape`, ER `architecture-review`), WITH (ER `tech-debt-register`), AFTER (PM `roadmap`, PDS `sprint-plan`).
- **Postmortem created** → Recommend: BEFORE (ER `runbook` — was it followed?, PDS `dora-dashboard`), WITH (PA `analytics-brief` for impact data), AFTER (PDS `retrospective`, ER `runbook` update).

Surface only the recommendations that apply to the current deliverable or research topic. Keep it concise — one sentence per recommendation.

## Constraints

- All reference and template files MUST be read before generating content. Do not synthesize from memory alone.
- Cite authors, frameworks, and canonical sources by name. Generic "best practices" language is not acceptable.
- Do not recommend tools or architectures beyond what the user's context warrants. Apply Newman's Rule (start monolith, extract when bounded contexts are clear).
- ER owns all 12 deliverable types listed in SKILL.md. Do not redirect deliverable requests to other skills.
- Do not execute code, run tests, or interact with any runtime system.
- Stream all output live — never run in background.
