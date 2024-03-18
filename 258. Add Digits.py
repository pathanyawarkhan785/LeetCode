class Solution:
    def addDigits(self, num):
        if num < 10:
            return num
        while num > 9:
            num = sum(list(map(int, str(num))))
        return num


newAddDigits = Solution()
print(newAddDigits.addDigits(38))
