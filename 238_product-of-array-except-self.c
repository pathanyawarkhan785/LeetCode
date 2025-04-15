#include <stdio.h>
#include <stdlib.h>

int *productExceptSelf(int *nums, int numsSize, int *returnSize)
{

    int *result = (int *)malloc(numsSize * sizeof(int));
    if (!result)
        return NULL;

    *returnSize = numsSize;

    int prefix = 1;
    for (int i = 0; i < numsSize; i++)
    {
        result[i] = prefix;
        prefix *= nums[i];
    }

    int suffix = 1;
    for (int i = numsSize - 1; i >= 0; i--)
    {
        result[i] *= suffix;
        suffix *= nums[i];
    }

    return result;
}

int main()

{
    int nums[] = {1, 2, 3, 4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;

    int *res = productExceptSelf(nums, numsSize, &returnSize);

    for (int i = 0; i < returnSize; i++)
        printf("%d ", res[i]);

    return 0;
}