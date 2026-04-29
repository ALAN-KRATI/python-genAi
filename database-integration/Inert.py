import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

data = [
    ("Alex", "alex@mail.com"),
    ("John", "john@mail.com"),
    ("Riya", "riya@mail.com")
]

cursor.executemany("INSERT INTO customers (name, email) VALUES (?, ?)", data)

print("3 customer records added successfully.")

conn.commit()
conn.close()