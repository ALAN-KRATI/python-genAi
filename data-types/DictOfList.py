revenue = {
    "Delhi": [1000, 2000, 3000],
    "Mumbai": [2000, 3000, 4000],
    "Chennai": [1500, 2500, 3500]
}

max_branch = ""
max_total = 0

for branch, values in revenue.items():
    total = sum(values)
    
    if total > max_total:
        max_total = total
        max_branch = branch

print("Highest revenue branch:", max_branch)