class Solution:
    def topKFrequent(self, nums, k):
        temp = []
        i = 0
        while nums[i]:
            temp.append(max(nums, key=nums.count))
            nums.pop(nums[i])
            i += 1
            # nums.pop()


newTopK = Solution()
print(newTopK.topKFrequent([1, 2], 2))
