#include <stdio.h>

int subarraySum(int *nums, int numsSize)
{
    int totalSum = 0;

    for (int i = 0; i < numsSize; i++)
    {
        int start = i - nums[i] > 0 ? i - nums[i] : 0;

        int subarraySum = 0;
        for (int j = start; j <= i; j++)
            subarraySum += nums[j];

        totalSum += subarraySum;
    }

    return totalSum;
}

int main()
{
    int nums1[] = {2, 3, 1};
    int size1 = sizeof(nums1) / sizeof(nums1[0]);

    int res = subarraySum(nums1, size1);
    printf("%d", res);

    return 0;
}