import os
from datetime import date

# Class to represent one expense
class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date


# Class to manage all expenses
class ExpenseTracker:
    def __init__(self):
        self.expenses = []  # stores Expense objects
        os.makedirs("ExpenseTracker", exist_ok=True)  # make sure folder exists

    # Add a new expense
    def add_expense(self, amount, category, description, date_value):
        # simple validation
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return

        if amount < 0:
            print("Amount cannot be negative.")
            return

        # if no date entered, use today's date
        if date_value.strip() == "":
            date_value = date.today().strftime("%Y-%m-%d")

        # create and store the expense
        new_expense = Expense(amount, category, description, date_value)
        self.expenses.append(new_expense)

        # write to file
        with open("ExpenseTracker/expense.txt", "a") as file:
            file.write(f"{amount}|{category}|{description}|{date_value}\n")

        print(f"Expense of ${amount} added successfully!")

    # View all expenses
    def view_expenses(self):
        try:
            with open("ExpenseTracker/expense.txt", "r") as file:
                lines = file.readlines()

                if not lines:
                    print("No expenses found.")
                    return

                print("\n=== All Expenses ===")
                for index, line in enumerate(lines, start=1):
                    parts = line.strip().split("|")
                    if len(parts) == 4:
                        amount, category, description, date_value = parts
                        print(f"{index}. ${amount} - {category} - {description} - {date_value}")
                print("====================")

        except FileNotFoundError:
            print("No expenses file found. Add an expense first.")

    # Calculate total amount spent
    def calculate_total(self):
        total = 0
        try:
            with open("ExpenseTracker/expense.txt", "r") as file:
                for line in file:
                    parts = line.strip().split("|")
                    if len(parts) >= 1:
                        try:
                            total += float(parts[0])
                        except ValueError:
                            continue
            print(f"\nTotal amount spent: ${total:.2f}")
        except FileNotFoundError:
            print("No expenses file found. Add an expense first.")


# --- Menu system ---
tracker = ExpenseTracker()

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        date_value = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        tracker.add_expense(amount, category, description, date_value)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.calculate_total()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
