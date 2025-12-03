<div align="center">
  <img src="./docs/logo.png" alt="NoStack Logo" width="120">
  <br>
  <img src="./docs/banner.png" alt="NoStack Banner" width="100%">
</div>

# 🚀 NoStack — AI Development Stack Template

**The definitive, production-grade infrastructure for building, deploying, and scaling AI agents.**

---

## ⭐ Overview

**NoStack** is a unified, high-performance development environment designed for elite engineering teams building next-generation AI applications. It eliminates the complexity of fragmented tools by providing a single, cohesive workspace where services, databases, configurations, and orchestration live in perfect harmony.

Built for **developers, founders, and AI architects**, NoStack offers a "one-folder" philosophy: every piece of your infrastructure—from vector databases to frontend UIs—is contained, portable, and production-ready from day one.

## ❗ The Problem

Building AI-powered applications today is an exercise in chaos. Developers are forced to wrestle with:

*   **Fragmented Stacks**: Juggling disparate tools that refuse to talk to each other.
*   **Infrastructure Hell**: Spending more time on Docker networking than on shipping features.
*   **Cognitive Overload**: Managing scattered configs, hidden volumes, and fragile dependencies.
*   **Deployment Pain**: What works locally rarely works in production without a complete rewrite.

## 💡 The Solution: NoStack

NoStack solves this by enforcing a **Unified Infrastructure Architecture**.

*   **Fully Unified**: Backend, frontend, agents, vector DBs, and workflows all in one place.
*   **One-Config Philosophy**: All configurations are centralized in `config/`. No more hunting for env vars.
*   **Local-First & Portable**: The entire stack lives in one folder. Zip it, move it, run it anywhere.
*   **Production-Ready Orchestration**: Pre-tuned Docker Compose setup that scales with you.
*   **Seamless Extension**: Plug in new services like Lego blocks.

## 🧱 Project Structure

NoStack follows a strict, logical hierarchy designed for clarity and control.

```text
nostack/
├── services/           # 🧠 Source Code: Isolated sandboxes for every app & service
├── frontend/           # 🎨 Frontend: Next.js / React interfaces
├── backend/            # ⚙️ Backend: Python / Node.js API logic
├── databases/          # 🗄️ Persistence: PostgreSQL, Qdrant, Neo4j data
├── config/             # 🎛️ Control Plane: Centralized configuration files
├── agents/             # 🤖 AI Agents: Custom agent logic and definitions
├── docs/               # 📚 Documentation: Architecture & guides
└── docker-compose.yml  # 🎼 Orchestration: The brain of the stack
```

### Architecture Philosophy
We believe in **radical transparency**. Nothing is hidden in Docker volumes. Every byte of data, every line of config, and every service definition is visible and accessible within the project root. This ensures that your development environment is identical to your production environment, eliminating the "it works on my machine" paradox.

## 🧠 Architecture Diagram

![Architecture](./docs/architecture.svg)

## 🔌 Adding New Services

NoStack is designed to be extensible. Adding a tool like **Langflow** or **crewAI** is as simple as:

1.  **Create a Service Folder**: `services/langflow`
2.  **Add Configuration**: Create `config/langflow.env`
3.  **Register in Orchestrator**: Add the service to `docker-compose.yml`

**Example Service Layout:**
```text
services/
└── my-new-agent/
    ├── Dockerfile
    ├── src/
    └── requirements.txt
```

## 🧰 Features

*   **Unified Control Plane**: Manage all AI services from a single entry point.
*   **Pre-Configured Vector Stores**: Qdrant and pgvector ready for RAG pipelines.
*   **Graph Knowledge Base**: Neo4j integration for complex relationship modeling.
*   **Workflow Automation**: n8n pre-wired for seamless agentic workflows.
*   **Memory Systems**: Zep integration for long-term LLM memory.
*   **Zero-Config Networking**: Internal DNS and service discovery handled automatically.

## 📦 Tech Stack

*   **Orchestration**: Docker Compose
*   **Automation**: n8n
*   **Vector Database**: Qdrant, PostgreSQL (pgvector)
*   **Graph Database**: Neo4j
*   **Memory**: Zep
*   **Interface**: OpenWebUI
*   **LLM Orchestration**: Langflow, Flowise
*   **Caching**: Redis

## ⚙️ Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-org/nostack.git
    cd nostack
    ```

2.  **Configure Environment**
    ```bash
    cp .env.example .env
    # Edit .env with your API keys
    ```

## 🚀 Running the Stack

**Start everything:**
```bash
docker compose up -d
```

**View Logs:**
```bash
docker compose logs -f
```

**Stop:**
```bash
docker compose down
```

## 🧩 Extending NoStack

### AI Agents
Drop your agent code into `agents/` or `services/`. Use the shared network to communicate with Qdrant or Zep.

### Custom Workflows
Access n8n at `http://localhost:5679` and start building. Webhooks are pre-routed.

### Third-Party Tools
Integrate tools like Zapier or Make via the exposed webhooks in `backend/`.

## 🤝 Contributing

We welcome contributions from the community. Please ensure your code adheres to our **Elite Engineering Standards**:

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes with semantic messages.
4.  Push to the branch.
5.  Open a Pull Request.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
