# QA Automation Framework

A robust and scalable QA automation framework for end-to-end, integration, and regression testing. Built with Python and Pytest, this repository provides a foundation for automating web, API, and data validation tests.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Reporting](#reporting)
- [Contributing](#contributing)
- [License](#license)

## Overview
This framework is designed to help QA engineers automate test cases efficiently, integrate with CI/CD pipelines, and generate detailed test reports. It supports modular test development and easy maintenance.

## Features
- Pytest-based test execution
- Modular test organization
- Custom utilities and fixtures
- Configurable test environments
- HTML and Allure reporting
- Easy integration with CI/CD tools

## Project Structure
```
qa-automation-bootcamp/
├── pages/           # Page Object Models
├── reports/         # Test reports
├── tests/           # Test cases
├── utils/           # Utility scripts
├── chumma.py        # Sample script
├── conftest.py      # Pytest fixtures/config
├── pytest.ini       # Pytest configuration
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Getting Started
1. Clone the repository:
	```powershell
	git clone https://github.com/<your-org>/qa-automation-bootcamp.git
	cd qa-automation-bootcamp
	```
2. Set up a Python virtual environment (recommended).

## Installation
Install dependencies using pip:
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration
- Update `pytest.ini` for custom Pytest options.
- Add environment variables or config files as needed.

## Running Tests
Run all tests:
```powershell
pytest
```
Run specific tests:
```powershell
pytest tests/test_login.py
```
Generate HTML report:
```powershell
pytest --html=reports/report.html
```

## Reporting
Test results and reports are saved in the `reports/` directory. Integrate with Allure or other reporting tools as needed.

## Contributing
Contributions are welcome! Please submit issues and pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.

---

## Progress Log

**2025-09-03**
- Created a professional README.md template for the QA automation framework.
- Updated README.md to reflect project structure and setup instructions.
- Manual edits made to README.md for customization.
- Began work in `utils/helpers.py` for utility functions.
**2025-09-03 (Continued)**
- Refactored and improved test files for prime and factorial functions, including edge cases and exception handling.
- Added parameterized tests and grouped tests for better coverage and maintainability.
- Implemented a master runner script (`master_run_all_tests.py`) to execute all tests and generate HTML reports and logs.
- Configured logging to store test run logs in the `logs/` folder.
- Set up GitHub Actions workflow to run only the master runner script and upload both HTML report and log file as artifacts.
- Documented how to automate, schedule, and view test results and reports locally and in the cloud.