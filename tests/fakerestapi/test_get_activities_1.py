import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


def test_get_activities_validation(api_client):
    response = api_client.get("api/v1/Activities")
    print(response.json())
    assert response.status_code == 201
    assert len(response.json()) > 0
