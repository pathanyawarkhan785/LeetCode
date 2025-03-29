class Solution:
    def containsNearbyDuplicate(self, nums, k):
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap and abs(i - hashMap[nums[i]]) <= k:
                return True
            hashMap[nums[i]] = i
        return False


newContains = Solution()
print(newContains.containsNearbyDuplicate([1, 2, 3, 1], 3))
