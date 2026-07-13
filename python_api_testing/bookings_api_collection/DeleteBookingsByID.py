# To make a request to the server and Get Response from Server
import requests

# Created a new booking from Postman
# {"bookingid":11,"booking":{"firstname":"Jim","lastname":"Brown","totalprice":111,"depositpaid":true,"bookingdates":{"checkin":"2018-01-01","checkout":"2019-01-01"},"additionalneeds":"Breakfast"}}


# API URL
url = "https://restful-booker.herokuapp.com/booking/11"

# Re-Verifying the result with GET Method
response_get = requests.get(url)
print(response_get)


# Deleting the Data using Delete
# Storing the response in Response Object
response = requests.delete(url)

# Print Response
print(response)

# Print Response Code
print(response.status_code)

# Assert Response Status Code
# assert response.status_code == 403

# Re-Verifying the result with GET Method
response_get = requests.get(url)
print(response_get)
