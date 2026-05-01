# Review Checklist

Quick checklist for thorough code reviews.

## Critical (Must Check)

- [ ] No security vulnerabilities (SQL injection, XSS, auth bypass)
- [ ] No data loss risks
- [ ] No breaking changes without migration path
- [ ] Input validation on all external inputs
- [ ] Proper error handling (no silent failures)

## Important (Should Check)

- [ ] Logic correctness and edge cases
- [ ] Thread safety and race conditions
- [ ] Performance: N+1 queries, unnecessary loops
- [ ] Memory leaks and resource cleanup
- [ ] Test coverage for new code

## Style (Nice to Have)

- [ ] Consistent naming conventions
- [ ] Clear variable and function names
- [ ] Appropriate comments (why, not what)
- [ ] No dead code or unused imports
- [ ] Follows project conventions

## Questions to Ask

1. Is this the simplest solution that works?
2. How will this behave under load?
3. What happens if this dependency fails?
4. Is this easy to understand in 6 months?
5. Can this be tested effectively?

## Red Flags

- Large PRs (>400 lines changed)
- No tests for new features
- Copy-paste code without abstraction
- Magic numbers without constants
- Comments explaining obvious code
