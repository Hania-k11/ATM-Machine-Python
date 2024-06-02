import time

print("Please insert your card")

time.sleep(5)

password = 1234

pin = int(input("Enter your ATM PIN: "))

balance = 5000

if pin == password:
    while True:
        print("""
        1 == Check balance
        2 == Withdraw balance
        3 == Deposit balance
        4 == Exit
        """)

        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your balance is {balance}")

        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your current balance is {balance}")
            else:
                print("Insufficient balance")

        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is deposited into your account")
            print(f"Your current balance is {balance}")

        elif option == 4:
            print("Exiting...")
            break

        else:
            print("Invalid option, please try again")
else:
    print("Error!! Wrong PIN")
