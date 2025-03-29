class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        if not prices:
            return 0

        low = prices[0]
        max_profit = 0

        for price in prices:

            if price < low:
                low = price
            current_profit = price - low

            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit


newMax = Solution()
print(newMax.maxProfit([2, 4, 1]))
