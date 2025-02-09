import json
import os
from datetime import datetime
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Create the reports directory if it doesn't exist
    report_dir = "reports"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Add timestamp to report file name
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = os.path.join(report_dir, f"report_{now}.html")

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSetting up resources...")
    yield
    print("\nTearing down resources...")

@pytest.fixture
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data

# @pytest.fixture
# def load_user_data():
#     json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
#     with open(json_file_path) as json_file:
#         data = json.load(json_file)
#     return data