class Solution:
    def majorityElement(self, nums):
        ans = None
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            count += 1 if num == ans else -1

        return ans


newElem = Solution()
print(newElem.majorityElement([3, 2, 3]))
