# System Design Examples

Common patterns for specific system types.

## URL Shortener (TinyURL)

**Requirements:**
- Write: 1000 URLs/second
- Read: 10,000 redirects/second
- Short URL: 7 characters (base62)

**Key Design:**
- Hash long URL → short code (MD5 + base62)
- Collision handling: append counter
- Cache hot URLs in Redis
- Database: key-value (DynamoDB/Cassandra)

## Rate Limiter

**Algorithms:**
- Token Bucket: smooth rate, allows bursts
- Leaky Bucket: smooth output, strict rate
- Sliding Window Log: accurate, more memory
- Sliding Window Counter: approximate, less memory

**Distributed:**
- Redis with `INCR` + `EXPIRE`
- Consistent hashing for per-user limits

## Chat System (WhatsApp/Slack)

**Components:**
- WebSocket servers for real-time delivery
- Message queue for offline storage
- Read receipts via separate ACK channel
- Group chats: fan-out on write vs fan-out on read

**Trade-off:**
- Small groups: fan-out on write
- Large groups: fan-out on read

## News Feed (Twitter)

**Pull Model (Fan-out on read):**
- Read user's follow list, fetch recent tweets
- Simple, slow for users with many follows

**Push Model (Fan-out on write):**
- Pre-compute feed for each user
- Fast read, expensive write for celebrities

**Hybrid:**
- Normal users: push model
- Celebrities: pull model

## Video Streaming (YouTube)

**Upload flow:**
- Upload → transcoding service → multiple resolutions
- Store in object storage (S3)
- CDN for delivery

**Adaptive Bitrate:**
- Client switches quality based on bandwidth
- HLS or DASH protocols

## Ride Sharing (Uber)

**Key challenge:** Real-time driver location + matching

**Geo-spatial indexing:**
- Quadtree or Geohash
- Update driver location every few seconds
- Match nearest drivers using spatial index

**Dispatch service:**
- Assign driver to rider
- Handle supply-demand imbalance with surge pricing
