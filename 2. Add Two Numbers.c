/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    struct ListNode *answer;
    struct ListNode *last;
    int sum = 0, useless;
    answer = (struct ListNode *)malloc(sizeof(struct ListNode));
    if (l1 == NULL)
    {
        if (l2 != NULL) // Only l2 contains value
        {
            answer->val = l2->val % 10;
            if (l2->next == NULL)
            {
                if (l2->val >= 10)
                {
                    last = (struct ListNode *)malloc(sizeof(struct ListNode));
                    last->val = 1;
                    last->next = NULL;
                    answer->next = last;
                    last = NULL;
                }
                else
                {
                    answer->next = NULL;
                }
            }
            else
            {
                l2->next->val = (l2->val >= 10) ? ++l2->next->val : l2->next->val;
                answer->next = addTwoNumbers(NULL, l2->next);
            }
        }
    }
    else
    {
        if (l2 == NULL)
        {
            answer->val = l1->val % 10;
            if (l1->next == NULL)
            {
                if (l1->val >= 10)
                {
                    last = (struct ListNode *)malloc(sizeof(struct ListNode));
                    last->val = 1;
                    last->next = NULL;
                    answer->next = last;
                    last = NULL;
                }
                else
                {
                    answer->next = NULL;
                }
            }
            else
            {
                l1->next->val = (l1->val >= 10) ? ++l1->next->val : l1->next->val;
                answer->next = addTwoNumbers(l1->next, NULL);
            }
        }
        else // Both contains values
        {
            if (l1->next == NULL)
            {
                if (l2->next == NULL)
                {
                    sum = l1->val + l2->val;
                    answer->val = sum % 10;
                    if (sum >= 10)
                    {
                        last = (struct ListNode *)malloc(sizeof(struct ListNode));
                        last->val = 1;
                        last->next = NULL;
                        answer->next = last;
                        last = NULL;
                    }
                    else
                    {
                        answer->next = NULL;
                    }
                }
                else
                {
                    sum = l1->val + l2->val;
                    answer->val = sum % 10;
                    l2->next->val = (sum >= 10) ? ++l2->next->val : l2->next->val;
                    answer->next = addTwoNumbers(NULL, l2->next);
                }
            }
            else
            {
                if (l2->next == NULL)
                {
                    sum = l1->val + l2->val;
                    answer->val = sum % 10;
                    l1->next->val = (sum >= 10) ? ++l1->next->val : l1->next->val;
                    answer->next = addTwoNumbers(l1->next, NULL);
                }
                else
                {
                    sum = l1->val + l2->val;
                    answer->val = sum % 10;
                    l1->next->val = (sum >= 10) ? ++l1->next->val : l1->next->val;
                    answer->next = addTwoNumbers(l1->next, l2->next);
                }
            }
        }
    }
    return answer;
}