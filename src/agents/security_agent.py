"""Security scanning agent."""

from __future__ import annotations

from .base_agent import BaseAgent


class SecurityAgent(BaseAgent):
    def __init__(self, config: dict | None = None):
        super().__init__(name="security_agent", config=config or {})

    def run(self, repo_path: str):
        self.log("scan_repo", repo_path=repo_path)
        return {
            "agent": self.name,
            "status": "ok",
            "findings": [],
            "severity_counts": {"critical": 0, "high": 0, "medium": 0, "low": 0},
        }
