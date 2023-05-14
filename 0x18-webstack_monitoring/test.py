#!/usr/bin/python3
import requests

# Set up the API endpoint and parameters
api_url = "https://api.datadoghq.com/api/v1/dashboard/"
api_key = "81ed10735392a0c2e87f1e45964539d6"
api_app_key = "4b405bb4b4e9f21d3bbd9ea5b952041a811ac594"
headers = {'Content-type': 'application/json', 'DD-API-KEY': api_key, 'DD-APPLICATION-KEY': api_app_key}
query_params = {'filter': 'host:153520-web-01'}

# Make the API call to get the host details
response = requests.get(api_url, headers=headers, params=query_params)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    print(response_json)
