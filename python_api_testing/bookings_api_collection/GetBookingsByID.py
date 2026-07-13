# To make a request to the server and Get Response from Server
import requests
import json
import jsonpath

# API URL
url = "https://restful-booker.herokuapp.com/booking/11"


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

print("====JSON Path - Specific Data from JSON Response Content===")

# Fetch Specific Data using JSONPATH
# Storing the Result into Total_Price Variable
total_price = jsonpath.jsonpath(json_response, 'totalprice')
print(total_price)

booking_dates = jsonpath.jsonpath(json_response, 'bookingdates')
print(booking_dates)

print("===Asserting the Values====")
assert total_price == [111]


