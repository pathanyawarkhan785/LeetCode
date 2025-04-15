#include <stdio.h>
#include <stdbool.h>

int countPrimes(int n)
{
    if (n < 2 || n > 5000000)
        return 0;

    bool sieve[n + 1];

    for (int i = 0; i <= n; i++)
        sieve[i] = true;

    sieve[0] = sieve[1] = false;

    for (int i = 2; i * i <= n; i++)
    {
        if (sieve[i])
        {
            for (int j = i * i; j <= n; j += i)
                sieve[j] = false;
        }
    }

    int count = 0;
    for (int i = 2; i < n; i++)
    {
        if (sieve[i])
            count++;
    }

    return count;
}

int main()
{

    int res = countPrimes(10);
    printf("%d", res);

    return 0;
}
