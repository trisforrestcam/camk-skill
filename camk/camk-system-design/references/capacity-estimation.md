# Capacity Estimation

Rules of thumb and formulas for back-of-the-envelope calculations.

## Time Conversions

| Unit | Value |
|------|-------|
| 1 day | 86,400 seconds |
| 1 month | ~30 days = 2.6M seconds |
| 1 year | ~365 days = 31.5M seconds |

## Request Estimation

**Daily to RPS:**
```
RPS = Total requests per day / 86,400
Peak RPS = Average RPS * 2 to 5 (use 3 as default)
```

**Examples:**
- 1M requests/day → ~12 RPS average, ~36 RPS peak
- 1B requests/day → ~11,574 RPS average, ~35,000 RPS peak

## Storage Estimation

**Text data:**
- Tweet: ~300 bytes
- URL record: ~500 bytes
- User profile: ~1-10 KB

**Media data:**
- Image (compressed): ~100-500 KB
- 1 minute video (1080p): ~50-100 MB
- 1 minute audio: ~1-5 MB

**Annual storage:**
```
Storage per year = Daily data * 365 * replication_factor
```

## Bandwidth Estimation

```
Ingress = Write volume per second
Egress = Read volume per second
```

**Example:** 100 images/second @ 200KB = 20 MB/s ingress

## Memory Estimation

**Cache sizing:**
- Store hot data (20% of total often serves 80% of requests)
- Rule: Cache hit ratio target = 90%+

**Example:**
- 1M daily users, 100KB profile each = 100GB total
- Hot cache: 20GB for 200K active users

## Server Estimation

**Throughput per server:**
- Web server (Node/Go): ~1,000-10,000 RPS
- Database (PostgreSQL): ~1,000-5,000 QPS
- Cache (Redis): ~100,000+ QPS

```
Servers needed = Peak RPS / RPS per server
```
