#include <stdio.h>
#include <stdbool.h>

bool isPowerOfFour(int n)
{
    if (n <= 0)
        return false;

    return (n & (n - 1)) == 0 && (n - 1) % 3 == 0;
}

int main()

{
    int res = isPowerOfFour(16);
    printf("%d", res);
    return 0;
}