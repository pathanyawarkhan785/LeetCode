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

struct ListNode *mergeTwoLists(struct ListNode *list1, struct ListNode *list2)
{
    struct ListNode dummy;
    struct ListNode *current = &dummy;
    dummy.next = NULL;

    while (list1 != NULL && list2 != NULL)
    {
        if (list1->val < list2->val)
        {
            current->next = list1;
            list1 = list1->next;
        }
        else
        {
            current->next = list2;
            list2 = list2->next;
        }
        current = current->next;
    }

    if (list1 != NULL)
        current->next = list1;

    else
        current->next = list2;

    return dummy.next;
}

int main()
{
    struct ListNode *list1 = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *second = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *third = (struct ListNode *)malloc(sizeof(struct ListNode));

    list1->val = 1;
    list1->next = second;

    second->val = 2;
    second->next = third;

    third->val = 4;
    third->next = NULL;

    struct ListNode *list2 = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *fifth = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *sixth = (struct ListNode *)malloc(sizeof(struct ListNode));

    list2->val = 1;
    list2->next = fifth;

    fifth->val = 3;
    fifth->next = sixth;

    sixth->val = 4;
    sixth->next = NULL;

    mergeTwoLists(list1, list2);
    printList(list1);

    return 0;
}