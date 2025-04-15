#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int arrayPairSum(int *nums, int numsSize)
{
    int res = 0;

    qsort(nums, numsSize, sizeof(int), cmp);

    for (int i = 0; i < numsSize; i += 2)
        res += nums[i];

    return res;
}

int main()

{
    int nums[] = {1, 4, 3, 2};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int res = arrayPairSum(nums, numsSize);
    printf("%d", res);

    return 0;
}