#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{
    struct ListNode *ptrA = headA;
    struct ListNode *ptrB = headB;

    while (ptrA != ptrB)
    {
        ptrA = ptrA ? ptrA->next : headB;
        ptrB = ptrB ? ptrB->next : headA;
    }

    return ptrA;
}

int main()
{
    struct ListNode *headA = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *secondA = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *thirdA = (struct ListNode *)malloc(sizeof(struct ListNode));

    struct ListNode *headB = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *secondB = (struct ListNode *)malloc(sizeof(struct ListNode));

    struct ListNode *intersection = (struct ListNode *)malloc(sizeof(struct ListNode));

    headA->val = 4;
    headA->next = secondA;
    secondA->val = 1;
    secondA->next = intersection;
    intersection->val = 8;
    intersection->next = thirdA;
    thirdA->val = 4;
    thirdA->next = NULL;

    headB->val = 5;
    headB->next = secondB;
    secondB->val = 6;
    secondB->next = intersection;

    struct ListNode *res = getIntersectionNode(headA, headB);

    res ? printf("%d\n", res->val) : printf("No intersection found.\n");

    free(headA);
    free(secondA);
    free(thirdA);
    free(headB);
    free(secondB);
    free(intersection);

    return 0;
}