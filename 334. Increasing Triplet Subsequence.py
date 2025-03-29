class Solution:
    def increasingTriplet(self, nums):

        if len(nums) < 3:
            return False

        num1 = num2 = float("inf")

        for i in nums:
            # print(i)
            if i > num2:
                return True
            if i <= num1:
                num1 = i
            elif i <= num2:
                num2 = i

        # print(num1)
        # print(num2)

        return False


newIncreasing = Solution()
print(newIncreasing.increasingTriplet([20, 100, 10, 12, 5, 13]))
