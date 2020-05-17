# Problem 242: Valid Anagram
# Given two strings s and t, write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)

        for letter, count in s_count.items():
            if t_count[letter] != count:
                return False
        return True
