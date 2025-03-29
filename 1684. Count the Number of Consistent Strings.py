from collections import Counter


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        return sum(all(char in allowed_set for char in word) for word in words)


newCount = Solution()
print(newCount.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
