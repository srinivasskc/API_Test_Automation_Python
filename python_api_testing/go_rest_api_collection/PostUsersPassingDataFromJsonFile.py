import requests
import json

base_url = "https://gorest.in/public"

request_header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer demo-token",
}

json_file = open("./Users.json")
json_payload = json.load(json_file)


print("POST Request Body: ", json_payload)


# response = requests.post(
#     url=base_url + "/v2/users", headers=request_header, json=json_payload
# )


# If we are using json, no need to use dumps. But if we are having csv, we need to dumps.
response = requests.post(
    url=base_url + "/v2/users", headers=request_header, data=json.dumps(json_payload)
)

# print(type(response.json()))


print("Response Body: ", response.json())
print("Response Status: ", response.status_code)
