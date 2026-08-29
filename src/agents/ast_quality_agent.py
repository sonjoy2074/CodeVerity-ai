"""AST-based code quality analysis agent."""

from __future__ import annotations

from .base_agent import BaseAgent


class ASTQualityAgent(BaseAgent):
    def __init__(self, config: dict | None = None):
        super().__init__(name="ast_quality_agent", config=config or {})

    def run(self, repo_path: str):
        self.log("analyze_repo", repo_path=repo_path)
        return {
            "agent": self.name,
            "status": "ok",
            "findings": [],
            "score": 0.0,
        }
