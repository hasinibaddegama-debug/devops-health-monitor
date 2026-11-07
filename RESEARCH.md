# Research Log — DevOps Health Monitor

## Phase 1 — Setup the environment and Writing the 1st phase of Application

### 1. Project Overview

I decided to develop a Python-based Application Health Monitor that checks the availability and response times of web applications.

The main purpose is to help developers and DevOps engineers identify applications that are healthy, responding slowly, or unavailable.

I chose Python because I wanted to learn a new programming language and explore its use in DevOps automation.

### 2. Learning Python and Setting Up the Environment

**What I needed to learn:**
- How to create and run a Python application.
- How to create and activate a Python virtual environment.
- How to install external libraries using pip.
- How to manage dependencies using `requirements.txt`.

**Problem encountered:**

Initially, I accidentally created `monitor.py` and other project files inside the `.venv` directory.

When I tried to run the application, Python could not find `monitor.py`.

**Solution:**

I moved the application files into the main project directory and kept only the virtual environment files inside `.venv`.

I also encountered the following error:

`ModuleNotFoundError: No module named 'requests'`

I discovered that the `requests` library was available in my virtual environment, but I had not activated that environment before running the application.

I activated the virtual environment and successfully ran the program.

**What I learned:**

- Virtual environments isolate Python dependencies between projects.
- The Python interpreter and installed packages must belong to the same environment.
- Project source files should be kept separate from virtual environment files.
- `requirements.txt` helps other developers install the required dependencies.

### 3. Learning JSON Configuration

**What I needed to learn:**

How to store application configuration separately from Python code.

**Approach:**

I created a `config.json` file containing application names, URLs, timeout settings and a response-time threshold.

I used Python's built-in `json` module to read this configuration.

**Why I chose JSON:**

JSON is human-readable and widely used for application configuration.

Separating configuration from code allows application URLs and monitoring settings to be changed without modifying the monitoring logic.

**What I learned:**

- JSON stores structured data using objects and arrays.
- `json.load()` converts JSON content into Python objects.
- Python dictionaries can represent JSON objects.
- Python lists can represent JSON arrays.

### 4. Learning HTTP Monitoring

**What I needed to learn:**

How to check whether a web application is responding.

**Approach:**

I used the Python `requests` library to send HTTP GET requests to configured application URLs.

I checked the HTTP response status code to determine whether a request was successful.

**Current classification:**

- HTTP 2xx: Successful response.
- HTTP non-2xx: Unhealthy response.
- Connection failure or timeout: Down.

**What I learned:**

An HTTP response code provides information about the result of a request.

However, receiving an HTTP 200 response does not necessarily mean every part of an application is functioning correctly. A dedicated health endpoint can provide more meaningful information.

### 5. Learning Response-Time Measurement

**What I needed to learn:**

How to measure the time an application takes to respond.

**Approach:**

I used Python's `time.perf_counter()` before and after sending an HTTP request.

I calculated the elapsed time and converted it into milliseconds.

**Example results from my testing:**

| Application | Response Time | Health |
|---|---|---|
| Example Website | 478.91 ms | HEALTHY |
| Python Website | 506.81 ms | HEALTHY |

I configured a response-time threshold of 2,000 milliseconds to identify slow responses.

**What I learned:**

- `time.perf_counter()` is suitable for measuring elapsed time.
- Multiplying elapsed seconds by 1,000 converts the value into milliseconds.
- Response times can vary depending on network conditions and server performance.

### 6. Learning Error Handling

**What I needed to learn:**

How to prevent the monitoring application from crashing when a website is unavailable.

**Approach:**

I used Python's `try / except` mechanism to catch errors raised by the `requests` library.

**Testing:**

I configured a test URL:

`http://127.0.0.1:9999`

The connection was refused because no service was listening on that port.

The application correctly displayed:

`Health: DOWN`

It also printed the connection error without crashing.

**What I learned:**

- `try / except` is similar to `try / catch` in Java.
- Network requests can fail even when the Python code is correct.
- Error handling is important for reliable automation.
- One unavailable application should not prevent the monitoring of other applications.

### 7. Research Resources

Resources used or to be reviewed and verified:

- Python documentation: https://docs.python.org/3/
- Python virtual environments: https://docs.python.org/3/library/venv.html
- Requests documentation: https://requests.readthedocs.io/en/latest/
- Python JSON documentation: https://docs.python.org/3/library/json.html
- Python time documentation: https://docs.python.org/3/library/time.html

I also used ChatGPT to help explain unfamiliar Python concepts and troubleshoot errors. I verified the code by running it locally and observing the output.

### 8. Next Steps

- Generate a structured JSON health report.
- Improve error handling and configuration validation.
- Add automated tests using pytest.
- Explore Docker and GitHub Actions for DevOps automation.

## Phase 2 — JSON Report Generation and Data Handling

**Date:** 7 November 2026

### 1. Problem I Wanted to Solve

In the previous implementation, my Python Health Monitor checked multiple applications and displayed their HTTP status codes, response times and health conditions in the terminal.

However, the monitoring results were not saved, making it difficult to review them later.

I decided to extend the application to collect monitoring results, calculate a summary and generate a structured JSON report.

### 2. What I Needed to Learn

During this phase, I explored the following Python concepts:

- Lists and dictionaries for storing structured data.
- Iterating through collections and calculating summary statistics.
- Generating JSON files using the built-in `json` module.
- Recording timestamps using the `datetime` module.
- Creating directories and managing file paths using `pathlib`.

### 3. Python Lists and Dictionaries

I learned that a Python list can store multiple values, while a dictionary stores information using key-value pairs.

I used a list called `results` to collect the monitoring results for each application.

Each result was stored as a dictionary containing the application name, URL, HTTP status code, response time, health status and error details.

