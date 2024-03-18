class Solution:
    def addDigits(self, num):
        i = 0
        while num > 10:
            num = str(num)
            num = int(num[i]) + (int(num[i + 1]))
        return num, type(num)


newAddDigits = Solution()