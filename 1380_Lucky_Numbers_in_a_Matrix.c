#include <stdio.h>
#include <stdlib.h>

int *luckyNumbers(int **matrix, int matrixSize, int *matrixColSize, int *returnSize)
{
    int *result = malloc(matrixSize * sizeof(int));
    *returnSize = 0;

    for (int i = 0; i < matrixSize; i++)
    {
        int minVal = matrix[i][0];
        int minCol = 0;

        for (int j = 1; j < *matrixColSize; j++)
        {
            if (matrix[i][j] < minVal)
            {
                minVal = matrix[i][j];
                minCol = j;
            }
        }

        int isLucky = 1;
        for (int k = 0; k < matrixSize; k++)
        {
            if (matrix[k][minCol] > minVal)
            {
                isLucky = 0;
                break;
            }
        }
        if (isLucky)
            result[(*returnSize)++] = minVal;
    }

    return result;
}

int main()
{
    int staticMatrix[3][3] = {{3, 7, 8}, {9, 11, 13}, {15, 16, 17}};
    int matrixSize = sizeof(staticMatrix) / sizeof(staticMatrix[0]);
    int matrixColSize = sizeof(staticMatrix[0]) / sizeof(staticMatrix[0][0]);
    int returnSize;

    int **matrix = malloc(matrixSize * sizeof(int *));
    for (int i = 0; i < matrixSize; i++)
    {
        matrix[i] = malloc(matrixColSize * sizeof(int));
        for (int j = 0; j < matrixColSize; j++)
            matrix[i][j] = staticMatrix[i][j];
    }

    int *res = luckyNumbers(matrix, matrixSize, &matrixColSize, &returnSize);
    printf("%d", *res);

    for (int i = 0; i < matrixSize; i++)
        free(matrix[i]);

    free(matrix);

    return 0;
}