# Problem:229 Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3, 2, 3]
# Output: [3]
# Example 2:

# Input: [1, 1, 1, 3, 3, 2, 2, 2]
# Output: [1, 2]

from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        l = len(nums)
        if l==1:
            return nums[0]
        freq_table = Counter(nums)
        m = []
        for k, v in freq_table.items():
            if v*3 > l:
                m.append(k)
        return m
