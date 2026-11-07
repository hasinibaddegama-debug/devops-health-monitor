
import json
import time
import requests

from datetime import datetime, timezone
from pathlib import Path


# Classify application health
def classify_health(status_code, response_time, threshold):
    if 200 <= status_code < 300:
        if response_time > threshold:
            return "SLOW"
        return "HEALTHY"

    return "UNHEALTHY"


# Check a single application
def check_application(application, timeout, slow_threshold):
    name = application["name"]
    url = application["url"]

    print(f"\nChecking: {name}")

    result = {
        "name": name,
        "url": url,
        "http_status": None,
        "response_time_ms": None,
        "health": "DOWN",
        "error": None
    }

    try:
        start_time = time.perf_counter()

        response = requests.get(url, timeout=timeout)

        elapsed_time = time.perf_counter() - start_time
        response_time = round(elapsed_time * 1000, 2)

        health = classify_health(
            response.status_code,
            response_time,
            slow_threshold
        )

        result["http_status"] = response.status_code
        result["response_time_ms"] = response_time
        result["health"] = health

        print(f"HTTP Status: {response.status_code}")
        print(f"Response Time: {response_time} ms")
        print(f"Health: {health}")

    except requests.exceptions.RequestException as error:
        result["error"] = str(error)

        print("Health: DOWN")
        print(f"Error: {error}")

    return result


# Calculate monitoring summary
def calculate_summary(results):
    summary = {
        "total": len(results),
        "healthy": 0,
        "slow": 0,
        "unhealthy": 0,
        "down": 0
    }

    for result in results:
        status = result["health"].lower()
        summary[status] += 1

    return summary


# Save the JSON report
def save_report(results, summary):
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "summary": summary,
        "applications": results
    }

    report_directory = Path("reports")
    report_directory.mkdir(exist_ok=True)

    report_path = report_directory / "health_report.json"

    with open(report_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"\nReport saved to: {report_path}")


# Main application entry point
def main():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)

    applications = config["applications"]
    timeout = config["timeout_seconds"]
    slow_threshold = config["slow_threshold_ms"]

    results = []

    for application in applications:
        result = check_application(
            application,
            timeout,
            slow_threshold
        )
        results.append(result)

    summary = calculate_summary(results)

    print("\n===== HEALTH MONITORING SUMMARY =====")
    print(f"Total Applications: {summary['total']}")
    print(f"Healthy: {summary['healthy']}")
    print(f"Slow: {summary['slow']}")
    print(f"Unhealthy: {summary['unhealthy']}")
    print(f"Down: {summary['down']}")

    save_report(results, summary)


if __name__ == "__main__":
    main()
