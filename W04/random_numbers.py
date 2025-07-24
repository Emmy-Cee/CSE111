import random

def append_random_numbers(numbers_list, quantity=1):
    """Append 'quantity' random integers (1-100) to the end of numbers_list."""
    for _ in range(quantity):
        num = random.uniform(1, 100)
        rounded = round(num, 1)
        numbers_list.append(rounded)


def main():
    numbers = [16.2, 75.1, 52.3]
    append_random_numbers(numbers)  # Appends 1 random number
    append_random_numbers(numbers, 3)  # Appends 3 random numbers
    print(numbers)

if __name__ == "__main__":
    main()
