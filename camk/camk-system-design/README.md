# camk-system-design — Hướng dẫn tác giả (Author Guide)

> **Lưu ý:** File này dành cho ngườiv iết/maintain skill. AI sẽ không tự động đọc file này khi skill hoạt động.

---

## 1. Mục đích skill

Skill này hướng dẫn AI thiết kế distributed systems theo workflow có cấu trúc 8 bước, từ requirements gathering đến final design document.

**Phạm vi:**
- System design interview prep
- Design scalable web applications
- Capacity planning và infrastructure sizing
- Technology selection (database, cache, queue, LB)

---

## 2. Cấu trúc thư mục

```
camk-system-design/
├── SKILL.md                              ← File duy nhất kimi-cli quan tâm
│   ├── YAML frontmatter (metadata)       ← Luôn trong system prompt
│   └── Markdown body (instructions)      ← Load khi skill trigger
├── references/                           ← "Từ điển tra cứu" — AI đọc khi cần
│   ├── capacity-estimation.md
│   ├── database-patterns.md
│   ├── scaling-patterns.md
│   └── system-design-examples.md
├── scripts/                              ← "Máy tính" — AI chạy qua Shell tool
│   ├── capacity_calc.py
│   └── estimate_resources.py
├── assets/                               ← "Template" — AI copy cho output
│   └── design-doc-template.md
└── README.md                             ← File bạn đang đọc (không dùng bởi AI)
```

---

## 3. Cơ chế Progressive Disclosure (3 Levels)

Kimi-cli quản lý context theo 3 level để tiết kiệm token:

### Level 1: Metadata (Always in context)

**File:** `SKILL.md` dòng 1-5 (YAML frontmatter)

**Nội dung được load:**
```yaml
name: camk-system-design
description: System design and architecture workflow...
```

**Khi nào load:** Mỗi khi kimi-cli khởi động, scan `~/.kimi/skills/` và inject tất cả metadata vào system prompt.

**Kích thước:** ~100-200 words.

**Tác dụng:** Giúp AI biết skill tồn tại và quyết định có trigger không.

> **Quan trọng:** `description` là **duy nhất** trigger mechanism. AI không nhìn thấy body khi quyết định trigger. Nếu description quá ngắn/generic, skill sẽ "vô dụng" vì AI không bao giờ trigger.

### Level 2: SKILL.md Body (Load khi trigger)

**File:** Toàn bộ `SKILL.md` sau dòng `---` (phần Markdown)

**Nội dung được load:** Workflow, instructions, references link.

**Khi nào load:**
```
User: "Design a URL shortener"
    ↓
AI nhìn system prompt, thấy description của camk-system-design
    ↓
AI quyết định: "Tôi cần đọc SKILL.md này"
    ↓
Kimi-cli gọi read_skill_text() → đọc file → append vào conversation context
```

**Kích thước:** Khuyến nghị < 500 lines (~3000-5000 words).

**Tác dụng:** Hướng dẫn AI cách thực hiện task.

> **Quan trọng:** Skill này là **standard skill** (không có `type: flow`), nên AI có thể linh hoạt. Không bắt buộc follow từng bước tuần tự.

### Level 3: Bundled Resources (AI chủ động)

**Files:** `references/*`, `scripts/*`, `assets/*`

**Khi nào load:** Không tự động. AI phải chủ động:
- Đọc references: dùng `ReadFile` tool
- Chạy scripts: dùng `Shell` tool
- Copy assets: dùng `ReadFile` hoặc `cp`

**Kích thước:** Không giới hạn (vì không load vào context trừ khi cần).

---

## 4. Chi tiết từng thành phần

### 4.1 SKILL.md — Frontmatter

```yaml
---
name: camk-system-design
description: System design and architecture workflow...
---
```

**Cơ chế parse:**
- Kimi-cli dùng `parse_frontmatter()` để đọc YAML block
- `name`: skill identifier (dùng cho `/skill:name` và `/flow:name`)
- `description`: Được inject vào system prompt để AI quyết định trigger

**Ảnh hưởng đến skill:**
- Description quá ngắn → AI không trigger → skill "chết"
- Description không có trigger keywords → AI không biết khi nào dùng
- Description quá dài (>1024 chars) → tốn context

**Best practice đã áp dụng:**
- Mở đầu bằng "Use when..." để AI biết context
- Liệt kê trigger phrases cụ thể
- Nhắc đến các loại task phổ biến (URL shortener, chat, rate limiter...)

### 4.2 SKILL.md — Body

