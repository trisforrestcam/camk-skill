---
name: camk-debug
description: Debug workflow
---

# Debug & Analyze

Systematic debugging methodology. Use when investigating bugs, errors, or unexpected behavior in JS/TS, Python, Go, or Vue.js codebases.

## Core Workflow

1. **Reproduce**
   - Confirm the bug exists
   - Document exact steps to reproduce
   - Note environment (Node version, Go version, browser, OS)
   - Capture error messages, stack traces, and logs

2. **Isolate**
   - Narrow down the scope (which file, function, component)
   - Identify the minimal code path triggering the issue
   - Check recent changes (`git log`, `git diff`)
   - Determine if environmental or code-related

3. **Hypothesize**
   - List possible causes (top 3-5)
   - Rank by likelihood
   - Consider edge cases, race conditions, async ordering
   - Check for similar issues in codebase or issue tracker

4. **Verify**
   - Test each hypothesis systematically
   - Add logging or breakpoints
   - Create minimal reproduction case
   - Confirm root cause before fixing

5. **Fix**
   - Apply minimal, targeted fix
   - Ensure fix addresses root cause, not symptom
   - Check for similar issues elsewhere
   - Document the fix and root cause

6. **Prevent**
   - Add regression test
   - Update documentation if needed
   - Consider if process/tooling can prevent recurrence

## Language-Specific Debug Tools

### JavaScript / TypeScript (Node.js)
| Tool | Command | Use Case |
|------|---------|----------|
| Built-in debugger | `node --inspect` | Attach Chrome DevTools |
| `console` | `console.table()`, `console.time()` | Quick inspection |
| `debugger` | `debugger;` | Breakpoint in code |
| Vitest | `vitest --reporter=verbose` | Test debugging |

### Go
| Tool | Command | Use Case |
|------|---------|----------|
| Delve | `dlv debug` | Interactive debugger |
| Built-in trace | `go test -trace` | Trace goroutines |
| Race detector | `go run -race` | Detect race conditions |
| Profiler | `go tool pprof` | CPU/memory profiling |

### Vue.js
| Tool | Use Case |
|------|----------|
| Vue DevTools | Inspect component tree, props, state |
| Browser DevTools | Breakpoints, network, console |
| `console.log` | Reactive values (use `.value` for refs) |

### Python
| Tool | Command | Use Case |
|------|---------|----------|
| pdb | `import pdb; pdb.set_trace()` | Interactive debugger |
| ipdb | `import ipdb; ipdb.set_trace()` | Enhanced debugger |
| pytest | `pytest -s --tb=short` | Test debugging |

## Decision Tree

```
Error reported
    |
    v
Can reproduce? --No--> Gather more info (logs, env, steps)
    |Yes                        |
    v                           v
Known error pattern? <---------+
    |No
    v
Recent changes? --Yes--> Check git diff, rollback test
    |No                    |
    v                     v
Environmental? --Yes--> Check config, dependencies, infra
    |No                    |
    v                     v
Code logic bug? --Yes--> Trace execution, add logging
    |                     |
    v                     v
Apply fix <---------------+
    |
    v
Verify fix + add test
```

## Common Patterns by Language

### JS/TS: Async/Await Issues
- Missing `await` causing promise instead of value
- Unhandled promise rejections
- Race conditions in parallel `Promise.all`

### Go: Concurrency Issues
- Goroutine leaks (missing exit condition)
- Channel deadlocks (send/receive mismatch)
- Data races on shared state
- Nil pointer dereference

### Vue.js: Reactivity Issues
- Destructured reactive object losing reactivity
- Mutating props directly
- Missing `key` in `v-for` causing stale DOM
- Event handler not updating state

### Python: Type/None Issues
- `NoneType` has no attribute `x`
- Mutable default arguments
- Import circular dependencies
- GIL blocking in CPU-intensive tasks

## References

- **Error patterns**: See `references/error-patterns.md`
- **Logging best practices**: See `references/logging-guide.md`
