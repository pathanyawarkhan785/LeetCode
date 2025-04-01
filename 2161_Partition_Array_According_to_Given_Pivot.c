#include <stdio.h>
#include <stdlib.h>

int *pivotArray(int *nums, int numsSize, int pivot, int *returnSize)
{
    int *result = (int *)malloc(numsSize * sizeof(int));
    int lessCount = 0, equalCount = 0, greaterCount = 0;

    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] < pivot)
            result[lessCount++] = nums[i];
    }
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] == pivot)
            result[lessCount + equalCount++] = nums[i];
    }
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] > pivot)
            result[lessCount + equalCount + greaterCount++] = nums[i];
    }

    *returnSize = numsSize;
    return result;
}

int main()
{
    int nums[] = {9, 12, 5, 10, 14, 3, 10};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int pivot = 10;
    int returnSize;

    int *result = pivotArray(nums, numsSize, pivot, &returnSize);

    for (int i = 0; i < returnSize; i++)
        printf("%d ", result[i]);

    free(result);

    return 0;
}