# Architecture Templates

Common architecture patterns and when to use them.

## Layered Architecture

```
Presentation Layer (API/Routes)
        |
    Business Layer (Services)
        |
   Data Access Layer (Repositories)
        |
    Database
```

**Best for**: CRUD applications, simple business logic
**Trade-off**: Simple but can become rigid

## Clean Architecture / Ports & Adapters

```
    Adapters (Web, CLI, Tests)
            |
    Application (Use Cases)
            |
    Domain (Entities, Business Rules)
            |
    Infrastructure (DB, External APIs)
```

**Best for**: Complex business logic, long-term maintainability
**Trade-off**: More boilerplate, steeper learning curve

## Microservices

```
    API Gateway
         |
    +----+----+----+----+
    |    |    |    |    |
   Svc1 Svc2 Svc3 Svc4 Svc5
```

**Best for**: Large teams, independent deployment, scale needs
**Trade-off**: Operational complexity, distributed systems challenges

## Event-Driven

```
   Service A  --event-->  Message Bus  --event-->  Service B
                                               -->  Service C
```

**Best for**: Async processing, loose coupling, real-time updates
**Trade-off**: Eventual consistency, harder to debug

## Decision Matrix

| Factor | Monolith | Microservices | Serverless |
|--------|----------|---------------|------------|
| Team size | Small | Large | Any |
| Deployment freq | Weekly+ | Daily+ | Event-triggered |
| Scale needs | Predictable | Variable | Spiky |
| Complexity | Low | High | Medium |
| Cost at idle | Higher | Medium | Lowest |

## When to Choose

- **Start simple**: Monolith with clean boundaries
- **Extract when**: Service has different scaling needs or team ownership
- **Consider events**: When async processing adds value
- **Avoid premature**: Don't split until you feel the pain
