class Solution:
    def removeTrailingZeros(self, num):
        return num.strip("0")


newRemove = Solution()
print(newRemove.removeTrailingZeros("51230100"))
