class Solution:
    def numIdenticalPairs(self, nums):

        # method 1

        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] == nums[j]) and (i < j):
        #             count += 1
        # return count

        # method 2

        from collections import defaultdict

        count = 0
        freq = defaultdict(int)

        for num in nums:
            count += freq[num]
            freq[num] += 1

        return count


newNumIdentical = Solution()
print(newNumIdentical.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
