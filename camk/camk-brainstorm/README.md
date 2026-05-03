# camk-brainstorm

**Spec & Brainstorm Agent** — 1 senior TPM + staff engineer trong conversation. Chat với agent để explore ideas, evaluate options, và ra spec rõ ràng.

## Khi nào dùng

- Brainstorm ideas, solutions
- Evaluate options, compare approaches
- Make technical decisions
- Draft specs before implementation
- Bất kỳ khi cần "nghĩ trước khi làm"

## Cách dùng

```bash
# Load agent
/skill:camk-brainstorm

# Rồi chat tự nhiên như với đồng nghiệp
"Tôi muốn thêm real-time notification vào app"
"Nên chọn SQL hay NoSQL cho use case này?"
"Brainstorm cách optimize API latency"
```

## Conversation Flow

```
UNDERSTAND → EXPLORE → REFINE → SPEC → DONE
```

Agent sẽ:
1. **Hỏi đào sâu** — hiểu context, constraints, assumptions
2. **Explore ideas** — sinh 3-5 approaches, có 1 outlier
3. **Evaluate & recommend** — so sánh, tìm trade-offs, chọn hướng
4. **Output spec** — format chuẩn: Mục tiêu / Context / Spec / Non-goals / Edge cases

## Output Format

```markdown
Mục tiêu: [1 câu rõ ràng]

Context:
- [Tech stack / framework]
- [Architecture pattern]
- [Database / API / service]

Spec Requirement:
1. [Feature A]
2. [Feature B]
3. [Constraint]

Non-goals:
- [Cái không làm]

Edge cases:
- [Case 1]
- [Case 2]
```

## Files

| File | Mục đích |
|------|----------|
| `SKILL.md` | Agent persona + conversation rules + workflow |
| `QUICK-TRIGGER.md` | 4 cách kiểm soát AI + ví dụ conversation |
| `scripts/evaluate_options.py` | Tính weighted scoring matrix |
| `scripts/premortem.py` | Pre-mortem analysis |
| `assets/brainstorm-template.md` | Template cho brainstorm session |
| `assets/decision-log-template.md` | Ghi lại decisions |
| `references/ideation-techniques.md` | 8 kỹ thuật sinh ý tưởng |
| `references/decision-frameworks.md` | 5 framework đánh giá |
| `references/cognitive-biases.md` | 10 cognitive biases + debiasing |
| `references/scenario-testing.md` | Best/worst case, stress testing |

## Handoff

Khi spec ready, chuyển sang:
- `/skill:camk-dev` — Implement
- `/skill:spec-propose` — Formal spec + tasks
- `/skill:camk-system-design` — Architecture design
