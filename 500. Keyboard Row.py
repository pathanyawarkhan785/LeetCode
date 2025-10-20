class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        firstLine = "qwertyuiop"
        secondLine = "asdfghjkl"
        thirdLine = "zxcvbnm"

        for i in range(len(words)):
            for j in range(len(words[i])):
                print(words[i][j])


newFind = Solution()
newFind.findWords(["Hello", "Alaska", "Dad", "Peace"])
