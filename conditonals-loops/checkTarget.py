data = [120, 95, 110, 80]
target = 100

for i in range(len(data)):
    if data[i] < target:
        print(f"Day {i+1}: {data[i]} units (below target)")