from collections import defaultdict


class Solution:
    def equalPairs(self, grid):

        row_count = defaultdict(int)

        for row in grid:
            row_count[tuple(row)] += 1

        col_count = defaultdict(int)

        for col in zip(*grid):
            col_count[tuple(col)] += 1

        count = 0

        for row in row_count:
            if row in col_count:
                count += row_count[row] * col_count[row]

        return count


newEqual = Solution()
print(newEqual.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
