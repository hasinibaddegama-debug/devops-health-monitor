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

## Phase 4 — AI Assistance with Automated Testing

### How I Used AI

I used ChatGPT to understand automated testing in Python, including Pytest, assertions and mocking.

ChatGPT helped me explore how to write tests for application health classification, summary calculations, HTTP errors, connection failures and request timeouts.

### How I Verified AI Suggestions

I reviewed the suggested test cases and executed them locally using Pytest.

All seven tests passed in 0.42 seconds.

I also ran the Health Monitor normally to verify that the application continued monitoring services and generating JSON reports correctly.

### What I Learned

I learned how mocking can simulate HTTP responses and exceptions without relying on external websites.

I also learned how automated tests can help detect unexpected changes when refactoring or extending an application.

## Phase 5 — AI Assistance with Docker Containerisation

### 1. How I Used AI

I used ChatGPT to learn about Docker containerisation and understand how to package my Python Health Monitor into a Docker image.

ChatGPT helped me understand:

- The difference between Docker images and containers.
- How to create a Dockerfile.
- How to use `FROM`, `WORKDIR`, `COPY`, `RUN` and `CMD`.
- Why `.dockerignore` is useful.
- How Docker bind mounts work.
- How to troubleshoot Docker Engine connection errors.

### 2. Problems and AI Suggestions

During the initial setup, Docker commands failed because the Docker CLI could not connect to the Docker Engine.

I used ChatGPT to understand the error and investigate possible causes.

The suggested troubleshooting steps included checking Docker Desktop and verifying that the Docker Engine was running.

After starting Docker Desktop, I retried the build and successfully created the image.

### 3. How I Verified AI Suggestions

I did not rely only on the AI-generated instructions.

I executed the suggested commands locally and checked the results.

I successfully:

- Built the Docker image.
- Ran the Health Monitor inside a container.
- Verified the HTTP status codes and health classifications.
- Confirmed that the application generated its monitoring summary.
- Ran the application with a bind mount to connect the reports directory to the host filesystem.

### 4. What I Learned

Using ChatGPT helped me understand Docker concepts and investigate errors.

I learned the importance of verifying AI suggestions through practical testing rather than assuming they are correct.

I also gained experience using Docker to package and execute a Python application.

## Phase 6 — AI Assistance with GitHub Actions

### How I Used AI

I used ChatGPT to understand Continuous Integration, GitHub Actions and YAML workflow configuration.

ChatGPT helped me create a workflow that installs Python dependencies and executes my automated Pytest tests.

### Problems and Suggestions

After pushing my workflow, it did not appear in GitHub Actions.

I used ChatGPT to investigate the problem and identify that the workflow file was stored in the wrong directory.

I corrected the folder structure and pushed the changes again.

### How I Verified the Suggestions

I checked the repository structure and confirmed that GitHub recognised the workflow after moving the file.

I opened the GitHub Actions tab and verified that the workflow completed successfully.

The successful execution confirmed that the workflow configuration was recognised and the CI job completed.

### What I Learned

I learned how to automate testing with GitHub Actions and how important configuration file locations are.

I also learned to verify AI-generated instructions by checking actual execution results rather than relying on explanations alone.

### Final Verification of GitHub Actions

I verified the GitHub Actions workflow by reviewing the execution logs.

The workflow successfully installed the Python dependencies and executed all seven Pytest tests on a Linux runner.

All seven tests passed in 0.59 seconds.

This confirmed that the suggested CI configuration worked correctly after I corrected the workflow directory structure.