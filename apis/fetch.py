import requests

res = requests.get("https://api.example.com/data")
data = res.json()

print(data)