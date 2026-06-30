from __future__ import annotations

from workflow_permission_audit.models import Rule

PROJECT_NAME = 'workflow-permission-audit'
SUMMARY = 'Audit CI workflow snippets for broad permissions and risky triggers.'
SAMPLE_RISK = 'permissions write-all pull_request_target secrets available'
SAMPLE_CLEAN = 'permissions contents:read pull_request secrets none'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='write-all',
        severity='high',
        pattern='\\bwrite-all\\b|permissions\\s*:\\s*write',
        message='workflow has broad write permissions',
        recommendation='Use least-privilege permissions per job.',
    ),
    Rule(
        code='pull-request-target',
        severity='medium',
        pattern='\\bpull_request_target\\b',
        message='pull_request_target trigger detected',
        recommendation='Review untrusted code execution paths.',
    ),
    Rule(
        code='secrets-available',
        severity='low',
        pattern='\\bsecrets available\\b|secrets\\s*:\\s*inherit',
        message='secrets may be available to workflow',
        recommendation='Restrict secrets to trusted branches and jobs.',
    ),
)
