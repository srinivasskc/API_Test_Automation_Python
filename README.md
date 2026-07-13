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

## Reports

Test reports are generated in the `reports/` directory with timestamps.

## License

MIT License