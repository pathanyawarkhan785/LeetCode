#include <stdio.h>
#include <stdlib.h>

int *findArray(int *pref, int prefSize, int *returnSize)
{
    int *newArr = (int *)malloc(prefSize * sizeof(int));

    if (newArr == NULL)
    {
        printf("Memory allocation failed.");
        exit(1);
    }

    newArr[0] = pref[0];

    for (int i = 1; i < prefSize; i++)
        newArr[i] = pref[i] ^ pref[i - 1];

    *returnSize = prefSize;
    return newArr;
}

int main()

{
    int pref[5] = {5, 2, 0, 3, 1};
    int prefSize = sizeof(pref) / sizeof(pref[0]);
    int returnSize;

    int *res = findArray(pref, prefSize, &returnSize);

    for (int i = 0; i < returnSize; i++)
        printf("%d ", res[i]);

    free(res);

    return 0;
}