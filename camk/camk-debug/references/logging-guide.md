# Logging Guide

Best practices for effective logging during debugging.

## Log Levels

| Level | When to Use | Example |
|-------|-------------|---------|
| DEBUG | Detailed diagnostic info | `Processing item 42 with params {...}` |
| INFO | Normal operations | `User login successful: user_id=123` |
| WARNING | Unexpected but handled | `Retrying failed request (attempt 2/3)` |
| ERROR | Failed operation | `Database connection failed: timeout` |
| CRITICAL | System failure | `Cannot start server: port in use` |

## Structured Logging

```python
# Good: Structured, searchable
logger.info("user_action", 
    action="purchase",
    user_id=user.id,
    amount=order.total,
    item_count=len(order.items)
)

# Bad: Unstructured, hard to query
logger.info(f"User {user.id} purchased {len(order.items)} items for {order.total}")
```

## Context Propagation

```python
# Include request/trace ID
import contextvars

request_id = contextvars.ContextVar("request_id")

logger.info("processing_request", 
    request_id=request_id.get(),
    endpoint="/api/orders"
)
```

## What to Log

### Always Log
- Request/response summaries (not bodies with PII)
- Authentication events
- State changes
- Errors with stack traces

### Never Log
- Passwords, tokens, secrets
- PII (emails, phone numbers)
- Full credit card numbers
- Encryption keys

## Debugging with Logs

```python
# Add temporary debug logs
def debug_function(data):
    logger.debug("debug_input", data=data, type=type(data).__name__)
    result = process(data)
    logger.debug("debug_output", result=result)
    return result

# Remove before merging
```
