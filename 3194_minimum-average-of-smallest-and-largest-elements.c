#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) { return (*(int *)a - *(int *)b); }

double minimumAverage(int *nums, int numsSize)
{
    qsort(nums, numsSize, sizeof(int), compare);
    double *arr = (double *)malloc(sizeof(double) * (numsSize / 2));
    int right = numsSize - 1;
    int left = 0;
    while (left < right)
    {
        arr[left] = (nums[left] + nums[right]) / 2.0;
        left++;
        right--;
    }
    double result = arr[0];
    for (int i = 1; i < numsSize / 2; i++)
    {
        if (arr[i] < result)
            result = arr[i];
    }
    return result;
}

int main()

{
    int nums[] = {7, 8, 3, 4, 15, 13, 4, 1};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    double res = minimumAverage(nums, numsSize);
    printf("%f", res);

    return 0;
}