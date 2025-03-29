class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


newContainsDupl = Solution()
print(newContainsDupl.containsDuplicate([1, 2, 3, 1]))
