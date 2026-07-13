import requests

request_url = "https://gorest.in/public/v2/users"

request_header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer demo-token",
}

request_payload = {
    "name": "Srini Rao",
    "email": "srini.rao9@example.com",
    "gender": "male",
    "status": "active",
}

print("POST Request Body: ", request_payload)

response = requests.post(url=request_url, headers=request_header, json=request_payload)

print("POST Response Status Code: ", response.status_code)
print("POST Response Body: ", response.json())

assert response.status_code == 201
assert response.json()["name"] == "Srini Rao"


get_request_url = "https://gorest.in/public/v2/users"

# print(get_request_url + "/" + str(response.json()["id"]))

get_request_by_id = get_request_url + "/" + str(response.json()["id"])

get_response_by_id = requests.get(get_request_by_id)

print("GET Response By ID: ", get_response_by_id.json())
