# A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

def calculate_sum(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)

def get_integer(prompt, min_value=None, max_value=None):
    """Prompt the user for an integer, with optional bounds checking."""
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    try:
        n = get_integer(f"Enter the number of elements (1-{MAX}): ", 1, MAX)
        numbers = []
        print(f"Enter {n} integers:")
        for i in range(1, n + 1):
            num = get_integer(f"Element {i}: ")
            numbers.append(num)
        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
