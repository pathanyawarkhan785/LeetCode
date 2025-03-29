#include <stdio.h>
#include <stdlib.h>

char *convertToBase7(int num)
{
    if (num == 0)
    {
        char *result = malloc(2 * sizeof(char));
        result[0] = '0';
        result[1] = '\0';
        return result;
    }

    int absNum = abs(num);
    char buffer[100];
    int i = 0;

    while (absNum != 0)
    {
        buffer[i++] = (absNum % 7) + '0';
        absNum /= 7;
    }

    if (num < 0)
        buffer[i++] = '-';

    buffer[i] = '\0';

    int len = i;
    char *result = malloc((len + 1) * sizeof(char));

    for (int j = 0; j < len; j++)
        result[j] = buffer[len - 1 - j];

    result[len] = '\0';

    return result;
}

int main()
{
    int num = 100;
    char *base7 = convertToBase7(num);
    printf("%s\n", base7);
    free(base7);
    return 0;
}
