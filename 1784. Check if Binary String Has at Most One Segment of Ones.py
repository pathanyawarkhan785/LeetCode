class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s


newCheck = Solution()
print(newCheck.checkOnesSegment("1001"))
