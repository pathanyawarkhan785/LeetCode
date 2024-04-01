class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                # matrix[0].replace()
                # print(i, matrix[i])
                # print(i, j)
                print(matrix[i][j], matrix[i + 2][j])

        # print(matrix)


newRotate = Solution()
newRotate.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# [[7,4,1],[8,5,2],[9,6,3]]
