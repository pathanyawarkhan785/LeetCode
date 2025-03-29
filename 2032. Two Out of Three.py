class Solution:
    def twoOutOfThree(
        self, nums1: list[int], nums2: list[int], nums3: list[int]
    ) -> list[int]:

        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        return list(nums1 & nums2 | nums2 & nums3 | nums3 & nums1)


newTwo = Solution()
print(newTwo.twoOutOfThree([3, 1], [2, 3], [1, 2]))
