# ----------- SWAPPING METHODS -----------
# Method 1: Using temporary variable (SAFE)
def swap_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Method 2: Modified arithmetic approach (SAFE alternative)
# Instead of risking overflow, fallback to temp method
def swap_arithmetic_safe(a, b):
    # Avoid using a = a + b for large numbers
    return swap_temp(a, b)

# Method 3: Using bitwise XOR (SAFE for integers)
def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Method 4: Using tuple unpacking (BEST & PYTHONIC)
def swap_tuple(a, b):
    a, b = b, a
    return a, b


# ----------- MAIN EXECUTION -----------

if __name__ == "__main__":
    a, b = 100000000000000000000000, 200000000000000000000000

    print("Original Values:", a, b)

    print("Swap using Temp:", swap_temp(a, b))
    print("Swap using Safe Arithmetic:", swap_arithmetic_safe(a, b))
    print("Swap using XOR:", swap_xor(a, b))
    print("Swap using Tuple:", swap_tuple(a, b))