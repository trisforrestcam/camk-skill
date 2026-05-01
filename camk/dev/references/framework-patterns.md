# Framework Patterns

Common patterns for popular frameworks.

## Web API (FastAPI/Flask/Express)

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

### Route Pattern
```python
@router.post("/users", response_model=UserResponse)
async def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return user_service.create(db, data, current_user)
```

## React/Frontend

### Component Structure
```
src/
├── components/       # Reusable UI components
├── pages/           # Route-level components
├── hooks/           # Custom hooks
├── services/        # API calls
├── stores/          # State management
└── utils/           # Helpers
```

### Component Pattern
```tsx
// Container/Presentational split
// Or: Single component with hooks

export function UserProfile({ userId }: Props) {
  const { user, loading } = useUser(userId);
  
  if (loading) return <Skeleton />;
  if (!user) return <NotFound />;
  
  return (
    <Card>
      <Avatar src={user.avatar} />
      <Name>{user.name}</Name>
    </Card>
  );
}
```

## Database

### Repository Pattern
```python
class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_by_id(self, id: int) -> Optional[User]:
        return self.session.query(User).filter_by(id=id).first()
    
    def create(self, data: UserCreate) -> User:
        user = User(**data.dict())
        self.session.add(user)
        self.session.commit()
        return user
```

## Testing

### Test Structure
```python
# tests/conftest.py - shared fixtures
@pytest.fixture
def client():
    return TestClient(app)

# tests/test_users.py - feature tests
class TestUserCreation:
    def test_valid_user(self, client):
        response = client.post("/users", json={"name": "test"})
        assert response.status_code == 201
```
