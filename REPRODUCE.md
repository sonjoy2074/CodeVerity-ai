# Reproduction Guide

This document explains how to run the CodeVerity-AI evaluation pipeline in a sandboxed environment.

## Prerequisites

- Docker and Docker Compose
- Python 3.11+
- Network access for package installation

## Quickstart

```bash
docker compose up --build
```

## Local MCP server

```bash
python -m src.server
```

## Evaluation

```bash
python eval/run_eval.py
```

## Notes

- Use the generated MCP configuration in `config/mcp_config.json` for Claude Desktop or Cursor.
- Benchmark repositories live under `data/test_repos/`.
- Execution artifacts are stored under `trajectories/`.
