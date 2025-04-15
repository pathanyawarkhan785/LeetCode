#include <stdio.h>
#include <stdbool.h>

bool searchMatrix(int **matrix, int matrixSize, int *matrixColSize, int target)
{
    // int start = m
    printf("%d", matrix[0][0]);
    // [(6 - (6 % 4)) / 4][6 % 4]
}

int main()
{
    int mat1[4] = {1, 3, 5, 7};
    int mat2[4] = {10, 11, 16, 20};
    int mat3[4] = {23, 30, 34, 60};

    int *matrix[3] = {mat1, mat2, mat3};
    int matrixSize = sizeof(matrix) / sizeof(matrix[0]);
    int matrixColSize = sizeof(mat1) / sizeof(mat1[0]);
    int target = 3;

    searchMatrix(matrix, matrixSize, &matrixColSize, target);

    return 0;
}