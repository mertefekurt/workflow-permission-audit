import csv
import json

from workflow_permission_audit.cli import main
from workflow_permission_audit.core import audit_records, read_records, render_json, should_fail
from workflow_permission_audit.rules import SAMPLE_CLEAN, SAMPLE_RISK


def test_detects_risky_sample() -> None:
    report = audit_records([{"id": "case-1", "text": SAMPLE_RISK}])

    assert report.findings
    assert any(finding.severity == "high" for finding in report.findings)
    assert report.risk_level in {"medium", "high"}


def test_clean_sample_has_no_findings() -> None:
    report = audit_records([{"id": "clean", "text": SAMPLE_CLEAN}])

    assert report.findings == ()
    assert report.score == 0


def test_json_report_is_machine_readable() -> None:
    report = audit_records([{"id": "case-2", "text": SAMPLE_RISK}])
    payload = json.loads(render_json(report))

    assert payload["records_scanned"] == 1
    assert payload["findings"][0]["severity"] == "high"


def test_csv_reader_preserves_text(tmp_path) -> None:
    path = tmp_path / "input.csv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "text"])
        writer.writeheader()
        writer.writerow({"id": "row-1", "text": SAMPLE_RISK})

    records = read_records(path)

    assert records[0]["id"] == "row-1"
    assert SAMPLE_RISK in records[0]["text"]


def test_fail_threshold() -> None:
    report = audit_records([{"id": "case-3", "text": SAMPLE_RISK}])

    assert should_fail(report, "high")


def test_cli_json_exit_code(tmp_path, capsys) -> None:
    path = tmp_path / "input.txt"
    path.write_text(SAMPLE_RISK, encoding="utf-8")

    exit_code = main([str(path), "--json", "--fail-on", "high"])

    captured = capsys.readouterr()
    assert exit_code == 2
    assert json.loads(captured.out)["findings"][0]["severity"] == "high"
