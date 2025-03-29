class Solution:
    def findNumbers(self, nums):
        count = 0
        for val in nums:
            val = str(val)
            if len(val) % 2 == 0:
                count += 1

        return count


newFind = Solution()
print(newFind.findNumbers([12, 345, 2, 6, 7896]))
