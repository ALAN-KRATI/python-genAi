def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def generate_fibonacci(n):
    result = []
    for i in range(n):
        result.append(fibonacci(i))
    return result

print(generate_fibonacci(6))