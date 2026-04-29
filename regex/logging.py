import re

emails = ["alex@corp.com", "wrong.email@"]

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

for email in emails:
    try:
        if re.match(pattern, email):
            print("Valid:", email)
        else:
            raise ValueError("Invalid email")
    except:
        print("Invalid:", email)