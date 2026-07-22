import pytest
from datetime import datetime
import os
import json
import requests


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Adding timestamp to report file.
    report_dir = os.path.join(os.path.dirname(__file__), "reports")
    now = datetime.now().strftime("%d-%m-%y-%H_%M_%S")
    config.option.htmlpath = f"{report_dir}/reports_{now}.html"


@pytest.fixture(scope="session", autouse=True)
def setup_teardom():
    # Setting up resources
    print("Starting...")
    yield
    print("Ending...")


@pytest.fixture
def load_activities_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "test_data.json")
    with open(json_file_path) as json_data_file:
        data = json.load(json_data_file)
    return data
