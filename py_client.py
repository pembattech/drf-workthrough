import requests

endpoint = "http://127.0.0.1:8000/api"

get_response = requests.get(endpoint)

# print(get_response.text) # return raw text response
# print(get_response.status_code) # return status_code of get_response
print(get_response.json()) # return JSON

