import math


class Solution:
    def divide(self, dividend, divisor):
        if divisor >= 2147483648:
            return 2147483647
        elif divisor <= -2147483647:
            return -2147483647
        elif divisor < 0:
            divisor = math.pow(divisor, 2)
            divisor = math.sqrt(divisor)
            divisor = math.floor(dividend / divisor)
            return -divisor
        return math.floor(dividend / divisor)


newDivide = Solution()
print(newDivide.divide(-2147483648, -1))
