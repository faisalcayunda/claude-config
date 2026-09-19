# UXR-01: Usability Testing

## Usability Test Types
| Type | Format | Best For |
|:---|:---|:---|
| **Moderated in-person** | Facilitator + participant in lab | Complex flows, sensitive tasks, deep probing |
| **Moderated remote** | Video call with screen share | Geographic diversity, faster recruitment |
| **Unmoderated remote** | Participant completes tasks solo | Scale, speed, quantitative benchmarks |
| **RITE** (Medlock) | Fix issues between sessions | Rapid iteration, agile context |
| **Benchmark** | Standardized tasks + SUS/metrics | Tracking progress over time |

## 5-User Testing (Nielsen/Landauer 1993)
Mathematical model: P(n) = 1 - (1 - λ)^n where λ ≈ 0.31
Result: **5 users find ~85% of usability problems**
Best practice: Run 3 rounds of 5 users with fixes between rounds rather than 1 round of 15.

## Think-Aloud Protocol (Ericsson/Simon)
| Level | What Participant Does | Reactivity |
|:---|:---|:---|
| **Level 1** | Verbalize internal speech | Non-reactive (Fox et al. 2011 meta-analysis) |
| **Level 2** | Describe visual/spatial processing | Non-reactive |
| **Level 3** | Explain reasoning (why) | REACTIVE — may alter behavior |
Best practice: Use Level 1-2 during tasks. Save "why" questions for post-task interview.

## RITE Method (Medlock et al. 2002)
1. Test participant 1 → identify critical issues
2. Fix issues immediately (same day/next day)
3. Test participant 2 with fixed design → find new issues
4. Repeat until design stabilizes (~3-5 participants total)
Advantage: Higher fix-to-problem ratio than traditional formative testing.

## Core Usability Metrics (Sauro/Lewis, Albert/Tullis)
| Metric | Measure | Benchmark |
|:---|:---|:---|
| Task completion rate | % completing task successfully | 78% average (Sauro) |
| Time on task | Seconds/minutes to complete | Compare vs. expert time |
| Errors | Count of missteps/wrong paths | Lower is better |
| Satisfaction (post-task) | SEQ, ASQ, or SUS | SUS 68 = 50th percentile |
| Learnability | Performance change across trials | Improvement curve slope |

---

# UXR-02: Heuristic Evaluation & Expert Review

## Nielsen's 10 Usability Heuristics (1994)
| # | Heuristic | Key Question |
|:---|:---|:---|
| H1 | Visibility of system status | Does the system show what's happening? |
| H2 | Match between system and real world | Does it use familiar language/concepts? |
| H3 | User control and freedom | Can users undo/redo easily? |
| H4 | Consistency and standards | Are similar things done the same way? |
| H5 | Error prevention | Does design prevent errors before they occur? |
| H6 | Recognition rather than recall | Is information visible, not memorized? |
| H7 | Flexibility and efficiency of use | Are there shortcuts for experts? |
| H8 | Aesthetic and minimalist design | Is every element necessary? |
| H9 | Help users recognize/recover from errors | Are error messages helpful + actionable? |
| H10 | Help and documentation | Is help available when needed? |

## Severity Rating Scale (Nielsen 1995)
| Rating | Label | Description |
|:---|:---|:---|
| 0 | Not a problem | Evaluator disagrees it's an issue |
| 1 | Cosmetic | Fix only if extra time available |
| 2 | Minor | Low priority — causes slight delay |
| 3 | Major | High priority — significantly impairs use |
| 4 | Catastrophic | Must fix — prevents task completion |

## Cognitive Walkthrough (Wharton et al. 1994)
For each step in a task, ask 4 questions:
1. Will the user try to achieve the right effect?
2. Will the user notice the correct action is available?
3. Will the user associate the correct action with the desired effect?
4. If the correct action is performed, will the user see progress?

