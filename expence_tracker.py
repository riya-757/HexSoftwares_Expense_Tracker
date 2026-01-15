# Expense Tracker Application

expenses = []

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    description = input("Enter description: ")

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | ₹{exp['amount']} | {exp['category']} | {exp['description']}")
    print()

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Expense: ₹{total}\n")

def category_summary():
    summary = {}

    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]

    print("\n--- Category-wise Summary ---")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")
    print()

def menu():
    print("==== Expense Tracker ====")
    print("1. Add an Expense")
    print("2. View All the Expenses")
    print("3. View Total Expense")
    print("4. Category-wise Summary")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Thanks for using Expence Tracker!")
        break
    else:
        print("Invalid choice. Please try again...!!\n")
