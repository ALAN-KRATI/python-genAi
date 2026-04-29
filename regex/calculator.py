try:
    a = 10
    b = 'a'
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except TypeError:
    print("Error: Invalid input type.")