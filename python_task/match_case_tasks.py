print("-----MENU-----")
print("1. Mutton Biryani")
print("2. Chicken Biryani")
print("3. Fish Biryani")
print("4. Prawn Biryani")
print("5. Butter Chicken")
option=int(input("Enter your choice: "))
match option:
    case 1:
        print("Item       : Mutton Biryani")
        print("Price      : 500")
        print("Desciption : Rice with tender goat meat")
    case 2:
        print("Item       : Chicken Biryani")
        print("Price      : 300")
        print("Desciption : Rice with spiced chicken.")
    case 3:
        print("Item       : Fish Biryani")
        print("Price      : 350")
        print("Desciption : Rice with seasoned fish.")
    case 4:
        print("Item       : Prawn Biryani")
        print("Price      : 400")
        print("Desciption : Rice with juicy prawns.")
    case 5:
        print("Item       : Butter Chicken")
        print("Price      : 350")
        print("Desciption : Chicken in creamy tomato sauce.")
    case _:
        print("Invalid Choice")


balance = 10000
print("----- ATM MENU -----")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
option=int(input("Enter your choice: "))
match option:
    case 1:
        print(f"Current Balance: {balance}")
    case 2:
        amount=float(input("Enter deposit amount: "))
        balance+=amount
        print("Amount Deposited Successfully")
        print(f"Updated balance: {balance}")
    case 3:
        amount=float(input("Enter withdrawal amount: "))
        if amount<=balance:
            balance-=amount
            print("Amount Withdrawal Successfully")
            print(f"Updated balance: {balance}")
        else:
            print("Insufficient balance")
    case 4:
        print("Thankyou for using ATM. Goodbye")
    case _:
        print("Invalid Choice")