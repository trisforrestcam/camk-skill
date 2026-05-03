# Database Patterns

Guide for selecting and scaling databases.

## SQL vs NoSQL Decision Matrix

| Factor | SQL (PostgreSQL, MySQL) | NoSQL (Mongo, Cassandra, DynamoDB) |
|--------|------------------------|-----------------------------------|
| Schema | Fixed, relational | Flexible, dynamic |
| Transactions | ACID, strong consistency | BASE, eventual consistency |
| Complex queries | Excellent | Limited |
| Horizontal scale | Harder (sharding needed) | Easier (built-in) |
| Read-heavy | Good with replicas | Excellent |
| Write-heavy | Single node bottleneck | Excellent (partitioned writes) |

## When to Use What

**Relational (SQL):**
- Financial data, inventory, user accounts
- Complex joins and reporting
- Strong consistency requirements

**Document (MongoDB):**
- Content management, catalogs
- Rapidly evolving schemas
- Read-heavy with simple queries

**Key-Value (Redis, DynamoDB):**
- Caching, sessions, counters
- Simple access patterns
- Extreme low latency needs

**Wide-Column (Cassandra, Bigtable):**
- Time-series data, logs, metrics
- Massive write throughput
- Linear scalability

**Graph (Neo4j):**
- Social networks, recommendation engines
- Complex relationship traversals

## Sharding Strategies

**Hash-based:**
- shard = hash(key) % N
- Even distribution, hard to add/remove shards

**Range-based:**
- shard by key range (A-M, N-Z)
- Easy range queries, hot spots possible

**Directory-based:**
- Lookup table maps key to shard
- Flexible, requires additional lookup service

## Replication Patterns

**Master-Slave (Primary-Replica):**
- Writes to master, reads from replicas
- Good for read-heavy workloads
- Risk: replication lag

**Multi-Master:**
- Writes to any node
- Good for multi-region
- Risk: conflict resolution needed

**Quorum (Cassandra-style):**
- W + R > N for strong consistency
- Tunable consistency per query
