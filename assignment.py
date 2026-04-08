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
def print_sequence(data):
    try:
        if not data:
            print("Error: The list is empty.")
            return
        
        print("Sequence:")
        for i, value in enumerate(data):
            print(f"Index {i}: {value}")
    
    except Exception as e:
        print(f"Unexpected error in print_sequence: {e}")


def process_data(data):
    try:
        if not data:
            raise ValueError("Input list is empty.")

        processed = []

        for item in data:
            # Check if value is numeric
            if not isinstance(item, (int, float)):
                raise TypeError(f"Non-numeric value found: {item}")
            
            # Example processing: square the number
            processed.append(item ** 2)

        return processed

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except TypeError as te:
        print(f"Type Error: {te}")
    except Exception as e:
        print(f"Unexpected error in process_data: {e}")

    return None


# ✅ Testing the functions
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],
        [5, "a", 7],     # contains non-numeric
        [],              # empty list
        [2.5, 3.1, 4.8]  # float values
    ]

    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i+1}: {test}")
        
        result = process_data(test)
        
        if result is not None:
            print_sequence(result)

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