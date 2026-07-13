import pytest
import requests


def test_getrequest_validation():
    """
    Response Status Code Validation.
    """
    header = {"Accept": "text/plain; v=1.0"}
    base_url = "https://fakerestapi.azurewebsites.net"

    response = requests.get(
        url=str(base_url + "/api/v1/Activities"), headers=header, timeout=5000
    )

    assert response.status_code == 200
    data = response.json()
    assert data[0]["id"] == 1
