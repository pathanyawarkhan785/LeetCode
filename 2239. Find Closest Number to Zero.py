class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        closest = float("inf")
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        return closest


newFind = Solution()
print(newFind.findClosestNumber([2, -1, 1]))
