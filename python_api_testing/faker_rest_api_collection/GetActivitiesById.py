import requests


header = {"Accept": "text/plain; v=1.0"}

response = requests.get(
    url="https://fakerestapi.azurewebsites.net/api/v1/Activities/7", headers=header
)

print("Response Body: \n", response.content)
print("\n")
print("Response Status Code: ", response.status_code)


assert response.status_code == 200
