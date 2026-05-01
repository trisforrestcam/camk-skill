# Testing Guide

Quick reference for writing effective tests across JS/TS, Python, Go, and Vue.js.

## Test Structure (Arrange - Act - Assert)

```typescript
// Universal pattern
describe("Feature", () => {
  it("should do something", () => {
    // Arrange: setup data and mocks
    const input = { name: "test" };

    // Act: execute the code under test
    const result = process(input);

    // Assert: verify expectations
    expect(result).toBe("expected");
  });
});
```

## Coverage Targets

| Component | Minimum | Ideal |
|-----------|---------|-------|
| Business logic | 80% | 90%+ |
| API endpoints | 70% | 80%+ |
| Utility functions | 60% | 80%+ |
| UI components | 50% | 70%+ |
| Composables | 70% | 80%+ |

## Test Types

### Unit Tests
- Test one function/class in isolation
- Mock all dependencies
- Fast execution (< 10ms each)

### Integration Tests
- Test component interactions (service + repo, API + DB)
- Use test database or containers
- Verify data flow end-to-end

### E2E Tests
- Test critical user journeys
- Use real browser (Playwright/Cypress) or API client
- Keep minimal (5-10 core flows)

---

## JavaScript / TypeScript (Node.js)

### Framework: Vitest (Recommended)
```typescript
// vitest.config.ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    globals: true,
    environment: "node",
    coverage: {
      provider: "v8",
      reporter: ["text", "json", "html"],
    },
  },
});
```

### Unit Test Example
```typescript
import { describe, it, expect, vi } from "vitest";
import { UserService } from "@/services/user.service";

describe("UserService", () => {
  it("should throw if email exists", async () => {
    const mockRepo = {
      findByEmail: vi.fn().mockResolvedValue({ id: 1 }),
    };
    const service = new UserService(mockRepo as any);

    await expect(
      service.create({ email: "dup@example.com", name: "Test" })
    ).rejects.toThrow("Email already exists");
  });
});
```

### API Integration Test (Supertest)
```typescript
import { describe, it, expect, beforeAll, afterAll } from "vitest";
import request from "supertest";
import { app } from "@/app";

describe("POST /users", () => {
  it("should create a user", async () => {
    const res = await request(app)
      .post("/users")
      .send({ email: "test@example.com", name: "Test" });

    expect(res.status).toBe(201);
    expect(res.body).toHaveProperty("id");
  });
});
```

---

## Python

### Framework: pytest
```python
# tests/conftest.py - shared fixtures
import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    return TestClient(app)

# tests/test_users.py
class TestUserCreation:
    def test_valid_user(self, client):
        response = client.post("/users", json={"name": "test"})
        assert response.status_code == 201
```

### Testing Async Code
```python
import pytest

@pytest.mark.asyncio
async def test_async_feature():
    result = await async_function()
    assert result is not None
```

### Testing Exceptions
```python
def test_raises_error():
    with pytest.raises(ValueError, match="invalid"):
        process_input(None)
```

---

## Go

### Framework: built-in `testing`
```go
package service

import (
    "testing"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/mock"
)

func TestUserService_Create(t *testing.T) {
    // Arrange
    mockRepo := new(MockUserRepository)
    mockRepo.On("FindByEmail", "test@example.com").Return(nil, nil)
    mockRepo.On("Create", mock.Anything).Return(&User{ID: 1}, nil)

    svc := NewUserService(mockRepo)

    // Act
    user, err := svc.Create(context.Background(), CreateUserRequest{
        Email: "test@example.com",
        Name:  "Test",
    })

    // Assert
    assert.NoError(t, err)
    assert.Equal(t, 1, user.ID)
    mockRepo.AssertExpectations(t)
}
```

### Table-Driven Tests (Idiomatic Go)
```go
func TestCalculateDiscount(t *testing.T) {
    tests := []struct {
        name     string
        years    int
        expected float64
    }{
        {"new customer", 0, 0.0},
        {"loyal customer", 5, 0.2},
        {"vip customer", 10, 0.3},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := CalculateDiscount(tt.years)
            assert.Equal(t, tt.expected, got)
        })
    }
}
```

---

## Vue.js

### Framework: Vitest + Vue Test Utils
```typescript
// vitest.config.ts
import { defineConfig } from "vitest/config";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  test: {
    environment: "jsdom",
    globals: true,
  },
});
```

### Component Test
```typescript
import { describe, it, expect } from "vitest";
import { mount } from "@vue/test-utils";
import UserCard from "@/components/UserCard.vue";

describe("UserCard", () => {
  it("renders user name", () => {
    const wrapper = mount(UserCard, {
      props: {
        user: { id: 1, name: "Alice", avatar: "https://..." },
      },
    });

    expect(wrapper.text()).toContain("Alice");
  });

  it("emits edit event on click", async () => {
    const wrapper = mount(UserCard, {
      props: { user: { id: 1, name: "Alice", avatar: "" } },
    });

    await wrapper.find("button:first-of-type").trigger("click");

    expect(wrapper.emitted("edit")).toBeTruthy();
    expect(wrapper.emitted("edit")[0]).toEqual([1]);
  });
});
```

### Composable Test
```typescript
import { describe, it, expect } from "vitest";
import { useCounter } from "@/composables/useCounter";

describe("useCounter", () => {
  it("increments count", () => {
    const { count, increment } = useCounter();
    expect(count.value).toBe(0);

    increment();
    expect(count.value).toBe(1);
  });
});
```

---

## Common Patterns

### Testing Async Code
```typescript
// JS/TS
await expect(asyncFn()).resolves.toBe("ok");
await expect(badAsyncFn()).rejects.toThrow("error");
```

### Testing with Time
```python
# Python
from freezegun import freeze_time

@freeze_time("2024-01-01")
def test_time_dependent():
    assert get_current_year() == 2024
```

```typescript
// JS/TS - use fake timers
vi.useFakeTimers();
vi.setSystemTime(new Date("2024-01-01"));
```

## Anti-patterns to Avoid

- Testing implementation details instead of behavior
- Mocking what you don't own
- Tests that depend on test order
- Sleep-based waiting in async tests
- Testing getters and setters
- Not cleaning up after tests (DB, timers, mocks)
