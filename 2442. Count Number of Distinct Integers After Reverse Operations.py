class Solution(object):
    def countDistinctIntegers(self, nums):
        nums = list(set(nums))
        revNums = nums[::-1]
        for val in revNums:
            val = str(val)
            nums.append(int(val[::-1]))
        return len(list(set(nums)))


newCount = Solution()
print(newCount.countDistinctIntegers([1, 13, 10, 12, 31]))
