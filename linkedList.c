#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *printList(struct ListNode *head); // first function declare
struct ListNode *deleteMiddle(struct ListNode *head);
struct ListNode *middleNode(struct ListNode *head);
struct ListNode *reverseList(struct ListNode *head);
struct ListNode *deleteMiddle(struct ListNode *head);
struct ListNode *oddEvenList(struct ListNode *head);

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

    third->val = 15;
    third->next = fourth;

    fourth->val = 20;
    fourth->next = fifth;
    // fourth->next = NULL;

    fifth->val = 25;
    fifth->next = NULL;

    // printList(head); // second function call
    // deleteMiddle(head);
    // printf("%d", middleNode(head));
    // reverseList(head);

    return 0;
}

struct ListNode *printList(struct ListNode *head)
{
    while (head != NULL)
    {
        printf("%d --> ", head->val);
        head = head->next;
    }
};

struct ListNode *deleteMiddle(struct ListNode *head)

{
    int count = 0;
    while (head != NULL)
    {
        printf("%d --> ", head->val);
        head = head->next;
        count++;
    }
    // printf("\n%d", count);
    // printf("\n%f", ceil(count / 2.0));

    count = ceil(count / 2.0);
    int temp = 0;

    while (temp != count)
    {
        temp++;
    }
};

struct ListNode *middleNode(struct ListNode *head)
{
    struct ListNode *slow = head;
    struct ListNode *fast = head;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    };
    return (void *)(slow->val);
}

struct ListNode *reverseList(struct ListNode *head)
{
    struct ListNode *next, *prev = NULL;
    while (head)
    {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
};

struct ListNode *deleteMiddle(struct ListNode *head)
{
    if (!head || !head->next)
    {
        return NULL;
    }

    struct ListNode *slow = head, *fast = head, *prev = NULL;

    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    prev->next = slow->next;
    free(slow);

    return head;
}

struct ListNode *oddEvenList(struct ListNode *head)
{
    if (!head)
        return head;

    struct ListNode *odd = head;
    struct ListNode *even = head->next;
    struct ListNode *evenHead = even;

    while (even && even->next)
    {
        odd->next = even->next;
        odd = odd->next;
        even->next = odd->next;
        even = even->next;
    }
    odd->next = evenHead;
    return head;
}

int maxTwinSum(struct ListNode *head)
{
    if (!head || !head->next)
        return 0;

    struct ListNode *slow = head, *fast = head;
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    struct ListNode *secondHalf = reverseList(slow);

    int maxSum = 0;
    struct ListNode *firstHalf = head;
    while (secondHalf)
    {
        int twinSum = firstHalf->val + secondHalf->val;
        if (twinSum > maxSum)
        {
            maxSum = twinSum;
        }
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }
    return maxSum;
}

int pairSum(struct ListNode *head)
{
    if (!head)
        return 0;

    struct ListNode *slow = head, *fast = head;
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    struct ListNode *prev = NULL;
    struct ListNode *curr = slow;
    struct ListNode *next = NULL;
    while (curr)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    struct ListNode *secondHalf = prev;

    int maxSum = 0;
    struct ListNode *firstHalf = head;
    while (secondHalf)
    {
        int twinSum = firstHalf->val + secondHalf->val;
        if (twinSum > maxSum)
        {
            maxSum = twinSum;
        }
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }
    return maxSum;
}