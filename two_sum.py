def two_sum(nums, target):
    # Dictionary to store number -> index
    num_map = {}

    for index, num in enumerate(nums):
        # Check if complement exists
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        # Store the number and its index
        num_map[num] = index

    # If no solution found (shouldn't happen as per problem constraints)
    return []

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print("Indices of the numbers that add up to target:", result)
