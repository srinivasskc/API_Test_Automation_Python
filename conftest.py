import pytest
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    import os
    report_dir = os.path.join(os.path.dirname(__file__), "reports")
    now = datetime.now().strftime("%d-%m-%y-%H_%M_%S")
    config.option.htmlpath = f"{report_dir}/reports_{now}.html"


def setup_teardom(scope="session", autouse=True):
    print("Starting...")
    yield
    print("Ending...")
