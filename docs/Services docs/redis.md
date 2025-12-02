# Redis - In-Memory Data Store

## Overview

Redis is a high-performance, in-memory data structure store used for caching, message brokering, and session management. It's essential for building fast, scalable AI applications.

## Technical Configuration

### Storage
- **Type**: In-memory with persistence
- **Data File**: `data/redis/dump.rdb`
- **Persistence**: RDB snapshots

### Ports
- **Redis**: `localhost:6379`
- **Redis Commander** (GUI): `http://localhost:8081`

### Authentication
- **Password**: Set in `.env` (`REDIS_PASSWORD`)

## How to Use Redis

### 1. Access Redis CLI
```bash
docker exec -it ai-redis redis-cli -a your-password
```

### 2. Access Redis Commander (GUI)
Open your browser:
```
http://localhost:8081
```

### 3. Basic Operations

#### Set and Get Values
```bash
SET key "value"
GET key
```

#### Set with Expiration
```bash
SETEX session:user123 3600 "user-data"  # Expires in 1 hour
```

#### Check if Key Exists
```bash
EXISTS key
```

#### Delete Key
```bash
DEL key
```

### 4. Data Structures

#### Lists
```bash
LPUSH mylist "item1"
LPUSH mylist "item2"
LRANGE mylist 0 -1  # Get all items
```

#### Sets
```bash
SADD myset "member1"
SADD myset "member2"
SMEMBERS myset  # Get all members
```

#### Hashes
```bash
HSET user:1 name "Alice"
HSET user:1 email "alice@example.com"
HGETALL user:1  # Get all fields
```

#### Sorted Sets
```bash
ZADD leaderboard 100 "player1"
ZADD leaderboard 200 "player2"
ZRANGE leaderboard 0 -1 WITHSCORES  # Get sorted list
```

## Use Cases for AI Applications

### 1. Session Management
Store user sessions:
```bash
SETEX session:abc123 3600 '{"user_id": "user123", "context": "..."}'
```

### 2. Caching LLM Responses
Cache expensive LLM calls:
```bash
SET cache:prompt:hash "LLM response" EX 86400  # Cache for 24 hours
```

### 3. Rate Limiting
Implement rate limits:
```bash
INCR rate:user123:minute
EXPIRE rate:user123:minute 60
```

### 4. Message Queue
Use Redis as a simple queue:
```bash
LPUSH queue:tasks '{"task": "process_document", "id": 123}'
RPOP queue:tasks  # Get next task
```

### 5. Real-time Analytics
Track events:
```bash
INCR analytics:page_views:2024-12-02
HINCRBY analytics:user:123 clicks 1
```

## Integration with Other Services

### Python Integration
```python
import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    password='your-password',
    decode_responses=True
)

# Set value
r.set('key', 'value')

# Get value
value = r.get('key')

# Set with expiration
r.setex('session', 3600, 'data')
```

### n8n Integration
Use the **Redis** node:
1. Add Redis node
2. Configure:
   - **Host**: `ai-redis`
   - **Port**: `6379`
   - **Password**: From `.env`

### Node.js Integration
```javascript
const redis = require('redis');

const client = redis.createClient({
    host: 'localhost',
    port: 6379,
    password: 'your-password'
});

await client.set('key', 'value');
const value = await client.get('key');
```

## Advanced Features

### Pub/Sub Messaging
```bash
# Subscribe to channel
SUBSCRIBE notifications

# Publish message (in another terminal)
PUBLISH notifications "New message"
```

### Transactions
```bash
MULTI
SET key1 "value1"
SET key2 "value2"
EXEC
```

### Lua Scripts
```bash
EVAL "return redis.call('SET', KEYS[1], ARGV[1])" 1 mykey myvalue
```

## Monitoring

### Server Info
```bash
INFO
```

### Memory Usage
```bash
INFO memory
```

### Connected Clients
```bash
CLIENT LIST
```

### Slow Queries
```bash
SLOWLOG GET 10
```

## Persistence

### RDB Snapshots
Automatic snapshots are configured. Manual save:
```bash
SAVE  # Synchronous
BGSAVE  # Background
```

### Check Last Save
```bash
LASTSAVE
```

## Backup and Restore

### Backup
```bash
# Copy the dump file
cp data/redis/dump.rdb data/redis/dump_backup_$(date +%Y%m%d).rdb
```

### Restore
```bash
# Stop Redis
docker stop ai-redis

# Replace dump file
cp backup.rdb data/redis/dump.rdb

# Start Redis
docker start ai-redis
```

## Performance Tips

1. **Use Pipelining**: Batch multiple commands
2. **Set Expiration**: Always set TTL for cache keys
3. **Use Appropriate Data Structures**: Choose the right type for your use case
4. **Monitor Memory**: Use `INFO memory` regularly
5. **Avoid Large Keys**: Split large data into smaller keys

## Troubleshooting

### Check Logs
```bash
docker logs ai-redis
```

### Restart Redis
```bash
docker restart ai-redis
```

### Clear All Data
```bash
docker exec -it ai-redis redis-cli -a your-password FLUSHALL
```

### Test Connection
```bash
docker exec -it ai-redis redis-cli -a your-password PING
# Should return: PONG
```

## Security Best Practices

1. **Strong Password**: Set a strong `REDIS_PASSWORD` in `.env`
2. **Disable Dangerous Commands**: Configure in `redis.conf`
3. **Network Isolation**: Redis is only accessible within Docker network
4. **Regular Backups**: Automate RDB backups

## Resources

- [Official Documentation](https://redis.io/documentation)
- [Commands Reference](https://redis.io/commands)
- [Redis University](https://university.redis.com/)
- [Best Practices](https://redis.io/topics/best-practices)
