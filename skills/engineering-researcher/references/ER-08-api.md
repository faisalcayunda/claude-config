# ER-06: Quality Engineering & Testing

## Test Pyramid (Cohn/Fowler)
```
      /  E2E  \        Few, slow, expensive, fragile
     /Integration\     Moderate amount
    /    Unit      \   Many, fast, cheap, stable
```
Modern addition: **Contract tests** between integration and E2E (Pact).

## Agile Testing Quadrants (Crispin/Gregory)
| | Technology-Facing | Business-Facing |
|:---|:---|:---|
| **Supporting team** | Q1: Unit + Component tests (automated) | Q2: Functional + Story tests |
| **Critiquing product** | Q4: Performance, Security, "-ility" testing | Q3: Exploratory, Usability, UAT |

## TDD Cycle (Beck)
1. **Red**: Write a failing test for desired behavior
2. **Green**: Write minimum code to make test pass
3. **Refactor**: Clean up while keeping tests green
Repeat. Tests = executable specification of behavior.

## Chaos Engineering Principles (Rosenthal/Netflix)
1. Build a hypothesis around **steady state** behavior
2. Vary real-world events (server failure, network partition, traffic spike)
3. Run experiments in **production** (with blast radius controls)
4. Automate experiments for continuous verification
5. Minimize blast radius

## Contract Testing (Pact)
Consumer writes expected interactions → Provider verifies against contract
Catches API breaking changes without running full E2E environments.
**Consumer-driven**: Consumer defines expectations; provider verifies compatibility.

---

# ER-07: Technical Debt & Code Quality

## Tech Debt Quadrant (Fowler 2009)
| | Reckless | Prudent |
|:---|:---|:---|
| **Deliberate** | "We don't have time for design" | "We must ship now and deal with consequences" |
| **Inadvertent** | "What's layering?" | "Now we know how we should have done it" |

## Fitness Functions (Ford/Parsons 2017)
Automated tests protecting architectural characteristics as systems evolve:
- Dependency direction tests (no domain → infrastructure imports)
- Cyclomatic complexity limits per module
- API response time budgets
- Security compliance checks in CI pipeline

## Behavioral Code Analysis (Tornhill 2015)
**Hotspot analysis**: Files changed most frequently + highest complexity = highest ROI for refactoring
**Temporal coupling**: Files that change together but shouldn't = hidden dependencies
**Knowledge maps**: Who knows which code? Single-developer hotspots = bus factor risk.

## Legacy Code Strategy (Feathers 2004)
Legacy code = "code without tests"
Approach: Find **seam** (place to inject test) → Write characterization test → Refactor safely
Seam types: Object, Preprocessing, Link seams

---

# ER-08: API Design & Integration

## REST Maturity Model (Richardson)
| Level | Description | Example |
|:---|:---|:---|
| 0 | Single URI, single verb | POST /api |
| 1 | Multiple URIs (resources) | POST /orders |
| 2 | HTTP verbs + status codes | GET /orders/123 → 200 |
| 3 | Hypermedia (HATEOAS) | Response includes links to related resources |

## API Design Principles
| Principle | Practice |
|:---|:---|
| **Consumer-first** | Design for developer experience, not internal model |
| **Consistent** | Naming, pagination, error format across all endpoints |
| **Versioned** | URL path (/v2/) or header-based versioning |
| **Documented** | OpenAPI spec as single source of truth |
| **Secure** | OAuth 2.0 + JWT, rate limiting, input validation |

## Enterprise Integration Patterns (Hohpe/Woolf)
65 patterns in categories: Messaging Channels, Message Routing, Message Transformation, Message Endpoints
Key patterns: **Aggregator**, **Content-Based Router**, **Dead Letter Channel**, **Idempotent Receiver**, **Saga**

---

# ER-09: Performance Engineering & Scalability

## USE Method (Gregg 2013)
For every resource (CPU, memory, disk, network):
- **U**tilization: % time resource is busy
- **S**aturation: Degree of queuing/backlog
- **E**rrors: Count of error events
Systematic checklist preventing ad hoc troubleshooting.

## Scale Cube (Abbott/Fisher 2015)
| Axis | Strategy | Example |
|:---|:---|:---|
| **X** | Horizontal cloning | Multiple identical instances behind load balancer |
| **Y** | Functional decomposition | Microservices splitting by function |
| **Z** | Data partitioning | Sharding by customer_id or geography |

## Core Web Vitals (Google 2020)
| Metric | Measures | Good | Poor |
|:---|:---|:---|:---|
| **LCP** | Largest Contentful Paint | ≤2.5s | >4.0s |
| **INP** | Interaction to Next Paint | ≤200ms | >500ms |
| **CLS** | Cumulative Layout Shift | ≤0.1 | >0.25 |

---

# ER-10: Emerging Technology & AI Engineering

## RAG Architecture (Lewis et al. 2020)
Query → **Retriever** (vector search over knowledge base) → Top-K chunks → **Generator** (LLM + context) → Response
Components: Embedding model, vector database, chunking strategy, re-ranking, prompt template.

## LLM Integration Patterns
| Pattern | Description | When |
|:---|:---|:---|
| **Zero-shot** | Direct prompt without examples | Simple tasks |
| **Few-shot** | Include examples in prompt | Format-sensitive tasks |
| **Chain-of-Thought** | "Think step by step" | Reasoning tasks |
| **RAG** | Retrieve context, then generate | Knowledge-intensive tasks |
| **Tool Use** | LLM calls external APIs/functions | Action-oriented tasks |
| **Fine-tuning** | Train on domain data | Specialized behavior at scale |

## Technology Radar (ThoughtWorks)
4 quadrants: **Techniques**, **Tools**, **Platforms**, **Languages & Frameworks**
4 rings: **Adopt** (proven, use), **Trial** (worth pursuing), **Assess** (explore), **Hold** (proceed with caution)
Process: Bottom-up contributions → Assessment group review → Consensus on ring placement
