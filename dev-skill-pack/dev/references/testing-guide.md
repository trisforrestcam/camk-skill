# Testing Guide

Quick reference for writing effective tests across common scenarios.

## Test Structure

```python
# Arrange - Act - Assert pattern
def test_feature():
    # Arrange: setup data and mocks
    user = create_user(name="test")
    
    # Act: execute the code under test
    result = user.greet()
    
    # Assert: verify expectations
    assert result == "Hello, test"
```

## Coverage Targets

| Component | Minimum | Ideal |
|-----------|---------|-------|
| Business logic | 80% | 90%+ |
| API endpoints | 70% | 80%+ |
| Utility functions | 60% | 80%+ |
| UI components | 50% | 70%+ |

## Test Types

### Unit Tests
- Test one function/class in isolation
- Mock all dependencies
- Fast execution (< 10ms each)

### Integration Tests
- Test component interactions
- Use test database or containers
- Verify data flow end-to-end

### E2E Tests
- Test critical user journeys
- Use real browser/API
- Keep minimal (5-10 core flows)

## Common Patterns

### Testing Async Code
```python
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

### Testing with Time
```python
from freezegun import freeze_time

@freeze_time("2024-01-01")
def test_time_dependent():
    assert get_current_year() == 2024
```

## Anti-patterns to Avoid

- Testing implementation details instead of behavior
- Mocking what you don't own
- Tests that depend on test order
- Sleep-based waiting in async tests
