# API Automation Testing Framework 

##  Overview
This project is a scalable **API automation testing framework** designed to validate both **positive and negative API scenarios**, ensuring APIs behave correctly under valid and invalid conditions.

It focuses on:
- Verifying correct API functionality
- Validating error handling and response codes
- Ensuring response structure and data integrity
- Improving overall API reliability and quality

The framework is built using **Python, PyTest, and Requests**, with **CI automation via GitHub Actions**.

---

## Tech Stack
- **Python 3.14**
- **PyTest** – Test execution framework
- **Requests** – API interaction
- **Allure** – Test reporting
- **JSON Schema** – Response validation
- **GitHub Actions** – Continuous Integration (CI)

---

#  Test Coverage
###  Positive Test Scenarios
- Successful GET, POST, PUT, DELETE requests
- Correct status codes and response payloads
- Schema validation for successful responses

### Negative Test Scenarios
- Invalid request payloads
- Missing or incorrect headers
- Invalid resource IDs
- Proper error codes (400, 403, 404, etc.)

---

## Retry & Timeout Handling
- Built-in retry mechanism for flaky APIs
- Custom timeout configuration to prevent hanging tests

---

##  How to Run Tests Locally

### Clone the Repository
```bash
git clone https://github.com/KamzyPrinzel/api-automation-framework.git
cd api-automation-framework

## Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

## Install Dependencies
pip install -r requirements.txt

## Run All Tests
pytest

## Run Tests with Allure Report
pytest --alluredir=allure-results
allure serve allure-results
