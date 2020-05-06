# Problem 169: Majority Element

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3, 2, 3]
# Output: 3
# Example 2:

# Input: [2, 2, 1, 1, 1, 2, 2]
# Output: 2


class Solution:
    def majorityElement(self, nums):
        if len(nums)==1:
            return nums[0]
        nums.sort()
        return nums[len(nums)//2]
