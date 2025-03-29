class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key=lambda x: (bin(x).count("1"), x))
        return arr


newSort = Solution()
print(newSort.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
