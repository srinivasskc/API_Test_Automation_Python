# API Test Automation with Python

A comprehensive API testing framework using Python, pytest, and the Requests library.

## Project Overview

This project provides automated tests for various REST APIs including:
- **Fakerest API** - Activity management endpoints
- **GoRest API** - User authentication and data operations
- **Bookings API** - Hotel booking management
- **ReqRes API** - User creation and update operations

## Tech Stack

- **Python** - Programming language
- **pytest** - Testing framework
- **requests** - HTTP library for API calls

## Project Structure

```
API_Test_Automation_Python/
├── python_api_testing/       # Main API test implementations
│   ├── faker_rest_api_collection/
│   ├── go_rest_api_collection/
│   ├── bookings_api_collection/
│   └── reqres_api_collection/
├── tests/                    # Test files
├── postman/                  # Postman collections for reference
├── utils/                    # Utility functions
├── conftest.py               # pytest configuration
├── pytest.ini                # pytest settings
└── requirements.txt         # Python dependencies
```

## Prerequisites

- Python 3.7+
- pip

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_get_activities.py
```

Run with HTML report:
```bash
pytest --html=reports/report.html
```

## Configuration

Test configuration is in `pytest.ini`:
- Max failures before stopping: 2
- Verbose output enabled
- HTML report generation

## Reports & CI/CD Summaries

Test reports are automatically generated locally and uploaded to GitHub Actions during every pipeline run.

### 1. View Locally
Locally executed test reports are written directly into the `reports/` directory with explicit execution timestamps:
* **Path:** `reports/reports_<timestamp>.html`

### 2. Access via GitHub Actions
Every time the automated CI/CD suite triggers on a push or a pull request, the test report is bundled up as a downloadable build artifact:

1. Navigate to the [Actions tab](https://github.com/srinivasskc/API_Test_Automation_Python/actions) in the repository.
2. Click on the most recent completed workflow run (marked with a green checkmark).
3. Scroll down to the absolute bottom of the run summary page to the **Artifacts** block.
4. Click on the **`pytest-report`** archive link to download the zip file containing your execution logs and interactive HTML summary.

## License

MIT License