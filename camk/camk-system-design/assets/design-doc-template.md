# System Design: [System Name]

## 1. Requirements

### Functional
- [Feature 1]
- [Feature 2]
- [Feature 3]

### Non-functional
- DAU: [number]
- Peak RPS: [number]
- Latency (p99): [ms]
- Availability: [99.9% / 99.99%]

## 2. Capacity Estimation

| Metric | Value |
|--------|-------|
| Daily Active Users | |
| Average RPS | |
| Peak RPS | |
| Daily Storage | |
| Yearly Storage | |
| Ingress Bandwidth | |
| Egress Bandwidth | |

## 3. API Design

### [Endpoint 1]
```
POST /api/v1/...
Request: { ... }
Response: { ... }
```

### [Endpoint 2]
```
GET /api/v1/...
Response: { ... }
```

## 4. Data Model

### Entity Relationship
```
[User] 1---* [Post]
[Post] *---* [Tag]
```

### Database Choice
- Primary DB: [PostgreSQL / MongoDB / Cassandra]
- Cache: [Redis]
- Search: [Elasticsearch]

### Schema
```sql
-- Example table
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    created_at TIMESTAMP
);
```

## 5. High-Level Design

```
[Client] → [CDN] → [Load Balancer] → [API Gateway]
                                         ↓
                        [Service A] ←→ [Service B]
                             ↓              ↓
                        [Cache] ←→ [Queue] ←→ [Database]
```

### Component Descriptions
- **CDN**: Caches static content
- **Load Balancer**: Distributes traffic across web servers
- **API Gateway**: Routes requests, handles auth
- **Service A**: [description]
- **Cache**: Redis cluster for hot data
- **Queue**: Kafka for async processing
- **Database**: [description]

## 6. Deep Dive

### [Component 1]: [Name]
[Detailed explanation of the most critical component]

### [Component 2]: [Name]
[Detailed explanation]

## 7. Trade-offs

| Decision | Option A | Option B | Chosen | Reason |
|----------|----------|----------|--------|--------|
| Database | SQL | NoSQL | | |
| Consistency | Strong | Eventual | | |
| Architecture | Microservices | Monolith | | |

## 8. Future Considerations

- [Scaling to 10x traffic]
- [Multi-region deployment]
- [Disaster recovery plan]
