#include <stdio.h>

int countOperations(int num1, int num2)
{
    int count = 0;

    while (num1 != 0 && num2 != 0)
    {
        if (num1 < num2)
            num2 -= num1;
        else
            num1 -= num2;

        count++;
    }

    return count;
}

int main()

{

    int res = countOperations(2, 3);
    printf("%d", res);

    return 0;
}