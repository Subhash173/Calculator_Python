# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to get user input and handle invalid inputs
def get_numbers():
    try:
        # Prompt user for input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        # Handle non-numerical input
        print("Invalid input! Please enter numerical values.")
        return None, None

# Main calculator function
def calculator():
    while True:
        # Display the menu options
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user choice
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user wants to exit
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the choice is one of the valid options
        if choice in ['1', '2', '3', '4']:
            # Get numbers from the user
            num1, num2 = get_numbers()
            if num1 is None or num2 is None:
                continue

            # Perform the chosen operation and display the result
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            # Handle invalid menu choice
            print("Invalid choice! Please select a valid operation.")

# Run the calculator function if this script is executed
if __name__ == "__main__":
    calculator()
