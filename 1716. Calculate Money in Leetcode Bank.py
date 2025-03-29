class Solution:
    def totalMoney(self, n: int) -> int:
        bal = 0

        for i in range(n):
            bal += (i // 7) + 1 + (i % 7)

        return bal


newTotal = Solution()
print(newTotal.totalMoney(10))
