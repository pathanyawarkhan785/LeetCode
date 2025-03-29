#include <stdio.h>
#include <stdlib.h>

double *convertTemperature(double celsius, int *returnSize)
{
    *returnSize = 2;
    double *arr = malloc(*returnSize * sizeof(double));

    if (arr == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }

    arr[0] = celsius + 273.15;
    arr[1] = celsius * 1.80 + 32.00;

    return arr;
}

int main()
{
    int size;
    double *res = convertTemperature(36.50, &size);

    printf("Kelvin: %f\n", res[0]);
    printf("Fahrenheit: %f\n", res[1]);

    free(res);

    return 0;
}
