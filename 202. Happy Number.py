import math


class Solution:
    def isHappy(self, n):
        n = str(n)
        for i in range(0, len(n)):
            while i < len(n) - 1:
                temp = int(n[i]) * int(n[i]) + int(n[i + 1]) * int(n[i + 1])
                print(temp)
                if temp != 1:
                    print("inside if")
                    n = int(n[i]) * int(n[i]) + int(n[i + 1]) * int(n[i + 1])
                    print(temp, "new temp")
                else:
                    return


newIsHappy = Solution()
newIsHappy.isHappy(19)
