def calculate_total(price, quantity):
    total = price * quantity
    if total > 1000:
        discount = total * 10 / 100
        total = total - discount
        print("Discount Applied")
    else:
        print("No Discount")
    return total

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
result = calculate_total(price,quantity)
print("Final Amount:", result)
print("Thank You!")
   