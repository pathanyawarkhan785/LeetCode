#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool hasSameDigits(char *s)
{
    while (strlen(s) > 2)
    {
        int len = strlen(s);
        char *newS = (char *)malloc((len) * sizeof(char));
        int j = 0;

        for (int i = 0; i < len - 1; i++)
        {
            int newDigit = ((s[i] - '0') + (s[i + 1] - '0')) % 10;
            newS[j++] = newDigit + '0';
        }

        newS[j] = '\0';

        strcpy(s, newS);
        free(newS);
    }

    return s[0] == s[1];
}

int main()
{
    char s[6] = "34789";
    int res = hasSameDigits(s);

    res ? printf("true\n") : printf("false\n");

    return 0;
}