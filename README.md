# CAMK Skill Pack

Bộ skill hỗ trợ phát triển phần mềm gồm 5 skill: **camk:docs**, **camk:dev**, **camk:debug**, **camk:brainstorm**, **camk:git-push**.

## Cài đặt

```bash
./install.sh
```

Script sẽ copy tất cả skill vào `~/.kimi/skills/`. Nếu skill đã tồn tại sẽ tự động replace.

### Cách khác: `--skills-dir` (test nhanh)

```bash
kimi --skills-dir /path/to/camk
```

### Cách khác: `extra_skill_dirs` trong config

```toml
# ~/.kimi/config.toml
extra_skill_dirs = ["/path/to/camk"]
```

## Các skill

| Skill | Type | Khi nào dùng | Lệnh gọi |
|-------|------|-------------|----------|
| **camk:docs** | Flow | Viết README, API docs, changelog | `/flow:docs` |
| **camk:dev** | Flow | Code, review, conventions | `/flow:dev` |
| **camk:debug** | Standard | Debug lỗi, investigate | Tự động trigger |
| **camk:brainstorm** | Flow | Brainstorm, quyết định | `/flow:brainstorm` |
| **camk:git-push** | Flow | Push code lên branch | `/flow:git-push` |

## Sử dụng

### Flow skill — tương tác qua decision node

```
Kimi: {What do you need?}
      - Write code
      - Review code
      - Understand project

You: Write code
```

### Standard skill — tự động trigger

```
You: "Fix bug này giúp tôi"        → camk:debug tự trigger
You: "Code feature X"              → camk:dev tự trigger
```

## Scripts

| Script | Skill | Cách dùng |
|--------|-------|-----------|
| `generate_tests.py` | camk:dev | `echo '{"module_path":"src/app.py"}' \| python3 camk/dev/scripts/generate_tests.py` |
| `check_complexity.py` | camk:dev | `echo '{"path":"src/"}' \| python3 camk/dev/scripts/check_complexity.py` |
| `trace_error.py` | camk:debug | `echo '{"traceback":"..."}' \| python3 camk/debug/scripts/trace_error.py` |

## Troubleshooting

### Skill không trigger

```bash
ls ~/.kimi/skills/docs/SKILL.md
head -5 ~/.kimi/skills/docs/SKILL.md
```

### Flow lỗi khi chạy

```
/flow:docs
```

Kimi sẽ báo lỗi parse nếu flowchart sai syntax.

## License

MIT
