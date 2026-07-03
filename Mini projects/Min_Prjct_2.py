balance = 5000

def show_menu():
    print("===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter your deposit amount: "))
    balance += amount
    print("Amount deposited successfully!")
    print("Current Balance:", balance)

def withdraw():
    global balance
    amount = int(input("enter amount to withdraw :"))
    if amount <= balance:
        balance = balance -amount
        print("collect your cash.")
        print("current balance :", balance)
    else:
        print("insufficient balance")


while True:
    show_menu()

    choice = int(input("enter your choice :"))
    if choice ==1:
        check_balance()
    elif choice ==2:
        deposit()
    elif choice==3:
        withdraw()
    elif choice==4:
        print("Thank you for using this ATM")
        break
    else:
        print('invalid choice')
