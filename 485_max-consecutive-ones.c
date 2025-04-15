#include <stdio.h>

int findMaxConsecutiveOnes(int *nums, int numsSize)
{
    int maxCount = 0;
    int count = 0;

    for (int i = 0; i < numsSize; i++)
        if (nums[i] == 1)
        {
            count++;

            if (count > maxCount)
                maxCount = count;
        }
        else
            count = 0;

    return maxCount;
}

int main()

{
    int nums[] = {1, 0, 1, 1, 0, 1};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int res = findMaxConsecutiveOnes(nums, numsSize);
    printf("%d", res);

    return 0;
}