#include <stdio.h>

int removeElement(int *nums, int numsSize, int val)
{
    int k = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] != val)
        {
            nums[k] = nums[i];
            k += 1;
        }
    }
    return k;
}

int main()

{
    int nums[] = {3, 2, 2, 3};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int val = 3;

    int res = removeElement(nums, numsSize, val);
    printf("%d", res);

    return 0;
}
