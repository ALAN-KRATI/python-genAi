import requests

try:
    requests.get("https://api.example.com", timeout=5)
except requests.exceptions.Timeout:
    print("Request Timeout")