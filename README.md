🚀 API Test Automation Suite (Python)

A lightweight, scalable API test automation framework built using Python, pytest, and requests.
This project validates REST APIs with schema validation, negative testing, logging, and a custom themed HTML report.

🧠 Project Overview

This framework tests public REST APIs from:

👉 https://jsonplaceholder.typicode.com

It demonstrates real-world API testing practices including:

Functional validation
Schema validation (contract testing)
Negative test scenarios
Logging and structured test design
CI-ready setup
🛠 Tech Stack
Python
pytest
requests
jsonschema
pytest-html
📁 Project Structure
api-test-suite/
│
├── tests/
│   ├── test_users.py
│   └── test_posts.py
│
├── utils/
│   ├── api_client.py
│   ├── logger.py
│   └── schemas.py
│
├── ui/
│   ├── index.html
│   └── theme.css
│
├── assets/
│   └── style.css
│
├── requirements.txt
├── README.md
└── report.html (generated)
✅ Features
🔹 REST API testing using reusable client
🔹 Schema validation using jsonschema
🔹 Positive + negative test coverage
🔹 Structured logging for API calls
🔹 HTML test reports with custom theme
🔹 Clean and modular framework design
▶️ Setup & Installation

Install dependencies:

pip install -r requirements.txt
🧪 Run Tests
pytest
📊 Generate Themed HTML Report
pytest --html=report.html --self-contained-html --css=assets/style.css

Open the report:

report.html
🎨 UI/UX Visualization (Attack Theme)

A themed visual dashboard is available for demonstration purposes:

ui/index.html
ui/theme.css

Open in browser to showcase a styled testing dashboard.

Note: Theme is inspired by dark tactical visuals and does not use copyrighted assets.

### Run dashboard with Flask (optional)

Install dependencies, generate the report, then start the app from the project folder:

```bash
pip install -r requirements.txt
pytest
python app.py
```

Open **http://127.0.0.1:5000/** for the UI and **http://127.0.0.1:5000/report.html** for the themed pytest report (after `pytest` has run).

🔍 Test Coverage
✔ Positive Tests
Validate successful API responses
Status code verification
Response structure validation
❌ Negative Tests
Missing required fields
Invalid data types
Schema validation failures
🧠 Key Highlights
Designed with separation of concerns (client, tests, schemas)
Uses schema validation for contract testing
Includes negative scenarios (edge cases)
Ready for CI/CD integration (GitHub Actions)
💬 How to Explain This Project

Built a Python-based API test automation framework using pytest and requests, incorporating reusable client architecture, schema validation, negative testing, logging, and themed HTML reporting.

🚀 Future Enhancements
Environment-based configuration (dev/staging/prod)
Retry logic and error handling
API response time assertions
Integration with CI/CD pipelines
Docker support
📌 Notes
Uses a mock API (jsonplaceholder) for demonstration
Some endpoints may not return real validation errors
Schema validation is used to simulate strict API contracts
👨‍💻 Author

Built as a portfolio project to demonstrate API testing and automation skills.
![Tests](https://github.com/arshmeen/api-test-automation-framework/actions/workflows/tests.yml/badge.svg)