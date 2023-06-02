import requests


url = "https://api.meraki.com/api/v1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)