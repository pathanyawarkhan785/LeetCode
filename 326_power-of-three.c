#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPowerOfThree(int n)
{
    if (n == 1)
        return true;

    if (n % 3 || n == 0)
        return false;

    return isPowerOfThree(n / 3);
}

int main()

{
    int res = isPowerOfThree(27);
    printf("%d", res);
    return 0;
}
