import math


class Solution:
    def isHappy(self, n):
        n = str(n)
        n = list(n)
        temp = 0

        for i in range(len(n)):
            temp += int(n[i]) * int(n[i])
            if len(str(temp)) > 1:
                temp += int(n[i]) * int(n[i])
        print(temp)
        print(len(str(temp)))


newIsHappy = Solution()
newIsHappy.isHappy(124)
