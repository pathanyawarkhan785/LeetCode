#include <stdio.h>
#include <stdlib.h>

int *evenOddBit(int n, int *returnSize)
{
    int *arr = (int *)malloc(sizeof(int) * 2);
    arr[0] = 0;
    arr[1] = 0;

    for (int i = 0; i < 10; i += 2)
    {
        if ((n >> i) & 1 == 1)
            arr[0]++;
        if ((n >> i + 1) & 1 == 1)
            arr[1]++;
    }

    *returnSize = 2;

    return arr;
}

int main()

{
    int returnSize;
    int *res = evenOddBit(50, &returnSize);

    printf("%d\n", res[0]);
    printf("%d\n", res[1]);

    return 0;
}