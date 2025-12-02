# Zep - Long-Term Memory for AI Assistants

## Overview

Zep is a long-term memory service designed for AI assistants and chatbots. It provides persistent memory storage, enabling personalized AI experiences by remembering user conversations, preferences, and context across sessions.

## Technical Configuration

### Embedding Model
- **Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Dimensions**: 384
- **Type**: Local embedding (no external API required)
- **Provider**: Zep NLP Server (runs as a separate container)

### Database
- **Type**: PostgreSQL with pgvector extension
- **Database Name**: `zep`
- **Connection**: `nostack-postgres:5432`

### Architecture
Zep runs as two containers:
1. **zep-nlp**: Handles embedding generation using the local model
2. **zep**: Main Zep service that manages memory storage and retrieval

## How to Use Zep

### 1. Access the API
Zep exposes a REST API on port `8000` (configurable via `.env`):
```
http://localhost:8000
```

### 2. API Key
Set your API key in `.env`:
```bash
ZEP_API_KEY=your-api-key-here
```

### 3. Basic Usage

#### Create a Session
```bash
curl -X POST http://localhost:8000/api/v1/sessions \
  -H "Authorization: Bearer your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "user-123",
    "user_id": "user-123",
    "metadata": {"name": "John Doe"}
  }'
```

#### Add Memory
```bash
curl -X POST http://localhost:8000/api/v1/sessions/user-123/memory \
  -H "Authorization: Bearer your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "My favorite color is blue"},
      {"role": "assistant", "content": "I'll remember that!"}
    ]
  }'
```

#### Retrieve Memory
```bash
curl http://localhost:8000/api/v1/sessions/user-123/memory \
  -H "Authorization: Bearer your-api-key-here"
```

#### Search Memory
```bash
curl -X POST http://localhost:8000/api/v1/sessions/user-123/search \
  -H "Authorization: Bearer your-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "what is my favorite color?",
    "limit": 5
  }'
```

## Integration with Other Services

### n8n Integration
Use the HTTP Request node to interact with Zep:
1. Set Method to `POST`
2. URL: `http://nostack-zep:8000/api/v1/sessions/{session_id}/memory`
3. Add Header: `Authorization: Bearer ${ZEP_API_KEY}`

### Flowise Integration
Flowise has built-in Zep memory nodes:
1. Add "Zep Memory" node to your flow
2. Configure:
   - Base URL: `http://nostack-zep:8000`
   - API Key: Your Zep API key
   - Session ID: User identifier

### Langflow Integration
Use the HTTP Request component to call Zep API endpoints.

## Configuration Files

### `config/zep.yaml`
Main configuration file for Zep service. Key settings:
- `llm`: LLM configuration (optional, for summarization)
- `nlp`: NLP server endpoint
- `store`: Database configuration

### Environment Variables
```bash
ZEP_DB_HOST=nostack-postgres
ZEP_DB_PORT=5432
ZEP_DB_USER=postgres
ZEP_DB_PASS=your-password
ZEP_DB_NAME=zep
ZEP_API_KEY=your-api-key
ZEP_PORT=8000
```

## Data Storage

### Location
- **Database**: `postgres-data/` (PostgreSQL data)
- **Cache**: `data/zep/` (temporary cache files)

### Backup
To backup Zep data:
```bash
docker exec nostack-postgres pg_dump -U postgres zep > zep_backup.sql
```

### Restore
```bash
docker exec -i nostack-postgres psql -U postgres zep < zep_backup.sql
```

## Advanced Features

### Memory Summarization
Zep can automatically summarize long conversations to maintain context efficiently. Configure in `config/zep.yaml`.

### Fact Extraction
Zep extracts facts from conversations for structured memory retrieval.

### Vector Search
Uses pgvector for semantic search across conversation history.

## Troubleshooting

### Check Zep Logs
```bash
docker logs nostack-zep
docker logs nostack-zep-nlp
```

### Verify NLP Server
```bash
curl http://localhost:5555/healthz
```

### Test Database Connection
```bash
docker exec nostack-zep psql -h nostack-postgres -U postgres -d zep -c "SELECT 1;"
```

## Resources

- [Official Documentation](https://docs.getzep.com/)
- [API Reference](https://docs.getzep.com/sdk/)
- [GitHub Repository](https://github.com/getzep/zep)
