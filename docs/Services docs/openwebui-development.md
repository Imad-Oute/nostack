# OpenWebUI Development Guide

## Overview
OpenWebUI is now configured for local development with full source code access.

## Repository Location
- **Path**: `/home/sog/infrastack/ai-dev-stack/services/openwebui-backend`
- **Repository**: https://github.com/Imad-Oute/open-webui.git

## Development Configuration

### Docker Setup
The OpenWebUI service is configured to:
- Build from source (not use pre-built image)
- Mount source code for live development
- Run in development mode (`ENV=dev`)

### Volume Mounts
```yaml
volumes:
  - ./postgres-data/openwebui:/app/backend/data  # Data persistence
  - ./services/openwebui-backend/backend:/app/backend  # Backend source code
  - ./services/openwebui-backend/src:/app/src  # Frontend source code
```

### Environment Variables
- `DATABASE_URL`: PostgreSQL connection string
- `WEBUI_SECRET_KEY`: Secret key for sessions
- `ENV`: Set to `dev` for development mode

## Development Workflow

### 1. Making Code Changes
Edit files in:
- **Backend**: `services/openwebui-backend/backend/`
- **Frontend**: `services/openwebui-backend/src/`

### 2. Rebuilding After Changes
```bash
cd /home/sog/infrastack/ai-dev-stack

# Rebuild and restart OpenWebUI
docker compose up -d --build openwebui-backend

# Or just restart (for Python changes that don't need rebuild)
docker compose restart openwebui-backend
```

### 3. Viewing Logs
```bash
docker logs ai-openwebui-backend -f
```

### 4. Accessing the Application
- **URL**: http://localhost:3005
- **Database**: PostgreSQL (credentials: `postgres/imad.123`)

## Project Structure
```
services/openwebui-backend/
├── backend/          # FastAPI backend
│   ├── apps/        # Application modules
│   ├── config.py    # Configuration
│   └── main.py      # Entry point
├── src/             # SvelteKit frontend
│   ├── lib/         # Components and utilities
│   └── routes/      # Page routes
├── Dockerfile       # Production build
└── package.json     # Frontend dependencies
```

## Common Tasks

### Install Frontend Dependencies
```bash
cd services/openwebui-backend
npm install
```

### Run Frontend Dev Server (Optional)
```bash
cd services/openwebui-backend
npm run dev
```

### Run Backend Locally (Optional)
```bash
cd services/openwebui-backend/backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
```

## Troubleshooting

### Container Won't Start
```bash
# Check logs
docker logs ai-openwebui-backend

# Rebuild from scratch
docker compose build --no-cache openwebui-backend
docker compose up -d openwebui-backend
```

### Database Connection Issues
- Verify PostgreSQL is running: `docker ps | grep ai-postgres`
- Check connection string in `.env`: `OPENWEBUI_DB_URL`

### Port Conflicts
- OpenWebUI runs on port 3005 (configurable in `.env`)
- Ensure no other service is using this port

## Next Steps
1. Explore the codebase in `services/openwebui-backend`
2. Make your changes
3. Test locally
4. Rebuild and restart the container
