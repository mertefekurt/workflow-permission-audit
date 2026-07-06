# Workflow Permission Audit

| | |
| --- | --- |
| Focus | GitHub Actions |
| Command | `workflow-permission-audit` |
| Inputs | text, JSON, JSONL, or CSV |
| Output | Markdown or JSON |

![Workflow Permission Audit cover](assets/readme-cover.svg)

Audit CI workflow snippets for broad permissions and risky triggers. The idea is simple: give Workflow Permission Audit the local file or fixture, get a readable result, and decide what needs attention before the next handoff.

## Policy surface

| Rule | Level | Why it matters |
| --- | --- | --- |
| `write-all` | high | workflow has broad write permissions |
| `pull-request-target` | medium | pull_request_target trigger detected |
| `secrets-available` | low | secrets may be available to workflow |

## Local run

```bash
git clone https://github.com/mertefekurt/workflow-permission-audit.git
cd workflow-permission-audit
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
workflow-permission-audit examples/sample.txt
workflow-permission-audit examples/sample.txt --json
```

## Why the sample fails

`permissions write-all pull_request_target secrets available` is intentionally shaped to hit the rules above, so it is useful as a quick smoke test after edits.
