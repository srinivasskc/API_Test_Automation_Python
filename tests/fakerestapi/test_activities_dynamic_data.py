import pytest
from utils.api_client import APIClient
import uuid
import copy
import secrets


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


# Need to pass on the fixture as argument from conftest.py
def test_post_activities_validation(api_client, load_activities_data):
    # reading the data from test_data.json file.
    activities_data = copy.deepcopy(load_activities_data["new_activity"])

    # Creating unique data fro Activity Id
    num_id = secrets.randbits(16)
    print(num_id)

    # Creating unique data for Activity Name
    base_name = "Activity"

    # 1. Use .hex to get a clean alphanumeric string without hyphens
    # 2. Slice the first 8 characters directly
    short_uuid_value = uuid.uuid4().hex[:8]
    unique_title = f"{base_name}_{short_uuid_value}"
    print(unique_title)

    # In the test_data.json, update the id key with num_id value.
    activities_data["id"] = num_id

    # In the test_data.json, update the title key with unique_title value
    activities_data["title"] = unique_title

    response = api_client.post_activities_dynamic(
        "api/v1/Activities", data=activities_data
    )
    print(response.json())
    assert response.status_code == 200

    assert response.json()["id"] == num_id
    assert response.json()["title"] == unique_title
    assert len(response.json()) > 0
