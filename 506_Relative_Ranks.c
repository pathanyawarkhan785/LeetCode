#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char **findRelativeRanks(int *score, int scoreSize, int *returnSize)
{
    char **result = (char **)malloc(scoreSize * sizeof(char *));
    int *sortedScore = (int *)malloc(scoreSize * sizeof(int));
    memcpy(sortedScore, score, scoreSize * sizeof(int));

    for (int i = 0; i < scoreSize - 1; i++)
    {
        for (int j = i + 1; j < scoreSize; j++)
        {
            if (sortedScore[i] < sortedScore[j])
            {
                int temp = sortedScore[i];
                sortedScore[i] = sortedScore[j];
                sortedScore[j] = temp;
            }
        }
    }

    for (int i = 0; i < scoreSize; i++)
    {
        for (int j = 0; j < scoreSize; j++)
        {
            if (score[i] == sortedScore[j])
            {
                if (j == 0)
                    result[i] = strdup("Gold Medal");

                else if (j == 1)
                    result[i] = strdup("Silver Medal");

                else if (j == 2)
                    result[i] = strdup("Bronze Medal");

                else
                {
                    result[i] = (char *)malloc(12 * sizeof(char));
                    sprintf(result[i], "%d", j + 1);
                }
                break;
            }
        }
    }

    *returnSize = scoreSize;
    free(sortedScore);
    return result;
}

int main()
{
    int scores[] = {10, 3, 8, 9, 4};
    int scoreSize = 5;
    int returnSize;
    char **ranks = findRelativeRanks(scores, scoreSize, &returnSize);

    for (int i = 0; i < returnSize; i++)
    {
        printf("%s\n", ranks[i]);
        free(ranks[i]);
    }
    free(ranks);
    return 0;
}