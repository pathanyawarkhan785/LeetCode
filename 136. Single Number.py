class Solution:
    def singleNumber(self, nums):

        # method 1

        # temp = set(nums)
        # for val in temp:
        #     if nums.count(val) == 1:
        #         return val

        # method 2

        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res


newsingleNumber = Solution()
print(newsingleNumber.singleNumber([1, 2, 4, 1, 2]))
