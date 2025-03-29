import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        res = math.log(n, 4)
        return res.is_integer()


newIsPower = Solution()
print(newIsPower.isPowerOfFour(1))
