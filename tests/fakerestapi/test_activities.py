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


def test_put_activities_validation(api_client):
    update_activities_data = {
        "id": 30,
        "title": "Update Activity 30",
        "dueDate": "2026-07-18T02:24:17.731Z",
        "completed": True,
    }

    response = api_client.put_activities("api/v1/Activities/30", update_activities_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["title"] == "Update Activity 30"
    assert len(response.json()) > 0

    id = response.json()["id"]
    response = api_client.get_activities("api/v1/Activities/30")
    print(response.json())
    assert response.status_code == 200
    assert response.json()["title"] == "Activity 30"


def test_delete_activities_validation(api_client):
    response = api_client.get_activities("api/v1/Activities/30")
    print(response.json())
    assert response.status_code == 200
    assert response.json()["title"] == "Activity 30"

    response = api_client.delete_activities("api/v1/Activities/30")
    assert response.status_code == 200
