# Dev Skill Pack

Bộ skill hỗ trợ phát triển phần mềm gồm 5 skill: docs, dev, debug, brainstorm, git-push.

## Cài đặt

```bash
./install.sh
```

Script sẽ copy tất cả skill vào `~/.kimi/skills/`. Nếu skill đã tồn tại sẽ tự động replace.

### Cách khác: `--skills-dir` (test nhanh)

```bash
kimi --skills-dir /path/to/dev-skill-pack
```

### Cách khác: `extra_skill_dirs` trong config

```toml
# ~/.kimi/config.toml
extra_skill_dirs = ["/path/to/dev-skill-pack"]
```

## Các skill

| Skill | Type | Khi nào dùng | Lệnh gọi |
|-------|------|-------------|----------|
| **docs** | Flow | Viết README, API docs, changelog | `/flow:docs` |
| **dev** | Flow | Code, review, conventions | `/flow:dev` |
| **debug** | Standard | Debug lỗi, investigate | Tự động trigger |
| **brainstorm** | Flow | Brainstorm, quyết định | `/flow:brainstorm` |
| **git-push** | Flow | Push code lên branch | `/flow:git-push` |

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
You: "Fix bug này giúp tôi"        → debug tự trigger
You: "Code feature X"              → dev tự trigger
```

## Scripts

| Script | Skill | Cách dùng |
|--------|-------|-----------|
| `generate_tests.py` | dev | `echo '{"module_path":"src/app.py"}' \| python3 dev/scripts/generate_tests.py` |
| `check_complexity.py` | dev | `echo '{"path":"src/"}' \| python3 dev/scripts/check_complexity.py` |
| `trace_error.py` | debug | `echo '{"traceback":"..."}' \| python3 debug/scripts/trace_error.py` |

## Troubleshooting

### Skill không trigger

```bash
ls ~/.kimi/skills/dev/SKILL.md
head -5 ~/.kimi/skills/dev/SKILL.md
```

### Flow lỗi khi chạy

```
/flow:dev
```

Kimi sẽ báo lỗi parse nếu flowchart sai syntax.

## License

MIT
