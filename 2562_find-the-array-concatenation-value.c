#include <stdio.h>
#include <string.h>
#include <stdlib.h>

long long findTheArrayConcVal(int *nums, int numsSize)
{
    int left = 0;
    int right = numsSize - 1;
    long long concatVal = 0;

    while (left < right)
    {
        char str1[10], str2[10];
        sprintf(str1, "%d", nums[left]);
        sprintf(str2, "%d", nums[right]);

        char result[20];
        strcpy(result, str1);
        strcat(result, str2);

        concatVal += atoi(result);

        left++;
        right--;
    }

    if (left == right)
        concatVal += nums[left];

    return concatVal;
}

int main()

{
    int nums[] = {5, 14, 13, 8, 12};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int res = findTheArrayConcVal(nums, numsSize);
    printf("%d", res);

    return 0;
}