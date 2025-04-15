#include <stdio.h>
#include <stdlib.h>

int countGoodTriplets(int *arr, int arrSize, int a, int b, int c)
{
    int count = 0;

    for (int j = 1; j < arrSize - 1; j++)
    {
        for (int k = j + 1; k < arrSize; k++)
        {
            if (abs(arr[j] - arr[k]) <= b)
            {
                for (int i = 0; i < j; i++)
                {
                    if (abs(arr[i] - arr[j]) <= a && abs(arr[i] - arr[k]) <= c)
                        count++;
                }
            }
        }
    }

    return count;
}

int main()

{
    int arr[] = {3, 0, 1, 1, 9, 7};
    int arrSize = sizeof(arr) / sizeof(arr[0]);
    int a = 7;
    int b = 2;
    int c = 3;

    int res = countGoodTriplets(arr, arrSize, a, b, c);
    printf("%d", res);

    return 0;
}