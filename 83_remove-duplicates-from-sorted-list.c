#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

void printList(struct ListNode *head)
{
    while (head != NULL)
    {
        printf("%d->", head->val);
        head = head->next;
    }
}

struct ListNode *deleteDuplicates(struct ListNode *head)
{
    struct ListNode *curr = head;

    while (curr != NULL && curr->next != NULL)
    {
        if (curr->val == curr->next->val)
        {
            struct ListNode *temp = curr->next;
            curr->next = curr->next->next;
            free(temp);
        }
        else
            curr = curr->next;
    }
    return head;
}

int main()
{
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *second = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *third = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *fourth = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *fifth = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *sixth = (struct ListNode *)malloc(sizeof(struct ListNode));

    head->val = 1;
    head->next = second;

    second->val = 1;
    second->next = third;

    third->val = 2;
    third->next = fourth;

    fourth->val = 3;
    fourth->next = fifth;

    fifth->val = 3;
    fifth->next = NULL;

    deleteDuplicates(head);
    printList(head);

    return 0;
}