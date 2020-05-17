# Problem 438: Find All Anagrams in a String
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20, 100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab". 

class Solution(object):
    def findAnagrams(self, s, p):
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len:
            return []
        ref = [0] * 26
        curr = [0] * 26
        for c in p:
            ref[ord(c) - ord('a')] += 1
        i = 0
        indices = []
        while i < s_len:
            curr[ord(s[i]) - ord('a')] += 1
            if ref == curr:
                indices.append(i - p_len + 1)
            if i - len(p) + 1 >= 0:
                curr[ord(s[i - p_len + 1]) - ord('a')] -= 1
            i += 1
        return indices 
