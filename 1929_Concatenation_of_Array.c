#include <stdio.h>
#include <stdlib.h>

int *getConcatenation(int *nums, int numsSize, int *returnSize)
{
    int *newNums = (int *)malloc(2 * numsSize * sizeof(nums[0]));

    if (newNums == NULL)
    {
        printf("Memory allocation Failed.");
        exit(1);
    }

    for (int i = 0; i < numsSize; i++)
    {

        newNums[i] = nums[i];
        newNums[i + numsSize] = nums[i];
    }
    *returnSize = 2 * numsSize;

    return newNums;
}

int main()

{
    int nums[3] = {1, 2, 1};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;

    int *res = getConcatenation(nums, numsSize, &returnSize);

    for (int i = 0; i < returnSize; i++)
        printf("%d ", res[i]);

    free(res);

    return 0;
}
