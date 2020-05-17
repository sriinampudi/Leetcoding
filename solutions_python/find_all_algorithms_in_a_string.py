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
        delta = [0]*26 #delta array for a->z
        N = len(p)
        results = []

        for c in p:
            delta[ord(c)-ord('a')] +=1
        for index,c in enumerate(s):
            # we add s[index] to current window i.e. remove s[index] from delta
            delta[ord(c)-ord('a')] -= 1
            if index>=N:
            # we remove s[index-N] from current window i.e. add s[index-N] back to delta
                delta[ord(s[index-N])-ord('a')] +=1

            if index>=N-1 and all (x==0 for x in delta):
                #check that all delta is zero
                results.append(index-(N-1))
        return results

                                                            
