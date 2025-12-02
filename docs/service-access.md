# Accessing Services - Web UI Guide

## Service Access URLs

### Services with Web Interfaces

| Service | URL | Credentials |
|---------|-----|-------------|
| **Flowise** | http://localhost:3002 | - |
| **n8n** | http://localhost:5679 or [Ngrok URL](https://stutteringly-unneat-delcie.ngrok-free.dev) | User: `admin`, Pass: `admin123` |
| **OpenWebUI** | http://localhost:3005 | Create account on first visit |
| **Neo4j Browser** | http://localhost:7475 | User: `neo4j`, Pass: `password123` |
| **Redis Commander** | http://localhost:8081 | - |
| **Qdrant Dashboard** | http://localhost:6334/dashboard | - |

### Services Without Web UI (CLI/API Only)

**PostgreSQL** (Port 5435)
```bash
# Connect via psql
docker exec -it ai-postgres psql -U postgres -d maindb

# Or use a GUI client like pgAdmin, DBeaver, etc.
# Host: localhost
# Port: 5435
# User: postgres
# Password: imad.123
```

**Zep** (Port 8002)
- API only, no web UI
- API endpoint: http://localhost:8002
- Check health: `curl http://localhost:8002/health`

**Zep NLP** (Port 5555)
- Internal service for embeddings
- No direct web access needed

## Redis Access Options

### 1. Redis Commander (Web UI) ✅ RECOMMENDED
- **URL**: http://localhost:8081
- **Features**: Browse keys, edit values, run commands
- **Already configured** in your stack

### 2. Redis CLI (Command Line)
```bash
# Access Redis CLI
docker exec -it ai-redis redis-cli -a redis.123

# Common commands:
KEYS *           # List all keys
GET key_name     # Get value
SET key value    # Set value
DEL key_name     # Delete key
INFO             # Server info
```

### 3. Desktop Clients
- **RedisInsight** (Free, official): https://redis.com/redis-enterprise/redis-insight/
- **Medis** (macOS): https://getmedis.com/
- **Another Redis Desktop Manager**: https://github.com/qishibo/AnotherRedisDesktopManager

Connection details for desktop clients:
- Host: `localhost`
- Port: `6380`
- Password: `redis.123`

## Troubleshooting

### Service Not Accessible
```bash
# Check if service is running
docker ps --filter "name=ai-"

# Check service logs
docker logs ai-<service-name>

# Restart service
docker compose restart <service-name>
```

### Port Already in Use
If you get "port already in use" errors, edit `.env` to change the port numbers.
