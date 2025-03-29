class Solution:
    def calculate(self, s: str) -> int:
        return eval(s)


newCal = Solution()
print(newCal.calculate("1 + 1"))
