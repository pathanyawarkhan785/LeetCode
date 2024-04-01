import math


class Solution:
    def productExceptSelf(self, nums):
        newList = []
        product = math.prod(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                newList.append(int(math.prod(nums)))
                nums.insert(i, 0)
            else:
                newList.append(int(product / nums[i]))
        return newList


newProduct = Solution()
print(newProduct.productExceptSelf([-1, 1, 0, -3, 3]))
