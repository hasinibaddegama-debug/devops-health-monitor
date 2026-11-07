from unittest.mock import patch
import requests
from monitor import (
    classify_health,
    calculate_summary,
    check_application
)

def test_healthy_application():
    result = classify_health(200, 500, 2000)
    assert result == "HEALTHY"


def test_slow_application():
    result = classify_health(200, 2500, 2000)
    assert result == "SLOW"


def test_unhealthy_application():
    result = classify_health(500, 300, 2000)
    assert result == "UNHEALTHY"


def test_summary():
    results = [
        {"health": "HEALTHY"},
        {"health": "HEALTHY"},
        {"health": "DOWN"}
    ]

    summary = calculate_summary(results)

    assert summary["total"] == 3
    assert summary["healthy"] == 2
    assert summary["slow"] == 0
    assert summary["unhealthy"] == 0
    assert summary["down"] == 1


def test_http_500_response():
    application = {
        "name": "Test Service",
        "url": "https://example.com"
    }

    with patch("monitor.requests.get") as mock_get:
        mock_get.return_value.status_code = 500

        result = check_application(application, 5, 2000)

    assert result["health"] == "UNHEALTHY"
    assert result["http_status"] == 500


def test_connection_failure():
    application = {
        "name": "Test Service",
        "url": "https://example.com"
    }

    with patch("monitor.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.ConnectionError(
            "Connection refused"
        )

        result = check_application(application, 5, 2000)

    assert result["health"] == "DOWN"
    assert result["http_status"] is None
    assert "Connection refused" in result["error"]


def test_request_timeout():
    application = {
        "name": "Test Service",
        "url": "https://example.com"
    }

    with patch("monitor.requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout(
            "Request timed out"
        )

        result = check_application(application, 5, 2000)

    assert result["health"] == "DOWN"
    assert result["http_status"] is None
    assert "Request timed out" in result["error"]
