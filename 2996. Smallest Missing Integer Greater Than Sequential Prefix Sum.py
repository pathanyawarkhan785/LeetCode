class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        if not nums:
            return 1

        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        missing = total

        while missing in nums:
            missing += 1

        return missing


newMissing = Solution()
print(newMissing.missingInteger([1, 2, 3, 2, 5]))
