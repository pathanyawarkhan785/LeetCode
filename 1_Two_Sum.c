#include <stdio.h>
#include <stdlib.h>

int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    for (int i = 1; i < numsSize; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (nums[j] + nums[i] == target)
            {
                int *result = (int *)malloc(2 * sizeof(int));
                result[0] = j;
                result[1] = i;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}

int main()
{
    int nums[4] = {2, 7, 11, 15};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int target = 9;
    int returnSize;

    int *result = twoSum(nums, numsSize, target, &returnSize);
    if (result != NULL)
    {
        printf("Indices: {%d, %d}\n", result[0], result[1]);
        printf("Values: {%d, %d}\n", nums[result[0]], nums[result[1]]);
        free(result);
    }
    else
        printf("No solution found.\n");

    return 0;
}