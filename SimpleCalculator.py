# Simple Calculator Program
# This program performs basic arithmetic operations: addition, subtraction,
# multiplication, and division based on user input.

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Display available operations to the user
print("Select Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Take user input for operation
choice = input("Enter choice (1/2/3/4): ")

# Validate operation choice
if choice in ['1', '2', '3', '4']:
    try:
        # Take user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the chosen operation
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
    except ValueError:
        print("Invalid input: Please enter valid numbers.")
else:
    print("Invalid choice: Please enter a number between 1 and 4.")
