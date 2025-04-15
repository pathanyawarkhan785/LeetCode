#include <stdio.h>
#include <stdlib.h>

int *lastVisitedIntegers(int *nums, int numsSize, int *returnSize)
{
    int *seen = (int *)malloc(sizeof(int) * numsSize);
    int *ans = (int *)malloc(sizeof(int) * numsSize);
    int seenSize = 0;
    int k = 0;
    int consecutiveNegOnes = 0;

    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] > -1)
        {

            seen[seenSize++] = nums[i];
            consecutiveNegOnes = 0;
        }
        else
        {
            consecutiveNegOnes++;

            if (consecutiveNegOnes <= seenSize)
                ans[k++] = seen[seenSize - consecutiveNegOnes];

            else
                ans[k++] = -1;
        }
    }

    *returnSize = k;
    free(seen);
    return ans;
}

int main()

{
    int nums[] = {1, 2, -1, -1, -1};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;

    int *res = lastVisitedIntegers(nums, numsSize, &returnSize);

    for (int i = 0; i < returnSize; i++)
        printf("%d ", res[i]);

    return 0;
}