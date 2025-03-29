#include <stdio.h>
#include <stdbool.h>

bool checkRecord(char *s)
{
    int countOfA = 0, countOfConsecutiveL = 0;

    for (int i = 0; s[i] != '\0'; i++)
    {
        if (s[i] == 'A')
        {
            countOfA++;
            if (countOfA > 1)
                return false;
        }

        if (s[i] == 'L')
        {
            countOfConsecutiveL++;
            if (countOfConsecutiveL >= 3)
                return false;
        }
        else
            countOfConsecutiveL = 0;
    }

    return true;
}

int main()
{
    char s[] = "ALL";
    printf("%d\n", checkRecord(s));
    return 0;
}