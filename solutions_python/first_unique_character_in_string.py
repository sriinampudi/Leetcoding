# Problem 387: First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.


class Solution:
    def firstUniqChar(self, s):
        count = {}
        for c in set(s):
            count[c] = s.count(c)

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1
