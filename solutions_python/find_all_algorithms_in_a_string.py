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
        if len(s) < len(p):
            return []

        delta_a = [0]*26  # delta array for a->z

        for c in p:
            delta_a[ord(c)-ord('a')] += 1

        delta_b = [0]*26  # delta array for a->z
        N = len(p)
        indices = []

        for i, c in enumerate(s):

            if i < N-1:
                delta_b[ord(c)-ord('a')] += 1
            else:
                delta_b[ord(c)-ord('a')] += 1
                if delta_a == delta_b:
                    indices.append(i-N+1)
                delta_b[ord(s[i-N+1])-ord('a')] -= 1

        return indices
