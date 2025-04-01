#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

int getDecimalValue(struct ListNode *head)
{
    int binNum = 0;

    while (head != NULL)
    {
        binNum = binNum << 1 | head->val;
        head = head->next;
    }

    return binNum;
}

int main()
{
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *second = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *third = (struct ListNode *)malloc(sizeof(struct ListNode));

    head->val = 1;
    head->next = second;

    second->val = 0;
    second->next = third;

    third->val = 0;
    third->next = NULL;

    int res = getDecimalValue(head);
    printf("%d", res);

    return 0;
}
