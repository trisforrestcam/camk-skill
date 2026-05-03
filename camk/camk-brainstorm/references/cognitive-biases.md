# Cognitive Biases in Decision Making

> Awareness of biases helps you catch them before they derail your brainstorm.

---

## Common Biases in Brainstorming

### 1. Anchoring Bias
**What:** Dính vào idea/số đầu tiên nghe được.  
**Example:** "NgườI đầu tiên suggest dùng Redis, cả team chỉ discuss Redis."  
**Fix:** Randomize thứ tự present options. Viết ideas ra giấy trước khi discuss.

### 2. Confirmation Bias
**What:** Chỉ tìm evidence ủng hộ idea mình thích.  
**Example:** "Tôi thích Option A, nên tôi chỉ tìm pros của A, ignore cons."  
**Fix:** Assign "devil's advocate" — 1 ngườI bắt buộc argue AGAINST mỗi option.

### 3. Sunk Cost Fallacy
**What:** "Đã invest nhiều vào A nên phải chọn A."  
**Example:** "Team đã code 3 tháng trên framework X, không thể đổi."  
**Fix:** Evaluate từ zero. Ask: "Nếu bắt đầu lại từ đầu, chọn gì?"

### 4. Availability Heuristic
**What:** Đánh giá dựa trên ví dụ dễ nhớ nhất, không phải dữ kiện.  
**Example:** "Tôi nhớ 1 lần Docker fail, nên reject Docker cho mọi project."  
**Fix:** Dùng data, không dùng anecdote. Tính toán, không đoán.

### 5. Bandwagon Effect
**What:** Theo đám đông vì đám đông đang theo.  
**Example:** "Mọi ngườI đều dùng Kubernetes, nên chúng ta cũng dùng."  
**Fix:** "Nếu không có trend này, quyết định có khác không?"

### 6. Overconfidence Bias
**What:** Đánh giá thấp risk, đánh giá cao khả năng thành công.  
**Example:** "Feature này đơn giản, 1 tuần xong." (thực tế 1 tháng)  
**Fix:** Nhân estimate x2-x3. Dùng reference class forecasting.

### 7. Framing Effect
**What:** Quyết định thay đổi tùy cách present.  
**Example:** "90% survival rate" vs "10% mortality rate" — cùng data, khác feel.  
**Fix:** Present cả 2 frames. Dùng numbers thay vì words.

### 8. False Dichotomy
**What:** Chỉ thấy 2 options khi thực tế có nhiều hơn.  
**Example:** "Hoặc SQL hoặc NoSQL" — ignore NewSQL, graph DB, v.v.  
**Fix:** Force tìm option thứ 3, thứ 4 trước khi chọn.

### 9. Halo Effect
**What:** 1 điểm tốt làm sáng toàn bộ option.  
**Example:** "Google dùng cái này → chắc tốt" (ignore context khác biệt)  
**Fix:** Evaluate từng dimension độc lập.

### 10. Planning Fallacy
**What:** Underestimate time/effort cần thiết.  
**Example:** Estimate 2 tuần, thực tế 2 tháng.  
**Fix:** Dùng historical data. Nhân estimate x2 cho unknown unknowns.

---

## Bias Detection Checklist

Trước khi chốt decision, hỏi:

- [ ] Có đang dính vào idea đầu tiên không? (Anchoring)
- [ ] Có ignore evidence trái chiều không? (Confirmation)
- [ ] Có để quá khứ influence quyết định không? (Sunk Cost)
- [ ] Có đang dùng anecdote thay vì data không? (Availability)
- [ ] Có chọn vì "mọi ngườI đều làm" không? (Bandwagon)
- [ ] Estimate có quá optimistic không? (Overconfidence)
- [ ] Có present 1-sided không? (Framing)
- [ ] Có ignore option thứ 3 không? (False Dichotomy)
- [ ] Có đánh giá toàn diện không? (Halo Effect)
- [ ] Timeline có realistic không? (Planning Fallacy)

---

## Debiasing Techniques

| Technique | How |
|-----------|-----|
| **Red Team** | 1 ngườI bắt buộc argue against |
| **Pre-mortem** | Tưởng tượng project fail, tìm lý do |
| **Reference Class** | So sánh với similar projects |
| **Blind Evaluation** | Remove identifying info khỏi options |
| **Devil's Advocate** | Rotate ngườI challenge ideas |
| **Sleep On It** | Đợi 24h trước khi chốt |
| **External Review** | Nhờ ngườI ngoài team review |

→ Dùng `scripts/premortem.py` để chạy pre-mortem analysis.
