# Problem 169: Majority Element

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input:
# [3, 2, 3]
# Output:
# 3

# Example 2:

# Input:
# [2, 2, 1, 1, 1, 2, 2]
# Output:
# 2


def find_candidate(nums):
    if len(nums) == 1:
        return nums[0]
    majority_e = nums[0]
    count = 1
    for index in range(len(nums)):
        if nums[index] == majority_e:
            count += 1
        else:
            count -= 1
        if count == 0:
            majority_e = nums[index]
            count = 1
    return majority_e


def verify_candidate(nums, x):
    if nums.count(x) > len(nums)//2:
        return True
    else:
        return False


class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        candidate = find_candidate(nums)
        if verify_candidate(nums, candidate):
            return candidate
        else:
            return -1


