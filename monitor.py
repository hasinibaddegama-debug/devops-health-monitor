
import json
import time
import requests
from datetime import datetime, timezone
from pathlib import Path

# Read application settings from config.json
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)


applications = config["applications"]
timeout = config["timeout_seconds"]
slow_threshold = config["slow_threshold_ms"]
results = []

# Check each application

for application in applications:

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

        if 200 <= response.status_code < 300:
            if response_time > slow_threshold:
                health = "SLOW"
            else:
                health = "HEALTHY"
        else:
            health = "UNHEALTHY"

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

    results.append(result)


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


print("\n===== HEALTH MONITORING SUMMARY =====")
print(f"Total Applications: {summary['total']}")
print(f"Healthy: {summary['healthy']}")
print(f"Slow: {summary['slow']}")
print(f"Unhealthy: {summary['unhealthy']}")
print(f"Down: {summary['down']}")


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
