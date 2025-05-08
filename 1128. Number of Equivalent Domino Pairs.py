from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:

        countPair = defaultdict(int)
        result = 0

        for d in dominoes:
            key = tuple(sorted(d))
            countPair[key] += 1

        for val in countPair.values():
            result += val * (val - 1) // 2

        return result


newEquiv = Solution()
print(newEquiv.numEquivDominoPairs([[1, 1], [2, 2], [1, 1], [1, 2], [1, 2], [1, 1]]))
