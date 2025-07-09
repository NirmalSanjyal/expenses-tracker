print(" 💰 Welcome to Smart Expenses Tracker 💰 ")
print("1. Add Expenses")
print("2. View Expesnses")
print("3. Exit")


choice = input("Enter your choice (1/2/3): ")
if choice == "1":
    category = input("Enter expenses category (e.g., Food, Travel): ")
    amount = input("Enter the amount (Rs): ")

    with open ("Expenses.txt", "a") as file:
        file.write(f"{category} - Rs.{amount}\n")

    print("✅ Expense recorded!")


elif choice == "2":
    try:
        with open("expenses.txt", "r") as file:
            print("\n--- Expense History ---")
            print(file.read())
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.")

elif choice == "3":
    print("👋 Exiting .... Have a nice day!")
    import sys
    sys.exit() # exit the program

else:
    print("❌ Invalid Option. Please enter 1,2 or 3")