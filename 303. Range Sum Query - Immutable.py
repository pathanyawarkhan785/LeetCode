class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


newNum = NumArray([-2, 0, 3, -5, 2, -1])
print(newNum.sumRange(0, 2))
