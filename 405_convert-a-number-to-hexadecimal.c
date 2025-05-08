#include <stdio.h>

char out[9];

char *toHex(int num)
{
    if (num == 0)
        return "0";

    unsigned int demo = num;
    int temp = 0;
    out[8] = '\0';
    int count = 7;
    while (demo)
    {
        temp = (demo & 0x0000000F);
        if (temp <= 9)
            out[count] = '0' + temp;

        else
            out[count] = 'a' + temp - 10;

        count--;
        demo = demo >> 4;
    }
    return out + (count + 1);
}

int main()

{
    printf("%s", toHex(26));

    return 0;
}