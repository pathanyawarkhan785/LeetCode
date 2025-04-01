#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *removeNthFromEnd(struct ListNode *head, int n)
{
    struct ListNode *dummy = (struct ListNode *)malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode *slow = dummy;
    struct ListNode *fast = dummy;

    for (int i = 0; i <= n; i++)
    {
        fast = fast->next;
    }

    while (fast != NULL)
    {
        slow = slow->next;
        fast = fast->next;
    }

    struct ListNode *temp = slow->next;
    slow->next = slow->next->next;
    free(temp);

    struct ListNode *newHead = dummy->next;
    free(dummy);

    return newHead;
}

struct ListNode *printList(struct ListNode *head)
{
    while (head != NULL)
    {
        printf("%d --> ", head->val);
        head = head->next;
    }
};

int main()
{
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *second = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *third = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *fourth = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *fifth = (struct ListNode *)malloc(sizeof(struct ListNode));

    head->val = 5;
    head->next = second;

    second->val = 10;
    second->next = third;
    // second->next = NULL;

    third->val = 15;
    third->next = fourth;

    fourth->val = 20;
    fourth->next = fifth;

    fifth->val = 25;
    fifth->next = NULL;

    removeNthFromEnd(head, 2);
    printList(head);

    return 0;
}

// 5 -> 10 -> 15 -> 20 -> 25