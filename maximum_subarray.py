def max_sub_array(nums):
    if not nums:
        return 0

    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        # Either start new subarray at current num or extend previous one
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
if __name__ == "__main__":
    test_cases = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [5,4,-1,7,8],
        [-1, -2, -3]
    ]
    for nums in test_cases:
        print(f"Input: {nums} => Max Subarray Sum: {max_sub_array(nums)}")