I used `results.append(result)` to add each application's result to the list.

Since I already have experience with Java, I found it helpful to compare Python lists with Java's `ArrayList` and Python dictionaries with Java's `Map`.

**What I learned:** Lists and dictionaries provide a simple way to organise structured information without creating separate classes for every data structure.

### 4. Generating JSON Reports

I used Python's built-in `json` module to convert the collected monitoring results into a JSON report.

The report contains:

- A UTC timestamp.
- A summary of application health statuses.
- Individual application monitoring results.
- Error information for unavailable services.

I used `json.dump(report, file, indent=4)` to write the report into `health_report.json`.

**Why I chose JSON:** JSON is lightweight, human-readable and widely supported. It can also be processed by other applications and automation tools.

### 5. Learning About Timestamps

I used `datetime.now(timezone.utc).isoformat()` to record the time when the monitoring report was generated.

I learned that UTC timestamps are useful in monitoring systems because applications and servers may operate in different time zones.

My generated report included the following timestamp:

`2026-11-07T12:23:44.784243+00:00`

This identifies when the monitoring report was created.

### 6. Filesystem Operations Using pathlib

I learned how to create directories and manage file paths using Python's `pathlib` module.

I used:

`Path("reports")`

to represent the reports directory, followed by:

`mkdir(exist_ok=True)`

to create the directory if it did not already exist.

The application then saved the generated report to:

`reports/health_report.json`

**What I learned:** Using `pathlib` makes filesystem operations more readable and helps avoid manually constructing file paths.

### 7. Actual Testing Results

I ran the application using three configured services.

| Application | HTTP Status | Response Time | Health |
|---|---|---|---|
| Example Website | 200 | 480.87 ms | HEALTHY |
| Python Website | 200 | 499.01 ms | HEALTHY |
| Unavailable Test Service | No response | N/A | DOWN |

The terminal displayed the following summary:

- Total Applications: 3
- Healthy: 2
- Slow: 0
- Unhealthy: 0
- Down: 1

I verified that the application generated `reports/health_report.json`.

I opened the generated file in VS Code and confirmed that the summary, timestamp and visible application results matched the terminal output.

### 8. Problems Encountered and Solutions

**Problem 1 — Handling an unavailable application**

The test service at `http://127.0.0.1:9999` refused the connection because no application was listening on that port.

**Solution:** I used a `try / except` block to catch network-related exceptions and record the service as DOWN.

The application continued running and successfully generated the monitoring summary and JSON report.

**Problem 2 — Preserving results when requests fail**

A failed HTTP request does not provide a normal response object containing an HTTP status code.

**Solution:** I initialised a result dictionary with default values before making each request. This allowed the application to record failed checks with a DOWN status and error message.

### 9. Design Decisions

- I kept the application as a command-line tool because a graphical interface was unnecessary for the problem.
- I used Python's built-in modules for JSON processing, timestamps and filesystem operations to avoid unnecessary dependencies.
- I separated generated reports from the source code by creating a dedicated `reports` directory.
- I excluded generated reports from Git using `.gitignore`.
- I chose to overwrite the existing report during each execution to keep the initial implementation simple.

### 10. What I Learned

This phase helped me understand how Python handles structured data and generates useful output.

I also learned that a monitoring application should not simply display information. Saving structured results makes them more useful for troubleshooting, reporting and future automation.

### 11. Next Improvements

- Add automated unit tests using pytest.
- Test SLOW and UNHEALTHY classifications.
- Validate configuration values and handle invalid JSON.
- Refactor the application into smaller functions.
- Explore Docker and GitHub Actions for automated testing and deployment.

## Phase 3 — Refactoring and Introduction to Automated Testing

**Date:** 7 November 2026

### 1. Problem

The initial implementation contained most of the application logic in a single block of code.

Although the application worked, it was difficult to test individual operations independently.

I decided to refactor the application into smaller functions to improve readability, maintainability and testability.

### 2. What I Learned

**Python functions**

I learned how to define reusable functions using `def`, pass parameters and return results.

I separated the application into five functions:

- `classify_health()` — Determines application health based on HTTP status and response time.
- `check_application()` — Checks an application and collects monitoring results.
- `calculate_summary()` — Calculates health statistics.
- `save_report()` — Generates the JSON report.
- `main()` — Coordinates the monitoring process.

**Refactoring**

I learned that refactoring means improving the internal structure of code without intentionally changing its external behaviour.

**Application entry point**

I learned how `if __name__ == "__main__":` allows Python to run the application when executed directly without automatically running it when imported by another module.

This is particularly useful for automated testing.

### 3. Testing and Verification

After refactoring, I executed the application using:

`python monitor.py`

The application successfully checked three services.

| Application | Response Time | Health |
|---|---|---|
| Example Website | 477.26 ms | HEALTHY |
| Python Website | 492.79 ms | HEALTHY |
| Unavailable Test Service | N/A | DOWN |

The application produced the expected summary:

- Total: 3
- Healthy: 2
- Slow: 0
- Unhealthy: 0
- Down: 1

It also successfully generated the JSON report.

This confirmed that the refactored application preserved the behaviour observed in the previous implementation.

### 4. Introduction to Pytest

I installed Pytest to explore automated testing in Python.

I learned that Pytest discovers test functions and uses assertions to check whether actual results match expected results.

I also explored how automated tests can verify health classification without depending on live websites.

### 5. Challenges and Learning

The main challenge was reorganising the existing monitoring logic without changing its behaviour.

Separating the code into functions made it easier to identify the responsibilities of each component.

### 6. Next Steps

- Run the initial Pytest tests and verify their results.
- Learn mocking to simulate HTTP responses and failures.
- Test timeouts and connection errors.
- Explore Docker and GitHub Actions.