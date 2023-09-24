def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i]

        num_indices[num] = i
    return None
nums = [1, 2, 5 ,11 , 20, 6]
target = 16
result = two_sum(nums, target)
print(result)