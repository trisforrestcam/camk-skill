# Error Patterns

Common error patterns and how to investigate them across JS/TS, Python, Go, and Vue.js.

---

## JavaScript / TypeScript (Node.js)

### `TypeError: Cannot read property 'x' of undefined`
**Symptoms**: Crash when accessing nested property on null/undefined

**Investigation**:
1. Trace the variable back to its source (API response, DB query)
2. Check if the property is optional in the type definition
3. Add null checks or use optional chaining `?.`
4. Validate API responses with Zod/io-ts

**Prevention**:
```typescript
// Use optional chaining
const name = user?.profile?.name ?? "Anonymous";

// Validate external data
const UserSchema = z.object({ profile: z.object({ name: z.string() }).optional() });
const user = UserSchema.parse(apiResponse);
```

### `UnhandledPromiseRejection`
**Symptoms**: Process crash or silent failure on async errors

**Investigation**:
1. Check for missing `await` or `.catch()`
2. Look for `try/catch` around async calls
3. Check event handlers that don't await

**Prevention**:
```typescript
// Always await or handle promises
app.get("/users", async (req, res, next) => {
  try {
    const users = await userService.list();
    res.json(users);
  } catch (err) {
    next(err); // Pass to error handler
  }
});

// Or use express-async-errors wrapper
```

### `ECONNREFUSED` / `ETIMEDOUT`
**Symptoms**: External API or DB connection fails

**Investigation**:
1. Check service is running and reachable
2. Verify connection string / URL
3. Check firewall / network policies
4. Review connection pool settings

---

## Go

### `panic: runtime error: invalid memory address or nil pointer dereference`
**Symptoms**: Application crashes with stack trace

**Investigation**:
1. Check if pointer was initialized before use
2. Verify struct fields are populated
3. Look for missing error checks that return nil

**Prevention**:
```go
// Always check errors before using result
user, err := repo.FindByID(ctx, id)
if err != nil {
    return err
}
// user is safe to use here
```

### Goroutine Leaks
**Symptoms**: Memory grows over time, goroutine count increases

**Investigation**:
1. Check `runtime.NumGoroutine()` over time
2. Look for channels without receivers
3. Check for `select` with no exit condition

**Prevention**:
```go
// Use contexts with timeout
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

// Ensure goroutines can exit
func worker(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            return
        case job := <-jobs:
            process(job)
        }
    }
}
```

### `sql: no rows in result set`
**Symptoms**: Query returns no rows when data expected

**Investigation**:
1. Verify query parameters
2. Check if row actually exists
3. Use `errors.Is(err, sql.ErrNoRows)` to handle gracefully

---

## Vue.js

### `[Vue warn]: Invalid prop: type check failed`
**Symptoms**: Console warning, component may not render correctly

**Investigation**:
1. Check `defineProps` type definition
2. Verify parent is passing correct type
3. Check for null/undefined being passed as required prop

**Prevention**:
```vue
<script setup lang="ts">
interface Props {
  user: User;           // required
  limit?: number;       // optional
}

const props = withDefaults(defineProps<Props>(), {
  limit: 10,
});
</script>
```

### `Cannot read property of null` in Template
**Symptoms**: White screen or broken UI

**Investigation**:
1. Add `v-if` guards for async data
2. Check initial state in setup
3. Use `?.` optional chaining in computed

**Prevention**:
```vue
<template>
  <div v-if="user">
    <h1>{{ user.name }}</h1>
    <p>{{ user.profile?.bio }}</p>
  </div>
  <Skeleton v-else />
</template>
```

### Reactivity Not Updating
**Symptoms**: UI doesn't reflect state changes

**Investigation**:
1. Check if reactive object was destructured (loses reactivity)
2. Verify array mutations use reactive methods
3. Check if primitive was passed instead of ref

**Prevention**:
```typescript
// Good: Use ref/reactive
const count = ref(0);
count.value++; // reactive

// Bad: Destructuring reactive object loses reactivity
const { name } = reactive({ name: "Alice" }); // NOT reactive

// Good: Use toRefs
const { name } = toRefs(reactive({ name: "Alice" })); // reactive
```

---

## Universal Patterns

### Null/Undefined Errors
**Symptoms**: `AttributeError`, `TypeError: Cannot read property`, `NullPointerException`

**Investigation**:
1. Trace the variable back to its source
2. Check initialization order
3. Verify data flow from external sources
4. Add null checks or use Optional types

**Prevention**:
- Use static type checking (TypeScript, mypy)
- Validate inputs at boundaries
- Initialize variables explicitly

### Race Conditions
**Symptoms**: Intermittent failures, data corruption, inconsistent state

**Investigation**:
1. Identify shared mutable state
2. Check async/await ordering
3. Review lock/sem usage (Go: `sync.Mutex`, JS: single-threaded but check event loop)
4. Add logging to trace execution order

**Prevention**:
- Minimize shared state
- Use immutable data structures
- Proper locking primitives
- Consider atomic operations for counters

### Memory Leaks
**Symptoms**: Gradual memory growth, OOM errors, degraded performance

**Investigation**:
1. Profile memory usage over time
2. Check for growing collections
3. Verify event listener cleanup (Vue: `onUnmounted`)
4. Look for circular references

**Common Causes**:
- Uncleared timers/intervals (`setInterval` without `clearInterval`)
- Event listeners not removed
- Large caches without eviction
- Closure capturing large objects
- Vue: not cleaning up watchers or event bus subscriptions

```typescript
// Vue: cleanup on unmount
import { onUnmounted } from "vue";

const interval = setInterval(poll, 5000);
onUnmounted(() => clearInterval(interval));
```

### Performance Degradation
**Symptoms**: Slow responses, timeouts, high CPU/memory

**Investigation**:
1. Profile to find hotspots
2. Check for N+1 queries
3. Review algorithmic complexity
4. Monitor external dependencies

**Common Fixes**:
- Add database indexes
- Implement caching (Redis)
- Batch operations
- Optimize hot paths
- Vue: Use `v-once`, `computed` caching, virtual scrolling for large lists
