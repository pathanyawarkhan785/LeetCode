class Solution:
    def heightChecker(self, heights):
        count = 0
        orgHeight = heights.copy()
        heights.sort()

        for i in range(len(heights)):
            if heights[i] != orgHeight[i]:
                count = count + 1
        return count


newHeights = Solution()
print(newHeights.heightChecker([1, 1, 4, 2, 1, 3]))
