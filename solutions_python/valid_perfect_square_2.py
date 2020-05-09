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
        head = 1
        tail = 1 << 31
        while head < tail:
            current = (tail+head)//2
            if current*current - num >= 0:
                tail = current
            else:
                head = current + 1
        return head*head == num
