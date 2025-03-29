class Solution:
    def findDifference(self, nums1, nums2):

        # method 1

        # nums1 = set(nums1)
        # nums2 = set(nums2)
        # return [list(nums1 - nums2), list((nums2) - (nums1))]

        # method 2

        # return [list(set(nums1) - set(nums2)), list((set(nums2)) - (set(nums1)))]

        # method 3

        nums1Set = set(nums1)
        nums2Set = set(nums2)

        diff1, diff2 = set(), set()

        for i in nums1:
            if i not in nums2Set:
                diff1.add(i)

        for i in nums2:
            if i not in nums1Set:
                diff2.add(i)

        return [list(diff1), list(diff2)]


newFind = Solution()
print(newFind.findDifference([1, 2, 3], [2, 4, 6]))
