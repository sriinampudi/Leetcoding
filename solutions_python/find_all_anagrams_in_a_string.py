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

from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        s_length, p_length = len(s), len(p)
        if s_length < p_length:
            return []
        p_count = Counter(p)
        s_count = Counter()

        result = []

        for i in range(s_length):
            s_count[s[i]] += 1
            if i >= p_length:
                if s_count[s[i-p_length]] == 1:
                    del s_count[s[i-p_length]]
                else:
                    s_count[s[i-p_length]] -= 1
            if p_count == s_count:
                result.append(i-p_length+1)
        return result
