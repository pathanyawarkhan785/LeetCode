#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

struct ListNode *insertGreatestCommonDivisors(struct ListNode *head)
{
    struct ListNode *current = head;

    while (current != NULL && current->next != NULL)
    {
        int val = gcd(current->val, current->next->val);

        struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
        temp->val = val;
        temp->next = current->next;

        current->next = temp;

        current = temp->next;
    }
    return head;
}

void printList(struct ListNode *head)
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

    head->val = 18;
    head->next = second;

    second->val = 6;
    second->next = third;

    third->val = 10;
    third->next = fourth;

    fourth->val = 3;
    fourth->next = NULL;

    insertGreatestCommonDivisors(head);
    printList(head);

    return 0;
}