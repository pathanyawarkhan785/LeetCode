#include <stdio.h>

int uniqueMorseRepresentations(char **words, int wordsSize)
{
    char engAlphabet[26][5] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};

    for (int i = 0; i < wordsSize; i++)
    {
        // printf("%s ", words[i]);
        printf("%s ", engAlphabet[*words[i] - 97]);
    }

    // printf("%d", wordsSize);
    // printf("%s", words[0]);
}

int main()

{
    char words1[] = "gin";
    char words2[] = "zen";
    char words3[] = "gig";
    char words4[] = "msg";

    char *words[] = {words1, words2, words3, words4};
    int wordsSize = sizeof(words) / sizeof(words[0]);

    uniqueMorseRepresentations(words, wordsSize);
    return 0;
}