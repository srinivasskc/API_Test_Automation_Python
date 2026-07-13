import requests

activities_url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/18"

request_header = {
    "Accept": "text/plain; v=1.0",
    "Content-Type": "application/json; v=1.0",
}

get_Request = requests.get(
    url="https://fakerestapi.azurewebsites.net/api/v1/Activities/18",
    headers=request_header,
)

print("Get Request Response: ", get_Request.json())


request_payload = {
    "id": 41,
    "title": "Srini_Updating_18_41",
    "dueDate": "2026-07-12T02:29:57.240Z",
    "completed": False,
}

print("PUT Request Body: ", request_payload)


response = requests.put(
    url=activities_url, headers=request_header, json=request_payload
)

print("PUT Response Status Code: ", response.status_code)
print("PUT Response Body: ", response.json())
print("PUT Response Body-Id: ", response.json()["id"])

assert response.status_code == 200
assert response.json()["id"] == 41
