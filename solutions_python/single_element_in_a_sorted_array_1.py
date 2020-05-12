# Problem 540: Single Element in a Sorted Array
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.


# Example 1:

# Input: [1, 1, 2, 3, 3, 4, 4, 8, 8]
# Output: 2

# Example 2:

# Input: [3, 3, 7, 7, 10, 11, 11]
# Output: 10


# Note: Your solution should run in O(log n) time and O(1) space.


class Solution(object):
    def singleNonDuplicate(self, nums):
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid-1]:
                if (mid - left) % 2 == 0:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                if (mid - left) % 2 == 1:
                    right = mid - 1
                else:
                    left = mid
        return nums[left]
