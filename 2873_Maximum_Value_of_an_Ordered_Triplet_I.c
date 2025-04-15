#include <stdio.h>

long long maximumTripletValue(int *nums, int numsSize)
{
    long long max = 0;
    int rightMax[numsSize];
    rightMax[numsSize - 1] = nums[numsSize - 1];

    for (int i = numsSize - 2; i >= 0; i--)
    {
        rightMax[i] = nums[i] > rightMax[i + 1] ? nums[i] : rightMax[i + 1];
    }

    for (int i = 0; i < numsSize - 2; i++)
    {
        for (int j = i + 1; j < numsSize - 1; j++)
        {
            long long currMax = (long long)(nums[i] - nums[j]) * rightMax[j + 1];
            if (max < currMax)
                max = currMax;
        }
    }

    return max;
}

int main()

{
    int nums[] = {12, 6, 1, 2, 7};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    // maximumTripletValue(nums, numsSize);

    int res = maximumTripletValue(nums, numsSize);
    printf("%d", res);

    return 0;
}