class Solution:
    def isSameAfterReversals(self, num):
        # print(num % 10)
        if num % 10 == 0 and num != 0:
            return False
        return True


newSame = Solution()
print(newSame.isSameAfterReversals(5026))
