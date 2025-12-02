# 📚 NoStack Documentation

This directory contains comprehensive technical documentation for all services in the NoStack AI development stack.

## Service Documentation

### Workflow & Automation
- **[n8n](n8n.md)** - Workflow automation platform with 400+ integrations
- **[Flowise](flowise.md)** - No/low-code AI agent builder
- **[Langflow](langflow.md)** - Visual framework for multi-agent AI applications

### Memory & Storage
- **[Zep](zep.md)** - Long-term memory for AI assistants
  - Embedding Model: `all-MiniLM-L6-v2` (384 dimensions)
  - Local embeddings (no external API)
- **[Qdrant](qdrant.md)** - High-performance vector database
  - Supports multiple embedding dimensions
  - REST API and gRPC
- **[Neo4j](neo4j.md)** - Graph database for knowledge graphs
  - Cypher query language
  - Ideal for complex relationships

### Databases
- **[PostgreSQL](postgresql.md)** - Relational database with pgvector
  - Supports vector similarity search
  - Used by: n8n, Flowise, Langflow, Zep, OpenWebUI
- **[Redis](redis.md)** - In-memory data store
  - Caching and session management
  - Message brokering

## Architecture Documentation
- **[Stack Infrastructure](Stack-Infrastructure.md)** - Complete architecture overview
- **[OpenWebUI Development](openwebui-development.md)** - Development setup guide
- **[Service Access](service-access.md)** - URLs and connection details

## Quick Reference

### Embedding Dimensions
| Model | Dimensions | Used By |
|-------|-----------|---------|
| all-MiniLM-L6-v2 | 384 | Zep (default) |
| all-mpnet-base-v2 | 768 | - |
| text-embedding-ada-002 | 1536 | OpenAI |
| text-embedding-3-large | 3072 | OpenAI |

### Service URLs
| Service | URL | Purpose |
|---------|-----|---------|
| n8n | http://localhost:5679 | Workflow automation |
| Flowise | http://localhost:3002 | AI agent builder |
| Langflow | http://localhost:7860 | Visual AI framework |
| Qdrant | http://localhost:6333 | Vector database API |
| Qdrant Dashboard | http://localhost:6334/dashboard | Vector DB GUI |
| Neo4j Browser | http://localhost:7474 | Graph database UI |
| Redis Commander | http://localhost:8081 | Redis GUI |
| PostgreSQL | localhost:5432 | Database |
| Redis | localhost:6379 | Cache/Queue |
| Zep | http://localhost:8000 | Memory API |

### Database Credentials
All databases use the credentials defined in `.env`:
- **User**: `postgres`
- **Password**: Set in `POSTGRES_PASSWORD`
- **Redis Password**: Set in `REDIS_PASSWORD`
- **Neo4j**: `neo4j` / Set in `NEO4J_AUTH`

## Integration Patterns

### Pattern 1: RAG (Retrieval Augmented Generation)
```
Document → Embeddings → Qdrant → Retrieval → LLM → Response
```

### Pattern 2: Multi-Agent with Memory
```
User Input → n8n → Langflow (Agent) → Zep (Memory) → Response
```

### Pattern 3: Knowledge Graph + Vector Search
```
Data → Neo4j (Relationships) + Qdrant (Vectors) → Hybrid Search
```

## Getting Started

1. **Setup**: Run `python3 setup.py` to initialize the stack
2. **Explore**: Visit each service's documentation for detailed usage
3. **Integrate**: Use the integration examples in each service doc
4. **Build**: Combine services to create powerful AI applications

## Contributing

To add or update documentation:
1. Create/edit the relevant `.md` file
2. Follow the existing structure
3. Include code examples and use cases
4. Update this index if adding new files
