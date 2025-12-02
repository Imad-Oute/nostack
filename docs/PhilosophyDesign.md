📦 NoStack: Folder Structure & Infrastructure Summary

This document explains the full architecture, folder structure, and design philosophy of the NoStack/ infrastructure.
The core goal is simple:

✅ Have every service, every database, every config file, and every piece of data inside one single folder — fully portable, fully isolated, and fully controllable.

This approach makes the entire AI development environment modular, extensible, reproducible, and easy to manage.

🧠 Design Philosophy

The entire infrastructure follows 4 universal layers used in modern AI developer stacks:

Layer 1 — Orchestration

Handles everything related to:

Docker services

Networking

Environment variables

Service connections

Files:

docker-compose.yml

.env

Layer 2 — Storage (Volumes)

Persisted and local data for:

Databases

Vector stores

Graph stores

Memory systems

App data

This ensures no service stores anything in hidden Docker volumes → everything is visible and easy to back up.

Layer 3 — Services (Source Code / Apps)

Every external application (Flowise, Langflow, OpenWebUI, Zep, etc.) gets its own folder.
This allows:

Full customization

Version tracking

Local development

Hot-reloading

Layer 4 — Configuration

All config files live here:

Zep config

Qdrant config

Flowise config

Neo4j config

OpenWebUI env
This gives you full transparency over how each service is wired.

📁 Full Folder Structure Overview
ai-dev-stack/
│
├── docker-compose.yml           <-- Layer 1: Orchestration
├── .env                         <-- Layer 1: Global environment variables
│
├── postgres-data/               <-- Layer 2: Databases (PostgreSQL)
│   ├── zep/
│   ├── nhn/
│   ├── flowise/
│   ├── neo/
│   └── openwebui/
│
├── data/                        <-- Layer 2: File-based datastores
│   ├── qdrant/
│   ├── neo4j/
│   ├── zep/
│   └── flowise/
│
├── services/                    <-- Layer 3: App source code
│   ├── openwebui-frontend/
│   ├── openwebui-backend/
│   ├── flowise/
│   ├── nhn/
│   ├── zep/
│   └── neo4j/
│
└── config/                      <-- Layer 4: Configurations
    ├── flowise.json
    ├── zep.yaml
    ├── qdrant.yml
    ├── openwebui.env
    └── neo4j.conf

🔍 Detailed Explanation of Each Layer
🔹 Layer 1 — Orchestration (docker-compose.yml, .env)

This is the brain of the entire dev stack.

docker-compose.yml:

Defines all services

Mounts volumes

Connects containers together

Defines ports, networks, images

Links all database paths

.env:
Centralized configuration:

API keys

Postgres passwords

Ports

External URLs

Webhook URLs (e.g., n8n)

Your entire stack becomes portable → copy/paste the folder anywhere, and it works.

🔹 Layer 2 — Data Storage

This layer ensures complete data persistence.

🗄️ postgres-data/

Contains every PostgreSQL database for every service:

zep/ → memory store

nhn/ → your custom service

flowise/ → Flowise internal DB

neo/ → application metadata

openwebui/ → user data & chat history

Everything lives locally → traditional Docker volumes are avoided to keep everything transparent.

💽 data/

File-based datastores:

qdrant/ → vector embeddings

neo4j/ → graph database storage

zep/ → memory cache

flowise/ → flow JSONs or binary data

This separation lets you see exactly what each service stores.

🔹 Layer 3 — Services (services/)

Each service has its own sandbox folder:

services/
  ├── openwebui-frontend/
  ├── openwebui-backend/
  ├── flowise/
  ├── nhn/
  ├── zep/
  ├── neo4j/


This allows:

Custom build overrides

Editing UI/UX

Cloning Git repos directly into the folder

Version pinning

Local code modifications

You fully control the services you run — no black-box containers.

🔹 Layer 4 — Configurations (config/)

All config files for all services are saved under one folder.

config/
  flowise.json
  zep.yaml
  qdrant.yml
  openwebui.env
  neo4j.conf


Instead of configs being spread across:

/etc/

inside containers

Docker volumes

hardcoded image defaults

They are centralized here, ensuring:

100% clarity

Easy customization

Version control compatibility

Shareability

🚀 Why This Architecture Is Powerful
1️⃣ Everything in ONE folder

No hidden volumes
No disconnected services
No mystery locations
No wondering “where is my data?”

2️⃣ Portable

Zip the folder → same environment everywhere:

New laptop

New server

Cloud deployment

Local dev machine

3️⃣ Extensible

To add a new service (e.g., Langflow), you simply:

Add one folder under /services

Add one folder under /data (if needed)

Add one section to docker-compose.yml

Add config file under /config

4️⃣ Debuggable

You always know:

Where logs are

Where data lives

How services connect

What ports are used

5️⃣ Professional-grade

This is the same architecture used by:

Kubernetes development clusters

Enterprise AI platforms

Research labs

Full-stack developer teams