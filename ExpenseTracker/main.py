import os  # Importing the os module for file and directory operations
from datetime import date  # Importing date class to work with dates

# Class to represent one expense
class Expense:
    def __init__(self, amount, category, description, date):
        # Initialize an Expense object with amount, category, description, and date
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date


# Class to manage all expenses
class ExpenseTracker:
    def __init__(self):
        # Initialize an ExpenseTracker object with an empty list to store expenses
        self.expenses = []  
        # Ensure the "ExpenseTracker" folder exists
        os.makedirs("ExpenseTracker", exist_ok=True)  

    # Add a new expense
    def add_expense(self, amount, category, description, date_value):
        # Validate and convert the amount to a float
        try:
            amount = float(amount)
        except ValueError:
            # Print error message if the amount is invalid
            print("Invalid amount. Please enter a number.")
            return

        # Check if the amount is negative
        if amount < 0:
            print("Amount cannot be negative.")
            return

        # If no date is entered, use today's date
        if date_value.strip() == "":
            date_value = date.today().strftime("%Y-%m-%d")

        # Create a new Expense object and add it to the list
        new_expense = Expense(amount, category, description, date_value)
        self.expenses.append(new_expense)

        # Write the expense details to a file
        with open("ExpenseTracker/expense.txt", "a") as file:
            file.write(f"{amount}|{category}|{description}|{date_value}\n")

        # Print confirmation message
        print(f"Expense of ${amount} added successfully!")

    # View all expenses
    def view_expenses(self):
        try:
            # Open the file containing expenses
            with open("ExpenseTracker/expense.txt", "r") as file:
                lines = file.readlines()

                # Check if the file is empty
                if not lines:
                    print("No expenses found.")
                    return

                # Print all expenses in a formatted way
                print("\n=== All Expenses ===")
                for index, line in enumerate(lines, start=1):
                    parts = line.strip().split("|")
                    if len(parts) == 4:
                        amount, category, description, date_value = parts
                        print(f"{index}. ${amount} - {category} - {description} - {date_value}")
                print("====================")

        # Handle case where the file does not exist
        except FileNotFoundError:
            print("No expenses file found. Add an expense first.")

    # Calculate total amount spent
    def calculate_total(self):
        total = 0  # Initialize total amount to 0
        try:
            # Open the file containing expenses
            with open("ExpenseTracker/expense.txt", "r") as file:
                for line in file:
                    parts = line.strip().split("|")
                    if len(parts) >= 1:
                        try:
                            # Add the amount to the total
                            total += float(parts[0])
                        except ValueError:
                            continue
            # Print the total amount spent
            print(f"\nTotal amount spent: ${total:.2f}")
        # Handle case where the file does not exist
        except FileNotFoundError:
            print("No expenses file found. Add an expense first.")


# --- Menu system ---
tracker = ExpenseTracker()  # Create an instance of ExpenseTracker

while True:
    # Display the menu options
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        # Prompt user for expense details and add the expense
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        date_value = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        tracker.add_expense(amount, category, description, date_value)

    elif choice == "2":
        # View all expenses
        tracker.view_expenses()

    elif choice == "3":
        # Calculate and display the total amount spent
        tracker.calculate_total()

    elif choice == "4":
        # Exit the program
        print("Goodbye!")
        break

    else:
        # Handle invalid menu choice
        print("Invalid choice. Please try again.")
