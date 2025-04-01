#include <stdio.h>
#include <stdlib.h>

void insertHeap(int *heap, int *size, int value)
{
    heap[(*size)++] = value;
    int i = *size - 1;
    while (i > 0 && heap[i] < heap[(i - 1) / 2])
    {
        int temp = heap[i];
        heap[i] = heap[(i - 1) / 2];
        heap[(i - 1) / 2] = temp;
        i = (i - 1) / 2;
    }
}

int removeMin(int *heap, int *size)
{
    int min = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (i * 2 + 1 < *size)
    {
        int smallest = i * 2 + 1;

        if (smallest + 1 < *size && heap[smallest + 1] < heap[smallest])
            smallest++;

        if (heap[i] > heap[smallest])
        {
            int temp = heap[i];
            heap[i] = heap[smallest];
            heap[smallest] = temp;
            i = smallest;
        }
        else
            break;
    }
    return min;
}

int furthestBuilding(int *heights, int heightsSize, int bricks, int ladders)
{
    int heap[heightsSize];
    int heapSize = 0;

    for (int i = 0; i < heightsSize - 1; i++)
    {
        int diff = heights[i + 1] - heights[i];
        if (diff > 0)
        {
            insertHeap(heap, &heapSize, diff);

            if (heapSize > ladders)
            {
                bricks -= removeMin(heap, &heapSize);
                if (bricks < 0)
                    return i;
            }
        }
    }
    return heightsSize - 1;
}

int main()
{
    int heights[] = {1, 5, 1, 2, 3, 4, 10000};
    int heightsSize = sizeof(heights) / sizeof(heights[0]);
    int bricks = 4;
    int ladders = 1;

    int res = furthestBuilding(heights, heightsSize, bricks, ladders);
    printf("%d\n", res);

    return 0;
}