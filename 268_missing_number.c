#include <stdio.h>

int missingNumber(int *nums, int numsSize)
{
    int xorAll = 0;
    int xorNums = 0;

    for (int i = 0; i <= numsSize; i++)
        xorAll ^= i;

    for (int i = 0; i < numsSize; i++)
        xorNums ^= nums[i];

    return xorAll ^ xorNums;
}

int main()

{
    int nums[3] = {3, 0, 1};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int res = missingNumber(nums, numsSize);
    printf("%d", res);

    return 0;
}
