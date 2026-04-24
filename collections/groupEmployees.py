from collections import defaultdict

def group_employees(data):
    result = defaultdict(list)
    
    for dept, name in data:
        result[dept].append(name)
    
    return dict(result)

print(group_employees([("IT", "Alex"), ("HR", "Riya"), ("IT", "John")]))