class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split(" ")

        if len(s) != len(pattern):
            return False
        word = {}
        char = {}

        for c, w in zip(pattern, s):
            if c in word and word[c] != w:
                return False
            if w in char and char[w] != c:
                return False
            word[c] = w
            char[w] = c

        return True


newWord = Solution()

print(newWord.wordPattern("abbaa", "dog cat cat dog dog"))
