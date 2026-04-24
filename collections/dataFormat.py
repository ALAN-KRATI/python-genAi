def serialize(data):
    return [{"name": name, "department": dept} for name, dept in data]

print(serialize([("Alex", "IT"), ("Riya", "HR")]))