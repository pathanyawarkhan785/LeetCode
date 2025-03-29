class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        sortedWords = sorted(words, key=lambda x: x[-1])
        result = " ".join(word[:-1] for word in sortedWords)
        return result


newSort = Solution()
print(newSort.sortSentence("is2 sentence4 This1 a3"))
