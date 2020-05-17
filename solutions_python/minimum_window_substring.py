# Problem 76: Minimum Window Substring
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        S_L = len(s)
        T_L = len(t)
        if T_L > S_L:
            return ""
        map_t = Counter(t)
        left, right = 0, 0
        mwStart, mwEnd = 0, 0
        no_of_chars = T_L
        while right < S_L:
            if map_t[s[right]] > 0:
                no_of_chars -= 1
            map_t[s[right]] -= 1
            right += 1

            while no_of_chars == 0:
                if mwEnd == 0 or right-left < mwEnd-mwStart:
                    mwStart, mwEnd = left, right
                map_t[s[left]] += 1
                if map_t[s[left]] > 0:
                    no_of_chars += 1
                left += 1
        return s[mwStart:mwEnd]
