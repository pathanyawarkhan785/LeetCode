# nums = [3, 2, 3]
# target = 6


# def twoSum(nums, target):
#     for i in range(0, len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# print(twoSum(nums, target))
# # twoSum(nums, target)


class Solution:
    def twoSum(self, nums, target):
        dictionary = {}
        for i in range(len(nums)):
            if target - nums[i] in dictionary:
                return [dictionary[target - nums[i]], i]
            dictionary[nums[i]] = i

        return [-1, -1]


newTwoSum = Solution()
print(newTwoSum.twoSum([2, 9, 0, 11, 7], 9))
