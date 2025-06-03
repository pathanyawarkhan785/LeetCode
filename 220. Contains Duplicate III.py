class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: list[int], indexDiff: int, valueDiff: int
    ) -> bool:

        if valueDiff < 0:
            return False

        hashMap = {}
        hashMapSize = valueDiff + 1

        for i, j in enumerate(nums):
            hashMapId = j // hashMapSize

            if hashMapId in hashMap:
                return True

            if (
                hashMapId - 1 in hashMap
                and abs(j - hashMap[hashMapId - 1]) <= valueDiff
            ):
                return True
            if (
                hashMapId + 1 in hashMap
                and abs(j - hashMap[hashMapId + 1]) <= valueDiff
            ):
                return True

            hashMap[hashMapId] = j

            if i >= indexDiff:
                del hashMap[nums[i - indexDiff] // hashMapSize]

        return False


newContains = Solution()
print(newContains.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
