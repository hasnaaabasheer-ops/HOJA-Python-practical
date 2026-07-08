try:
    num = int(input("Enter a number :"))
    print("square :",num**2)
except ValueError:
    print("invalid number entered")
else:
    print("calculation successfull")