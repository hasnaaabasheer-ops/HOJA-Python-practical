def get_product_name():
    product = input("Enter product name :")
    quantity = int(input("Enter quantity :"))
    price = int(input("Enter the price :"))
    return product, quantity,price

def calculate(quantity,price):
    total = quantity * price
    return total

def print_bill(product,quantity,price,total):
    print("----GROCERY BILL----")
    print("product :",product)
    print("Quantity :",quantity)
    print("Price :",price)
    print("Total Bill :",total)

def main():
    product ,quantity,price = get_product_name()
    total =calculate(quantity,price)
    print_bill(product,quantity,price,total)

main()