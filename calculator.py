import time


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def perform_operation(operation, a, b):
    start_time = time.perf_counter()

    if operation == "1":
        result = add(a, b)
        operation_name = "Addition"

    elif operation == "2":
        result = subtract(a, b)
        operation_name = "Subtraction"

    elif operation == "3":
        result = multiply(a, b)
        operation_name = "Multiplication"

    elif operation == "4":
        result = divide(a, b)
        operation_name = "Division"

    else:
        return None, None

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return result, execution_time


def main():
    print("=" * 40)
    print("       BASIC PYTHON CALCULATOR")
    print("=" * 40)

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "5":
            print("\nCalculator closed.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        result, execution_time = perform_operation(choice, num1, num2)

        print("\nResult:", result)

        if execution_time is not None:
            print(f"Execution Time: {execution_time:.10f} seconds")


if __name__ == "__main__":
    main()