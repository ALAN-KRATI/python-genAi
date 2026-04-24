def clean_csv(text):
    text = text.replace("!!", "").replace(",,", ",")
    parts = text.split(",")
    
    cleaned = []
    for p in parts:
        p = p.strip()
        if p:
            cleaned.append(p)
    
    return ", ".join(cleaned)

print(clean_csv("John,, Doe!!, New York "))