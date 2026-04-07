#!/usr/bin/env python3
"""A simple todo list CLI app."""

import json
import os
import sys

TODO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")


def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []


def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def add(text):
    todos = load_todos()
    todos.append({"id": len(todos) + 1, "text": text, "done": False})
    save_todos(todos)
    print(f"Added: {text}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos yet!")
        return
    for t in todos:
        status = "x" if t["done"] else " "
        print(f"[{status}] {t['id']}: {t['text']}")


def done(todo_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            save_todos(todos)
            print(f"Done: {t['text']}")
            return
    print(f"Todo #{todo_id} not found")


def usage():
    print("Usage:")
    print("  python3 app.py add <text>    Add a todo")
    print("  python3 app.py list          List all todos")
    print("  python3 app.py done <id>     Mark a todo as done")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "add":
        if len(sys.argv) < 3:
            print("Error: missing todo text")
            sys.exit(1)
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_todos()
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Error: missing todo id")
            sys.exit(1)
        done(int(sys.argv[2]))
    else:
        usage()
        sys.exit(1)
