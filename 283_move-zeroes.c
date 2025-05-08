#include <stdio.h>

void moveZeroes(int *nums, int numsSize)
{
    int nonZero = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] != 0)
        {
            nums[nonZero] = nums[i];
            nonZero++;
        }
    }

    for (int i = nonZero; i < numsSize; i++)
        nums[i] = 0;
}

int main()

{
    int nums[] = {0, 1, 0, 3, 12};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    moveZeroes(nums, numsSize);

    for (int i = 0; i < numsSize; i++)
        printf("%d ", nums[i]);

    return 0;
}