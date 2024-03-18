class Solution:
    def findWordsContaining(self, words, x):
        temp = []
        # for word in words:
        #     print(word)
        #     if x in word:
        #         print(words.index(word))
        # temp.append(words.index(word))
        # return temp
        i = 0
        while i < len(words):
            if x in words[i]:
                temp.append(words.index(words[i]))
            i += 1
        print(temp)


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
