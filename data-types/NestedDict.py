departments = {
    "IT": ["Alex", "Sam"],
    "HR": ["John", "Emma"],
    "Finance": ["Raj", "Priya"]
}

dept = input("Enter department: ")

print("Employees:", departments.get(dept, "Department not found"))