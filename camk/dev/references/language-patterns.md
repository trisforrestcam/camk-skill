# Language Patterns

Common patterns for writing clean, maintainable code.

## Defensive Programming

```python
# Guard clauses instead of nested if
def process_user(user):
    if not user:
        return None
    if not user.is_active:
        return None
    return user.get_data()
```

## Error Handling

```python
# Prefer explicit error handling
try:
    result = risky_operation()
except SpecificError as e:
    logger.error("Operation failed: %s", e)
    return default_value
```

## Null Safety

```python
# Use optional chaining / walrus operator
if data := fetch_data():
    process(data)

# Avoid None checks scattered everywhere
user_name = user.name if user else "Anonymous"
```

## Resource Management

```python
# Always use context managers
with open("file.txt") as f:
    data = f.read()

# For locks, connections, sessions
with acquire_lock():
    process_critical_section()
```

## Configuration

```python
# Environment-based config with defaults
import os

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "30"))
```
