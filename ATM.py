print("===============================")
print("Welcome to the ATM")
print("===============================")

balance = 5000
ATM_Pin = 1111

try:
    pin = int(input("Enter your ATM Pin: "))

    if pin != ATM_Pin:
        raise ValueError("Invalid Pin")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        try:
            if choice == "1":
                print("Your balance is:", balance)

            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    raise ValueError("Amount must be positive!")

                if amount > balance:
                    raise Exception("Insufficient balance!")

                balance -= amount

                print("Withdrawal successful!")
                print("Remaining balance:", balance)

            elif choice == "3":
                amount = float(input("Enter deposit amount: "))

                if amount <= 0:
                    raise ValueError("Amount must be positive!")

                balance += amount

                print("Deposit successful!")
                print("Updated balance:", balance)

            elif choice == "4":
                print("Thank you for using Python ATM!")
                break

            else:
                print("Invalid choice! Try again.")

        except ValueError as e:
            print("Input Error:", e)

        except Exception as e:
            print("Transaction Error:", e)

except ValueError as e:
    print("Authentication Error:", e)

finally:
    print("Exiting the ATM. Have a nice day!")