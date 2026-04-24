def normalize_ids(ids):
    result = []
    
    for pid in ids:
        pid = pid.replace("_", "-").upper()
        result.append(pid)
    
    return result

print(normalize_ids(["prod-001", "PROD_002", "prod-003"]))