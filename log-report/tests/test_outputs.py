import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    # read and parse the report the agent wrote
    assert REPORT.exists(), "No report generated"
    return json.loads(REPORT.read_text())


def test_report_is_valid_json_object():
    """criterion 1: a file exists at /app/report.json and contains a single valid json object."""
    assert REPORT.exists(), "no file found at /app/report.json"
    data = load_report()
    assert isinstance(data, dict), "report.json is not a single json object"
    expected_keys = {
        "total_requests",
        "unique_ips",
        "top_path",
    }

    assert set(data.keys()) == expected_keys, (
        f"Expected keys {expected_keys}, got {set(data.keys())}"
    )


def test_total_requests():
    """criterion 2: total_requests is an integer equal to the number of requests in the log."""
    data = load_report()
    assert isinstance(data.get("total_requests"), int), "total_requests is missing or not an integer"
    assert data["total_requests"] == 6, f"expected 6 requests, got {data['total_requests']}"


def test_unique_ips():
    """criterion 3: unique_ips is an integer equal to the number of distinct client ip addresses in the log."""
    data = load_report()
    assert isinstance(data.get("unique_ips"), int), "unique_ips is missing or not an integer"
    assert data["unique_ips"] == 3, f"expected 3 unique ips, got {data['unique_ips']}"


def test_top_path():
    """criterion 4: top_path is a string equal to the most frequently requested path in the log."""
    data = load_report()
    assert isinstance(data.get("top_path"), str), "top_path is missing or not a string"
    assert data["top_path"] == "/index.html", f"expected /index.html, got {data['top_path']}"