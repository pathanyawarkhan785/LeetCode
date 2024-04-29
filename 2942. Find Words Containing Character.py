class Solution:
    def findWordsContaining(self, words, x):
        temp = []
        i = 0
        while i < len(words):
            if x in words[i]:
                temp.append(i)
            i += 1

        return temp


newFindWords = Solution()
print(
    newFindWords.findWordsContaining(
        [
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        ],
        "a",
    )
)
