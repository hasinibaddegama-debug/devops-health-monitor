# Research Log — DevOps Health Monitor

## 1st Step

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