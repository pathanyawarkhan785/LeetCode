#include <stdio.h>

int search(int *nums, int numsSize, int target)
{
    int start = 0;
    int end = numsSize - 1;

    while (start <= end)
    {
        int mid = (start + end) / 2;

        if (nums[mid] == target)
            return mid;

        if (nums[start] <= nums[mid])
        {
            if (nums[start] <= target && target < nums[mid])
                end = mid - 1;

            else
                start = mid + 1;
        }
        else
        {
            if (nums[mid] < target && target <= nums[end])
                start = mid + 1;

            else
                end = mid - 1;
        }
    }

    return -1;
}

int main()
{
    int nums[] = {4, 5, 6, 7, 0, 1, 2};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int target = 0;

    int result = search(nums, numsSize, target);

    if (result != -1)
        printf("%d\n", result);
    else
        printf("Target not found\n");

    return 0;
}