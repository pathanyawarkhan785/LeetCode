from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:

        freqS = Counter(s)
        sortVal = dict(sorted(freqS.items(), key=lambda x: x[1], reverse=True))
        newStr = ""

        for i, j in sortVal.items():
            newStr += "".join(i) * j

        return newStr


newFrequency = Solution()
print(newFrequency.frequencySort("tree"))
