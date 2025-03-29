class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        matchStr = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j] and words[i] not in matchStr:
                    matchStr.append(words[i])

        return matchStr


newString = Solution()
print(newString.stringMatching(["mass", "as", "hero", "superhero"]))
