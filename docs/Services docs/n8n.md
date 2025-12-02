# n8n - Workflow Automation Platform

## Overview

n8n is a powerful, low-code workflow automation platform with over 400 integrations. It enables you to connect different services, APIs, and databases to create complex automation workflows and AI agent pipelines.

## Technical Configuration

### Database
- **Type**: PostgreSQL
- **Database Name**: `n8n`
- **Connection**: `nostack-postgres:5432`
- **Persistence**: All workflows, credentials, and executions are stored in PostgreSQL

### Data Storage
- **Workflows**: Stored in PostgreSQL database
- **Binary Data**: `data/n8n/binaryData/`
- **Custom Nodes**: `data/n8n/nodes/`
- **Configuration**: `data/n8n/config/`

### Authentication
- **Type**: Basic Auth (configurable)
- **Default User**: `admin` (change in `.env`)
- **Default Password**: `password` (change in `.env`)

## How to Use n8n

### 1. Access the Editor
Open your browser and navigate to:
```
http://localhost:5679
```

### 2. Create Your First Workflow

#### Example: Simple HTTP Webhook
1. Add a **Webhook** node (trigger)
2. Set the webhook path (e.g., `/test`)
3. Add a **Function** node to process data
4. Add a **Respond to Webhook** node
5. Click "Execute Workflow"
6. Test: `curl http://localhost:5679/webhook/test`

#### Example: Database Query
1. Add a **Schedule Trigger** node
2. Add a **Postgres** node
3. Configure connection:
   - Host: `nostack-postgres`
   - Port: `5432`
   - Database: `n8n` (or any other)
   - User: `postgres`
   - Password: Your password
4. Write your SQL query
5. Add processing nodes as needed

### 3. Working with AI Services

#### Integrate with Flowise
1. Add **HTTP Request** node
2. Method: `POST`
3. URL: `http://nostack-flowise:3000/api/v1/prediction/{flowId}`
4. Body: Your input data
5. Headers: `Authorization: Bearer {API_KEY}`

#### Integrate with Zep (Memory)
1. Add **HTTP Request** node
2. URL: `http://nostack-zep:8000/api/v1/sessions/{sessionId}/memory`
3. Headers: `Authorization: Bearer {ZEP_API_KEY}`
4. Use for storing/retrieving conversation context

#### Integrate with Qdrant (Vector Store)
1. Add **HTTP Request** node
2. URL: `http://nostack-qdrant:6333/collections/{collection}/points`
3. Use for semantic search and vector operations

## Webhook Configuration

### Ngrok Setup (for External Access)
Configure in `.env`:
```bash
N8N_EDITOR_BASE_URL=https://your-domain.ngrok-free.dev
WEBHOOK_URL=https://your-domain.ngrok-free.dev
N8N_EXPRESS_TRUST_PROXY=true
```

### Local Testing
For local development:
```bash
N8N_EDITOR_BASE_URL=http://localhost:5679
WEBHOOK_URL=http://localhost:5679
```

## Advanced Features

### Custom Nodes
Install custom nodes in `data/n8n/nodes/`:
```bash
cd data/n8n/nodes
npm init -y
npm install n8n-nodes-{package-name}
```

Restart n8n to load new nodes:
```bash
docker restart nostack-n8n
```

### Environment Variables in Workflows
Access environment variables in Function nodes:
```javascript
const apiKey = $env.MY_API_KEY;
```

### Workflow Templates
Save workflows as JSON and share them:
1. Open workflow
2. Click "..." menu
3. Select "Download"
4. Share the JSON file

## Integration Patterns

### Pattern 1: AI Agent Pipeline
```
Webhook → Extract Data → Call LLM (Flowise) → Store in Zep → Respond
```

### Pattern 2: Data Processing
```
Schedule → Query Database → Transform Data → Send to API → Log Results
```

### Pattern 3: Multi-Agent System
```
Webhook → Route to Agent (Langflow) → Process → Store in Neo4j → Respond
```

## Database Access

### Query n8n Database
```bash
docker exec -it nostack-postgres psql -U postgres -d n8n
```

### Common Queries

#### List all workflows:
```sql
SELECT id, name, active FROM workflow_entity;
```

#### View workflow executions:
```sql
SELECT id, workflow_id, finished, mode 
FROM execution_entity 
ORDER BY started_at DESC 
LIMIT 10;
```

## Configuration Files

### Environment Variables
```bash
N8N_PORT=5679
N8N_DB_TYPE=postgresdb
N8N_DB_POSTGRESDB_HOST=nostack-postgres
N8N_DB_POSTGRESDB_PORT=5432
N8N_DB_POSTGRESDB_DB=n8n
N8N_DB_POSTGRESDB_USER=postgres
N8N_DB_POSTGRESDB_PASSWORD=your-password
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=password
```

## Backup and Restore

### Export All Workflows
1. Go to Workflows page
2. Select all workflows
3. Click "Download"
4. Save JSON file

### Backup Database
```bash
docker exec nostack-postgres pg_dump -U postgres n8n > n8n_backup.sql
```

### Restore Database
```bash
docker exec -i nostack-postgres psql -U postgres n8n < n8n_backup.sql
```

## Troubleshooting

### Check Logs
```bash
docker logs nostack-n8n
docker logs -f nostack-n8n  # Follow logs
```

### Restart n8n
```bash
docker restart nostack-n8n
```

### Clear Execution Data
```sql
docker exec -it nostack-postgres psql -U postgres -d n8n -c "DELETE FROM execution_entity WHERE finished = true;"
```

### Reset Webhooks
If webhooks aren't working:
1. Check `WEBHOOK_URL` in `.env`
2. Restart n8n: `docker restart nostack-n8n`
3. Deactivate and reactivate workflow

## Best Practices

1. **Use Credentials**: Store API keys in n8n Credentials, not in nodes
2. **Error Handling**: Add Error Trigger nodes to catch failures
3. **Logging**: Use Set node to log important data
4. **Testing**: Use Execute Node to test individual nodes
5. **Version Control**: Export workflows regularly as JSON

## Resources

- [Official Documentation](https://docs.n8n.io/)
- [Community Forum](https://community.n8n.io/)
- [Workflow Templates](https://n8n.io/workflows/)
- [Node Reference](https://docs.n8n.io/integrations/)
