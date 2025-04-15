#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

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

struct ListNode *modifiedList(int *nums, int numsSize, struct ListNode *head)
{
    bool hashSet[100001] = {false};
    for (int i = 0; i < numsSize; i++)
        hashSet[nums[i]] = true;

    struct ListNode *dummy = (struct ListNode *)malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode *prev = dummy;
    struct ListNode *curr = head;

    while (curr != NULL)
    {
        if (hashSet[curr->val])
        {
            prev->next = curr->next;
            free(curr);
            curr = prev->next;
        }
        else
        {
            prev = curr;
            curr = curr->next;
        }
    }

    struct ListNode *newHead = dummy->next;
    free(dummy);
    return newHead;
}

int main()
{
    int nums[] = {1, 2, 3};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

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
    fourth->next = fifth;

    fifth->val = 5;
    fifth->next = NULL;

    struct ListNode *newHead = modifiedList(nums, numsSize, head);
    printList(newHead);

    return 0;
}