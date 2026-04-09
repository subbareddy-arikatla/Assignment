# ----------- SWAPPING METHODS -----------

# Method 1: Using temporary variable
def swap_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Method 2: Using arithmetic operations
def swap_arithmetic(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Method 3: Using bitwise XOR
def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Method 4: Using tuple unpacking (Pythonic way)
def swap_tuple(a, b):
    a, b = b, a
    return a, b


# ----------- CLASS WITH OPERATOR OVERLOADING -----------

class Number:
    def __init__(self, value):
        self.value = value

    # Overloading + operator
    def __add__(self, other):
        return Number(self.value + other.value)

    # Overloading > operator
    def __gt__(self, other):
        return self.value > other.value

    # Overloading == operator
    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f"Number({self.value})"


# ----------- PYTHON OPERATORS DEMO -----------

def operator_examples(a, b):
    print("Arithmetic Operators:")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

    print("\nComparison Operators:")
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("a == b:", a == b)

    print("\nLogical Operators:")
    print("(a > 0 and b > 0):", a > 0 and b > 0)
    print("(a > 0 or b < 0):", a > 0 or b < 0)
    print("not(a > 0):", not(a > 0))

    print("\nAssignment Operators:")
    x = a
    x += b
    print("x += b:", x)
    x -= b
    print("x -= b:", x)


# ----------- MAIN EXECUTION -----------

if __name__ == "__main__":
    a, b = 10, 5

    print("Original Values:", a, b)

    print("\nSwap using Temp:", swap_temp(a, b))
    print("Swap using Arithmetic:", swap_arithmetic(a, b))
    print("Swap using XOR:", swap_xor(a, b))
    print("Swap using Tuple:", swap_tuple(a, b))

    print("\n--- Operator Overloading Demo ---")
    n1 = Number(10)
    n2 = Number(20)

    n3 = n1 + n2
    print("Addition of objects:", n3)
    print("n1 > n2:", n1 > n2)
    print("n1 == n2:", n1 == n2)

    print("\n--- Python Operators Example ---")
    operator_examples(10, 5)