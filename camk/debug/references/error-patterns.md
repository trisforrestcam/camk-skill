# Error Patterns

Common error patterns and how to investigate them.

## Null/Undefined Errors

**Symptoms**: `AttributeError`, `TypeError: Cannot read property`, `NullPointerException`

**Investigation**:
1. Trace the variable back to its source
2. Check initialization order
3. Verify data flow from external sources
4. Add null checks or use Optional types

**Prevention**:
- Use static type checking
- Validate inputs at boundaries
- Initialize variables explicitly

## Race Conditions

**Symptoms**: Intermittent failures, data corruption, inconsistent state

**Investigation**:
1. Identify shared mutable state
2. Check async/await ordering
3. Review lock usage
4. Add logging to trace execution order

**Prevention**:
- Minimize shared state
- Use immutable data structures
- Proper locking primitives
- Consider actor model for concurrency

## Memory Leaks

**Symptoms**: Gradual memory growth, OOM errors, degraded performance

**Investigation**:
1. Profile memory usage over time
2. Check for growing collections
3. Verify event listener cleanup
4. Look for circular references

**Common Causes**:
- Uncleared timers/intervals
- Event listeners not removed
- Large caches without eviction
- Closure capturing large objects

## Performance Degradation

**Symptoms**: Slow responses, timeouts, high CPU/memory

**Investigation**:
1. Profile to find hotspots
2. Check for N+1 queries
3. Review algorithmic complexity
4. Monitor external dependencies

**Common Fixes**:
- Add database indexes
- Implement caching
- Batch operations
- Optimize hot paths
