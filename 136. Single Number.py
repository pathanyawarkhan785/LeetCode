class Solution:
    def singleNumber(self, nums):
        temp = set(nums)
        for val in temp:
            if nums.count(val) == 1:
                return val

        # for val in nums:
        #     if nums.count(val) == 1:
        #         return val


newsingleNumber = Solution()
print(newsingleNumber.singleNumber([1, 2, 4, 1, 2]))
