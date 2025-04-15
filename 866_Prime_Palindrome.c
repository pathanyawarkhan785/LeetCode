#include <stdio.h>

int isPalindrome(int num)
{
    int reversed = 0, original = num;
    while (num > 0)
    {
        reversed = reversed * 10 + num % 10;
        num /= 10;
    }
    return reversed == original;
}

int isPrime(int num)
{
    if (num <= 1)
        return 0;

    for (int i = 2; i * i <= num; i++)
    {
        if (num % i == 0)
            return 0;
    }

    return 1;
}

int primePalindrome(int n)
{
    int next = n;

    while (!isPrime(next) || !isPalindrome(next))
        next++;

    return next;
}

int main()

{
    int res = primePalindrome(2);
    printf("%d", res);
    return 0;
}