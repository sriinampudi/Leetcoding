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


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if (l2: = len(s)) < (l1: = len(p)):
            return []

        p_hash = sum(map(hash, p))
        s_hash = sum(hash(s[i]) for i in range(l1))

        if p_hash == s_hash:
            return [0] + list(i+1 for i in range(l2-l1) if p_hash == (s_hash: =s_hash-hash(s[i])+hash(s[i+l1])))
        else:
            return list(i+1 for i in range(l2-l1) if p_hash == (s_hash: =s_hash-hash(s[i])+hash(s[i+l1])))
