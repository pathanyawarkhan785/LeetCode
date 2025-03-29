from collections import Counter


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        moduloVal = Counter(val % k for val in arr)
        for val in moduloVal:
            if val and moduloVal[val] != moduloVal[k - val]:
                return False

        return moduloVal[0] % 2 == 0


newCan = Solution()
print(newCan.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))
