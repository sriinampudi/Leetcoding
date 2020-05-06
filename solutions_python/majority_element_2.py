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

from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        l = len(nums)
        if l == 1:
            return nums[0]
        freq_table = Counter(nums)
        for k, v in freq_table.items():
            if v*2 > l:
                return k
        return -1

