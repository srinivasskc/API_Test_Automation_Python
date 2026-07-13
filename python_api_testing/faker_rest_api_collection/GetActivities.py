import requests

response = requests.get(url="https://fakerestapi.azurewebsites.net/api/v1/Activities")

print("Response Body: ", response.content)
print("\n")
print("Response Status Code: ", response.status_code)
