from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

        commonChar = Counter(words[0])

        for word in words[1:]:
            commonChar &= Counter(word)

        return list(commonChar.elements())


newCommonChars = Solution()
print(newCommonChars.commonChars(["bella", "label", "roller"]))
