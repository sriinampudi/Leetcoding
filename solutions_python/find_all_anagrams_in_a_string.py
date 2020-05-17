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

        S1_L = len(p)
        S2_L = len(s)
        indices = []
        #Edge Condition
        if S1_L > S2_L:
            return indices

        map1 = [0] * 26
        map2 = [0] * 26
        i = 0

        while i < S1_L:
            map1[ord(p[i])-ord('a')] += 1
            map2[ord(s[i])-ord('a')] += 1
            i += 1

        # Check Initial Window
        if map1 == map2:
            indices.append(0)

        #Initialize Window Pointers
        left, right = 0, i

        while right < S2_L:
            # Slide Window
            map2[ord(s[right]) - ord('a')] += 1
            map2[ord(s[left]) - ord('a')] -= 1
            # Increment  Window Pointers
            left += 1
            right += 1
            # Check for slided window
            if map1 == map2:
                indices.append(left)

        return indices
