class Solution:
    def maximumWealth(self, accounts):
        maxWealth = [sum(accounts[i]) for i in range(0, len(accounts))]
        return max(maxWealth)


newMaximum = Solution()
print(newMaximum.maximumWealth([[1, 5], [7, 3], [3, 5]]))
