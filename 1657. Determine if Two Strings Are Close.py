from collections import Counter


class Solution:
    def closeStrings(self, word1, word2):

        if len(word1) != len(word2):
            return False

        for val in word1:
            if val not in word2:
                return False

        for val in word2:
            if val not in word1:
                return False

        word1 = Counter(word1)
        word2 = Counter(word2)

        word1 = list(word1.values())
        word2 = list(word2.values())

        word1.sort()
        word2.sort()

        return word1 == word2


newCloseStrings = Solution()
print(newCloseStrings.closeStrings("abc", "bca"))
