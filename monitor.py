
import json
import time
import requests


# Read application settings from config.json
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)


applications = config["applications"]
timeout = config["timeout_seconds"]
slow_threshold = config["slow_threshold_ms"]


# Check each application
for application in applications:

    name = application["name"]
    url = application["url"]

    print(f"\nChecking: {name}")

    try:
        start_time = time.perf_counter()

        response = requests.get(url, timeout=timeout)

        end_time = time.perf_counter()

        response_time = (end_time - start_time) * 1000

        if 200 <= response.status_code < 300:
            if response_time > slow_threshold:
                health = "SLOW"
            else:
                health = "HEALTHY"
        else:
            health = "UNHEALTHY"

        print(f"HTTP Status: {response.status_code}")
        print(f"Response Time: {response_time:.2f} ms")
        print(f"Health: {health}")

    except requests.exceptions.RequestException as error:
        print("Health: DOWN")
        print(f"Error: {error}")
