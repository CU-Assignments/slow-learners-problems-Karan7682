def is_palindrome(x):
    # Negative numbers and numbers ending with 0 (but not 0 itself) can't be palindrome
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x = x // 10

    # Check if original first half equals reversed second half (or its half)
    return x == reversed_half or x == reversed_half // 10

# Example usage
if __name__ == "__main__":
    test_cases = [121, -121, 10, 12321, 0]
    for x in test_cases:
        print(f"Input: {x} => Is Palindrome? {is_palindrome(x)}")
