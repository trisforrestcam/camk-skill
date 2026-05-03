# Scenario Testing

> Test your ideas against different futures before committing.

---

## Best Case / Worst Case / Expected Case

For each option, define 3 scenarios:

| Scenario | Probability | Outcome | What to ask |
|----------|-------------|---------|-------------|
| **Best Case** | 10-20% | Everything goes right | "What if this works 10x better than expected?" |
| **Expected Case** | 50-60% | Most likely outcome | "What happens on a normal day?" |
| **Worst Case** | 20-30% | Things go wrong | "What if this fails completely?" |

**Template:**
```
Option: [Name]

Best Case (20%):
  - Outcome: [What happens?]
  - Impact: [How good?]
  - Preparation: [Cần chuẩn bị gì để capitalize?]

Expected Case (60%):
  - Outcome: [What happens?]
  - Impact: [How good?]
  - Preparation: [Plan for this scenario]

Worst Case (20%):
  - Outcome: [What happens?]
  - Impact: [How bad?]
  - Mitigation: [How to recover?]
  - Kill switch: [When to abandon?]
```

---

## Sensitivity Analysis

"Nếu [assumption] thay đổi, quyết định có đổi không?"

| Assumption | Current Value | If +20% | If -20% | Decision Change? |
|------------|---------------|---------|---------|------------------|
| User growth | 10%/month | 12%/month | 8%/month | |
| Dev cost | $50K | $60K | $40K | |
| Timeline | 3 months | 3.6 months | 2.4 months | |
| Team size | 5 people | 6 people | 4 people | |

**When to use:** Có assumptions quan trọng nhưng chưa verify.

---

## Pre-Mortem

"Fast forward 6 months. Project failed. Why?"

1. Imagine the project has failed
2. Work backwards to find root causes
3. Identify early warning signs
4. Plan mitigations NOW

→ Dùng `scripts/premortem.py` để chạy.

---

## Monte Carlo Thinking

Instead of single-point estimates, use ranges:

```
Bad estimate: "3 months"
Good estimate: "2-5 months (60% confidence)"

Why: Forces acknowledgment of uncertainty
```

**When to use:** High uncertainty, complex projects.

---

## Stress Testing

Deliberately push options to extremes:

| Stress Test | Question |
|-------------|----------|
| 10x Scale | "What if traffic tăng 10x ngày mai?" |
| 0.5x Resource | "What if team giảm một nửa?" |
| Competitor Move | "What if đối thủ launch tính năng tương tự?" |
| Tech Shift | "What if [technology] bị deprecated?" |
| Regulatory | "What if luật mới ban hành?" |

**When to use:** Options cần resilient lâu dài.

---

## Scenario Testing Checklist

- [ ] Defined best/expected/worst case cho mỗi option
- [ ] Identified key assumptions
- [ ] Tested sensitivity của assumptions
- [ ] Ran pre-mortem
- [ ] Stress tested với 10x scale
- [ ] Identified kill switches (khi nào abandon?)
- [ ] Planned mitigations cho worst case
