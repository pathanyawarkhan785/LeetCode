#include <stdio.h>

int getSum(int a, int b)
{

    while (b != 0)
    {

        unsigned int carry = a & b;

        a = a ^ b;
        b = carry << 1;
    }
    return a;
}

int main()

{
    int res = getSum(1, 2);
    printf("%d", res);

    return 0;
}