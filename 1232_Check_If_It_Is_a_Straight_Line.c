#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool checkStraightLine(int **coordinates, int coordinatesSize, int *coordinatesColSize)
{
    int x1 = coordinates[0][0];
    int y1 = coordinates[0][1];
    int x2 = coordinates[1][0];
    int y2 = coordinates[1][1];

    for (int i = 2; i < coordinatesSize; i++)
    {
        int x3 = coordinates[i][0];
        int y3 = coordinates[i][1];

        if ((x2 - x1) * (y3 - y2) != (y2 - y1) * (x3 - x2))
            return false;
    }

    return true;
}

int main()

{
    int newCoordinates[6][2] = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}};
    int coordinatesSize = sizeof(newCoordinates) / sizeof(newCoordinates[0]);
    int coordinatesColSize = sizeof(newCoordinates[0]) / sizeof(newCoordinates[0][0]);

    int **coordinates = malloc(coordinatesSize * sizeof(int));

    for (int i = 0; i < coordinatesSize; i++)
    {
        coordinates[i] = malloc(coordinatesColSize * sizeof(int));
        for (int j = 0; j < coordinatesColSize; j++)
            coordinates[i][j] = newCoordinates[i][j];
    }

    int res = checkStraightLine(coordinates, coordinatesSize, &coordinatesColSize);
    printf("%d", res);

    return 0;
}