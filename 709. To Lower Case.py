class Solution:
    def toLowerCase(self, s: str) -> str:
        if s != s.lower():
            return s.lower()
        return s


newToLower = Solution()
print(newToLower.toLowerCase("here"))
