# DevOps Health Monitor

A lightweight Python-based application that monitors the availability and response times of multiple websites or services, classifies their health status, and generates a structured JSON report.

## 1. Project Overview

The DevOps Health Monitor is a command-line application designed to help identify unavailable or slow web services.

The application reads a list of services from a JSON configuration file, sends HTTP requests to each service, measures response times and determines their health status.

It displays the results in the terminal and generates a JSON report for further analysis.

### Why I Built This

Service availability and performance monitoring are important aspects of DevOps and production support.

I chose this project because I wanted to explore monitoring and automation while developing my Python skills.

I also wanted to gain practical experience with automated testing, Docker containerisation and Continuous Integration using GitHub Actions.

Rather than building a large application, I focused on creating a small, maintainable solution that I could understand, test and improve.

## 2. Features

- Monitor multiple websites and HTTP services.
- Configure monitored services using a JSON file.
- Measure HTTP response times in milliseconds.
- Classify services as HEALTHY, SLOW, UNHEALTHY or DOWN.
- Handle connection failures and request timeouts.
- Display individual monitoring results in the terminal.
- Generate a summary of application health.
- Save monitoring results to a JSON report with a UTC timestamp.
- Run automated tests using Pytest.
- Package and run the application using Docker.
- Automatically execute tests through GitHub Actions.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Application development |
| Requests | HTTP requests |
| JSON | Configuration and report generation |
| Pytest | Automated testing |
| unittest.mock | Simulating HTTP responses and failures |
| Docker | Application containerisation |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | Continuous Integration |

The application also uses Python standard libraries including `time`, `datetime` and `pathlib`.

## 4. Project Structure

```text
devops-health-monitor/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── tests/
│   └── test_monitor.py
├── reports/
│   └── health_report.json
├── .dockerignore
├── .gitignore
├── AI.md
├── Dockerfile
├── README.md
├── RESEARCH.md
├── config.json
├── monitor.py
└── requirements.txt
```

The `reports/` directory is generated locally and excluded from Git.

## 5. Prerequisites

To run the application locally, you need:

- Python 3.13 or a compatible Python 3 version.
- pip, the Python package installer.
- Git to clone the repository.
- An internet connection to monitor external websites.

Docker Desktop or another compatible Docker installation is required only for container execution.

## 6. Installation and Local Setup

### Step 1 — Clone the repository

```bash
git clone https://github.com/hasinibaddegama-debug/devops-health-monitor.git
cd devops-health-monitor
```

### Step 2 — Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

### Step 3 — Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4 — Run the application

```bash
python monitor.py
```

The application reads `config.json`, checks each configured service and displays the monitoring results.

## 7. Configuration

The application uses `config.json` to define which services to monitor and the timeout and response-time thresholds.

Example configuration:

```json
{
  "applications": [
    {
      "name": "Example Website",
      "url": "https://example.com"
    },
    {
      "name": "Python Website",
      "url": "https://www.python.org"
    },
    {
      "name": "Unavailable Test Service",
      "url": "http://127.0.0.1:9999"
    }
  ],
  "timeout_seconds": 5,
  "slow_threshold_ms": 2000
}
```

### Configuration Fields

| Field | Description |
|---|---|
| `applications` | List of services to monitor |
| `name` | Display name of the service |
| `url` | HTTP or HTTPS endpoint |
| `timeout_seconds` | Maximum time allowed for an HTTP request |
| `slow_threshold_ms` | Response-time threshold for identifying slow services |

You can add or remove applications without changing the Python source code.

The unavailable test service is intentionally configured to demonstrate connection failure handling.

## 8. How the Application Works

The monitoring process follows these steps:

1. Read the application configuration from `config.json`.
2. Loop through the configured services.
3. Send an HTTP GET request to each URL.
4. Measure the request duration using `time.perf_counter()`.
5. Classify the response according to its HTTP status and response time.
6. Catch network exceptions and record error details.
7. Calculate the overall monitoring summary.
8. Display the results in the terminal.
9. Generate a JSON report with a UTC timestamp.

### Health Classification

| Health Status | Condition |
|---|---|
| HEALTHY | HTTP 2xx response within the configured threshold |
| SLOW | HTTP 2xx response exceeding the configured threshold |
| UNHEALTHY | HTTP response outside the 2xx range |
| DOWN | Connection failure, timeout or another request exception |

### Example Terminal Output

```text
Checking: Example Website
HTTP Status: 200
Response Time: 105.74 ms
Health: HEALTHY

Checking: Python Website
HTTP Status: 200
Response Time: 112.82 ms
Health: HEALTHY

Checking: Unavailable Test Service
Health: DOWN
Error: Connection refused

===== HEALTH MONITORING SUMMARY =====
Total Applications: 3
Healthy: 2
Slow: 0
Unhealthy: 0
Down: 1

Report saved to: reports/health_report.json
```

Actual response times and health classifications depend on the network and service availability.

## 9. JSON Report Generation

After completing the checks, the application generates:

`reports/health_report.json`

Example report structure:

```json
{
  "timestamp": "2026-11-09T12:00:00+00:00",
  "summary": {
    "total": 3,
    "healthy": 2,
    "slow": 0,
    "unhealthy": 0,
    "down": 1
  },
  "applications": [
    {
      "name": "Example Website",
      "url": "https://example.com",
      "http_status": 200,
      "response_time_ms": 105.74,
      "health": "HEALTHY",
      "error": null
    }
  ]
}
```

The example shows one application entry for brevity. Actual reports contain an entry for every configured application.

The report includes a timestamp, overall health summary and individual service results.

The current implementation overwrites the previous report each time it runs.

## 10. Automated Testing with Pytest

