class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

        count = 0

        currSum = sum(arr[:k])
        targetSum = k * threshold

        if currSum >= targetSum:
            count += 1

        for i in range(k, len(arr)):

            currSum += arr[i] - arr[i - k]
            if currSum >= targetSum:
                count += 1

        return count


newNum = Solution()
print(
    newNum.numOfSubarrays(
        [2, 2, 2, 2, 5, 5, 5, 8],
        3,
        4,
    )
)