**Cấu trúc:**
```markdown
# System Design Workflow

## Quick Start
Khi skill trigger, AI làm gì đầu tiên...

## Core Workflow
### 1. Gather Requirements
...
### 2. Capacity Estimation
...

## When to Use References
| Reference | When to Read |

## When to Use Scripts
| Script | When to Run |

## When to Use Assets
| Asset | When to Use |
```

**Cơ chế load:**
- Kimi-cli append toàn bộ nội dung vào conversation context
- AI đọc và follow instructions

**Ảnh hưởng đến skill:**
- Body quá dài → chiếm context window, AI có thể bị "quá tải"
- Body không có "When to Use" sections → AI không biết khi nào đọc references
- Thiếu "Quick Start" → AI không biết bắt đầu từ đâu

**Best practice đã áp dụng:**
- Giữ body < 500 lines (hiện tại ~180 lines)
- Bảng "When to Use" cho từng loại resource
- Quick Start ngắn gọn (3 bullets)
- Workflow numbered để AI có structure

### 4.3 References

**Mục đích:** Cung cấp chi tiết chuyên sâu mà không làm SKILL.md bị phình to.

**Cơ chế:**
```
AI đang thiết kế database
    ↓
Nhớ trong SKILL.md có ghi: "See references/database-patterns.md"
    ↓
AI gọi ReadFile("references/database-patterns.md")
    ↓
Nội dung được load vào context
    ↓
AI dùng thông tin để quyết định SQL vs NoSQL
```

**Từng file:**

| File | Nội dung | Khi AI đọc |
|------|----------|------------|
| `capacity-estimation.md` | Formulas, time conversions, server throughput | Bước 2: Capacity Estimation |
| `database-patterns.md` | SQL vs NoSQL, sharding, replication | Bước 4: Data Model |
| `scaling-patterns.md` | Caching, LB, CDN, queues | Bước 5: HLD |
| `system-design-examples.md` | Patterns từ URL shortener, chat, news feed | Bước 6: Deep Dive |

**Ảnh hưởng đến skill:**
- References giúp SKILL.md gọn nhẹ
- AI chỉ đọc khi cần → tiết kiệm token
- Nhưng nếu AI không đọc → có thể miss thông tin quan trọng

**Mitigation:** Trong SKILL.md, ghi rõ "When to Read" cho từng reference.

### 4.4 Scripts

**Mục đích:** Thực hiện tính toán deterministic thay vì AI tự tính.

**Cơ chế:**
```
AI cần tính capacity
    ↓
Thấy trong SKILL.md: "Use scripts/capacity_calc.py"
    ↓
AI gọi Shell tool:
    Shell(command="python3 scripts/capacity_calc.py --dau 1000000 ...")
    ↓
Script chạy → output trả về AI
    ↓
AI dùng output (không cần đọc source code)
```

**Từng file:**

| File | Input | Output |
|------|-------|--------|
| `capacity_calc.py` | DAU, requests/user, payload, read ratio | RPS, bandwidth, storage |
| `estimate_resources.py` | Peak RPS, storage TB | Số servers, DB nodes, cache nodes |

**Key advantage:** Script chạy mà **không cần load source vào context**. AI chỉ thấy output, tiết kiệm rất nhiều token.

**Ảnh hưởng đến skill:**
- Scripts đảm bảo tính toán chính xác (AI đôi khi tính sai)
- Scripts có thể chạy nhiều lần với tham số khác nhau
- Nếu script lỗi → AI có thể đọc source để debug

### 4.5 Assets

**Mục đích:** Template cho output cuối cùng.

**Cơ chế:**
```
AI đang ở bước cuối (Final Design Document)
    ↓
Thấy trong SKILL.md: "Use assets/design-doc-template.md"
    ↓
AI đọc template
    ↓
AI copy structure và điền nội dung
    ↓
Trả về user 1 document hoàn chỉnh
```

**File:** `design-doc-template.md`
- 8 sections tương ứng với workflow
- Có placeholders để AI điền
- Đảm bảo output consistent giữa các lần chạy

**Ảnh hưởng đến skill:**
- Output có structure chuẩn
- User dễ đọc, dễ so sánh giữa các design
- AI không cần tự nghĩ structure → tiết kiệm thinking effort

---

## 5. Ví dụ toàn bộ flow

**Input:** User nói "Design a URL shortener like TinyURL"

### Step 1: Metadata Trigger
- Kimi-cli inject vào system prompt: `camk-system-design: System design and architecture...`
- AI thấy trigger phrase "design a system" trong description
- AI quyết định trigger skill

### Step 2: Load SKILL.md Body
- Kimi-cli đọc toàn bộ `SKILL.md`
- AI thấy workflow 8 bước
- AI bắt đầu với Step 1: Gather Requirements