The project uses Pytest to verify application behaviour.

Run the tests using:

```bash
python -m pytest -v
```

### Implemented Tests

| Test | Purpose |
|---|---|
| `test_healthy_application` | Verify HEALTHY classification |
| `test_slow_application` | Verify SLOW classification |
| `test_unhealthy_application` | Verify UNHEALTHY classification |
| `test_summary` | Verify health summary calculations |
| `test_http_500_response` | Verify HTTP 500 handling |
| `test_connection_failure` | Verify connection failure handling |
| `test_request_timeout` | Verify request timeout handling |

The tests use `unittest.mock.patch()` to simulate HTTP responses and network errors without depending on live external services.

### Verified Test Results

**Local environment:**

- Seven tests passed.
- No failures.
- Execution time: 0.42 seconds.

**GitHub Actions environment:**

- Seven tests passed.
- No failures.
- Execution time: 0.59 seconds.
- Python 3.13.18 on Linux.

## 11. Running with Docker

Docker allows the application to run in a packaged environment containing Python and its dependencies.

### Build the Docker image

From the project root:

```bash
docker build -t devops-health-monitor .
```

### Run the container

```bash
docker run --rm devops-health-monitor
```

The container runs the Health Monitor, displays the results and exits when monitoring finishes.

The `--rm` option removes the container after execution.

### Preserve the JSON report using a bind mount

First, create the reports directory.

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path reports
```

Run the container with a bind mount:

```powershell
docker run --rm --mount "type=bind,source=$((Get-Location).Path)\reports,target=/app/reports" devops-health-monitor
```

The generated report will be saved in the local `reports` directory.

### Docker Verification

I successfully built the Docker image and ran the application inside a Linux container.

The application monitored three configured services and produced the expected health summary.

I also tested a bind mount to connect the container's reports directory with the host filesystem.

## 12. Continuous Integration with GitHub Actions

The project uses GitHub Actions to automate testing.

Workflow file:

`.github/workflows/python-tests.yml`

### Workflow Triggers

The workflow is configured to run when:

- Changes are pushed to the repository.
- Pull requests are opened or updated.

### Workflow Steps

1. Check out the repository.
2. Set up Python 3.13.
3. Install the required dependencies.
4. Execute the automated Pytest tests.
5. Report the workflow result.

### Verified CI Results

The GitHub Actions workflow executed successfully after a push to the main branch.

All seven tests passed on a GitHub-hosted Linux runner.

This provides automated feedback when changes are pushed and helps detect regressions.

The workflow performs Continuous Integration only; it does not deploy the application.

## 13. Research and AI Usage

### Research Documentation

My learning process, technical decisions, problems and solutions are documented in:

`RESEARCH.md`

Topics include:

- Python fundamentals and environment setup.
- HTTP monitoring and response-time measurement.
- JSON configuration and report generation.
- Python functions and refactoring.
- Automated testing with Pytest.
- Docker containerisation.
- GitHub Actions Continuous Integration.

### AI Usage

I used ChatGPT as a learning and development assistant.

AI assistance is documented in:

`AI.md`

This explains which concepts I explored using AI, how I reviewed suggestions and how I verified the implementation through local testing, Docker execution and GitHub Actions.

## 14. Challenges Encountered

### Python Environment Setup

Initially, the application could not import the Requests library because the correct Python virtual environment was not being used.

I activated the virtual environment and verified that the required dependency was installed.

### Docker Engine Connectivity

The Docker CLI was installed, but the Docker Engine was initially unavailable.

I investigated the error, started Docker Desktop and successfully built the image.

### GitHub Actions Workflow Discovery

My GitHub Actions workflow did not initially appear in the Actions tab.

I discovered that the workflow file had been placed in the wrong directory.

After moving it into `.github/workflows/` and pushing the correction, GitHub successfully executed the CI workflow.

These problems helped me develop practical troubleshooting skills.

## 15. Current Limitations

The current application has several limitations:

- Monitoring runs once per execution rather than continuously.
- HTTP requests are performed sequentially.
- Only HTTP GET checks are supported.
- A successful HTTP response does not necessarily mean the application is fully functional.
- The JSON report is overwritten on each run.
- No automatic email or messaging alerts are implemented.
- Configuration validation is limited.
- Automated tests do not yet cover every possible scenario.
- The CI workflow runs tests but does not deploy the application.

These limitations were intentionally kept within the scope of a small technical challenge project.

## 16. Future Improvements

With more time, I would consider:

1. **Scheduled monitoring:** Run checks automatically at configurable intervals.
2. **Alerting:** Send notifications when services become unhealthy or unavailable.
3. **Historical reports:** Store timestamped reports to analyse availability and performance trends.
4. **Configuration validation:** Validate URLs, timeout values and required configuration fields.
5. **Additional testing:** Improve test coverage for configuration handling and report generation.
6. **Parallel monitoring:** Check multiple services concurrently to reduce total execution time.
7. **Docker improvements:** Explore image security, non-root execution and dependency optimisation.
8. **CI/CD enhancements:** Automatically build Docker images and investigate deployment automation.

I would prioritise configuration validation, historical reporting and automated scheduling before introducing more complex features.

## 17. Conclusion

This project provided an opportunity to explore Python development and DevOps practices through a practical monitoring application.

I learned how to build a configurable command-line tool, handle HTTP failures, write automated tests, containerise an application using Docker and configure Continuous Integration using GitHub Actions.

The main focus was not application complexity, but understanding the technologies, making sensible engineering decisions, documenting my research and verifying that the solution worked correctly.

The project demonstrates my approach to learning unfamiliar technologies, troubleshooting problems and improving software incrementally.