#include <stdio.h>
#include <stdlib.h>

// int minMovesToSeat(int *, int, int *, int);

int cmp(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int minMovesToSeat(int *seats, int seatsSize, int *students, int studentsSize)
{
    qsort(seats, seatsSize, sizeof(int), cmp);
    qsort(students, studentsSize, sizeof(int), cmp);
    printf("%d\n", seats[0]);
    printf("%d", students[1]);
    return 0;
}

int main()
{
    int arr1[] = {3, 1, 5};
    int arr2[] = {4, 7, 5};

    minMovesToSeat(arr1, sizeof(arr1) / sizeof(arr1[0]), arr2, sizeof(arr2) / sizeof(arr2[0]));
    return 0;
}
