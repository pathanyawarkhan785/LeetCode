from collections import Counter


class Solution:
    def majorityElement(self, nums):

        n = len(nums) / 2
        nums = Counter(nums)
        print(nums)

        for val, occ in nums.items():
            if occ > n:
                return val


newElem = Solution()
print(newElem.majorityElement([3, 2, 3]))
