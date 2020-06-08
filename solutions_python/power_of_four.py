# Problem 342: Power of Four 

# Given an integer(signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        while num > 0:
            if num == 1:
                return True
            elif num % 4 == 0:
                num = num/4
            else:
                return False
        return True
