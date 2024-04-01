class Solution:
    def intersection(self, nums1, nums2):
        # return list(set([nums1[i] for i in range(len(nums1)) if nums1[i] in nums2]))
        return {*nums1} & {*nums2}


newIntersection = Solution()
print(newIntersection.intersection([1, 2, 2, 1], [2, 2]))
