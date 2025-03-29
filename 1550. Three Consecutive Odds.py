class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:

        count = 0

        for i in range(len(arr)):

            if arr[i] % 2:
                count += 1
            else:
                count = 0

            if count == 3:
                return True

        return False


newThree = Solution()
print(newThree.threeConsecutiveOdds([1, 2, 1, 1]))
