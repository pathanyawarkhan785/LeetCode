#include <stdio.h>
#include <string.h>

char findTheDifference(char *s, char *t)
{
    char ans = 0;

    for (int i = 0; t[i]; i++)
        ans = ans ^ t[i] ^ s[i];

    return ans;
}

int main()

{
    char s[] = "abcd";
    char t[] = "ebcad";

    char res = findTheDifference(s, t);
    printf("%c", res);

    return 0;
}