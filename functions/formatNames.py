def normalize_names(name_list):
    result = []

    for name in name_list:
        result.append(name.strip().lower())

    return result

print(normalize_names([" John ", "MARY", " Alex "]))