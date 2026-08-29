"""Shared workflow state and trajectory tracking."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowState:
    """Mutable evaluation context reused by the multi-agent workflow."""

    repo_path: str | None = None
    srs_path: str | None = None
    findings: list[dict[str, Any]] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)
    trajectory: list[dict[str, Any]] = field(default_factory=list)

    def record(self, event: str, **details: Any) -> None:
        self.trajectory.append({"event": event, **details})
