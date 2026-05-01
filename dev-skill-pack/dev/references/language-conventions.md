# Language Conventions

Quick reference for common language conventions.

## Python

### Naming
- `snake_case`: functions, variables, modules
- `PascalCase`: classes, exceptions
- `UPPER_SNAKE_CASE`: constants
- `_prefix`: internal/private

### Imports
```python
# Order: stdlib, third-party, local
import os
from datetime import datetime

import requests
from pydantic import BaseModel

from myproject.models import User
from myproject.utils import helper
```

### Type Hints
```python
from typing import Optional, List

def process_users(users: List[User], limit: Optional[int] = None) -> dict:
    ...
```

## JavaScript/TypeScript

### Naming
- `camelCase`: variables, functions
- `PascalCase`: classes, components, types
- `UPPER_SNAKE_CASE`: constants
- `_prefix`: private (convention)

### Modern Syntax
```javascript
// Prefer const/let over var
const items = [];
let count = 0;

// Prefer arrow functions for callbacks
const doubled = items.map(x => x * 2);

// Use destructuring
const { name, email } = user;

// Use template literals
const message = `Hello, ${name}`;
```

## Go

### Naming
- `camelCase`: unexported
- `PascalCase`: exported
- Short names for local variables

### Error Handling
```go
// Always check errors
result, err := doSomething()
if err != nil {
    return fmt.Errorf("doing something: %w", err)
}
```

## Rust

### Naming
- `snake_case`: functions, variables, modules
- `PascalCase`: types, traits, enums
- `SCREAMING_SNAKE_CASE`: constants, statics

### Error Handling
```rust
// Use Result for recoverable errors
fn may_fail() -> Result<T, Error> { ... }

// Use ? operator
let value = may_fail()?;
```
