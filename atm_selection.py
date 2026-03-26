balance = 1000
choice = ""

while choice != "exit":

    print("1 - Check balance")
    print("2 - Withdraw money")
    print("3 - Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        balance = balance - amount
        print("New balance:", balance)

    elif choice == "3":
        choice = "exit"