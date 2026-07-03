balance = 5000

def show_menu():
    print("===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    global balance
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter your deposit amount: "))
    balance += amount
    print("Amount deposited successfully!")
    print("Current Balance:", balance)

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
        print("Current Balance:", balance)
    else:
        print("Insufficient balance!")


while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid choice, please try again.")
