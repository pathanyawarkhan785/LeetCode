class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""

        comp = ""
        count = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                while count > 9:
                    comp += "9" + word[i - 1]
                    count -= 9
                if count > 0:
                    comp += str(count) + word[i - 1]
                count = 1

        while count > 9:
            comp += "9" + word[-1]
            count -= 9
        if count > 0:
            comp += str(count) + word[-1]

        return comp


newCompressed = Solution()
print(newCompressed.compressedString("aaaaaaaaaaaaaabb"))
