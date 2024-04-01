class Solution:
    def mySqrt(self, x):
        sqrt = x / 2
        temp = 0
        while sqrt != temp:
            temp = sqrt
            sqrt = ((x / temp) + temp) / 2
        return int(sqrt)


newMySqrt = Solution()
print(newMySqrt.mySqrt(35))
