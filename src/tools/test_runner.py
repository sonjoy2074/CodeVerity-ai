"""Sandboxed test execution runner for pytest and JUnit-style suites."""

from __future__ import annotations


def run_tests(repo_path: str, command: str = "pytest -q"):
    """Placeholder test execution helper."""
    return {
        "repo_path": repo_path,
        "command": command,
        "results": {
            "passed": 0,
            "failed": 0,
            "skipped": 0,
        },
    }
