principal = 1000
rate = 5
years = 3

year = 1

while year <= years:
    principal *= (1 + rate/100)
    print(f"Year {year}: {round(principal, 2)}")
    year += 1