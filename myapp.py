def calculator():
    """
    A simple calculator function that allows users to perform basic arithmetic operations.

    The calculator provides the following options:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage calculation
    6. Exit the calculator

    The user is prompted to select an operation and input the required numbers.
    The function handles invalid inputs and division by zero gracefully.

    Usage:
    - Enter the number corresponding to the desired operation.
    - For operations 1-4, input two numbers.
    - For operation 5 (Percentage), input a single number to calculate its percentage (divided by 100).
    - Enter 6 to exit the calculator.

    Error Handling:
    - If the user enters an invalid choice, they are prompted to try again.
    - If the user enters non-numeric input, an error message is displayed.
    - Division by zero is not allowed and will display an error message.

    The function runs in a loop until the user chooses to exit.
    """
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Percentage")
        print("6. Exit")

        try:
            choice = int(input("Enter choice (1/2/3/4/5/6): "))
            if choice == 6:
                print("Exiting the calculator. Goodbye!")
                break
            if choice not in [1, 2, 3, 4, 5]:
                print("Invalid choice")
                continue

            num1 = float(input("Enter first number: "))
            if choice == 5:
                print(f"The result is: {num1 / 100}")
            else:
                num2 = float(input("Enter second number: "))
                if choice == 1:
                    print(f"The result is: {num1 + num2}")
                elif choice == 2:
                    print(f"The result is: {num1 - num2}")
                elif choice == 3:
                    print(f"The result is: {num1 * num2}")
                elif choice == 4:
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                    else:
                        print(f"The result is: {num1 / num2}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()