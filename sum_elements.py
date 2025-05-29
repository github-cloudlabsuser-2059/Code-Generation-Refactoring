"""
A program that prompts the user for the number of elements to sum,
takes those integers as input, and handles basic error cases.
"""

MAX_ELEMENTS = 100

def calculate_sum(numbers: list[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(numbers)

def prompt_for_integer(prompt: str, min_value: int = None, max_value: int = None) -> int:
    """Prompt the user for an integer within optional bounds."""
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    """Main loop for summing user-provided integers."""
    while True:
        try:
            n = prompt_for_integer(f"Enter the number of elements (1-{MAX_ELEMENTS}): ", 1, MAX_ELEMENTS)
            numbers = []
            print(f"Enter {n} integers:")
            for i in range(n):
                num = prompt_for_integer(f"Element {i+1}: ")
                numbers.append(num)
            total = calculate_sum(numbers)
            print("Sum of the numbers:", total)
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break

        again = input("Would you like to sum another set of numbers? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
