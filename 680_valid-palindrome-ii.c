#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isPalindrome(char *s, int start, int end)
{
    while (start < end)
    {
        if (s[start] != s[end])
            return false;
        start++;
        end--;
    }
    return true;
}

bool validPalindrome(char *s)
{
    int start = 0;
    int end = strlen(s) - 1;

    while (start < end)
    {
        if (s[start] != s[end])
            return isPalindrome(s, start + 1, end) || isPalindrome(s, start, end - 1);

        start++;
        end--;
    }

    return true;
}

int main()

{
    char s[] = "aba";

    int res = validPalindrome(s);
    printf("%d", res);

    return 0;
}