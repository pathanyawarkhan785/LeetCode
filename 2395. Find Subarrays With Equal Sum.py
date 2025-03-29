class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        sums_seen = set()

        for i in range(len(nums) - 1):
            current_sum = nums[i] + nums[i + 1]
            if current_sum in sums_seen:
                return True
            sums_seen.add(current_sum)

        return False


newFind = Solution()
print(newFind.findSubarrays([4, 2, 4]))
