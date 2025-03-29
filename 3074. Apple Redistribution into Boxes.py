class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:

        capacity.sort(reverse=True)
        appleSum = sum(apple)

        for j, i in enumerate(capacity):
            appleSum -= i
            if appleSum <= 0:
                return j + 1


newMinimum = Solution()
print(newMinimum.minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2]))
