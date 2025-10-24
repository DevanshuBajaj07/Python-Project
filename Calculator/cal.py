# Define a function to perform addition
def add():
    return a + b

# Define a function to perform subtraction
def subtract():
    return a - b

# Define a function to perform multiplication
def multiply():
    return a * b

# Define a function to perform division
def divide():
    return a / b

# Print a message indicating the module is loaded
print("Calculator module loaded.")
# Print the available functions in the module
print("Available functions: add, subtract, multiply, divide")

# Prompt the user to input the first number and convert it to an integer
a = int(input(("Enter first number: ")))

# Prompt the user to input the second number and convert it to an integer
b = int(input(("Enter second number: ")))

# Ask the user what operation they would like to perform
print("What operation would you like to perform?")

# Get the operation input from the user, convert it to lowercase, and strip any extra spaces
operation = input("Add, Subtract, Multiply, Divide: ").lower().strip()

# Define a constant message for displaying results
RESULT_MESSAGE = "The result is:"

# Check the operation and call the corresponding function
if operation == "add":
    # Perform addition and print the result
    print(RESULT_MESSAGE, add())
elif operation == "subtract":
    # Perform subtraction and print the result
    print(RESULT_MESSAGE, subtract())
elif operation == "multiply":
    # Perform multiplication and print the result
    print(RESULT_MESSAGE, multiply())
elif operation == "divide":
    # Perform division and print the result
    print(RESULT_MESSAGE, divide())
else:
    # Print an error message if the operation is invalid
    print("Invalid operation selected.")