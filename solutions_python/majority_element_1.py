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
    majority_c = nums[0]
    vote = 1
    for index in range(len(nums)):
        if nums[index] == majority_c:
            vote += 1
        else:
            vote -= 1
        if vote == 0:
            majority_c = nums[index]
            vote = 1
    return majority_c


def verify_candidate(nums, majority_c):
    if nums.count(majority_c) > len(nums)//2:
        return True
    else:
        return False


class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        majority_c = find_candidate(nums)
        if verify_candidate(nums, majority_c):
            return majority_c
        else:
            return -1


