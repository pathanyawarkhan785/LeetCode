#include <stdio.h>

int rangeBitwiseAnd(int left, int right)
{
    int count = 0;
    while (left < right)
    {
        left >>= 1;
        right >>= 1;
        count++;
    }
    return left << count;
}

int main()

{

    int res = rangeBitwiseAnd(5, 7);
    printf("%d", res);

    return 0;
}

// 1 0 -> 2
// 1 1 -> 3
// 1

// 1 -> 1
// 1 -> 1
// 2

// 1 << 2 = 4