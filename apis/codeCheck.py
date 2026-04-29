codes = [200, 401, 500]

for c in codes:
    if 400 <= c < 500:
        print("Client Error:", c)
    elif 500 <= c < 600:
        print("Server Error:", c)