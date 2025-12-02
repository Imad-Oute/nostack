# Langflow - Visual AI Framework

## Overview

Langflow is a visual framework for building multi-agent AI applications and LLM flows. It provides a drag-and-drop interface to create complex AI pipelines, agents, and workflows.

## Technical Configuration

### Database
- **Type**: PostgreSQL
- **Database Name**: `langflow`
- **Connection**: `ai-postgres:5432`

### Data Storage
- **Flows**: Stored in PostgreSQL
- **Uploads**: `data/langflow/`
- **Config**: `config/langflow.env`

### Port
- **Web UI**: `http://localhost:7860`
- **API**: `http://localhost:7860/api/v1`

## How to Use Langflow

### 1. Access the UI
Open your browser:
```
http://localhost:7860
```

### 2. Create Your First Flow

#### Simple LLM Chain
1. Click "New Flow"
2. Add **LLM** component (OpenAI, Anthropic, or local)
3. Add **Prompt Template** component
4. Add **Output** component
5. Connect components
6. Click "Run"

#### Multi-Agent System
1. Add multiple **Agent** components
2. Add **Tools** (Calculator, Search, etc.)
3. Add **Memory** component (optional)
4. Connect agents with routing logic
5. Test the flow

### 3. Using Components

#### LLM Components
- **OpenAI**: GPT-3.5, GPT-4
- **Anthropic**: Claude
- **HuggingFace**: Open-source models
- **Ollama**: Local models

#### Memory Components
- **Buffer Memory**: Simple conversation memory
- **Zep Memory**: Long-term memory with Zep integration
- **Vector Store Memory**: Semantic memory

#### Vector Stores
- **Qdrant**: Connect to `http://ai-qdrant:6333`
- **PostgreSQL**: Use pgvector extension
- **Chroma**: Local vector store

## API Usage

### Run Flow
```bash
curl -X POST http://localhost:7860/api/v1/run/{flow_id} \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": {
      "input": "What is AI?"
    }
  }'
```

### Get Flows
```bash
curl http://localhost:7860/api/v1/flows
```

## Integration with Other Services

### n8n Integration
```
URL: http://ai-langflow:7860/api/v1/run/{flow_id}
Method: POST
Body: {"inputs": {"input": "{{$json.userMessage}}"}}
```

### Zep Integration
1. Add "Zep Memory" component
2. Configure:
   - **URL**: `http://ai-zep:8000`
   - **API Key**: Your Zep API key

### Qdrant Integration
1. Add "Qdrant" vector store
2. URL: `http://ai-qdrant:6333`
3. Collection: Your collection name

## Configuration

### Environment Variables (`config/langflow.env`)
```bash
LANGFLOW_DATABASE_URL=postgresql://postgres:password@ai-postgres:5432/langflow
LANGFLOW_PORT=7860
```

## Advanced Features

### Custom Components
Create custom Python components:
```python
from langflow import CustomComponent

class MyComponent(CustomComponent):
    def build(self):
        # Your logic here
        return result
```

### Streaming
Enable streaming for real-time responses in chat applications.

### API Keys Management
Store API keys securely in Langflow's credential manager.

## Backup and Restore

### Export Flows
1. Select flow
2. Click "Export"
3. Save JSON file

### Backup Database
```bash
docker exec ai-postgres pg_dump -U postgres langflow > langflow_backup.sql
```

## Troubleshooting

### Check Logs
```bash
docker logs ai-langflow
```

### Restart Service
```bash
docker restart ai-langflow
```

## Resources

- [Official Documentation](https://docs.langflow.org/)
- [GitHub Repository](https://github.com/logspace-ai/langflow)
- [Community Discord](https://discord.gg/EqksyE2EX9)
