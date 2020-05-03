# Problem 383: Ransom Note

# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines
# otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false

from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote_letters = Counter(ransomNote)
        magazine_letters = Counter(magazine)
        for x, y in ransomNote_letters.items():
            if y > magazine_letters[x]:
                return False
        return True
