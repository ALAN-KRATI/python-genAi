d1 = {"A": 5, "B": 10}
d2 = {"A": 3, "C": 8}

result = {}

for key in d1.keys() | d2.keys():
    result[key] = d1.get(key, 0) + d2.get(key, 0)

print(result)