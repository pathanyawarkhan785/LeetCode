class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums) - k]


newFind = Solution()
print(newFind.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
