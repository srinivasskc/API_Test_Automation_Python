# To make a request to the server and Get Response from Server
import requests
import json

# API URL
url = "https://restful-booker.herokuapp.com/booking"


# Sending GET Request
# When we sent the request, we would get the response.
# We can store the response in response variable/object
response = requests.get(url)

print("=====RESPONSE======")

# Printing the Response
print(response)
# It shows Response Status Code

# To Display response content using response.content method
print(response.content)

# To Display Header of Response
print(response.headers)


print("====JSON RESPONSE====")

# Loading the response in the form of JSON Format.
# To DO: We need to import JSON
json_response = json.loads(response.text)

# Display the response in JSON Format
print(json_response)

