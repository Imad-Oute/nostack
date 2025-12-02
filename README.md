# 🚀 AI Development Stack

A comprehensive, production-ready Docker-based development stack for building AI-powered applications. This stack integrates multiple AI/ML tools, workflow automation, vector databases, and memory systems into a unified development environment.

## 📋 Table of Contents

- [Overview](#overview)
- [Design Philosophy](#-design-philosophy)
- [Architecture](#architecture)
- [Services Included](#services-included)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Service Access](#service-access)
- [Configuration](#configuration)
- [Database Management](#database-management)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Documentation](#documentation)
- [Contributing](#contributing)

## 📂 Folder Structure

```
ai-dev-stack/
├── config/                 # Configuration files for services
│   ├── init-db.sh          # Database initialization script
│   ├── langflow.env        # Langflow environment variables
│   ├── neo4j.conf          # Neo4j configuration
│   ├── openwebui.env       # OpenWebUI environment variables
│   ├── qdrant.yml          # Qdrant configuration
│   └── zep.yaml            # Zep configuration
├── data/                   # Persistent data storage for services
│   ├── flowise/            # Flowise data
│   ├── langflow/           # Langflow data
│   ├── n8n/                # n8n data
│   ├── neo4j/              # Neo4j data
│   ├── qdrant/             # Qdrant data
│   ├── redis/              # Redis data
│   └── zep-nlp/            # Zep NLP cache
├── docs/                   # Documentation files
│   ├── architecture.svg    # Architecture diagram
│   └── ...                 # Other documentation
├── postgres-data/          # PostgreSQL data storage
├── services/               # Source code for custom services
│   └── openwebui-backend/  # OpenWebUI backend source
├── .env.example            # Example environment variables
├── docker-compose.yml      # Main Docker Compose file
└── README.md               # Project documentation
```

## 🎯 Overview

This stack provides a complete AI development environment with:

- **Workflow Automation**: n8n and Flowise for building AI workflows
- **AI Flow Builder**: Langflow for visual AI application development
- **Vector Database**: Qdrant for semantic search and embeddings
- **Graph Database**: Neo4j for knowledge graphs and relationships
- **Memory System**: Zep for conversational AI memory management
- **Data Layer**: PostgreSQL with pgvector extension and Redis
- **UI Framework**: OpenWebUI backend for chat interfaces

All services are containerized, networked, and configured to work together seamlessly.

## 🧠 Design Philosophy

The entire infrastructure follows 4 universal layers used in modern AI developer stacks:

### Layer 1 — Orchestration

Handles everything related to:

- Docker services
- Networking
- Environment variables
- Service connections

**Files:**
- `docker-compose.yml`
- `.env`

### Layer 2 — Storage (Volumes)

Persisted and local data for:

- Databases
- Vector stores
- Graph stores
- Memory systems
- App data

This ensures no service stores anything in hidden Docker volumes → everything is visible and easy to back up.

### Layer 3 — Services (Source Code / Apps)

Every external application (Flowise, Langflow, OpenWebUI, Zep, etc.) gets its own folder.
This allows:

- Full customization
- Version tracking
- Local development
- Hot-reloading

### Layer 4 — Configuration

All config files live here:

- Zep config
- Qdrant config
- Flowise config
- Neo4j config
- OpenWebUI env

This gives you full transparency over how each service is wired.

## 🏗️ Architecture

![Architecture Diagram](docs/architecture.svg)

## 🛠️ Services Included

### Application Services

| Service | Description | Port | Documentation |
|---------|-------------|------|---------------|
| **n8n** | Workflow automation platform | 5679 | [n8n Docs](https://docs.n8n.io/) |
| **Flowise** | Build LLM apps with drag-and-drop | 3002 | [Flowise Docs](https://docs.flowiseai.com/) |
| **Langflow** | Visual framework for AI applications | 7860 | [Langflow Docs](https://docs.langflow.org/) |
| **OpenWebUI** | Chat UI backend for LLMs | 3005 | [OpenWebUI Docs](https://docs.openwebui.com/) |

### AI/ML Services

| Service | Description | Port |
|---------|-------------|------|
| **Zep** | Long-term memory for AI assistants | 8002 |
| **Zep NLP** | Embedding service for Zep | 5555 |

### Data Layer

| Service | Description | Port |
|---------|-------------|------|
| **PostgreSQL** | Primary database with pgvector | 5435 |
| **Redis** | Cache and message broker | 6380 |
| **Qdrant** | Vector database for embeddings | 6334 |
| **Neo4j** | Graph database | 7475 (HTTP), 7688 (Bolt) |

### Management Tools

| Service | Description | Port |
|---------|-------------|------|
| **Redis Commander** | Redis web UI | 8081 |

## 📦 Prerequisites

- **Docker**: Version 20.10 or higher
- **Docker Compose**: Version 2.0 or higher
- **System Resources**:
  - Minimum: 8GB RAM, 20GB disk space
  - Recommended: 16GB RAM, 50GB disk space
- **Ports**: Ensure the following ports are available:
  - 3002, 3005, 5435, 5555, 5679, 6334, 6380, 7475, 7688, 7860, 8002, 8081

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-dev-stack
```

### 2. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your preferred settings
nano .env  # or use your favorite editor
```

### 3. Start the Stack

```bash
# Start all services
docker compose up -d

# Check service status
docker compose ps

# View logs
docker compose logs -f
```

### 4. Verify Installation

```bash
# Check all containers are running
docker ps --filter "name=ai-"

# Test service health
curl http://localhost:7860/  # Langflow
curl http://localhost:3002/  # Flowise
curl http://localhost:5679/  # n8n
```

## 🌐 Service Access

### Web Interfaces

| Service | URL | Default Credentials |
|---------|-----|---------------------|
| **Langflow** | http://localhost:7860 | Create account on first visit |
| **Flowise** | http://localhost:3002 | No authentication by default |
| **n8n** | http://localhost:5679 | Create account on first visit |
| **OpenWebUI** | http://localhost:3005 | Create account on first visit |
| **Neo4j Browser** | http://localhost:7475 | User: `neo4j`, Pass: `password123` |
| **Redis Commander** | http://localhost:8081 | No authentication |
| **Qdrant Dashboard** | http://localhost:6334/dashboard | No authentication |

### API Endpoints

- **Zep API**: http://localhost:8002
- **Qdrant API**: http://localhost:6334/dashboard

### Database Connections

**PostgreSQL**:
```bash
Host: localhost
Port: 5435
User: postgres
Password: imad.123
Databases: maindb, n8n, flowise, zep, openwebui, langflow
```

**Redis**:
```bash
Host: localhost
Port: 6380
Password: redis.123
```

## ⚙️ Configuration

### Environment Files

The stack uses multiple environment files:

- **`.env`**: Main configuration for all services
- **`config/langflow.env`**: Langflow-specific settings
- **`config/openwebui.env`**: OpenWebUI-specific settings

See [`.env.example`](.env.example) for all available configuration options.

### Key Configuration Options

#### PostgreSQL
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password
POSTGRES_PORT=5435
```

#### Redis
```env
REDIS_PASSWORD=your_redis_password
REDIS_PORT=6380
```

#### n8n
```env
N8N_PORT=5679
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=your_password
```

See the [Configuration Guide](docs/configuration.md) for detailed information.

## 🗄️ Database Management

### PostgreSQL Databases

The stack automatically creates the following databases:

- `maindb` - Main database
- `n8n` - n8n workflows and credentials
- `flowise` - Flowise chatflows and configurations
- `zep` - Zep memory storage
- `openwebui` - OpenWebUI data
- `langflow` - Langflow flows and components

### Accessing PostgreSQL

```bash
# Using Docker
docker exec -it ai-postgres psql -U postgres -d maindb

# Using external client
psql -h localhost -p 5435 -U postgres -d maindb
```

### Database Backups

```bash
# Backup all databases
docker exec ai-postgres pg_dumpall -U postgres > backup_$(date +%Y%m%d).sql

# Backup specific database
docker exec ai-postgres pg_dump -U postgres -d langflow > langflow_backup.sql

# Restore database
cat backup.sql | docker exec -i ai-postgres psql -U postgres
```

## 💻 Development

### OpenWebUI Development

The OpenWebUI backend is configured for development with live code reloading:

```bash
# Source code is mounted at:
./services/openwebui-backend/backend
./services/openwebui-backend/src

# View logs
docker logs -f ai-openwebui-backend

# Restart after config changes
docker compose restart openwebui-backend
```

See [docs/openwebui-development.md](docs/openwebui-development.md) for more details.

### Adding Custom Services

1. Add service definition to `docker-compose.yml`
2. Add environment variables to `.env`
3. Create service-specific config in `config/` if needed
4. Update this README

### Volume Management

All persistent data is stored in:

- `./data/` - Application data (Redis, Qdrant, Neo4j, etc.)
- `./postgres-data/` - PostgreSQL data
- `./config/` - Configuration files

## 🔧 Troubleshooting

### Common Issues

#### Port Conflicts

If you get "port already in use" errors:

```bash
# Check what's using the port
lsof -i :7860  # Replace with your port

# Change port in .env file
LANGFLOW_PORT=7861
```

#### Service Won't Start

```bash
# Check logs
docker logs ai-<service-name>

# Restart service
docker compose restart <service-name>

# Rebuild service
docker compose up -d --build <service-name>
```

#### Database Connection Issues

```bash
# Check PostgreSQL is healthy
docker exec ai-postgres pg_isready -U postgres

# List all databases
docker exec ai-postgres psql -U postgres -c "\l"

# Create missing database
docker exec ai-postgres psql -U postgres -c "CREATE DATABASE <dbname>;"
```

#### Reset Everything

```bash
# Stop all services
docker compose down

# Remove all data (WARNING: This deletes all data!)
rm -rf data/ postgres-data/

# Start fresh
docker compose up -d
```

### Health Checks

```bash
# Check all container status
docker compose ps

# Check specific service health
docker inspect ai-postgres --format='{{.State.Health.Status}}'

# View all logs
docker compose logs

# Follow specific service logs
docker compose logs -f langflow
```

## 📚 Documentation

Additional documentation is available in the `docs/` directory:

- [Service Access Guide](docs/service-access.md) - Detailed access information
- [OpenWebUI Development](docs/openwebui-development.md) - Development setup
- [Local Embeddings](docs/local-embeddings.md) - Using local embedding models
- [Status Report](docs/status-report.md) - Current stack status

## 🔐 Security Notes

> [!WARNING]
> **This configuration is for development only!** Before deploying to production:

- Change all default passwords in `.env`
- Enable authentication on all services
- Use proper SSL/TLS certificates
- Configure firewalls and network security
- Review and restrict CORS settings
- Enable audit logging
- Regular security updates

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

This stack integrates the following open-source projects:

- [n8n](https://n8n.io/) - Workflow automation
- [Flowise](https://flowiseai.com/) - LLM orchestration
- [Langflow](https://www.langflow.org/) - AI application framework
- [OpenWebUI](https://openwebui.com/) - Chat interface
- [Zep](https://www.getzep.com/) - Memory management
- [Qdrant](https://qdrant.tech/) - Vector database
- [Neo4j](https://neo4j.com/) - Graph database
- [PostgreSQL](https://www.postgresql.org/) - Relational database
- [Redis](https://redis.io/) - Cache and message broker

---

**Built with ❤️ for the AI development community**
