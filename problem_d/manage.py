#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

try:
    from consolemenu import ConsoleMenu
    from consolemenu.items import FunctionItem
except ImportError:
    print("Missing dependency: consolemenu")
    print("Install with: pip install console-menu")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
DB_DIR = ROOT / "problem_d_database"
BACKEND_DIR = ROOT / "problem_d_backend"
FRONTEND_DIR = ROOT / "problem_d_frontend"


def run(cmd, cwd=None):
    subprocess.run(cmd, cwd=cwd, check=True)


def seed_db():
    seed_script = DB_DIR / "seed.sh"
    if not seed_script.exists():
        print("seed.sh not found in problem_d_database")
        return
    run([str(seed_script)], cwd=DB_DIR)


def start_backend():
    try:
        run(["npm", "ci"], cwd=BACKEND_DIR)
    except subprocess.CalledProcessError:
        print("npm ci failed, falling back to npm install (backend).")
        run(["npm", "install"], cwd=BACKEND_DIR)
    run(["npm", "run", "start:dev"], cwd=BACKEND_DIR)


def start_frontend():
    try:
        run(["npm", "ci"], cwd=FRONTEND_DIR)
    except subprocess.CalledProcessError:
        print("npm ci failed, falling back to npm install (frontend).")
        run(["npm", "install"], cwd=FRONTEND_DIR)
    run(["npm", "run", "dev"], cwd=FRONTEND_DIR)


def show_paths():
    print(f"Root: {ROOT}")
    print(f"Database: {DB_DIR}")
    print(f"Backend: {BACKEND_DIR}")
    print(f"Frontend: {FRONTEND_DIR}")


def main():
    menu = ConsoleMenu("Problem D Control Panel", "Seed DB and launch services")

    menu.append_item(FunctionItem("Seed SQLite database", seed_db))
    menu.append_item(FunctionItem("Start backend (NestJS)", start_backend))
    menu.append_item(FunctionItem("Start frontend (Vite)", start_frontend))
    menu.append_item(FunctionItem("Show project paths", show_paths))

    menu.show()


if __name__ == "__main__":
    main()