## Evaluation Method Comparison
| Method | Evaluators | Time | Finds | Limitation |
|:---|:---|:---|:---|:---|
| Heuristic evaluation | 3-5 experts | 1-2 hours each | Breadth of issues | False positives (Cockton) |
| Cognitive walkthrough | 1-3 analysts | 30 min per task | Learnability issues | Narrow focus |
| Usability test | 5 participants | 1 hour each | Real user problems | Time + cost |
| Expert review | 1-2 senior UX | 2-4 hours | Design patterns | Evaluator bias |

---

# UXR-03: Qualitative UX Research

## Contextual Inquiry (Holtzblatt/Beyer)
Master/apprentice model: researcher observes user in their real context.
4 principles: **Context** (go to the workplace), **Partnership** (collaborate), **Interpretation** (share understanding in real-time), **Focus** (keep research question in mind)
Output: Affinity diagram, sequence models, flow models, artifact models

## Interview Techniques (Portigal 2023)
| Technique | How | When |
|:---|:---|:---|
| **Grand tour** | "Walk me through a typical day" | Opening — establishes context |
| **Mini tour** | "Tell me more about that step" | Depth — explores specific area |
| **Example** | "Can you show me an example?" | Evidence — grounds abstract claims |
| **Contrast** | "How is that different from...?" | Comparison — reveals mental models |

## Mental Models (Young 2008)
Diagram structure: **Behavior towers** (top) aligned against **Product support** (bottom)
Gaps where behaviors lack product support = design opportunities.

## Diary Study Designs (Bolger et al. 2003)
| Design | When Entries Made | Best For |
|:---|:---|:---|
| **Interval-contingent** | Fixed schedule (daily/weekly) | Routine behaviors |
| **Signal-contingent** | Random prompt (ESM) | In-the-moment experience |
| **Event-contingent** | After specific event occurs | Trigger-based behaviors |

---

# UXR-04: Information Architecture & Navigation

## Card Sorting Types (Spencer 2009)
| Type | Participants Do | Output |
|:---|:---|:---|
| **Open sort** | Group items + name groups | Discover user mental models |
| **Closed sort** | Place items into pre-defined groups | Validate existing categories |
| **Hybrid** | Place items + suggest new groups | Best of both |

Sample size: **20-30 participants** for stable results (Tullis/Wood 2004)
Analysis: Cluster analysis, similarity matrix, dendrogram

## Tree Testing
Test the IA structure without visual design influence.
Present hierarchical text tree → ask participants to find items → measure:
- **Success rate**: % finding correct location
- **Directness**: % going straight to correct path (no backtracking)
- **Time to complete**: Speed of navigation

## First-Click Testing (Bailey/Wolfson 2006)
Key finding: **Correct first click → 2-3x higher task completion**
If first click is wrong, only 46% eventually succeed. If right, 87% succeed.
Implication: Invest heavily in clear, obvious entry points.

---

# UXR-05: Quantitative UX Metrics

## System Usability Scale — SUS (Brooke 1996)
10 items, alternating positive/negative, 5-point Likert (Strongly Disagree → Strongly Agree)
Scoring: For odd items: score - 1. For even items: 5 - score. Sum × 2.5 = SUS (0-100)

| SUS Score | Percentile | Grade | Adjective |
|:---|:---|:---|:---|
| >80.3 | 90th | A | Excellent |
| 68 | 50th | C | OK |
| 51 | 15th | F | Poor |

Two-factor structure (Lewis/Sauro 2009): Items 4,10 = Learnability; Items 1,2,3,5,6,7,8,9 = Usability

## Ultra-Short Alternatives
| Scale | Items | Correlation w/SUS | Best For |
|:---|:---|:---|:---|
| **UMUX** (Finstad) | 4 items | r = 0.96 | Quick post-task assessment |
| **UMUX-LITE** (Lewis) | 2 items | r = 0.83 | Ultra-quick check |
| **SEQ** (Single Ease Question) | 1 item (7-point) | — | After each task |

## UX Benchmarking Process
1. Define tasks (3-5 representative scenarios)
2. Choose metrics: task success, time, SUS, SEQ
3. Establish baseline (test current version)
4. Set targets (e.g., SUS from 62 to 72)
5. Re-test after changes with same tasks/metrics
6. Compare with confidence intervals (Sauro: ±12.5 for SUS at n=12)
