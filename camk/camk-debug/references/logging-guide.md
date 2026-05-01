# Logging Guide

Best practices for effective logging during debugging across JS/TS, Python, Go, and Vue.js.

## Log Levels

| Level | When to Use | Example |
|-------|-------------|---------|
| DEBUG | Detailed diagnostic info | `Processing item 42 with params {...}` |
| INFO | Normal operations | `User login successful: user_id=123` |
| WARNING | Unexpected but handled | `Retrying failed request (attempt 2/3)` |
| ERROR | Failed operation | `Database connection failed: timeout` |
| CRITICAL | System failure | `Cannot start server: port in use` |

---

## JavaScript / TypeScript (Node.js)

### Structured Logging with Pino
```typescript
import pino from "pino";

const logger = pino({
  level: process.env.LOG_LEVEL || "info",
  transport: process.env.NODE_ENV === "development" 
    ? { target: "pino-pretty" } 
    : undefined,
});

// Good: Structured, searchable
logger.info({ userId: 123, action: "purchase", amount: 99.99 }, "Order placed");

// Bad: Unstructured, hard to query
logger.info(`User 123 purchased items for $99.99`);
```

### Request Context (AsyncLocalStorage)
```typescript
import { AsyncLocalStorage } from "async_hooks";

const requestStore = new AsyncLocalStorage<Map<string, string>>();

// Middleware
app.use((req, res, next) => {
  const store = new Map<string, string>();
  store.set("requestId", req.headers["x-request-id"] || generateId());
  store.set("userId", req.user?.id);
  requestStore.run(store, next);
});

// Usage
function getLogger() {
  const store = requestStore.getStore();
  return logger.child({
    requestId: store?.get("requestId"),
    userId: store?.get("userId"),
  });
}
```

### Error Logging
```typescript
try {
  await processOrder(order);
} catch (error) {
  logger.error(
    { 
      err: error, 
      orderId: order.id,
      userId: order.userId 
    },
    "Failed to process order"
  );
}
```

---

## Python

### Structured Logging
```python
import structlog

logger = structlog.get_logger()

# Good: Structured, searchable
logger.info(
    "user_action",
    action="purchase",
    user_id=user.id,
    amount=order.total,
    item_count=len(order.items)
)

# Bad: Unstructured, hard to query
logger.info(f"User {user.id} purchased {len(order.items)} items for {order.total}")
```

### Context Propagation
```python
import contextvars

request_id = contextvars.ContextVar("request_id")

logger.info(
    "processing_request",
    request_id=request_id.get(),
    endpoint="/api/orders"
)
```

---

## Go

### Structured Logging with slog
```go
package main

import (
    "log/slog"
    "os"
)

func main() {
    logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{
        Level: slog.LevelInfo,
    }))

    // Structured logging
    logger.Info("order_placed",
        slog.Int("user_id", 123),
        slog.String("action", "purchase"),
        slog.Float64("amount", 99.99),
    )

    // With context
    ctx := context.Background()
    logger.InfoContext(ctx, "request_processed",
        slog.String("request_id", "req-123"),
        slog.Duration("duration", 150*time.Millisecond),
    )
}
```

### Error Logging
```go
if err != nil {
    logger.Error("failed_to_process_order",
        slog.String("order_id", order.ID),
        slog.String("error", err.Error()),
    )
}
```

---

## Vue.js (Frontend)

### Browser Logging
```typescript
// composables/useLogger.ts
const isDev = import.meta.env.DEV;

export function useLogger(scope: string) {
  return {
    debug: (...args: unknown[]) => {
      if (isDev) console.debug(`[${scope}]`, ...args);
    },
    info: (...args: unknown[]) => console.info(`[${scope}]`, ...args),
    warn: (...args: unknown[]) => console.warn(`[${scope}]`, ...args),
    error: (...args: unknown[]) => console.error(`[${scope}]`, ...args),
  };
}

// Usage
const log = useLogger("UserCard");
log.info("mounted", { userId: props.user.id });
```

### Error Boundary (Vue)
```vue
<script setup lang="ts">
import { onErrorCaptured } from "vue";

onErrorCaptured((err, instance, info) => {
  console.error("[ErrorBoundary]", err, { component: instance, info });
  // Send to error tracking service (Sentry, etc.)
  return false; // Prevent error from propagating
});
</script>
```

---

## What to Log

### Always Log
- Request/response summaries (not bodies with PII)
- Authentication events (login, logout, failed attempts)
- State changes (order status, user role changes)
- Errors with stack traces
- Background job start/complete/fail

### Never Log
- Passwords, tokens, secrets
- PII (emails, phone numbers, addresses)
- Full credit card numbers
- Encryption keys
- Session IDs in debug logs

## Debugging with Logs

```typescript
// Add temporary debug logs
def debugFunction(data: unknown) {
  logger.debug("debug_input", { data, type: typeof data });
  const result = process(data);
  logger.debug("debug_output", { result });
  return result;
}

// Remove before merging
```

```go
// Temporary debug in Go
slog.Debug("debug_trace",
    slog.String("function", "ProcessOrder"),
    slog.Any("input", order),
    slog.String("file", "order.go"),
    slog.Int("line", 42),
)
```
