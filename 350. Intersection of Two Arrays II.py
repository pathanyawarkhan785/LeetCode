class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        nums1 = set(nums1)
        newNums = nums1.intersection(nums2)
        print(newNums)


newIntersect = Solution()
newIntersect.intersect([1, 2, 2, 1], [2, 2])
