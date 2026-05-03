# Scaling Patterns

Strategies for scaling distributed systems.

## Caching

**Cache-Aside (Lazy Loading):**
- App checks cache first, loads from DB on miss
- Simple, but cache misses cause latency spikes

**Write-Through:**
- Write to cache and DB simultaneously
- Cache always fresh, slower writes

**Write-Behind (Write-Back):**
- Write to cache, async flush to DB
- Fast writes, risk of data loss

**Cache Eviction:**
- LRU (Least Recently Used) — default choice
- LFU (Least Frequently Used)
- TTL (Time To Live)

## Load Balancing

**Layer 4 (Transport):**
- Based on IP + port
- Fast, no SSL termination
- HAProxy, AWS NLB

**Layer 7 (Application):**
- Based on URL, headers, cookies
- Smart routing, SSL termination
- Nginx, AWS ALB

**Algorithms:**
- Round Robin — simple, even distribution
- Least Connections — good for long connections
- IP Hash — session affinity
- Consistent Hashing — cache-friendly

## CDN (Content Delivery Network)

**Use for:**
- Static assets (images, CSS, JS)
- Video streaming
- Downloadable content

**Cache headers:**
- `Cache-Control: max-age=3600`
- `ETag` for validation
- `Last-Modified`

## Message Queues vs Streams

**Queue (RabbitMQ, SQS):**
- Point-to-point delivery
- At-least-once or exactly-once
- Good for task distribution

**Stream (Kafka, Kinesis):**
- Pub/sub, multiple consumers
- Ordered, replayable
- Good for event sourcing, logs

## Microservices Patterns

**API Gateway:**
- Single entry point
- Auth, rate limiting, routing
- Aggregation of multiple services

**Service Discovery:**
- Consul, Eureka, Kubernetes DNS
- Health checks essential

**Circuit Breaker:**
- Fail fast when downstream is unhealthy
- Prevent cascade failures

**Bulkhead:**
- Isolate resources per service
- Prevent one service from starving others
