import requests
import json
import time

with open('request.json') as f:
    sample_request_input = json.load(f)
while True:
    response = requests.get("http://localhost:8000/", json=sample_request_input)
