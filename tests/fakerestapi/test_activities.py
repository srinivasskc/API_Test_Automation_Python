import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


def test_get_activities_validation(api_client):
    response = api_client.get_activities("api/v1/Activities")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_post_activities_validation(api_client):
    create_activities_data = {
        "id": 1507,
        "title": "Post Activities",
        "dueDate": "2026-07-15T05:38:43.120Z",
        "completed": True,
    }

    response = api_client.post_activities("api/v1/Activities", create_activities_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["title"] == "Post Activities"
    assert len(response.json()) > 0
    id = response.json()["id"]
    response = api_client.get_activities("api/v1/Activities/29")
    print(response.json())
    assert response.status_code == 200
    assert response.json()["title"] == "Activity 29"
