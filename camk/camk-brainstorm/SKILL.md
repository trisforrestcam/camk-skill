---
name: camk-brainstorm
description: Brainstorming and structured ideation workflow. Use when the user needs to generate ideas, evaluate options, compare approaches, make technical decisions, or plan solutions before implementation. Trigger on phrases like "brainstorm", "what are my options", "which approach should I choose", "help me decide", "evaluate trade-offs", "plan this feature", or when exploring multiple solutions to a problem.
type: flow
---

# Brainstorm Workflow

Structured ideation that prevents premature convergence.

```d2
BEGIN -> FRAME

FRAME: |md
  Frame the problem
  - Restate the goal in own words
  - Identify constraints and boundaries
  - Clarify success criteria
  - Note implicit assumptions
|

FRAME -> PROBLEM_CLEAR
PROBLEM_CLEAR: Problem clear?
PROBLEM_CLEAR -> DIVERGE: Yes
PROBLEM_CLEAR -> REFINE: Need refinement

REFINE: |md
  Refine problem statement
  - Break into sub-problems if too broad
  - Identify missing context
  - Ask targeted questions
  - Restate with user confirmation
|
REFINE -> FRAME

DIVERGE: |md
  Generate ideas broadly
  - Brainstorm 5-10 distinct approaches
  - Include unconventional/outlier ideas
  - Mix incremental and radical solutions
  - Note pros/cons of each briefly
|
DIVERGE -> ENOUGH_IDEAS

ENOUGH_IDEAS: Enough ideas?
ENOUGH_IDEAS -> EVALUATE: Yes
ENOUGH_IDEAS -> DIVERGE: Generate more

EVALUATE: |md
  Evaluate options systematically
  - Score against: feasibility, impact, effort, risk
  - Identify trade-offs between top candidates
  - Consider second-order effects
  - Check alignment with constraints
|
EVALUATE -> CLEAR_WINNER

CLEAR_WINNER: Clear winner?
CLEAR_WINNER -> RECOMMEND: Yes
CLEAR_WINNER -> COMPARE: Need comparison
CLEAR_WINNER -> HYBRID: Combine ideas

COMPARE: |md
  Deep-dive comparison
  - Side-by-side analysis of top 2-3
  - Scenario testing: best case / worst case
  - Resource requirement breakdown
  - Time-to-value estimate
|
COMPARE -> RECOMMEND

HYBRID: |md
  Design hybrid approach
  - Identify complementary elements
  - Merge best parts of multiple ideas
  - Check for conflicts or contradictions
  - Validate against constraints
|
HYBRID -> EVALUATE

RECOMMEND: |md
  Make recommendation
  - State recommended approach clearly
  - Explain why it wins over alternatives
  - Outline implementation path
  - Flag risks and mitigations
|
RECOMMEND -> USER_SATISFIED

USER_SATISFIED: User satisfied?
USER_SATISFIED -> NEXT_STEPS: Yes
USER_SATISFIED -> DIVERGE: Explore more
USER_SATISFIED -> RECOMMEND: Tweak recommendation

NEXT_STEPS: |md
  Define next steps
  - Immediate action items
  - Who does what
  - Decision points and timelines
  - How to validate the chosen path
|
NEXT_STEPS -> END
```

## Evaluation Criteria

When scoring ideas, use these dimensions:

| Criteria | Weight | Questions |
|----------|--------|-----------|
| Feasibility | High | Can we build this with current resources? |
| Impact | High | How much value does this create? |
| Effort | Medium | How long to implement? |
| Risk | Medium | What could go wrong? |
| Maintainability | Medium | How hard to maintain long-term? |

## References

- **Decision frameworks**: See `references/decision-frameworks.md`
- **Idea generation techniques**: See `references/ideation-techniques.md`
