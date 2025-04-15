#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool isValid(char *s)
{
    int n = strlen(s);
    char *stack = (char *)malloc(sizeof(char) * n);
    int top = -1;

    for (int i = 0; i < n; i++)
    {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
            stack[++top] = s[i];

        else
        {

            if (top == -1)
            {
                free(stack);
                return false;
            }

            char open = stack[top--];

            if ((s[i] == ')' && open != '(') ||
                (s[i] == '}' && open != '{') ||
                (s[i] == ']' && open != '['))
            {
                free(stack);
                return false;
            }
        }
    }

    free(stack);
    return top == -1;
}

int main()

{
    char s[] = "()";

    int res = isValid(s);
    printf("%d", res);

    return 0;
}