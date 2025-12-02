# Qdrant - Vector Database

## Overview

Qdrant is a high-performance vector database designed for similarity search and AI applications. It's optimized for storing and querying high-dimensional vectors (embeddings) with metadata filtering.

## Technical Configuration

### Storage
- **Type**: File-based storage
- **Location**: `data/qdrant/`
- **Collections**: Stored in `data/qdrant/collections/`
- **Aliases**: `data/qdrant/aliases/`

### API Endpoints
- **REST API**: `http://localhost:6333`
- **gRPC**: `localhost:6334`
- **Dashboard**: `http://localhost:6334/dashboard`

### Configuration
- **Config File**: `config/qdrant.yml`
- **Default Settings**: Optimized for local development

## How to Use Qdrant

### 1. Access the Dashboard
Open your browser:
```
http://localhost:6334/dashboard
```

### 2. Create a Collection

#### Via REST API
```bash
curl -X PUT http://localhost:6333/collections/my_collection \
  -H "Content-Type: application/json" \
  -d '{
    "vectors": {
      "size": 384,
      "distance": "Cosine"
    }
  }'
```

**Vector Sizes for Common Models:**
- `all-MiniLM-L6-v2`: 384 dimensions
- `text-embedding-ada-002` (OpenAI): 1536 dimensions
- `all-mpnet-base-v2`: 768 dimensions

#### Distance Metrics
- **Cosine**: Best for normalized vectors (default for embeddings)
- **Euclidean**: For absolute distance
- **Dot**: For inner product similarity

### 3. Insert Vectors

```bash
curl -X PUT http://localhost:6333/collections/my_collection/points \
  -H "Content-Type: application/json" \
  -d '{
    "points": [
      {
        "id": 1,
        "vector": [0.1, 0.2, 0.3, ...],
        "payload": {
          "text": "This is a document",
          "category": "tech"
        }
      }
    ]
  }'
```

### 4. Search Vectors

#### Basic Search
```bash
curl -X POST http://localhost:6333/collections/my_collection/points/search \
  -H "Content-Type: application/json" \
  -d '{
    "vector": [0.1, 0.2, 0.3, ...],
    "limit": 5
  }'
```

#### Search with Filters
```bash
curl -X POST http://localhost:6333/collections/my_collection/points/search \
  -H "Content-Type: application/json" \
  -d '{
    "vector": [0.1, 0.2, 0.3, ...],
    "filter": {
      "must": [
        {"key": "category", "match": {"value": "tech"}}
      ]
    },
    "limit": 5
  }'
```

## Integration with Other Services

### Flowise Integration
1. Add "Qdrant" vector store node
2. Configure:
   - **URL**: `http://nostack-qdrant:6333`
   - **Collection**: Your collection name
   - **Embeddings**: Select model (must match collection dimensions)

### Langflow Integration
1. Add Qdrant component
2. Set URL: `http://nostack-qdrant:6333`
3. Configure collection and embeddings

### Python Integration
```python
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)

# Create collection
client.create_collection(
    collection_name="my_collection",
    vectors_config={"size": 384, "distance": "Cosine"}
)

# Insert vectors
client.upsert(
    collection_name="my_collection",
    points=[
        {
            "id": 1,
            "vector": [0.1, 0.2, ...],
            "payload": {"text": "Document text"}
        }
    ]
)

# Search
results = client.search(
    collection_name="my_collection",
    query_vector=[0.1, 0.2, ...],
    limit=5
)
```

## Advanced Features

### Payload Indexing
Create indexes for faster filtering:
```bash
curl -X PUT http://localhost:6333/collections/my_collection/index \
  -H "Content-Type: application/json" \
  -d '{
    "field_name": "category",
    "field_schema": "keyword"
  }'
```

### Batch Operations
Upload multiple points efficiently:
```bash
curl -X PUT http://localhost:6333/collections/my_collection/points/batch \
  -H "Content-Type: application/json" \
  -d '{
    "points": [...]
  }'
```

### Snapshots
Create backups:
```bash
curl -X POST http://localhost:6333/collections/my_collection/snapshots
```

## Common Use Cases

### 1. Semantic Search
Store document embeddings and search by meaning, not keywords.

### 2. Recommendation Systems
Find similar items based on vector similarity.

### 3. RAG (Retrieval Augmented Generation)
Store knowledge base embeddings for LLM context retrieval.

### 4. Duplicate Detection
Find similar or duplicate content using vector similarity.

## Monitoring

### Collection Info
```bash
curl http://localhost:6333/collections/my_collection
```

### Cluster Info
```bash
curl http://localhost:6333/cluster
```

### Health Check
```bash
curl http://localhost:6333/healthz
```

## Backup and Restore

### Create Snapshot
```bash
curl -X POST http://localhost:6333/collections/my_collection/snapshots
```

### List Snapshots
```bash
curl http://localhost:6333/collections/my_collection/snapshots
```

### Restore from Snapshot
```bash
curl -X PUT http://localhost:6333/collections/my_collection/snapshots/upload \
  -H "Content-Type: multipart/form-data" \
  -F "snapshot=@snapshot.tar"
```

## Troubleshooting

### Check Logs
```bash
docker logs nostack-qdrant
```

### Restart Qdrant
```bash
docker restart nostack-qdrant
```

### Clear Collection
```bash
curl -X DELETE http://localhost:6333/collections/my_collection
```

## Performance Tips

1. **Use Batch Operations**: Insert multiple points at once
2. **Index Payloads**: Create indexes for frequently filtered fields
3. **Optimize Vector Size**: Use smaller embeddings when possible
4. **Use HNSW**: Default index is optimized for speed

## Resources

- [Official Documentation](https://qdrant.tech/documentation/)
- [API Reference](https://qdrant.github.io/qdrant/redoc/index.html)
- [GitHub Repository](https://github.com/qdrant/qdrant)
- [Python Client](https://github.com/qdrant/qdrant-client)
