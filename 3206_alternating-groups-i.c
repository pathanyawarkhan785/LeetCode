#include <stdio.h>

int numberOfAlternatingGroups(int *colors, int colorsSize)
{
    int count = 0;

    for (int i = 0; i < colorsSize; i++)
    {
        int second = (i + 1) % colorsSize;
        int third = (i + 2) % colorsSize;

        if (colors[i] != colors[second] && colors[second] != colors[third])
            count++;
    }

    return count;
}

int main()

{
    int colors[] = {0, 1, 0, 0, 1};
    int colorsSize = sizeof(colors) / sizeof(colors[0]);

    int res = numberOfAlternatingGroups(colors, colorsSize);
    printf("%d", res);

    return 0;
}
