#include <stdio.h>

int subsetXORSum(int *nums, int numsSize)
{
    int target = 0;

    for (int i = 0; i < numsSize; i++)
        target |= nums[i];

    return target << (numsSize - 1);
}

int main()

{
    int nums[] = {1, 3};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int res = subsetXORSum(nums, numsSize);
    printf("%d", res);

    return 0;
}