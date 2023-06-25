class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word = {}
        for letter in s:
            if letter not in word:
                word[letter] = 1
            elif letter in word:
                word[letter] += 1
        for l in t:
            if l in word.keys():
                word[l] -= 1
        for val in word.values():
            if val != 0:
                return False
        return True
