---
name: camk-brainstorm
description: "Structured brainstorming and ideation workflow. Use when: (1) User wants to explore ideas, solutions, or approaches, (2) Need to evaluate multiple options before deciding, (3) Want structured output: problem framing → idea generation → evaluation → recommendation. Prevents premature convergence and ensures thorough exploration."
type: flow
---

# Brainstorm Workflow

Structured ideation that prevents premature convergence and ensures thorough exploration before recommendation.

```mermaid
flowchart TD
    BEGIN([Begin]) --> FRAME

    FRAME[Frame the problem<br/>- Restate the goal in own words<br/>- Identify constraints and boundaries<br/>- Clarify success criteria<br/>- Note implicit assumptions] --> {Problem clear?}

    {Problem clear?} --> |Yes| DIVERGE
    {Problem clear?} --> |Need refinement| REFINE

    REFINE[Refine problem statement<br/>- Break into sub-problems if too broad<br/>- Identify missing context<br/>- Ask targeted questions<br/>- Restate with user confirmation] --> FRAME

    DIVERGE[Generate ideas broadly<br/>- Brainstorm 5-10 distinct approaches<br/>- Include unconventional/outlier ideas<br/>- Mix incremental and radical solutions<br/>- Note pros/cons of each briefly] --> {Enough ideas?}

    {Enough ideas?} --> |Yes| EVALUATE
    {Enough ideas?} --> |Generate more| DIVERGE

    EVALUATE[Evaluate options systematically<br/>- Score against: feasibility, impact, effort, risk<br/>- Identify trade-offs between top candidates<br/>- Consider second-order effects<br/>- Check alignment with constraints] --> {Clear winner?}

    {Clear winner?} --> |Yes| RECOMMEND
    {Clear winner?} --> |Need comparison| COMPARE
    {Clear winner?} --> |Combine ideas| HYBRID

    COMPARE[Deep-dive comparison<br/>- Side-by-side analysis of top 2-3<br/>- Scenario testing: best case / worst case<br/>- Resource requirement breakdown<br/>- Time-to-value estimate] --> RECOMMEND

    HYBRID[Design hybrid approach<br/>- Identify complementary elements<br/>- Merge best parts of multiple ideas<br/>- Check for conflicts or contradictions<br/>- Validate against constraints] --> EVALUATE

    RECOMMEND[Make recommendation<br/>- State recommended approach clearly<br/>- Explain why it wins over alternatives<br/>- Outline implementation path<br/>- Flag risks and mitigations] --> {User satisfied?}

    {User satisfied?} --> |Yes| NEXT_STEPS
    {User satisfied?} --> |Explore more| DIVERGE
    {User satisfied?} --> |Tweak recommendation| RECOMMEND

    NEXT_STEPS[Define next steps<br/>- Immediate action items<br/>- Who does what<br/>- Decision points and timelines<br/>- How to validate the chosen path] --> END([End])
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
