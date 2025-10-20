#include <stdio.h>

int finalValueAfterOperations(char **operations, int operationsSize)
{
    int X = 0;
    for (int i = 0; i < operationsSize; i++)
        operations[i][1] == '-' ? X-- : X++;

    return X;
}

int main()

{
    char *operations[] = {"X++", "++X", "--X", "X--"};
    int operationsSize = sizeof(operations) / sizeof(operations[0]);

    int X = finalValueAfterOperations(operations, operationsSize);
    printf("%d", X);

    return 0;
}
