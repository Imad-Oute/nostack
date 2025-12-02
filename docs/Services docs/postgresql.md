# PostgreSQL - Relational Database with pgvector

## Overview

PostgreSQL is a powerful, open-source relational database system. This stack uses the `pgvector` extension, enabling vector similarity search for AI applications alongside traditional relational data.

## Technical Configuration

### Version
- **PostgreSQL**: 16
- **Extension**: pgvector (for vector operations)

### Storage
- **Data Directory**: `postgres-data/`
- **Init Scripts**: `config/init-db.sh`

### Port
- **Database**: `localhost:5432`

### Authentication
- **User**: `postgres`
- **Password**: Set in `.env` (`POSTGRES_PASSWORD`)

## Databases in the Stack

The stack creates multiple databases for different services:

| Database | Purpose | Used By |
|----------|---------|---------|
| `postgres` | Default database | System |
| `n8n` | Workflow storage | n8n |
| `flowise` | Chatflow storage | Flowise |
| `langflow` | Flow storage | Langflow |
| `zep` | Memory storage | Zep |
| `openwebui` | User data & chats | OpenWebUI |

## How to Use PostgreSQL

### 1. Connect to Database

#### Using psql (CLI)
```bash
docker exec -it ai-postgres psql -U postgres
```

#### Connect to Specific Database
```bash
docker exec -it ai-postgres psql -U postgres -d n8n
```

### 2. Basic SQL Operations

#### Create Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Insert Data
```sql
INSERT INTO users (name, email) 
VALUES ('Alice', 'alice@example.com');
```

#### Query Data
```sql
SELECT * FROM users WHERE name = 'Alice';
```

### 3. Using pgvector for AI

#### Enable Extension
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

#### Create Table with Vectors
```sql
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding vector(384)  -- 384 dimensions for all-MiniLM-L6-v2
);
```

#### Insert Vectors
```sql
INSERT INTO documents (content, embedding)
VALUES (
    'This is a document',
    '[0.1, 0.2, 0.3, ...]'::vector
);
```

#### Vector Similarity Search
```sql
-- Cosine similarity
SELECT content, 
       1 - (embedding <=> '[0.1, 0.2, ...]'::vector) AS similarity
FROM documents
ORDER BY embedding <=> '[0.1, 0.2, ...]'::vector
LIMIT 5;

-- Euclidean distance
SELECT content,
       embedding <-> '[0.1, 0.2, ...]'::vector AS distance
FROM documents
ORDER BY distance
LIMIT 5;
```

## Common Vector Dimensions

| Model | Dimensions |
|-------|-----------|
| all-MiniLM-L6-v2 | 384 |
| all-mpnet-base-v2 | 768 |
| text-embedding-ada-002 (OpenAI) | 1536 |
| text-embedding-3-small (OpenAI) | 1536 |
| text-embedding-3-large (OpenAI) | 3072 |

## Integration with Other Services

### n8n Integration
1. Add **Postgres** node
2. Configure:
   - **Host**: `ai-postgres`
   - **Port**: `5432`
   - **Database**: Your database name
   - **User**: `postgres`
   - **Password**: From `.env`

### Python Integration
```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="your-password"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
```

### Flowise/Langflow Integration
Use the "Postgres" vector store component with pgvector support.

## Database Management

### List All Databases
```sql
\l
```

### List Tables
```sql
\dt
```

### Describe Table
```sql
\d table_name
```

### Database Size
```sql
SELECT 
    pg_database.datname,
    pg_size_pretty(pg_database_size(pg_database.datname)) AS size
FROM pg_database
ORDER BY pg_database_size(pg_database.datname) DESC;
```

## Backup and Restore

### Backup Single Database
```bash
docker exec ai-postgres pg_dump -U postgres n8n > n8n_backup.sql
```

### Backup All Databases
```bash
docker exec ai-postgres pg_dumpall -U postgres > all_databases_backup.sql
```

### Restore Database
```bash
docker exec -i ai-postgres psql -U postgres -d n8n < n8n_backup.sql
```

### Automated Backup Script
```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
docker exec ai-postgres pg_dumpall -U postgres > backup_$DATE.sql
```

## Performance Optimization

### Create Indexes
```sql
CREATE INDEX idx_users_email ON users(email);
```

### Vector Indexes (HNSW)
```sql
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops);
```

### Analyze Query Performance
```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'alice@example.com';
```

## Monitoring

### Active Connections
```sql
SELECT * FROM pg_stat_activity;
```

### Database Statistics
```sql
SELECT * FROM pg_stat_database;
```

### Table Statistics
```sql
SELECT * FROM pg_stat_user_tables;
```

## Troubleshooting

### Check Logs
```bash
docker logs ai-postgres
```

### Restart PostgreSQL
```bash
docker restart ai-postgres
```

### Connection Issues
Check if PostgreSQL is running:
```bash
docker exec ai-postgres pg_isready -U postgres
```

### Reset Password
```bash
docker exec -it ai-postgres psql -U postgres -c "ALTER USER postgres PASSWORD 'new-password';"
```

## Security Best Practices

1. **Change Default Password**: Update `POSTGRES_PASSWORD` in `.env`
2. **Use Strong Passwords**: Minimum 16 characters
3. **Limit Connections**: Configure `max_connections` in `neo4j.conf`
4. **Regular Backups**: Automate daily backups
5. **Monitor Access**: Review `pg_stat_activity` regularly

## Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [pgvector Documentation](https://github.com/pgvector/pgvector)
- [SQL Tutorial](https://www.postgresqltutorial.com/)
