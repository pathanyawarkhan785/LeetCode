#include <stdio.h>
#include <stdbool.h>

bool isMonotonic(int *nums, int numsSize)
{
    bool increasing = true;
    bool decreasing = true;

    for (int i = 0; i < numsSize - 1; i++)
    {
        if (nums[i] > nums[i + 1])
            increasing = false;

        if (nums[i] < nums[i + 1])
            decreasing = false;
    }

    return increasing || decreasing;
}

int main()

{
    int nums[] = {1, 2, 2, 3};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int res = isMonotonic(nums, numsSize);
    printf("%d", res);

    return 0;
}