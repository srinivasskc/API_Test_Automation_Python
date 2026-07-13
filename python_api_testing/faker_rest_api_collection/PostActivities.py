import requests


activities_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

request_header = {
    "Accept": "text/plain; v=1.0",
    "Content-Type": "application/json; v=1.0",
}

# Request Body
request_payload = {
    "id": 34,
    "title": "Srinivas API Testing",
    "dueDate": "2026-07-12T01:57:59.199Z",
    "completed": True,
}

response = requests.post(
    url=activities_url,
    headers=request_header,
    json=request_payload,
)

print(response.status_code)
print(response.json())

response_body = response.json()
print(response_body["id"])

assert response.status_code == 200
assert response_body["id"] == 34
