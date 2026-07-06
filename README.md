# Workflow Permission Audit

<p align="center">
  <img src="assets/readme-cover.svg" alt="Workflow Permission Audit cover" width="100%" />
</p>

![stack](https://img.shields.io/badge/stack-Python-7c3aed?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-0891b2?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-b45309?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-be185d?style=flat-square)

Audit CI workflow snippets for broad permissions and risky triggers.

## The short version

`workflow-permission-audit` is intentionally small: feed it a file, get deterministic findings, and decide whether the result should block a merge or just guide cleanup.

## Rule surface

| Rule | Severity | What it catches |
| --- | --- | --- |
| `write-all` | high | workflow has broad write permissions |
| `pull-request-target` | medium | pull_request_target trigger detected |
| `secrets-available` | low | secrets may be available to workflow |

## Usage

```bash
python -m pip install -e ".[dev]"
workflow-permission-audit examples/sample.txt
workflow-permission-audit examples/sample.txt --json --fail-on medium
```

## Useful defaults

| Option | Reason |
| --- | --- |
| `--json` | machine-readable output for scripts |
| `--fail-on medium` | stricter CI gate when warnings matter |
| `--format auto` | let the reader detect text, CSV, JSON, or JSONL |

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m workflow_permission_audit --help
```
