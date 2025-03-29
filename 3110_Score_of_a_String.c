#include <stdio.h>
#include <stdlib.h>

int scoreOfString(char *s)
{
    int i = 0, ans = 0;

    while (s[i + 1] != '\0')
    {
        ans += abs(s[i] - s[i + 1]);
        i++;
    }

    return ans;
}

int main()

{
    char s[6] = "zaz";
    int res = scoreOfString(s);
    printf("%d", res);

    return 0;
}