import requests
import json
import jsonpath



# API URL
url="https://reqres.in/api/users/2"

# In POST Request, we need to send Request Body in JSON
# Copy the Sample Request into JSON Text File
# E:\Python\Programs\API Testing with Python\CreateBooking.json

# Read Input from JSON File
# open(file,mode)
file = open("E:\\Python\\Programs\\API Testing with Python\\UpdateUsers.json", 'r')
# r = read mode

# Reading Data from File
json_input = file.read()
print(json_input)

# Loading the JSON_Input in the form of JSON Format.
requests_json  = json.loads(json_input)
print(requests_json)

# Making PUT REQUEST WITH JSON INPUT BODY
response_put = requests.put(url, requests_json)
print(response_put.status_code)  # We should get 200 Created for POST Requests
print(response_put.content)


# Fetch Header from Response
print(response_put.headers)
print(response_put.headers.get('Etag'))
print(response_put.headers.get('Content-Length'))



# Validating Response Code
assert response_put.status_code == 200

# Parsing the response to JSON Format
response_json = json.loads(response_put.text)
print(response_json)

# Picking ID using JSON Path, 1 - Import the Module : JSONPath
updatedAt = jsonpath.jsonpath(response_json, 'updatedAt')
print(updatedAt)
print(updatedAt[0])




