class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefixSum = 0
        prefixSumCounts = {0: 1}

        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixSumCounts:
                count += prefixSumCounts[prefixSum - k]
            if prefixSum in prefixSumCounts:
                prefixSumCounts[prefixSum] += 1
            else:
                prefixSumCounts[prefixSum] = 1

        return count


newSubarray = Solution()
print(newSubarray.subarraySum([1, 1, 1], 2))
