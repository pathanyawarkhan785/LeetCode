class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) % 2:
            return nums1[int(len(nums1) / 2)]

        return (nums1[int(len(nums1) / 2) - 1] + nums1[int(len(nums1) / 2)]) / 2


newMedianArray = Solution()
print(newMedianArray.findMedianSortedArrays([1, 3], [2, 4]))
