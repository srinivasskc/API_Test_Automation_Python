# Combine configurations for environment.json used by pytest framework.
# Terminal Run: pytest --env qa --base_url https://api.qa.com -> pytest_addoption: Registers custom CLI options ->
# -> pytest_configure: Fires automatically at startup -> configure_env: Reads environment.json + overrides with CLI options ->
# -> Global Storage: Stores output in `pytest.env` -> Test Execution: All tests can import `pytest` and use `pytest.env`


import os
import json
import time
import traceback
import pytest
from datetime import datetime


# Built-in Python Hook function, when we run pytest in terminal.
# Pytest automatically executes this function right after command-line options have been parsed and
# the main config object is initialized, but before any test files or fixtures are executed.
def pytest_configure(config):
    pytest.env = configure_env(config)


# Python Hook Function, Takes Custom Command Line Arguments from User.
def pytest_addoption(parser):
    parser.addoption("--env", dest="env", action="store", required=True)
    parser.addoption("--client_id", dest="client_id", action="store")
    parser.addoption("--client_secret", dest="client_secret", action="store")
    parser.addoption("--base_url", dest="base_url", action="store")


# Function reads environment configuration from environment.json file
# Overrides the settings with any custom options provided via CLI
def configure_env(config):
    env = None
    with open(os.getcwd() + os.sep + "environment.json", "r+") as json_file:
        env = json.load(json_file)

        # Accesses the mandatory --env CLI option stored in Pytest's config.option.
        env["env"] = str(config.option.env).lower()

        # Checks if the optional CLI arguments (--client_id, --client_secret, --base_url) were passed in the terminal command.
        # If any were supplied, their values overwrite whatever defaults were initially loaded from environment.json.
        if config.option.client_id is not None:
            env["client_id"] = config.option.client_id

        if config.option.client_secret is not None:
            env["client_secret"] = config.option.client_secret

        if config.option.base_url is not None:
            env["base_url"] = str(config.option.base_url).lower()

        json_file.seek(0)
        json.dump(env, json_file, indent=4)
        json_file.truncate()
        json_file.close()

    return env


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
