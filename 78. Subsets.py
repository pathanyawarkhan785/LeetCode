# class Solution:
#     def subsets(self, nums):
#         nums.sort()
#         newArr = [[], nums]
#         if len(nums) <= 1:
#             return newArr
#         for i in range(len(nums)):
#             for j in range(i):
#                 if [nums[j], nums[i]] not in newArr:
#                     newArr.append([nums[j], nums[i]])
#             newArr.append([nums[i]])

#         return newArr


# newSubSets = Solution()
# print(newSubSets.subsets([3, 2, 4, 1]))

# # [[],[1,2,3,4],[1],[1,2],[2],[1,3],[2,3],[3],[1,4],[2,4],[3,4],[4]]
# # [[],[3],[2],[2,3],[4],[3,4],[2,4],[2,3,4],[1],[1,3],[1,2],[1,2,3],[1,4],[1,3,4],[1,2,4],[1,2,3,4]]


# class Solution:
#     def subsets(self, nums):
#         nums.sort()
#         n = len(nums)
#         result = []
#         for i in range(1 << n):
#             subset = []
#             for j in range(n):
#                 if i & (1 << j):
#                     subset.append(nums[j])
#             result.append(subset)
#         return result


# newSubSets = Solution()
# print(newSubSets.subsets([3, 2, 4, 1]))
