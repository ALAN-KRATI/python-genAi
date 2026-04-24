def clean_list(data):
    return [x for x in data if x]

print(clean_list(["Alex", "", "John", None, "Riya"]))