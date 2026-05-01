# Common Anti-patterns

Patterns to watch for and avoid during code review.

## Code Smells

### God Object
```python
# Bad: Class doing everything
class UserManager:
    def create_user(self): ...
    def send_email(self): ...
    def generate_report(self): ...
    def backup_database(self): ...

# Better: Separate concerns
class UserService: ...
class EmailService: ...
class ReportService: ...
```

### Primitive Obsession
```python
# Bad: Using strings for everything
def create_user(email: str, phone: str): ...

# Better: Use value objects
@dataclass
class Email:
    value: str
    def __post_init__(self):
        validate_email(self.value)
```

### Feature Envy
```python
# Bad: Method using mostly another class's data
class Order:
    def calculate_discount(self, customer):
        if customer.loyalty_years > 5:
            return 0.2
        return 0.0

# Better: Move to the class that owns the data
class Customer:
    def get_discount_rate(self):
        return 0.2 if self.loyalty_years > 5 else 0.0
```

## Security Anti-patterns

- Hardcoded secrets in code
- SQL string concatenation
- Trusting client-side validation
- Storing passwords in plain text
- Missing authentication checks

## Performance Anti-patterns

- N+1 database queries
- Loading entire datasets into memory
- Synchronous calls in async contexts
- No caching for expensive operations
- Blocking the main thread

## Testing Anti-patterns

- Tests that depend on external services
- Mocking internal implementation
- Tests with random data (flaky)
- Tests that don't clean up
- Testing getters and setters
