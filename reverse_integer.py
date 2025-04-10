def reverse_integer(x):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    # Reverse logic
    res = 0
    negative = x < 0
    x = abs(x)

    while x != 0:
        digit = x % 10
        x = x // 10

        # Check for overflow before adding digit
        if res > (INT_MAX - digit) // 10:
            return 0

        res = res * 10 + digit

    return -res if negative else res

# Example usage
if __name__ == "__main__":
    test_cases = [123, -456, 120, 0, 1534236469]
    for x in test_cases:
        print(f"Input: {x} => Reversed: {reverse_integer(x)}")
