import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"Numbers: {numbers}")

    append_random_numbers(numbers)
    print(f"List append one number: {numbers}")

    append_random_numbers(numbers, 3)
    print(f"List append three numbers: {numbers}")

def append_random_numbers (numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = round(random.uniform())

# Call the main function
if __name__ == "__main__":
    main()