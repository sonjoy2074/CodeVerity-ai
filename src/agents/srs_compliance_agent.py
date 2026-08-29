"""SRS compliance detection agent."""

from __future__ import annotations

from .base_agent import BaseAgent


class SRSComplianceAgent(BaseAgent):
    def __init__(self, config: dict | None = None):
        super().__init__(name="srs_compliance_agent", config=config or {})

    def run(self, repo_path: str, srs_path: str | None = None):
        self.log("check_compliance", repo_path=repo_path, srs_path=srs_path)
        return {
            "agent": self.name,
            "status": "ok",
            "coverage": 0.0,
            "requirements": [],
        }
