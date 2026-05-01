# Dev Skill Pack

Bộ skill hỗ trợ phát triển phần mềm gồm 4 skill: docs, dev, debug, brainstorm.

## Cài đặt

### Cách 1: `--skills-dir` (test nhanh)

```bash
kimi --skills-dir /path/to/dev-skill-pack
```

### Cách 2: `extra_skill_dirs` trong config (dùng lâu dài)

```bash
# Mở config
nano ~/.kimi/config.toml
```

Thêm dòng:
```toml
extra_skill_dirs = ["/path/to/dev-skill-pack"]
```

Sau đó chạy `kimi` bình thường.

### Cách 3: Copy vào `~/.kimi/skills/` (khuyến nghị)

```bash
# Copy từng skill
mkdir -p ~/.kimi/skills
cp -r /path/to/dev-skill-pack/docs ~/.kimi/skills/
cp -r /path/to/dev-skill-pack/dev ~/.kimi/skills/
cp -r /path/to/dev-skill-pack/debug ~/.kimi/skills/
cp -r /path/to/dev-skill-pack/brainstorm ~/.kimi/skills/
```

### Cách 4: Dùng `.skill` files

```bash
cd ~/.kimi/skills/
unzip /path/to/dev-skill-pack/docs.skill
unzip /path/to/dev-skill-pack/dev.skill
unzip /path/to/dev-skill-pack/debug.skill
unzip /path/to/dev-skill-pack/brainstorm.skill
```

## Các skill

| Skill | Type | Khi nào dùng | Lệnh gọi |
|-------|------|-------------|----------|
| **docs** | Flow | Viết README, API docs, changelog | `/flow:docs` |
| **dev** | Flow | Code, review, conventions | `/flow:dev` |
| **debug** | Standard | Debug lỗi, investigate | Tự động trigger |
| **brainstorm** | Flow | Brainstorm, quyết định | `/flow:brainstorm` |

## Sử dụng

### Flow skill — tương tác qua decision node

Flow skill sẽ hỏi bạn chọn nhánh ở các decision node:

```
Kimi: {What do you need?}
      - Write code
      - Review code
      - Understand project

You: <choice>Write code</choice>
```

Hoặc viết tự nhiên:
```
You: Write code
```

### Standard skill — tự động trigger

```
You: "Fix bug này giúp tôi"        → debug tự trigger
You: "Code feature X"              → dev tự trigger
```

## Cấu trúc flow

### dev
```
Choose → Coding / Reviewing / Conventions
```

### docs
```
Identify → README / API docs / Architecture / Changelog / User guide → Review → Publish
```

### brainstorm
```
Frame → {Clear?} → Diverge → Evaluate → {Winner?} → Compare / Hybrid / Recommend → Next steps
```

## Scripts

| Script | Skill | Cách dùng |
|--------|-------|-----------|
| `generate_tests.py` | dev | `echo '{"module_path":"src/app.py"}' \| python3 dev/scripts/generate_tests.py` |
| `check_complexity.py` | dev | `echo '{"path":"src/"}' \| python3 dev/scripts/check_complexity.py` |
| `trace_error.py` | debug | `echo '{"traceback":"..."}' \| python3 debug/scripts/trace_error.py` |

## Troubleshooting

### Skill không trigger

1. Kiểm tra skill đã copy đúng chỗ:
   ```bash
   ls ~/.kimi/skills/dev/SKILL.md
   ```

2. Kiểm tra description có match không:
   ```bash
   head -5 ~/.kimi/skills/dev/SKILL.md
   ```

3. Restart Kimi session

### Flow lỗi khi chạy

1. Kiểm tra flowchart syntax:
   - Phải có đúng 1 `BEGIN` và 1 `END`
   - Decision node phải có edge labels khác nhau
   - Tất cả node phải reachable từ BEGIN

2. Kiểm tra trong Kimi:
   ```
   /flow:dev
   ```

### Script không chạy

1. Kiểm tra Python path:
   ```bash
   which python3
   ```

2. Kiểm tra input JSON:
   ```bash
   echo '{"module_path":"src/app.py"}' | python3 dev/scripts/generate_tests.py
   ```

## Tùy chỉnh

### Thêm conventions cho project riêng

Tạo file `references/project-conventions.md` trong `dev/`:

```markdown
# Project Conventions — [Tên project]

## Tech Stack
- Backend: FastAPI + SQLAlchemy
- Frontend: React + TanStack Query

## Quy tắc đặc biệt
- API response luôn wrap trong `{data, error, meta}`
```

## License

MIT
