#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
import time

def print_color(text, color="green"):
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    print(f"{colors.get(color, '')}{text}{colors['reset']}")

def check_command(command):
    return shutil.which(command) is not None

def run_command(command, shell=False):
    try:
        subprocess.check_call(command, shell=shell)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print_color("\n🚀 Starting AI Development Stack Setup...\n", "blue")

    # 1. Check Prerequisites
    print_color("Checking prerequisites...", "yellow")
    if not check_command("docker"):
        print_color("❌ Docker is not installed. Please install Docker first.", "red")
        sys.exit(1)
    
    # Check for docker compose (v2) or docker-compose (v1)
    docker_compose_cmd = "docker compose"
    if not run_command(["docker", "compose", "version"], shell=False):
        if check_command("docker-compose"):
            docker_compose_cmd = "docker-compose"
        else:
            print_color("❌ Docker Compose is not installed.", "red")
            sys.exit(1)
            
    print_color("✅ Prerequisites checked.", "green")

    # 2. Setup Environment Variables
    print_color("\nSetting up environment variables...", "yellow")
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            shutil.copy(".env.example", ".env")
            print_color("✅ Created .env from .env.example", "green")
        else:
            print_color("❌ .env.example not found!", "red")
            sys.exit(1)
    else:
        print_color("ℹ️  .env already exists, skipping creation.", "blue")

    # 3. Start Services
    print_color("\nStarting services (this may take a while)...", "yellow")
    if run_command(f"{docker_compose_cmd} up -d", shell=True):
        print_color("\n✅ Stack started successfully!", "green")
    else:
        print_color("\n❌ Failed to start stack.", "red")
        sys.exit(1)

    # 4. Display Info
    print_color("\n🎉 Setup Complete! Here are your services:\n", "green")
    
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
        print(f"{name:<20} {url:<40} {desc}")
    
    print_color("\nℹ️  To stop the stack, run: docker compose down", "blue")

if __name__ == "__main__":
    main()
