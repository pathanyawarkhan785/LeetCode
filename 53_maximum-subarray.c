#include <stdio.h>
#include <limits.h>

int maxSubArray(int *nums, int numsSize)
{
    int maxSum = INT_MIN;
    int currSum = 0;

    for (int i = 0; i < numsSize; i++)
    {
        currSum += nums[i];
        if (currSum > maxSum)
            maxSum = currSum;

        if (currSum < 0)
            currSum = 0;
    }

    return maxSum;
}

int main()
{
    int nums[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    printf("%d\n", maxSubArray(nums, numsSize));
    return 0;
}