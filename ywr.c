#include <stdio.h>

int main()

{

    int arr[] = {4, 3, 6, 7, 1, 3};
    int arrSize = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < arrSize; i++)
    {
        int max = arr[i];
        for (int j = i + 1; j < arrSize; j++)
        {
            if (arr[j] > max)
                max = arr[j];
        }
        arr[i] = max;
    }

    for (int i = 0; i < arrSize; i++)
        printf("%d ", arr[i]);

    return 0;
}
