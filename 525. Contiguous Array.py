class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length


newFindMaxLength = Solution()
print(newFindMaxLength.findMaxLength([0, 1, 0, 1]))
