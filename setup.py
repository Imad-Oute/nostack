#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
import time

# --- Configuration ---
REQUIRED_COMMANDS = ["docker", "git"]
ENV_EXAMPLE_FILE = ".env.example"
ENV_FILE = ".env"
OPENWEBUI_DIR = "services/openwebui-backend"
DEFAULT_OPENWEBUI_REPO = "https://github.com/open-webui/open-webui.git"

# --- Colors ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_step(msg):
    print(f"\n{Colors.BLUE}{Colors.BOLD}[STEP] {msg}{Colors.ENDC}")

def print_success(msg):
    print(f"{Colors.GREEN}✅ {msg}{Colors.ENDC}")

def print_warning(msg):
    print(f"{Colors.WARNING}⚠️  {msg}{Colors.ENDC}")

def print_error(msg):
    print(f"{Colors.FAIL}❌ {msg}{Colors.ENDC}")

def check_prerequisites():
    print_step("Checking Prerequisites")
    missing = []
    for cmd in REQUIRED_COMMANDS:
        if shutil.which(cmd) is None:
            missing.append(cmd)
    
    if missing:
        print_error(f"Missing required tools: {', '.join(missing)}")
        print("Please install them and try again.")
        sys.exit(1)
    
    # Check Docker Compose
    if subprocess.call(["docker", "compose", "version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        if subprocess.call(["docker-compose", "version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
             print_error("Docker Compose plugin not found.")
             sys.exit(1)

    print_success("All prerequisites met.")

def setup_env():
    print_step("Setting up Environment Variables")
    if not os.path.exists(ENV_FILE):
        if os.path.exists(ENV_EXAMPLE_FILE):
            shutil.copy(ENV_EXAMPLE_FILE, ENV_FILE)
            print_success(f"Created {ENV_FILE} from {ENV_EXAMPLE_FILE}")
            print_warning(f"Please review {ENV_FILE} and update secrets/URLs before running the stack.")
        else:
            print_error(f"{ENV_EXAMPLE_FILE} not found!")
            sys.exit(1)
    else:
        print_success(f"{ENV_FILE} already exists.")

    # Basic validation
    with open(ENV_FILE, 'r') as f:
        content = f.read()
        if "your-domain.ngrok-free.dev" in content:
            print_warning("It looks like you haven't configured your Ngrok domain in .env yet.")
            print_warning("n8n webhooks might not work correctly.")

def setup_openwebui():
    print_step("Setting up OpenWebUI")
    
    # Get repo URL from .env or default
    repo_url = DEFAULT_OPENWEBUI_REPO
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, 'r') as f:
            for line in f:
                if line.startswith("OPENWEBUI_REPO_URL="):
                    repo_url = line.strip().split("=", 1)[1]
                    break
    
    target_dir = os.path.abspath(OPENWEBUI_DIR)
    backend_dir = os.path.join(target_dir, "backend")

    if os.path.exists(backend_dir):
        print_success("OpenWebUI seems to be already set up.")
        return

    print(f"Cloning OpenWebUI from {repo_url}...")
    
    # Ensure directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    try:
        # Clone into a temporary directory first or directly if empty
        # We use '.' to clone into the existing directory
        subprocess.check_call(["git", "clone", repo_url, "."], cwd=target_dir)
        print_success("OpenWebUI cloned successfully.")
    except subprocess.CalledProcessError:
        print_error("Failed to clone OpenWebUI.")
        sys.exit(1)

def start_stack():
    print_step("Starting the Stack")
    print("This might take a while to download images and build containers...")
    
    cmd = "docker compose up -d"
    if subprocess.call(cmd, shell=True) == 0:
        print_success("Stack started successfully!")
    else:
        print_error("Failed to start the stack.")
        sys.exit(1)

def print_summary():
    print(f"\n{Colors.HEADER}{Colors.BOLD}🎉 NoStack Setup Complete!{Colors.ENDC}\n")
    
    services = [
        ("n8n", "http://localhost:5679", "Workflow Automation"),
        ("Flowise", "http://localhost:3002", "LLM App Builder"),
        ("Langflow", "http://localhost:7860", "Visual AI Framework"),
        ("OpenWebUI", "http://localhost:3005", "Chat Interface"),
        ("Redis Commander", "http://localhost:8081", "Redis GUI"),
        ("Qdrant Dashboard", "http://localhost:6334/dashboard", "Vector DB GUI"),
        ("Neo4j Browser", "http://localhost:7475", "Graph DB GUI (User: neo4j, Pass: password123)"),
    ]

    print(f"{'Service':<20} {'URL':<40} {'Description'}")
    print("-" * 80)
    for name, url, desc in services:
        print(f"{Colors.CYAN}{name:<20}{Colors.ENDC} {url:<40} {desc}")
    
    print(f"\n{Colors.BLUE}ℹ️  To stop the stack, run: docker compose down{Colors.ENDC}")

def main():
    print(f"{Colors.HEADER}{Colors.BOLD}🚀 Initializing NoStack Setup...{Colors.ENDC}")
    
    check_prerequisites()
    setup_env()
    setup_openwebui()
    start_stack()
    print_summary()

if __name__ == "__main__":
    main()
