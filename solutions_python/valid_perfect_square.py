# Problem 367: Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false


class Solution(object):
    def isPerfectSquare(self, num):
        current = 1
        while current**2 < num:
            current += 1
        return current*current == num
