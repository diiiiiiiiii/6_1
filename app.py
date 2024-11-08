def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

print("Welcome to the calculator app!")
operation = input("Enter operation (add, subtract, or multiply): ").strip().lower()

try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit(1)

if operation == "add":
    print("Result:", add(x, y))
elif operation == "subtract":
    print("Result:", subtract(x, y))
elif operation == "multiply":
    print("Result:", multiply(x, y))
else:
    print("Unsupported operation. Please enter 'add', 'subtract', or 'multiply'.")
