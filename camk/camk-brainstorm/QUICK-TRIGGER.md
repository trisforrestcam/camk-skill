# Quick Trigger Guide (Manual Control)

> File này giúp bạn tự inject skill vào conversation **mà không cần tin tưởng AI tự trigger**.

---

## Cách 1: Dùng `/skill:` Command (Force Trigger)

Gõ lệnh này trong kimi-cli:

```
/skill:camk-brainstorm
```

Sau đó **chat với agent như với 1 đồng nghiệp**.

---

## Cách 2: Copy-Paste Prompt (Kiểm soát tối đa)

Copy đoạn dưới đây, paste vào kimi-cli:

```markdown
## SPEC & BRAINSTORM AGENT

Bạn là 1 senior technical product manager + staff engineer. 
Nhiệm vụ: hỏi đào sâu, explore ideas, evaluate options, và cuối cùng ra 1 spec rõ ràng.

**Quy tắc:**
- HỎI trước, assume sau
- Mỗi turn: trả lờI + đặt 1-2 câu hỏi tiếp
- Tách biệt Diverge (sinh ý tưởng) và Evaluate (đánh giá)
- Output cuối phải theo format:

```
Mục tiêu: [1 câu rõ ràng]

Context:
- [Tech stack]
- [Architecture]
- [Constraints]

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

Bây giờ hãy giúp tôi brainstorm: [ĐIỀN VẤN ĐỀ CỦA BẠN]
```

---

## Cách 3: Từng Bước Một (Step-by-Step Mode)

Không dùng skill. Bạn tự hỏi AI từng bước:

```
# Bước 1: Frame
"Tôi muốn [làm X]. Hỏi tôi 2-3 câu để hiểu rõ vấn đề."

# Bước 2: Explore
"Với context đã có, sinh 3-5 approaches khác nhau. Có 1 outlier."

# Bước 3: Evaluate
"So sánh các options. Tôi ưu tiên [speed/correctness/simplicity]."

# Bước 4: Spec
"Chuyển approach đã chọn thành spec chi tiết theo format:
Mục tiêu / Context / Spec Requirement / Non-goals / Edge cases"
```

---

## Cách 4: Dùng `/plan` Mode (Approve từng bước)

```
/plan on
/skill:camk-brainstorm
Tôi muốn brainstorm cách [làm X]
```

AI sẽ:
1. Chỉ đọc file (không sửa gì)
2. Viết plan
3. **Chờ bạn approve** mới chạy

---

## Ví dụ conversation hoàn chỉnh

```
You: /skill:camk-brainstorm

You: Tôi muốn thêm tính năng real-time notification vào app

AI: Cool. Để tôi hiểu rõ hơn:
1. App hiện tại dùng stack gì? (frontend, backend, DB)
2. Notification này trigger từ đâu? (user action, system event, scheduled?)
3. Scale hiện tại bao nhiêu users? Peak concurrent?

You: React + Node.js + PostgreSQL. Trigger từ user action. 
     Hiện tại ~10K DAU, peak ~500 concurrent.

AI: Got it. Context: React/Node/Postgres, 10K DAU, 500 concurrent, 
     user-action triggered notifications.

     Giờ explore approaches:
     1. **Polling** — client poll mỗi X giây. Đơn giản, không cần infra mới.
     2. **WebSocket** — persistent connection. Real-time, nhưng cần manage connections.
     3. **SSE (Server-Sent Events)** — one-way streaming. Lighter than WS, chỉ server→client.
     4. **Push Notification** — qua FCM/APNs. Work khi app background, nhưng phức tạp hơn.

     Bạn nghiêng về hướng nào? Hoặc có constraint gì tôi chưa biết?

You: Tôi muốn real-time nhưng không muốn thêm infra phức tạp. 
     WebSocket nghe scary.

AI: Fair. Vậy top 2 là SSE và Polling.

     **SSE:** Real-time, đơn giản hơn WS, chỉ cần 1 HTTP connection.
     **Polling:** Đơn giản nhất, nhưng không real-time + tốn resource.

     Với 500 concurrent, polling mỗi 5s = 100 req/s. Chấp nhận được.
     Nhưng nếu scale lên 10x, polling sẽ đau.

     Tôi recommend **SSE** — real-time, đơn giản, scale tốt hơn.
     Bạn OK không?

You: OK. Viết spec đi.

AI: 
Mục tiêu: Thêm real-time notification cho user actions trong app

Context:
- Frontend: React
- Backend: Node.js
- Database: PostgreSQL
- Scale: 10K DAU, 500 concurrent peak

Spec Requirement:
1. Khi user A thực hiện action X, user B (liên quan) nhận notification real-time
2. Notification phải persist trong DB để show history
3. Connection phải auto-reconnect khi mất mạng
4. Chỉ gửi notification cho users có quyền xem action đó

Non-goals:
- Push notification khi app background (scope sau)
- Group/batch notifications
- Notification preferences/settings

Edge cases cần xử lý:
- User B offline khi action xảy ra → queue và gửi khi reconnect
- Multiple tabs của cùng user → không duplicate notification
- Server restart → clients auto-reconnect

You: Perfect. Giờ tôi muốn implement.

AI: Khi ready, dùng `/skill:camk-dev` hoặc `/skill:spec-propose` để triển khai nhé.
```

→ **Bạn chat tự nhiên. Agent hỏi đào sâu, explore, recommend, rồi ra spec.**

---

## Tips để kiểm soát AI tốt hơn

### 1. Luôn đặt ràng buộc
```
"Brainstorm cách [X]. Ràng buộc: không đổi DB, timeline 2 tuần."
```

### 2. Yêu cầu AI hỏi trước khi assume
```
"Nếu thiếu thông tin, hỏi tôi. Đừng tự assume."
```

### 3. Giới hạn phạm vi
```
"Chỉ brainstorm đến bước explore thôi. Evaluate sau."
```

### 4. Yêu cầu justification
```
"Mỗi recommendation phải giải thích tại sao."
```

### 5. Dùng `/btw` để hỏi sidebar
```
/btw Cái trade-off này có bias gì không?
```
→ Hỏi nhỏ mà không làm gián đoạn main flow.

---

## Lệnh hữu ích

| Lệnh | Tác dụng |
|------|----------|
| `/skill:camk-brainstorm` | Load agent |
| `/skill:camk-dev` | Chuyển sang implement |
| `/skill:spec-propose` | Chuyển sang formal spec + tasks |
| `/skill:camk-system-design` | Chuyển sang system design |
| `/plan on` | AI chỉ đọc, đợi approve |
| `/yolo` | Auto-approve (cẩn thận) |
| `/btw [question]` | Hỏi sidebar không gián đoạn |
