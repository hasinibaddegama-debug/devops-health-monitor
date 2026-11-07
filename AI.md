# AI Usage — DevOps Health Monitor

## AI Tools Used

**Tool:** ChatGPT (OpenAI)

## How I Used AI

I used ChatGPT as a learning and development assistant while building my Python DevOps Health Monitor.

Specifically, I used it to:

- Understand Python syntax and concepts by comparing them with my existing Java knowledge.
- Learn how to create Python virtual environments and manage dependencies.
- Understand how to send HTTP requests using the Requests library.
- Learn how to read JSON configuration files.
- Understand exception handling and response-time measurement.
- Troubleshoot errors encountered during development.

## How I Verified AI Suggestions

I ran the suggested Python code locally in Visual Studio Code.

I verified that:

- The application successfully returned HTTP 200 for two reachable websites.
- Response times were calculated and displayed.
- An unavailable local service was classified as DOWN.
- The application handled the connection failure without crashing.

I also used the official Python and Requests documentation as references where applicable.

## Limitations and Problems

During setup, I encountered a missing-file error and a missing-module error.

I investigated the project structure and Python environment, applied the suggested corrections, and successfully ran the application.

## My Approach

I used AI for explanations, example code and troubleshooting guidance rather than treating generated suggestions as automatically correct.

I tested the application locally and am working to understand each part of the implementation before submitting it.

## Phase 3 — AI Assistance with Code Refactoring and Automated Testing

### How I Used AI

I used ChatGPT to understand how to refactor my existing Python Health Monitor into smaller, reusable functions.

ChatGPT helped me learn:

- **Python functions:** How to define functions using `def`, pass parameters and return values.
- **Code refactoring:** How to separate application logic into smaller functions to improve readability, maintainability and testability.
- **Separation of concerns:** How to give each function a specific responsibility.
- **Application entry point:** How `if __name__ == "__main__":` works and why it prevents the application from running automatically when imported.
- **Pytest:** How automated testing works in Python and how assertions can verify expected results.

### How I Verified AI Suggestions

I reviewed the suggested code and updated my existing `monitor.py` implementation.

After refactoring, I ran the application locally using `python monitor.py` and confirmed that:

- The application successfully monitored three configured services.
- Two applications were classified as HEALTHY.
- One unavailable service was classified as DOWN.
- The monitoring summary contained the expected counts.
- The application continued generating the JSON health report.

This confirmed that the refactoring preserved the application's existing behaviour in the scenarios I tested.

### Challenges and Learning

The main challenge was understanding how to reorganise the existing application without changing its functionality.

I used ChatGPT explanations and comparisons with Java to better understand Python functions and application structure.

I also learned why separating business logic from application execution makes automated testing easier.

### Next Steps

I plan to use Pytest to verify individual functions and learn how to use mocking to simulate HTTP responses, connection failures and timeouts.

I will run the tests locally and verify their results before considering the automated testing work complete.