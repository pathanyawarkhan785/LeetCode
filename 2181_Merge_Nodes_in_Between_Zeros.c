#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *mergeNodes(struct ListNode *head)
{

    if (!head->next)
        return NULL;

    struct ListNode *ptr = head->next;

    int sum = 0;
    while (ptr->val != 0)
        sum += ptr->val, ptr = ptr->next;

    head->next->val = sum;
    head->next->next = mergeNodes(ptr);

    return head->next;
}

int main()
{
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *second = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *third = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *fourth = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *fifth = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *sixth = (struct ListNode *)malloc(sizeof(struct ListNode));

    head->val = 0;
    head->next = second;

    second->val = 3;
    second->next = third;

    third->val = 1;
    third->next = fourth;

    fourth->val = 0;
    fourth->next = fifth;

    fifth->val = 4;
    fifth->next = sixth;

    sixth->val = 0;
    sixth->next = NULL;

    mergeNodes(head);

    return 0;
}