
from monitor import classify_health


def test_healthy_application():
    result = classify_health(200, 500, 2000)
    assert result == "HEALTHY"


def test_slow_application():
    result = classify_health(200, 2500, 2000)
    assert result == "SLOW"


def test_unhealthy_application():
    result = classify_health(500, 300, 2000)
    assert result == "UNHEALTHY"
