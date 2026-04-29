import re

try:
    text = "Na#me: A$le%x"
    cleaned = re.sub(r'[^a-zA-Z0-9: ]', '', text)
    print("Cleaned Data:", cleaned)
except:
    print("Error processing data")