#include <stdio.h>

int hammingWeight(int n)
{
    int count = 0;
    while (n != 0)
    {
        if (n & 1 == 1)
            count++;
        n = n >> 1;
    }
    return count;
}

int main()
{
    int oneBit = hammingWeight(11);
    printf("%d", oneBit);

    return 0;
}