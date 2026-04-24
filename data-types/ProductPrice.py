name = input("Enter the name of the product: ")
price = float(input("Enter the price of the product: "))
discount = float(input("Enter the discount percentage: "))

totalPrice = price - (price * discount / 100)

print("final price is: ", totalPrice)