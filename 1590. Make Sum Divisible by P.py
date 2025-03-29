class Solution:
    def minSubarray(self, nums, p):
        sumOfNums = sum(nums)
        lenOfNums = len(nums)

        if sumOfNums % p == 0:
            print("already divisible")
            return

        for i in range(lenOfNums):
            if sumOfNums - nums[i] % 6 == 0:
                print(nums[i])

        # print(sumOfNums)
        # print(nums, p)


newMin = Solution()
newMin.minSubarray([3, 1, 4, 2], 6)
