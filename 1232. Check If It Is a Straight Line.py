class Solution:
    def checkStraightLine(self, coordinates):
        for i in range(1, len(coordinates)):

            print(coordinates[i][0] - coordinates[i - 1][0])
            print(coordinates[i][1] - coordinates[i - 1][1])

            # break


newCheck = Solution()
newCheck.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
