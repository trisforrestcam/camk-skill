# Decision Frameworks

Structured approaches for making technical decisions.

---

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

**When to use:** Prioritizing features, roadmap decisions.

---

## Weighted Decision Matrix

```
Option A:  (9×0.3) + (7×0.2) + (8×0.3) + (6×0.2) = 7.7
Option B:  (7×0.3) + (9×0.2) + (6×0.3) + (8×0.2) = 7.3
```

**Steps:**
1. List criteria
2. Assign weights (sum = 1.0)
3. Score each option (1-10)
4. Calculate weighted sum
5. Highest score wins

**When to use:** Comparing specific options with multiple factors.

→ Dùng `scripts/evaluate_options.py` để tính tự động.

---

## Cost-Benefit Analysis

```
Net Value = (Benefits × Probability) - (Costs × Risk)
```

**When to use:** Financial decisions, resource allocation.

---

## Eisenhower Matrix

| | Urgent | Not Urgent |
|--|--------|------------|
| **Important** | Do first | Schedule |
| **Not Important** | Delegate | Eliminate |

**When to use:** Prioritizing tasks, time management.

---

## Decision Tree

```
        [Decision]
       /    |    \
    Opt A  Opt B  Opt C
    /  \   /  \   /  \
  G1  B1 G2  B2 G3  B3
  
  G = Good outcome, B = Bad outcome
  Calculate expected value at each branch
```

**When to use:** Decisions with probabilistic outcomes.

---

## When to Use Each

| Framework | Best For | Avoid When |
|-----------|----------|------------|
| RICE | Prioritizing features | One-off technical choices |
| Weighted Matrix | Comparing specific options | High uncertainty |
| Cost-Benefit | Financial decisions | Qualitative trade-offs |
| Eisenhower | Task prioritization | Complex multi-factor choices |
| Decision Tree | Probabilistic outcomes | Simple binary choices |
| Pros/Cons List | Quick decisions | Complex multi-factor choices |

---

## Combining Frameworks

**Scenario: Chọn tech stack cho new project**

1. **Eisenhower** → Xác định decision này urgent/important?
2. **Weighted Matrix** → So sánh các stack candidates
3. **Cost-Benefit** → Tính TCO (total cost of ownership)
4. **Decision Tree** → Model các scenarios (success/failure)

**Scenario: Prioritize feature backlog**

1. **RICE** → Score từng feature
2. **Eisenhower** → Phân loại urgent/important
3. **Weighted Matrix** → Tie-breaker cho features cùng score
