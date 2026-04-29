import requests

data = {"username": "alex", "password": "1234"}

res = requests.post("https://api.example.com/login", json=data)

print(res.status_code)