def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b, or raise an error if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def get_number(prompt):
    """Prompt the user for a number and validate input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Basic Calculator")
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide)
    }

    while True:
        print("\nSelect operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid input. Please select a valid operation.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = operations[choice][1](num1, num2)
            print("Result:", result)
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
