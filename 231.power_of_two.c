#include <stdio.h>
#include <stdbool.h>

bool isPowerOfTwo(int n)
{
    if (n <= 0)
        return false;

    return (n & (n - 1)) == 0;
}

int main()

{
    printf("%d", isPowerOfTwo(9));
    return 0;
}
