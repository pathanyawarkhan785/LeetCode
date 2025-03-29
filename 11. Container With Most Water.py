class Solution:
    def maxArea(self, height):
        lenHeight = len(height)
        start = 0
        end = lenHeight - 1
        maxArea = 0

        while start < end:
            weight = end - start
            distance = min(height[start], height[end])
            area = weight * distance
            maxArea = max(maxArea, area)
            # print(area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        # print(height)
        # print(maxArea)

        return maxArea


newMax = Solution()
print(newMax.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
