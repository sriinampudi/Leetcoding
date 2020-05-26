# Problem 525: Contiguous Array

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0, 1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
# Input: [0, 1, 0]
# Output: 2
# Explanation: [0, 1](or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50, 000.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        result = 0
        dict_seen = {0: -1}
        for i in range(len(nums)):
              n = nums[i]
               if n == 0:
                    count -= 1
                if n == 1:
                    count += 1
                if count in dict_seen:
                    result = max(result, i-dict_seen[count])
                else:
                    dict_seen[count] = i

        return result
