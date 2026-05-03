---
name: camk-debug
description: Systematic debugging and root-cause analysis for software bugs. Use when investigating errors, crashes, unexpected behavior, test failures, or performance issues in any codebase — especially JS/TS, Python, Go, or Vue.js. Trigger on stack traces, error messages, "it doesn't work", flaky tests, or when the user asks to debug, investigate, or fix a bug.
---

# Debug & Analyze

Follow this methodology to systematically find and fix bugs.

## Quick Start

When this skill triggers:
1. Ask for the error message / stack trace / reproduction steps if not provided
2. Follow the Core Workflow below in order
3. Do not jump to Fix before confirming root cause through Verify

## Core Workflow

### 1. Reproduce
- Confirm the bug exists and document exact steps to reproduce
- Note environment (Node/Go/Python version, browser, OS)
- Capture error messages, stack traces, and logs

### 2. Isolate
- Narrow scope to the specific file, function, or component
- Identify the minimal code path triggering the issue
- Check recent changes (`git log`, `git diff`)
- Determine if environmental or code-related

### 3. Hypothesize
- List top 3-5 possible causes ranked by likelihood
- Consider edge cases, race conditions, async ordering
- Check for similar issues in codebase or issue tracker

### 4. Verify
- Test each hypothesis systematically
- Add logging or breakpoints
- Create a minimal reproduction case
- Confirm root cause before fixing

### 5. Fix
- Apply a minimal, targeted fix
- Ensure the fix addresses root cause, not just symptoms
- Check for similar issues elsewhere in the codebase
- Document the fix and root cause

### 6. Prevent
- Add a regression test
- Update documentation if needed
- Consider if process or tooling can prevent recurrence

## Debug Decision Checklist

Use this sequence when unsure where to start:

- [ ] Can you reproduce the error consistently?
  - No → Gather more info: logs, environment, exact steps
- [ ] Does it match a known error pattern?
  - No → Check `references/error-patterns.md`
- [ ] Any recent changes to the code?
  - Yes → Check `git diff`, consider rollback test
- [ ] Is it environmental (config, dependency, infra)?
  - Yes → Check versions, env vars, infrastructure state
- [ ] Is it a code logic bug?
  - Yes → Trace execution, add logging, find root cause
- [ ] After fix: verified and regression test added?

## Language-Specific Debug Tools

### JavaScript / TypeScript
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
| Race detector | `go run -race` | Detect race conditions |
| Profiler | `go tool pprof` | CPU/memory profiling |

### Vue.js
| Tool | Use Case |
|------|----------|
| Vue DevTools | Inspect component tree, props, state |
| Browser DevTools | Breakpoints, network, console |

### Python
| Tool | Command | Use Case |
|------|---------|----------|
| pdb | `import pdb; pdb.set_trace()` | Interactive debugger |
| pytest | `pytest -s --tb=short` | Test debugging |

## Common Patterns by Language

### JS/TS: Async/Await
- Missing `await` causing promise instead of value
- Unhandled promise rejections
- Race conditions in parallel `Promise.all`

### Go: Concurrency
- Goroutine leaks (missing exit condition)
- Channel deadlocks (send/receive mismatch)
- Data races on shared state
- Nil pointer dereference

### Vue.js: Reactivity
- Destructured reactive object losing reactivity
- Mutating props directly
- Missing `key` in `v-for` causing stale DOM

### Python: Type/None
- `NoneType` has no attribute `x`
- Mutable default arguments
- Import circular dependencies

## References

- **Error patterns**: See `references/error-patterns.md`
- **Logging best practices**: See `references/logging-guide.md`
