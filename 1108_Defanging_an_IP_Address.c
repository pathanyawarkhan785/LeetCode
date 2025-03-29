#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *defangIPaddr(char *address)
{
    int len = strlen(address);

    char *defanged = malloc((len + 6 + 1) * sizeof(char));
    int j = 0;

    for (int i = 0; i < len; i++)
    {
        if (address[i] == '.')
        {
            defanged[j++] = '[';
            defanged[j++] = '.';
            defanged[j++] = ']';
        }
        else
        {
            defanged[j++] = address[i];
        }
    }
    defanged[j] = '\0';

    return defanged;
}

int main()
{
    char arr[20] = "1.1.1.1";
    char *result = defangIPaddr(arr);

    printf("%s\n", result);

    free(result);

    return 0;
}
