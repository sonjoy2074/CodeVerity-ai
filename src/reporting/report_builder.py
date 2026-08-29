"""Build markdown and JSON reports from agent findings."""

from __future__ import annotations


def build_report(findings: list[dict] | None = None):
    """Return a minimal report structure."""
    return {
        "summary": "CodeVerity-AI evaluation report",
        "findings": findings or [],
        "generated": True,
    }
