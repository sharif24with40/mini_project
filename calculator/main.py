import calc_art  # Importing my own module containing ASCII art for the calculator logo
print(calc_art.logo)  # Printing the calculator logo

# Function to add two numbers
def add(n1, n2):
    return n1 + n2

# Function to subtract the second number from the first
def subtract(n1, n2):
    return n1 - n2

# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2

# Function to divide the first number by the second
def divide(n1, n2):
    if n2 == 0:  # Checking for division by zero
        return "Error! Division by zero."
    return n1 / n2

# Dictionary to map operation symbols to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Function to get a valid number input from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))  # Attempt to convert the input to a float
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Handle invalid input

# Main calculator function
def calculator():
    num1 = get_number("\nEnter your number: ")  # Get the first number from the user
    for symbol in operations:  # Print available operations
        print(symbol)

    should_continue = True  # Variable to control the calculator loop

    while should_continue:
        operation_symbol = input("Pick an operation: ")  # Get the desired operation from the user
        if operation_symbol not in operations:  # Check if the operation is valid
            print("Invalid operation. Please choose a valid operation.")
            continue
        num2 = get_number("What's the next number?: ")  # Get the second number from the user
        calculation_function = operations[operation_symbol]  # Get the corresponding function for the operation
        answer = calculation_function(num1, num2)  # Perform the calculation
        print(f"{num1} {operation_symbol} {num2} = {answer}")  # Print the result

        # Prompt the user for the next step
        next_step = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'e' to exit: ").lower()
        if next_step == 'y':  # Continue with the current result
            num1 = answer
        elif next_step == 'n':  # Start a new calculation
            should_continue = False
            calculator()
        elif next_step == 'e':  # Exit the calculator
            should_continue = False
        else:  # Handle invalid input
            print("Invalid input. Exiting calculator.")
            should_continue = False

calculator()  # Start the calculator
