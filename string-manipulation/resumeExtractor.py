def extract_keywords(text, keywords):
    words = text.lower().split()
    result = []
    
    for key in keywords:
        if key.lower() in words:
            result.append(key)
    
    return result

text = "John has experience in Python, Django, and React."
print(extract_keywords(text, ["Python", "Django"]))