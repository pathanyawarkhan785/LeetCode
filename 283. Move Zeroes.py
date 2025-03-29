class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(nums)

        if len(nums) == 1:
            return nums

        for val in nums:
            if val == 0:
                nums.remove(0)
                nums.append(0)
        # print(nums)
        return nums


newMoves = Solution()
print(newMoves.moveZeroes([0, 1, 0, 3, 12]))
