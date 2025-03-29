#include <stdio.h>
#include <stdlib.h>

int **generate(int numRows, int *returnSize, int **returnColumnSizes)
{
    *returnColumnSizes = (int *)malloc(numRows * sizeof(int));

    int **pascalTriangle = (int **)malloc(numRows * sizeof(int *));

    for (int i = 0; i < numRows; i++)
    {
        (*returnColumnSizes)[i] = i + 1;

        pascalTriangle[i] = (int *)malloc((i + 1) * sizeof(int));

        pascalTriangle[i][0] = 1;
        pascalTriangle[i][i] = 1;

        for (int j = 1; j < i; j++)
        {
            pascalTriangle[i][j] = pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j];
        }
    }

    *returnSize = numRows;

    return pascalTriangle;
}

int main()
{
    int numRows;
    printf("Enter the number of rows for Pascal's Triangle: ");
    scanf("%d", &numRows);

    int returnSize;
    int *returnColumnSizes;

    int **pascalTriangle = generate(numRows, &returnSize, &returnColumnSizes);

    printf("[");
    for (int i = 0; i < returnSize; i++)
    {
        printf("[");
        for (int j = 0; j < returnColumnSizes[i]; j++)
        {
            printf("%d", pascalTriangle[i][j]);
            if (j != returnColumnSizes[i] - 1)
                printf(",");
        }
        printf("]");
        if (i != returnSize - 1)
            printf(",");
    }
    printf("]\n");

    for (int i = 0; i < returnSize; i++)
    {
        free(pascalTriangle[i]);
    }
    free(pascalTriangle);
    free(returnColumnSizes);

    return 0;
}