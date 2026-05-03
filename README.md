# CAMK Skill Pack

Bộ skill hỗ trợ phát triển phần mềm — từ brainstorm ý tưởng, design system, viết code, debug, đến viết docs.

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
| **camk-brainstorm** | Skill | Brainstorm, evaluate options, draft spec | `/skill:camk-brainstorm` |
| **camk-system-design** | Flow | Design distributed systems, architecture | `/skill:camk-system-design` |
| **camk-dev** | Flow | Code, review, conventions | `/skill:camk-dev` |
| **camk-debug** | Standard | Debug lỗi, investigate | Tự động trigger |
| **camk-docs** | Flow | Viết README, API docs, changelog | `/skill:camk-docs` |

### Skill chi tiết

#### camk-brainstorm — Spec & Brainstorm Agent

Chat với agent để explore ideas, evaluate options, và ra spec rõ ràng.

```
/skill:camk-brainstorm
"Tôi muốn thêm real-time notification vào app"
```

Agent sẽ hỏi đào sâu → explore approaches → recommend → output spec theo format:
```
Mục tiêu / Context / Spec Requirement / Non-goals / Edge cases
```

Xem thêm: `camk/camk-brainstorm/QUICK-TRIGGER.md`

#### camk-system-design — System Design Workflow

Guide từng bước để design distributed systems: requirements → capacity → API → data model → HLD → deep dive → trade-offs.

```
/skill:camk-system-design
"Design a URL shortener"
```

Có scripts tính capacity, template design doc, và QUICK-TRIGGER để kiểm soát tay.

Xem thêm: `camk/camk-system-design/QUICK-TRIGGER.md`

#### camk-dev — Development Workflow

Orchestrator cho coding, code review, và project exploration.

```
/skill:camk-dev
"Implement feature X"
"Review this PR"
"Explain this codebase"
```

#### camk-debug — Debug & Analyze

Tự động trigger khi gặp stack trace, error message, hoặc "it doesn't work".

```
"Fix bug này giúp tôi"
"Test này flaky quá"
```

#### camk-docs — Documentation Workflow

Viết và maintain technical documentation.

```
/skill:camk-docs
"Update README"
"Write API documentation"
```

## Scripts

| Script | Skill | Mô tả | Cách dùng |
|--------|-------|-------|-----------|
| `evaluate_options.py` | camk-brainstorm | Weighted scoring matrix | `python3 camk/camk-brainstorm/scripts/evaluate_options.py --interactive` |
| `premortem.py` | camk-brainstorm | Pre-mortem analysis | `python3 camk/camk-brainstorm/scripts/premortem.py --interactive` |
| `capacity_calc.py` | camk-system-design | Tính capacity (RPS, storage, bandwidth) | `python3 camk/camk-system-design/scripts/capacity_calc.py --dau 1000000` |
| `estimate_resources.py` | camk-system-design | Estimate infrastructure resources | `python3 camk/camk-system-design/scripts/estimate_resources.py` |
| `generate_tests.py` | camk-dev | Generate test cases | `echo '{"module_path":"src/app.py"}' \| python3 camk/camk-dev/scripts/generate_tests.py` |
| `check_complexity.py` | camk-dev | Check code complexity | `echo '{"path":"src/"}' \| python3 camk/camk-dev/scripts/check_complexity.py` |
| `trace_error.py` | camk-debug | Trace error patterns | `echo '{"traceback":"..."}' \| python3 camk/camk-debug/scripts/trace_error.py` |

## Structure

```
camk/
├── camk-brainstorm/      # Spec & brainstorm agent
│   ├── SKILL.md
│   ├── QUICK-TRIGGER.md
│   ├── README.md
│   ├── assets/
│   │   ├── brainstorm-template.md
│   │   └── decision-log-template.md
│   ├── references/
│   │   ├── cognitive-biases.md
│   │   ├── decision-frameworks.md
│   │   ├── ideation-techniques.md
│   │   └── scenario-testing.md
│   └── scripts/
│       ├── evaluate_options.py
│       └── premortem.py
├── camk-system-design/   # System design workflow
│   ├── SKILL.md
│   ├── QUICK-TRIGGER.md
│   ├── README.md
│   ├── assets/
│   │   └── design-doc-template.md
│   ├── references/
│   │   ├── capacity-estimation.md
│   │   ├── database-patterns.md
│   │   ├── scaling-patterns.md
│   │   └── system-design-examples.md
│   └── scripts/
│       ├── capacity_calc.py
│       └── estimate_resources.py
├── camk-dev/             # Development workflow
│   ├── SKILL.md
│   └── references/
│       ├── anti-patterns.md
│       ├── architecture-templates.md
│       ├── framework-patterns.md
│       ├── language-conventions.md
│       ├── language-patterns.md
│       ├── review-checklist.md
│       └── testing-guide.md
│   └── scripts/
│       ├── check_complexity.py
│       └── generate_tests.py
├── camk-debug/           # Debug workflow
│   ├── SKILL.md
│   └── references/
│       ├── error-patterns.md
│       └── logging-guide.md
│   └── scripts/
│       └── trace_error.py
└── camk-docs/            # Documentation workflow
    └── SKILL.md
```

## Troubleshooting

### Skill không trigger

```bash
ls ~/.kimi/skills/camk-brainstorm/SKILL.md
head -5 ~/.kimi/skills/camk-brainstorm/SKILL.md
```

### Kiểm tra skill đã load

```bash
kimi --skills-dir /path/to/camk --list-skills
```

## License

MIT
