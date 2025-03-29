#include <stdio.h>
#include <stdbool.h>

bool isFascinating(int n)
{
    char num[10];
    int digitCount[10] = {0};

    sprintf(num, "%d%d%d", n, n * 2, n * 3);

    for (int i = 0; i < 9; i++)
    {
        int digit = num[i] - '0';

        if (digit == 0 || digitCount[digit] > 0)
            return false;

        digitCount[digit]++;
    }
    return true;
}

int main()

{
    int res = isFascinating(192);

    res ? printf("true") : printf("false");

    return 0;
}