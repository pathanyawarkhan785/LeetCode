class Solution:
    def sortColors(self, nums):
        count = [0, 0, 0]

        for colour in nums:
            count[colour] += 1

        r, w, b = count

        nums[:r] = [0] * r
        nums[r : r + w] = [1] * w
        nums[r + w :] = [2] * b

        return nums


newSortColors = Solution()
print(newSortColors.sortColors([2, 0, 2, 1, 1, 0]))
