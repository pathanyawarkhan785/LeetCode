from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = Counter(s)

        if len(set(s.values())) == 1:
            return True

        return False


newOccur = Solution()
print(newOccur.areOccurrencesEqual("abacbc"))
