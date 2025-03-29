class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        res = []
        streak = 0

        for i in range(n):
            if i == 0 or nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1

            if i + 1 >= k:
                if streak >= k:
                    res.append(max(nums[i - k + 1 : i + 1]))
                else:
                    res.append(-1)

        return res


newResult = Solution()
print(newResult.resultsArray([1, 2, 3, 4, 3, 2, 5], 3))
