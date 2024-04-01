class Solution:
    def getCommon(self, nums1, nums2):
        if set(nums1).intersection(set(nums2)) == set():
            return -1
        return min(set(nums1).intersection(set(nums2)))


newGetCommon = Solution()
print(newGetCommon.getCommon([1, 2, 3, 4], [24, 41]))
