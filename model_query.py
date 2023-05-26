import requests
import json

with open('request.json') as f:
    sample_request_input = json.load(f)
response = requests.get("http://localhost:8000/", json=sample_request_input)
print(response.text)
