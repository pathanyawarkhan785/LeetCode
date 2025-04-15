#include <stdio.h>
#include <stdbool.h>

void delThreeElem(int *nums, int *numsSize)
{
    int removeCount = (*numsSize < 3) ? *numsSize : 3;
    for (int i = removeCount; i < *numsSize; i++)
    {
        nums[i - removeCount] = nums[i];
    }

    *numsSize -= removeCount;
}

bool isDistinct(int *nums, int numsSize)
{
    for (int i = 0; i < numsSize; i++)
    {
        for (int j = i + 1; j < numsSize; j++)
        {
            if (nums[i] == nums[j])
                return false;
        }
    }
    return true;
}

int minimumOperations(int *nums, int numsSize)
{

    int count = 0;

    while (!isDistinct(nums, numsSize) && numsSize > 0)
    {
        delThreeElem(nums, &numsSize);
        count++;
    }

    return count;
}

int main()

{
    int nums[] = {1, 2, 3, 4, 2, 3, 3, 5, 7};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int res = minimumOperations(nums, numsSize);
    printf("%d", res);

    return 0;
}