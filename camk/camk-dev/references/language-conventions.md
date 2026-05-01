# Language Conventions

Quick reference for common language conventions.

## JavaScript / TypeScript (Node.js)

### Naming
- `camelCase`: variables, functions, methods
- `PascalCase`: classes, interfaces, types, enums, React/Vue components
- `UPPER_SNAKE_CASE`: constants, env vars
- `_prefix`: private fields (convention, use `#` for true private)

### Modern Syntax
```typescript
// Prefer const/let over var
const items: string[] = [];
let count = 0;

// Prefer arrow functions for callbacks
const doubled = items.map(x => x * 2);

// Use destructuring
const { name, email } = user;
const [first, ...rest] = items;

// Use template literals
const message = `Hello, ${name}`;

// Prefer optional chaining & nullish coalescing
const userName = user?.profile?.name ?? "Anonymous";

// Prefer async/await over raw promises
async function fetchData() {
  const res = await fetch("/api/data");
  return res.json();
}
```

### Imports Order
```typescript
// 1. Node built-ins
import path from "path";

// 2. Third-party packages
import express from "express";
import { z } from "zod";

// 3. Internal aliases / absolute imports
import { UserService } from "@/services/user";

// 4. Relative imports
import { helper } from "./utils";
```

### TypeScript Best Practices
- Enable `strict` mode in `tsconfig.json`
- Prefer `interface` for object shapes, `type` for unions/aliases
- Use `unknown` instead of `any`; narrow before use
- Return explicit types on public APIs

---

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

---

## Go

### Naming
- `camelCase`: unexported (private)
- `PascalCase`: exported (public)
- Short names for local variables (`i`, `ok`, `ctx`)
- Acronyms stay uppercase: `HTTPClient`, `userID`

### Error Handling
```go
// Always check errors; wrap with context
result, err := doSomething()
if err != nil {
    return fmt.Errorf("doing something: %w", err)
}

// Sentinel errors for specific checks
if errors.Is(err, sql.ErrNoRows) { ... }

// Custom error types
var ErrNotFound = errors.New("not found")
```

### Project Layout (Standard)
```
cmd/           # Main applications
internal/      # Private code
pkg/           # Public libraries
api/           # API definitions
configs/       # Config files
scripts/       # Build scripts
```

---

## Vue.js (Frontend)

### Naming
- `PascalCase`: Single-File Components (SFC), composables exported as functions
- `camelCase`: composable functions (`useAuth`, `useFetch`)
- `kebab-case`: template tags, custom events, file names recommended

### Composition API (Preferred)
```vue
<script setup lang="ts">
import { ref, computed, watch } from "vue";
import { useRoute } from "vue-router";

// Reactive state
const count = ref(0);
const doubled = computed(() => count.value * 2);

// Composables
const route = useRoute();

// Methods
function increment() {
  count.value++;
}

// Lifecycle & watchers
watch(count, (newVal) => {
  console.log("count changed:", newVal);
});
</script>
```

### Script Setup Rules
- Use `<script setup>` for all new components
- Use `lang="ts"` for type safety
- Define props with `defineProps<Props>()`
- Define emits with `defineEmits<Emits>()`
- Expose only when needed with `defineExpose()`

### Vue-Specific Conventions
```vue
<!-- Props: define interface, use withDefaults if needed -->
<script setup lang="ts">
interface Props {
  title: string;
  limit?: number;
}

const props = withDefaults(defineProps<Props>(), {
  limit: 10,
});

const emit = defineEmits<{
  submit: [payload: { id: number }];
}>();
</script>
```
