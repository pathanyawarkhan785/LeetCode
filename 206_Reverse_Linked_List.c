#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int data;
    struct ListNode *next;
};

struct ListNode *reverseList(struct ListNode *head)
{
    struct ListNode *current = *head;
    struct ListNode *prev = NULL;
    struct ListNode *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev; // Update the head to the new first node
}

// Helper function to print the linked list
void printList(struct ListNode *head)
{
    while (head != NULL)
    {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

int main()
{
    struct ListNode *head = NULL;
    // Create a sample linked list: 20 -> 4 -> 15 -> 85
    // You can modify this part as needed
    // ...

    printf("Original linked list: ");
    printList(head);

    reverse(&head);

    printf("Reversed linked list: ");
    printList(head);

    return 0;
}
