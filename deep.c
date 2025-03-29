#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct
{
    char *name;
} Person;

int main()

{

    Person p1;
    p1.name = (char *)malloc(sizeof(char));
    strcpy(p1.name, "yawar");

    Person p2 = p1;

    printf("%s\n", p1.name);
    printf("%s\n", p2.name);

    return 0;
}