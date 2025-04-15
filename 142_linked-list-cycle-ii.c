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

struct ListNode *detectCycle(struct ListNode *head)
{
    struct ListNode *slow = head;
    struct ListNode *fast = head;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
        {
            struct ListNode *start = head;
            while (start != slow)
            {
                start = start->next;
                slow = slow->next;
            }
            return start;
        }
    }
    return NULL;
}

int main()
{
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *second = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *third = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *fourth = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *fifth = (struct ListNode *)malloc(sizeof(struct ListNode));

    head->val = 3;
    head->next = second;

    second->val = 2;
    second->next = third;

    third->val = 0;
    third->next = fourth;

    fourth->val = -4;
    fourth->next = second;

    struct ListNode *res = detectCycle(head);
    printf("%d", res->val);

    return 0;
}
