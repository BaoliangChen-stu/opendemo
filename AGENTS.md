# AGENTS.md

## Project

Single-file Python 3 CLI todo app. No dependencies, no build step.

## Commands

- Run: `python3 app.py <cmd>`
- Commands: `add <text>`, `list`, `done <id>`

## Key Facts

- Entry point: `app.py` (uses `if __name__ == "__main__"`)
- Data stored in `todos.json` (auto-created in same directory on first `add`)
- Python 3 stdlib only — no `pip install` needed
- No tests, lint, or CI configured yet
