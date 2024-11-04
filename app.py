def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Prompt the user for the operation and numbers
print("Welcome to the calculator app!")
operation = input("Enter operation (add, subtract, multiply, or divide): ").strip().lower()

try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit(1)

# Perform the calculation based on the chosen operation
if operation == "add":
    print("Result:", add(x, y))
elif operation == "subtract":
    print("Result:", subtract(x, y))
elif operation == "multiply":
    print("Result:", multiply(x, y))
elif operation == "divide":
    print("Result:", divide(x, y))
else:
    print("Unsupported operation. Please enter 'add', 'subtract', 'multiply', or 'divide'.")
