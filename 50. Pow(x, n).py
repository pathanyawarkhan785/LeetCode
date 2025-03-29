import math


class Solution:
    def myPow(self, x, n):
        return x**n
        # return math.pow(x, n)


newMyPow = Solution()
print(newMyPow.myPow(2, 3))
