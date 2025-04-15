#include <stdio.h>

char *fractionToDecimal(int numerator, int denominator)
{
    double ans = (double)(numerator) / (double)(denominator);
    printf("%f", ans);
}

int main()

{
    fractionToDecimal(1, 2);
    return 0;
}