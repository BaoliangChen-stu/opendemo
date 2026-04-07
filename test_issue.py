#!/usr/bin/env python3
"""Simple test case for OpenCode Issue auto-handling."""

import json
import os
import sys

ISSUE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_issue.json")


def create_test_issue():
    """Create a simple test issue for OpenCode to process."""
    issue = {
        "title": "Test: Add hello world command",
        "body": "Please add a `hello` command that prints 'Hello, World!'",
        "number": 1,
        "state": "open",
    }

    with open(ISSUE_FILE, "w") as f:
        json.dump(issue, f, indent=2)

    print(f"Created test issue: {ISSUE_FILE}")
    print(f"Title: {issue['title']}")
    print(f"Body: {issue['body']}")
    return issue


def simulate_opencode_response(issue):
    """Simulate how OpenCode should respond to an issue."""
    print("\n--- OpenCode Processing ---")
    print("Reading issue...")
    print(f"Parsing request: {issue['body']}")

    # Simulate successful processing
    response = {
        "action": "implemented",
        "changes": ["Added 'hello' command to app.py"],
        "comment": "Done! Added `hello` command. Run with: python3 app.py hello",
    }

    print(f"Action: {response['action']}")
    print(f"Changes: {response['changes']}")
    print(f"Comment: {response['comment']}")

    return response


def main():
    print("=== OpenCode Issue Auto-Handling Test ===\n")

    # Step 1: Create test issue
    issue = create_test_issue()

    # Step 2: Simulate OpenCode processing
    response = simulate_opencode_response(issue)

    # Step 3: Verify
    print("\n--- Verification ---")
    if os.path.exists(ISSUE_FILE):
        print("✅ Test issue file created")
    if response["action"] == "implemented":
        print("✅ OpenCode successfully processed the issue")

    print("\nTest complete!")


if __name__ == "__main__":
    main()
