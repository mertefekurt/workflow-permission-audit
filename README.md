# workflow-permission-audit

**Risk Register.** Audit CI workflow snippets for broad permissions and risky triggers.

## Risk

CI permissions are production credentials. This CLI checks workflow snippets for broad token access and unsafe triggers.

## Detection

`workflow-permission-audit` accepts CI workflow YAML or review text in text, JSON, JSONL, or CSV form.

## Mitigation

```bash
python -m pip install -e ".[dev]"
workflow-permission-audit examples/sample.txt
workflow-permission-audit examples/sample.txt --json --fail-on medium
```

## Automation

| Rule | Severity | Meaning |
|---|---:|---|
| `write-all` | high | workflow has broad write permissions |
| `pull-request-target` | medium | pull_request_target trigger detected |
| `secrets-available` | low | secrets may be available to workflow |

## Status

```bash
ruff check .
pytest
python -m workflow_permission_audit --help
```

License: MIT

### Example Input

```text
permissions write-all pull_request_target secrets available
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the workflow-permission-audit policy surface explicit.
