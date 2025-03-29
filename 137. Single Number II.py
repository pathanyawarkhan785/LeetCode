from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        # method 1 counter
        nums = Counter(nums)
        for i, j in nums.items():
            if j == 1:
                return i

        # method 2 bit manipulation
        one = 0
        two = 0
        for num in nums:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one
        return one


newSingle = Solution()
print(newSingle.singleNumber([2, 2, 3, 2]))
