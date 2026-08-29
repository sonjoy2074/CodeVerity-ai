"""Scoring rubric for benchmark evaluation."""

from __future__ import annotations


def score_results(results: list[dict] | None = None):
    """Placeholder rubric implementation."""
    return {
        "precision": 0.0,
        "recall": 0.0,
        "f1": 0.0,
        "results": results or [],
    }
