#include <stdio.h>

int totalHammingDistance(int *nums, int numsSize)
{
    int totalCount = 0;
    for (int bit = 0; bit < 31; bit++)
    {
        unsigned int mask = 1U << bit;
        int ones = 0, zeros = 0;

        for (int i = 0; i < numsSize; i++)
        {
            if (nums[i] & mask)
                ones++;
            else
                zeros++;
        }
        totalCount += ones * zeros;
    }
    return totalCount;
}

int main()

{
    int nums[] = {1337, 7331};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int res = totalHammingDistance(nums, numsSize);
    printf("%d", res);

    return 0;
}