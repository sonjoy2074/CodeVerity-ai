"""Health score and SRS coverage calculator."""

from __future__ import annotations


def compute_score(metrics: dict | None = None):
    """Simple placeholder scoring function."""
    metrics = metrics or {}
    return {
        "overall_score": 0.0,
        "coverage": 0.0,
        "metrics": metrics,
    }
