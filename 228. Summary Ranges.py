class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        temp = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start != nums[i]:
                temp.append(f"{str(start)}->{str(nums[i])}")
            else:
                temp.append(str(start))

            i += 1

        return temp


newSummary = Solution()
print(newSummary.summaryRanges([0, 1, 2, 4, 5, 7]))
