# Problem 567: Permutation in String

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1("ba").
# Example 2:

# Input: s1 = "ab" s2 = "eidboaoo"
# Output: False


# Note:

# The input strings only contain lower case letters.
# The length of both given strings is in range[1, 10, 000].

class Solution:
    def checkInclusion(self, s: str, t: str) -> bool:

        S1_L = len(s)
        S2_L = len(t)

        #Edge Condition
        if S1_L > S2_L:
            return False

        map1 = [0] * 26
        map2 = [0] * 26
        i = 0

        while i < S1_L:
            map1[ord(s[i])-ord('a')] += 1
            map2[ord(t[i])-ord('a')] += 1
            i += 1
        # Check Initial Window
        if map1 == map2:
            return True
        #Initialize Window Pointers
        left, right = 0, i
        while right < S2_L:
            # Slide Window
            map2[ord(t[right]) - ord('a')] += 1
            map2[ord(t[left]) - ord('a')] -= 1
            # Increment  Window Pointers
            left += 1
            right += 1
            # Check for slided window
            if map1 == map2:
                return True

        return False
