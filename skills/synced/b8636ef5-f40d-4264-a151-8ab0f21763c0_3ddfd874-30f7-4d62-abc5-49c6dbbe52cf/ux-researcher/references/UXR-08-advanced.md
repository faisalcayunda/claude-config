# UXR-06: Accessibility Research

## WCAG 2.2 — POUR Principles (W3C 2023)
| Principle | Meaning | Key Criteria |
|:---|:---|:---|
| **Perceivable** | Content perceivable by all senses | Text alternatives, captions, color contrast (4.5:1 AA) |
| **Operable** | Interface navigable by all input methods | Keyboard accessible, sufficient time, no seizure triggers |
| **Understandable** | Content and operation comprehensible | Readable, predictable, input assistance |
| **Robust** | Works with current + future assistive tech | Valid HTML, ARIA roles, name/role/value |

## Accessibility Testing Checklist
| Test | Method | Tools |
|:---|:---|:---|
| Automated scan | axe-core / Lighthouse | Finds ~30-40% of WCAG issues |
| Keyboard navigation | Tab through all interactive elements | No mouse — Tab, Enter, Space, Arrow, Esc |
| Screen reader | NVDA (Windows) / VoiceOver (Mac/iOS) / TalkBack (Android) | Test reading order, landmarks, alt text |
| Color contrast | Contrast ratio checker | WebAIM, Colour Contrast Analyser |
| Zoom/reflow | Browser zoom to 200% | Content must reflow, no horizontal scroll |
| Cognitive | Plain language, clear instructions | Reading level test, user testing with diverse users |

## Severity for Accessibility Issues
| Level | Impact | Compliance |
|:---|:---|:---|
| **Critical** | Blocks access entirely (no keyboard, no alt text on key images) | WCAG A violation |
| **Serious** | Makes tasks very difficult for some users | WCAG AA violation |
| **Moderate** | Causes frustration but workaround exists | WCAG AA best practice |
| **Minor** | Cosmetic or minor inconvenience | Enhancement opportunity |

---

# UXR-07: Design System Evaluation

## Atomic Design (Frost 2016)
| Level | Definition | Example |
|:---|:---|:---|
| **Atoms** | Basic building blocks | Button, input, label, icon |
| **Molecules** | Groups of atoms functioning together | Search form (input + button) |
| **Organisms** | Complex UI sections | Header (logo + nav + search) |
| **Templates** | Page-level layouts (wireframe) | Homepage layout |
| **Pages** | Templates with real content | Actual homepage |

## Design System Evaluation Criteria
| Dimension | What to Evaluate |
|:---|:---|
| **Consistency** | Same component looks/behaves same everywhere |
| **Completeness** | All needed components exist in the library |
| **Accessibility** | Every component meets WCAG 2.2 AA |
| **Documentation** | Usage guidelines, do's/don'ts, code examples |
| **Adoption** | % of product using system components |
| **Contribution** | Process for proposing new/modified components |
| **Token coverage** | Colors, spacing, typography managed as tokens |

## Design System Maturity (Sparkbox Survey)
Stage 1: Ad hoc (no formal system) → Stage 2: Initial (unofficial patterns) → Stage 3: Growing (documented, partial adoption) → Stage 4: Mature (governance, full adoption, metrics)

---

# UXR-08: Advanced UX Methods

## Eye Tracking Patterns (Nielsen/Pernice 2010)
| Pattern | Shape | When |
|:---|:---|:---|
| **F-pattern** | Two horizontal sweeps + vertical scan | Text-heavy pages, scanning |
| **Spotted pattern** | Scattered fixations | Visual-heavy pages, browsing |
| **Layer-cake** | Horizontal lines on headings | Structured content with headings |
| **Commitment pattern** | Thorough left-to-right reading | High-motivation content |

## Desirability Study (Benedek/Miner 2002)
**Microsoft Product Reaction Cards**: 118 word cards (60% positive, 40% negative/neutral)
Process: User selects 5 cards → explains why → analyze frequency + reasoning
Measures emotional/subjective response that task metrics miss.

## Service Blueprint (Shostack 1984)
| Layer | Content |
|:---|:---|
| **Physical evidence** | What customer sees/touches |
| **Customer actions** | Steps the customer takes |
| **Line of interaction** | ─────── boundary ─────── |
| **Frontstage actions** | Employee actions visible to customer |
| **Line of visibility** | ─────── boundary ─────── |
| **Backstage actions** | Employee actions hidden from customer |
| **Line of internal interaction** | ─────── boundary ─────── |
| **Support processes** | Systems, policies, technology enabling service |

---

# UXR-09: UX Research Process & Operations

## UX Maturity Model (NNg — 6 Levels)
| Level | Name | Characteristics |
|:---|:---|:---|
| 1 | **Absent** | No UX research, no awareness |
| 2 | **Limited** | Ad hoc, inconsistent research |
| 3 | **Emergent** | Functional UX work, not yet strategic |
| 4 | **Structured** | Semi-systematic, methodology in place |
| 5 | **Integrated** | UX embedded in all product decisions |
| 6 | **User-Driven** | Organization runs on UX insights |

## Design Sprint (Knapp/GV — 5 days)
Monday: **Map** the problem → Tuesday: **Sketch** solutions → Wednesday: **Decide** on best → Thursday: **Prototype** → Friday: **Test** with 5 users
Key principle: "Prototype anything in one day" — fidelity just enough to test.

## ResearchOps 8 Pillars (Towsey/Community)
Environment, Scope, Recruitment & Admin, Governance, Knowledge Management, Tools & Infrastructure, Organizational Context, People

## Research in Agile (Sy 2007, NNg, Torres)
- **Staggered sprints**: Research 1 sprint ahead of development
- **Testing Tuesdays**: Regular weekly usability testing slot
- **Continuous discovery**: Weekly customer touchpoints (Torres)
- **Sprint demos**: Present research findings alongside dev demos

---

# UXR-10: Emerging Platforms & Content

## AI UX Research (Google PAIR + Microsoft HAX)
**Google PAIR — 6 chapters**: User Needs, Mental Models, Explainability & Trust, Data Collection, Feedback & Control, Errors & Graceful Failure
**Microsoft HAX — 18 guidelines**: Initially (set expectations), During (support interaction), When wrong (support correction), Over time (adapt)

## Voice UI Research (Pearl 2017)
Unique challenges: No visual affordances, no undo, linear interactions.
Test: Wizard of Oz (human simulates voice system) → measure task success, error recovery, satisfaction.

## UX Writing Research (Podmajersky 2019)
| Test | What | How |
|:---|:---|:---|
| **Comprehension test** | Do users understand? | Ask to paraphrase |
| **Cloze test** | Is reading level right? | Remove every 5th word, measure fill accuracy |
| **A/B test** | Which text performs better? | Compare conversions |
| **Preference test** | Which text do users prefer? | Show both, ask preference + why |

## Dark Patterns (Brignull/Gray)
5 categories: **Nagging, Obstruction, Sneaking, Interface interference, Forced action**
Research responsibility: Identify dark patterns in competitive audits. Never recommend implementing them.
