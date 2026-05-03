# Quick Trigger Guide (Manual Control)

> File này giúp bạn tự inject skill vào conversation **mà không cần tin tưởng AI tự trigger**.

---

## Cách 1: Copy-Paste Prompt (Kiểm soát tối đa)

Copy đoạn dưới đây, paste vào kimi-cli khi bạn muốn design system:

```markdown
## SYSTEM DESIGN WORKFLOW

Follow this exact workflow. Do not skip steps. Ask me before making assumptions.

### Step 1: Requirements
- Functional features needed?
- Non-functional: DAU, QPS, latency, availability?
- If I don't provide numbers, ask me. Do not assume.

### Step 2: Capacity Estimation
- Calculate: RPS, storage, bandwidth
- Use back-of-envelope math
- Show your calculations

### Step 3: API Design
- REST or gRPC?
- List endpoints with methods and payloads

### Step 4: Data Model
- Logical entities and relationships
- Physical DB choice (justify SQL vs NoSQL)
- Sharding strategy if needed

### Step 5: High-Level Design
- Draw architecture: Client → CDN → LB → API Gateway → Services → Cache → DB
- Explain each component choice

### Step 6: Deep Dive (2-3 components)
- Most critical/scaling bottleneck
- Trade-offs of chosen approach

### Step 7: Trade-offs Table
| Decision | Option A | Option B | Chosen | Reason |

### Step 8: Final Document
- Structure: Requirements → Capacity → API → Data Model → HLD → Deep Dive → Trade-offs

---

Now help me design: [ĐIỀN SYSTEM CỦA BẠN VÀO ĐÂY]
```

---

## Cách 2: Dùng `/skill:` Command (Force Trigger)

Gõ lệnh này trong kimi-cli:

```
/skill:camk-system-design
```

Sau đó **bạn chỉ đạo từng bước**:

```
Bây giờ bước 1: Thu thập requirements. Hỏi tôi từng cái.
```

Khi AI hỏi xong:

```
Bước 2: Tính capacity. Dùng script nếu có số liệu.
```

Khi AI tính xong:

```
Bước 3: API Design. Chỉ design 2 endpoint chính thôi.
```

**→ Bạn kiểm soát tốc độ và phạm vi hoàn toàn.**

---

## Cách 3: Từng Bước Một (Step-by-Step Mode)

Không dùng skill. Bạn tự hỏi AI từng bước:

```
# Bước 1
"Tôi muốn design [URL shortener]. Hỏi tôi requirements để thu thập."

# Bước 2
"Với DAU 1M, tính giúp tôi capacity: RPS, storage, bandwidth."

# Bước 3
"Design API: POST /shorten và GET /:code"

# Bước 4
"Chọn database cho use case này. So sánh SQL vs NoSQL."

# Bước 5
"Vẽ high-level architecture với load balancer, cache, DB"

# Bước 6
"Deep dive vào hashing strategy cho short code."

# Bước 7
"Trade-offs: hash-based vs base62?"

# Bước 8
"Tổng hợp thành 1 document"
```

---

## Cách 4: Dùng `/plan` Mode (Approve từng bước)

```
/plan on
/skill:camk-system-design
Design a URL shortener
```

AI sẽ:
1. Chỉ đọc file (không sửa gì)
2. Viết plan
3. **Chờ bạn approve** mới chạy

Bạn có thể:
- **Approve**: Chạy theo plan
- **Reject**: Sửa plan
- **Revise**: Bảo AI sửa

---

## So sánh 4 cách

| Cách | Kiểm soát | Effort | Khi nào dùng |
|------|-----------|--------|--------------|
| Copy-paste prompt | Cao nhất | Cao | Bạn muốn tự viết prompt, không cần skill |
| `/skill:` + steering | Cao | Trung bình | Bạn muốn dùng skill nhưng chỉ đạo tay |
| Step-by-step | Cao | Cao | Bạn muốn làm từng bước nhỏ |
| `/plan` mode | Cao | Thấp | Bạn muốn AI làm nháp, bạn duyệt |

---

## Tips để kiểm soát AI tốt hơn

### 1. Luôn đặt ràng buộc
```
"Design [X]. Ràng buộc: latency < 100ms, budget thấp, không dùng managed services."
```

### 2. Yêu cầu AI hỏi trước khi assume
```
"Nếu thiếu thông tin, hỏi tôi. Đừng tự assume."
```

### 3. Giới hạn phạm vi
```
"Chỉ design đến bước API + Data Model thôi. Deep dive sau."
```

### 4. Yêu cầu justification
```
"Mỗi quyết định phải giải thích lý do. Không được chọn default."
```

### 5. Dùng `/btw` để hỏi sidebar
```
/btw Cái trade-off này có đúng không?
```
→ Hỏi nhỏ mà không làm gián đoạn main flow.

---

## Lệnh hữu ích để kiểm soát

| Lệnh | Tác dụng |
|------|----------|
| `/skill:camk-system-design` | Force load skill |
| `/plan on` | AI chỉ đọc, đợi approve |
| `/yolo` | Auto-approve (cẩn thận) |
| `/undo` | Quay lại bước trước |
| `/btw [question]` | Hỏi sidebar không gián đoạn |
| `Ctrl-C` | Dừng AI ngay lập tức |

---

## Ví dụ conversation hoàn chỉnh (Step-by-Step)

```
You: /skill:camk-system-design

You: Bây giờ chỉ làm Step 1. Hỏi tôi requirements cho 1 chat app.
AI: DAU target? Geographic? Message size limit?

You: DAU 10M, global, text + image.

You: Step 2. Tính capacity.
AI: [Tính toán]

You: Kiểm tra lại storage calculation. Tôi nghĩ số message cao hơn.
AI: [Sửa lại]

You: Step 3. API Design. Chỉ cần 3 endpoints chính.
AI: [Design API]

You: Step 4. Data Model. So sánh MongoDB vs Cassandra.
AI: [So sánh]

You: Chọn Cassandra. Vì sao?
AI: [Giải thích]

You: Step 5. HLD. Không cần CDN vì real-time.
AI: [Vẽ architecture]

You: Bỏ queue đi, dùng WebSocket trực tiếp.
AI: [Sửa lại]

You: Tổng hợp lại thành document.
AI: [Output]
```

→ **Bạn kiểm soát 100%. AI chỉ là công cụ thực thi.**
