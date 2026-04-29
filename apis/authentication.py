import requests

token = "abc123"

headers = {
    "Authorization": f"Bearer {token}"
}

res = requests.get("https://api.example.com", headers=headers)

print(res.status_code)