### Step 3: Gather Requirements
- AI hỏi user hoặc assume:
  - DAU: 1M users
  - Write: 1000 URLs/second
  - Read: 10,000 redirects/second
  - Latency: < 100ms for redirect

### Step 4: Capacity Estimation
- AI thấy instruction: "Use scripts/capacity_calc.py"
- AI chạy script với số liệu
- Script output: Peak RPS, storage, bandwidth
- AI dùng số liệu này

### Step 5: API Design
- AI tự thiết kế (không cần reference):
  - POST /shorten → trả short URL
  - GET /:shortCode → redirect

### Step 6: Data Model
- AI thấy instruction: "See references/database-patterns.md"
- AI đọc reference
- Reference gợi ý: key-value DB phù hợp
- AI chọn DynamoDB/Cassandra

### Step 7: HLD
- AI thấy instruction: "See references/scaling-patterns.md"
- AI đọc reference (nếu cần gợi ý caching/LB)
- AI vẽ architecture:
  ```
  Client → LB → API Gateway → Shorten Service → DB
                           ↘  Cache (Redis)
  ```

### Step 8: Deep Dive
- AI thấy instruction: "See references/system-design-examples.md"
- AI đọc reference
- Thấy pattern cho URL shortener: base62 encoding, consistent hashing
- AI áp dụng

### Step 9: Trade-offs
- AI tự evaluate (không cần reference):
  - Hash-based vs range-based sharding
  - Cache-aside vs write-through

### Step 10: Final Document
- AI thấy instruction: "Use assets/design-doc-template.md"
- AI đọc template
- AI điền nội dung vào 8 sections
- Trả về user

---

## 6. Cách kiểm tra skill hoạt động đúng

### 6.1 Kiểm tra metadata

```bash
# Xem skill có được detect không
kimi
/help
# Tìm "User" section, xem có "camk-system-design" không
```

### 6.2 Kiểm tra trigger

```bash
kimi
# Nói 1 câu trigger
design a URL shortener for me
# Quan sát AI có đọc SKILL.md không (sẽ hiện "ReadFile" tool call)
```

### 6.3 Kiểm tra script

```bash
# Chạy thử script
python3 ~/.kimi/skills/camk-system-design/scripts/capacity_calc.py --dau 1000000 --requests-per-user 10
```

### 6.4 Kiểm tra parse

```bash
# Kiểm tra Mermaid/D2 (nếu skill có flow)
# Skill này là standard, không cần check
```

---

## 7. Common issues và cách fix

| Issue | Nguyên nhân | Fix |
|-------|-------------|-----|
| Skill không trigger | Description quá ngắn/generic | Thêm trigger phrases cụ thể |
| AI không đọc references | Thiếu "When to Read" trong SKILL.md | Thêm bảng hướng dẫn |
| AI không chạy scripts | Không ghi rõ command trong SKILL.md | Thêm ví dụ command |
| Output không consistent | Không có template | Thêm assets/design-doc-template.md |
| Body quá dài | Nhiều nội dung trong SKILL.md | Chuyển sang references |

---

## 8. Cách modify skill

### Thêm reference mới
1. Tạo file trong `references/`
2. Thêm vào bảng "When to Use References" trong SKILL.md
3. Test bằng cách yêu cầu AI đọc reference đó

### Thêm script mới
1. Tạo file trong `scripts/`
2. Test chạy thủ công trước
3. Thêm vào bảng "When to Use Scripts" trong SKILL.md
4. Ghi rõ cách chạy và tham số

### Thêm asset mới
1. Tạo file trong `assets/`
2. Thêm vào bảng "When to Use Assets" trong SKILL.md

### Sửa description
1. Edit frontmatter trong SKILL.md
2. Restart kimi-cli để reload metadata

---

## 9. Best practices đã áp dụng trong skill này

✅ **Description chi tiết** với nhiều trigger phrases
✅ **Body < 500 lines** (gọn nhẹ)
✅ **Quick Start section** để AI biết bắt đầu từ đâu
✅ **Bảng "When to Use"** cho references, scripts, assets
✅ **Scripts tested** trước khi đưa vào
✅ **References lazy-loaded** (không tự động)
✅ **Template cho output** (consistent structure)
✅ **Standard skill** (linh hoạt, không rigid flow)

---

## 10. Cách cài đặt

```bash
# Copy vào user skills directory
cp -r camk-system-design ~/.kimi/skills/

# Hoặc nếu dùng install.sh, thêm vào loop:
# for skill_path in "${SCRIPT_DIR}/camk"/*/; do ...

# Restart kimi-cli để load
kimi
```

Kiểm tra:
```bash
/help
# Tìm section "User", xem có camk-system-design không
```

---

*Skill version: 1.0*
*Created: 2026-05-03*
