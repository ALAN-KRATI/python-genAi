import requests
import json

try:
    res = requests.get("https://api.example.com")
    data = res.json()
except json.decoder.JSONDecodeError:
    print("Invalid JSON response")