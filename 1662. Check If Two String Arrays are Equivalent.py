class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)


newArray = Solution()
print(newArray.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
