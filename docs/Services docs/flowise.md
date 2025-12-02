# Flowise - AI Agent Builder

## Overview

Flowise is a no/low-code platform for building LLM applications and AI agents. It provides a visual interface to create complex AI workflows, chatbots, and agent systems without writing code.

## Technical Configuration

### Database
- **Type**: PostgreSQL
- **Database Name**: `flowise`
- **Connection**: `ai-postgres:5432`
- **Purpose**: Stores chatflows, API keys, and configurations

### Data Storage
- **Chatflows**: Stored in PostgreSQL
- **Uploads**: `data/flowise/uploads/`
- **Config**: `data/flowise/config.json`
- **API Keys**: `data/flowise/`

### Port
- **Web UI**: `http://localhost:3002`
- **API**: `http://localhost:3002/api/v1`

## How to Use Flowise

### 1. Access the UI
Open your browser:
```
http://localhost:3002
```

### 2. Create Your First Chatflow

#### Simple LLM Chat
1. Click "Add New" chatflow
2. Drag **Chat Models** → Select your LLM (e.g., OpenAI, Ollama)
3. Drag **Chains** → Select "Conversation Chain"
4. Connect nodes
5. Click "Save" and "Deploy"

#### RAG (Retrieval Augmented Generation)
1. Add **Document Loaders** (PDF, Text, etc.)
2. Add **Text Splitters** (Recursive Character)
3. Add **Embeddings** (OpenAI or local)
4. Add **Vector Store** (Qdrant)
5. Add **Retrieval QA Chain**
6. Add **Chat Model**
7. Connect and deploy

### 3. Using Vector Stores

#### Connect to Qdrant
1. Add "Qdrant" node
2. Configure:
   - **URL**: `http://ai-qdrant:6333`
   - **Collection Name**: Your collection name
   - **Embeddings**: Select embedding model

#### Connect to PostgreSQL (pgvector)
1. Add "Postgres" vector store node
2. Configure:
   - **Host**: `ai-postgres`
   - **Port**: `5432`
   - **Database**: Your database
   - **Table Name**: Your table

## API Usage

### Get Chatflows
```bash
curl http://localhost:3002/api/v1/chatflows
```

### Execute Prediction
```bash
curl -X POST http://localhost:3002/api/v1/prediction/{chatflowId} \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is AI?",
    "overrideConfig": {}
  }'
```

### With API Key
```bash
curl -X POST http://localhost:3002/api/v1/prediction/{chatflowId} \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"question": "Hello"}'
```

## Integration with Other Services

### n8n Integration
Use HTTP Request node:
```
URL: http://ai-flowise:3000/api/v1/prediction/{chatflowId}
Method: POST
Body: {"question": "{{$json.userInput}}"}
```

### Zep Memory Integration
1. Add "Zep Memory" node in Flowise
2. Configure:
   - **Base URL**: `http://ai-zep:8000`
   - **API Key**: Your Zep API key
   - **Session ID**: User identifier

### Qdrant Integration
1. Add "Qdrant" vector store
2. URL: `http://ai-qdrant:6333`
3. Use for document storage and retrieval

## Configuration

### Environment Variables
```bash
FLOWISE_PORT=3002
FLOWISE_DB_PORT=5432
FLOWISE_DB_USER=postgres
FLOWISE_DB_PASSWORD=your-password
FLOWISE_DB_NAME=flowise
```

### Config File (`config/flowise.json`)
```json
{
  "port": 3000,
  "database": {
    "type": "postgres",
    "host": "ai-postgres",
    "port": 5432,
    "database": "flowise"
  }
}
```

## Advanced Features

### Custom Functions
Use the "Custom JS Function" node to write custom logic:
```javascript
const processData = (input) => {
  // Your custom logic
  return transformedData;
};
```

### Streaming Responses
Enable streaming in chatflow settings for real-time responses.

### Multi-Agent Systems
Combine multiple agents using:
- **Agent** nodes
- **Tools** nodes
- **Memory** nodes

## Backup and Restore

### Export Chatflows
1. Go to Chatflows page
2. Click "..." on chatflow
3. Select "Export"
4. Save JSON file

### Backup Database
```bash
docker exec ai-postgres pg_dump -U postgres flowise > flowise_backup.sql
```

## Troubleshooting

### Check Logs
```bash
docker logs ai-flowise
docker logs -f ai-flowise
```

### Clear Cache
```bash
docker exec ai-flowise rm -rf /root/.flowise/cache
docker restart ai-flowise
```

### Database Connection Issues
Check connection string in `config/flowise.json` and environment variables.

## Resources

- [Official Documentation](https://docs.flowiseai.com/)
- [GitHub Repository](https://github.com/FlowiseAI/Flowise)
- [Community Discord](https://discord.gg/jbaHfsRVBW)
