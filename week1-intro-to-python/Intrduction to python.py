num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "Invalid operation!"

print(f"{num1} {operation} {num2} = {result}")
# This code performs basic arithmetic operations based on user input.
# It prompts the user to enter two numbers and an operation, then calculates and displays the result
# based on the chosen operation.
# The code handles addition, subtraction, multiplication, and division.
# It also includes basic error handling for invalid operations.
# The result is printed in a formatted string for clarity.
# The code is a simple calculator that performs basic arithmetic operations.
# The user can input any two numbers and choose an operation to perform on them.
# The code is designed to be user-friendly and straightforward.
# The code can be extended to include more operations or error handling as needed