# Decision Frameworks

Structured approaches for making technical decisions.

## RICE Scoring

```
RICE = (Reach × Impact × Confidence) / Effort
```

| Factor | Scale | Question |
|--------|-------|----------|
| Reach | 1-10 | How many users affected? |
| Impact | 0.25-3 | How much does it help? (0.25=minimal, 3=massive) |
| Confidence | 0-100% | How sure are we about estimates? |
| Effort | Person-months | How much work required? |

## Weighted Decision Matrix

```
Option A:  (9×0.3) + (7×0.2) + (8×0.3) + (6×0.2) = 7.7
Option B:  (7×0.3) + (9×0.2) + (6×0.3) + (8×0.2) = 7.3
```

## Cost-Benefit Analysis

```
Net Value = (Benefits × Probability) - (Costs × Risk)
```

## When to Use Each

| Framework | Best For | Avoid When |
|-----------|----------|------------|
| RICE | Prioritizing features | One-off technical choices |
| Weighted Matrix | Comparing specific options | High uncertainty |
| Cost-Benefit | Financial decisions | Qualitative trade-offs |
| Pros/Cons List | Quick decisions | Complex multi-factor choices |
