# Problem 208: Implement Trie(Prefix Tree)

# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie()

# trie.insert("apple")
# trie.search("apple")
# // returns true
# trie.search("app")
# // returns false
# trie.startsWith("app")
# // returns true
# trie.insert("app")
# trie.search("app")
# // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.


class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie

        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = True

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True
