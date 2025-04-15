#include <stdio.h>
#include <string.h>

int countSymmetricIntegers(int low, int high)
{
    int count = 0;

    for (int i = low; i <= high; i++)
    {
        char str[20];
        sprintf(str, "%d", i);
        int len = strlen(str);

        if (len % 2)
            continue;

        int sumFirstHalf = 0, sumSecondHalf = 0;
        int mid = len / 2;

        for (int j = 0; j < mid; j++)
        {
            sumFirstHalf += str[j] - '0';
            sumSecondHalf += str[mid + j] - '0';
        }

        if (sumFirstHalf == sumSecondHalf)
            count++;
    }

    return count;
}

int main()

{
    int res = countSymmetricIntegers(1200, 1230);
    printf("%d", res);
    return 0;
}