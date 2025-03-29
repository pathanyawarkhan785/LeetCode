class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            ind = abs(num) - 1
            nums[ind] = -abs(nums[ind])

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res


newFind = Solution()
print(newFind.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
