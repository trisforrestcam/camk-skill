---
name: camk-system-design
description: System design and architecture workflow for designing scalable, reliable, and maintainable distributed systems. Use when the user asks to design a system, architect a solution, scale an application, evaluate technology choices, or prepare for system design interviews. Trigger on phrases like "design a system", "how would you build", "architecture for", "scale this to", "system design interview", "design URL shortener", "design chat app", "design rate limiter", or when discussing high-level architecture, capacity planning, database sharding, caching strategy, load balancing, microservices, or distributed systems.
---

# System Design Workflow

Guide the user through designing scalable distributed systems step by step.

## Quick Start

When this skill triggers:
1. Identify the system to design from the user's request
2. Follow the workflow below in order
3. Always start with requirements — never jump to the solution
4. Use references for specific patterns and formulas
5. Use scripts for calculations when numbers are involved
6. Produce a final design document using the template from assets

## Core Workflow

### 1. Gather Requirements

Separate into functional and non-functional:

**Functional:**
- What features must the system support?
- Who are the users? (human, services, IoT)
- What are the read/write ratios?

**Non-functional:**
- Expected QPS/RPS (queries/requests per second)
- Latency requirements (p50, p99)
- Availability target (99.9%, 99.99%)
- Data durability requirements
- Geographic distribution

If the user hasn't provided numbers, ask for them or use reasonable assumptions and state them clearly.

### 2. Capacity Estimation

Use `scripts/capacity_calc.py` to compute:
- Daily active users (DAU)
- Requests per second (peak and average)
- Storage requirements (per day, per year)
- Bandwidth (ingress/ egress)

If the user provides numbers, run the script. If not, make reasonable estimates and document assumptions.

**Reference:** See `references/capacity-estimation.md` for formulas and rules of thumb.

### 3. API Design

Define the core APIs:
- REST or GraphQL or gRPC?
- Endpoints with methods (GET/POST/PUT/DELETE)
- Request/response payloads
- Authentication/authorization approach

### 4. Data Model

Design at two levels:
- **Logical:** Entities, relationships, cardinalities
- **Physical:** Which database type (SQL/NoSQL/Graph/Time-series)

**Key decisions:**
- Read-heavy vs write-heavy?
- Need ACID or eventual consistency?
- Data size and growth rate?

**Reference:** See `references/database-patterns.md` for database selection and sharding strategies.

### 5. High-Level Design (HLD)

Draw the architecture with these layers:

```
Client → CDN → Load Balancer → API Gateway → Services → Cache → Database
```

For each component, explain:
- What it does
- Why it's needed
- What technology choices are reasonable

**Reference:** See `references/scaling-patterns.md` for caching, load balancing, and CDN strategies.

### 6. Deep Dive into Critical Components

Pick 2-3 components that are most challenging and dive deep:
- **Data partitioning:** Consistent hashing, range-based, hash-based
- **Caching:** Cache-aside, write-through, write-behind
- **Concurrency:** Optimistic/pessimistic locking, idempotency
- **Messaging:** Queue vs stream, delivery guarantees
- **Real-time:** WebSockets, SSE, polling

**Reference:** See `references/system-design-examples.md` for common patterns in specific systems.

### 7. Trade-offs and Alternatives

Always present trade-offs:
- SQL vs NoSQL
- Strong consistency vs eventual consistency
- Microservices vs monolith
- Synchronous vs asynchronous communication
- Self-hosted vs managed services

### 8. Final Design Document

Use `assets/design-doc-template.md` as the structure.
Produce a complete document with:
- Requirements
- Capacity estimates
- API spec
- Data model
- Architecture diagram (text-based)
- Deep dives
- Trade-offs
- Future scaling considerations

## When to Use References

| Reference | When to Read |
|-----------|--------------|
| `references/capacity-estimation.md` | When computing QPS, storage, bandwidth |
| `references/database-patterns.md` | When choosing or sharding databases |
| `references/scaling-patterns.md` | When designing caching, LB, CDN |
| `references/system-design-examples.md` | When stuck or need pattern inspiration |

## When to Use Scripts

| Script | When to Run |
|--------|-------------|
| `scripts/capacity_calc.py` | After gathering requirements with numbers |
| `scripts/estimate_resources.py` | After capacity calc to size infrastructure |

## When to Use Assets

| Asset | When to Use |
|-------|-------------|
| `assets/design-doc-template.md` | At the end, to structure the final output |

## Common System Design Topics

- URL Shortener
- Rate Limiter
- Web Crawler
- Chat/Messaging System
- News Feed (Twitter/Facebook)
- Video Streaming (YouTube)
- Ride Sharing (Uber)
- Payment System
- Distributed Cache
- Distributed ID Generator
- Search Engine
- File Storage (Dropbox)
- Monitoring/Alerting System
