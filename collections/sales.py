def total_sales(data):
    result = {}
    
    for category, amount in data:
        result[category] = result.get(category, 0) + amount
    
    return result

print(total_sales([("Electronics", 1000), ("Furniture", 2000), ("Electronics", 1500)]))