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
        printf("%d ", head->val);
        head = head->next;
    }
}

void swapVal(struct ListNode *temp1, struct ListNode *temp2)
{
    int temp;

    temp = temp2->val;
    temp2->val = temp1->val;
    temp1->val = temp;
}

struct ListNode *swapPairs(struct ListNode *head)
{

    if (head == NULL || head->next == NULL)
        return head;

    struct ListNode *slow = head;
    struct ListNode *fast;

    while (slow != NULL && slow->next != NULL)
    {
        fast = slow->next;

        swapVal(slow, fast);

        slow = slow->next->next;
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

    head->val = 1;
    head->next = second;

    second->val = 2;
    second->next = third;

    third->val = 3;
    third->next = fourth;

    fourth->val = 4;
    fourth->next = NULL;

    head = swapPairs(head);
    printList(head);

    free(head);
    free(second);
    free(third);
    free(fourth);

    return 0;
}