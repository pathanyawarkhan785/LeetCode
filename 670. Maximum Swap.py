class Solution:
    def maximumSwap(self, num):
        num = list(str(num))
        num.sort(reverse=True)
        print(num)


newMaximumGap = Solution()
newMaximumGap.maximumSwap(2736)
