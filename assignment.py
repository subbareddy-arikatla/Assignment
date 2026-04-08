def sum_even_numbers(numbers):
    """
    Sums all even numbers in a given list of integers.

    Parameters:
        numbers (list): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    total = 0
    for num in numbers:
        if isinstance(num, int) and num % 2 == 0:
            total += num
    return total


def find_max_value(numbers):
    """
    Finds the maximum value in a list using a while loop.

    Parameters:
        numbers (list): A list of numbers.

    Returns:
        int/float: The maximum value in the list.
    """
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non-empty list.")

    index = 0
    max_value = numbers[0]

    while index < len(numbers):
        if numbers[index] > max_value:
            max_value = numbers[index]
        index += 1

    return max_value


# ---------------------- TEST CASES ----------------------

if __name__ == "__main__":
    # Test sum_even_numbers
    print("Sum of even numbers:", sum_even_numbers([1, 2, 3, 4, 6, 7]))

    # Test find_max_value
    print("Max value:", find_max_value([10, 25, 3, 99, 45]))

    # Test print_sequence
    print("Fibonacci sequence:")
    print_sequence(7)

    # Test process_data
    print("Processing string data:")
    process_data(["apple", "banana", "kiwi", 123])