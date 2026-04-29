import requests
import time

for i in range(3):
    try:
        res = requests.get("https://api.example.com")
        print("Success")
        break
    except:
        print("Retrying...")
        time.sleep(2)