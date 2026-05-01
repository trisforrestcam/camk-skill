# Language Patterns

Common patterns for writing clean, maintainable code across JS/TS, Python, Go, and Vue.js.

## Defensive Programming

```typescript
// JS/TS: Guard clauses instead of nested if
function processUser(user: User | null): UserData | null {
  if (!user) return null;
  if (!user.isActive) return null;
  if (!user.profile) return null;
  return user.profile.getData();
}
```

```go
// Go: Early returns
func ProcessUser(user *User) (*UserData, error) {
    if user == nil {
        return nil, errors.New("user is nil")
    }
    if !user.IsActive {
        return nil, errors.New("user is inactive")
    }
    return user.Profile.GetData(), nil
}
```

## Error Handling

```typescript
// JS/TS: Prefer explicit error handling; avoid catch-all
async function fetchUser(id: number): Promise<User> {
  try {
    const res = await api.get(`/users/${id}`);
    return res.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response?.status === 404) {
      throw new UserNotFoundError(id);
    }
    throw new UserFetchError("Failed to fetch user", { cause: error });
  }
}
```

```python
# Python: Prefer explicit error handling
try:
    result = risky_operation()
except SpecificError as e:
    logger.error("Operation failed: %s", e)
    return default_value
```

```go
// Go: Errors are values; always check
result, err := doSomething()
if err != nil {
    return fmt.Errorf("doing something: %w", err)
}
```

## Null Safety

```typescript
// JS/TS: Optional chaining & nullish coalescing
const userName = user?.profile?.name ?? "Anonymous";

// Avoid scattered null checks
if (data := fetchData()) {
    process(data);
}
```

```vue
<!-- Vue: v-if guards before accessing nested props -->
<template>
  <div v-if="user">
    <h1>{{ user.profile?.name ?? 'Guest' }}</h1>
  </div>
</template>
```

## Resource Management

```typescript
// JS/TS: Always cleanup async resources
const controller = new AbortController();
try {
  const res = await fetch(url, { signal: controller.signal });
} finally {
  controller.abort();
}
```

```python
# Python: Always use context managers
with open("file.txt") as f:
    data = f.read()

# For locks, connections, sessions
with acquire_lock():
    process_critical_section()
```

```go
// Go: defer for cleanup
f, err := os.Open("file.txt")
if err != nil {
    return err
}
defer f.Close()
```

## Configuration

```typescript
// JS/TS: Environment-based config with validation (Zod)
import { z } from "zod";

const envSchema = z.object({
  NODE_ENV: z.enum(["development", "production", "test"]),
  PORT: z.string().default("3000").transform(Number),
  DATABASE_URL: z.string().url(),
});

export const env = envSchema.parse(process.env);
```

```python
# Python: Environment-based config with defaults
import os

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "30"))
```

```go
// Go: Config struct with env tags
type Config struct {
    Port        int    `env:"PORT" envDefault:"8080"`
    DatabaseURL string `env:"DATABASE_URL" validate:"required"`
    Debug       bool   `env:"DEBUG" envDefault:"false"`
}
```

## Async Patterns

```typescript
// JS/TS: Prefer Promise.all for parallel
const [users, orders] = await Promise.all([
  fetchUsers(),
  fetchOrders(),
]);

// Avoid Promise.allSettled unless you need partial results
```

```go
// Go: Use errgroup for concurrent tasks
import "golang.org/x/sync/errgroup"

g, ctx := errgroup.WithContext(ctx)
g.Go(func() error { return fetchUsers(ctx) })
g.Go(func() error { return fetchOrders(ctx) })
if err := g.Wait(); err != nil {
    return err
}
```

## Vue.js Composable Patterns

```typescript
// Fetch with loading & error state
import { ref, watchEffect } from "vue";

export function useFetch<T>(url: Ref<string>) {
  const data = ref<T | null>(null);
  const error = ref<Error | null>(null);
  const loading = ref(false);

  watchEffect(async () => {
    loading.value = true;
    error.value = null;
    try {
      const res = await fetch(url.value);
      data.value = await res.json();
    } catch (e) {
      error.value = e as Error;
    } finally {
      loading.value = false;
    }
  });

  return { data, error, loading };
}
```
