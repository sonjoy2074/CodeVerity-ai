"""Coordinator for the multi-agent repository evaluation workflow."""

from __future__ import annotations

from ..agents.ast_quality_agent import ASTQualityAgent
from ..agents.security_agent import SecurityAgent
from ..agents.srs_compliance_agent import SRSComplianceAgent
from ..agents.verification_agent import VerificationAgent
from .state import WorkflowState


class Workflow:
    def __init__(self, repo_path: str, srs_path: str | None = None):
        self.state = WorkflowState(repo_path=repo_path, srs_path=srs_path)
        self.agents = {
            "quality": ASTQualityAgent(),
            "security": SecurityAgent(),
            "srs": SRSComplianceAgent(),
            "verification": VerificationAgent(),
        }

    def run(self):
        self.state.record("workflow_start")
        quality_result = self.agents["quality"].run(self.state.repo_path)
        security_result = self.agents["security"].run(self.state.repo_path)
        srs_result = self.agents["srs"].run(self.state.repo_path, self.state.srs_path)
        verification_result = self.agents["verification"].run(
            findings=quality_result.get("findings", []) + security_result.get("findings", [])
        )

        self.state.findings = verification_result.get("validated_findings", [])
        self.state.metrics = {
            "quality": quality_result,
            "security": security_result,
            "srs": srs_result,
            "verification": verification_result,
        }
        self.state.record("workflow_end", findings=len(self.state.findings))
        return self.state
