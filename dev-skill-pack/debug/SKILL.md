---
name: debug
description: "Systematic debugging and error analysis. Use when: (1) User reports a bug or error, (2) Code behaves unexpectedly, (3) Need to investigate failures: reproduce → isolate → hypothesize → verify → fix. Provides structured approach and scripts for common debugging tasks."
---

# Debug & Analyze

Systematic debugging methodology. Use when investigating bugs, errors, or unexpected behavior.

## Core Workflow

1. **Reproduce**
   - Confirm the bug exists
   - Document exact steps to reproduce
   - Note environment (OS, version, config)
   - Capture error messages and logs

2. **Isolate**
   - Narrow down the scope
   - Identify the minimal code path triggering the issue
   - Check recent changes (git log, deployments)
   - Determine if environmental or code-related

3. **Hypothesize**
   - List possible causes (top 3-5)
   - Rank by likelihood
   - Consider edge cases and race conditions
   - Check for similar issues in codebase

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

## Common Patterns

### Null/Undefined Errors
- Check initialization order
- Verify data flow from source
- Add defensive checks

### Race Conditions
- Check async/await usage
- Verify lock/semaphore usage
- Look for shared mutable state

### Performance Issues
- Profile before optimizing
- Check N+1 queries
- Verify caching strategy

### Memory Leaks
- Check event listener cleanup
- Verify resource disposal
- Look for circular references

## References

- **Error patterns**: See `references/error-patterns.md`
- **Logging best practices**: See `references/logging-guide.md`
