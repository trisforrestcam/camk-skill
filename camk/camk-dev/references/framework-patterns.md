# Framework Patterns

Common patterns for popular frameworks in the stack: Node.js/TS, Python, Go, Vue.js.

---

## Node.js / TypeScript Backend

### Project Structure
```
src/
├── config/           # Env & configuration
├── controllers/      # Route handlers
├── services/         # Business logic
├── repositories/     # Data access
├── models/           # DB schemas / ORM models
├── middlewares/      # Express/Fastify middlewares
├── routes/           # Route definitions
├── utils/            # Helpers
├── types/            # Shared TS types/interfaces
└── app.ts            # App entry
```

### Route Pattern (Express + Zod)
```typescript
// routes/user.routes.ts
import { Router } from "express";
import { z } from "zod";
import { validate } from "@/middlewares/validate";
import { UserController } from "@/controllers/user.controller";

const router = Router();

const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1),
});

router.post("/", validate(createUserSchema), UserController.create);

export default router;
```

### Service Pattern
```typescript
// services/user.service.ts
import { UserRepository } from "@/repositories/user.repository";
import { CreateUserDto } from "@/types/user";

export class UserService {
  constructor(private repo: UserRepository) {}

  async create(data: CreateUserDto) {
    const existing = await this.repo.findByEmail(data.email);
    if (existing) throw new Error("Email already exists");
    return this.repo.create(data);
  }
}
```

---

## Python (FastAPI / Flask)

### Project Structure
```
app/
├── api/
│   ├── routes/
│   ├── dependencies/
│   └── middleware/
├── services/
├── models/
├── repositories/
├── schemas/
└── utils/
```

### Route Pattern (FastAPI)
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import UserCreate, UserResponse
from app.services import user_service

router = APIRouter(prefix="/users")

@router.post("/", response_model=UserResponse)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    return user_service.create(db, data)
```

---

## Go

### Project Structure (Standard Layout)
```
cmd/
├── api/             # HTTP server main
└── worker/          # Background worker main

internal/
├── handler/         # HTTP handlers
├── service/         # Business logic
├── repository/      # Data access
├── model/           # Domain models
├── middleware/      # HTTP middlewares
└── config/          # Configuration

pkg/
└── utils/           # Shared utilities
```

### Handler Pattern
```go
package handler

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type UserHandler struct {
    svc UserService
}

func NewUserHandler(svc UserService) *UserHandler {
    return &UserHandler{svc: svc}
}

func (h *UserHandler) Create(c *gin.Context) {
    var req CreateUserRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }

    user, err := h.svc.Create(c.Request.Context(), req)
    if err != nil {
        c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
        return
    }

    c.JSON(http.StatusCreated, user)
}
```

### Service Pattern
```go
package service

import (
    "context"
    "fmt"
)

type UserService interface {
    Create(ctx context.Context, req CreateUserRequest) (*User, error)
}

type userService struct {
    repo UserRepository
}

func NewUserService(repo UserRepository) UserService {
    return &userService{repo: repo}
}

func (s *userService) Create(ctx context.Context, req CreateUserRequest) (*User, error) {
    // business logic
    return s.repo.Create(ctx, req)
}
```

---

## Vue.js 3 (Frontend)

### Project Structure
```
src/
├── components/       # Reusable UI components
│   ├── ui/           # Primitive UI (Button, Input, Modal)
│   └── features/     # Feature-specific components
├── views/            # Page-level components (or pages/)
├── composables/      # Reusable logic (useAuth, useFetch)
├── stores/           # Pinia stores
├── router/           # Vue Router config
├── services/         # API clients
├── types/            # Shared TS types
└── utils/            # Helpers
```

### Composable Pattern
```typescript
// composables/useAuth.ts
import { ref, computed } from "vue";
import { authApi } from "@/services/auth";

const user = ref<User | null>(null);
const isLoading = ref(false);

export function useAuth() {
  const isAuthenticated = computed(() => !!user.value);

  async function login(email: string, password: string) {
    isLoading.value = true;
    try {
      user.value = await authApi.login({ email, password });
    } finally {
      isLoading.value = false;
    }
  }

  function logout() {
    user.value = null;
    authApi.logout();
  }

  return { user, isAuthenticated, isLoading, login, logout };
}
```

### Pinia Store Pattern
```typescript
// stores/counter.ts
import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useCounterStore = defineStore("counter", () => {
  // State
  const count = ref(0);

  // Getters
  const doubled = computed(() => count.value * 2);

  // Actions
  function increment() {
    count.value++;
  }

  return { count, doubled, increment };
});
```

### Component Pattern
```vue
<!-- components/UserCard.vue -->
<script setup lang="ts">
interface Props {
  user: User;
  showActions?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  showActions: true,
});

const emit = defineEmits<{
  edit: [id: number];
  delete: [id: number];
}>();
</script>

<template>
  <div class="user-card">
    <img :src="user.avatar" :alt="user.name" />
    <h3>{{ user.name }}</h3>
    <div v-if="showActions" class="actions">
      <button @click="emit('edit', user.id)">Edit</button>
      <button @click="emit('delete', user.id)">Delete</button>
    </div>
  </div>
</template>
```

---

## Database

### Repository Pattern
```typescript
// repositories/user.repository.ts
import { PrismaClient, User } from "@prisma/client";

export class UserRepository {
  constructor(private db: PrismaClient) {}

  async findById(id: number): Promise<User | null> {
    return this.db.user.findUnique({ where: { id } });
  }

  async create(data: CreateUserInput): Promise<User> {
    return this.db.user.create({ data });
  }
}
```

---

## Testing

### Test Structure
```typescript
// tests/unit/services/user.service.test.ts
import { describe, it, expect, vi } from "vitest";
import { UserService } from "@/services/user.service";

describe("UserService", () => {
  it("should create a user", async () => {
    // Arrange
    const mockRepo = { findByEmail: vi.fn().mockResolvedValue(null), create: vi.fn() };
    const service = new UserService(mockRepo as any);

    // Act
    await service.create({ email: "test@example.com", name: "Test" });

    // Assert
    expect(mockRepo.create).toHaveBeenCalledWith({ email: "test@example.com", name: "Test" });
  });
});
```
