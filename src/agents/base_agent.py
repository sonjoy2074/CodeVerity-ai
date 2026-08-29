"""Base class for all analysis agents."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class BaseAgent:
    """Minimal reusable agent interface with logging and trajectory support."""

    name: str
    config: dict[str, Any] = field(default_factory=dict)
    trajectory: list[dict[str, Any]] = field(default_factory=list)

    def log(self, event: str, **details: Any) -> None:
        self.trajectory.append({"event": event, **details})

    def run(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        self.log("run", args=args, kwargs=kwargs)
        return {"agent": self.name, "status": "ok"}
